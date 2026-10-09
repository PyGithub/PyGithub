#!/usr/bin/env python3
############################ Copyrights and license ############################
#                                                                              #
# Copyright 2026 Ahmed Tahri <tahri.ahmed@proton.me>                           #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################
"""
Analysis-driven async code generator for PyGithub.

Run from within the `async/` project (a standalone sibling of the classic PyGithub project, kept in sync via
`scripts/sync_async.sh`). Introspects the classic PyGithub package (`../github`) to discover which classes and methods
perform I/O (directly or transitively), then generates async/await source into the `githubasyncio/` root module here.
Also generates async test files into `tests/`.

Adapted from the PRAW async-generator that I (Ahmed Tahri) made. Previously also made a sync to async generator for
grafana-client but wasn't based on AST parsing.

"""

from __future__ import annotations

import argparse
import ast
import functools
import logging
import re
import shutil
import subprocess
import sys
import tokenize
from collections.abc import Callable
from pathlib import Path
from typing import NamedTuple

logger = logging.getLogger(__name__)


@functools.cache
def _compile(pattern: str) -> re.Pattern[str]:
    return re.compile(pattern)


REPO_ROOT = Path(__file__).resolve().parent.parent
# The classic (sync) PyGithub project this async project is generated from — a sibling
# directory, not a subdirectory: `sync_async.sh` deliberately does not copy `github/` or
# `tests/` into here, so the generator reads them straight from the sync checkout.
SYNC_ROOT = REPO_ROOT.parent
SRC_PKG = SYNC_ROOT / "github"
DST_PKG = REPO_ROOT / "githubasyncio"
TEST_SRC = SYNC_ROOT / "tests"
TEST_DST = REPO_ROOT / "tests"

AUTO_HEADER = "# FILE AUTO GENERATED DO NOT TOUCH\n"

# Files that should NEVER be copied to async: __init__.py is custom-generated (see
# generate_async_init()), not derived 1:1 from the sync module of the same name.
SKIP_FILES = {"__init__.py"}
# Stems (without .py) for membership tests against Path.stem or bare module names.
SKIP_STEMS = {f.removesuffix(".py") for f in SKIP_FILES}

# Names github/__init__.py re-exports as a class of the same name, shadowing the module itself at
# the package-attribute level (`github.X` becomes the class, not the module, once
# github/__init__.py finishes running -- see _find_shadowed_module_aliases()). This is about how
# code that does `import github.X as X` (bare dotted-attribute access) must special-case these,
# not about whether X gets its own githubasyncio/X.py (every module does now -- see main()).
SHADOWED_MODULE_NAMES = frozenset(
    {"GithubException", "GithubIntegration", "GithubRetry", "InputFileContent", "InputGitAuthor", "InputGitTreeElement"}
)

# Modules that, if given a real (import-fixed) copy, would produce a circular import
# `_fix_imports` can't resolve on its own: it always rewrites cross-references eagerly (`from
# githubasyncio.X import Y`, or `import githubasyncio.X` for a bare `github.X.`
# reference anywhere in the file -- even one the sync source only reaches lazily, behind `if
# TYPE_CHECKING:` + a same-method dotted access). The sync package tolerates this because such a
# reference never actually triggers loading the target module as a side effect of an unrelated
# import; eagerly resolving it here can. ARCHITECTURE.md's documented convention for sync-side
# runtime references -- bare `import github.X` + `github.X.Y` dotted access, never eager
# `from github.X import Y` name-extraction across modules -- is what keeps _fix_imports' normal
# handling safe: it produces a module-only `import githubasyncio.X` rewrite, which tolerates the
# target module still being mid-import. `github/GithubIntegration.py`'s `github.Github(...)`
# construction is the one place that pattern doesn't apply cleanly on its own (MainClass.py
# imports back from GithubIntegration.py, a genuine mutual dependency); PATCHES["GithubIntegration"]
# handles that one directly instead of relying on this set.
# Left empty, not deleted: a named escape hatch for the next module that hits the general problem
# in a way that can't be fixed at the sync source (`_fix_imports` still doesn't understand
# TYPE_CHECKING-only laziness in general).
CIRCULAR_IMPORT_REEXPORT: frozenset[str] = frozenset()

# Pure-data modules (no I/O, no SyncProxy bridging needed): Consts has no classes at all, and the
# rest define only plain data/exception classes with no async methods of their own. Used to scope
# transform_test_file's package-level class rewrite (below) to classes that are safe to construct
# directly -- unlike e.g. Github (MainClass), which has async methods and would return raw,
# unbridged coroutines if a test constructed `githubasyncio.MainClass.Github(...)` directly
# instead of going through the framework's SyncProxy-wrapped self.g.
PURE_DATA_MODULES = frozenset(
    {"Consts", "GithubException", "GithubRetry", "InputFileContent", "InputGitAuthor", "InputGitTreeElement"}
)

# Regex patterns: a test *method* containing any of these keeps constructing entry-point classes
# (Github, GithubIntegration) the classic (sync) way, even though transform_test_file otherwise
# routes such construction through Framework.make_async() for SyncProxy bridging. See the call
# site (in transform_test_file) for why each needs the escape hatch. (`mock.Mock(return_value=...)`
# / `side_effect=` are plain function stubs -- e.g. a frozen `datetime.now` -- and behave the same
# against either stack, so they don't count.)
ENTRY_POINT_CTOR_SKIP_MARKERS = (r"\bmock\.MagicMock\(", r"\bmock\.Mock\((?!return_value=|side_effect=)")

# Test files to skip (not test modules, or infrastructure)
SKIP_TEST_FILES = {
    "__init__.py",
    "Framework.py",
    "VcrSerializer.py",
    "__pycache__",
    # ExposeAllAttributes: request ordering differs in async due to eager completion timing
    "ExposeAllAttributes.py",
}

# Methods that must NEVER be made async (Python doesn't support async __init__, etc.)
# __enter__/__exit__/__iter__ are handled separately by dedicated conversion methods
NEVER_ASYNC_METHODS = {
    "__init__",
    "__new__",
    "__del__",
    "__repr__",
    "__str__",
    "__hash__",
    "__eq__",
    "__ne__",
    "__lt__",
    "__le__",
    "__gt__",
    "__ge__",
    "__bool__",
    "__len__",
    "__contains__",
    "__getattr__",
    "__setattr__",
    "__delattr__",
    "__enter__",
    "__exit__",
    "__iter__",
    "__reversed__",
    "__getitem__",
}

# Requester methods that perform HTTP/GraphQL I/O.
# help us build the tree of what need sync to async.
IO_METHOD_PATTERNS = frozenset(
    {
        "requestJsonAndCheck",
        "requestMultipartAndCheck",
        "requestBlobAndCheck",
        "requestMemoryBlobAndCheck",
        "requestJson",
        "requestMultipart",
        "requestBlob",
        "graphql_query",
        "graphql_query_class",
        "graphql_node",
        "graphql_node_class",
        "graphql_named_mutation",
        "graphql_named_mutation_class",
        "getFile",
        "getStream",
    }
)

# Methods that need an `await` when called on a requester object in generated part.
REQUESTER_AWAIT_METHODS = IO_METHOD_PATTERNS | {"close", "check", "postProcess"}

# Bases through which async-ness does NOT propagate to subclasses.
# WithRequester subclasses (the Auth hierarchy) are token providers deliberately
# shared between the sync and async stacks: the async Requester consumes the sync
# Auth objects as-is, so they must never be transformed.
NON_PROPAGATING_BASES = frozenset({"WithRequester"})

# Classes that perform I/O directly (seeds of the async propagation).
IO_ROOT_CLASSES = frozenset(
    {
        "Requester",
        "HTTPSRequestsConnectionClass",
        "HTTPRequestsConnectionClass",
        "RequestsResponse",
        "WithRequester",
        "PaginatedListBase",  # defines _grow, __fetchToIndex that do I/O via _fetchNextPage
    }
)

# Private Requester methods that are part of the I/O call chain (name-mangled
# callers can't be detected by the generic self.X( pattern alone).
REQUESTER_PRIVATE_IO = frozenset(
    {
        "__requestRaw",
        "__requestEncode",
        "__deferRequest",
        "__createConnection",
        "__check",
        "__postProcess",
    }
)

# a method touching self.session with one of these
# performs the actual network I/O.
HTTP_SESSION_VERBS = (".get(", ".post(", ".put(", ".patch(", ".delete(", ".head(", ".query(")

# Connection wrapper classes whose session-touching methods are async.
CONNECTION_CLASSES = frozenset({"HTTPSRequestsConnectionClass", "HTTPRequestsConnectionClass"})

# A close() method owning one of these must be async (closes async resources).
CLOSE_OWNER_PATTERNS = (
    "__requester.close()",
    "_requester.close()",
    "__connection.close()",
    "session.close()",
)

# Lock attributes guarded by `with` in sync code -> `async with` (asyncio.Lock).
LOCK_ATTRS = ("__connection_lock", "_connection_lock")

# HTTP library sync->async API mapping.
SESSION_REWRITES = {"niquests.Session(": "niquests.AsyncSession("}

# Mock-target string rewrites for generated tests: (match, replace, excluded
# test stems). These encode RUNTIME knowledge that cannot be derived
# statically.
TEST_MOCK_REWRITES: tuple[tuple[str, str, frozenset[str]], ...] = (
    (
        'mock.patch("github.Requester.time.sleep"',
        'mock.patch("githubasyncio.Requester.asyncio.sleep"',
        frozenset(),
    ),
    ('"github.Requester.datetime"', '"githubasyncio.Requester.datetime"', frozenset()),
    ('mock.patch("github.PublicKey.encrypt")', 'mock.patch("githubasyncio.PublicKey.encrypt")', frozenset()),
    ('"github.AccessToken.datetime"', '"githubasyncio.AccessToken.datetime"', frozenset()),
    ("github.GithubObject.NotSet", "githubasyncio.GithubObject.NotSet", frozenset()),
    # The async stack reads its own Consts / requestlib, so patch and use those.
    ('"github.Requester.Consts.', '"githubasyncio.Requester.Consts.', frozenset()),
    ("from github.requestlib import ", "from githubasyncio.requestlib import ", frozenset()),
    ("github.requestlib.", "githubasyncio.requestlib.", frozenset()),
    # `gr` alias of the Requester module: a Requester built here is called directly (requestJson),
    # so it needs the same SyncProxy wrapping as a directly-built entry point.
    ("from github import Requester as gr", "from githubasyncio import Requester as gr", frozenset()),
    ("return gr.Requester(", "return Framework.make_async(gr.Requester, ", frozenset()),
    ("r = gr.Requester(", "r = Framework.make_async(gr.Requester, ", frozenset()),
    # A test stub replacing Requester.__requestRaw must be awaitable, since the async
    # __requestEncode does `await self.__requestRaw(...)`.
    ("def requestRaw(cnx, verb,", "async def requestRaw(cnx, verb,", frozenset()),
    # An incomplete object built on a bare mock requester: the async class, SyncProxy-wrapped so
    # `_completeIfNeeded` (async) raises synchronously through assertRaises. It raises before
    # touching the requester, so the plain mock is enough.
    (
        "github.UserKey.UserKey.setCheckAfterInitFlag(False)",
        "githubasyncio.UserKey.UserKey.setCheckAfterInitFlag(False)",
        frozenset(),
    ),
    (
        "github.UserKey.UserKey(mock.MagicMock(), {}, {}, False)",
        "Framework.make_async(githubasyncio.UserKey.UserKey, mock.MagicMock(), {}, {}, False)",
        frozenset(),
    ),
)

# Logger injection: the tests' logger plumbing targets the async Requester (these classmethods stay
# sync, so this is a decision -- not derivable from the analysis).
TEST_LOGGER_CALLS: tuple[tuple[str, str], ...] = (
    (
        "github.Requester.Requester.injectLogger(self.logger)",
        "githubasyncio.Requester.Requester.injectLogger(self.logger)",
    ),
    (
        "github.Requester.Requester.resetLogger()",
        "githubasyncio.Requester.Requester.resetLogger()",
    ),
)

# Module-level helpers patched in PATCHES["GithubObject"] whose async variants
# must be imported by tests instead of the sync originals (the async versions
# accept both sync and async NotSet).
TEST_HELPER_IMPORT_REWRITES: tuple[tuple[str, str], ...] = (
    ("from github.GithubObject import is_undefined", "from githubasyncio.GithubObject import is_undefined"),
    ("from github.GithubObject import is_defined", "from githubasyncio.GithubObject import is_defined"),
)

# Markers identifying transformable test files, and paths under TEST_DST this generator doesn't
# own and must never delete: ReplayData/ (the VCR cassette fixtures) is synced in by
# scripts/sync_async.sh, not generated here.
TEST_BASE_CLASS_MARKERS = ("Framework.TestCase", "BasicTestCase")
PRESERVE_TEST_FILES = frozenset({"ReplayData"})

# Sync test infrastructure copied byte-for-byte into TEST_DST (no async transformation): just
# VcrSerializer.py, a vcrpy serializer format with no dependency on the classic package at all.
COPY_TEST_FILES = ("VcrSerializer.py",)

# tests/AsyncFramework.py (self-contained: see the file's own docstring for why) is copied in
# from this hand-maintained template, same idea as COPY_TEST_FILES but sourced from scripts/
# (which sync_async.sh doesn't touch) instead of the classic tests/ dir.
TEMPLATE_TEST_FILES = {"AsyncFramework.py": REPO_ROOT / "scripts" / "async_framework_template.py"}

# Public exports of the generated githubasyncio/__init__.py: {module: (name, ...)}.
ASYNC_INIT_EXPORTS: dict[str, tuple[str, ...]] = {"MainClass": ("Github",)}


class Patch(NamedTuple):
    """
    One declarative source patch for a generated module (see PATCHES).

    ``match`` is an exact string unless ``regex=True`` (then a MULTILINE pattern whose ``replace`` may use backrefs).
    ``count`` is the exact number of occurrences expected in the source — generation aborts on any mismatch, so
    upstream drift breaks the build instead of silently skipping the patch.

    """

    reason: str
    match: str
    replace: str
    regex: bool = False
    count: int = 1


# Manual surgery for modules whose ASYNC SEMANTICS legitimately differ from what
# mechanical transformation can produce. This is the complete catalog of
# hand-maintained differences between the sync and async variants.
PATCHES: dict[str, list[Patch]] = {
    "GithubObject": [
        Patch(
            reason="cannot await inside __init__ — store a flag; SyncProxy._wrap()/user code completes later",
            regex=True,
            match=(
                r"^(\s+)if requester\.is_not_lazy and completed is None and not response_given:\s*\n"
                r"\s+(?:await )?self\.complete\(\)\n"
            ),
            replace=(
                r"\1# Async: store flag instead of calling self.complete() (can't await in __init__).\n"
                r"\1# The SyncProxy._wrap() or user code should call await obj.complete() when this is True.\n"
                r"\1self._needs_async_completion = (\n"
                r"\1    requester.is_not_lazy and completed is None and not response_given\n"
                r"\1)\n"
            ),
        ),
        Patch(
            reason="__eq__ must accept both sync and async class hierarchies (compare names, not identity)",
            regex=True,
            match=r"other\.__class__ is self\.__class__",
            replace="other.__class__.__name__ == self.__class__.__name__",
        ),
        Patch(
            reason="TypeGuard now imported from typing, not typing_extensions; drop it here since "
            "is_defined/is_undefined switch to TypeIs (typing_extensions-only)",
            match="from typing import TYPE_CHECKING, Any, TypeGuard, Union, overload",
            replace="from typing import TYPE_CHECKING, Any, Union, overload",
        ),
        Patch(
            reason="TypeIs narrows in both branches (TypeGuard only narrows the True branch)",
            match="from typing_extensions import ParamSpec, Protocol, Self, TypeVar",
            replace="from typing_extensions import ParamSpec, Protocol, Self, TypeIs, TypeVar",
        ),
        Patch(
            reason="TypeIs narrows in both branches (TypeGuard only narrows the True branch)",
            match=("def is_defined(v: T | _NotSetType) -> TypeGuard[T]:\n" "    return not isinstance(v, _NotSetType)"),
            replace=("def is_defined(v: T | _NotSetType) -> TypeIs[T]:\n" "    return not isinstance(v, _NotSetType)"),
        ),
        Patch(
            reason="TypeIs narrows in both branches (TypeGuard only narrows the True branch)",
            match=(
                "def is_undefined(v: T | _NotSetType) -> TypeGuard[_NotSetType]:\n"
                "    return isinstance(v, _NotSetType)"
            ),
            replace=(
                "def is_undefined(v: T | _NotSetType) -> TypeIs[_NotSetType]:\n    return isinstance(v, _NotSetType)"
            ),
        ),
    ],
    "PaginatedList": [
        Patch(
            reason="sync iteration protocol (__iter__) becomes async iteration (__aiter__) for both "
            "PaginatedListBase and _Slice",
            regex=True,
            count=2,
            match=r"def __iter__\(self\)\s*->\s*Iterator\[T\]:",
            replace="async def __aiter__(self) -> AsyncIterator[T]:",
        ),
        Patch(
            reason="_Slice.__aiter__ must use the async getitem() (subscript would call sync __getitem__)",
            regex=True,
            match=r"(\s+)yield (?:await )?(self\.__list)\[index\]",
            replace=r"\1yield await \2.getitem(index)",
        ),
        Patch(
            reason="__getitem__ stays sync (Python cannot await dunders) — drop the awaited fetch; "
            "async fetching moves to the injected getitem()",
            regex=True,
            match=r"^(\s+)await self\.(?:_PaginatedListBase)?__fetchToIndex\(index\)\n",
            replace="",
        ),
        Patch(
            reason="document that the now-sync __getitem__ only returns already-fetched elements",
            regex=True,
            match=r"(def __getitem__\(self, index: int \| slice\)[^\n]*\n)(\s+assert isinstance\(index,)",
            replace=(
                r"\1"
                '        """Synchronous element access \u2014 only returns already-fetched elements.\n'
                "\n"
                "        For async-aware fetching (which loads pages on demand), use\n"
                "        ``await obj.getitem(index)`` instead.\n"
                "\n"
                "        :raises IndexError: if *index* has not been fetched yet.\n"
                '        """\n'
                r"\2"
            ),
        ),
        Patch(
            reason="inject async getitem() — the async-aware replacement for __getitem__",
            regex=True,
            match=r"(return self\._Slice\(self, index\)\n)",
            replace=(
                r"\1"
                "\n"
                "    async def getitem(self, index: int | slice) -> T | _Slice:\n"
                '        """Async element access with on-demand page fetching.\n'
                "\n"
                "        This is the async replacement for ``__getitem__`` — Python cannot\n"
                "        implicitly ``await`` dunder methods, so ``obj[i]`` would return a\n"
                "        coroutine rather than a value if ``__getitem__`` were async.\n"
                "\n"
                "        Usage::\n"
                "\n"
                "            element = await paginated_list.getitem(0)\n"
                "            sliced  = await paginated_list.getitem(slice(2, 5))\n"
                '        """\n'
                "        assert isinstance(index, (int, slice))\n"
                "        if isinstance(index, int):\n"
                "            await self.__fetchToIndex(index)\n"
                "            return self.__elements[index]\n"
                "        else:\n"
                "            return self._Slice(self, index)\n"
            ),
        ),
        Patch(
            reason="remove __reversed__ — a sync dunder cannot await the async `reversed` property; "
            "the SyncProxy.__reversed__ bridge handles it for tests",
            regex=True,
            match=(
                r"\n    # To support Python's built-in `reversed\(\)` method\n"
                r"    def __reversed__\(self\)[^\n]*\n"
                r"        return self\.reversed\n"
            ),
            replace="\n",
        ),
        Patch(
            reason="__aiter__ annotations need AsyncIterator",
            match="from collections.abc import ",
            replace="from collections.abc import AsyncIterator, ",
        ),
    ],
    "Auth": [
        Patch(
            reason="the analyzer can't type `self.__integration` / `self.__app` (private attributes "
            "assigned in withRequester from lazily imported classes), so it misses that fetching or "
            "refreshing a token is I/O. Auth.authentication() is what the Requester calls per request; "
            "make it awaitable, and let it await a subclass `token` that is itself async (the "
            "installation / user token classes below) -- token classes with no I/O keep a plain "
            "property.",
            match='        headers["Authorization"] = f"{self.token_type} {self.token}"',
            replace="        token = self.token\n"
            "        if inspect.isawaitable(token):\n"
            "            token = await token\n"
            '        headers["Authorization"] = f"{self.token_type} {token}"',
        ),
        Patch(
            reason="authentication() is now a coroutine (see above)",
            match="    def authentication(self, headers: dict) -> None:",
            replace="    async def authentication(self, headers: dict) -> None:",
        ),
        Patch(
            reason="inspect.isawaitable, used by authentication()",
            match="import base64\n",
            replace="import base64\nimport inspect\n",
        ),
        Patch(
            reason="AppInstallationAuth.token fetches a live installation access token (I/O)",
            match="    def token(self) -> str:\n"
            "        if self.__installation_authorization is None or self._is_expired:\n"
            "            self.__installation_authorization = self._get_installation_authorization()\n",
            replace="    async def token(self) -> str:  # type: ignore[override]  # awaited by Auth.authentication()\n"
            "        if self.__installation_authorization is None or self._is_expired:\n"
            "            self.__installation_authorization = await self._get_installation_authorization()\n",
        ),
        Patch(
            reason="GithubIntegration.get_access_token is a coroutine",
            match="    def _get_installation_authorization(self) -> InstallationAuthorization:\n"
            '        assert self.__integration is not None, "Method withRequester(Requester) must be called first"\n'
            "        return self.__integration.get_access_token(",
            replace="    async def _get_installation_authorization(self) -> InstallationAuthorization:\n"
            '        assert self.__integration is not None, "Method withRequester(Requester) must be called first"\n'
            "        return await self.__integration.get_access_token(",
        ),
        Patch(
            reason="AppUserAuth.token refreshes an expired user token (I/O)",
            match="    def token(self) -> str:\n        if self._is_expired:\n            self._refresh()\n",
            replace="    async def token(self) -> str:  # type: ignore[override]  # awaited by Auth.authentication()\n        if self._is_expired:\n            await self._refresh()\n",
        ),
        Patch(
            reason="ApplicationOAuth.refresh_access_token is a coroutine",
            match="    def _refresh(self) -> None:",
            replace="    async def _refresh(self) -> None:",
        ),
        Patch(
            reason="ApplicationOAuth.refresh_access_token is a coroutine",
            match="        token = self.__app.refresh_access_token(self._refresh_token)",
            replace="        token = await self.__app.refresh_access_token(self._refresh_token)",
        ),
    ],
    "Requester": [
        Patch(
            reason="Auth.authentication() is a coroutine (see PATCHES['Auth']), but a user-defined "
            "Auth subclass may still override it as a plain method, so only await a coroutine",
            match="            self.__auth.authentication(requestHeaders)",
            replace="            authenticated = self.__auth.authentication(requestHeaders)\n"
            "            if asyncio.iscoroutine(authenticated):\n"
            "                await authenticated",
        ),
        Patch(
            reason="async I/O requires niquests's AsyncSession, which githubasyncio.requestlib "
            "intentionally doesn't export (it covers the symbols async code needs as plain "
            "values -- PreparedRequest/Response/Retry/adapters -- not a sync-vs-async Session "
            "choice, so the async Session comes straight from niquests instead)",
            match="from githubasyncio.requestlib import PreparedRequest, Response, Retry, Session, adapters",
            replace=(
                "from githubasyncio.requestlib import PreparedRequest, Response, Retry, adapters\n"
                "from niquests import AsyncSession as Session"
            ),
        ),
        Patch(
            reason="mount the async adapter on the async session (adapters.HTTPAdapter is sync-only)",
            regex=True,
            count=2,
            match=r"adapters\.HTTPAdapter\(",
            replace="adapters.AsyncHTTPAdapter(",
        ),
    ],
    "GithubIntegration": [
        Patch(
            reason="get_github_for_installation() constructs a Github client via the classic "
            "package's bare `import github` + `github.Github(...)` -- Step 3b (which would "
            "normally rewrite this to the bare async class name) deliberately skips it, since "
            "MainClass.py imports back from GithubIntegration.py (a real, mutual dependency, not "
            "just this generator's eagerness), so 'bare Github' isn't safely in scope here either "
            "way. Use the package-level `githubasyncio.Github` instead (resolved at call time, so "
            "safe regardless of load order), matching Step 3b's own rewrite for package re-exports.",
            match="return github.Github(**self.__requester.withAuth(auth).kwargs)",
            replace="return githubasyncio.Github(**self.__requester.withAuth(auth).kwargs)",
        ),
        Patch(
            reason="bare package import backing the usage above (replaces the classic bare `import github`)",
            match="import github\n",
            replace="import githubasyncio\n",
        ),
        Patch(
            reason="qualify the return type annotation to match (lazy string either way, thanks "
            "to `from __future__ import annotations`, but keep it consistent for type checkers)",
            match=") -> github.Github:",
            replace=") -> githubasyncio.Github:",
        ),
        Patch(
            reason="a docstring mention of `github.GithubIntegration` (not real code) is enough "
            "to fool _ensure_import_github's textual github.X scan into re-adding the `import "
            "github` the patches above just removed -- drop the now-stale sync-package prefix",
            match="          with github.GithubIntegration(...) as gi:",
            replace="          with GithubIntegration(...) as gi:",
        ),
        Patch(
            reason="likewise, this deprecation message's `github.Github` mention (also not real "
            "code) would otherwise fool _ensure_import_github the same way. Step 2 already "
            "rewrote the two `github.Auth.AppAuth` mentions to `githubasyncio.Auth.AppAuth` "
            "(they're plain `github.X.` text, same as real code), so only `github.Github` needs "
            "fixing here.",
            match="Use github.Github(auth=githubasyncio.Auth.AppAuth), githubasyncio.Auth.AppAuth.token or "
            "githubasyncio.Auth.AppAuth.create_jwt(expiration) instead",
            replace="Use githubasyncio.Github(auth=githubasyncio.Auth.AppAuth), githubasyncio.Auth.AppAuth.token or "
            "githubasyncio.Auth.AppAuth.create_jwt(expiration) instead",
        ),
    ],
}


def _apply_patches(stem: str, src: str) -> str:
    for p in PATCHES.get(stem, ()):
        if p.regex:
            new_src, n = re.subn(p.match, p.replace, src, flags=re.MULTILINE)
        else:
            n = src.count(p.match)
            new_src = src.replace(p.match, p.replace)
        if n != p.count:
            raise RuntimeError(f"PATCHES[{stem!r}]: expected {p.count} match(es), found {n} — {p.reason}")
        logger.debug("apply_patches[%s]: %s", stem, p.reason)
        src = new_src
    return src


@functools.lru_cache(maxsize=1)
def _shadowed_skip_modules() -> tuple[str, ...]:
    """
    SKIP modules whose name is shadowed by a same-name re-export in github/__init__.py.

    For these modules, ``import github.M as M`` resolves to the re-exported object (usually the CLASS), not the module,
    once __init__.py has completed. Generated async code (which loads after __init__.py) therefore needs the
    _sys.modules fix applied by _fix_shadowed_module_alias.

    """
    init_file = SRC_PKG / "__init__.py"
    if not init_file.exists():
        return ()
    try:
        tree = ast.parse(init_file.read_text(encoding="utf-8"))
    except SyntaxError:
        return ()
    shadowed = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.level == 1 and node.module in SHADOWED_MODULE_NAMES:
            for alias in node.names:
                if (alias.asname or alias.name) == node.module:
                    shadowed.add(node.module)
    return tuple(sorted(shadowed))


@functools.lru_cache(maxsize=1)
def _init_reexports_map() -> dict[str, str]:
    """
    Map class_name -> module_name for every class github/__init__.py re-exports under a name different from its own
    defining module (e.g. Github -> MainClass, UnknownObjectException -> GithubException).

    Used to rewrite `github.ClassName` (package-level access relying on this re-export) to the
    async equivalent, both in AsyncTransformer._fix_imports (source files, step 3b) and
    transform_test_file (test files).

    """
    init_file = SRC_PKG / "__init__.py"
    reexports: dict[str, str] = {}
    if not init_file.exists():
        return reexports
    init_src = init_file.read_text()
    # Multi-line parenthesized imports, e.g.
    #   from .GithubException import (
    #       BadAttributeException,
    #       ...
    #   )
    import_patterns = [
        re.compile(r"^from \.(\w+) import \(([^)]*)\)", re.MULTILINE | re.DOTALL),
        # Single-line imports, e.g. `from .MainClass import Github`
        re.compile(r"^from \.(\w+) import ([^(\n]+)$", re.MULTILINE),
    ]
    for pattern in import_patterns:
        for m in pattern.finditer(init_src):
            mod_name, names_blob = m.group(1), m.group(2)
            for cls_name in re.findall(r"\w+", names_blob):
                if cls_name != mod_name:
                    reexports.setdefault(cls_name, mod_name)
    return reexports


def _sync_dotted_ref(mod: str, cls_name: str) -> str:
    """
    The sync-package reference for cls_name, defined in module mod, for dual sync/async isinstance/issubclass checks.

    Normally `github.{mod}.{cls_name}` (module, then class). But when mod is itself shadowed by a
    same-named class re-export (SHADOWED_MODULE_NAMES), `github.{mod}` is already a CLASS, not the
    module (github/__init__.py's re-export shadows the module at the package-attribute level) --
    for *every* class cls_name defined in that module, not just the one sharing its name (e.g.
    `github.GithubException` is the GithubException class, so `github.GithubException.
    BadCredentialsException` is also broken, not just `github.GithubException.GithubException`).
    Every such class is, however, also re-exported bare at the package level in the same
    __init__.py block (that's how the shadowing itself happens), so `github.{cls_name}` reaches it
    directly there instead.

    """
    if mod in SHADOWED_MODULE_NAMES:
        return f"github.{cls_name}"
    return f"github.{mod}.{cls_name}"


