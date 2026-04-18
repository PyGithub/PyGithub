"""
Async test framework - wraps the sync Framework for async tests.

Uses a SyncProxy approach: the async Github object and all objects returned
from it are wrapped in a proxy that automatically runs coroutines synchronously.
This allows test method bodies to remain identical to sync tests.
"""

from __future__ import annotations

import asyncio

import github.asyncio.GithubObject
import github.asyncio.Requester
import github.GithubObject
import github.Requester
from github.asyncio.MainClass import Github
from github.GithubException import IncompletableObject
from tests import Framework

# Re-export BasicTestCase so that async test files referencing
# Framework.BasicTestCase find it here.
BasicTestCase = Framework.BasicTestCase


def _is_completable(obj):
    """
    Check if an object is a CompletableGithubObject that may need completion.
    """
    try:
        return isinstance(obj, github.asyncio.GithubObject.CompletableGithubObject)
    except Exception:
        return False


class AsyncReplayingConnection(Framework.ReplayingConnection):
    """
    Async-aware replaying connection.

    Inherits the replay file logic from ReplayingConnection. Overrides getresponse() and close() to be async, since the
    async Requester awaits these methods.

    """

    async def getresponse(self):
        # The real connection's getresponse is async
        response = await self._ReplayingConnection__cnx.getresponse()
        # Restore original headers to the response
        response.headers = self.response_headers
        return response

    async def close(self):
        await self._ReplayingConnection__cnx.close()


class AsyncReplayingHttpConnection(AsyncReplayingConnection):
    _realConnection = github.asyncio.Requester.HTTPRequestsConnectionClass

    def __init__(self, *args, **kwds):
        super().__init__("http", *args, **kwds)


class AsyncReplayingHttpsConnection(AsyncReplayingConnection):
    _realConnection = github.asyncio.Requester.HTTPSRequestsConnectionClass

    def __init__(self, *args, **kwds):
        super().__init__("https", *args, **kwds)


