"""
Async test framework.

Self-contained: needs neither the classic checkout's tests/Framework.py (this replaces it -- see
TEMPLATE_TEST_FILES) or its tests/ReplayData (scripts/sync_async.sh copies that in directly), nor
the classic PyGithub package. Copied byte-for-byte into tests/AsyncFramework.py by
scripts/generate_async.py -- edit this file, not the generated one.

This module provides:

- Cassette replay (BasicTestCase and friends): built on niquests directly. vcrpy only patches
  *synchronous* HTTP transports, so it can't see niquests's AsyncSession either way; the async
  connection classes bridge each request through a real sync CassetteConnection instead.
- Sync-to-async bridging (SyncProxy, TestCase): a proxy that wraps the async Github object (and
  everything it returns) so generated test method bodies -- copied verbatim from the classic
  project's sync test files -- can call async methods without themselves being async.

"""

from __future__ import annotations

import asyncio
import contextlib
import functools
import os
import traceback
import unittest
import warnings
from collections.abc import Generator
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlsplit

import vcr
import vcr.cassette
from niquests import Session
from vcr.matchers import requests_match

import githubasyncio.Auth
import githubasyncio.GithubObject
import githubasyncio.Requester
from githubasyncio import Consts
from githubasyncio.GithubException import IncompletableObject
from githubasyncio.MainClass import Github
from githubasyncio.Requester import RequestsResponse
from githubasyncio.requestlib import CaseInsensitiveDict, adapters
from tests import VcrSerializer

APP_PRIVATE_KEY = """
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC+5ePolLv6VcWLp2f17g6r6vHl+eoLuodOOfUl8JK+MVmvXbPa
xDy0SS0pQhwTOMtB0VdSt++elklDCadeokhEoGDQp411o+kiOhzLxfakp/kewf4U
HJnu4M/A2nHmxXVe2lzYnZvZHX5BM4SJo5PGdr0Ue2JtSXoAtYr6qE9maQIDAQAB
AoGAFhOJ7sy8jG+837Clcihso+8QuHLVYTPaD+7d7dxLbBlS8NfaQ9Nr3cGUqm/N
xV9NCjiGa7d/y4w/vrPwGh6UUsA+CvndwDgBd0S3WgIdWvAvHM8wKgNh/GBLLzhT
Bg9BouRUzcT1MjAnkGkWqqCAgN7WrCSUMLt57TNleNWfX90CQQDjvVKTT3pOiavD
3YcLxwkyeGd0VMvKiS4nV0XXJ97cGXs2GpOGXldstDTnF5AnB6PbukdFLHpsx4sW
Hft3LRWnAkEA1pY15ke08wX6DZVXy7zuQ2izTrWSGySn7B41pn55dlKpttjHeutA
3BEQKTFvMhBCphr8qST7Wf1SR9FgO0tFbwJAEhHji2yy96hUyKW7IWQZhrem/cP8
p4Va9CQolnnDZRNgg1p4eiDiLu3dhLiJ547joXuWTBbLX/Y1Qvv+B+a74QJBAMCW
O3WbMZlS6eK6//rIa4ZwN00SxDg8I8FUM45jwBsjgVGrKQz2ilV3sutlhIiH82kk
m1Iq8LMJGYl/LkDJA10CQBV1C+Xu3ukknr7C4A/4lDCa6Xb27cr1HanY7i89A+Ab
eatdM6f/XVqWp8uPT9RggUV9TjppJobYGT2WrWJMkYw=
-----END RSA PRIVATE KEY-----
"""


@dataclass
class Request:
    protocol: str
    verb: str
    host: str
    port: int | None
    url: str
    request_headers: dict[str, Any]
    input: Any

    def with_response(self, status: int, response_headers: dict[str, Any], output: bytes) -> RequestResponse:
        return RequestResponse(
            self.protocol,
            self.verb,
            self.host,
            self.port,
            self.url,
            self.request_headers,
            self.input,
            status,
            response_headers,
            output,
        )


@dataclass
class RequestResponse(Request):
    protocol: str
    verb: str
    host: str
    port: int | None
    url: str
    request_headers: dict[str, Any]
    input: Any
    status: int
    response_headers: dict[str, Any]
    output: bytes