class IOAnalyzer:
    """
    Statically analyses the github package to find classes/methods that do I/O.
    """

    def __init__(self):
        # class_name -> set of method names that need to be async
        self.async_methods: dict[str, set[str]] = {}
        # class_name -> True  (class itself needs async variant)
        self.async_classes: set[str] = set()
        # file stem -> AST module
        self.trees: dict[str, ast.Module] = {}
        # file stem -> source text
        self.sources: dict[str, str] = {}
        # class_name -> file stem
        self.class_to_file: dict[str, str] = {}
        # class_name -> set of base class names
        self.class_bases: dict[str, list[str]] = {}
        # base class_name -> set of direct subclasses (reverse of class_bases)
        self._subclass_map: dict[str, set[str]] = {}
        # class_name -> set of @property method names (must NEVER be made async)
        self.property_methods: dict[str, set[str]] = {}
        # class_name -> set of property names that were PROMOTED to async def
        # (were @property but now async because they call _completeIfNotSet etc.)
        self.promoted_properties: dict[str, set[str]] = {}
        # --- Type registry (populated by build_type_registry) ---
        # Classes that inherit from CompletableGithubObject
        self.completable_classes: set[str] = set()
        # class_name -> {prop_or_method_name -> set of class names from return type}
        self.return_types: dict[str, dict[str, set[str]]] = {}
        # class_name -> {method_name -> {param_name -> set of class names from type annotation}}
        self.param_types: dict[str, dict[str, dict[str, set[str]]]] = {}
        # class_name -> set of method names that are @staticmethod or @classmethod
        self.static_methods: dict[str, set[str]] = {}
        # caches: method source text and class ancestor lists
        self._method_src_cache: dict[tuple[str, str, int], str] = {}
        self._mro_cache: dict[str, list[str]] = {}

    @staticmethod
    def _search(pattern: str, text: str) -> re.Match[str] | None:
        """
        Regex search using the shared compilation cache.
        """
        return _compile(pattern).search(text)

    def _get_method_src(
        self, cls_name: str, method_name: str, method_node: ast.FunctionDef | ast.AsyncFunctionDef
    ) -> str:
        """
        Get method source text, cached.

        Keyed by node identity (not just cls_name/method_name) because overloaded methods
        (multiple `@overload` stubs plus the real implementation) share the same name but
        are distinct AST nodes with different bodies — caching by name alone would return
        the first-seen overload's (often trivial `...`) source for all of them.

        """
        key = (cls_name, method_name, id(method_node))
        result = self._method_src_cache.get(key)
        if result is None:
            stem = self.class_to_file.get(cls_name)
            if stem is None:
                return ""
            src = self.sources.get(stem, "")
            result = ast.get_source_segment(src, method_node) or ""
            self._method_src_cache[key] = result
        return result

    def _get_mro(self, cls_name: str) -> list[str]:
        """
        Get full ancestor list (excluding cls_name itself), cached.
        """
        result = self._mro_cache.get(cls_name)
        if result is not None:
            return result
        ancestors: list[str] = []
        visited: set[str] = set()
        queue = list(self.class_bases.get(cls_name, []))
        while queue:
            base = queue.pop(0)
            if base in visited:
                continue
            visited.add(base)
            ancestors.append(base)
            queue.extend(self.class_bases.get(base, []))
        self._mro_cache[cls_name] = ancestors
        return ancestors

    def _get_inherited_async(self, cls_name: str) -> set[str]:
        """
        Get all async methods inherited from ancestor classes.
        """
        result: set[str] = set()
        for base in self._get_mro(cls_name):
            result |= self.async_methods.get(base, set())
        return result

    def _get_descendant_async(self, cls_name: str) -> set[str]:
        """
        Get all async methods defined by descendant classes.

        Used for virtual dispatch: a base-class method calling ``self.M()`` may dispatch to an async override at
        runtime (e.g. PaginatedListBase._grow calls self._fetchNextPage, which only the PaginatedList subclass
        implements with I/O).

        """
        result: set[str] = set()
        visited: set[str] = set()
        queue = list(self._subclass_map.get(cls_name, ()))
        while queue:
            cn = queue.pop(0)
            if cn in visited:
                continue
            visited.add(cn)
            result |= self.async_methods.get(cn, set())
            queue.extend(self._subclass_map.get(cn, ()))
        return result

    def _get_inherited_promoted(self, cls_name: str) -> set[str]:
        """
        Get all promoted properties from ancestor classes.
        """
        result: set[str] = set()
        for base in self._get_mro(cls_name):
            result |= self.promoted_properties.get(base, set())
        return result

    def parse_all(self):
        """
        Parse all .py files under github/.
        """
        for p in sorted(SRC_PKG.glob("*.py")):
            stem = p.stem
            if stem.startswith("__"):
                logger.debug("parse_all: skipping dunder module '%s'", stem)
                continue
            src = p.read_text(encoding="utf-8")
            try:
                tree = ast.parse(src, filename=str(p))
            except SyntaxError:
                logger.debug("parse_all: skipping '%s' (SyntaxError)", stem)
                continue
            self.trees[stem] = tree
            self.sources[stem] = src
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    self.class_to_file[node.name] = stem
                    self.class_bases[node.name] = [self._base_name(b) for b in node.bases]
                    # Track @staticmethod and @classmethod methods
                    statics: set[str] = set()
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef):
                            for dec in item.decorator_list:
                                if isinstance(dec, ast.Name) and dec.id in ("staticmethod", "classmethod"):
                                    statics.add(item.name)
                    if statics:
                        self.static_methods[node.name] = statics
                    logger.debug(
                        "parse_all: registered class '%s' in '%s' bases=%s",
                        node.name,
                        stem,
                        self.class_bases[node.name],
                    )

        # Build the reverse-inheritance map (base -> direct subclasses), used
        # for polymorphic descendant checks in is_attr_async_on_type().
        for cn, bases in self.class_bases.items():
            for base in bases:
                self._subclass_map.setdefault(base, set()).add(cn)

    @staticmethod
    def _base_name(node: ast.expr) -> str:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            return node.attr
        if isinstance(node, ast.Subscript):
            # Generic base: PaginatedListBase[T] -> PaginatedListBase
            return IOAnalyzer._base_name(node.value)
        return ""

    def _get_class_node(self, class_name: str) -> ast.ClassDef | None:
        stem = self.class_to_file.get(class_name)
        if stem is None or stem not in self.trees:
            return None
        for node in ast.walk(self.trees[stem]):
            if isinstance(node, ast.ClassDef) and node.name == class_name:
                return node
        return None

    @staticmethod
    def _extract_class_names(node: ast.expr | None) -> set[str]:
        """
        Extract class names from a type annotation AST node.

        Returns the set of class names referenced by the annotation,
        filtering out builtins (str, int, bool, float, bytes, None, Any, Self)
        and structural types (dict, tuple, Callable, Iterable).

        Handles these AST patterns:
          - Name(id='ClassName')
          - Attribute(value=Attribute(value=Name('github'), attr='Mod'), attr='Cls')
              → extracts 'Cls' (the innermost class name)
          - BinOp(left=..., op=BitOr(), right=...)  → PEP 604 union X | Y
          - Subscript(value=Name('list'), slice=X)  → element type X
          - Subscript(value=Name('PaginatedList'), slice=X)  → element type X
          - Subscript(value=Name('Opt'), slice=X)  → inner type X (Opt = Union[T, _NotSetType])
          - Subscript(value=Name('Attribute'), slice=X) → inner type X
          - Subscript(value=Name('dict'), slice=Tuple(...)) → value types
          - Subscript(value=Name('NotRequired'), slice=X) → inner type X
          - Constant(value=None) → ignored

        """
        if node is None:
            return set()

        # Builtins and non-domain types that should never appear in the result
        _SKIP_NAMES = frozenset(
            {
                "str",
                "int",
                "bool",
                "float",
                "bytes",
                "None",
                "NoneType",
                "Any",
                "Self",
                "object",
                "type",
                "datetime",
                "date",
                "timedelta",
                "Decimal",
                "Path",
            }
        )
        # Generic wrappers whose type parameter we should recurse into
        _WRAPPER_NAMES = frozenset(
            {
                "list",
                "set",
                "frozenset",
                "tuple",
                "Iterable",
                "Iterator",
                "Sequence",
                "Collection",
                "Mapping",
                "MutableMapping",
                "Opt",
                "Attribute",
                "NotRequired",
                "ClassVar",
                "Final",
            }
        )
        # Generic wrappers that ALSO contribute their own class name to the result
        # (because the variable may hold the container itself, not just elements)
        _WRAPPER_ALSO_SELF = frozenset(
            {
                "PaginatedList",
            }
        )
        # Structural types whose inner types we skip (not domain objects)
        _STRUCTURAL_NAMES = frozenset(
            {
                "dict",
                "Callable",
                "Generator",
                "AsyncGenerator",
                "Coroutine",
                "Awaitable",
            }
        )

        result: set[str] = set()

        def _visit(n: ast.expr) -> None:
            if isinstance(n, ast.Constant):
                # e.g. None literal in X | None
                return
            if isinstance(n, ast.Name):
                name = n.id
                if name in _SKIP_NAMES:
                    return
                if name.startswith("_"):
                    # e.g. _NotSetType — internal sentinel, skip
                    return
                if name in _WRAPPER_NAMES or name in _STRUCTURAL_NAMES or name in _WRAPPER_ALSO_SELF:
                    # Bare 'list', 'dict' etc without subscript — no useful type info
                    return
                result.add(name)
                return
            if isinstance(n, ast.Attribute):
                # Dotted name like github.NamedUser.NamedUser
                # Extract the final attribute as the class name
                name = n.attr
                if name in _SKIP_NAMES or name.startswith("_"):
                    return
                if name in _WRAPPER_NAMES or name in _STRUCTURAL_NAMES or name in _WRAPPER_ALSO_SELF:
                    return
                result.add(name)
                return
            if isinstance(n, ast.BinOp) and isinstance(n.op, ast.BitOr):
                # PEP 604 union: X | Y
                _visit(n.left)
                _visit(n.right)
                return
            if isinstance(n, ast.Subscript):
                # Generic type: Container[T]
                wrapper = n.value
                wrapper_name = ""
                if isinstance(wrapper, ast.Name):
                    wrapper_name = wrapper.id
                elif isinstance(wrapper, ast.Attribute):
                    wrapper_name = wrapper.attr

                if wrapper_name in _STRUCTURAL_NAMES:
                    # For dict[K, V], recurse into V (second element of Tuple)
                    # to catch dict[str, ContentFile | Commit] patterns
                    if wrapper_name == "dict" and isinstance(n.slice, ast.Tuple) and len(n.slice.elts) >= 2:
                        _visit(n.slice.elts[-1])
                    return
                if wrapper_name in _WRAPPER_NAMES:
                    # Recurse into the type parameter
                    _visit(n.slice)
                    return
                if wrapper_name in _WRAPPER_ALSO_SELF:
                    # Include both the container class AND the element type
                    # so that e.g. PaginatedList[PullRequest] → {PaginatedList, PullRequest}
                    result.add(wrapper_name)
                    _visit(n.slice)
                    return
                # Unknown generic — recurse into the wrapper itself
                # (could be a domain class used as generic)
                _visit(wrapper)
                _visit(n.slice)
                return
            if isinstance(n, ast.Tuple):
                # e.g. inside Subscript slices: tuple[str, int]
                for elt in n.elts:
                    _visit(elt)
                return

        _visit(node)
        return result

    def build_type_registry(self) -> None:
        """
        Build type registry from AST annotations of all parsed classes.

        Populates:
          - self.completable_classes: set of classes inheriting from CompletableGithubObject
          - self.return_types: class_name -> {attr_name -> set of class names from return type}
          - self.param_types: class_name -> {method_name -> {param_name -> set of class names}}

        """
        logger.info("build_type_registry: scanning %d parsed files", len(self.trees))

        # Phase 1: Identify completable classes via transitive inheritance
        # Start with the root
        completable_roots = {"CompletableGithubObject"}
        changed = True
        while changed:
            changed = False
            for cls_name, bases in self.class_bases.items():
                if cls_name in self.completable_classes:
                    continue
                for base in bases:
                    if base in completable_roots or base in self.completable_classes:
                        self.completable_classes.add(cls_name)
                        changed = True
                        break

        logger.info(
            "build_type_registry: found %d completable classes",
            len(self.completable_classes),
        )
        logger.debug(
            "build_type_registry: completable classes: %s",
            sorted(self.completable_classes),
        )

        # Phase 2: Extract return types and parameter types from all class methods
        for cls_name in list(self.class_to_file.keys()):
            cls_node = self._get_class_node(cls_name)
            if cls_node is None:
                continue

            cls_returns: dict[str, set[str]] = {}
            cls_params: dict[str, dict[str, set[str]]] = {}

            for item in ast.iter_child_nodes(cls_node):
                if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                method_name = item.name

                # Extract return type annotation
                if item.returns is not None:
                    ret_classes = self._extract_class_names(item.returns)
                    if ret_classes:
                        cls_returns[method_name] = ret_classes

                # Extract parameter type annotations
                param_types: dict[str, set[str]] = {}
                all_args = item.args.args + item.args.posonlyargs + item.args.kwonlyargs
                for arg in all_args:
                    if arg.arg == "self" or arg.arg == "cls":
                        continue
                    if arg.annotation is not None:
                        arg_classes = self._extract_class_names(arg.annotation)
                        if arg_classes:
                            param_types[arg.arg] = arg_classes
                # Also check *args and **kwargs
                if item.args.vararg and item.args.vararg.annotation:
                    arg_classes = self._extract_class_names(item.args.vararg.annotation)
                    if arg_classes:
                        param_types[item.args.vararg.arg] = arg_classes
                if item.args.kwarg and item.args.kwarg.annotation:
                    arg_classes = self._extract_class_names(item.args.kwarg.annotation)
                    if arg_classes:
                        param_types[item.args.kwarg.arg] = arg_classes

                if param_types:
                    cls_params[method_name] = param_types

            if cls_returns:
                self.return_types[cls_name] = cls_returns
            if cls_params:
                self.param_types[cls_name] = cls_params

        logger.info(
            "build_type_registry: extracted return types for %d classes, param types for %d classes",
            len(self.return_types),
            len(self.param_types),
        )

    def resolve_type(self, class_name: str, attr_name: str) -> set[str]:
        """
        Given a class and an attribute access, return the set of class names in the attribute's return type annotation.

        Walks the inheritance chain (class + all ancestors) to find the attribute.

        """
        for cn in (class_name, *self._get_mro(class_name)):
            cls_returns = self.return_types.get(cn, {})
            if attr_name in cls_returns:
                return cls_returns[attr_name]
        return set()

    def is_attr_async_on_type(self, type_names: set[str], attr_name: str) -> bool:
        """
        Check if attr_name would be an async method or promoted property on ANY of the given types.

        Returns True if at least one type in type_names has attr_name in its
        async_methods or promoted_properties (including inherited via ancestors).

        Also handles the polymorphic base-type case: if the declared type is a
        base class (e.g. ``GithubObject``) and the attribute is promoted on a
        subclass (e.g. ``CompletableGithubObject.raw_data``), we conservatively
        return True because the runtime object may be any subclass.

        """
        for type_name in type_names:
            # 0) Check if this type has a sync @property override of the attribute
            # AND no descendant promotes it to async.  If the declared type is a
            # base class, the runtime object may be a subclass that promotes it,
            # so we can only short-circuit when the type has no subclasses that
            # promote the attribute.  We defer this check: first scan ancestors
            # (fast path), then descendants.  The descendant walk will catch the
            # polymorphic case regardless.
            local_sync = self.property_methods.get(type_name, set())
            local_promoted = self.promoted_properties.get(type_name, set())
            has_sync_override = attr_name in local_sync and attr_name not in local_promoted

            # 1) Check ancestors (walk UP the MRO)
            # If the type itself has a sync override, ancestor promotion doesn't
            # apply (the subclass override wins).  Skip the upward walk.
            if not has_sync_override:
                for cn in (type_name, *self._get_mro(type_name)):
                    if attr_name in self.async_methods.get(cn, set()):
                        return True
                    if attr_name in self.promoted_properties.get(cn, set()):
                        return True

            # 2) Check descendants (walk DOWN the inheritance tree)
            # If the declared type is a base class, any concrete subclass
            # could be the runtime type (uses the reverse-inheritance map
            # built in parse_all).

            # BFS down from type_name through all descendants
            desc_visited: set[str] = set()
            desc_queue = [type_name]
            while desc_queue:
                cn = desc_queue.pop(0)
                if cn in desc_visited:
                    continue
                desc_visited.add(cn)
                if attr_name in self.async_methods.get(cn, set()):
                    logger.debug(
                        "is_attr_async_on_type: %s.%s found via descendant %s (async_method)",
                        type_name,
                        attr_name,
                        cn,
                    )
                    return True
                if attr_name in self.promoted_properties.get(cn, set()):
                    logger.debug(
                        "is_attr_async_on_type: %s.%s found via descendant %s (promoted_property)",
                        type_name,
                        attr_name,
                        cn,
                    )
                    return True
                desc_queue.extend(self._subclass_map.get(cn, set()))
        return False

    def get_all_method_var_types(self, class_name: str) -> dict[str, dict[str, set[str]]]:
        """
        Compute variable types for all methods in a class.

        Returns: method_name → {var_name → {type_names}}

        """
        class_node = self._get_class_node(class_name)
        if class_node is None:
            return {}
        result: dict[str, dict[str, set[str]]] = {}
        for item in class_node.body:
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                var_types = self._resolve_variable_types_in_method(class_name, item)
                if var_types:
                    result[item.name] = var_types
        return result

    def _resolve_variable_types_in_method(
        self, cls_name: str, method_node: ast.FunctionDef | ast.AsyncFunctionDef
    ) -> dict[str, set[str]]:
        """
        Resolve types of local variables and parameters in a method body.

        Returns a dict: variable_name -> set of class names.
        Sources of type info:
          1. Parameter annotations (from self.param_types)
          2. Local assignments where RHS is a call/attribute on a typed expression
          3. For-loop targets (``for x in iterable`` propagates iterable's element types)
          4. Comprehension targets (generator/list/set/dict comprehensions)
          5. isinstance narrowing (``isinstance(x, SomeClass)`` narrows x to SomeClass)
          6. Constructor calls (``var = ClassName(...)`` infers var as ClassName)

        """
        var_types: dict[str, set[str]] = {}

        # 1. Parameter types from annotations
        method_name = method_node.name
        cls_params = self.param_types.get(cls_name, {})
        if method_name in cls_params:
            for param_name, param_classes in cls_params[method_name].items():
                var_types[param_name] = set(param_classes)

        # 2-6. Walk the method body to find assignments, for-loops, comprehensions, isinstance
        for stmt in ast.walk(method_node):
            if isinstance(stmt, ast.Assign):
                # Simple case: var = self.method(...) or var = self.property
                for target in stmt.targets:
                    if isinstance(target, ast.Name):
                        inferred = self._infer_expr_type(cls_name, stmt.value, var_types)
                        if inferred:
                            var_types[target.id] = inferred
            elif isinstance(stmt, ast.AnnAssign) and stmt.target and isinstance(stmt.target, ast.Name):
                # Annotated assignment: var: Type = expr
                if stmt.annotation:
                    ann_types = self._extract_class_names(stmt.annotation)
                    if ann_types:
                        var_types[stmt.target.id] = ann_types

            # 3. For-loop targets: ``for var in iterable``
            # The element types of the iterable are the types of ``var``.
            # Since _extract_class_names already unwraps list[X], PaginatedList[X], etc.,
            # the param_types for the iterable already contain the element class names.
            elif isinstance(stmt, ast.For):
                if isinstance(stmt.target, ast.Name):
                    iter_types = self._infer_expr_type(cls_name, stmt.iter, var_types)
                    if not iter_types:
                        # Fall back: if the iterable is a known variable, use its types
                        if isinstance(stmt.iter, ast.Name):
                            iter_types = var_types.get(stmt.iter.id, set())
                    if iter_types:
                        var_types[stmt.target.id] = iter_types

            # 5. isinstance narrowing: ``isinstance(var, ClassName)``
            # In an if-branch guarded by isinstance, narrow the var type.
            # We ALSO add the narrowed types to the variable's overall type set,
            # so that cross-object detection can find accesses on the narrowed type
            # anywhere in the method (conservative: the var COULD be that type).
            elif isinstance(stmt, ast.If):
                isinstance_types = self._extract_isinstance_narrowing(stmt.test)
                for var_name, narrowed_types in isinstance_types.items():
                    # Only add domain types that we know about
                    domain_types = {t for t in narrowed_types if t in self.class_to_file}
                    if domain_types:
                        # Add to the variable's type set (union)
                        if var_name in var_types:
                            var_types[var_name] = var_types[var_name] | domain_types
                        else:
                            var_types[var_name] = domain_types
                        # Walk the if-body to find assignments that use the narrowed type
                        for body_stmt in ast.walk(stmt):
                            if isinstance(body_stmt, ast.Assign):
                                for target in body_stmt.targets:
                                    if isinstance(target, ast.Name):
                                        inferred = self._infer_expr_type(
                                            cls_name, body_stmt.value, {**var_types, var_name: domain_types}
                                        )
                                        if inferred:
                                            var_types[target.id] = inferred

        # Handle comprehension targets (generator, list, set, dict comprehensions)
        # These appear as ast.comprehension nodes inside ListComp, SetComp, GeneratorExp, DictComp
        for node in ast.walk(method_node):
            if isinstance(node, ast.comprehension):
                if isinstance(node.target, ast.Name):
                    iter_types = self._infer_expr_type(cls_name, node.iter, var_types)
                    if not iter_types:
                        if isinstance(node.iter, ast.Name):
                            iter_types = var_types.get(node.iter.id, set())
                    if iter_types:
                        var_types[node.target.id] = iter_types

        # Also add 'self' -> cls_name
        var_types["self"] = {cls_name}

        return var_types

    @staticmethod
    def _extract_isinstance_narrowing(test_node: ast.expr) -> dict[str, set[str]]:
        """
        Extract isinstance narrowing from a conditional test.

        For ``isinstance(var, ClassName)`` returns {var: {ClassName}}.
        For ``isinstance(var, (A, B))`` returns {var: {A, B}}.
        For ``isinstance(var, module.ClassName)`` extracts the class name.
        Returns empty dict if not an isinstance call.

        """
        result: dict[str, set[str]] = {}
        if not isinstance(test_node, ast.Call):
            return result
        if not isinstance(test_node.func, ast.Name) or test_node.func.id != "isinstance":
            return result
        if len(test_node.args) < 2:
            return result
        var_node = test_node.args[0]
        type_node = test_node.args[1]

        if not isinstance(var_node, ast.Name):
            return result

        var_name = var_node.id
        type_names: set[str] = set()

        def _extract_type_name(n: ast.expr) -> str | None:
            if isinstance(n, ast.Name):
                return n.id
            if isinstance(n, ast.Attribute):
                # module.ClassName -> ClassName
                return n.attr
            return None

        if isinstance(type_node, ast.Tuple):
            for elt in type_node.elts:
                name = _extract_type_name(elt)
                if name:
                    type_names.add(name)
        else:
            name = _extract_type_name(type_node)
            if name:
                type_names.add(name)

        if type_names:
            result[var_name] = type_names
        return result

    def _infer_expr_type(self, cls_name: str, expr: ast.expr, known_vars: dict[str, set[str]]) -> set[str]:
        """
        Infer the set of class names an expression evaluates to.

        Handles:
          - self.method(...) → return type of method on cls_name
          - self.property → return type of property on cls_name
          - var.method(...) → return type if var's type is known
          - var.property → return type if var's type is known
          - ClassName(...) → constructor call, infers ClassName
          - module.ClassName(...) → constructor call, infers ClassName

        """
        if isinstance(expr, ast.Call):
            # Check if it's a constructor call: ClassName(...) or module.ClassName(...)
            func = expr.func
            if isinstance(func, ast.Name):
                # ClassName(...) — if ClassName is a known class, the type is ClassName
                if func.id in self.class_to_file:
                    return {func.id}
            elif isinstance(func, ast.Attribute):
                # module.ClassName(...) — if ClassName is a known class
                if func.attr in self.class_to_file:
                    return {func.attr}
            # Otherwise, func(...) → resolve func's return type
            return self._infer_expr_type(cls_name, expr.func, known_vars)

        if isinstance(expr, ast.Attribute):
            # obj.attr → resolve obj type, then look up attr's return type
            obj_types = self._infer_expr_type(cls_name, expr.value, known_vars)
            if not obj_types:
                return set()
            # Look up attr's return type on any of the resolved types
            result: set[str] = set()
            for ot in obj_types:
                result |= self.resolve_type(ot, expr.attr)
            return result

        if isinstance(expr, ast.Name):
            if expr.id == "self":
                return {cls_name}
            return known_vars.get(expr.id, set())

        return set()

    def _method_has_cross_object_async(
        self, cls_name: str, method_node: ast.FunctionDef | ast.AsyncFunctionDef
    ) -> str | None:
        """
        Check if a method body contains cross-object async accesses.

        Returns a reason string if cross-object async is detected, None otherwise.

        """
        var_types = self._resolve_variable_types_in_method(cls_name, method_node)

        for node in ast.walk(method_node):
            # Check attribute access: expr.attr
            if isinstance(node, ast.Attribute):
                # Skip self.attr — handled by existing passes
                if isinstance(node.value, ast.Name) and node.value.id == "self":
                    continue

                # Resolve the type of the object being accessed
                obj_types = self._infer_obj_types(node.value, cls_name, var_types)
                if not obj_types:
                    continue

                attr_name = node.attr
                # Check if this attribute is async on any of the resolved types
                if self.is_attr_async_on_type(obj_types, attr_name):
                    # Build a readable reason
                    if isinstance(node.value, ast.Name):
                        return "cross-object: {}.{} (type {})".format(
                            node.value.id,
                            attr_name,
                            obj_types,
                        )
                    else:
                        return f"cross-object: *.{attr_name} (type {obj_types})"

        return None

    def _infer_obj_types(self, expr: ast.expr, cls_name: str, var_types: dict[str, set[str]]) -> set[str]:
        """
        Infer the set of class names for an expression (for cross-object detection).

        Handles:
          - Name('var') → look up in var_types
          - Attribute(Name('self'), 'prop') → return type of self.prop
          - Attribute(expr, 'attr') → resolve expr type, look up attr's return type
          - Call(func, ...) → resolve func's return type

        """
        if isinstance(expr, ast.Name):
            if expr.id == "self":
                return {cls_name}
            return var_types.get(expr.id, set())

        if isinstance(expr, ast.Attribute):
            # Recursively resolve the object type, then look up the attribute
            obj_types = self._infer_obj_types(expr.value, cls_name, var_types)
            if not obj_types:
                return set()
            result: set[str] = set()
            for ot in obj_types:
                result |= self.resolve_type(ot, expr.attr)
            return result

        if isinstance(expr, ast.Call):
            # func(...) → the return type of the function
            return self._infer_obj_types(expr.func, cls_name, var_types)

        return set()

    def compute_cross_object_rules_per_method(
        self, cls_name: str
    ) -> dict[str, tuple[dict[str, set[str]], dict[str, set[str]]]]:
        """
        Compute per-method type-registry-based cross-object await rules.

        Returns a dict mapping method_name to (prop_rules, method_rules). This avoids variable-name collisions across
        methods (e.g. 'element' being a CompletableGithubObject in one method but a plain class in another).

        """
        result: dict[str, tuple[dict[str, set[str]], dict[str, set[str]]]] = {}

        cls_node = self._get_class_node(cls_name)
        if cls_node is None:
            return result

        for item in ast.iter_child_nodes(cls_node):
            if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            # Only process methods that are async (otherwise no await needed)
            if item.name not in self.async_methods.get(cls_name, set()):
                continue

            prop_rules: dict[str, set[str]] = {}
            method_rules: dict[str, set[str]] = {}

            var_types = self._resolve_variable_types_in_method(cls_name, item)

            for node in ast.walk(item):
                if not isinstance(node, ast.Attribute):
                    continue
                # Skip self.attr — handled by existing passes
                if isinstance(node.value, ast.Name) and node.value.id == "self":
                    continue
                # Only process simple variable access: var.attr
                if not isinstance(node.value, ast.Name):
                    continue
                var_name = node.value.id
                attr_name = node.attr

                obj_types = var_types.get(var_name, set())
                if not obj_types:
                    continue

                if self.is_attr_async_on_type(obj_types, attr_name):
                    is_call = False
                    for parent_node in ast.walk(item):
                        if isinstance(parent_node, ast.Call) and parent_node.func is node:
                            is_call = True
                            break

                    if is_call:
                        method_rules.setdefault(attr_name, set()).add(var_name)
                    else:
                        prop_rules.setdefault(attr_name, set()).add(var_name)

            if prop_rules or method_rules:
                result[item.name] = (prop_rules, method_rules)

        return result

    def seed_io_classes(self):
        """
        Seed the async class set with the I/O root classes (IO_ROOT_CLASSES).
        """
        for cls_name in sorted(IO_ROOT_CLASSES):
            if cls_name in self.class_to_file:
                self.async_classes.add(cls_name)
                logger.debug("seed_io_classes: seeded I/O root '%s'", cls_name)
            else:
                logger.debug("seed_io_classes: I/O root '%s' not in parsed sources, skipping", cls_name)

    def propagate_async_classes(self):
        """
        Iteratively find classes that need async (hold Requester or inherit from async class).
        """
        # First, mark any class whose source references self._requester or self.__requester.
        # This must run BEFORE inheritance propagation so that e.g. CompletableGithubObject
        # is already marked, allowing subclasses like SourceImport to be detected.
        for stem, src in self.sources.items():
            for node in ast.walk(self.trees.get(stem, ast.Module(body=[], type_ignores=[]))):
                if isinstance(node, ast.ClassDef):
                    cls_src = ast.get_source_segment(src, node)
                    if cls_src and ("_requester" in cls_src or "__requester" in cls_src):
                        if node.name not in self.async_classes:
                            self.async_classes.add(node.name)
                            logger.debug("propagate: marking '%s' async (references _requester)", node.name)

        # Then propagate: classes that inherit from async classes also need async.
        changed = True
        pass_num = 0
        while changed:
            changed = False
            pass_num += 1
            logger.debug("propagate: inheritance pass #%d", pass_num)
            for cls_name, bases in self.class_bases.items():
                if cls_name in self.async_classes:
                    continue
                for base in bases:
                    if base in NON_PROPAGATING_BASES:
                        # Deliberately shared classes (e.g. the Auth hierarchy via
                        # WithRequester) are consumed by both stacks — never transformed.
                        continue
                    if base in self.async_classes:
                        self.async_classes.add(cls_name)
                        logger.debug("propagate: marking '%s' async (inherits from '%s')", cls_name, base)
                        changed = True
                        break

    def analyze_methods(self):
        """
        Find all methods in async classes that need to become async.
        """
        # First pass: methods that directly call requester methods (IO_METHOD_PATTERNS) or time.sleep
        # Pre-compile I/O method patterns
        io_method_res = {p: re.compile(rf"\.{re.escape(p)}\s*\(") for p in IO_METHOD_PATTERNS}

        for cls_name in self.async_classes:
            cls_node = self._get_class_node(cls_name)
            if cls_node is None:
                continue
            methods_needing_async = set()

            # Build set of ALL property names for this class.
            # After the main analysis, we'll determine which properties need to
            # stay sync (simple properties) vs. which need to become async (I/O properties).
            all_property_methods: set[str] = set()
            for item in ast.walk(cls_node):
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    for deco in item.decorator_list:
                        deco_name = ""
                        if isinstance(deco, ast.Name):
                            deco_name = deco.id
                        elif isinstance(deco, ast.Attribute):
                            deco_name = deco.attr
                        if deco_name == "property":
                            all_property_methods.add(item.name)
                            break

            # Temporarily store all properties — we'll split them after the transitive pass
            self.property_methods[cls_name] = all_property_methods

            for item in ast.walk(cls_node):
                if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                method_name = item.name

                # NEVER make __init__ and other special methods async
                if method_name in NEVER_ASYNC_METHODS:
                    continue

                # NEVER make @property methods async in the first pass.
                # After the transitive pass, we'll check which properties need to be
                # async (those calling async methods) and re-add them.
                if method_name in all_property_methods:
                    continue

                method_src = self._get_method_src(cls_name, method_name, item)

                needs_async = False

                # Direct I/O calls - must be actual method calls (preceded by '.')
                for pattern_str, pattern_re in io_method_res.items():
                    if pattern_str in method_src and pattern_re.search(method_src):
                        needs_async = True
                        break

                # time.sleep
                if "time.sleep(" in method_src:
                    needs_async = True

                # Private Requester I/O-chain methods (REQUESTER_PRIVATE_IO)
                if cls_name == "Requester":
                    if method_name in REQUESTER_PRIVATE_IO:
                        needs_async = True

                    # Also check for name-mangled calls to these methods
                    for priv in sorted(REQUESTER_PRIVATE_IO):
                        mangled = f"_Requester{priv}"
                        if mangled in method_src and self._search(rf"self\.{re.escape(mangled)}\s*\(", method_src):
                            needs_async = True
                            break
                        if priv in method_src and self._search(rf"self\.{re.escape(priv)}\s*\(", method_src):
                            needs_async = True
                            break
                    # The actual I/O method
                    if "self.session" in method_src and any(verb in method_src for verb in HTTP_SESSION_VERBS):
                        needs_async = True

                # Session methods on connection classes
                if cls_name in CONNECTION_CLASSES:
                    if "self.session" in method_src:
                        needs_async = True

                # close() methods that close the requester/connection
                if method_name == "close" and any(x in method_src for x in CLOSE_OWNER_PATTERNS):
                    needs_async = True

                if needs_async:
                    methods_needing_async.add(method_name)

            self.async_methods[cls_name] = methods_needing_async
            if methods_needing_async:
                logger.debug("analyze[pass1] %s: direct I/O methods %s", cls_name, sorted(methods_needing_async))

        # Outer loop: passes 2-4 + cross-object detection iterate until stable.
        # Cross-object detection needs promoted_properties (populated in pass 3),
        # so it runs after pass 4.  If it adds new methods, passes 2-4 re-run.
        outer_changed = True
        outer_iter = 0
        while outer_changed:
            outer_changed = False
            outer_iter += 1
            logger.debug("analyze: outer iteration #%d", outer_iter)

            # Second pass: transitive - methods calling other async methods
            changed = True
            pass2_num = 0
            while changed:
                changed = False
                pass2_num += 1
                logger.debug("analyze[pass2]: transitive closure pass #%d", pass2_num)
                for cls_name in self.async_classes:
                    cls_node = self._get_class_node(cls_name)
                    if cls_node is None:
                        continue
                    current = self.async_methods.get(cls_name, set())
                    cls_properties = self.property_methods.get(cls_name, set())

                    # Gather inherited async methods from parent classes for super() detection
                    inherited_async = self._get_inherited_async(cls_name)
                    # Async methods on DESCENDANT classes: a base-class method calling
                    # self.M() may dispatch to an async override at runtime.
                    descendant_async = self._get_descendant_async(cls_name)

                    for item in ast.walk(cls_node):
                        if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            continue
                        if item.name in current:
                            continue
                        # NEVER make __init__ and other special methods async
                        if item.name in NEVER_ASYNC_METHODS:
                            continue
                        # NEVER make @property methods async
                        if item.name in cls_properties:
                            continue
                        # Signature consistency: if a DESCENDANT overrides this method
                        # as async, the base declaration must be async too.
                        if item.name in descendant_async:
                            current.add(item.name)
                            logger.debug("analyze[pass2] %s.%s: async override on a descendant", cls_name, item.name)
                            changed = True
                            continue
                        method_src = self._get_method_src(cls_name, item.name, item)
                        # Check for self.method( calls to async methods, including methods
                        # INHERITED from ancestors (e.g. Repository.edit calling
                        # self._completeIfNotSet defined on CompletableGithubObject) and
                        # methods whose async override lives on a DESCENDANT (virtual dispatch).
                        for async_method in list(current) + sorted((inherited_async | descendant_async) - current):
                            # Check for self.method( or self.__method( or self._method(
                            # Fast pre-check: method name must appear in source
                            if async_method in method_src and self._search(
                                rf"self\.(?:_\w+)?{re.escape(async_method)}\s*\(", method_src
                            ):
                                current.add(item.name)
                                logger.debug(
                                    "analyze[pass2] %s.%s: calls async method '%s'", cls_name, item.name, async_method
                                )
                                changed = True
                                break
                        if item.name in current:
                            continue
                        # Also check for super().method( calls to inherited async methods
                        if "super()" in method_src:
                            for async_method in inherited_async:
                                if async_method in method_src and self._search(
                                    rf"super\(\)\.{re.escape(async_method)}\s*\(", method_src
                                ):
                                    current.add(item.name)
                                    logger.debug(
                                        "analyze[pass2] %s.%s: calls inherited async method via super().%s()",
                                        cls_name,
                                        item.name,
                                        async_method,
                                    )
                                    changed = True
                                    break
                        if item.name in current:
                            continue
                        # Check for inline construction patterns: ClassName(...).async_method(...)
                        # E.g. GithubIntegration(**self.__requester.kwargs).get_app()
                        # If ClassName has async_method, the caller must also be async.
                        for other_cls in self.async_classes:
                            # Fast pre-check: class name must appear in source
                            if other_cls not in method_src:
                                continue
                            other_async = self.async_methods.get(other_cls, set())
                            for async_method in other_async:
                                if async_method in NEVER_ASYNC_METHODS:
                                    continue
                                # Fast pre-check: method name must appear in source
                                if async_method not in method_src:
                                    continue
                                if self._search(
                                    rf"\b{re.escape(other_cls)}\s*\([^)]*\)\.{re.escape(async_method)}\s*\(",
                                    method_src,
                                ):
                                    current.add(item.name)
                                    logger.debug(
                                        "analyze[pass2] %s.%s: calls %s(...).%s() (inline construction)",
                                        cls_name,
                                        item.name,
                                        other_cls,
                                        async_method,
                                    )
                                    changed = True
                                    break
                            if item.name in current:
                                break

                    self.async_methods[cls_name] = current

            # Remove any NEVER_ASYNC_METHODS that somehow got added
            for cls_name in self.async_methods:
                self.async_methods[cls_name] -= NEVER_ASYNC_METHODS

            # _completeIfNotSet and _completeIfNeeded STAY in async_methods.
            # They are genuinely async (they await __complete which does HTTP I/O).
            # Properties that call them will be promoted to async in the third pass,
            # which is correct: callers must `await obj.name` to access attributes.

            # Third pass: property re-check.
            # Now that we know ALL async methods (after transitive closure),
            # re-examine each @property.  If its body calls an async method
            # or a direct I/O pattern, it MUST be async too (not a simple
            # cached-value property).  Promote it to async_methods and remove
            # from property_methods so it gets the `async def` treatment.
            # We loop until no more promotions happen (transitive closure for property-calls-property).
            io_method_patterns_re = "|".join(re.escape(p) for p in IO_METHOD_PATTERNS)
            io_method_combined_re = re.compile(rf"\.(?:{io_method_patterns_re})\s*\(")
            prop_changed = True
            pass3_num = 0
            while prop_changed:
                prop_changed = False
                pass3_num += 1
                logger.debug("analyze[pass3]: property promotion pass #%d", pass3_num)
                for cls_name in list(self.async_methods):
                    cls_node = self._get_class_node(cls_name)
                    if cls_node is None:
                        continue
                    current_async = set(self.async_methods[cls_name])
                    # Include inherited async methods from ALL ancestor classes (full MRO)
                    current_async |= self._get_inherited_async(cls_name)

                    # Also gather promoted properties (async properties accessed without parens)
                    current_promoted = set(self.promoted_properties.get(cls_name, set()))
                    current_promoted |= self._get_inherited_promoted(cls_name)

                    props = self.property_methods.get(cls_name, set())
                    promote = set()
                    for item in ast.walk(cls_node):
                        if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            continue
                        if item.name not in props:
                            continue
                        method_src = self._get_method_src(cls_name, item.name, item)
                        # Check 1: does this property call any known async method?
                        for am in current_async:
                            if am in method_src and self._search(rf"self\.(?:_\w+)?{re.escape(am)}\s*\(", method_src):
                                promote.add(item.name)
                                logger.debug(
                                    "analyze[pass3] %s.%s: promoting @property (calls async method '%s')",
                                    cls_name,
                                    item.name,
                                    am,
                                )
                                break
                        if item.name in promote:
                            continue
                        # Check 1b: does this property call an inherited async method via super()?
                        if "super()" in method_src:
                            for am in current_async:
                                if am in method_src and self._search(rf"super\(\)\.{re.escape(am)}\s*\(", method_src):
                                    promote.add(item.name)
                                    logger.debug(
                                        "analyze[pass3] %s.%s: promoting @property (calls super().%s())",
                                        cls_name,
                                        item.name,
                                        am,
                                    )
                                    break
                        if item.name in promote:
                            continue
                        # Check 2: does this property call a direct I/O pattern?
                        if io_method_combined_re.search(method_src):
                            promote.add(item.name)
                            logger.debug(
                                "analyze[pass3] %s.%s: promoting @property (direct I/O pattern)", cls_name, item.name
                            )
                            continue
                        # Check 3: does this property ACCESS another promoted async property
                        # (without parentheses)? e.g. `return self.login` where `login` is async
                        for pp in current_promoted:
                            # Match self.prop NOT followed by ( — it's a property access
                            if pp in method_src and self._search(rf"self\.{re.escape(pp)}(?!\s*\()(?!\w)", method_src):
                                promote.add(item.name)
                                logger.debug(
                                    "analyze[pass3] %s.%s: promoting @property (accesses promoted property '%s')",
                                    cls_name,
                                    item.name,
                                    pp,
                                )
                                break
                        if item.name in promote:
                            continue
                        # Check 3b: does this property ACCESS a promoted property via super()?
                        # e.g. `return super().node_id` where parent's node_id is async
                        if "super()" in method_src:
                            for pp in current_promoted:
                                if pp in method_src and self._search(
                                    rf"super\(\)\.{re.escape(pp)}(?!\s*\()(?!\w)", method_src
                                ):
                                    promote.add(item.name)
                                    logger.debug(
                                        "analyze[pass3] %s.%s: promoting @property (accesses super().%s)",
                                        cls_name,
                                        item.name,
                                        pp,
                                    )
                                    break
                    if promote:
                        self.async_methods[cls_name] |= promote
                        self.property_methods[cls_name] -= promote
                        self.promoted_properties.setdefault(cls_name, set()).update(promote)
                        prop_changed = True

            # Fourth pass: promote regular methods that ACCESS promoted properties
            # OR that call newly-async methods. Unified transitive closure.
            # e.g. get_repo() has `self.login` in a string — login is an async
            # property, so get_repo must be async too to await it.
            # Also handles: method B calls method A which was just promoted — B must be async too.
            fourth_changed = True
            pass4_num = 0
            while fourth_changed:
                fourth_changed = False
                pass4_num += 1
                logger.debug("analyze[pass4]: transitive method promotion pass #%d", pass4_num)
                for cls_name in list(self.async_methods):
                    cls_node = self._get_class_node(cls_name)
                    if cls_node is None:
                        continue

                    # Gather async methods from this class + all ancestors (full MRO)
                    current_async = set(self.async_methods.get(cls_name, set()))
                    current_async |= self._get_inherited_async(cls_name)

                    cls_properties = self.property_methods.get(cls_name, set())

                    # Gather promoted properties from this class + all ancestors (full MRO)
                    all_promoted = set(self.promoted_properties.get(cls_name, set()))
                    all_promoted |= self._get_inherited_promoted(cls_name)

                    promote_methods = set()
                    for item in ast.walk(cls_node):
                        if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            continue
                        if item.name in current_async:
                            continue
                        if item.name in cls_properties:
                            continue
                        if item.name in NEVER_ASYNC_METHODS:
                            continue
                        method_src = self._get_method_src(cls_name, item.name, item)
                        found = False
                        found_reason = ""
                        # Check A: accesses a promoted async property via self
                        for pp in all_promoted:
                            if pp in method_src and self._search(rf"self\.{re.escape(pp)}(?!\s*\()(?!\w)", method_src):
                                found = True
                                found_reason = "accesses promoted property '%s'" % pp
                                break
                        # Check A2: accesses a promoted async property via super()
                        if not found and "super()" in method_src:
                            for pp in all_promoted:
                                if pp in method_src and self._search(
                                    rf"super\(\)\.{re.escape(pp)}(?!\s*\()(?!\w)", method_src
                                ):
                                    found = True
                                    found_reason = "accesses promoted property via super().%s" % pp
                                    break
                        # Check B: calls an async method via self
                        if not found:
                            for am in current_async:
                                if am in method_src and self._search(
                                    rf"self\.(?:_\w+)?{re.escape(am)}\s*\(", method_src
                                ):
                                    found = True
                                    found_reason = "calls async method '%s'" % am
                                    break
                        # Check B2: calls an async method via super()
                        if not found and "super()" in method_src:
                            for am in current_async:
                                if am in method_src and self._search(rf"super\(\)\.{re.escape(am)}\s*\(", method_src):
                                    found = True
                                    found_reason = "calls async method via super().%s()" % am
                                    break
                        if found:
                            promote_methods.add(item.name)
                            logger.debug(
                                "analyze[pass4] %s.%s: promoting method (%s)",
                                cls_name,
                                item.name,
                                found_reason,
                            )

                    if promote_methods:
                        self.async_methods[cls_name] |= promote_methods
                        fourth_changed = True

            # Cross-object detection (pass 5): find methods that access async
            # methods / promoted properties on OTHER objects (not self).
            # This runs AFTER passes 2-4 so that promoted_properties is populated.
            # We also check properties for cross-object access (e.g. PaginatedList.reversed).
            cross_object_count = 0
            for cls_name in list(self.async_classes):
                cls_node = self._get_class_node(cls_name)
                if cls_node is None:
                    continue
                current = self.async_methods.get(cls_name, set())
                cls_properties = self.property_methods.get(cls_name, set())
                for item in ast.iter_child_nodes(cls_node):
                    if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        continue
                    if item.name in current:
                        continue
                    if item.name in NEVER_ASYNC_METHODS:
                        continue
                    reason = self._method_has_cross_object_async(cls_name, item)
                    if reason:
                        current.add(item.name)
                        cross_object_count += 1
                        logger.debug(
                            "analyze[cross-object] %s.%s: %s",
                            cls_name,
                            item.name,
                            reason,
                        )
                        # If this was a @property, promote it
                        if item.name in cls_properties:
                            cls_properties.discard(item.name)
                            self.property_methods[cls_name].discard(item.name)
                            self.promoted_properties.setdefault(cls_name, set()).add(item.name)
                            logger.debug(
                                "analyze[cross-object] %s.%s: promoted @property",
                                cls_name,
                                item.name,
                            )
                self.async_methods[cls_name] = current
            if cross_object_count:
                logger.info(
                    "analyze[cross-object]: found %d methods, re-running passes 2-4",
                    cross_object_count,
                )
                outer_changed = True
            else:
                logger.debug("analyze[cross-object]: no new methods found")

        # Ensure any async method that is also in property_methods
        # gets removed from property_methods (it needs async def, not @property def).
        for cls_name in list(self.async_methods):
            props = self.property_methods.get(cls_name, set())
            overlap = props & self.async_methods.get(cls_name, set())
            if overlap:
                logger.debug(
                    "analyze: async/property cleanup %s: removing %s from property_methods",
                    cls_name,
                    sorted(overlap),
                )
                self.property_methods[cls_name] -= overlap
                # Also track these as promoted properties
                self.promoted_properties.setdefault(cls_name, set()).update(overlap)

    def entry_point_classes(self) -> list[tuple[str, str]]:
        """
        Classes that construct their own Requester, the user-facing entry points.

        These are the classes tests instantiate directly to talk to the API (e.g. Github, GithubIntegration), so test
        imports of them must be rewritten to the async package. Returns sorted (module_stem, class_name) pairs.

        """
        result = []
        for cls_name in sorted(self.async_classes):
            stem = self.class_to_file.get(cls_name)
            node = self._get_class_node(cls_name)
            if stem is None or node is None:
                continue
            cls_src = ast.get_source_segment(self.sources.get(stem, ""), node) or ""
            if self._search(r"=\s*Requester\(", cls_src):
                result.append((stem, cls_name))
        return result

    def async_static_methods(self) -> list[tuple[str, str, str]]:
        """
        Static/class methods that became async.

        Sync test bodies calling these get a coroutine back, so calls must be bridged through the event loop. Returns
        sorted (module_stem, class_name, method_name) triples.

        """
        result = []
        for cls_name, statics in sorted(self.static_methods.items()):
            stem = self.class_to_file.get(cls_name)
            if stem is None:
                continue
            for m in sorted(statics & self.async_methods.get(cls_name, set())):
                result.append((stem, cls_name, m))
        return result

    def run(self):
        self.parse_all()
        self.build_type_registry()
        self.seed_io_classes()
        self.propagate_async_classes()
        self.analyze_methods()