class SyncProxy:
    """
    Proxy that wraps an async object and makes its async methods callable synchronously.

    When an async method is called, it is automatically run to completion in an event loop. Objects returned from async
    calls are recursively wrapped in SyncProxy. Supports sync iteration over objects that implement __aiter__/__anext__.

    """

    # Types that should NOT be wrapped (they are plain values)
    _PASSTHROUGH = (str, int, float, bool, bytes, type(None))
    # Cache: id(obj) -> SyncProxy, so the same underlying object always
    # returns the same wrapper (preserves `is` identity checks).
    _cache: dict[int, SyncProxy] = {}

    def __init__(self, obj, loop=None):
        object.__setattr__(self, "_obj", obj)
        object.__setattr__(self, "_loop", loop or asyncio.new_event_loop())
        # Register in cache
        SyncProxy._cache[id(obj)] = self

    @staticmethod
    def _deep_unwrap(obj):
        """
        Recursively unwrap SyncProxy objects inside containers.

        This is needed because async methods may iterate over list/tuple/dict arguments and access async properties on
        the elements. If the elements are still SyncProxy-wrapped, accessing an async property triggers
        SyncProxy.__getattr__ -> run_until_complete, which fails with 'RuntimeError: This event loop is already running'
        since the outer async call is already running on the same loop.

        """
        if isinstance(obj, SyncProxy):
            return object.__getattribute__(obj, "_obj")
        if isinstance(obj, list):
            return [SyncProxy._deep_unwrap(item) for item in obj]
        if isinstance(obj, tuple):
            if hasattr(type(obj), "_fields"):
                # NamedTuple
                return type(obj)(*[SyncProxy._deep_unwrap(item) for item in obj])
            return tuple(SyncProxy._deep_unwrap(item) for item in obj)
        if isinstance(obj, dict):
            return {k: SyncProxy._deep_unwrap(v) for k, v in obj.items()}
        if isinstance(obj, set):
            return {SyncProxy._deep_unwrap(item) for item in obj}
        return obj

    @classmethod
    def _wrap(cls, result, loop):
        """
        Wrap a result if it's a complex object, pass through primitives.
        """
        if isinstance(result, cls._PASSTHROUGH):
            return result
        # Don't wrap _NotSetType instances (NotSet sentinel).
        # Tests call is_undefined(obj._attr) which needs the raw _NotSetType,
        # not a SyncProxy wrapper.
        if isinstance(
            result,
            (
                github.GithubObject._NotSetType,
                github.asyncio.GithubObject._NotSetType,
            ),
        ):
            return result
        # Also pass through _ValuedAttribute and _BadAttribute instances
        # which are internal attribute wrappers, not user-facing objects.
        if isinstance(
            result,
            (
                github.GithubObject._ValuedAttribute,
                github.asyncio.GithubObject._ValuedAttribute,
                github.GithubObject._BadAttribute,
                github.asyncio.GithubObject._BadAttribute,
            ),
        ):
            return result
        if isinstance(result, dict):
            return {k: cls._wrap(v, loop) for k, v in result.items()}
        if isinstance(result, (list, tuple)):
            wrapped = [cls._wrap(item, loop) for item in result]
            # NamedTuples require positional args, not a single list
            if hasattr(type(result), "_fields"):
                return type(result)(*wrapped)
            return type(result)(wrapped)
        if isinstance(result, set):
            return {cls._wrap(item, loop) for item in result}
        # Return cached wrapper if we've already wrapped this exact object
        # (preserves `is` identity checks across multiple attribute accesses).
        cached = cls._cache.get(id(result))
        if cached is not None and object.__getattribute__(cached, "_obj") is result:
            return cached
        # Auto-complete CompletableGithubObjects created with _needs_async_completion.
        # This handles the case where sync __init__ would call self.complete()
        # immediately (requester.is_not_lazy, completed=None, no response).
        # The async __init__ stores a flag instead; we check and run it here.
        # NOTE: We do NOT complete objects with completed=False here (lazy objects).
        # Those are completed lazily on first attribute access in __getattr__,
        # matching the sync behavior where _completeIfNotSet triggers on property access.
        if _is_completable(result) and getattr(result, "_needs_async_completion", False):
            try:
                coro = result.complete()
                if asyncio.iscoroutine(coro):
                    loop.run_until_complete(coro)
            except IncompletableObject:
                pass  # May fail for objects without URLs, that's OK
        return cls(result, loop)

    def _ensure_completed(self):
        """
        Lazily complete the underlying object if it's a CompletableGithubObject that hasn't been completed yet.

        This mirrors the sync code's _completeIfNotSet() which triggers completion on property access.

        """
        obj = object.__getattribute__(self, "_obj")
        loop = object.__getattribute__(self, "_loop")
        if _is_completable(obj) and not obj.completed:
            try:
                coro = obj.complete()
                if asyncio.iscoroutine(coro):
                    loop.run_until_complete(coro)
            except IncompletableObject:
                pass

    def __getattr__(self, name):
        obj = object.__getattribute__(self, "_obj")
        loop = object.__getattribute__(self, "_loop")

        # Properties that call _completeIfNotSet are now async def,
        # so they return coroutines. We handle that below.

        attr = getattr(obj, name)

        # If attr is a class/type, return it directly without wrapping
        # in a function wrapper. This preserves identity across multiple
        # accesses (e.g., obj.__contentClass == obj.__contentClass).
        if isinstance(attr, type):
            return attr

        if callable(attr):
            if asyncio.iscoroutinefunction(attr):

                def async_wrapper(*args, **kwargs):
                    # Deep-unwrap any SyncProxy arguments (including inside containers)
                    args = tuple(SyncProxy._deep_unwrap(a) for a in args)
                    kwargs = {k: SyncProxy._deep_unwrap(v) for k, v in kwargs.items()}
                    result = loop.run_until_complete(attr(*args, **kwargs))
                    return SyncProxy._wrap(result, loop)

                return async_wrapper
            else:

                def sync_wrapper(*args, **kwargs):
                    args = tuple(SyncProxy._deep_unwrap(a) for a in args)
                    kwargs = {k: SyncProxy._deep_unwrap(v) for k, v in kwargs.items()}
                    result = attr(*args, **kwargs)
                    if asyncio.iscoroutine(result):
                        result = loop.run_until_complete(result)
                    return SyncProxy._wrap(result, loop)

                return sync_wrapper

        # Handle coroutines from async properties (property getter returns coroutine)
        if asyncio.iscoroutine(attr):
            attr = loop.run_until_complete(attr)
        return SyncProxy._wrap(attr, loop)

    def __setattr__(self, name, value):
        if isinstance(value, SyncProxy):
            value = object.__getattribute__(value, "_obj")
        setattr(object.__getattribute__(self, "_obj"), name, value)

    @property  # type: ignore[misc]
    def __class__(self):
        return type(object.__getattribute__(self, "_obj"))

    def __repr__(self):
        return repr(object.__getattribute__(self, "_obj"))

    def __str__(self):
        return str(object.__getattribute__(self, "_obj"))

    def __eq__(self, other):
        if isinstance(other, SyncProxy):
            other = object.__getattribute__(other, "_obj")
        return object.__getattribute__(self, "_obj") == other

    def __ne__(self, other):
        if isinstance(other, SyncProxy):
            other = object.__getattribute__(other, "_obj")
        return object.__getattribute__(self, "_obj") != other

    def __hash__(self):
        return hash(object.__getattribute__(self, "_obj"))

    def __bool__(self):
        return bool(object.__getattribute__(self, "_obj"))

    def __len__(self):
        obj = object.__getattribute__(self, "_obj")
        if hasattr(obj, "__len__"):
            return len(obj)
        raise TypeError(f"object of type '{type(obj).__name__}' has no len()")

    def __iter__(self):
        obj = object.__getattribute__(self, "_obj")
        loop = object.__getattribute__(self, "_loop")

        if hasattr(obj, "__aiter__"):
            # Async iterable - use async iteration
            aiter = obj.__aiter__()
            while True:
                try:
                    item = loop.run_until_complete(aiter.__anext__())
                    yield SyncProxy._wrap(item, loop)
                except StopAsyncIteration:
                    return
        elif hasattr(obj, "__iter__"):
            for item in obj:
                yield SyncProxy._wrap(item, loop)
        else:
            raise TypeError(f"'{type(obj).__name__}' object is not iterable")

    def __getitem__(self, index):
        obj = object.__getattribute__(self, "_obj")
        loop = object.__getattribute__(self, "_loop")
        # Use the async getitem() method if available (PaginatedListBase)
        # so that pages are fetched on demand.  Fall back to sync
        # __getitem__ for non-PaginatedList objects.
        if hasattr(obj, "getitem"):
            result = loop.run_until_complete(obj.getitem(index))
        else:
            result = obj.__getitem__(index)
            if asyncio.iscoroutine(result):
                result = loop.run_until_complete(result)
        return SyncProxy._wrap(result, loop)

    def __reversed__(self):
        obj = object.__getattribute__(self, "_obj")
        loop = object.__getattribute__(self, "_loop")
        # For PaginatedList, .reversed returns a new PaginatedList.
        # Use try/except instead of hasattr() to avoid triggering the
        # property getter twice (hasattr calls getattr internally).
        try:
            rev = obj.reversed
            if asyncio.iscoroutine(rev):
                rev = loop.run_until_complete(rev)
            return iter(SyncProxy._wrap(rev, loop))
        except AttributeError:
            pass
        # Fallback: try __reversed__
        try:
            return iter([SyncProxy._wrap(item, loop) for item in obj.__reversed__()])
        except AttributeError:
            raise TypeError(f"'{type(obj).__name__}' object is not reversible")

    def __contains__(self, item):
        obj = object.__getattribute__(self, "_obj")
        if isinstance(item, SyncProxy):
            item = object.__getattribute__(item, "_obj")
        return item in obj

    def __enter__(self):
        obj = object.__getattribute__(self, "_obj")
        loop = object.__getattribute__(self, "_loop")
        if hasattr(obj, "__aenter__"):
            result = loop.run_until_complete(obj.__aenter__())
            return SyncProxy._wrap(result, loop)
        return SyncProxy._wrap(obj.__enter__(), loop)

    def __exit__(self, *args):
        obj = object.__getattribute__(self, "_obj")
        loop = object.__getattribute__(self, "_loop")
        if hasattr(obj, "__aexit__"):
            return loop.run_until_complete(obj.__aexit__(*args))
        return obj.__exit__(*args)

    def __isinstance_check__(self):
        """
        Return the wrapped object for isinstance checks.
        """
        return object.__getattribute__(self, "_obj")