class OrderedCassette(vcr.cassette.Cassette):
    """
    Same as vcrpy's ``Cassette``, but only ever considers the next not-yet-played interaction as a candidate match,
    instead of searching the whole cassette for any not-yet-played interaction that matches.

    vcrpy's default behavior replays same-shaped requests in recording order (since
    it always returns the earliest unplayed match), but happily serves requests out of order
    relative to *other*, differently-shaped requests -- e.g. cassette [A, B, C] replays fine as
    [B, A, C] as long as each of A, B, C individually matches something unplayed. That would let a
    refactor that accidentally reorders API calls pass silently. Requiring an exact match against
    the next interaction turns that into a hard ``CannotOverwriteExistingCassetteException``.

    """

    def _responses(self, request):
        request = self._before_record_request(request)
        for index, (stored_request, response) in enumerate(self.data):
            if self.play_counts[index] == 0:
                if requests_match(request, stored_request, self._match_on):
                    yield index, response
                return


class OrderedVCR(vcr.VCR):
    def _use_cassette(self, with_current_defaults=False, **kwargs):
        if with_current_defaults:
            config = self.get_merged_config(**kwargs)
            return OrderedCassette.use(**config)
        args_getter = functools.partial(self.get_merged_config, **kwargs)
        return OrderedCassette.use_arg_getter(args_getter)


# A single VCR instance, shared across all tests: it patches http.client/urllib3 generically
# enough that it transparently intercepts niquests traffic (see
# https://niquests.readthedocs.io/en/latest/community/extensions.html), unlike "responses", which
# required fooling it into believing niquests IS requests via sys.modules aliasing.
# OrderedVCR additionally enforces that requests are replayed in exactly the order they were
# recorded (see OrderedCassette above).
_vcr = OrderedVCR(serializer="pygithub-replaydata", record_mode="none")
_vcr.register_serializer("pygithub-replaydata", VcrSerializer)
_vcr.register_persister(VcrSerializer.Utf8FilesystemPersister)


class CassetteConnection:
    """
    Sync HTTP connection used only to make replay/record traffic visible to vcrpy.

    niquests's AsyncSession is invisible to vcrpy (it only patches *synchronous* HTTP transports), so cassette-backed
    tests need a genuinely synchronous connection for it to intercept -- AsyncCassetteConnection (below) bridges each
    async Requester call through an instance of this class instead. Deliberately built on niquests's plain (sync)
    Session directly, mimicking the shape of githubasyncio.Requester's own connection classes closely enough for
    RequestsResponse to work unmodified, but without depending on githubasyncio.Requester itself -- that one always
    awaits, which a sync connection can't do.

    """

    _protocol: str
    _default_port: int

    def __init__(self, host, port=None, *args, retry=None, pool_size=None, **kwds):
        BasicTestCase.ensureCassette()
        self.host = host
        self.port = port if port else self._default_port
        # honour the Requester's retry/pool_size like its real connection classes do, so Retry tests see the retries
        retry = adapters.DEFAULT_RETRIES if retry is None else retry
        pool_size = adapters.DEFAULT_POOLSIZE if pool_size is None else pool_size
        self.adapter = adapters.HTTPAdapter(
            max_retries=retry,
            pool_connections=pool_size,
            pool_maxsize=pool_size,
        )
        self.session = Session()
        self.session.mount(f"{self._protocol}://", self.adapter)

    def request(self, verb, url, input, headers, stream=False):
        self.verb = verb
        self.url = url
        self.input = input
        self.headers = headers

    def getresponse(self):
        verb = getattr(self.session, self.verb.lower())
        url = f"{self._protocol}://{self.host}:{self.port}{self.url}"
        r = verb(url, headers=self.headers, data=self.input, allow_redirects=False)
        return RequestsResponse(r)

    def close(self):
        self.session.close()


class CassetteHttpConnection(CassetteConnection):
    _protocol = "http"
    _default_port = 80


class CassetteHttpsConnection(CassetteConnection):
    _protocol = "https"
    _default_port = 443