class AsyncTransformer:
    """
    Transforms sync source files into async counterparts.
    """

    def __init__(self, analyzer: IOAnalyzer):
        self.analyzer = analyzer

    @staticmethod
    def _prepend_import(src: str, import_line: str) -> str:
        """
        Insert a top-level import statement as early as possible in the file.

        `from __future__ import annotations` must be the first statement in the file (only
        a docstring/comments may precede it), and by the time this runs `src` already
        contains the original file's own future-import further down (e.g. after a copyright
        header). Inserting right after it — rather than unconditionally prepending — avoids
        producing a SyntaxError.

        """
        future_import = re.search(r"^from __future__ import annotations\n", src, re.MULTILINE)
        if future_import:
            insert_at = future_import.end()
            return src[:insert_at] + import_line + src[insert_at:]
        return import_line + src

    @staticmethod
    def _code_only(src: str) -> str:
        """
        Blank out every string literal (docstrings and f-string text too) and comment in `src`.

        A textual search on the result only sees real code; f-string replacement fields stay. Falls back to `src` if
        it doesn't tokenize.

        """
        lines = src.splitlines(keepends=True)
        offsets = [0]
        for line in lines:
            offsets.append(offsets[-1] + len(line))
        blank_types = {tokenize.STRING, tokenize.COMMENT, getattr(tokenize, "FSTRING_MIDDLE", tokenize.STRING)}
        chars = list(src)
        try:
            for tok in tokenize.generate_tokens(iter(lines).__next__):
                if tok.type in blank_types:
                    start = offsets[tok.start[0] - 1] + tok.start[1]
                    end = offsets[tok.end[0] - 1] + tok.end[1]
                    for i in range(start, end):
                        if chars[i] != "\n":
                            chars[i] = " "
        except (tokenize.TokenError, SyntaxError, IndentationError):
            return src
        return "".join(chars)

    @staticmethod
    def _sub_outside_docstrings(pattern: str, repl: str, src: str) -> tuple[str, bool]:
        """
        Apply re.sub(pattern, repl) to `src`, skipping any line that is inside — or is itself a delimiter of — a
        triple-quoted docstring.

        A class name can appear in prose (e.g. a Sphinx :meth: cross-reference naming
        another class) without being actual code usage. Rewriting such a mention and,
        worse, treating it as "the class is used here" (which callers use to decide
        whether to add an import) can introduce a spurious import — and in a tightly-
        coupled module graph, a spurious import can create a genuine circular import.
        Lines carrying a triple-quote delimiter are skipped entirely (conservative: this
        can under-rewrite a line that happens to share a line with a delimiter, but never
        over-rewrites prose).

        Returns (new_src, matched) where `matched` is True only if the pattern matched
        outside a docstring.

        """
        compiled = re.compile(pattern)
        lines = src.split("\n")
        in_docstring = False
        matched = False
        out_lines = []
        for line in lines:
            tq_count = line.count('"""') + line.count("'''")
            if in_docstring:
                out_lines.append(line)
                if tq_count % 2 == 1:
                    in_docstring = False
                continue
            if tq_count:
                out_lines.append(line)
                if tq_count % 2 == 1:
                    in_docstring = True
                continue
            new_line, n = compiled.subn(repl, line)
            if n:
                matched = True
            out_lines.append(new_line)
        return "\n".join(out_lines), matched

    def transform_file(self, stem: str, src: str) -> str:
        """
        Apply async transformations to a source file.
        """
        logger.debug("transform[%s]: begin 17-step pipeline", stem)
        lines = src

        # 1) Add auto-generated header
        lines = AUTO_HEADER + lines
        logger.debug("transform[%s]: step 1 — added auto-generated header", stem)

        # 2) Fix imports: github.X -> githubasyncio.X for local modules
        lines = self._fix_imports(lines, stem)
        logger.debug("transform[%s]: step 2 — fixed imports", stem)

        # 2.5) Fix double-dereference patterns where `from .X import X` (class)
        # collides with body usage of `X.X(...)` or `X.Attr`.
        lines = self._fix_double_dereference(lines)
        logger.debug("transform[%s]: step 2.5 — fixed double-dereference patterns", stem)

        # 2a) Fix the module/class alias problem for shadowed SKIP modules.
        # In Python, `import github.M as M` resolves via getattr(github, 'M'), which
        # returns the CLASS (not the module) when github/__init__.py does
        # `from .M import M`.  The sync code works because it is loaded during
        # __init__.py execution (before the shadowing line runs); the async code is
        # loaded after __init__.py completes, so the alias gets the class.
        # Fix: use sys.modules to get the module (currently applies to GithubException).
        lines = self._fix_shadowed_module_alias(lines)
        logger.debug("transform[%s]: step 2a — fixed shadowed module/class aliases", stem)

        # 2b) Move class-body from-imports to TYPE_CHECKING
        lines = self._move_class_body_imports(lines)
        logger.debug("transform[%s]: step 2b — moved class-body imports to TYPE_CHECKING", stem)

        # 2c) Deduplicate runtime imports that bind the same name twice (F811)
        lines = self._dedup_runtime_imports(lines)
        logger.debug("transform[%s]: step 2c — deduplicated runtime imports (F811 fix)", stem)

        # 3) For classes in this file, apply method-level transformations
        for node in ast.walk(self.analyzer.trees.get(stem, ast.Module(body=[], type_ignores=[]))):
            if isinstance(node, ast.ClassDef) and node.name in self.analyzer.async_classes:
                logger.debug("transform[%s]: step 3 — transforming class %s", stem, node.name)
                lines = self._transform_class(lines, node.name, stem)

        # 4) threading.Lock -> asyncio.Lock
        lines = lines.replace("threading.Lock()", "asyncio.Lock()")
        if "threading.Lock" in lines or "asyncio.Lock" in lines:
            if "import asyncio" not in lines:
                lines = self._prepend_import(lines, "import asyncio\n")
            # Remove threading import if no longer needed
            if "threading." not in lines.replace("asyncio.Lock", ""):
                lines = re.sub(r"^import threading\n", "", lines, flags=re.MULTILINE)
        logger.debug("transform[%s]: step 4 — threading.Lock → asyncio.Lock", stem)

        # 5) time.sleep -> await asyncio.sleep
        lines = re.sub(r"(?<!await\s)time\.sleep\(", "await asyncio.sleep(", lines)
        if "asyncio.sleep" in lines and "import asyncio" not in lines:
            lines = self._prepend_import(lines, "import asyncio\n")
        logger.debug("transform[%s]: step 5 — time.sleep → await asyncio.sleep", stem)

        # 6) HTTP library session: sync API -> async API (SESSION_REWRITES)
        for sync_api, async_api in SESSION_REWRITES.items():
            lines = lines.replace(sync_api, async_api)
        logger.debug("transform[%s]: step 6 — rewrote HTTP session APIs", stem)

        # 7) __enter__/__exit__ -> __aenter__/__aexit__
        lines = self._convert_context_managers(lines)
        logger.debug("transform[%s]: step 7 — converted context managers", stem)

        # 8) with self.__connection_lock: -> async with self.__connection_lock:
        lines = self._convert_with_to_async_with(lines)
        logger.debug("transform[%s]: step 8 — converted with → async with for locks", stem)

        # 9) Apply declarative surgery for modules whose async semantics differ
        # (iteration protocol, NotSet duality, __init__ completion — see PATCHES).
        lines = _apply_patches(stem, lines)
        logger.debug("transform[%s]: step 9 — applied declarative patches", stem)

        # 9b) `yield from` is a SyntaxError inside async generators — rewrite it
        # to an explicit element loop in every async def body (generic).
        lines = self._fix_yield_from_in_async_defs(lines)
        logger.debug("transform[%s]: step 9b — rewrote yield from in async defs", stem)

        # 11) Add close() await patterns
        lines = self._add_close_awaits(lines, stem)
        logger.debug("transform[%s]: step 11 — added close() awaits", stem)

        # 12/13) _fix_isinstance_dual_class/_fix_issubclass_dual_class exist but are never called
        # here: calling them would widen isinstance/issubclass checks against async-only classes
        # to also accept the classic sync class (e.g. `isinstance(auth, (githubasyncio.Auth.Auth,
        # github.Auth.Auth))`), letting a classic PyGithub object pass into the async client. Left
        # disabled: githubasyncio is meant to be self-contained (no runtime dependency on the
        # classic PyGithub package), and that `github.X.Y` half would be the only thing pulling it
        # back in. Callers need githubasyncio's own Auth/Repository/GithubObject instances, not
        # classic PyGithub ones.
        logger.debug("transform[%s]: steps 12/13 — dual sync/async isinstance/issubclass checks disabled", stem)

        # 14) Replace `X is NotSet` / `X is not NotSet` with is_undefined(X) / is_defined(X).
        # This handles cases where sync objects (with sync _NotSetType attributes) are
        # passed to async code which uses async NotSet. The is_undefined/is_defined
        # functions check both sync and async _NotSetType.
        # Skip GithubObject.py itself since it defines is_undefined/is_defined.
        if stem != "GithubObject":
            lines = self._replace_is_notset_with_helpers(lines)
            logger.debug("transform[%s]: step 14 — replaced is/is not NotSet with helpers", stem)

        # 15) Final: if the body still references `github.X` (e.g. from isinstance dual-class
        # patterns or non-async data classes), ensure `import github` is present.
        lines = self._ensure_import_github(lines)
        logger.debug("transform[%s]: step 15 — ensured import github", stem)

        # 16) Fix sync dunder methods (__repr__, __eq__, __hash__): they can't be async
        # but may reference async properties. Replace self.X with self._X.value.
        lines = self._fix_sync_dunder_methods(lines, stem)
        logger.debug("transform[%s]: step 16 — fixed sync dunder methods", stem)

        # 17) Fix async generators in str.join(): change (await x for x) to [await x for x]
        # In Python, `(await x for x in items)` creates an async generator which
        # str.join() cannot consume. A list comprehension `[await x for x in items]`
        # creates a proper list that join() can use.
        lines = self._fix_async_generator_in_join(lines)
        logger.debug("transform[%s]: step 17 — fixed async generators in str.join()", stem)

        return lines

    @staticmethod
    def _fix_shadowed_module_alias(lines: str) -> str:
        """
        Fix ``import github.M as M`` when M is shadowed by a same-name re-export in github/__init__.py.

        At runtime the alias would resolve to the re-exported CLASS, not the module (the async package loads after
        __init__.py completes). For each shadowed module actually alias-imported by this file:

        1. Keep ``import github.M as M`` (mypy sees the module)
        2. Add ``import sys as _sys`` (stays in the import block, avoids E402)
        3. Insert an ``M = _sys.modules["github.M"]`` override wrapped in ``if not TYPE_CHECKING:`` (runtime only)
        4. Remove bare ``import github.M`` and ``from github import M`` variants (redundant / would shadow the alias)

        """
        for mod in _shadowed_skip_modules():
            if not re.search(rf"^import github\.{re.escape(mod)} as {re.escape(mod)}\s*$", lines, re.MULTILINE):
                continue
            logger.debug("fix_shadowed_module_alias: applying _sys.modules fix for '%s'", mod)
            # Add `import sys as _sys` BEFORE the aliased import (stays in import block)
            lines = re.sub(
                rf"^(import github\.{re.escape(mod)} as {re.escape(mod)})\s*$",
                r"import sys as _sys\n\1",
                lines,
                flags=re.MULTILINE,
            )
            # Remove the bare `import github.M` (if present) since the aliased
            # import already handles it
            lines = re.sub(
                rf"^import github\.{re.escape(mod)}\s*\n",
                "",
                lines,
                flags=re.MULTILINE,
            )
            # Also remove `from github import M` variants (if produced by
            # _fix_imports or ruff transformations — these import the CLASS, not
            # the MODULE, and would shadow our aliased import)
            lines = re.sub(
                rf"^from github import {re.escape(mod)}\s*\n",
                "",
                lines,
                flags=re.MULTILINE,
            )
            # Insert the runtime-only _sys.modules override before the first
            # TYPE_CHECKING block or class definition (whichever comes first).
            sysmod_block = (
                "if not TYPE_CHECKING:\n"
                f'    {mod} = _sys.modules["github.{mod}"]'
                "  # noqa: F811  # Get MODULE, not class\n"
            )
            m_tc = re.search(r"^if TYPE_CHECKING:", lines, re.MULTILINE)
            m_class = re.search(r"^class \w+", lines, re.MULTILINE)
            # Pick the earliest anchor
            insert_pos = None
            for anchor in [m_tc, m_class]:
                if anchor and (insert_pos is None or anchor.start() < insert_pos):
                    insert_pos = anchor.start()
            if insert_pos is not None:
                lines = lines[:insert_pos] + sysmod_block + "\n" + lines[insert_pos:]
            else:
                lines += "\n" + sysmod_block
        return lines

    def _fix_sync_dunder_methods(self, src: str, stem: str) -> str:
        """
        Fix sync dunder methods that access async properties.

        In async classes, properties like self.name, self.url become async def, so sync dunder methods (__repr__,
        __eq__, __hash__, etc.) can't call them. Instead, access the underlying _Attribute storage directly:
        self._name.value, self._url.value.

        Also handles other.PROP patterns in __eq__ (e.g., other.login, other.id).

        """
        # Collect ALL promoted properties across all classes
        all_promoted = set()
        for pp_set in self.analyzer.promoted_properties.values():
            all_promoted |= pp_set

        # Sync dunder methods that should NEVER be async but may reference properties
        sync_dunders = {"__repr__", "__eq__", "__ne__", "__hash__", "__lt__", "__le__", "__gt__", "__ge__"}

        lines = src.split("\n")
        result_lines = []
        in_dunder = False
        dunder_indent = -1

        for line in lines:
            stripped = line.lstrip()
            indent = len(line) - len(stripped)

            # Detect sync dunder method start
            if any(stripped.startswith(f"def {d}") for d in sync_dunders):
                in_dunder = True
                dunder_indent = indent
                dunder_name = stripped.split("(")[0].replace("def ", "")
                logger.debug("fix_sync_dunders[%s]: entering %s", stem, dunder_name)
                result_lines.append(line)
                continue

            # Track when we exit the dunder method
            if in_dunder and stripped and not stripped.startswith("#") and indent <= dunder_indent:
                if not any(stripped.startswith(f"def {d}") for d in sync_dunders):
                    in_dunder = False

            if in_dunder:
                # Replace self.PROP and other.PROP with self._PROP.value / other._PROP.value
                # for promoted properties
                for prop in all_promoted:
                    # Match self.prop (not self._prop)
                    pattern = rf"(?<!\w)self\.{re.escape(prop)}(?!\w)"
                    if re.search(pattern, stripped):
                        logger.debug(
                            "fix_sync_dunders[%s]: replacing self.%s → self._%s.value",
                            stem,
                            prop,
                            prop,
                        )
                        line = re.sub(pattern, f"self._{prop}.value", line)
                    # Match other.prop (common in __eq__)
                    pattern_other = rf"(?<!\w)other\.{re.escape(prop)}(?!\w)"
                    if re.search(pattern_other, stripped):
                        logger.debug(
                            "fix_sync_dunders[%s]: replacing other.%s → other._%s.value",
                            stem,
                            prop,
                            prop,
                        )
                        line = re.sub(pattern_other, f"other._{prop}.value", line)
                    stripped = line.lstrip()  # update for next prop

            result_lines.append(line)

        return "\n".join(result_lines)

    @staticmethod
    def _fix_async_generator_in_join(src: str) -> str:
        """
        Fix async generators passed to str.join().

        Converts patterns like: `".join((await x.prop) for x in items)`
        to: `".join([(await x.prop) for x in items])`

        In Python, `(await x for x in items)` inside .join() creates an async
        generator that str.join() cannot consume. Wrapping in [...] makes it a
        list comprehension.

        """
        # Match .join( ... await ... for ... in ... ) where the join contains
        # an async generator expression (no square brackets).
        # Strategy: find `.join(` then check if what follows is a generator with await.
        # Replace the outer ( ) of .join(genexpr) with .join([genexpr])
        result = re.sub(
            r"\.join\((\(await [^)]+\) for [^)]+)\)",
            r".join([\1])",
            src,
        )
        return result

    @staticmethod
    def _last_toplevel_import_end(src: str) -> int:
        """
        Return the character offset of the end of the last top-level import line.

        Indented imports (e.g. inside TYPE_CHECKING blocks or functions) are ignored. Multi-line parenthesized imports
        are handled: the offset points past the closing ``)`` line. Returns 0 if no top-level import is found.

        """
        last_import_end = 0
        for m in re.finditer(r"^(?:import |from )\S+", src, re.MULTILINE):
            line_start = src.rfind("\n", 0, m.start()) + 1
            if m.start() > line_start:  # indented — skip
                continue
            line_end = src.find("\n", m.end())
            if line_end == -1:
                line_end = len(src)
            full_line = src[line_start:line_end]
            if "(" in full_line and ")" not in full_line:
                close_paren = src.find(")", line_end)
                if close_paren != -1:
                    close_eol = src.find("\n", close_paren)
                    if close_eol == -1:
                        close_eol = len(src)
                    last_import_end = close_eol
                else:
                    last_import_end = line_end
            else:
                last_import_end = line_end
        return last_import_end

    @classmethod
    def _ensure_import_github(cls, result: str) -> str:
        """
        Add `import github` if the body references github.X and it's not already imported.
        """
        body_has_github_ref = False
        for line in result.split("\n"):
            s = line.lstrip()
            if s.startswith(("import ", "from ", "#", '"""', "'''", "@")):
                continue
            if not s:
                continue
            # Check for github.X pattern (but not github.com or similar URL-like refs)
            if re.search(r"\bgithub\.\w+", s) and not re.search(r"github\.com|github\.v\d|github\.groot", s):
                body_has_github_ref = True
                break
        if not body_has_github_ref:
            return result
        if "import github\n" in result or "import github " in result:
            return result
        # Also check for `import github.GithubObject` etc. which already makes `github` available.
        # NOTE: `import github.X as Y` does NOT make `github` available, only `Y`.
        if re.search(r"^import github\.\w+\s*$", result, re.MULTILINE):
            return result
        # Plain `import github` (no .X suffix)
        if re.search(r"^import github\s*$", result, re.MULTILINE):
            return result

        logger.debug("ensure_import_github: adding 'import github' (body references github.X)")

        # Add `import github` after the last TOP-LEVEL import line
        last_import_end = cls._last_toplevel_import_end(result)
        if last_import_end > 0:
            result = result[:last_import_end] + "\nimport github" + result[last_import_end:]
        return result

    @staticmethod
    def _replace_is_notset_with_helpers(src: str) -> str:
        """
        Replace `X is NotSet` with `is_undefined(X)` and `X is not NotSet` with `is_defined(X)`.

        This ensures correct behavior when sync objects (whose attributes are sync _NotSetType) are checked against the
        async NotSet singleton. The is_undefined/is_defined functions in async GithubObject check both sync and async
        _NotSetType.

        """
        had_is_not = bool(re.search(r"\bis\s+not\s+NotSet\b", src))
        had_is = bool(re.search(r"\bis\s+NotSet\b", src))
        # Replace `VAR is not NotSet` -> `is_defined(VAR)` first (before `is NotSet`)
        # Match patterns like: `x is not NotSet`, `self._x is not NotSet`, `foo.bar is not NotSet`
        src = re.sub(
            r"\b([\w.]+)\s+is\s+not\s+NotSet\b",
            r"is_defined(\1)",
            src,
        )
        # Replace `VAR is NotSet` -> `is_undefined(VAR)`
        src = re.sub(
            r"\b([\w.]+)\s+is\s+NotSet\b",
            r"is_undefined(\1)",
            src,
        )
        if had_is_not or had_is:
            logger.debug(
                "replace_notset: replaced is_not_NotSet=%s, is_NotSet=%s with helpers",
                had_is_not,
                had_is,
            )

        # Ensure is_defined and is_undefined are imported.
        # Look for existing parenthesized import from GithubObject and add names inside.
        for fn_name in ["is_undefined", "is_defined"]:
            if fn_name + "(" not in src:
                continue
            # Check if already imported (either in a parenthesized block or standalone)
            # Match both relative (.GithubObject) and absolute (githubasyncio.GithubObject) forms
            if re.search(rf"from (?:\.|\bgithubasyncio\.)GithubObject import[^)]*\b{fn_name}\b", src, re.DOTALL):
                continue
            # Try to add to existing parenthesized import from .GithubObject:
            paren_import = re.search(
                r"(from (?:\.|\bgithubasyncio\.)GithubObject import \([^)]*)(\))",
                src,
                re.DOTALL,
            )
            if paren_import:
                block = paren_import.group(1)
                src = (
                    src[: paren_import.start()]
                    + block
                    + f"    {fn_name},\n"
                    + paren_import.group(2)
                    + src[paren_import.end() :]
                )
            else:
                # No existing import to extend; add a new standalone one. Absolute, since this
                # introduces a new import rather than extending one already there.
                src = AsyncTransformer._prepend_import(src, f"from githubasyncio.GithubObject import {fn_name}\n")

        return src

    def _move_class_body_imports(self, src: str) -> str:
        """
        Move from-imports inside class bodies to TYPE_CHECKING blocks.

        The sync code has `from github.X import Y` inside class bodies for type annotations. With `from __future__
        import annotations`, these are strings at runtime, so we can safely move them to TYPE_CHECKING. This prevents
        circular imports that occur when the imported module is still being loaded.

        Imports inside method/function bodies (def) are kept as-is since they execute at call time when all modules are
        loaded.

        """
        lines = src.split("\n")
        result_lines = []
        imports_to_add_to_type_checking = []

        # Track whether we're inside a class body (but not inside a method)
        in_class = False
        class_indent = 0
        in_method = False
        method_indent = 0

        for i, line in enumerate(lines):
            stripped = line.lstrip()
            indent = len(line) - len(stripped)

            # Track class/method context
            if stripped.startswith("class ") and ":" in stripped:
                in_class = True
                class_indent = indent
                in_method = False
                result_lines.append(line)
                continue

            if (
                in_class
                and indent <= class_indent
                and stripped
                and not stripped.startswith("#")
                and not stripped.startswith("class ")
            ):
                in_class = False
                in_method = False

            if in_class and (stripped.startswith("def ") or stripped.startswith("async def ")):
                in_method = True
                method_indent = indent
            elif (
                in_class
                and in_method
                and indent <= method_indent
                and stripped
                and not stripped.startswith("#")
                and not stripped.startswith("@")
            ):
                # Exited method body
                if stripped.startswith("def ") or stripped.startswith("async def "):
                    method_indent = indent
                else:
                    in_method = False

            # Check if this is a from-import inside a class body but NOT inside a method
            if (
                in_class
                and not in_method
                and indent > class_indent
                and stripped.startswith("from github")
                and "import " in stripped
            ):
                # Move to TYPE_CHECKING
                imports_to_add_to_type_checking.append(stripped)
                # Remove this line (replace with blank to preserve line count for error messages)
                result_lines.append("")
                continue

            result_lines.append(line)

        if not imports_to_add_to_type_checking:
            return src

        logger.debug(
            "move_class_body_imports: moving %d imports to TYPE_CHECKING: %s",
            len(imports_to_add_to_type_checking),
            imports_to_add_to_type_checking,
        )

        # Add imports to TYPE_CHECKING block
        new_src = "\n".join(result_lines)

        # Find the TYPE_CHECKING block
        tc_match = re.search(r"^if TYPE_CHECKING:\n", new_src, re.MULTILINE)
        if tc_match:
            # Find the end of the TYPE_CHECKING block (first non-indented, non-empty line)
            pos = tc_match.end()
            tc_lines = new_src[pos:].split("\n")
            insert_idx = 0
            for j, tl in enumerate(tc_lines):
                tl_stripped = tl.strip()
                if tl_stripped and not tl_stripped.startswith("#"):
                    tl_indent = len(tl) - len(tl.lstrip())
                    if tl_indent == 0:
                        break
                insert_idx = j + 1

            # Build new imports to add (deduplicate with existing ones)
            existing_tc_block = "\n".join(tc_lines[:insert_idx])
            new_imports = []
            for imp in imports_to_add_to_type_checking:
                if imp not in existing_tc_block:
                    new_imports.append(f"    {imp}")

            if new_imports:
                # Insert at the end of TYPE_CHECKING block
                tc_lines_list = tc_lines[:insert_idx]
                tc_lines_list.extend(new_imports)
                tc_lines_list.extend(tc_lines[insert_idx:])
                new_src = new_src[:pos] + "\n".join(tc_lines_list)
        else:
            # No TYPE_CHECKING block — create one
            # Find the right position (after imports, before code)
            import_block_end = 0
            for match in re.finditer(r"^(import |from )", new_src, re.MULTILINE):
                line_end = new_src.find("\n", match.start())
                if line_end == -1:
                    line_end = len(new_src)
                import_block_end = line_end + 1

            tc_block = "\nif TYPE_CHECKING:\n"
            for imp in imports_to_add_to_type_checking:
                tc_block += f"    {imp}\n"
            tc_block += "\n"

            # Ensure TYPE_CHECKING is imported
            if "TYPE_CHECKING" not in new_src:
                new_src = new_src.replace("from typing import ", "from typing import TYPE_CHECKING, ", 1)
                if "TYPE_CHECKING" not in new_src:
                    new_src = "from typing import TYPE_CHECKING\n" + new_src

            new_src = new_src[:import_block_end] + tc_block + new_src[import_block_end:]

        return new_src

    @staticmethod
    def _split_import_names(names_part: str, identifiers_only: bool = False) -> list[str]:
        """
        Split the name list of an import statement into clean names.

        Strips parentheses, whitespace and trailing commas from e.g. ``"A, B"`` or ``"(A,"``. With
        ``identifiers_only=True``, entries that are not valid identifiers (e.g. ``X as Y``) are dropped.

        """
        names: list[str] = []
        for raw in names_part.replace("(", "").replace(")", "").split(","):
            n = raw.strip().rstrip(",").strip()
            if not n:
                continue
            if identifiers_only and not n.isidentifier():
                continue
            names.append(n)
        return names

    @staticmethod
    def _track_type_checking(line: str, in_tc: bool, tc_indent: int) -> tuple[bool, int, bool]:
        """
        Update TYPE_CHECKING-block tracking state for one source line.

        Returns ``(in_tc, tc_indent, is_header)``.  ``is_header`` is True when the line is the ``if TYPE_CHECKING:``
        header itself.  The block ends at the first non-blank, non-comment line indented at or above the header.

        """
        stripped = line.strip()
        if stripped.startswith("if TYPE_CHECKING"):
            return True, len(line) - len(line.lstrip()), True
        if in_tc and stripped and not stripped.startswith("#"):
            if len(line) - len(line.lstrip()) <= tc_indent:
                return False, tc_indent, False
        return in_tc, tc_indent, False

    @classmethod
    def _dedup_runtime_imports(cls, src: str) -> str:
        """
        Remove duplicate name bindings that cause F811 (redefinition of unused import).

        After _fix_imports and _move_class_body_imports, two F811 patterns exist:

        Pattern A — Runtime module + runtime class (same name bound twice at runtime):
            from . import PaginatedList               # module
            from .PaginatedList import PaginatedList   # class → F811
          Fix: remove the name from the module import (class import is needed at runtime).

        Pattern B — Runtime module + TYPE_CHECKING class (shadowing):
            from . import Commit                      # module (runtime)
            if TYPE_CHECKING:
                from .Commit import Commit            # class → F811
          Fix: remove the TYPE_CHECKING import (module is already available, and all
          annotations are strings due to `from __future__ import annotations`).

        Also handles absolute variants and _sys.modules reassignments:
            from github import Consts, GithubRetry
            from github.GithubRetry import GithubRetry   → F811

            from github import GithubException
            GithubException = _sys.modules[...]           → F811

        """
        lines = src.split("\n")

        # --- Pass 1: Collect runtime module imports and runtime class imports ---
        in_type_checking = False
        tc_indent = 0
        in_multiline_from_dot_import = False

        # Names imported as modules at runtime: `from . import X` or individual entries
        runtime_module_names: set[str] = set()
        # Names imported as classes at runtime: `from .X import X` where mod == name
        runtime_class_imports: set[str] = set()
        # Names reassigned via `X = _sys.modules[...]`
        sysmodules_assignments: set[str] = set()

        for line in lines:
            stripped = line.strip()

            # Track TYPE_CHECKING blocks (their imports are type-only — skip them)
            in_type_checking, tc_indent, is_tc_header = cls._track_type_checking(line, in_type_checking, tc_indent)
            if is_tc_header or in_type_checking:
                continue

            # Handle continuation of multi-line `from . import (` block
            if in_multiline_from_dot_import:
                if ")" in stripped:
                    in_multiline_from_dot_import = False
                # Extract names from continuation lines
                runtime_module_names.update(cls._split_import_names(stripped, identifiers_only=True))
                continue

            # Collect `from . import X, Y, Z` names (runtime module imports)
            m = re.match(r"^from \. import (.+)$", stripped)
            if m:
                names_part = m.group(1)
                if "(" in names_part and ")" not in names_part:
                    # Start of multi-line import
                    in_multiline_from_dot_import = True
                runtime_module_names.update(cls._split_import_names(names_part, identifiers_only=True))
                continue

            # Collect `from .X import X` (runtime class imports where mod == name)
            m = re.match(r"^from \.(\w+) import (.+)$", stripped)
            if m:
                mod_name = m.group(1)
                if mod_name in cls._split_import_names(m.group(2)):
                    runtime_class_imports.add(mod_name)

            # Collect `from github import X, Y` names (absolute module imports that bind names)
            # BUT: skip names in SHADOWED_MODULE_NAMES — those are direct class re-exports from
            # github/__init__.py (e.g. InputGitAuthor, InputGitTreeElement, GithubException) and
            # the bare name already refers to the class, not a module. Adding them to
            # runtime_module_names would cause Pass 2b to incorrectly rewrite `InputGitAuthor` →
            # `InputGitAuthor.InputGitAuthor`.
            m = re.match(r"^from github import (.+)$", stripped)
            if m:
                for n in cls._split_import_names(m.group(1), identifiers_only=True):
                    if n not in SHADOWED_MODULE_NAMES:
                        runtime_module_names.add(n)

            # Collect `from github.X import X` (absolute runtime class imports)
            m = re.match(r"^from github\.(\w+) import (.+)$", stripped)
            if m:
                mod_name = m.group(1)
                if mod_name in cls._split_import_names(m.group(2)):
                    runtime_class_imports.add(mod_name)

            # Collect `X = _sys.modules[...]`
            m = re.match(r"^(\w+)\s*=\s*_sys\.modules\[", stripped)
            if m:
                sysmodules_assignments.add(m.group(1))

        # Pattern A: names to remove from `from . import (...)` because a runtime
        # class import or _sys.modules assignment provides the same name
        names_to_remove_from_module_import = (runtime_class_imports | sysmodules_assignments) & runtime_module_names

        # Pattern B: names to remove from TYPE_CHECKING blocks because the runtime
        # module import already provides the name (and annotations are strings).
        # Only names that will STILL remain in the runtime module imports after Pattern A.
        names_to_remove_from_tc = runtime_module_names - names_to_remove_from_module_import

        if not names_to_remove_from_module_import and not names_to_remove_from_tc:
            return src

        logger.debug(
            "dedup_runtime_imports: removing from module imports: %s; removing from TYPE_CHECKING: %s",
            sorted(names_to_remove_from_module_import),
            sorted(names_to_remove_from_tc),
        )

        # --- Pass 2: Remove conflicting names ---
        result_lines: list[str] = []
        i = 0
        in_type_checking = False
        tc_indent = 0

        while i < len(lines):
            line = lines[i]
            stripped = line.strip()

            # Track TYPE_CHECKING blocks
            in_type_checking, tc_indent, is_tc_header = cls._track_type_checking(line, in_type_checking, tc_indent)
            if is_tc_header:
                result_lines.append(line)
                i += 1
                continue

            # --- Inside TYPE_CHECKING: remove duplicate names from imports ---
            # Handles both relative (`from .X import ...`) and absolute (`from github.X import ...`)
            # in both single-line and multi-line (parenthesized) forms.
            if in_type_checking and names_to_remove_from_tc:
                # Match single-line: `from .X import Y, Z` or `from github.X import Y, Z`
                m = re.match(r"^(\s*)from (?:\.|\bgithub\.)(\w+) import (.+)$", line)
                if m and "(" not in m.group(3):
                    mod_name = m.group(2)
                    indent = m.group(1)
                    names = cls._split_import_names(m.group(3))
                    # Remove names that duplicate a runtime module import
                    filtered = [n for n in names if n not in names_to_remove_from_tc]
                    # Determine import prefix (relative or absolute)
                    prefix = "." if line.lstrip().startswith("from .") else "github."
                    if not filtered:
                        # All names removed — drop the line
                        i += 1
                        continue
                    elif len(filtered) < len(names):
                        result_lines.append(f"{indent}from {prefix}{mod_name} import {', '.join(filtered)}")
                        i += 1
                        continue
                    # else: no change, fall through

                # Match multi-line: `from .X import (` or `from github.X import (`
                m_ml = re.match(r"^(\s*)from (?:\.|\bgithub\.)(\w+) import \($", line)
                if m_ml:
                    indent = m_ml.group(1)
                    mod_name = m_ml.group(2)
                    prefix = "." if line.lstrip().startswith("from .") else "github."
                    # Collect all lines of the multi-line import block
                    block_lines = [line]
                    i += 1
                    while i < len(lines) and ")" not in lines[i]:
                        block_lines.append(lines[i])
                        i += 1
                    if i < len(lines):
                        block_lines.append(lines[i])  # closing ")"
                        i += 1
                    # Extract names from the block body (skip first and last lines)
                    all_names: list[str] = []
                    for bl in block_lines[1:-1]:
                        name = bl.strip().rstrip(",").strip()
                        if name and name.isidentifier():
                            all_names.append(name)
                    filtered = [n for n in all_names if n not in names_to_remove_from_tc]
                    if not filtered:
                        # All names removed — drop entire block
                        continue
                    elif len(filtered) < len(all_names):
                        # Some names removed — rebuild block
                        if len(filtered) == 1:
                            result_lines.append(f"{indent}from {prefix}{mod_name} import {filtered[0]}")
                        else:
                            result_lines.append(f"{indent}from {prefix}{mod_name} import (")
                            for fn in filtered:
                                result_lines.append(f"{indent}    {fn},")
                            result_lines.append(f"{indent})")
                        continue
                    else:
                        # No change — re-add all block lines
                        result_lines.extend(block_lines)
                        continue

            # --- Outside TYPE_CHECKING: handle runtime dedup ---
            if not in_type_checking and names_to_remove_from_module_import:
                # Handle `from . import (` multi-line block
                if re.match(r"^from \. import \($", stripped):
                    block_lines = [line]
                    i += 1
                    while i < len(lines) and ")" not in lines[i]:
                        block_lines.append(lines[i])
                        i += 1
                    if i < len(lines):
                        block_lines.append(lines[i])  # closing ")"
                        i += 1

                    kept_names: list[str] = []
                    for bl in block_lines[1:-1]:
                        name = bl.strip().rstrip(",").strip()
                        if name and name not in names_to_remove_from_module_import:
                            kept_names.append(name)

                    if kept_names:
                        block_indent = line[: len(line) - len(line.lstrip())]
                        result_lines.append(f"{block_indent}from . import (")
                        for kn in kept_names:
                            result_lines.append(f"{block_indent}    {kn},")
                        result_lines.append(f"{block_indent})")
                    continue

                # Handle single-line `from . import X, Y, Z`
                m = re.match(r"^(\s*)from \. import (.+)$", line)
                if m and "(" not in m.group(2):
                    indent = m.group(1)
                    names = cls._split_import_names(m.group(2))
                    filtered = [n for n in names if n not in names_to_remove_from_module_import]
                    if filtered:
                        result_lines.append(f"{indent}from . import {', '.join(filtered)}")
                    i += 1
                    continue

                # Handle `from github import X, Y` — remove conflicting names
                m = re.match(r"^(\s*)from github import (.+)$", line)
                if m and "(" not in m.group(2):
                    indent = m.group(1)
                    names = cls._split_import_names(m.group(2))
                    filtered = [n for n in names if n not in names_to_remove_from_module_import]
                    if filtered:
                        result_lines.append(f"{indent}from github import {', '.join(filtered)}")
                    i += 1
                    continue

            result_lines.append(line)
            i += 1

        # --- Pass 2b: Qualify bare class names that lost their TYPE_CHECKING import ---
        # When Pattern B removes a TYPE_CHECKING import `from .X import X`, the bare
        # name `X` in annotations (Attribute[X], -> X, param: X) now resolves to the
        # *module* instead of the class.  Rewrite bare `X` → `X.X` in annotation
        # contexts so the reference is module.class (correct).
        if names_to_remove_from_tc:
            # Regex to split a line into string-literal vs non-string segments.
            # Capturing group means re.split returns both code and string parts.
            _string_re = re.compile(
                r"""(r?f?b?\"\"\".*?\"\"\"|r?f?b?\'\'\'.*?\'\'\'|r?f?b?\"[^\"\\]*(?:\\.[^\"\\]*)*\"|r?f?b?\'[^\'\\]*(?:\\.[^\'\\]*)*\')""",
                re.DOTALL,
            )
            qualified_lines: list[str] = []
            in_docstring = False
            in_import_paren = False
            for line in result_lines:
                stripped = line.strip()
                # Skip the continuation lines of a multi-line parenthesized import
                # (e.g. `from .X import (\n    Name,\n    ...\n)`) — these don't start
                # with "from "/"import " themselves, so the check below wouldn't catch
                # them, and rewriting a bare imported name here would corrupt the
                # import statement (e.g. `GithubObject,` -> `GithubObject.GithubObject,`).
                if in_import_paren:
                    qualified_lines.append(line)
                    if ")" in stripped:
                        in_import_paren = False
                    continue
                # Skip import lines — don't rewrite imports themselves
                if stripped.startswith(("from ", "import ")):
                    qualified_lines.append(line)
                    if "(" in stripped and ")" not in stripped:
                        in_import_paren = True
                    continue
                # Skip comment lines
                if stripped.startswith("#"):
                    qualified_lines.append(line)
                    continue
                # Track docstrings (triple-quoted strings) — skip them
                # Count triple-quote toggles on this line
                tq_count = stripped.count('"""') + stripped.count("'''")
                if in_docstring:
                    if tq_count % 2 == 1:
                        in_docstring = False
                    qualified_lines.append(line)
                    continue
                if tq_count >= 1:
                    if tq_count % 2 == 1:
                        # Opening triple quote without close on same line
                        in_docstring = True
                        qualified_lines.append(line)
                        continue
                    # tq_count is even: opens and closes on same line, skip rewriting
                    # (could be single-line docstring), but it's safe to process normally
                    # since type names rarely appear in single-line docstrings.

                # Split off inline comments — only rewrite the code part
                code_part = line
                comment_part = ""
                if "#" in line:
                    # Find the first # that's not inside a string
                    # Simple heuristic: split at first # not inside quotes
                    in_sq = False
                    in_dq = False
                    for ci, ch in enumerate(line):
                        if ch == "'" and not in_dq:
                            in_sq = not in_sq
                        elif ch == '"' and not in_sq:
                            in_dq = not in_dq
                        elif ch == "#" and not in_sq and not in_dq:
                            code_part = line[:ci]
                            comment_part = line[ci:]
                            break

                # Split code_part into string-literal vs non-string segments.
                # We only rewrite bare names in non-string segments to avoid
                # corrupting string values like "Team" → "Team.Team".
                segments = _string_re.split(code_part)
                # segments alternates: [non-string, string, non-string, string, ...]
                modified_segments: list[str] = []
                for si, seg in enumerate(segments):
                    if si % 2 == 1:
                        # This is a string literal — leave it untouched
                        modified_segments.append(seg)
                    else:
                        # This is code — apply the rewrites
                        mod = seg
                        for name in names_to_remove_from_tc:
                            # Replace bare `X` with `X.X` where X is NOT preceded by `.`
                            # and NOT already followed by `.` (meaning X is used as a module
                            # dereference like X.something — already correct).
                            mod = re.sub(
                                rf"(?<!\.)\b{re.escape(name)}\b(?!\.)",
                                f"{name}.{name}",
                                mod,
                            )
                        modified_segments.append(mod)
                modified = "".join(modified_segments)
                qualified_lines.append(modified + comment_part)
            result_lines = qualified_lines

        # --- Pass 3: Clean up empty TYPE_CHECKING blocks and unused imports ---
        result = "\n".join(result_lines)

        # 3a) Remove empty TYPE_CHECKING blocks.
        # An empty block is `if TYPE_CHECKING:` followed by blank lines or non-indented code.
        result = re.sub(
            r"^if TYPE_CHECKING:\n(?=\s*\n|\s*(?:class |def |[A-Z]))",
            "",
            result,
            flags=re.MULTILINE,
        )

        # 3b) If TYPE_CHECKING is no longer referenced anywhere in the file (no
        # `if TYPE_CHECKING:` block remains), remove it from the typing import.
        if "if TYPE_CHECKING" not in result and "TYPE_CHECKING" in result:
            # Remove TYPE_CHECKING from `from typing import TYPE_CHECKING, ...`
            result = re.sub(
                r"^(from typing import )TYPE_CHECKING,\s*",
                r"\1",
                result,
                flags=re.MULTILINE,
            )
            # Also handle `from typing import ..., TYPE_CHECKING, ...`
            result = re.sub(
                r"^(from typing import .+),\s*TYPE_CHECKING\b",
                r"\1",
                result,
                flags=re.MULTILINE,
            )
            # Handle `from typing import TYPE_CHECKING` alone on a line
            result = re.sub(
                r"^from typing import TYPE_CHECKING\s*\n",
                "",
                result,
                flags=re.MULTILINE,
            )

        # 3c) Remove `from . import X` lines where X is no longer referenced in the
        # file body. Only remove module imports that we know became orphaned (i.e.,
        # names we removed from TYPE_CHECKING that were also runtime module imports
        # and have no other references).
        if names_to_remove_from_tc:
            result_lines_2 = result.split("\n")
            # Build body text EXCLUDING import lines for reference checking
            body_for_check = []
            for rl in result_lines_2:
                rs = rl.strip()
                if not rs.startswith(("from ", "import ")):
                    body_for_check.append(rl)
            body_text = "\n".join(body_for_check)

            final_lines: list[str] = []
            j = 0
            while j < len(result_lines_2):
                rl = result_lines_2[j]
                stripped_rl = rl.strip()

                # Check single-line `from . import X, Y, Z` — remove names not in body
                m = re.match(r"^(\s*)from \. import (.+)$", rl)
                if m and "(" not in m.group(2):
                    indent = m.group(1)
                    names = cls._split_import_names(m.group(2))
                    # Keep names that are referenced in the body (type hints, code, etc.)
                    # or that were NOT in our TC removal set (i.e., pre-existing imports)
                    kept = []
                    for n in names:
                        if n not in names_to_remove_from_tc:
                            # Not a name we touched — keep it
                            kept.append(n)
                        elif re.search(rf"\b{re.escape(n)}\b", body_text):
                            # Still referenced in the body — keep it
                            kept.append(n)
                        else:
                            logger.debug(
                                "dedup_runtime_imports: removing orphaned module import: %s",
                                n,
                            )
                    if kept:
                        final_lines.append(f"{indent}from . import {', '.join(kept)}")
                    j += 1
                    continue

                # Check multi-line `from . import (` block
                if re.match(r"^from \. import \($", stripped_rl):
                    block = [rl]
                    j += 1
                    while j < len(result_lines_2) and ")" not in result_lines_2[j]:
                        block.append(result_lines_2[j])
                        j += 1
                    if j < len(result_lines_2):
                        block.append(result_lines_2[j])
                        j += 1

                    kept_block: list[str] = []
                    for bl in block[1:-1]:
                        n = bl.strip().rstrip(",").strip()
                        if not n:
                            continue
                        if n not in names_to_remove_from_tc:
                            kept_block.append(n)
                        elif re.search(rf"\b{re.escape(n)}\b", body_text):
                            kept_block.append(n)
                        else:
                            logger.debug(
                                "dedup_runtime_imports: removing orphaned module import: %s",
                                n,
                            )

                    if kept_block:
                        block_indent = rl[: len(rl) - len(rl.lstrip())]
                        if len(kept_block) == 1:
                            final_lines.append(f"{block_indent}from . import {kept_block[0]}")
                        else:
                            final_lines.append(f"{block_indent}from . import (")
                            for kn in kept_block:
                                final_lines.append(f"{block_indent}    {kn},")
                            final_lines.append(f"{block_indent})")
                    continue

                final_lines.append(rl)
                j += 1

            result = "\n".join(final_lines)

        return result

    def _fix_imports(self, src: str, stem: str) -> str:
        """
        Fix import statements to reference the async package (githubasyncio) internally.

        Only ever introduces *absolute* `import githubasyncio.X` / `from githubasyncio import ...`
        / `from githubasyncio.X import ...` references. Relative imports already present in the
        sync source (a handful of `github/*.py` files use `from .X import Y` internally) are left
        completely alone — they still resolve correctly here since githubasyncio mirrors github's
        flat, single-level layout, and this generator does not "clean them up".

        Transforms:
          import github.X            → import githubasyncio.X        (for async modules)
          github.X.ClassName         → githubasyncio.X.ClassName      (after above import)
          from github.X import Y     → from githubasyncio.X import Y (for async modules)
          from .X import Y           → from .X import Y              (untouched — see above)
          from github.X import Y     → from github.X import Y  (for non-async SKIP_FILES)

        KNOWN BUG (noted, not yet fixed): this operates on raw text, not just live code, so a
        plain string *literal* that happens to mention `github.X(...)` as human-readable
        guidance (e.g. a deprecation warning: `"please use auth=github.Auth.Login(...) instead"`)
        gets the same rewrite as real code. Since the alias now equals the real module path
        (`githubasyncio.Auth.Login(...)`, not a meaningless internal `_async_Auth.Login(...)`
        name — see the `_alias()` comment below), this half of the bug is now mostly harmless:
        a `github.<module>.<name>` mention in a string literal comes out *correct*. What's still
        wrong is any bare `github.<ClassName>` mention (a class, not a module, e.g.
        `github.Github(...)` or `github.GithubIntegration(...)`), since Step 2's regex only
        matches `github.<module>.`, not the bare class form — those are left saying `github.`
        instead of `githubasyncio.` (confirmed still present, e.g. MainClass.py's
        get_app()/get_access_token() deprecation messages). Needs the generator to actually
        distinguish string-literal spans from code before rewriting (e.g. via tokenize/ast)
        rather than blind text substitution.

        """
        logger.debug("fix_imports[%s]: begin", stem)
        result = src

        # Build set of files that have async versions
        async_files = set()
        for cls_name in self.analyzer.async_classes:
            f = self.analyzer.class_to_file.get(cls_name)
            if f:
                async_files.add(f)
        for p in SRC_PKG.glob("*.py"):
            s = p.stem
            if s not in SKIP_STEMS and not s.startswith("_"):
                async_files.add(s)

        # Step 1: Convert bare `import github.X` → `import githubasyncio.X` (for async modules).
        # No alias, matching the sync source's own convention exactly: `import github.X` (no `as`
        # clause) only ever binds the top-level name `github` in Python -- never the bare
        # submodule name `X` -- so it can never collide with the bare-name class import
        # annotations need under `if TYPE_CHECKING:` (ARCHITECTURE.md's two-import pattern:
        # runtime references use `github.<File>.<Class>`, annotations use the bare `<Class>`).
        # `import githubasyncio.X` has that exact same property, for the exact same reason:
        # githubasyncio is root-level, structurally identical to github.
        def _alias(mod: str) -> str:
            return f"githubasyncio.{mod}"

        # (a trailing `# comment` is allowed and kept, e.g. `import github.NamedUser  # TODO ...`)
        bare_imports = re.findall(r"^import github\.(\w+)[ \t]*(?:#[^\n]*)?$", result, re.MULTILINE)
        already_imported: set[str] = set()
        for mod in bare_imports:
            if mod in async_files:
                result = re.sub(
                    rf"^import github\.{re.escape(mod)}([ \t]*(?:#[^\n]*)?)$",
                    rf"import githubasyncio.{mod}\1",
                    result,
                    flags=re.MULTILINE,
                )
                already_imported.add(mod)
                logger.debug(
                    "fix_imports[%s]: step 1 — import github.%s → import githubasyncio.%s",
                    stem,
                    mod,
                    mod,
                )

        # Step 1b: Convert self-aliased `import github.X as X` -> `from githubasyncio import X`.
        # No `_async_` prefix needed here: the alias already equals the module name, so there's
        # no bare-name collision with a TYPE_CHECKING class import to avoid (unlike Step 1 above)
        # -- repointing the import is enough, every body reference already uses the bare name.
        self_aliased = re.findall(r"^import github\.(\w+) as \1\s*$", result, re.MULTILINE)
        for mod in self_aliased:
            if mod in async_files:
                result = re.sub(
                    rf"^import github\.{re.escape(mod)} as {re.escape(mod)}\s*$",
                    f"from githubasyncio import {mod}",
                    result,
                    flags=re.MULTILINE,
                )
                already_imported.add(mod)
                logger.debug(
                    "fix_imports[%s]: step 1b — import github.%s as %s → from githubasyncio import %s",
                    stem,
                    mod,
                    mod,
                    mod,
                )

        # Also track modules already imported via `import githubasyncio.X` (Step 1's own form,
        # picked up here too since a module can appear via `bare_imports` in one place and get
        # referenced again elsewhere) or a bare `from githubasyncio import X` (Step 1b's form, for
        # modules the sync source itself imports under a bare alias).
        for m in re.findall(r"^import githubasyncio\.(\w+)\s*$", result, re.MULTILINE):
            if m in async_files:
                already_imported.add(m)
        for m in re.findall(r"from githubasyncio import .*", result):
            for name in re.findall(r"\b(\w+)\b", m.replace("from githubasyncio import ", "")):
                if name in async_files:
                    already_imported.add(name)

        # Step 2: Convert bare `github.X.` references → `githubasyncio.X.` (matching the runtime
        # import from Step 1). Only for modules that have async versions.
        # Also track which modules are referenced in the code body but not yet imported
        needed_imports: set[str] = set()
        # only a reference in real code needs an import: a mention in a string literal (e.g. a deprecation message's
        # `auth=github.Auth.AppAuth(...)`), docstring or comment still gets rewritten below, but needs no import
        code_only = self._code_only(result)
        for mod in sorted(async_files, key=len, reverse=True):
            # Check if this module is actually referenced in the body
            pattern_bare = rf"(?<!asyncio\.)github\.{re.escape(mod)}\."
            pattern_async = rf"githubasyncio\.{re.escape(mod)}\."
            has_ref = bool(re.search(pattern_bare, result)) or bool(re.search(pattern_async, result))
            has_code_ref = bool(re.search(pattern_bare, code_only)) or bool(re.search(pattern_async, code_only))

            if has_ref and mod == stem:
                # Self-reference: e.g. Enterprise.py using github.Enterprise.Enterprise(...)
                # The class name is the same as the module name — after stripping github.
                # we'd get Enterprise.Enterprise which breaks (Enterprise is the class itself).
                # Instead, find the actual class name and replace github.X.ClassName with just ClassName
                # Since module and class have the same name, github.X.X(...) → X(...)
                result = re.sub(
                    rf"(?<!asyncio\.)github\.{re.escape(mod)}\.{re.escape(mod)}\b",
                    mod,
                    result,
                )
                result = re.sub(
                    rf"githubasyncio\.{re.escape(mod)}\.{re.escape(mod)}\b",
                    mod,
                    result,
                )
                # Handle github.X.OtherName patterns (class != module name) — unlikely but safe
                result = re.sub(
                    rf"(?<!asyncio\.)github\.{re.escape(mod)}\.",
                    f"{mod}.",
                    result,
                )
                result = re.sub(
                    rf"githubasyncio\.{re.escape(mod)}\.",
                    f"{mod}.",
                    result,
                )
            else:
                result = re.sub(
                    pattern_bare,
                    f"{_alias(mod)}.",
                    result,
                )
                result = re.sub(
                    pattern_async,
                    f"{_alias(mod)}.",
                    result,
                )
                if has_code_ref and mod not in already_imported:
                    needed_imports.add(mod)

        # Add missing `import githubasyncio.X` for modules referenced but never imported
        if needed_imports:
            logger.debug("fix_imports[%s]: step 2 — adding missing imports: %s", stem, sorted(needed_imports))
            # Find last TOP-LEVEL import line (handling multi-line parenthesized
            # imports and skipping indented TYPE_CHECKING block imports) and add after it.
            last_import_end = self._last_toplevel_import_end(result)
            import_line = "\n" + "".join(f"import githubasyncio.{mod}\n" for mod in sorted(needed_imports))
            result = result[: last_import_end + 1] + import_line + result[last_import_end + 1 :]

        # Step 3: from github.X import Y -> from githubasyncio.X import Y (for async modules)
        for mod in sorted(async_files, key=len, reverse=True):
            result = result.replace(f"from github.{mod} import ", f"from githubasyncio.{mod} import ")
        # requestlib isn't a flat github/*.py module (it's a subpackage), so it's never in
        # async_files -- redirect it separately to the async project's own niquests-only shim
        # (see generate_async_requestlib()), keeping githubasyncio self-contained.
        result = result.replace("from github.requestlib import ", "from githubasyncio.requestlib import ")
        logger.debug("fix_imports[%s]: step 3 — converted from-imports for async modules", stem)

        # Step 3a: `from github import X` (bare package-level import, e.g. `from github import
        # Consts`) -> `from githubasyncio import X`, for modules that AREN'T shadowed by a
        # same-named class re-export (SHADOWED_MODULE_NAMES) -- for those the bare name already
        # refers to the class via github/__init__.py's re-export, not the module, so redirecting
        # here would be wrong (Step 3b below handles class re-exports instead).
        for mod in sorted(async_files - SHADOWED_MODULE_NAMES, key=len, reverse=True):
            result = re.sub(
                rf"^from github import {re.escape(mod)}\s*$",
                f"from githubasyncio import {mod}",
                result,
                flags=re.MULTILINE,
            )

        # Step 2d: `github.{mod}` (e.g. `github.InputFileContent(...)`, `isinstance(x,
        # github.InputFileContent)`) where mod is a module whose name is shadowed by a same-named
        # re-exported class (SHADOWED_MODULE_NAMES) — relying on that shadowing (`github.X`
        # resolves to the CLASS via github/__init__.py's re-export, not the module). Rewrite to
        # `githubasyncio.mod.mod` rather than the sync source's own bare `mod.mod` form: the bare
        # module name is commonly ALSO bound to the bare CLASS elsewhere in the same file, under
        # `if TYPE_CHECKING:`, for annotations (e.g. `Opt[dict[str, InputFileContent | None]]`) —
        # reusing it here for the module would collide (F811, plus real ambiguity for any type
        # checker not narrowing on TYPE_CHECKING the way this specific double-duty pattern needs).
        # `githubasyncio.mod` sidesteps that the same way Step 1 does: `import githubasyncio.mod`
        # only binds the name `githubasyncio`, never the bare `mod`. And unlike Step 2 above,
        # don't assume `mod` is already imported: this pattern is commonly the *only runtime*
        # reference to it in the file (that TYPE_CHECKING import is annotations-only). Only for
        # OTHER files: mod's own file handles this itself via the mod == stem branch in Step 2
        # above. Runs after Step 3 specifically so the `from github.{mod} import` line is already
        # converted by then — otherwise this would corrupt it too (it has no dot between "github"
        # and mod either).
        step2d_needed: set[str] = set()
        for mod in sorted(SHADOWED_MODULE_NAMES & async_files, key=len, reverse=True):
            if mod == stem:
                continue
            pattern = rf"(?<!asyncio\.)\bgithub\.{re.escape(mod)}\b(?!\.)"
            result, _matched = self._sub_outside_docstrings(pattern, f"{_alias(mod)}.{mod}", result)
            if _matched:
                logger.debug("fix_imports[%s]: step 2d — github.%s → %s.%s", stem, mod, _alias(mod), mod)
                if mod not in already_imported:
                    step2d_needed.add(mod)
                    already_imported.add(mod)
        if step2d_needed:
            last_import_end = self._last_toplevel_import_end(result)
            import_line = "\n" + "".join(f"import githubasyncio.{mod}\n" for mod in sorted(step2d_needed))
            result = result[: last_import_end + 1] + import_line + result[last_import_end + 1 :]

        # Step 3b: Rewrite package-level class references: `github.ClassName`
        # where ClassName is re-exported from github/__init__.py and the underlying
        # module has an async version.  e.g. `github.Github(...)` → `githubasyncio.Github(...)`
        # (using async class from MainClass). See _init_reexports_map().
        _init_reexports = {
            cls_name: mod_name for cls_name, mod_name in _init_reexports_map().items() if mod_name in async_files
        }
        for cls_name, mod_name in _init_reexports.items():
            # Skip if we're processing the file that defines this class
            # (e.g. don't add `from .MainClass import Github` when transforming MainClass.py)
            if mod_name == stem:
                # Still rewrite `github.ClassName` → `ClassName` (bare name, already in scope)
                pattern = rf"\bgithub\.{re.escape(cls_name)}\b(?!\.)"
                result, _matched = self._sub_outside_docstrings(pattern, cls_name, result)
                if _matched:
                    logger.debug(
                        "fix_imports[%s]: step 3b — github.%s → %s (same file, no import needed)",
                        stem,
                        cls_name,
                        cls_name,
                    )
                continue

            # Check for circular import: if mod_name imports from the current file (stem), keep
            # `github.ClassName` for a hand-written PATCHES entry to handle (see
            # PATCHES["GithubIntegration"]).
            target_src_file = SRC_PKG / f"{mod_name}.py"
            if target_src_file.exists():
                target_src = target_src_file.read_text()
                if re.search(rf"^import github\.{re.escape(stem)}\b", target_src, re.MULTILINE) or re.search(
                    rf"^from github\.{re.escape(stem)} import ", target_src, re.MULTILINE
                ):
                    logger.debug(
                        "fix_imports[%s]: step 3b — skipping github.%s → %s (circular import: %s imports %s)",
                        stem,
                        cls_name,
                        cls_name,
                        mod_name,
                        stem,
                    )
                    continue

            # Match github.ClassName that is NOT followed by '.' (which would be github.ClassName.attr,
            # already handled by step 2 via the module pattern). Skip docstrings: a class
            # mentioned only in prose (e.g. a Sphinx `:meth:` cross-reference) is not real
            # usage, and treating it as such would add a needless import.
            # Rewrite to `githubasyncio.ClassName` when githubasyncio/__init__.py re-exports it too
            # (ASYNC_INIT_EXPORTS, e.g. `githubasyncio.Github`), backed by a bare `import
            # githubasyncio`; otherwise to the module-qualified `githubasyncio.mod_name.ClassName`
            # backed by a module-only `import githubasyncio.mod_name` -- same form as Step 2d.
            # Both resolve lazily, at call time, never an eager `from githubasyncio.mod_name import
            # ClassName`: that one breaks when mod_name is still mid-import (e.g. MainClass -> ... ->
            # Installation -> MainClass), and a bare `ClassName` is commonly bound only under `if
            # TYPE_CHECKING:` (so a plain textual "already imported?" check wrongly concludes the
            # runtime name exists -- Installation.get_github_for_installation() raised NameError that
            # way).
            # Use word boundary to avoid partial matches.
            pkg_level = cls_name in ASYNC_INIT_EXPORTS.get(mod_name, ())
            target = f"githubasyncio.{cls_name}" if pkg_level else f"{_alias(mod_name)}.{cls_name}"
            pattern = rf"\bgithub\.{re.escape(cls_name)}\b(?!\.)"
            result, _matched = self._sub_outside_docstrings(pattern, target, result)
            if _matched:
                if pkg_level:
                    # any `import githubasyncio.X` already binds the bare `githubasyncio` name
                    if not re.search(r"^import githubasyncio\b", result, re.MULTILINE):
                        last_import_end = self._last_toplevel_import_end(result)
                        result = (
                            result[: last_import_end + 1] + "\nimport githubasyncio\n" + result[last_import_end + 1 :]
                        )
                elif mod_name not in already_imported:
                    last_import_end = self._last_toplevel_import_end(result)
                    import_line = f"\nimport githubasyncio.{mod_name}\n"
                    result = result[: last_import_end + 1] + import_line + result[last_import_end + 1 :]
                    already_imported.add(mod_name)
                logger.debug("fix_imports[%s]: step 3b — github.%s → %s", stem, cls_name, target)

        # Step 4: Handle relative imports (from .X → from .X, already correct)
        # These are already relative within the package.

        # Step 5: Relative imports for non-async modules -> github (absolute, since they're outside the package)
        for skip in SKIP_FILES:
            mod = skip.replace(".py", "")
            if mod == "__init__":
                continue
            result = re.sub(
                rf"^(\s*)from \. import {re.escape(mod)}\b", rf"\1from github import {mod}", result, flags=re.MULTILINE
            )
            result = re.sub(
                rf"^(\s*)from \.{re.escape(mod)} import ", rf"\1from github.{mod} import ", result, flags=re.MULTILINE
            )
        logger.debug("fix_imports[%s]: steps 5-7 — fixed SKIP_FILES and remaining relative imports", stem)

        # Step 6: Fix remaining bare relative imports
        result = re.sub(
            r"^(\s*)from \. import (\w+)",
            lambda m: (
                m.group(0)  # Already relative — keep as is
                if m.group(2) in async_files
                else f"{m.group(1)}from github import {m.group(2)}"
            ),
            result,
            flags=re.MULTILINE,
        )

        # Step 7: Fix remaining relative from-imports
        result = re.sub(
            r"^(\s*)from \.(\w+) import ",
            lambda m: (
                m.group(0)  # Already relative — keep as is
                if m.group(2) in async_files
                else f"{m.group(1)}from github.{m.group(2)} import "
            ),
            result,
            flags=re.MULTILINE,
        )

        return result

    @classmethod
    def _fix_double_dereference(cls, src: str) -> str:
        """
        Fix double-dereference patterns caused by class imports shadowing module imports.

        When `from .X import X` imports a CLASS and code uses `X.X(...)`,
        it fails because CLASS has no attribute CLASS.  Two strategies:

        Strategy A – Switch to module import:
            If the body uses `X.X(` (constructor via module), change
            `from .X import X` → `from . import X` so X = module.
            Type hints still work since `from __future__ import annotations`.

        Strategy B – Replace qualified access with bare names:
            For GithubObject.NotSet, GithubObject.Attribute, etc. where
            the names are already imported from .GithubObject, replace
            `GithubObject.NotSet` → `NotSet` in the body.

        """
        lines_list = src.split("\n")

        # --- Strategy A: Find `from .X import X` where body uses `X.X(` ---
        # Build map of: module_name -> set of imported names
        class_import_pattern = re.compile(r"^from \.(\w+) import (.+)$")

        # Collect all `from .X import Y,Z,...` where X == one of the imported names
        class_imports: dict[str, tuple[int, list[str]]] = {}  # module -> (line_idx, [names])

        # Track whether we're inside a TYPE_CHECKING block
        in_type_checking = False
        type_checking_indent = 0

        for i, line in enumerate(lines_list):
            stripped = line.strip()

            # Detect TYPE_CHECKING blocks
            if stripped.startswith("if TYPE_CHECKING"):
                in_type_checking = True
                type_checking_indent = len(line) - len(line.lstrip())
                continue
            if in_type_checking:
                if stripped and not stripped.startswith("#"):
                    line_indent = len(line) - len(line.lstrip())
                    if line_indent <= type_checking_indent and not stripped.startswith(("from ", "import ")):
                        in_type_checking = False
                    elif line_indent <= type_checking_indent and stripped.startswith(("class ", "def ")):
                        in_type_checking = False

            # Skip imports inside TYPE_CHECKING blocks — they're type-only
            if in_type_checking:
                continue

            m = class_import_pattern.match(stripped)
            if m:
                mod_name = m.group(1)
                names_str = m.group(2)
                names = cls._split_import_names(names_str)
                if "(" in names_str and ")" not in names_str:
                    # Multi-line import: collect names until the closing ")"
                    for j in range(i + 1, len(lines_list)):
                        part = lines_list[j].strip()
                        names.extend(cls._split_import_names(part))
                        if ")" in part:
                            break
                class_imports[mod_name] = (i, names)

        # For each module X where X is also imported as a class name AND body uses X.X(,
        # replace X.X with just X (since we have the class import).
        # Also handle X.Y patterns where Y is another class in the same module.
        modules_with_double_deref: set[str] = set()
        for mod_name, (line_idx, names) in class_imports.items():
            if mod_name not in names:
                continue  # Class import doesn't import same-name class, skip
            # Check if body uses X.X — double dereference
            body = "\n".join(lines_list[line_idx + 1 :])
            dbl_deref = re.search(rf"\b{re.escape(mod_name)}\.{re.escape(mod_name)}\b", body)
            if dbl_deref:
                modules_with_double_deref.add(mod_name)

        src = "\n".join(lines_list)

        # Strategy A: Replace X.X → X in the body (class constructor via module dereference).
        # Since `from .X import X` imports the CLASS, `X(...)` is the same as `X.X(...)`.
        for mod_name in modules_with_double_deref:
            logger.debug("fix_double_deref: Strategy A — replacing %s.%s → %s", mod_name, mod_name, mod_name)
            # Replace X.X with just X — but be careful not to affect strings/comments
            # or patterns like X.X.something (which would become X.something).
            # The pattern: word-boundary + ModName + . + ModName + word-boundary
            src = re.sub(
                rf"\b{re.escape(mod_name)}\.{re.escape(mod_name)}\b",
                mod_name,
                src,
            )

        # --- Strategy B: Replace GithubObject.NotSet → NotSet, etc. ---
        # For modules where we imported individual names (like NotSet, Attribute, etc.),
        # replace qualified references with bare names.
        # Only do this for GithubObject since it's the main source of this pattern.
        # Find all names imported from .GithubObject
        go_names: set[str] = set()
        for m in re.finditer(r"from \.GithubObject import ([^;\n]+)", src):
            import_text = m.group(1)
            # Handle parenthesized imports
            if "(" in import_text:
                start = m.start(1)
                paren_content = src[start:]
                close = paren_content.find(")")
                if close != -1:
                    import_text = paren_content[: close + 1]
            go_names.update(cls._split_import_names(import_text, identifiers_only=True))

        if go_names:
            logger.debug("fix_double_deref: Strategy B — replacing GithubObject.X → X for: %s", sorted(go_names))
            # Replace GithubObject.X → X for each imported name X, but only when
            # GithubObject refers to the CLASS (i.e., from .GithubObject import GithubObject)
            # and the code accesses GithubObject.X where X is an imported name.
            for name in go_names:
                # Only replace GithubObject.name when 'name' is imported
                # Use word boundary to avoid partial matches
                src = re.sub(
                    rf"\bGithubObject\.{re.escape(name)}\b",
                    name,
                    src,
                )

        return src

    def _transform_class(self, src: str, class_name: str, stem: str) -> str:
        """
        Transform methods in a class to be async.
        """
        methods = self.analyzer.async_methods.get(class_name, set())
        logger.debug("transform_class: %s — %d methods to make async: %s", class_name, len(methods), sorted(methods))

        for method_name in methods:
            # Skip __init__ and other never-async methods
            if method_name in NEVER_ASYNC_METHODS:
                logger.debug("transform_class: %s.%s — skipped (NEVER_ASYNC)", class_name, method_name)
                continue
            # Add async to def
            src = self._make_method_async(src, class_name, method_name)

        # For methods that call other async methods, add await
        src = self._add_awaits(src, class_name, stem)

        # Phase G: Chained awaits — handle (await EXPR).ATTR chains
        # After _add_awaits creates (await self.prop).something, resolve whether
        # .something is also async on the resolved type, and add outer await.
        # Run multiple passes since chains can be deep (e.g. (await self.head).repo.owner.login).
        src = self._add_chained_awaits(src, class_name)

        # Phase I: Break async method chains — handle cases where an async method call
        # has further .attr/.method() chained after its call parens.
        # E.g. "await repo.get_git_ref(args).delete()" is wrong because get_git_ref()
        # returns a coroutine and .delete() is called on the coroutine.
        # Fix: split into temp variable "(_tmp = await repo.get_git_ref(args))" + "_tmp.delete()".
        src = self._break_async_method_chains(src, class_name)

        # Phase J: Add # type: ignore[override] to sync @property definitions that
        # override an async property from a base class. mypy flags these as signature
        # mismatches (str vs Coroutine[Any, Any, str]).
        src = self._annotate_sync_property_overrides(src, class_name)

        return src

    def _make_method_async(self, src: str, class_name: str, method_name: str) -> str:
        """
        Convert 'def method_name(' to 'async def method_name(' within a class.
        """
        # Never make __init__ async
        if method_name in NEVER_ASYNC_METHODS:
            return src

        # Handle both regular and name-mangled private methods
        # Match 'def method(' but not 'async def method(' (avoid double-async)
        pattern = rf"(^[ \t]+)(def {re.escape(method_name)}\s*\()"

        made_async = False

        def _replace(m):
            nonlocal made_async
            indent = m.group(1)
            defpart = m.group(2)
            # Check if 'async ' already precedes 'def'
            line_start = src[: m.start()].rfind("\n") + 1
            prefix = src[line_start : m.start() + len(indent)]
            if "async" in prefix:
                return m.group(0)  # Already async
            made_async = True
            return f"{indent}async {defpart}"

        src = re.sub(pattern, _replace, src, flags=re.MULTILINE)

        if made_async:
            logger.debug("make_method_async: %s.%s — converted to async def", class_name, method_name)

        return src

    def _add_awaits(self, src: str, class_name: str, stem: str = "") -> str:
        """
        Add await before calls to async methods.
        """
        methods = set(self.analyzer.async_methods.get(class_name, set()))
        # Include inherited async methods from ALL ancestor classes (full MRO)
        for base in self.analyzer._get_mro(class_name):
            methods |= self.analyzer.async_methods.get(base, set())

        logger.debug(
            "add_awaits[%s]: %d async methods (including inherited): %s",
            class_name,
            len(methods),
            sorted(methods),
        )

        # For self.method() calls where method is async - batch into a single regex
        present_methods = [m for m in methods if m not in NEVER_ASYNC_METHODS and m in src]
        if present_methods:
            # Batch: combine all method names into one alternation pattern for a single pass
            alt = "|".join(re.escape(m) for m in sorted(present_methods, key=len, reverse=True))
            src = self._safe_add_await(src, rf"(?<!\w)self\.(?:{alt})\s*\(")

        # Handle name-mangled versions for private methods
        mangled_methods = []
        for method in present_methods:
            if method.startswith("__") and not method.endswith("__"):
                mangled = f"_{class_name}{method}"
                if mangled in src:
                    mangled_methods.append(mangled)
        if mangled_methods:
            alt = "|".join(re.escape(m) for m in mangled_methods)
            src = self._safe_add_await(src, rf"(?<!\w)self\.(?:{alt})\s*\(")

        # super().method( -> await super().method( — batch
        if "super()" in src:
            super_methods = [m for m in present_methods if m in src]
            if super_methods:
                alt = "|".join(re.escape(m) for m in sorted(super_methods, key=len, reverse=True))
                src = self._safe_add_await(src, rf"super\(\)\.(?:{alt})\s*\(")

        # For async properties: self.prop (no parentheses) -> await self.prop
        # Gather promoted properties for this class + all ancestors
        promoted = set(self.analyzer.promoted_properties.get(class_name, set()))
        promoted |= self.analyzer._get_inherited_promoted(class_name)

        # Exclude inherited promoted properties that the current class overrides
        # with a sync @property (e.g. CheckRun.url is sync even though the base
        # CompletableGithubObject.url is promoted to async).
        local_sync_props = self.analyzer.property_methods.get(class_name, set())
        local_promoted = self.analyzer.promoted_properties.get(class_name, set())
        sync_overrides = local_sync_props - local_promoted
        if sync_overrides & promoted:
            logger.debug(
                "add_awaits[%s]: excluding %d sync property override(s) from promoted set: %s",
                class_name,
                len(sync_overrides & promoted),
                sorted(sync_overrides & promoted),
            )
            promoted -= sync_overrides

        if promoted:
            logger.debug(
                "add_awaits[%s]: %d promoted properties (including inherited): %s",
                class_name,
                len(promoted),
                sorted(promoted),
            )

        for prop in promoted:
            if prop in NEVER_ASYNC_METHODS:
                continue
            # Fast pre-check: skip if property name doesn't appear in source
            if prop not in src:
                continue
            # Match self.prop NOT followed by ( (not a method call — those are handled above)
            # and NOT being a definition line (def prop or async def prop)
            # and NOT being an assignment target (self.prop =)
            # Use _safe_add_await_property which handles the no-parens case
            src = self._safe_add_await_property(src, prop)

        # For cross-object property access: var.prop where var is NOT self.
        # Use per-method type-registry-based rules computed from annotations.
        # Per-method rules avoid variable name collisions across methods (e.g.
        # 'element' being a CompletableGithubObject in one method but a plain
        # class in another).
        per_method_rules = self.analyzer.compute_cross_object_rules_per_method(class_name)

        if per_method_rules:
            # Apply cross-object rules to each method's source separately.
            src = self._apply_per_method_cross_object_rules(src, class_name, per_method_rules)

        # For requester method calls
        present_req_methods = [m for m in sorted(REQUESTER_AWAIT_METHODS) if m in src]
        if present_req_methods:
            req_alt = "|".join(re.escape(m) for m in sorted(present_req_methods, key=len, reverse=True))
            # Match various requester access patterns — batch per prefix
            # IMPORTANT: Use word boundary / specific prefixes to avoid
            # 'requester\.' matching inside 'self.__requester.'
            for prefix in [
                r"self\._requester\.",
                r"self\.__requester\.",
                r"self\._requester\._Requester__",
            ]:
                src = self._safe_add_await(src, rf"{prefix}(?:{req_alt})\s*\(")

            # For bare 'requester.method(' - batch
            src = self._safe_add_await(src, rf"(?<!\w)(?<!_)(?<!\.)requester\.(?:{req_alt})\s*\(")

        # For connection class method calls (getresponse is async, request is sync)
        if class_name == "Requester" or class_name in CONNECTION_CLASSES:
            src = self._safe_add_await(src, r"(?<!\w)cnx\.getresponse\s*\(")
            # Note: cnx.request() is intentionally NOT awaited - it just stores parameters
            # verb(...) calls in connection classes - these are HTTP session methods
            # Match 'verb(' when it appears in a statement (assigned or standalone)
            # The verb variable holds a session method like session.get, session.post, etc.
            # In async, these are coroutine functions that need await.
            src = self._safe_add_await(src, r"(?<!\w)verb\s*\(")

        # For .complete() calls on local variables (not self).
        # E.g.: user.complete(), repo.complete()
        # These are CompletableGithubObject.complete() which is async.
        src = self._safe_add_await(src, r"(?<!\w)(?<!self\.)\b\w+\.complete\s*\(")

        # Handle .complete() chained on constructor/method calls ending with ')'.
        # E.g.: return ClassName(requester, url=url).complete()
        #     → return await ClassName(requester, url=url).complete()
        # _safe_add_await can't handle this because the match starts at ')',
        # and inserting 'await' there gives wrong placement. Instead, use a
        # line-level regex that inserts 'await' after 'return' or '='.
        src = re.sub(
            r"^(\s*(?:return\s+))(?!await\b)(.*\)\.complete\s*\(\s*\))",
            r"\1await \2",
            src,
            flags=re.MULTILINE,
        )
        src = re.sub(
            r"^(\s*\w[\w\s,]*=\s*)(?!await\b)(.*\)\.complete\s*\(\s*\))",
            r"\1await \2",
            src,
            flags=re.MULTILINE,
        )

        # Phase H: Static/classmethod calls via Module.ClassName.method()
        # Only check methods that are @staticmethod/@classmethod (small set).
        for cls_name, statics in self.analyzer.static_methods.items():
            if cls_name not in src:
                continue
            cls_async = self.analyzer.async_methods.get(cls_name, set())
            async_statics = [m for m in (statics & cls_async) if m not in NEVER_ASYNC_METHODS and m in src]
            if not async_statics:
                continue
            alt = "|".join(re.escape(m) for m in sorted(async_statics, key=len, reverse=True))
            # Match the qualified runtime form `githubasyncio.Module.ClassName.method(` (see
            # _fix_imports) or the bare same-file self-reference `ClassName.method(`.
            mod_name = self.analyzer.class_to_file.get(cls_name, cls_name)
            src = self._safe_add_await(
                src,
                rf"(?<!\w)githubasyncio\.{re.escape(mod_name)}\.{re.escape(cls_name)}\.(?:{alt})\s*\(",
            )
            src = self._safe_add_await(
                src,
                rf"(?<!\w)(?<!\.){re.escape(cls_name)}\.(?:{alt})\s*\(",
            )

        # Phase I: Inline construction → async method call:
        # ClassName(...).async_method(...) needs await because async_method is async.
        # Batch per class: combine all async methods into one alternation pattern.
        for cls_name in self.analyzer.async_classes:
            # Fast pre-check: class name must appear in source
            if cls_name not in src:
                continue
            cls_async = self.analyzer.async_methods.get(cls_name, set())
            present_methods = [m for m in cls_async if m not in NEVER_ASYNC_METHODS and m in src]
            if not present_methods:
                continue
            alt = "|".join(re.escape(m) for m in sorted(present_methods, key=len, reverse=True))
            src = self._safe_add_await(
                src,
                rf"(?<!\w){re.escape(cls_name)}\([^)]*\)\.(?:{alt})\s*\(",
            )

        return src

    def _apply_per_method_cross_object_rules(
        self,
        src: str,
        class_name: str,
        per_method_rules: dict[str, tuple[dict[str, set[str]], dict[str, set[str]]]],
    ) -> str:
        """
        Apply cross-object property/method await rules per-method.

        Splits the source into method sections, applies each method's specific rules (from per_method_rules) only to
        that method's body, then reassembles. This prevents variable-name collisions across methods.

        """
        lines = src.split("\n")
        # Identify method boundaries: [(method_name, start_line, end_line), ...]
        # where line indices are 0-based
        method_spans: list[tuple[str, int, int]] = []
        i = 0
        while i < len(lines):
            stripped = lines[i].lstrip()
            if stripped.startswith("async def ") or stripped.startswith("def "):
                # Extract method name
                if stripped.startswith("async def "):
                    name_part = stripped[len("async def ") :]
                else:
                    name_part = stripped[len("def ") :]
                meth_name = name_part.split("(")[0].strip()
                indent = len(lines[i]) - len(stripped)
                start = i
                i += 1
                # Skip past multi-line signature: find the line ending with ':'
                # that closes the signature (after all parameters).
                sig_complete = ":" in stripped.split(")", 1)[-1] if ")" in stripped else False
                while i < len(lines) and not sig_complete:
                    s = lines[i].lstrip()
                    if ")" in s:
                        after_paren = s.split(")", 1)[-1]
                        if ":" in after_paren:
                            sig_complete = True
                    i += 1
                if not sig_complete:
                    # Signature never completed — treat the rest as body
                    method_spans.append((meth_name, start, len(lines)))
                    break
                i += 1  # move past the signature-closing line
                # Now find end of method body: next line at same or lower indent
                # that is not blank/comment and starts something new
                while i < len(lines):
                    s = lines[i].lstrip()
                    cur_indent = len(lines[i]) - len(s)
                    if s and cur_indent <= indent and not s.startswith("#"):
                        break
                    i += 1
                method_spans.append((meth_name, start, i))
            else:
                i += 1

        # For each method that has rules, extract its source, apply rules, replace
        # We process in reverse order to maintain line indices
        for meth_name, start, end in reversed(method_spans):
            if meth_name not in per_method_rules:
                continue
            prop_rules, method_rules = per_method_rules[meth_name]

            # Extract method source
            method_src = "\n".join(lines[start:end])

            for prop, allowed_vars in sorted(prop_rules.items()):
                logger.debug(
                    "add_awaits[%s.%s]: cross-object property '%s' (vars=%s)",
                    class_name,
                    meth_name,
                    prop,
                    sorted(allowed_vars),
                )
                method_src = self._safe_add_await_cross_object_property(method_src, prop, restrict_vars=allowed_vars)

            for meth, allowed_vars in sorted(method_rules.items()):
                logger.debug(
                    "add_awaits[%s.%s]: cross-object method '%s' (vars=%s)",
                    class_name,
                    meth_name,
                    meth,
                    sorted(allowed_vars),
                )
                method_src = self._safe_add_await_cross_object_method(method_src, meth, restrict_vars=allowed_vars)

            # Replace method lines
            new_method_lines = method_src.split("\n")
            lines[start:end] = new_method_lines

        return "\n".join(lines)

    def _add_chained_awaits(self, src: str, class_name: str) -> str:
        """Phase G: Add await to chained attribute accesses after (await ...).

        After earlier phases create patterns like ``(await self.owner).login``,
        this pass checks whether ``.login`` is async on the resolved type of
        ``owner``, and if so wraps with ``await``.

        Handles:
        - ``(await self.PROP).ATTR`` → ``await (await self.PROP).ATTR`` (property)
        - ``(await self.PROP).METHOD(`` → ``await (await self.PROP).METHOD(`` (method)
        - ``(await VAR.PROP).ATTR`` → ``await (await VAR.PROP).ATTR`` (cross-object)
        - Multi-segment chains: ``(await self.PROP).X.Y`` where X is sync → resolves
          through X's type to check if Y is async.

        Runs multiple passes until no more changes (chains can be multi-level).
        """
        # Build per-method variable type map for cross-object resolution
        all_method_var_types = self.analyzer.get_all_method_var_types(class_name)

        max_passes = 5
        for pass_num in range(max_passes):
            new_src = self._chained_await_pass(src, class_name, all_method_var_types)
            if new_src == src:
                break
            logger.debug(
                "chained_awaits[%s]: pass %d made changes",
                class_name,
                pass_num + 1,
            )
            src = new_src
        return src

    def _annotate_sync_property_overrides(self, src: str, class_name: str) -> str:
        """Phase J: Add ``# type: ignore[override]`` to sync @property defs that
        override an async property inherited from a base class.

        mypy reports these as signature mismatches (e.g. ``str`` vs
        ``Coroutine[Any, Any, str]``).  The override is intentional — the
        subclass property does *not* need completion so it stays sync.
        """
        # Compute which properties are sync overrides of inherited async ones
        inherited_promoted = self.analyzer._get_inherited_promoted(class_name)
        if not inherited_promoted:
            return src

        local_sync_props = self.analyzer.property_methods.get(class_name, set())
        local_promoted = self.analyzer.promoted_properties.get(class_name, set())
        sync_overrides = (local_sync_props - local_promoted) & inherited_promoted

        if not sync_overrides:
            return src

        for prop in sync_overrides:
            # Match the def line for this property within the class body.
            # Pattern: indented 'def prop(self' possibly with return annotation, colon, rest
            pattern = rf"(^[ \t]+def {re.escape(prop)}\(self[^)]*\)[^:\n]*:)(.*)"

            def _add_ignore(m):
                defline = m.group(1)
                rest = m.group(2)
                if "type: ignore" in rest:
                    return m.group(0)  # Already annotated
                return f"{defline}  # type: ignore[override]{rest}"

            src = re.sub(pattern, _add_ignore, src, count=1, flags=re.MULTILINE)

        logger.debug(
            "annotate_sync_overrides[%s]: added type: ignore[override] to %s",
            class_name,
            sorted(sync_overrides),
        )
        return src

    def _break_async_method_chains(self, src: str, class_name: str) -> str:
        """Phase I: Break chains where an async method call has further accesses.

        Detects patterns like ``await EXPR.async_method(ARGS).next(...)`` where
        ``.async_method()`` returns a coroutine in async mode and ``.next()``
        would be called on the coroutine object (a bug).

        Rewrites as::

            _chain_tmp = await EXPR.async_method(ARGS)
            await _chain_tmp.complete()  # if return type is CompletableGithubObject
            ... _chain_tmp.next(...) ...

        Only triggers when the chained method is known to be async.
        """
        # Collect all async methods across all classes for quick lookup
        all_async: dict[str, set[str]] = self.analyzer.async_methods
        # Build a flat set of all method names that are async on any class
        any_async_method: set[str] = set()
        for methods in all_async.values():
            any_async_method |= methods

        # Build set of method names that return CompletableGithubObject on any class
        completable_return_methods: set[str] = set()
        for cls_name, attrs in self.analyzer.return_types.items():
            for attr_name, return_types in attrs.items():
                if return_types & self.analyzer.completable_classes:
                    completable_return_methods.add(attr_name)

        lines = src.split("\n")
        result_lines: list[str] = []
        temp_counter = 0

        for line in lines:
            # Look for patterns: await STUFF.METHOD(
            # where METHOD is an async method name and there's .something after the call
            new_line = self._break_chain_in_line(line, any_async_method, completable_return_methods, class_name)
            if new_line is not None:
                result_lines.extend(new_line)
                temp_counter += 1
            else:
                result_lines.append(line)

        if temp_counter > 0:
            logger.debug(
                "break_async_method_chains[%s]: split %d chains",
                class_name,
                temp_counter,
            )

        return "\n".join(result_lines)

    def _break_chain_in_line(
        self, line: str, any_async_method: set[str], completable_return_methods: set[str], class_name: str
    ) -> list[str] | None:
        """
        Try to break an async method chain in a single line.

        Returns a list of replacement lines, or None if no change needed.

        Detects: ``await PREFIX.async_method(ARGS).SUFFIX``
        Rewrites as:
            ``_chain_tmp = await PREFIX.async_method(ARGS)``
            ``await _chain_tmp.complete()``  # if method returns CompletableGithubObject
            ``[original line with chain replaced by _chain_tmp.SUFFIX]``

        """
        stripped = line.lstrip()
        indent = line[: len(line) - len(stripped)]

        # Find "await " followed by an expression containing .method(args).something
        # We need to find: .METHOD( where METHOD is async, balance parens, then check for .SUFFIX
        # Strategy: find all .IDENT( patterns, check if IDENT is async, balance, check suffix
        for m in re.finditer(r"\.(\w+)\s*\(", line):
            method_name = m.group(1)
            if method_name not in any_async_method:
                continue

            # Check that this method call is preceded by "await " somewhere
            # (could be at start of expression, or after return/=)
            before_dot = line[: m.start()]
            if "await " not in before_dot:
                continue

            # Find the opening paren
            paren_open = m.end() - 1  # position of '('
            # Balance parens to find closing
            depth = 1
            pos = paren_open + 1
            while pos < len(line) and depth > 0:
                ch = line[pos]
                if ch == "(":
                    depth += 1
                elif ch == ")":
                    depth -= 1
                elif ch in ('"', "'"):
                    # Skip strings (simplified — handles basic f-strings)
                    quote = ch
                    pos += 1
                    while pos < len(line) and line[pos] != quote:
                        if line[pos] == "\\":
                            pos += 1  # skip escaped char
                        pos += 1
                    # pos is now on closing quote
                pos += 1

            if depth != 0:
                continue  # unbalanced — spans multiple lines, skip

            paren_close = pos  # position after ')'

            # Check if there's .SOMETHING after the closing paren
            rest = line[paren_close:]
            chain_match = re.match(r"\.(\w+)", rest)
            if not chain_match:
                continue  # no chain after call — fine, no problem

            # We found a chain: .method(args).next_thing
            # Find the "await" that covers this expression
            await_match = re.search(r"\bawait\s+", before_dot)
            if not await_match:
                continue

            # The await starts at await_match.start()
            await_start = await_match.start()
            # The chain call ends at paren_close
            # Everything from await through the call args is the expression to extract
            call_expr = line[await_start:paren_close]  # "await ...method(args)"
            suffix = line[paren_close:]  # ".delete()" etc.

            # Generate temp variable name
            tmp_var = f"_chain_{method_name}"

            # Build the result lines
            result = []

            # 1. Assignment: _chain_METHOD = await PREFIX.METHOD(ARGS)
            assign_line = f"{indent}{tmp_var} = {call_expr}"
            result.append(assign_line)

            # 2. If the method returns a CompletableGithubObject, add complete() call.
            # In async mode, __init__ can't auto-complete (no await in __init__),
            # so we need an explicit complete() to match sync behavior.
            if method_name in completable_return_methods:
                result.append(f"{indent}await {tmp_var}.complete()")

            # 3. Build the replacement expression: replace the entire
            # "await ...method(args).suffix" with tmp_var.suffix handling
            prefix_before_await = line[:await_start]
            replacement_expr = f"{tmp_var}{suffix}"

            # Check if suffix contains an async method call that needs await
            suffix_method_match = re.match(r"\.(\w+)\s*\(", suffix)
            if suffix_method_match and suffix_method_match.group(1) in any_async_method:
                replacement_expr = f"await {replacement_expr}"

            result_line = f"{prefix_before_await}{replacement_expr}"
            result.append(result_line)

            logger.debug(
                "break_chain[%s]: split '%s' into temp var '%s'%s",
                class_name,
                line.strip()[:80],
                tmp_var,
                " (with complete())" if method_name in completable_return_methods else "",
            )

            return result

        return None

    @staticmethod
    def _find_paren_end(src: str, open_pos: int) -> int:
        """
        Return the index just past the ``)`` matching the ``(`` at ``open_pos``.

        Returns -1 if the parenthesis is never balanced within ``src`` (e.g. the expression spans multiple lines).
        Note: does not skip parens inside string literals.

        """
        depth = 1
        j = open_pos + 1
        while j < len(src) and depth > 0:
            if src[j] == "(":
                depth += 1
            elif src[j] == ")":
                depth -= 1
            j += 1
        return j if depth == 0 else -1

    def _chained_await_pass(
        self, src: str, class_name: str, all_method_var_types: dict[str, dict[str, set[str]]] | None = None
    ) -> str:
        """
        Single pass of chained-await resolution.

        Finds ``(await EXPR).chain`` patterns and wraps with ``await`` where
        the chain accesses async attributes/methods.

        Also finds ``EXPR.chain`` patterns (without initial await) where EXPR
        resolves to a type with async attributes in the chain — e.g.
        ``(await self.head).repo.owner.login`` where ``.repo`` is sync but
        ``.owner`` is async.

        Strategy: find ``(await EXPR)`` blocks, parse the chain after them,
        walk the chain type-by-type, and when an async access is found,
        wrap from the start up to (and including) that async attribute in
        ``(await ...)`` or prepend ``await``.

        """
        # Pre-compute method boundaries for variable type lookup.
        # We scan for 'def method(' and 'async def method(' patterns and record
        # (char_position, method_name) so we can determine which method any
        # position in the source belongs to.
        method_positions: list[tuple[int, str]] = []
        if all_method_var_types:
            for m in re.finditer(r"(?:async\s+)?def\s+(\w+)\s*\(", src):
                method_positions.append((m.start(), m.group(1)))
            method_positions.sort()

        def _get_method_var_types(pos: int) -> dict[str, set[str]]:
            """
            Get variable types for the method containing ``pos``.
            """
            if not method_positions or not all_method_var_types:
                return {}
            # Binary search for the latest method start before pos
            method_name = None
            for mpos, mname in method_positions:
                if mpos <= pos:
                    method_name = mname
                else:
                    break
            if method_name and method_name in all_method_var_types:
                return all_method_var_types[method_name]
            return {}

        result = []
        i = 0
        changed = False

        while i < len(src):
            if src[i : i + 7] == "(await ":
                # Check if already preceded by "await "
                lookback = src[max(0, i - 20) : i]
                already_awaited = bool(re.search(r"await\s+$", lookback))

                # Find the matching closing paren
                paren_start = i
                paren_end = self._find_paren_end(src, paren_start)  # index past ')'

                if paren_end == -1:
                    result.append(src[i])
                    i += 1
                    continue

                inner = src[paren_start + 1 : paren_end - 1]  # "await ..."

                # Check what follows the closing paren
                after = src[paren_end:]
                if not after.startswith("."):
                    result.append(src[i:paren_end])
                    i = paren_end
                    continue

                # Parse the full chain after (await EXPR)
                chain_parts = self._parse_chain(src, paren_end)
                if not chain_parts:
                    result.append(src[i:paren_end])
                    i = paren_end
                    continue

                # Resolve the type of the (await EXPR) result
                method_vt = _get_method_var_types(paren_start)
                base_types = self._resolve_await_expr_type(inner, class_name, method_vt)
                if not base_types:
                    result.append(src[i:paren_end])
                    i = paren_end
                    continue

                # Walk the chain to find the FIRST async access point
                async_at, chain_char_lens = self._find_first_async_in_chain(base_types, chain_parts)

                if async_at is None:
                    # No async access in chain — emit as-is
                    result.append(src[i:paren_end])
                    i = paren_end
                    continue

                if already_awaited:
                    # Already have "await (await self.X).Y..." — the outer await
                    # covers the entire chain, regardless of which segment is async.
                    # Skip to avoid runaway await multiplication.
                    result.append(src[i:paren_end])
                    i = paren_end
                    continue

                # Calculate the end position of the async attribute in source
                chars_consumed = sum(chain_char_lens[: async_at + 1])
                full_end = paren_end + chars_consumed

                if async_at == 0 and not already_awaited:
                    # The first chain segment is async — prepend "await "
                    # Check if it's a method call at the end
                    name, is_call = chain_parts[async_at]
                    if is_call:
                        # Method call: await (await self.X).method(
                        result.append("await ")
                        result.append(src[paren_start:full_end])
                    else:
                        # Property: await (await self.X).prop → becomes
                        # (await (await self.X).prop) if there are more chain segments,
                        # or await (await self.X).prop if terminal
                        remaining_chain = src[full_end:]
                        if remaining_chain.startswith("."):
                            result.append("(await ")
                            result.append(src[paren_start:full_end])
                            result.append(")")
                        else:
                            result.append("await ")
                            result.append(src[paren_start:full_end])
                    i = full_end
                    changed = True
                    logger.debug(
                        "chained_awaits[%s]: added await (async_at=0) to '%s'",
                        class_name,
                        src[paren_start:full_end][:80],
                    )
                elif async_at > 0:
                    # An intermediate segment is async — we need to wrap
                    # (await self.X).sync1.sync2.asyncProp into
                    # (await (await self.X).sync1.sync2.asyncProp)
                    # The next pass will then handle further chain.
                    name, is_call = chain_parts[async_at]
                    remaining_chain = src[full_end:]
                    if is_call:
                        result.append("await ")
                        result.append(src[paren_start:full_end])
                    elif remaining_chain.startswith("."):
                        result.append("(await ")
                        result.append(src[paren_start:full_end])
                        result.append(")")
                    else:
                        result.append("await ")
                        result.append(src[paren_start:full_end])
                    i = full_end
                    changed = True
                    logger.debug(
                        "chained_awaits[%s]: added await (async_at=%d) to '%s'",
                        class_name,
                        async_at,
                        src[paren_start:full_end][:80],
                    )
                else:
                    result.append(src[i:paren_end])
                    i = paren_end
            else:
                result.append(src[i])
                i += 1

        if not changed:
            return src
        return "".join(result)

    @staticmethod
    def _parse_chain(src: str, start: int) -> list[tuple[str, bool]]:
        """
        Parse a chain of .attr or .method( starting at position ``start``.

        Returns a list of (name, is_call) tuples. ``is_call`` is True if
        the segment is a method call (followed by ``(``).

        """
        parts: list[tuple[str, bool]] = []
        pos = start
        while pos < len(src) and src[pos] == ".":
            pos += 1  # skip '.'
            # Read identifier
            ident_start = pos
            while pos < len(src) and (src[pos].isalnum() or src[pos] == "_"):
                pos += 1
            if pos == ident_start:
                break  # no identifier after '.'
            ident = src[ident_start:pos]
            # Check if followed by '(' (method call) — skip whitespace
            save_pos = pos
            while pos < len(src) and src[pos] in " \t":
                pos += 1
            if pos < len(src) and src[pos] == "(":
                parts.append((ident, True))
                # Don't consume past '(' — we just note it's a call
                pos = save_pos  # restore to just after ident (before whitespace/paren)
                break  # stop chain after method call
            else:
                parts.append((ident, False))
                pos = save_pos  # restore to just after ident
                # Continue — there might be more .attr segments
        return parts

    def _resolve_await_expr_type(
        self, await_expr: str, class_name: str, method_var_types: dict[str, set[str]] | None = None
    ) -> set[str]:
        """
        Resolve the type that an ``await EXPR`` evaluates to.

        Given the inner content of ``(await EXPR)`` — i.e. ``await self.prop``
        or ``await var.prop`` — determine the return type.

        Handles:
          - ``await self.prop`` → resolve_type(class_name, prop)
          - ``await (await INNER).chain.of.attrs`` → recursive resolution
          - ``await var.prop`` → uses method_var_types if available

        """
        # Strip the leading "await " prefix
        expr = await_expr.strip()
        if expr.startswith("await "):
            expr = expr[6:].strip()

        # Handle nested (await EXPR).chain: e.g. "(await self.head).repo.owner"
        if expr.startswith("(await "):
            # Find the matching close paren for the inner (await ...)
            inner_paren_end = self._find_paren_end(expr, 0)  # position after ')'
            if inner_paren_end != -1:
                inner_content = expr[1 : inner_paren_end - 1]  # "await ..."
                # Recursively resolve the inner type
                inner_types = self._resolve_await_expr_type(inner_content, class_name, method_var_types)
                if inner_types:
                    # Walk the chain after the inner (await ...) block
                    remaining = expr[inner_paren_end:]  # e.g. ".repo.owner"
                    if remaining.startswith("."):
                        current_types = inner_types
                        # Parse the chain segments
                        parts = remaining.split(".")
                        for part in parts:
                            part = part.strip()
                            if not part:
                                continue
                            # Strip any trailing call parens or brackets
                            ident = re.match(r"^([a-zA-Z_]\w*)", part)
                            if not ident:
                                break
                            attr_name = ident.group(1)
                            next_types: set[str] = set()
                            for t in current_types:
                                next_types |= self.analyzer.resolve_type(t, attr_name)
                            if not next_types:
                                return current_types  # Can't resolve further, return last known
                            current_types = next_types
                        return current_types
                    else:
                        return inner_types

        # Handle simple: self.PROP
        if expr.startswith("self."):
            prop = expr[5:]
            # prop might be a simple name or a chain itself
            # For simple case: self.prop
            if re.match(r"^[a-zA-Z_]\w*$", prop):
                return self.analyzer.resolve_type(class_name, prop)

        # Handle cross-object: var.prop — use method_var_types if available
        if method_var_types:
            m = re.match(r"^([a-zA-Z_]\w*)\.(.+)$", expr)
            if m:
                var_name = m.group(1)
                chain_str = m.group(2)
                if var_name in method_var_types:
                    current_types = method_var_types[var_name]
                    # Walk the chain
                    for attr_name in chain_str.split("."):
                        attr_name = attr_name.strip()
                        ident = re.match(r"^([a-zA-Z_]\w*)", attr_name)
                        if not ident:
                            break
                        next_types: set[str] = set()
                        for t in current_types:
                            next_types |= self.analyzer.resolve_type(t, ident.group(1))
                        if not next_types:
                            return current_types
                        current_types = next_types
                    return current_types

        return set()

    def _find_first_async_in_chain(
        self,
        base_types: set[str],
        chain: list[tuple[str, bool]],
    ) -> tuple[int | None, list[int]]:
        """
        Walk a chain and find the index of the first async access.

        Starting from ``base_types``, walk each segment. For each:
        - If async → return its index.
        - If sync → resolve next type and continue.

        Returns:
            (async_index_or_None, list_of_char_lengths_per_segment)
            char_lengths[i] = 1 + len(name) for segment i (the dot + identifier)

        """
        current_types = base_types
        char_lens: list[int] = []

        for idx, (name, is_call) in enumerate(chain):
            segment_len = 1 + len(name)  # dot + identifier
            char_lens.append(segment_len)

            if self.analyzer.is_attr_async_on_type(current_types, name):
                return idx, char_lens

            if is_call:
                # Sync method call — can't continue chain
                return None, char_lens

            # Sync property/attribute — resolve type for next segment
            next_types: set[str] = set()
            for t in current_types:
                next_types |= self.analyzer.resolve_type(t, name)
            if not next_types:
                return None, char_lens
            current_types = next_types

        return None, char_lens

    @staticmethod
    def _transform_async_def_lines(src: str, transform: Callable[[str], str], track_docstrings: bool = False) -> str:
        """
        Apply ``transform`` to each source line that is inside an ``async def`` body.

        Shared line-walking state machine for the ``_safe_add_await_*`` helpers.
        Tracks function context line by line; only lines inside ``async def``
        bodies are passed to ``transform``.  Everything else — sync def bodies,
        def signature lines (including multi-line signatures), decorators,
        comments, blank lines, module level code — is left untouched.

        With ``track_docstrings=True``, lines inside triple-quoted blocks are
        also left untouched.

        """
        lines = src.split("\n")
        result_lines = []
        # func_indent = indent level of the current def/async def line.
        # Any line with indent > func_indent is inside the function body.
        in_async_func = False
        func_indent = -1
        in_signature = False  # True while we're in a multi-line def signature
        in_docstring = False  # True while inside a triple-quoted block

        for line in lines:
            stripped = line.lstrip()
            indent = len(line) - len(stripped)

            # Track triple-quoted strings (docstrings): count occurrences to toggle state.
            # An even count means the line is self-contained (no quotes, or open+close).
            if track_docstrings:
                triple_count = stripped.count('"""') + stripped.count("'''")
                if in_docstring:
                    if triple_count % 2 == 1:
                        in_docstring = False
                    result_lines.append(line)
                    continue
                if triple_count % 2 == 1:
                    in_docstring = True
                    result_lines.append(line)
                    continue

            # Track function definitions
            if stripped.startswith("async def ") or stripped.startswith("def "):
                in_async_func = stripped.startswith("async def ")
                func_indent = indent
                # Signature is complete on this line if ':' follows the closing ')'
                in_signature = ":" not in stripped.split(")", 1)[-1] if ")" in stripped else True
                result_lines.append(line)
                continue

            # If we're in a multi-line signature, it ends on the line where ':' follows ')'
            if in_signature:
                if ")" in stripped:
                    after_paren = stripped.split(")", 1)[-1]
                    if ":" in after_paren:
                        in_signature = False
                result_lines.append(line)
                continue

            # Decorators, blank lines and comments don't change function context
            if stripped.startswith(("@", "#")) or not stripped:
                result_lines.append(line)
                continue

            # Dedent to (or above) the def line means we've left the function body
            if func_indent >= 0 and indent <= func_indent:
                in_async_func = False
                func_indent = -1

            if not in_async_func:
                result_lines.append(line)
                continue

            result_lines.append(transform(line))

        return "\n".join(result_lines)

    @classmethod
    def _safe_add_await_property(cls, src: str, prop: str) -> str:
        """
        Add 'await' before self.PROP accesses where PROP is an async property.

        Only adds await inside `async def` functions (not in sync defs like __repr__).

        Matches self.PROP that is NOT:
        - followed by ( or = (not a method call or assignment)
        - on a def/async def line (definition)
        - preceded by 'await' already
        - a decorator line (@property, etc.)

        When self.PROP is followed by '.' (chained access like self.owner.login),
        it wraps with parentheses: (await self.owner).login

        """
        # Pattern: self.prop NOT followed by ( or assignment = (with optional spaces)
        # and NOT preceded by 'await ' and NOT preceded by word char or dot
        # Note: =[^=] excludes assignment (=) but allows comparison (==)
        pattern = rf"(?<!await )(?<!\w)self\.{re.escape(prop)}(?!\s*(?:\(|=[^=]))(?!\w)"
        # Also handle super().prop → await super().prop
        super_pattern = rf"(?<!await )super\(\)\.{re.escape(prop)}(?!\s*(?:\(|=[^=]))(?!\w)"

        def _make_replacer(line: str, base: str) -> Callable[[re.Match], str]:
            def _replace(m: re.Match) -> str:
                # Check what follows the match
                after = line[m.end() :]
                if after.startswith("."):
                    # Chained access: self.prop.something → (await self.prop).something
                    return f"(await {base}.{prop})"
                # Check if we need parens for operator precedence.
                # `await` has very low precedence, so `await x == y` means `await (x == y)`.
                # We need parens when followed by operators: ==, !=, <, >, +, -, *, /, %, etc.
                # We DON'T need parens when followed by: ), ], }, comma, colon, end-of-line,
                # or whitespace before those (the await is a complete sub-expression).
                after_stripped = after.lstrip()
                if after_stripped and after_stripped[0] not in (")", "]", "}", ",", ":", "\n", "#", ""):
                    # Something follows — could be an operator. Use parens for safety.
                    return f"(await {base}.{prop})"
                return f"await {base}.{prop}"

            return _replace

        def transform(line: str) -> str:
            new_line = re.sub(pattern, _make_replacer(line, "self"), line)
            return re.sub(super_pattern, _make_replacer(new_line, "super()"), new_line)

        return cls._transform_async_def_lines(src, transform)

    @classmethod
    def _safe_add_await_cross_object_property(cls, src: str, prop: str, restrict_vars: set[str]) -> str:
        """
        Add 'await' before VARNAME.PROP accesses where PROP is a globally-known async property and VARNAME is NOT
        'self'.

        Only adds await inside `async def` functions.
        Only matches lowercase variable names (to avoid module.prop false positives).
        Handles chained access: var.prop.something -> (await var.prop).something

        Args:
            restrict_vars: Only match these specific variable names (determined by
                           type-registry analysis).

        Excludes:
        - self.prop (handled by _safe_add_await_property)
        - assignments: var.prop =
        - definitions: def prop
        - already-awaited: await var.prop

        """
        # Pattern: word_char_var.prop where var is NOT self
        # Match: lowercase-starting variable name followed by .prop
        # NOT preceded by 'await ' or 'self.' or '.' (not part of chain)
        # NOT followed by ( or assignment = (not a call or assignment)
        # Note: =[^=] excludes assignment (=) but allows comparison (==)
        # var must be at least 1 char, lowercase start (excluding self)
        pattern = (
            rf"(?<!await )(?<!self\.)"
            rf"(?<!\w)(?<!\.)"
            rf"(?!self\.)"
            rf"([a-z_]\w*)\.{re.escape(prop)}"
            rf"(?!\s*(?:\(|=[^=]))(?!\w)"
        )

        def _replace_cross(m: re.Match) -> str:
            var = m.group(1)
            if var not in restrict_vars:
                logger.debug(
                    "cross_object_prop: skipping %s.%s (var not in restrict_vars)",
                    var,
                    prop,
                )
                return m.group(0)
            logger.debug("cross_object_prop: adding await to %s.%s", var, prop)
            # Always use parentheses: handles chained access
            # (var.prop.something → (await var.prop).something) and operator
            # precedence (`await x.name if cond else y` → `(await x.name) if cond else y`)
            return f"(await {var}.{prop})"

        def transform(line: str) -> str:
            return re.sub(pattern, _replace_cross, line)

        return cls._transform_async_def_lines(src, transform, track_docstrings=True)

    @classmethod
    def _safe_add_await_cross_object_method(cls, src: str, method: str, restrict_vars: set[str]) -> str:
        """
        Add 'await' before VARNAME.METHOD( calls where METHOD is an async method and VARNAME is NOT 'self'.

        Only adds await inside `async def` functions.
        Only matches lowercase variable names (to avoid module.method false positives).

        Args:
            method: The method name to match.
            restrict_vars: Only match these specific variable names (determined by
                           type-registry analysis).

        """
        # Pattern: var.method( where var is NOT self
        # NOT preceded by 'await ' or 'self.' or '.' (not part of chain) or word char
        pattern = rf"(?<!await )(?<!self\.)" rf"(?<!\w)(?<!\.)" rf"(?!self\.)" rf"([a-z_]\w*)\.{re.escape(method)}\s*\("

        def _replace_cross_method(m: re.Match) -> str:
            var = m.group(1)
            if var not in restrict_vars:
                logger.debug(
                    "cross_object_method: skipping %s.%s() (var not in restrict_vars)",
                    var,
                    method,
                )
                return m.group(0)
            logger.debug("cross_object_method: adding await to %s.%s()", var, method)
            return f"await {var}.{method}("

        def transform(line: str) -> str:
            return re.sub(pattern, _replace_cross_method, line)

        return cls._transform_async_def_lines(src, transform)

    # Pre-compiled regex for checking if 'await' already precedes a match
    _AWAIT_LOOKBACK_RE = re.compile(r"await\s+$")

    @classmethod
    def _safe_add_await(cls, src: str, pattern: str) -> str:
        """
        Add 'await' before pattern matches, avoiding double-insertion.

        Uses a negative lookbehind approach: scans backwards from the match
        to check if 'await' already precedes it (with optional whitespace).

        """
        result_parts = []
        last_end = 0

        for m in _compile(pattern).finditer(src):
            start = m.start()
            # Check if 'await ' already precedes this match
            # Look back further (up to 20 chars) to handle indentation
            lookback = src[max(0, start - 20) : start]
            if cls._AWAIT_LOOKBACK_RE.search(lookback):
                continue  # Already has await
            # Insert 'await ' before the match
            result_parts.append(src[last_end:start])
            result_parts.append("await ")
            result_parts.append(m.group(0))
            last_end = m.end()

        if not result_parts:
            return src

        result_parts.append(src[last_end:])
        return "".join(result_parts)

    @staticmethod
    def _convert_context_managers(src: str) -> str:
        """
        Convert __enter__/__exit__ to __aenter__/__aexit__.
        """
        had_enter = "def __enter__(" in src
        had_exit = "def __exit__(" in src
        src = re.sub(r"def __enter__\(", "async def __aenter__(", src)
        src = re.sub(r"def __exit__\(", "async def __aexit__(", src)
        # Also convert usages: __enter__() -> __aenter__(), __exit__() -> __aexit__()
        src = src.replace(".__enter__(", ".__aenter__(")
        src = src.replace(".__exit__(", ".__aexit__(")
        if had_enter or had_exit:
            logger.debug("convert_context_managers: converted __enter__/%s __exit__/%s", had_enter, had_exit)
        return src

    @staticmethod
    def _convert_with_to_async_with(src: str) -> str:
        """
        Convert `with self.<lock>:` to `async with self.<lock>:` for LOCK_ATTRS (asyncio.Lock needs async with).
        """
        lock_alt = "|".join(rf"self\.{re.escape(a)}" for a in LOCK_ATTRS)
        src = re.sub(
            rf"^(\s+)with ({lock_alt})(.*:)\s*$",
            r"\1async with \2\3",
            src,
            flags=re.MULTILINE,
        )
        return src

    @staticmethod
    def _add_close_awaits(src: str, stem: str) -> str:
        """
        Add await to close() calls on connection/session objects.
        """
        if stem == "Requester":
            # self.__connection.close() -> await self.__connection.close()
            src = re.sub(
                r"(?<!await )self\.__connection\.close\(\)",
                "await self.__connection.close()",
                src,
            )
            # .close() on connections popped from deque
            src = re.sub(
                r"(?<!await )(self\.__custom_connections\.popleft\(\))\.close\(\)",
                r"await \1.close()",
                src,
            )
            # self.session.close() - for niquests.AsyncSession
            src = re.sub(
                r"(?<!await )self\.session\.close\(\)",
                "await self.session.close()",
                src,
            )
        if stem == "Requester" or stem in CONNECTION_CLASSES:
            # self.session.close() - for connection classes
            src = re.sub(
                r"(?<!await )self\.session\.close\(\)",
                "await self.session.close()",
                src,
            )
        return src

    @classmethod
    def _fix_yield_from_in_async_defs(cls, src: str) -> str:
        """
        Rewrite ``yield from EXPR`` inside async def bodies into an explicit element loop.

        ``yield from`` is a SyntaxError inside async generators, so any occurrence in a method that became async must
        be rewritten.

        """
        yield_from_re = re.compile(r"^(\s+)yield from (.+?)\s*$")

        def transform(line: str) -> str:
            m = yield_from_re.match(line)
            if not m:
                return line
            indent, expr = m.group(1), m.group(2)
            logger.debug("fix_yield_from: rewriting 'yield from %s'", expr)
            return f"{indent}for element in {expr}:\n{indent}    yield element"

        return cls._transform_async_def_lines(src, transform)

    def _fix_issubclass_dual_class(self, src: str) -> str:
        """
        Rewrite ``issubclass(x, C)`` where C is a bare async class name to also accept the sync class.

        Sync classes (github.X.Y) may be passed to async code (e.g. create_from_raw_data); an issubclass check against
        the async class alone would reject them. Adds ``import github.{mod}`` for each rewritten class.

        """
        needed_imports: set[str] = set()

        def _dual(m: re.Match) -> str:
            var, cls_name = m.group(1), m.group(2)
            mod = self.analyzer.class_to_file.get(cls_name)
            if mod is None or cls_name not in self.analyzer.async_classes:
                return m.group(0)
            needed_imports.add(mod)
            logger.debug("fix_issubclass_dual_class: %s → dual sync/async check", m.group(0))
            return f"issubclass({var}, {cls_name}) or issubclass({var}, {_sync_dotted_ref(mod, cls_name)})"

        src = re.sub(r"issubclass\((\w+),\s*(\w+)\)(?!\s+or\s+issubclass)", _dual, src)

        # Ensure the sync modules are importable
        for mod in sorted(needed_imports):
            if f"import github.{mod}" not in src:
                src = self._prepend_import(src, f"import github.{mod}\n")
        return src

    def _fix_isinstance_dual_class(self, src: str) -> str:
        """
        Fix isinstance checks to accept both async and sync class variants.

        After import rewriting, async code uses relative imports so classes
        appear as ``X.Y`` (e.g. ``Repository.Repository``).  Tests may pass
        sync objects (``github.X.Y`` instances).  Fix by also accepting
        ``github.X.Y`` alongside the async class.

        Transforms:
            isinstance(x, X.Y)  → isinstance(x, (X.Y, github.X.Y))

        Only applies when ``X`` is a known async module name.

        """
        logger.debug("fix_isinstance_dual_class: begin")
        # Build set of async module names
        async_files = set()
        for cls_name in self.analyzer.async_classes:
            f = self.analyzer.class_to_file.get(cls_name)
            if f:
                async_files.add(f)
        for p in SRC_PKG.glob("*.py"):
            s = p.stem
            if s not in SKIP_STEMS and not s.startswith("_"):
                async_files.add(s)

        # Build a pattern that matches the aliased async runtime reference
        # `_async_ModuleName.ClassName` for known async modules (e.g.
        # `_async_Repository.Repository`, `_async_NamedUser.NamedUser`). This is the form
        # `_fix_imports` produces for runtime references, so a match here always means
        # "async-only, needs the sync variant added" — no separate already-qualified check
        # is needed the way the old bare `ModuleName.ClassName` pattern required.
        mod_pattern = "|".join(re.escape(m) for m in sorted(async_files, key=len, reverse=True))
        async_class_pat = re.compile(rf"\b_async_({mod_pattern})\.(\w+)")

        result: list[str] = []
        i = 0
        isinstance_literal = "isinstance("

        while i < len(src):
            pos = src.find(isinstance_literal, i)
            if pos == -1:
                result.append(src[i:])
                break

            result.append(src[i:pos])

            # Determine context: is this isinstance used for type validation (assert)
            # or for type dispatch (if/elif/ternary)?
            # Only add sync variants for assert isinstance checks.
            # For type dispatch, the isinstance-narrowed variable may be used with
            # `await` which doesn't work on Union[Coroutine, str] types.
            line_start_pos = src.rfind("\n", 0, pos) + 1
            prefix_on_line = src[line_start_pos:pos].lstrip()
            is_assert_context = prefix_on_line.startswith("assert ")
            # Also check for `all(isinstance(...)` and similar assertion patterns
            is_assert_context = is_assert_context or prefix_on_line.startswith("assert all(")
            # Check for `... for ... in ...` loop context where isinstance is in an assertion
            # e.g. `assert all(isinstance(element, ...) for element in parents)`
            if not is_assert_context:
                # Look further back for assert ... comprehension patterns
                further_back = src[max(0, pos - 200) : pos]
                if re.search(r"assert\s+all\s*\(", further_back):
                    is_assert_context = True

            # Find matching closing paren
            paren_start = pos + len(isinstance_literal) - 1
            j = self._find_paren_end(src, paren_start)
            if j == -1:
                j = len(src)  # unbalanced — treat the rest of the source as the call

            full_call = src[pos:j]
            inner = src[paren_start + 1 : j - 1]

            if not async_class_pat.search(inner):
                result.append(full_call)
                i = j
                continue

            # Find first depth-0 comma separating object from type
            comma_depth = 0
            comma_pos = None
            for k, ch in enumerate(inner):
                if ch == "(":
                    comma_depth += 1
                elif ch == ")":
                    comma_depth -= 1
                elif ch == "," and comma_depth == 0:
                    comma_pos = k
                    break

            if comma_pos is None:
                result.append(full_call)
                i = j
                continue

            first_arg = inner[:comma_pos]
            type_arg = inner[comma_pos + 1 :].strip()
            type_arg_stripped = type_arg.rstrip().rstrip(",").rstrip()

            # A match always means "async-only, needs the sync variant added": the pattern
            # requires the `githubasyncio.` prefix, which never appears in the sync half
            # of an already-dual-wrapped check.
            if not async_class_pat.search(type_arg_stripped):
                result.append(full_call)
                i = j
                continue

            # Only add sync class variants for assert isinstance (type validation).
            # For if/elif/ternary isinstance (type dispatch), the isinstance-narrowed
            # variable may be accessed with `await` which doesn't work on Union types
            # when the sync variant returns a plain value instead of a coroutine.
            if not is_assert_context:
                result.append(full_call)
                i = j
                continue

            is_tuple = type_arg_stripped.startswith("(")

            if is_tuple:

                def _add_sync_in_tuple(m: re.Match) -> str:
                    return f"{m.group(0)}, {_sync_dotted_ref(m.group(1), m.group(2))}"

                new_type_arg = async_class_pat.sub(_add_sync_in_tuple, type_arg)
                logger.debug("fix_isinstance_dual_class: tuple — %s → %s", type_arg.strip(), new_type_arg.strip())
                result.append(f"isinstance({first_arg}, {new_type_arg})")
            else:
                if async_class_pat.fullmatch(type_arg_stripped):
                    m = async_class_pat.fullmatch(type_arg_stripped)
                    mod, cls = m.group(1), m.group(2)
                    logger.debug(
                        "fix_isinstance_dual_class: single — %s → (%s, github.%s.%s)",
                        m.group(0),
                        m.group(0),
                        mod,
                        cls,
                    )
                    result.append(f"isinstance({first_arg}, ({m.group(0)}, {_sync_dotted_ref(mod, cls)}))")
                else:

                    def _wrap_async_class(m2: re.Match) -> str:
                        return f"({m2.group(0)}, {_sync_dotted_ref(m2.group(1), m2.group(2))})"

                    new_type_arg = async_class_pat.sub(_wrap_async_class, type_arg)
                    result.append(f"isinstance({first_arg}, {new_type_arg})")

            i = j

        return "".join(result)