class TestCase(Framework.BasicTestCase):
    """
    Async version of Framework.TestCase.

    Creates an async Github instance wrapped in SyncProxy, so test methods can call async methods synchronously.

    """

    @staticmethod
    def _unwrap(obj):
        """
        Unwrap a SyncProxy to get the underlying object.
        """
        if isinstance(obj, SyncProxy):
            return object.__getattribute__(obj, "_obj")
        return obj

    @staticmethod
    def _resolve_async_class(cls):
        """
        Try to find the async equivalent of a sync class.

        For example, github.Repository.Repository -> github.asyncio.Repository.Repository

        """
        mod = getattr(cls, "__module__", "") or ""
        if mod.startswith("github.") and not mod.startswith("github.asyncio."):
            async_mod_name = mod.replace("github.", "github.asyncio.", 1)
            try:
                import importlib

                async_mod = importlib.import_module(async_mod_name)
                return getattr(async_mod, cls.__name__, cls)
            except (ImportError, AttributeError):
                pass
        return cls

    def assertIsInstance(self, obj, cls, msg=None):
        """
        Override to unwrap SyncProxy and also check async class hierarchy.
        """
        unwrapped = self._unwrap(obj)
        if isinstance(unwrapped, cls):
            return
        # Try async version of the class
        async_cls = self._resolve_async_class(cls)
        if async_cls is not cls and isinstance(unwrapped, async_cls):
            return
        # Fall through to standard assertion for proper error message
        super().assertIsInstance(unwrapped, cls, msg)

    def assertNotIsInstance(self, obj, cls, msg=None):
        """
        Override to unwrap SyncProxy and also check async class hierarchy.
        """
        unwrapped = self._unwrap(obj)
        async_cls = self._resolve_async_class(cls)
        # Must not be instance of EITHER sync or async class
        if isinstance(unwrapped, async_cls) and async_cls is not cls:
            self.fail(msg or f"{unwrapped!r} is an instance of async {async_cls!r}")
        super().assertNotIsInstance(unwrapped, cls, msg)

    def doCheckFrame(self, obj, frame):
        if obj._headers == {} and frame is None:
            return
        if obj._headers is None and frame == {}:
            return
        self.assertEqual(obj._headers, frame[2])

    def getFrameChecker(self):
        return lambda requester, obj, frame: self.doCheckFrame(obj, frame)

    def setUp(self):
        super().setUp()

        # Set up frame debugging on BOTH sync and async classes.
        # The async GithubObject/Requester are separate class hierarchies,
        # so we must set flags on both.
        github.GithubObject.GithubObject.setCheckAfterInitFlag(True)
        github.Requester.Requester.setDebugFlag(True)
        github.Requester.Requester.setOnCheckMe(self.getFrameChecker())
        github.asyncio.GithubObject.GithubObject.setCheckAfterInitFlag(True)
        github.asyncio.Requester.Requester.setDebugFlag(True)
        github.asyncio.Requester.Requester.setOnCheckMe(self.getFrameChecker())

        # super().setUp() calls setOpenFile on the SYNC ReplayingHttp(s)Connection
        # classes. Due to Python's name mangling of __openFile, the async subclasses
        # (AsyncReplayingHttp(s)Connection) don't inherit that class-level attribute.
        # We must explicitly propagate it to the async connection classes.
        AsyncReplayingHttpConnection.setOpenFile(Framework.ReplayingHttpConnection._Connection__openFile)
        AsyncReplayingHttpsConnection.setOpenFile(Framework.ReplayingHttpsConnection._Connection__openFile)

        # Inject async replaying connection classes into the async Requester
        github.asyncio.Requester.Requester.injectConnectionClasses(
            AsyncReplayingHttpConnection,
            AsyncReplayingHttpsConnection,
        )

        self.g = self.get_github(self.authMode, self.retry, self.pool_size)

    def tearDown(self):
        super().tearDown()
        github.asyncio.Requester.Requester.resetConnectionClasses()

    def get_github(self, authMode, retry=None, pool_size=None):
        if authMode == "token":
            auth = self.oauth_token
        elif authMode == "jwt":
            auth = self.jwt
        elif authMode == "app":
            auth = self.app_auth
        elif self.authMode == "none":
            auth = None
        else:
            raise ValueError(f"Unsupported test auth mode: {authMode}")

        g = Github(
            auth=auth,
            per_page=self.per_page,
            retry=retry,
            pool_size=pool_size,
            seconds_between_requests=self.seconds_between_requests,
            seconds_between_writes=self.seconds_between_writes,
        )
        return SyncProxy(g)