class AsyncCassetteConnection:
    """
    Bridges an async Requester connection to a real (sync) CassetteConnection -- see its docstring for why cassette
    replay needs a sync connection at all -- exposing the result through the awaitable getresponse()/close() interface
    the async Requester expects.
    """

    _realConnection: type[CassetteConnection]

    def __init__(self, host, port, *args, **kwds):
        self._cnx = self._realConnection(host, port, *args, **kwds)

    @property
    def host(self):
        return self._cnx.host

    def request(self, verb, url, input, headers, stream=False):
        self._cnx.request(verb, url, input, headers, stream=stream)

    async def getresponse(self):
        return self._cnx.getresponse()

    async def close(self):
        self._cnx.close()


class AsyncCassetteHttpConnection(AsyncCassetteConnection):
    _realConnection = CassetteHttpConnection


class AsyncCassetteHttpsConnection(AsyncCassetteConnection):
    _realConnection = CassetteHttpsConnection


class BasicTestCase(unittest.TestCase):
    recordMode = False
    replayDataFolder = os.path.join(os.path.dirname(__file__), "ReplayData")

    # The test currently running, i.e. the one whose stack `ensureCassette()` should inspect
    # to resolve the active replay file. `CassetteConnection.__init__` cannot reach this any
    # other way, since connections are constructed directly, not looked up by instance.
    __activeInstance: BasicTestCase | None = None

    def __init__(self, methodName="runTest") -> None:
        super().__init__(methodName)
        self.authMode = "token"
        self.per_page = Consts.DEFAULT_PER_PAGE
        self.retry = None
        self.pool_size = None
        self.seconds_between_requests: float | None = None
        self.seconds_between_writes: float | None = None

    def setUp(self):
        super().setUp()
        self.__customFilename: str | None = None
        self.__cassettePath: str | None = None
        self.__cassetteCm = None
        self.__cassette = None
        self.__capturedRequests: list[RequestResponse] | None = None
        BasicTestCase.__activeInstance = self

        githubasyncio.Requester.Requester.injectConnectionClasses(
            AsyncCassetteHttpConnection,
            AsyncCassetteHttpsConnection,
        )
        if (
            self.recordMode
        ):  # pragma no cover (Branch useful only when recording new tests, not used during automated tests)
            import GithubCredentials  # type: ignore

            self.oauth_token = (
                githubasyncio.Auth.Token(GithubCredentials.oauth_token) if GithubCredentials.oauth_token else None
            )
            self.jwt = githubasyncio.Auth.AppAuthToken(GithubCredentials.jwt) if GithubCredentials.jwt else None
            self.app_auth = (
                githubasyncio.Auth.AppAuth(GithubCredentials.app_id, GithubCredentials.app_private_key)
                if GithubCredentials.app_id and GithubCredentials.app_private_key
                else None
            )
        else:
            self.oauth_token = githubasyncio.Auth.Token("oauth_token")
            self.jwt = githubasyncio.Auth.AppAuthToken("jwt")
            self.app_auth = githubasyncio.Auth.AppAuth(123456, APP_PRIVATE_KEY)

    def setPerPage(self, per_page):
        self.per_page = per_page

    def setRetry(self, retry):
        self.retry = retry

    def setPoolSize(self, pool_size):
        self.pool_size = pool_size

    def setSecondsBetweenRequests(self, seconds_between_requests):
        self.seconds_between_requests = seconds_between_requests

    def setSecondsBetweenWrites(self, seconds_between_writes):
        self.seconds_between_writes = seconds_between_writes

    @property
    def thisTestFailed(self) -> bool:
        if hasattr(self._outcome, "errors"):  # type: ignore
            # Python 3.4 - 3.10
            result = self.defaultTestResult()
            self._feedErrorsToResult(result, self._outcome.errors)  # type: ignore
            ok = all(test != self for test, text in result.errors + result.failures)
            return not ok
        else:
            # Python 3.11+
            return self._outcome.result._excinfo is not None and self._outcome.result._excinfo  # type: ignore

    def tearDown(self):
        super().tearDown()
        self.__closeCassetteIfNeeded(silent=self.thisTestFailed)
        githubasyncio.Requester.Requester.resetConnectionClasses()
        BasicTestCase.__activeInstance = None

    def assertWarning(self, warning, expected):
        self.assertWarnings(warning, expected)

    def assertWarnings(self, warning, *expecteds):
        actual = [(type(message), type(message.message), message.message.args) for message in warning.warnings]
        expected = [(warnings.WarningMessage, DeprecationWarning, (expected,)) for expected in expecteds]
        self.assertSequenceEqual(actual, expected)

    @contextlib.contextmanager
    def ignoreWarning(self, category=Warning, module=""):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=category, module=module)
            yield

    @contextlib.contextmanager
    def replayData(self, filename: str):
        previous = self.__customFilename
        self.__customFilename = filename
        try:
            yield
        finally:
            self.__customFilename = previous

    @contextlib.contextmanager
    def captureRequests(self) -> Generator[list[RequestResponse]]:
        requests: list[RequestResponse] = []
        previous = self.__capturedRequests
        self.__capturedRequests = requests
        try:
            yield requests
        finally:
            self.__capturedRequests = previous

    @classmethod
    def ensureCassette(cls) -> None:
        """
        Called once per HTTP connection (i.e. once per request, connection reuse is disabled while testing) to make
        sure the vcrpy cassette matching the currently running setUp/test/tearDown method -- or a ``replayData()``
        override -- is the active one.
        """
        self = cls.__activeInstance
        if self is not None:
            self.__ensureCassette()

    def __resolveFileName(self) -> str | None:
        if self.__customFilename:
            return self.__customFilename
        fileName = None
        for _, _, functionName, _ in traceback.extract_stack():
            if functionName.startswith("test") or functionName == "setUp" or functionName == "tearDown":
                # because in class Hook(Framework.TestCase), method testTest calls Hook.test
                if functionName != "test":
                    fileName = f"{self.__class__.__name__}.{functionName}.txt"
        return fileName

    def __ensureCassette(self) -> None:
        fileName = self.__resolveFileName()
        path = os.path.join(self.replayDataFolder, fileName) if fileName else None
        if path == self.__cassettePath:
            return
        self.__closeCassetteIfNeeded()
        self.__cassettePath = path
        if path is None:
            return
        record_mode = "all" if self.recordMode else "none"
        if self.recordMode and os.path.exists(path):
            # vcrpy's "all" record mode never plays back existing interactions, but it still
            # loads them from disk and keeps them in Cassette.data -- so without this, recording
            # over an existing replay file would append the freshly recorded interactions after
            # the stale ones instead of replacing them.
            os.remove(path)
        cassetteCm = _vcr.use_cassette(path, record_mode=record_mode)
        self.__cassette = cassetteCm.__enter__()
        self.__cassetteCm = cassetteCm
        # wired unconditionally (not just while captureRequests() is active) and exactly once per
        # cassette: __recordInteraction() itself checks __capturedRequests, so this single wiring
        # transparently reflects whatever captureRequests() call is active by the time each
        # request actually happens, without ever double-wrapping play_response/append.
        self.__wireCaptureHook(self.__cassette)

    def __closeCassetteIfNeeded(self, silent=False):
        if self.__cassetteCm is not None:
            if (
                not self.recordMode and not silent
            ):  # pragma no branch (Branch useful only when recording new tests, not used during automated tests)
                self.assertTrue(
                    self.__cassette.all_played,
                    f"Not all replay data was used in {self.__cassettePath}",
                )
            self.__cassetteCm.__exit__(None, None, None)
            self.__cassetteCm = None
            self.__cassette = None

    def __wireCaptureHook(self, cassette) -> None:
        originalPlayResponse = cassette.play_response
        originalAppend = cassette.append

        def play_response(request):
            response = originalPlayResponse(request)
            self.__recordInteraction(request, response)
            return response

        def append(request, response):
            originalAppend(request, response)
            self.__recordInteraction(request, response)

        cassette.play_response = play_response
        cassette.append = append

    def __recordInteraction(self, request, response) -> None:
        if self.__capturedRequests is None:
            return
        parts = urlsplit(request.uri)
        url = parts.path + (f"?{parts.query}" if parts.query else "")
        response_headers = CaseInsensitiveDict(
            {name: values[0] if isinstance(values, list) else values for name, values in response["headers"].items()},
        )
        self.__capturedRequests.append(
            RequestResponse(
                parts.scheme,
                request.method,
                parts.hostname,
                parts.port,
                url,
                dict(request.headers),
                request.body,
                response["status"]["code"],
                {k: v for k, v in response_headers.lower_items()},
                response["body"]["string"],
            ),
        )

    def assertListKeyEqual(self, elements, key, expectedKeys):
        realKeys = [key(element) for element in elements]
        self.assertEqual(realKeys, expectedKeys)

    def assertListKeyBegin(self, elements, key, expectedKeys):
        realKeys = [key(element) for element in elements[: len(expectedKeys)]]
        self.assertEqual(realKeys, expectedKeys)