def _generate_reexport_stub(module_name: str) -> str:
    """
    Generate a stub module that re-exports everything from the sync counterpart.

    This ensures that e.g. ``githubasyncio.Auth.Auth``
    IS ``github.Auth.Auth`` (same object), avoiding isinstance mismatches.

    """
    return (
        f"{AUTO_HEADER}"
        f"# Re-export everything from the sync module so that\n"
        f"# isinstance checks work with both sync and async code.\n"
        f"from github.{module_name} import *  # noqa: F401,F403\n"
    )


def generate_async_requestlib() -> str:
    """
    Generate githubasyncio/requestlib.py: the async project's HTTP-backend shim.

    Mirrors the niquests branch of the classic project's github/requestlib/__init__.py, but
    unconditionally -- the async project mandates niquests (see async/pyproject.toml), so there's
    no requests-vs-niquests choice to make here, and no need to reach into the classic package's
    own requestlib for it.

    """
    return (
        f"{AUTO_HEADER}"
        '"""\n'
        "HTTP backend shim, always niquests: unlike the classic project's github.requestlib,\n"
        "there's no requests-vs-niquests choice here (see the niquests dependency in pyproject.toml).\n"
        '"""\n'
        "\n"
        "from niquests import Response, adapters, exceptions, utils\n"
        "from niquests import RetryConfiguration as Retry\n"
        "from niquests.models import CaseInsensitiveDict, PreparedRequest\n"
        "from niquests.packages import urllib3\n"
        "from niquests.packages.urllib3.util import Url\n"
        "\n"
        "netrc_auth_utils = utils.get_netrc_auth\n"
        "\n"
        'active = "niquests"\n'
        "\n"
        "__all__ = [\n"
        '    "active",\n'
        '    "adapters",\n'
        '    "exceptions",\n'
        '    "utils",\n'
        '    "Response",\n'
        '    "PreparedRequest",\n'
        '    "CaseInsensitiveDict",\n'
        '    "Retry",\n'
        '    "Url",\n'
        '    "urllib3",\n'
        '    "netrc_auth_utils",\n'
        "]\n"
    )


def generate_async_init() -> str:
    """
    Generate the __init__.py for githubasyncio.
    """
    lines = [AUTO_HEADER.rstrip()]
    lines.append('"""')
    lines.append("Async counterparts of the github package classes.")
    lines.append('"""')
    lines.append("")
    lines.append("")
    exported: list[str] = []
    for mod, names in sorted(ASYNC_INIT_EXPORTS.items()):
        for name in names:
            lines.append(f"from githubasyncio.{mod} import {name}")
            exported.append(name)
    lines.append("")
    lines.append("")
    lines.append("__all__ = [")
    for name in sorted(exported):
        lines.append(f'    "{name}",')
    lines.append("]")
    lines.append("")
    return "\n".join(lines)


def _in_string_literal(line: str, pos: int) -> bool:
    """
    Whether `pos` in a single source line falls inside a single-line string literal (quote parity up to `pos`,
    honouring backslash escapes and the other quote kind).
    """
    quote = None
    i = 0
    while i < pos:
        c = line[i]
        if quote and c == "\\":
            i += 2
            continue
        if c in "\"'" and quote in (None, c):
            quote = None if quote else c
        elif c == "#" and quote is None:
            return False
        i += 1
    return quote is not None


def _method_ranges_matching(src: str, patterns: tuple[str, ...]) -> list[tuple[int, int]]:
    """
    Line-index ranges [start, end) of every method (``    def name(...`` at one level of indentation) whose body
    matches any of `patterns`.

    Used to scope a rewrite to everything *except* particular test methods, by having the caller skip lines falling
    inside a returned range.

    """
    lines = src.split("\n")
    starts = [i for i, line in enumerate(lines) if re.match(r"^    def \w+\(", line)]
    if not starts:
        return []
    starts.append(len(lines))  # sentinel: end of the last method
    combined = _compile("|".join(patterns))
    ranges = []
    for start, end in zip(starts, starts[1:]):
        if combined.search("\n".join(lines[start:end])):
            ranges.append((start, end))
    return ranges