def activateRecordMode():  # pragma no cover (Function useful only when recording new tests, not used during automated tests)
    BasicTestCase.recordMode = True


def make_async(async_cls, *args, **kwargs):
    """
    Construct an async entry-point class (Github, GithubIntegration) directly and wrap it in SyncProxy.

    Most generated tests get their client from TestCase.get_github() (self.g), already SyncProxy-wrapped. A number
    instead construct their own client inline (e.g. to test an auth-failure path, or a non-default base_url) -- calling
    the async class directly there would just hand back an unawaited coroutine from the first method call; this gives
    them the same synchronous-looking bridging self.g gets. SyncProxy arguments are unwrapped first, so a wrapped Auth
    can be handed to the client.

    """
    args = tuple(SyncProxy._deep_unwrap(a) for a in args)
    kwargs = {k: SyncProxy._deep_unwrap(v) for k, v in kwargs.items()}
    return SyncProxy(async_cls(*args, **kwargs))


def type_of(obj):
    """
    SyncProxy-aware type(): the type of the wrapped object for a SyncProxy, type(obj) otherwise.

    SyncProxy spoofs __class__, which is enough for isinstance(), but type() can't be fooled. Generated tests call this
    wherever the classic test calls type(), since the argument may now be a SyncProxy.

    """
    return type(SyncProxy._deep_unwrap(obj)) if isinstance(obj, SyncProxy) else type(obj)