def _ensure_bare_githubasyncio_import(src: str) -> str:
    """
    Ensure a bare ``import githubasyncio`` line exists, inserted right after the last top-level ``import github`` /
    ``import github.X`` line.

    Several transform_test_file passes rewrite `github.X` text to `githubasyncio.X` and need the
    bare name bound as a result. A plain `src.replace("import github\n", ...)` -- this function's
    predecessor -- silently no-ops in any file whose only classic import is dotted (`import
    github.Foo`, no bare `import github` line), which is common once such a file's *other* dotted
    imports (`import github.Foo`) get fully redirected/removed by earlier passes or ruff's
    unused-import cleanup: exactly the files this function's callers run on.

    """
    if re.search(r"^import githubasyncio\s*$", src, re.MULTILINE):
        return src
    last_github_import = None
    for m in re.finditer(r"^import github(?:\.\w+)?\s*$", src, re.MULTILINE):
        last_github_import = m
    if last_github_import is None:
        return src
    insert_at = last_github_import.end()
    return src[:insert_at] + "\nimport githubasyncio" + src[insert_at:]


def transform_test_file(src: str, test_stem: str, analyzer: IOAnalyzer) -> str:
    """
    Transform a sync test file into an async version.

    Since we use SyncProxy to bridge async-to-sync, test method bodies remain identical. We only need to change
    imports/base class.

    """
    logger.debug("transform_test[%s]: begin", test_stem)
    result = AUTO_HEADER + src

    # Change Framework import to use the self-contained async Framework (tests/AsyncFramework.py
    # — see TEMPLATE_TEST_FILES), aliased back to the bare name `Framework` so the rest of the
    # test body (`Framework.TestCase`, etc.) is unchanged. Sync sources use either import form
    # depending on whether the test file sits directly in tests/ or not; both collapse onto the
    # same target here since tests/ is flat.
    result = result.replace("from . import Framework", "from tests import AsyncFramework as Framework")
    result = result.replace("from tests import Framework", "from tests import AsyncFramework as Framework")
    logger.debug("transform_test[%s]: changed Framework import to async", test_stem)

    # Entry-point classes (those that construct their own Requester, e.g. Github,
    # GithubIntegration) must come from the async package so that tests exercise
    # the async stack.  Derived from the analyzer, not hardcoded.
    _entry_point_pairs = analyzer.entry_point_classes()
    for mod, cls_name in _entry_point_pairs:
        result = result.replace(
            f"from github.{mod} import {cls_name}",
            f"from githubasyncio.{mod} import {cls_name}",
        )

    # A number of tests construct their own entry-point client inline instead of using self.g
    # (e.g. to exercise an auth-failure path, or a non-default base_url), via the package-level
    # `github.Github(...)` / `github.GithubIntegration(...)` form specifically (the `from
    # github.X import Y` form above already binds the bare name to the *async* class -- but then
    # it's unwrapped, so calling e.g. .get_user() on it would just hand back a coroutine). Route
    # the construction through Framework.make_async() so it's SyncProxy-wrapped like self.g,
    # *except* in methods matching ENTRY_POINT_CTOR_SKIP_MARKERS: a test that hands a plain
    # mock.MagicMock() to a connection slot and expects close() to be called on it synchronously
    # will fail differently (not incorrectly, just differently -- close() is
    # `await self.__connection.close()` on the async side, which can't await a MagicMock) if that
    # connection now belongs to a real async Requester. Such methods are left untouched (the
    # bare-connection-double and requester-spec-mock passes below convert the ones that can be);
    # a method that still ends up constructing a classic class fails loudly (no `github` import).
    # (pickle round-trips are not skipped: `pickle.dumps(X)` arguments get unwrapped from their
    # SyncProxy instead -- see the pickle pass below -- and the raw async objects pickle fine.)
    _protected_ranges = _method_ranges_matching(result, ENTRY_POINT_CTOR_SKIP_MARKERS)

    # Bare connection doubles: a method that assigns a plain `mock.MagicMock()` to a Requester's
    # connection slot (`_Requester__connection`, `__custom_connections`) only to check that
    # close() reaches it. That marker guard exists because the async close() is
    # `await connection.close()`, which a MagicMock's plain return value can't satisfy -- but
    # `mock.AsyncMock()` does, and records `close.assert_called_once_with()` the same way. Swapping
    # it in lets these methods run against the async stack like everything else, so they leave the
    # protected set. Only for methods whose *sole* mock use is that bare, argument-less form (a
    # spec'd or argument-carrying mock means something else, handled -- or not -- elsewhere).
    _bare_magic_re = re.compile(r"\bmock\.MagicMock\(\)")
    _arg_mock_re = re.compile(r"\bmock\.(?:Mock|MagicMock)\((?!\))")
    _connection_double_ranges = [
        (start, end)
        for start, end in _protected_ranges
        if "_Requester__connection" in "\n".join(result.split("\n")[start:end])
        and _bare_magic_re.search("\n".join(result.split("\n")[start:end]))
        and not _arg_mock_re.search("\n".join(result.split("\n")[start:end]))
    ]
    if _connection_double_ranges:
        _cd_lines = result.split("\n")
        for start, end in _connection_double_ranges:
            for _i in range(start, end):
                _cd_lines[_i] = _bare_magic_re.sub("mock.AsyncMock()", _cd_lines[_i])
        result = "\n".join(_cd_lines)
        _protected_ranges = [r for r in _protected_ranges if r not in _connection_double_ranges]

    if _entry_point_pairs:
        _lines = result.split("\n")
        _ctor_rewritten = False
        for _i, _line in enumerate(_lines):
            if any(start <= _i < end for start, end in _protected_ranges):
                continue
            for mod, cls_name in _entry_point_pairs:
                # inside a string literal (e.g. an expected deprecation message), this is prose naming
                # the class, not a construction: give it the plain async path the package's own message uses
                _line, _n = re.subn(
                    rf"(?<!\w)github\.{re.escape(cls_name)}\(",
                    lambda m, mod=mod, cls_name=cls_name, line=_line: (
                        f"githubasyncio.{mod}.{cls_name}("
                        if _in_string_literal(line, m.start())
                        else f"Framework.make_async(githubasyncio.{mod}.{cls_name}, "
                    ),
                    _line,
                )
                _line = _line.replace(f"githubasyncio.{mod}.{cls_name}, )", f"githubasyncio.{mod}.{cls_name})")
                _ctor_rewritten = _ctor_rewritten or _n > 0
                # reference-only use of the bare package-level name (e.g. an assertIsInstance target)
                _line, _n = re.subn(
                    rf"(?<![\w.])github\.{re.escape(cls_name)}\b(?!\()",
                    f"githubasyncio.{mod}.{cls_name}",
                    _line,
                )
                _ctor_rewritten = _ctor_rewritten or _n > 0
            _lines[_i] = _line
        result = "\n".join(_lines)
        if _ctor_rewritten:
            result = _ensure_bare_githubasyncio_import(result)

    # An entry-point class imported by bare name (`from github import Github`, then `Github(...)`)
    # is constructed without the `github.` prefix the loop above matches. Same wrapping applies:
    # rewrite the bare construction outside protected ranges and drop the name from the classic
    # import (the qualified `githubasyncio.<mod>.<cls>` form needs no import of its own beyond the
    # submodule sweep further down).
    for _mod, _cls_name in _entry_point_pairs:
        if not re.search(rf"^\s*from github import\b[^\n]*\b{re.escape(_cls_name)}\b", result, re.MULTILINE):
            continue
        _protected_body = "\n".join("\n".join(result.split("\n")[start:end]) for start, end in _protected_ranges)
        if re.search(rf"(?<![\w.]){re.escape(_cls_name)}\(", _protected_body):
            continue  # a protected method still constructs it the classic way: keep the import
        _bare_lines = result.split("\n")
        for _i, _line in enumerate(_bare_lines):
            if _line.lstrip().startswith(("from ", "import ")):
                m = re.match(r"^(\s*)from github import (.+)$", _line)
                if m and "(" not in m.group(2):
                    names = [n for n in AsyncTransformer._split_import_names(m.group(2)) if n != _cls_name]
                    _bare_lines[_i] = f"{m.group(1)}from github import {', '.join(names)}" if names else "\0"
                continue
            _bare_lines[_i] = re.sub(
                rf"(?<![\w.]){re.escape(_cls_name)}\(",
                f"Framework.make_async(githubasyncio.{_mod}.{_cls_name}, ",
                _line,
            ).replace(f"githubasyncio.{_mod}.{_cls_name}, )", f"githubasyncio.{_mod}.{_cls_name})")
        result = "\n".join(line for line in _bare_lines if line != "\0")
        result = _ensure_bare_githubasyncio_import(result)

    # A handful of tests build a `mock.Mock(github.Requester.Requester, ...)` /
    # `mock.MagicMock(github.Requester.Requester, ...)` purely as a spec for a Requester double
    # (not a bare connection-object mock), then construct an I/O-bearing class directly with it
    # (e.g. `github.Repository.Repository(requester, url=...)`) to test attribute-parsing from a
    # url/attributes dict, bypassing self.g entirely. This trips ENTRY_POINT_CTOR_SKIP_MARKERS'
    # `mock.Mock(`/`mock.MagicMock(` markers above, but a *spec'd* mock is safe to redirect to the
    # async class where a bare connection double isn't: unittest.mock auto-detects async methods
    # on the spec class and wraps the corresponding attribute as an AsyncMock, so an async
    # Requester spec just works as-is. The constructed class still needs Framework.make_async()
    # wrapping (same as the entry-point rewrite above), since its properties are `async def` and
    # would otherwise hand back raw, unawaited coroutines instead of values. Scoped narrowly to
    # methods where the Requester-spec mock is the *sole* mock.Mock/MagicMock usage (no bare
    # connection double) — those keep the classic (unrewritten) construction above.
    _requester_spec_mock_re = re.compile(r"\bmock\.(?:Mock|MagicMock)\(github\.Requester\.Requester\b")
    _other_mock_re = re.compile(r"\bmock\.(?:Mock|MagicMock)\((?!github\.Requester\.Requester\b)")
    _rs_all_lines = result.split("\n")
    _rs_method_starts = [i for i, line in enumerate(_rs_all_lines) if re.match(r"^    def \w+\(", line)]
    _requester_spec_ranges: list[tuple[int, int]] = []
    if _rs_method_starts:
        _rs_bounds = _rs_method_starts + [len(_rs_all_lines)]
        for start, end in zip(_rs_bounds, _rs_bounds[1:]):
            body = "\n".join(_rs_all_lines[start:end])
            if _requester_spec_mock_re.search(body) and not _other_mock_re.search(body):
                _requester_spec_ranges.append((start, end))

    if _requester_spec_ranges:
        _entry_point_cls_names = {cls_name for _, cls_name in _entry_point_pairs}
        _makeasync_candidates = {
            cls_name: mod_name
            for cls_name, mod_name in analyzer.class_to_file.items()
            if cls_name in analyzer.async_classes
            and mod_name not in PURE_DATA_MODULES
            and cls_name != "Requester"
            and cls_name not in _entry_point_cls_names
        }
        _rs_mods_needed: set[str] = {"Requester"}
        for _i, _line in enumerate(_rs_all_lines):
            if not any(start <= _i < end for start, end in _requester_spec_ranges):
                continue
            new_line = _line.replace(
                "mock.Mock(github.Requester.Requester", "mock.Mock(githubasyncio.Requester.Requester"
            ).replace("mock.MagicMock(github.Requester.Requester", "mock.MagicMock(githubasyncio.Requester.Requester")
            for cls_name, mod_name in sorted(_makeasync_candidates.items(), key=lambda kv: len(kv[0]), reverse=True):
                new_line, _n = re.subn(
                    rf"(?<!\w)github\.{re.escape(mod_name)}\.{re.escape(cls_name)}\(",
                    f"Framework.make_async(githubasyncio.{mod_name}.{cls_name}, ",
                    new_line,
                )
                if _n:
                    _rs_mods_needed.add(mod_name)
            _rs_all_lines[_i] = new_line
        result = "\n".join(_rs_all_lines)

        # Ensure every githubasyncio.<mod> touched above is importable (unlike bare `githubasyncio`,
        # used throughout every test file already, submodules need their own explicit import).
        _missing_mods = [
            mod
            for mod in sorted(_rs_mods_needed)
            if not re.search(rf"^import githubasyncio\.{re.escape(mod)}\s*$", result, re.MULTILINE)
        ]
        if _missing_mods:
            _last_github_import = None
            for _gm in re.finditer(r"^import github(?:\.\w+)?\s*$", result, re.MULTILINE):
                _last_github_import = _gm
            if _last_github_import:
                _insert_pos = _last_github_import.end()
                _import_block = "\n" + "\n".join(f"import githubasyncio.{mod}" for mod in _missing_mods)
                result = result[:_insert_pos] + _import_block + result[_insert_pos:]
        logger.debug(
            "transform_test[%s]: redirected %d requester-spec-mock method(s) to async",
            test_stem,
            len(_requester_spec_ranges),
        )

    # Package-level class references (`github.ClassName`, e.g. `github.InputFileContent(...)`,
    # `self.assertRaises(github.BadCredentialsException)`) into PURE_DATA_MODULES must use the
    # async twin instead: githubasyncio now has its own genuine (non-identical) copy of every
    # class github/__init__.py re-exports from one of those modules, whether same-named as its
    # module (SHADOWED_MODULE_NAMES: GithubException, GithubRetry, InputFileContent,
    # InputGitAuthor, InputGitTreeElement) or not (e.g. BadCredentialsException, from
    # GithubException.py — see _init_reexports_map()). A sync-constructed InputFileContent isn't a
    # githubasyncio.InputFileContent.InputFileContent, and the async Requester never raises a sync
    # exception. Scoped to PURE_DATA_MODULES specifically (not every re-export) because unlike
    # those, e.g. Github (MainClass) has async methods: constructing
    # `githubasyncio.MainClass.Github(...)` directly, instead of through the framework's
    # SyncProxy-wrapped self.g, would return raw, unbridged coroutines from every method call.
    # `githubasyncio` is already fully imported by every generated test file's own top-level
    # import by the time any test method runs, so this fully-qualified form needs no import of
    # its own.
    _test_reexports = {
        cls_name: mod_name for cls_name, mod_name in _init_reexports_map().items() if mod_name in PURE_DATA_MODULES
    }
    for _mod in SHADOWED_MODULE_NAMES:
        _test_reexports.setdefault(_mod, _mod)
    # Auth classes (Login, Token, AppAuth, ...): constructed directly in test bodies via
    # `from github.Auth import X` / `github.Auth.X(...)` and then handed as `auth=` to an
    # entry-point class -- since entry-point construction above now builds the *async* class,
    # the auth object needs to match (an async entry point rejects a sync-flavored auth instance
    # with a type/isinstance error; see the Auth branch below for the `github.Auth.X` form these
    # don't cover on their own). Unlike MainClass/GithubIntegration, Auth classes don't need
    # SyncProxy wrapping here even though a couple of them (AppAuth and friends) do have real
    # async methods -- tests only construct and hand them off, they don't call those methods
    # directly on the object built here.
    for _cls_name, _mod_name in analyzer.class_to_file.items():
        if _mod_name == "Auth":
            _test_reexports.setdefault(_cls_name, "Auth")
    # Any other class with no I/O of its own (not in analyzer.async_classes) -- e.g. CustomProperty,
    # a plain parameter container living in an otherwise I/O-bearing module
    # (OrganizationCustomProperty.py), reached via `from github.OrganizationCustomProperty import
    # CustomProperty` rather than a package-level re-export. Same reasoning as PURE_DATA_MODULES
    # above: there's no behavioral difference between the sync and async twin to preserve, so this
    # is safe regardless of which entry point (if any) a given test method otherwise stays classic
    # for. Only feeds the reimport machinery below (`from github.X import Y` -> `from
    # githubasyncio.X import Y`); the module-qualified in-body form (`github.X.Y(...)`) for classes
    # not reached via such an import is handled by the general pass further below instead.
    for _cls_name, _mod_name in analyzer.class_to_file.items():
        if _cls_name not in analyzer.async_classes:
            _test_reexports.setdefault(_cls_name, _mod_name)
    _shadowed_rewritten = False
    _shadowed_lines = result.split("\n")
    for _i, _line in enumerate(_shadowed_lines):
        stripped = _line.lstrip()
        if stripped.startswith("import ") or stripped.startswith("from "):
            continue  # leave import statements alone -- only rewrite expression usages
        new_line = _line
        for cls_name, mod_name in sorted(_test_reexports.items(), key=lambda kv: len(kv[0]), reverse=True):
            new_line, _n = re.subn(
                rf"\bgithub\.{re.escape(cls_name)}\b(?!\.)", f"githubasyncio.{mod_name}.{cls_name}", new_line
            )
            _shadowed_rewritten = _shadowed_rewritten or _n > 0
        _shadowed_lines[_i] = new_line
    result = "\n".join(_shadowed_lines)
    if _shadowed_rewritten:
        result = _ensure_bare_githubasyncio_import(result)

    # `Framework.github.X`: the classic sync Framework imports `github` at module level, so
    # test bodies copied from the classic suite reach modules through it (e.g.
    # `Framework.github.GithubObject`,
    # `Framework.github.NamedUser`) -- AsyncFramework.py is self-contained and has no `.github`
    # attribute at all, only `.githubasyncio` (it imports `githubasyncio.X` submodules directly).
    # The PURE_DATA_MODULES rewrite above already turned any *class* reference reached this way
    # (e.g. `Framework.github.BadAttributeException`) into its fully-qualified
    # `Framework.githubasyncio.<mod>.<cls>` form; only plain module references are left, and those
    # just need github -> githubasyncio.
    result = result.replace("Framework.github.", "Framework.githubasyncio.")

    # `github.Auth.X(...)` / `github.Requester.Requester(...)`: module-qualified (unlike the bare
    # `github.ClassName` shadow rewrite above), since neither is re-exported at the package level
    # -- only the modules themselves are (`from . import Auth` in github/__init__.py; Requester
    # isn't even re-exported there, but a test can still reach it via `import github.Requester`).
    # Like Auth, constructing a Requester directly doesn't need SyncProxy wrapping (__init__ and
    # the handful of methods tests call directly on one here -- .kwargs, .withAuth() -- are all
    # sync on both sides). Only the dot-continued form; import lines (`from github.Auth import
    # X`) don't match (no trailing dot after "Auth") and are handled below by the _test_reexports
    # machinery instead. Respects the same ENTRY_POINT_CTOR_SKIP_MARKERS protected ranges as the
    # entry-point rewrite above: a method left constructing e.g. `github.GithubIntegration(...)`
    # (because it mocks a connection) needs the `auth=` it's given to stay classic too, or the
    # two won't match types.
    _auth_rewritten = False
    _auth_lines = result.split("\n")
    for _i, _line in enumerate(_auth_lines):
        if any(start <= _i < end for start, end in _protected_ranges):
            continue
        new_line = _line.replace("github.Auth.", "githubasyncio.Auth.").replace(
            "github.Requester.Requester(", "githubasyncio.Requester.Requester("
        )
        # Auth classes whose `token` does I/O (installation / user tokens) have an async `token`
        # property, so a test that reads it directly needs the SyncProxy wrapping; make_async()
        # unwraps it again when it's handed to an entry point.
        new_line = re.sub(
            r"\bgithubasyncio\.Auth\.(AppInstallationAuth|AppUserAuth)\((?!\.\.\.)",
            r"Framework.make_async(githubasyncio.Auth.\1, ",
            new_line,
        )
        # static / attribute references (isRateLimitError, get_graphql_prefix, __init__ annotations,
        # ...) -- but not injectLogger/resetLogger, which TEST_LOGGER_CALLS handles explicitly
        new_line = re.sub(
            r"\bgithub\.Requester\.Requester\.(?!injectLogger|resetLogger)",
            "githubasyncio.Requester.Requester.",
            new_line,
        )
        _auth_rewritten = _auth_rewritten or new_line != _line
        _auth_lines[_i] = new_line
    result = "\n".join(_auth_lines)
    if _auth_rewritten:
        result = _ensure_bare_githubasyncio_import(result)

    # `if TYPE_CHECKING:` imports carry no runtime behavior at all (never executed -- the whole
    # point of the guard), so a classic reference there is always safe to redirect regardless of
    # everything the rest of this function is careful about (protected ranges, async_classes
    # membership, ...): there's no "the compared/constructed object is classic in this method" to
    # stay consistent with, because nothing is compared or constructed here, ever. Handles e.g.
    # `if TYPE_CHECKING:\n    from github.Repository import Repository` even though Repository is
    # a full I/O class the general pass elsewhere deliberately leaves alone at runtime.
    _tc_lines = result.split("\n")
    _in_type_checking = False
    _tc_indent = 0
    for _i, _line in enumerate(_tc_lines):
        stripped = _line.strip()
        if stripped == "if TYPE_CHECKING:":
            _in_type_checking = True
            _tc_indent = len(_line) - len(_line.lstrip())
            continue
        if _in_type_checking:
            if stripped and (len(_line) - len(_line.lstrip())) <= _tc_indent:
                _in_type_checking = False
            else:
                _tc_lines[_i] = re.sub(r"\bgithub\b(?!asyncio)", "githubasyncio", _line)
    result = "\n".join(_tc_lines)

    # Bare `from github import Consts` (a pure-data module, not a class) isn't covered above: the
    # entry-point rewrite only matches the module-qualified `from github.<mod> import <cls>` form,
    # and Consts is a module, not a class, so no class-keyed mechanism reaches it either. Safe to
    # redirect unconditionally -- pure data, identical behavior either side. Deliberately excludes
    # entry-point classes (Github/GithubIntegration) even though they're also bare package-level
    # re-exports: a `from github import Github` + bare `Github(...)` construction (confirmed in
    # GraphQl.py) needs the same Framework.make_async() wrapping the module-qualified
    # `github.Github(...)` form gets above, which this pass doesn't apply -- redirecting just the
    # import here would leave the bare construction returning raw, unbridged coroutines.
    _bare_module_names = {"Consts"}
    _bare_found = [
        n
        for n in _bare_module_names
        if re.search(rf"^\s*from github import\b.*\b{re.escape(n)}\b", result, re.MULTILINE)
    ]
    if _bare_found:
        _bm_lines = []
        for _line in result.split("\n"):
            _m = re.match(r"^(\s*)from github import (.+)$", _line)
            if _m and "(" not in _m.group(2):
                _indent, _names_part = _m.group(1), _m.group(2)
                _names = AsyncTransformer._split_import_names(_names_part)
                _filtered = [n for n in _names if n not in _bare_found]
                if not _filtered:
                    continue
                if len(_filtered) != len(_names):
                    _line = f"{_indent}from github import {', '.join(_filtered)}"
            _bm_lines.append(_line)
        result = "\n".join(_bm_lines)
        _last_import_bm = None
        for _last_import_bm in re.finditer(r"^(?:from|import) .+$", result, re.MULTILINE):
            pass
        if _last_import_bm:
            _insert_at_bm = _last_import_bm.end()
            _new_bm_imports = "\n".join(f"from githubasyncio import {n}" for n in _bare_found)
            result = result[:_insert_at_bm] + "\n" + _new_bm_imports + result[_insert_at_bm:]
            logger.debug("transform_test[%s]: redirected bare module import(s): %s", test_stem, _bare_found)

    # these classes by name (`from github.X import Y` or `from github import Y`) and then uses
    # the bare name directly never gets touched, and still binds the sync class. Replace that
    # classic import with the async twin (dropping the name from its original `from github[.X]
    # import ...` line, and the whole line if it becomes empty) so no classic `github` import
    # survives in the generated test file, then re-import the async twin after the existing
    # import block so it wins the name binding.
    # I/O-bearing classes (in analyzer.async_classes) imported by bare name get the same treatment,
    # but only if no protected method uses the class: an import binds one name for the whole
    # file, so it can't stay classic for a protected method and become async for the rest. (A
    # bare-name class *construction* still needs the make_async wrapping decisions described
    # above -- this only redirects the import, so it's meant for reference-only uses such as
    # assertIsInstance targets and static utility calls.)
    _protected_text = "\n".join("\n".join(result.split("\n")[start:end]) for start, end in _protected_ranges)
    _reimport_candidates = dict(_test_reexports)
    for _cls_name, _mod_name in analyzer.class_to_file.items():
        if _mod_name in {"Auth", "Requester"} | {m for m, _ in _entry_point_pairs}:
            continue
        # skip a class any protected method still uses under its classic name
        if re.search(rf"\b{re.escape(_cls_name)}\b", _protected_text):
            continue
        _reimport_candidates.setdefault(_cls_name, _mod_name)

    # Single aliased imports (`from github.X import Cls as Alias`): repoint in place, keeping the
    # alias so every body reference stays valid. Same per-class protected-method gate as above.
    def _repoint_alias(m: re.Match) -> str:
        indent, mod, cls_name, alias = m.group(1), m.group(2), m.group(3), m.group(4)
        if _reimport_candidates.get(cls_name) != mod or re.search(rf"\b{re.escape(alias)}\b", _protected_text):
            return m.group(0)
        return f"{indent}from githubasyncio.{mod} import {cls_name} as {alias}"

    result = re.sub(r"^(\s*)from github\.(\w+) import (\w+) as (\w+)\s*$", _repoint_alias, result, flags=re.MULTILINE)
    _needed_reimport_names = [
        cls_name
        for cls_name, mod_name in _reimport_candidates.items()
        if re.search(
            rf"^\s*from github\.{re.escape(mod_name)} import\b.*\b{re.escape(cls_name)}\b", result, re.MULTILINE
        )
        or re.search(rf"^\s*from github import\b.*\b{re.escape(cls_name)}\b", result, re.MULTILINE)
    ]
    _needed_reimports = [
        f"from githubasyncio.{_reimport_candidates[cls_name]} import {cls_name}" for cls_name in _needed_reimport_names
    ]
    if _needed_reimports:
        _names_to_drop = set(_needed_reimport_names)
        _stripped_lines = []
        for _line in result.split("\n"):
            _m = re.match(r"^(\s*)from github(?:\.\w+)? import (.+)$", _line)
            if _m and "(" not in _m.group(2):
                _indent, _names_part = _m.group(1), _m.group(2)
                _names = AsyncTransformer._split_import_names(_names_part)
                _filtered = [n for n in _names if n not in _names_to_drop]
                if not _filtered:
                    continue  # drop the now-empty import line entirely
                if len(_filtered) != len(_names):
                    _prefix = _line[: _m.start(2)]
                    _line = f"{_prefix}{', '.join(_filtered)}"
            _stripped_lines.append(_line)
        result = "\n".join(_stripped_lines)

        _last_import_m = None
        for _last_import_m in re.finditer(r"^(?:from|import) .+$", result, re.MULTILINE):
            pass
        if _last_import_m:
            _insert_at = _last_import_m.end()
            result = result[:_insert_at] + "\n" + "\n".join(_needed_reimports) + result[_insert_at:]
            logger.debug("transform_test[%s]: re-imported async twins: %s", test_stem, _needed_reimports)

    # Note: test methods are NOT made async. SyncProxy handles the bridging.
    # No @pytest.mark.asyncio needed either.

    # Mock-target rewrites (TEST_MOCK_REWRITES): point patches at the async module
    # bindings, honoring per-test exclusions (e.g. Authentication tests the sync stack).
    for match, replacement, excluded_stems in TEST_MOCK_REWRITES:
        if test_stem in excluded_stems:
            continue
        if match in result:
            logger.debug("transform_test[%s]: mock rewrite %s", test_stem, match)
        result = result.replace(match, replacement)

    # Logger injection (TEST_LOGGER_CALLS): point it at the async Requester.
    for match, replacement in TEST_LOGGER_CALLS:
        if match in result:
            logger.debug("transform_test[%s]: logger call %s", test_stem, match)
        result = result.replace(match, replacement)

    # Ensure modules referenced by the injected async twin calls are importable
    if "githubasyncio.Requester.Requester." in result:
        if "import githubasyncio.Requester" not in result:
            result = result.replace(
                "import github\n",
                "import github\nimport githubasyncio.Requester\n",
                1,
            )

    # Helper import rewrites (TEST_HELPER_IMPORT_REWRITES): use the async variants
    # of module-level helpers that were patched for sync/async NotSet duality.
    for match, replacement in TEST_HELPER_IMPORT_REWRITES:
        result = result.replace(match, replacement)

    # Async @staticmethod/@classmethod (derived from the analyzer) called directly
    # in sync test bodies return coroutines.  Rewrite the reference to the async
    # class (the sync method's isinstance checks would reject SyncProxy-wrapped
    # async objects), then bridge the call through the event loop and unwrap
    # SyncProxy arguments to avoid nested event loop issues.
    for mod, cls_name, meth in analyzer.async_static_methods():
        sync_path = f"github.{mod}.{cls_name}.{meth}"
        if sync_path not in result:
            continue
        async_path = f"githubasyncio.{mod}.{cls_name}.{meth}"
        logger.debug("transform_test[%s]: bridging async static %s", test_stem, sync_path)
        result = result.replace(sync_path, async_path)

        # Unlike `github.X` (used throughout every test file already), the bare name
        # `githubasyncio` used by async_path above isn't otherwise bound in the test file — make
        # sure it is.
        import_stmt = f"import githubasyncio.{mod}"
        if import_stmt not in result:
            result = result.replace("import github\n", f"import github\n{import_stmt}\n", 1)

        def _bridge_async_static(m: re.Match, _path: str = async_path) -> str:
            arg = m.group(1)
            return (
                f"object.__getattribute__(self.repo, '_loop').run_until_complete("
                f"{_path}("
                f"SyncProxy._deep_unwrap({arg})))"
            )

        result = re.sub(
            rf"{re.escape(async_path)}\(([^)]+)\)",
            _bridge_async_static,
            result,
        )
    # Ensure SyncProxy is importable in the test
    if "SyncProxy._deep_unwrap" in result and "from tests.AsyncFramework import SyncProxy" not in result:
        # SyncProxy is defined in AsyncFramework.py which is already imported
        # but may not be explicitly imported. Add import if needed.
        if "SyncProxy" not in result.split("class ")[0]:
            result = result.replace(
                "from tests import AsyncFramework as Framework",
                "from tests import AsyncFramework as Framework\nfrom tests.AsyncFramework import SyncProxy",
            )

    # General module-qualified redirect (`github.<Module>.<ClassName>`) for every other class with
    # a generated async twin, covering two distinct cases with two different safety rules:
    #  - A class outside `analyzer.async_classes` (no I/O, no async methods -- e.g. ReviewerParams,
    #    EnvironmentDeploymentBranchPolicyParams: plain parameter containers living in an otherwise
    #    I/O-bearing module, so they don't qualify for whole-module PURE_DATA_MODULES treatment)
    #    behaves exactly like Auth above: redirecting it, constructor call included, is always
    #    correct regardless of protected ranges, since there's no behavioral difference between the
    #    sync and async twin to begin with.
    #  - A class inside `analyzer.async_classes` (Repository, NamedUser, PaginatedList, HookDelivery,
    #    Migration, ...) is only touched when the reference is NOT an actual construction (i.e. not
    #    immediately followed by `(`) -- e.g. an assertIsInstance/assertRaises target, a bound
    #    staticmethod/classmethod access (`Cls.method(...)`), or a class object passed as a plain
    #    argument (`self.g.create_from_raw_data(github.NamedUser.NamedUser, ...)`, where the actual
    #    construction happens inside already-async code, not in the test body). An actual
    #    construction site needs case-by-case Framework.make_async() wrapping instead (see the
    #    requester-spec-mock pass above for the one general pattern already covered); left alone
    #    here. Respects the same protected ranges as the entry-point/Auth/Requester rewrites above,
    #    for the same reason: a reference compared against an object a protected method deliberately
    #    kept classic must stay classic too, or the comparison silently changes meaning. Runs after
    #    the async-static-method bridging pass above (not before it): that pass looks for the exact
    #    sync-qualified text `github.{mod}.{cls}.{meth}` to know which calls need event-loop
    #    bridging, so this pass must not have already rewritten it to `githubasyncio.{mod}.{cls}`
    #    first, or the bridging pass would silently skip it, leaving a raw unawaited coroutine
    #    (verified empirically: Repository.py's `as_url_param` static-method test regressed exactly
    #    this way when this pass ran before the bridging pass instead).
    _excluded_mods = {"Auth", "Requester"} | {mod for mod, _ in _entry_point_pairs}
    _general_candidates = {
        cls_name: mod_name for cls_name, mod_name in analyzer.class_to_file.items() if mod_name not in _excluded_mods
    }
    _general_rewritten = False
    _general_lines = result.split("\n")
    for _i, _line in enumerate(_general_lines):
        stripped = _line.lstrip()
        if stripped.startswith("import ") or stripped.startswith("from "):
            continue  # import lines are handled separately (reimport machinery / Step 1 equivalents)
        _in_protected = any(start <= _i < end for start, end in _protected_ranges)
        new_line = _line
        for cls_name, mod_name in sorted(_general_candidates.items(), key=lambda kv: len(kv[0]), reverse=True):
            pattern = rf"\bgithub\.{re.escape(mod_name)}\.{re.escape(cls_name)}\b"
            if cls_name in analyzer.async_classes:
                if _in_protected:
                    continue
                pattern += r"(?!\()"
            new_line, _n = re.subn(pattern, f"githubasyncio.{mod_name}.{cls_name}", new_line)
            _general_rewritten = _general_rewritten or _n > 0
        _general_lines[_i] = new_line
    result = "\n".join(_general_lines)
    if _general_rewritten:
        result = _ensure_bare_githubasyncio_import(result)

    # `pickle.dumps(X)`: X is typically a SyncProxy-wrapped async object (self.g / make_async()
    # results), whose __class__ spoofing breaks pickle's protocol. The raw async object underneath
    # pickles fine (Requester drops its lock/connection in __getstate__ and recreates them in
    # __setstate__), so unwrap it first; what pickle.loads() returns is then a raw async object,
    # which is all the (attribute-inspecting) assertions after it need.
    _pickle_re = re.compile(r"\bpickle\.dumps\(([^()]*)\)")
    if _pickle_re.search(result):
        result = _pickle_re.sub(r"pickle.dumps(SyncProxy._deep_unwrap(\1))", result)
        if "from tests.AsyncFramework import SyncProxy" not in result:
            result = result.replace(
                "from tests import AsyncFramework as Framework",
                "from tests import AsyncFramework as Framework\nfrom tests.AsyncFramework import SyncProxy",
            )

    # `type(X)`: X may now be a SyncProxy (e.g. a value reached through a wrapped client, like
    # `g._Github__requester.kwargs["auth"]`), whose __class__ spoofing satisfies isinstance() but not
    # type(). Framework.type_of() unwraps first, and is plain type() for anything else (the classic
    # tests only ever call one-argument type()).
    if "from tests import AsyncFramework as Framework" in result:
        result = re.sub(r"(?<![\w.])type\(", "Framework.type_of(", result)

    # Every `githubasyncio.<Module>.` reference must have its submodule imported: a bare
    # `import githubasyncio` doesn't bind `githubasyncio.<Module>` unless something already loaded
    # it (which the classic `github.<Module>` form got for free from the file's own `import
    # github.<Module>` lines, now redirected or removed). One sweep after all rewrite passes,
    # instead of each pass tracking the modules it introduced.
    _used_async_mods = sorted(
        {m for m in re.findall(r"\bgithubasyncio\.(\w+)\.", result) if (DST_PKG / f"{m}.py").exists()}
    )
    _missing_async_mods = [
        m for m in _used_async_mods if not re.search(rf"^import githubasyncio\.{m}\s*$", result, re.MULTILINE)
    ]
    if _missing_async_mods:
        _anchor = None
        for _anchor in re.finditer(
            r"^import githubasyncio(?:\.\w+)?\s*$|^import github(?:\.\w+)?\s*$", result, re.MULTILINE
        ):
            pass
        if _anchor is not None:
            result = (
                result[: _anchor.end()]
                + "".join(f"\nimport githubasyncio.{m}" for m in _missing_async_mods)
                + result[_anchor.end() :]
            )

    # Convert assertTrue(isinstance(X, Y)) -> assertIsInstance(X, Y)
    # This is needed because SyncProxy wraps objects, so isinstance() fails
    # on the raw wrapper.  assertIsInstance is overridden in Framework to unwrap.
    result = re.sub(
        r"self\.assertTrue\(isinstance\((.+?),\s*(.+?)\)\)",
        r"self.assertIsInstance(\1, \2)",
        result,
    )

    # Remove bare `assert isinstance(...)` statements (often "Make type checker happy")
    # These fail in async tests because the unwrapped object is an async class instance.
    result = re.sub(
        r"^\s*assert isinstance\(.+?\)\s*$",
        "        pass  # bare isinstance removed for async tests",
        result,
        flags=re.MULTILINE,
    )

    return result


def write_file(path: Path, content: str):
    """
    Write content to path, creating parent dirs as needed.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _find_tool(name: str) -> str | None:
    """
    Find a formatter binary.

    Looks in the running interpreter's bin directory first (covers the pre-commit venv that installs tools via
    additional_dependencies), then falls back to .venv/bin for manual / CI runs.

    """
    # 1. Same bin dir as the running python (pre-commit venv).
    # Do NOT resolve() here: in a venv, sys.executable is a symlink to the base
    # interpreter, and resolving it would escape the venv and pick up whatever
    # (unpinned) tool versions are installed in the base interpreter's bin dir.
    interpreter_bin = Path(sys.executable).parent
    candidate = interpreter_bin / name
    if candidate.exists():
        return str(candidate)
    # 2. Project .venv
    candidate = REPO_ROOT / ".venv" / "bin" / name
    if candidate.exists():
        return str(candidate)
    # 3. shutil.which as last resort
    return shutil.which(name)


FORMATTERS = ("pyupgrade", "ruff", "docformatter", "black")


def _require_tools() -> dict[str, str]:
    """
    Resolve all formatter binaries, exiting with an error if any is missing.

    Called before any output is written so a missing tool does not leave behind unformatted generated files.

    """
    tools = {name: _find_tool(name) for name in FORMATTERS}
    missing = [name for name, path in tools.items() if path is None]
    if missing:
        logger.error(
            "Required command(s) not found: %s. Install them (e.g. `pip install %s`) and retry.",
            ", ".join(missing),
            " ".join(missing),
        )
        sys.exit(1)
    return {name: path for name, path in tools.items() if path is not None}


def run_formatters(directory: Path, tools: dict[str, str]):
    """
    Run the same formatter chain as pre-commit (in the same order) so that the generated output is already stable and
    won't cause cascading "files were modified" failures on the next pre-commit run.

    Order: pyupgrade → ruff → docformatter → black

    """
    py_files = sorted(directory.rglob("*.py"))

    # 1. pyupgrade --py39-plus  (per-file tool)
    logger.info("  Running pyupgrade on %s...", directory)
    for f in py_files:
        subprocess.run(
            [tools["pyupgrade"], "--py39-plus", str(f)],
            cwd=str(REPO_ROOT),
            capture_output=True,
        )

    # 2. ruff check --fix --fixable=ALL  (matches pre-commit args)
    logger.info("  Running ruff check --fix on %s...", directory)
    subprocess.run(
        [tools["ruff"], "check", "--fix", "--fixable=ALL", str(directory), "--quiet"],
        cwd=str(REPO_ROOT),
        capture_output=True,
    )

    # 3. docformatter --in-place  (per-file tool, reads config from pyproject.toml)
    logger.info("  Running docformatter on %s...", directory)
    for f in py_files:
        subprocess.run(
            [tools["docformatter"], "--in-place", str(f)],
            cwd=str(REPO_ROOT),
            capture_output=True,
        )

    # 4. black  (directory-level tool, reads config from pyproject.toml)
    logger.info("  Running black on %s...", directory)
    subprocess.run(
        [tools["black"], str(directory), "--quiet"],
        cwd=str(REPO_ROOT),
        capture_output=True,
    )


def main():
    parser = argparse.ArgumentParser(description="PyGithub Async Code Generator")
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable DEBUG-level logging for the full decision tree"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    tools = _require_tools()

    logger.info("[1/6] Parsing source files...")
    analyzer = IOAnalyzer()
    analyzer.parse_all()
    logger.info(f"Found {len(analyzer.trees)} source modules")
    logger.info(f"Found {len(analyzer.class_to_file)} classes")

    logger.info("[2/6] Analyzing I/O dependencies...")
    analyzer.build_type_registry()
    logger.info(
        "Type registry: %d return types, %d param types",
        len(analyzer.return_types),
        len(analyzer.param_types),
    )
    analyzer.seed_io_classes()
    logger.info(f"I/O root classes: {sorted(analyzer.async_classes)}")
    analyzer.propagate_async_classes()
    logger.info(f"Total async classes: {len(analyzer.async_classes)}")
    analyzer.analyze_methods()
    total_methods = sum(len(v) for v in analyzer.async_methods.values())
    logger.info(f"Total async methods: {total_methods}")

    # Verify no __init__ got through
    for cls, methods in analyzer.async_methods.items():
        for m in NEVER_ASYNC_METHODS:
            if m in methods:
                logger.warning(f"{cls}.{m} is in async_methods (should not be!)")

    # Show some details
    for cls in sorted(analyzer.async_methods.keys()):
        methods = analyzer.async_methods[cls]
        if methods:
            logger.debug("%s: %s", cls, sorted(methods))

    logger.info(f"[3/6] Generating async source files in {DST_PKG}...")

    # Clean output directory
    if DST_PKG.exists():
        shutil.rmtree(DST_PKG)
    DST_PKG.mkdir(parents=True)

    transformer = AsyncTransformer(analyzer)
    generated_count = 0

    # Generate __init__.py
    write_file(DST_PKG / "__init__.py", generate_async_init())
    generated_count += 1

    # Generate requestlib.py (niquests-only shim; see generate_async_requestlib())
    write_file(DST_PKG / "requestlib.py", generate_async_requestlib())
    generated_count += 1

    # Generate transformed source files
    reexport_count = 0
    for p in sorted(SRC_PKG.glob("*.py")):
        stem = p.stem
        if stem in SKIP_STEMS or stem.startswith("_"):
            logger.debug("main: skipping %s (SKIP_FILES or private)", stem)
            continue

        src = p.read_text(encoding="utf-8")

        if stem in analyzer.trees and stem not in CIRCULAR_IMPORT_REEXPORT:
            # Full transform: whether or not this module has classes needing actual async
            # rewriting, the pass still fixes up its imports (github.X -> githubasyncio.X) so the
            # result is a genuine, self-contained copy rather than a stub re-exporting from the
            # classic package (`from github.X import *`) -- githubasyncio must not need the
            # classic PyGithub package installed. transform_file() is a safe no-op for any classes
            # it finds with nothing to make async.
            logger.debug("main: full transform for %s", stem)
            transformed = transformer.transform_file(stem, src)
        elif stem in CIRCULAR_IMPORT_REEXPORT:
            logger.debug("main: re-export stub for %s (CIRCULAR_IMPORT_REEXPORT)", stem)
            transformed = _generate_reexport_stub(stem)
            reexport_count += 1
        else:
            # Module not in parsed trees (e.g. a SyntaxError) — can't be transformed at all.
            # Falls back to a re-export stub, the one case where githubasyncio still ends up
            # needing the classic package.
            logger.debug("main: re-export stub for %s (not in parsed trees)", stem)
            transformed = _generate_reexport_stub(stem)
            reexport_count += 1

        write_file(DST_PKG / f"{stem}.py", transformed)
        generated_count += 1

    logger.info(f"Generated {generated_count} files ({reexport_count} re-export stubs)")

    logger.info(f"[4/6] Generating async test files in {TEST_DST}...")

    # Clean generated test files but preserve hand-maintained ones (PRESERVE_TEST_FILES).
    if TEST_DST.exists():
        for p in TEST_DST.iterdir():
            if p.name not in PRESERVE_TEST_FILES:
                if p.is_dir():
                    shutil.rmtree(p)
                else:
                    p.unlink()
    else:
        TEST_DST.mkdir(parents=True)

    write_file(TEST_DST / "__init__.py", AUTO_HEADER)

    # Copy sync test infrastructure byte-for-byte (see COPY_TEST_FILES) so the async project
    # doesn't need the classic checkout at import time.
    for name in COPY_TEST_FILES:
        src_file = TEST_SRC / name
        if src_file.exists():
            write_file(TEST_DST / name, AUTO_HEADER + src_file.read_text(encoding="utf-8"))
            logger.debug("main: copied sync test infrastructure %s", name)

    # Copy the hand-maintained async test framework in from its template (see
    # TEMPLATE_TEST_FILES) -- self-contained, no classic package dependency at all.
    for name, template_file in TEMPLATE_TEST_FILES.items():
        write_file(TEST_DST / name, AUTO_HEADER + template_file.read_text(encoding="utf-8"))
        logger.debug("main: copied async test framework template %s", name)

    test_count = 0
    for p in sorted(TEST_SRC.glob("*.py")):
        if p.name in SKIP_TEST_FILES:
            logger.debug("main: skipping test %s (SKIP_TEST_FILES)", p.name)
            continue
        if p.is_dir():
            continue

        src = p.read_text(encoding="utf-8")

        # Only transform files that are actual test files (contain test classes)
        if not any(marker in src for marker in TEST_BASE_CLASS_MARKERS):
            logger.debug("main: skipping test %s (no TestCase/BasicTestCase)", p.name)
            continue

        logger.debug("main: transforming test file %s", p.name)
        transformed = transform_test_file(src, p.stem, analyzer)
        write_file(TEST_DST / p.name, transformed)
        test_count += 1

    logger.info(f"Generated {test_count} async test files")

    logger.info("[5/6] Running formatters...")
    run_formatters(DST_PKG, tools)
    run_formatters(TEST_DST, tools)
    logger.info("Done.")

    logger.info("[6/6] Syntax-checking generated files...")
    errors = 0
    for p in sorted(DST_PKG.glob("*.py")):
        try:
            compile(p.read_text(encoding="utf-8"), str(p), "exec")
        except SyntaxError as e:
            logger.error(f"SYNTAX ERROR in {p.name}:{e.lineno}: {e.msg}")
            errors += 1
    for p in sorted(TEST_DST.glob("*.py")):
        try:
            compile(p.read_text(encoding="utf-8"), str(p), "exec")
        except SyntaxError as e:
            logger.error(f"SYNTAX ERROR in tests/{p.name}:{e.lineno}: {e.msg}")
            errors += 1

    logger.info("Generation complete!")
    logger.info(f"Async source: {DST_PKG}")
    logger.info(f"Async tests:  {TEST_DST}")

    if errors:
        logger.error(f"{errors} files with syntax errors! The async_generator NEED updating!")
        exit(1)
    else:
        logger.info("All files pass syntax check. Excellent news! Have a great day.")


if __name__ == "__main__":
    main()