def _is_completable(obj):
    """
    Check if an object is a CompletableGithubObject that may need completion.
    """
    try:
        return isinstance(obj, githubasyncio.GithubObject.CompletableGithubObject)
    except Exception:
        return False


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
        if isinstance(result, githubasyncio.GithubObject._NotSetType):
            return result
        # Also pass through _ValuedAttribute and _BadAttribute instances
        # which are internal attribute wrappers, not user-facing objects.
        if isinstance(
            result,
            (githubasyncio.GithubObject._ValuedAttribute, githubasyncio.GithubObject._BadAttribute),
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


class TestCase(BasicTestCase):
    """
    Creates an async Github instance wrapped in SyncProxy, so test methods -- copied verbatim from the classic
    project's sync test files -- can call async methods synchronously.
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

        Generated test method bodies are copied verbatim from the classic project's sync tests,
        so an assertIsInstance()/assertNotIsInstance() call may still name a classic
        `github.X.Y` class even though the object under test is really `githubasyncio.X.Y` --
        this resolves the latter from the former's __module__/__name__ so the assertion still
        makes sense. Purely a reflection-based lookup (importlib), not a dependency on the
        classic package actually being installed: it simply returns `cls` unchanged if
        `githubasyncio.X` doesn't exist (e.g. `github.PublicKey` was never given an async twin
        because it never did any I/O -- see FORCE_FULL_TRANSFORM history), or if `cls` was
        already an async class to begin with.

        """
        mod = getattr(cls, "__module__", "") or ""
        if mod.startswith("github.") and not mod.startswith("githubasyncio."):
            async_mod_name = "githubasyncio." + mod[len("github.") :]
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

        # Set up frame debugging
        githubasyncio.GithubObject.GithubObject.setCheckAfterInitFlag(True)
        githubasyncio.Requester.Requester.setDebugFlag(True)
        githubasyncio.Requester.Requester.setOnCheckMe(self.getFrameChecker())

        self.g = self.get_github(self.authMode, self.retry, self.pool_size)

    def tearDown(self):
        g = getattr(self, "g", None)
        if g is not None:
            loop = object.__getattribute__(g, "_loop")
            try:
                g.close()
            finally:
                loop.close()
        # Drop all wrappers cached during this test so the objects they
        # hold (and their event loops/connections) can be garbage collected.
        SyncProxy._cache.clear()
        super().tearDown()

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
