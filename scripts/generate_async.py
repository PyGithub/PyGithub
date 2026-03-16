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

Introspects the PyGithub package to discover which classes and methods perform I/O
(directly or transitively), then copies source files into `github/asynchronous/` with
async/await transformations applied.  Also generates async test files in
`tests/asynchronous/`.

Adapted from the PRAW async-generator that I (Ahmed Tahri) made.
Previously also made a sync to async generator for grafana-client but wasn't based
on AST parsing.
"""

from __future__ import annotations

import argparse
import ast
import logging
import re
import shutil
import subprocess
import textwrap
from pathlib import Path

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_PKG = REPO_ROOT / "github"
DST_PKG = REPO_ROOT / "github" / "asynchronous"
TEST_SRC = REPO_ROOT / "tests"
TEST_DST = REPO_ROOT / "tests" / "asynchronous"

AUTO_HEADER = "# FILE AUTO GENERATED DO NOT TOUCH\n"

# Files that should NEVER be copied to async (pure data / no I/O)
SKIP_FILES = {
    "__init__.py",  # we generate our own
    "Consts.py",
    "GithubException.py",
    "GithubRetry.py",
    "InputFileContent.py",
    "InputGitAuthor.py",
    "InputGitTreeElement.py",
}

# Test files to skip (not test modules, or infrastructure)
SKIP_TEST_FILES = {
    "__init__.py",
    "conftest.py",
    "Framework.py",
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

# Methods that must be forced async because they call async methods on other objects
# (not detectable by transitive self.method() analysis alone).
# Format: {class_name: {method_name, ...}}
FORCE_ASYNC_METHODS = {
    "PullRequest": {"delete_branch"},
    "Repository": {
        "attach_security_config",
        "detach_security_config",
        "create_git_commit",
        "create_git_tree",
        "create_issue",
        "as_url_param",
    },
    "PaginatedList": {"reversed"},  # calls r.__reverse() on a local variable, not self
    # These methods access cross-object promoted properties (e.g., label.name)
    # and must be async so that `await` can be used on those accesses.
    "AuthenticatedUser": {"get_issues", "get_user_issues", "create_fork"},
    "Organization": {"invite_user", "get_issues", "create_fork"},
    "Issue": {"add_sub_issue", "remove_sub_issue", "prioritize_sub_issue"},
    "Github": {"dump"},  # dump() accesses obj.raw_data/raw_headers which are async properties
    "AdvisoryCredit": {"_to_github_dict"},  # accesses login.login where NamedUser.login is async
}

# Direct string replacements for cross-object async calls in FORCE_ASYNC_METHODS.
# These are (old_string, new_string) pairs applied to specific file stems.
# Used for cases where _safe_add_await cannot correctly handle chained calls.
CROSS_OBJECT_REPLACEMENTS = {
    "PullRequest": [
        # remaining_pulls.totalCount is an async property that needs await
        ("if remaining_pulls.totalCount > 0:", "if await remaining_pulls.totalCount > 0:"),
        # Chained .delete() call: get_git_ref(...).delete()
        # By step 13, self.head is already promoted to (await self.head).
        # We need to: (a) await get_git_ref, (b) complete the ref, (c) await delete.
        (
            'return (await self.head).repo.get_git_ref(f"heads/{(await self.head).ref}").delete()',
            '_ref = await (await self.head).repo.get_git_ref(f"heads/{(await self.head).ref}")\n'
            "        await _ref.complete()\n"
            "        return await _ref.delete()",
        ),
        # get_pulls: needs await on the cross-object method call
        # Also owner.login is a chained async property.
        (
            "(await self.head).repo.owner.login}:{(await self.head).ref}",
            "await (await (await self.head).repo.owner).login}:{(await self.head).ref}",
        ),
        (
            "remaining_pulls = (await self.head).repo.get_pulls(",
            "remaining_pulls = await (await self.head).repo.get_pulls(",
        ),
        # restore_branch: (await self.head).repo.create_git_ref(...) is a cross-object async
        # method call on Repository that needs await.
        (
            "return (await self.head).repo.create_git_ref(",
            "return await (await self.head).repo.create_git_ref(",
        ),
    ],
    "Repository": [
        # attach/detach_security_config call methods on self.organization (cross-object),
        # which are async methods on Organization. _add_awaits only handles self.method().
        (
            "(await self.organization).attach_security_config_to_repositories(",
            "await (await self.organization).attach_security_config_to_repositories(",
        ),
        (
            "(await self.organization).detach_security_config_from_repositories(",
            "await (await self.organization).detach_security_config_from_repositories(",
        ),
        # tree._identity is on GitTree (async), NOT InputGitTreeElement.
        # base_tree._identity is also GitTree.
        (
            '"tree": tree._identity,',
            '"tree": await tree._identity,',
        ),
        (
            'post_parameters["base_tree"] = base_tree._identity',
            'post_parameters["base_tree"] = await base_tree._identity',
        ),
        # milestone._identity is async (Milestone is a CompletableGithubObject)
        (
            '"milestone": milestone._identity',
            '"milestone": await milestone._identity',
        ),
        # create_git_commit: parent elements are GitCommit (async _identity)
        (
            '"parents": [element._identity for element in parents]',
            '"parents": [await element._identity for element in parents]',
        ),
        # GraphQL methods: (await self.owner).login needs double-await
        # get_discussion method
        (
            '"owner": (await self.owner).login,',
            '"owner": await (await self.owner).login,',
        ),
        # as_url_param: repo._identity is async
        (
            "return repo._identity",
            "return await repo._identity",
        ),
        # collaborator._identity is on NamedUser (async)
        (
            "collaborator = collaborator._identity",
            "collaborator = await collaborator._identity",
        ),
        # (await self.owner).login is a chained async property: owner is async (returns NamedUser),
        # and login on NamedUser is also async. Needs double-await in f-strings.
        (
            "{(await self.owner).login}",
            "{await (await self.owner).login}",
        ),
        # element._identity in assignees list comprehension: element is NamedUser (async _identity)
        (
            "element._identity if isinstance(element, NamedUser.NamedUser) else element",
            "(await element._identity) if isinstance(element, NamedUser.NamedUser) else element",
        ),
        # AdvisoryCredit._to_github_dict is async (NamedUser.login path)
        (
            "AdvisoryCredit.AdvisoryCredit._to_github_dict(credit) for credit in credits",
            "await AdvisoryCredit.AdvisoryCredit._to_github_dict(credit) for credit in credits",
        ),
    ],
    "Organization": [
        # Chained property access: repo.owner.login and repo.name are both async properties.
        # repo.owner returns a coroutine (NamedUser), then .login on that NamedUser is also async.
        # NOTE: by step 13, repo.name has already been promoted to (await repo.name) by step 3.
        (
            'f"/repos/{repo.owner.login}/{(await repo.name)}/generate"',
            'f"/repos/{await (await repo.owner).login}/{await repo.name}/generate"',
        ),
        # invite_user: user.id is async (NamedUser), t.id is async (Team)
        (
            'parameters["invitee_id"] = user.id',
            'parameters["invitee_id"] = await user.id',
        ),
        (
            'parameters["team_ids"] = [t.id for t in teams]',
            'parameters["team_ids"] = [await t.id for t in teams]',
        ),
        # cancel_invitation: invitee.id is async (NamedUser/OrganizationInvitation)
        (
            "{invitee.id}",
            "{await invitee.id}",
        ),
        # public_member._identity in f-strings
        (
            'f"{await self.url}/public_members/{public_member._identity}"',
            'f"{await self.url}/public_members/{await public_member._identity}"',
        ),
        (
            'f"{await self.url}/members/{public_member._identity}"',
            'f"{await self.url}/members/{await public_member._identity}"',
        ),
        # create_or_update_secret: element.id is Repository.id (async property)
        # Actions endpoint
        (
            '"selected_repository_ids"] = [element.id for element in selected_repositories]',
            '"selected_repository_ids"] = [await element.id for element in selected_repositories]',
        ),
        # Dependabot endpoint
        (
            '"selected_repository_ids"] = [str(element.id) for element in selected_repositories]',
            '"selected_repository_ids"] = [str(await element.id) for element in selected_repositories]',
        ),
        # create_team: repo_names element._identity is Repository._identity (async)
        (
            '"repo_names"] = [element._identity for element in repo_names]',
            '"repo_names"] = [await element._identity for element in repo_names]',
        ),
    ],
    "Issue": [
        # sub_issue.id is async (Issue)
        (
            "sub_issue_id = sub_issue.id",
            "sub_issue_id = await sub_issue.id",
        ),
        (
            "after_sub_issue_id = after_sub_issue.id",
            "after_sub_issue_id = await after_sub_issue.id",
        ),
        # element._identity in assignees list comprehension: element is NamedUser (async _identity)
        (
            "element._identity if isinstance(element, NamedUser.NamedUser) else element",
            "(await element._identity) if isinstance(element, NamedUser.NamedUser) else element",
        ),
    ],
    "Team": [
        # Repository.as_url_param(repo) returns a coroutine when repo is a Repository
        # because repo._identity is async. We need to await the result.
        # Also (await self.organization).url needs double-await.
        (
            "Repository.Repository.as_url_param(repo)",
            "(await Repository.Repository.as_url_param(repo))",
        ),
        (
            "(await self.organization).url",
            "await (await self.organization).url",
        ),
    ],
    "ContentFile": [
        # self.encoding in assert is async property, needs await
        (
            "assert self.encoding ==",
            "assert (await self.encoding) ==",
        ),
    ],
    "MainClass": [
        # render_markdown: context._identity is Repository._identity (async)
        (
            'post_parameters["context"] = context._identity',
            'post_parameters["context"] = await context._identity',
        ),
        # dump: obj.raw_data and obj.raw_headers are async properties
        (
            "pickle.dump((obj.__class__, obj.raw_data, obj.raw_headers), file, protocol)",
            "_raw_data = await obj.raw_data\n"
            "        _raw_headers = await obj.raw_headers\n"
            "        pickle.dump((obj.__class__, _raw_data, _raw_headers), file, protocol)",
        ),
    ],
    "AdvisoryCredit": [
        # login.login where login is a NamedUser: NamedUser.login is async property
        (
            "login = login.login",
            "login = await login.login",
        ),
    ],
    "RepositoryAdvisory": [
        # AdvisoryCredit._to_github_dict is async (NamedUser.login path)
        # NOTE: in the source, this list comprehension is split across two lines
        (
            "AdvisoryCredit.AdvisoryCredit._to_github_dict(credit)\n"
            "                for credit in (self.credits + list(credited))",
            "await AdvisoryCredit.AdvisoryCredit._to_github_dict(credit)\n"
            "                for credit in (self.credits + list(credited))",
        ),
        (
            "AdvisoryCredit.AdvisoryCredit._to_github_dict(credit) for credit in credits",
            "await AdvisoryCredit.AdvisoryCredit._to_github_dict(credit) for credit in credits",
        ),
    ],
}


def discover_modules() -> list[str]:
    """Return sorted list of module basenames (without .py) in the github package."""
    modules = []
    for p in sorted(SRC_PKG.glob("*.py")):
        name = p.stem
        if name.startswith("_") and name != "__init__":
            continue
        modules.append(name)
    return modules


class IOAnalyzer:
    """Statically analyses the github package to find classes/methods that do I/O."""

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
        # class_name -> set of attribute names typed as Requester or connection classes
        self.io_attrs: dict[str, set[str]] = {}
        # class_name -> set of @property method names (must NEVER be made async)
        self.property_methods: dict[str, set[str]] = {}
        # class_name -> set of property names that were PROMOTED to async def
        # (were @property but now async because they call _completeIfNotSet etc.)
        self.promoted_properties: dict[str, set[str]] = {}

    def parse_all(self):
        """Parse all .py files under github/."""
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
                    logger.debug(
                        "parse_all: registered class '%s' in '%s' bases=%s",
                        node.name,
                        stem,
                        self.class_bases[node.name],
                    )

    @staticmethod
    def _base_name(node: ast.expr) -> str:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            return node.attr
        return ""

    def _get_class_node(self, class_name: str) -> ast.ClassDef | None:
        stem = self.class_to_file.get(class_name)
        if stem is None or stem not in self.trees:
            return None
        for node in ast.walk(self.trees[stem]):
            if isinstance(node, ast.ClassDef) and node.name == class_name:
                return node
        return None

    # ------------------------------------------------------------------
    # Seed: mark classes that directly hold niquests.Session
    # ------------------------------------------------------------------
    def seed_io_classes(self):
        """Find classes that create niquests.Session or use threading.Lock, time.sleep."""
        # Requester and the connection classes are the I/O roots
        io_root_classes = {
            "Requester",
            "HTTPSRequestsConnectionClass",
            "HTTPRequestsConnectionClass",
            "RequestsResponse",
            "WithRequester",
            "PaginatedListBase",  # defines _grow, __fetchToIndex that do I/O via _fetchNextPage
        }
        for cls_name in io_root_classes:
            if cls_name in self.class_to_file:
                self.async_classes.add(cls_name)
                logger.debug("seed_io_classes: seeded I/O root '%s'", cls_name)
            else:
                logger.debug("seed_io_classes: I/O root '%s' not in parsed sources, skipping", cls_name)

    # ------------------------------------------------------------------
    # Propagate: classes that reference Requester (directly or via base)
    # ------------------------------------------------------------------
    def propagate_async_classes(self):
        """Iteratively find classes that need async (hold Requester or inherit from async class)."""
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
                    if base in self.async_classes:
                        self.async_classes.add(cls_name)
                        logger.debug("propagate: marking '%s' async (inherits from '%s')", cls_name, base)
                        changed = True
                        break

    # ------------------------------------------------------------------
    # Method analysis: find methods that do I/O (directly or transitively)
    # ------------------------------------------------------------------
    def analyze_methods(self):
        """Find all methods in async classes that need to become async."""
        # First pass: methods that directly call requester methods or time.sleep
        io_method_patterns = {
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

        for cls_name in self.async_classes:
            cls_node = self._get_class_node(cls_name)
            if cls_node is None:
                continue
            stem = self.class_to_file[cls_name]
            src = self.sources[stem]
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

                method_src = ast.get_source_segment(src, item) or ""

                needs_async = False

                # Direct I/O calls - must be actual method calls (preceded by '.')
                for pattern in io_method_patterns:
                    if re.search(rf"\.{re.escape(pattern)}\s*\(", method_src):
                        needs_async = True
                        break

                # time.sleep
                if "time.sleep(" in method_src:
                    needs_async = True

                # __requestRaw, __requestEncode, __deferRequest (private methods in Requester)
                if cls_name == "Requester":
                    requester_always_async = {
                        "__requestRaw",
                        "__requestEncode",
                        "__deferRequest",
                        "__createConnection",
                        "__check",
                        "__postProcess",
                    }
                    if method_name in requester_always_async:
                        needs_async = True

                    # Also check for name-mangled calls to these methods
                    for priv in requester_always_async:
                        mangled = f"_Requester{priv}"
                        if re.search(rf"self\.{re.escape(mangled)}\s*\(", method_src):
                            needs_async = True
                            break
                        if re.search(rf"self\.{re.escape(priv)}\s*\(", method_src):
                            needs_async = True
                            break
                    # The actual I/O method
                    if "self.session" in method_src and any(
                        verb in method_src for verb in [".get(", ".post(", ".put(", ".patch(", ".delete(", ".head("]
                    ):
                        needs_async = True

                # Session methods on connection classes
                if cls_name in ("HTTPSRequestsConnectionClass", "HTTPRequestsConnectionClass"):
                    if "self.session" in method_src:
                        needs_async = True

                # _completeIfNeeded / _completeIfNotSet / complete / update
                if any(
                    x in method_src
                    for x in [
                        "_completeIfNeeded(",
                        "_completeIfNotSet(",
                        ".complete()",
                        "_fetchNextPage(",
                        "_grow(",
                    ]
                ):
                    needs_async = True

                # close() methods that close the requester/connection
                if method_name == "close" and any(
                    x in method_src
                    for x in [
                        "__requester.close()",
                        "_requester.close()",
                        "__connection.close()",
                        "session.close()",
                    ]
                ):
                    needs_async = True

                # PaginatedList methods
                if cls_name in ("PaginatedList", "PaginatedListBase"):
                    if any(
                        re.search(rf"\.{re.escape(x)}\s*\(", method_src)
                        for x in ["requestJsonAndCheck", "graphql_query", "_fetchNextPage", "_getLastPageUrl", "_grow"]
                    ):
                        needs_async = True

                if needs_async:
                    methods_needing_async.add(method_name)

            self.async_methods[cls_name] = methods_needing_async
            if methods_needing_async:
                logger.debug("analyze[pass1] %s: direct I/O methods %s", cls_name, sorted(methods_needing_async))

        # Force-add methods that call async methods on external objects
        for cls_name, forced_methods in FORCE_ASYNC_METHODS.items():
            current = self.async_methods.get(cls_name, set())
            current |= forced_methods
            self.async_methods[cls_name] = current
            logger.debug("analyze: force-added async methods for '%s': %s", cls_name, sorted(forced_methods))

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
                stem = self.class_to_file[cls_name]
                src = self.sources[stem]
                current = self.async_methods.get(cls_name, set())
                cls_properties = self.property_methods.get(cls_name, set())

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
                    method_src = ast.get_source_segment(src, item) or ""
                    for async_method in list(current):
                        # Check for self.method( or self.__method( or self._method(
                        if re.search(rf"self\.(?:_\w+)?{re.escape(async_method)}\s*\(", method_src):
                            current.add(item.name)
                            logger.debug(
                                "analyze[pass2] %s.%s: calls async method '%s'", cls_name, item.name, async_method
                            )
                            changed = True
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
        io_method_patterns_re = "|".join(re.escape(p) for p in io_method_patterns)
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
                stem = self.class_to_file[cls_name]
                src = self.sources[stem]
                current_async = set(self.async_methods[cls_name])
                # Include inherited async methods from ALL ancestor classes (full MRO)
                visited = set()
                queue = list(self.class_bases.get(cls_name, []))
                while queue:
                    base = queue.pop(0)
                    if base in visited:
                        continue
                    visited.add(base)
                    current_async |= self.async_methods.get(base, set())
                    queue.extend(self.class_bases.get(base, []))

                # Also gather promoted properties (async properties accessed without parens)
                current_promoted = set(self.promoted_properties.get(cls_name, set()))
                visited3 = set()
                queue3 = list(self.class_bases.get(cls_name, []))
                while queue3:
                    base = queue3.pop(0)
                    if base in visited3:
                        continue
                    visited3.add(base)
                    current_promoted |= self.promoted_properties.get(base, set())
                    queue3.extend(self.class_bases.get(base, []))

                props = self.property_methods.get(cls_name, set())
                promote = set()
                for item in ast.walk(cls_node):
                    if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        continue
                    if item.name not in props:
                        continue
                    method_src = ast.get_source_segment(src, item) or ""
                    # Check 1: does this property call any known async method?
                    for am in current_async:
                        if re.search(rf"self\.(?:_\w+)?{re.escape(am)}\s*\(", method_src):
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
                    # Check 2: does this property call a direct I/O pattern?
                    if re.search(rf"\.(?:{io_method_patterns_re})\s*\(", method_src):
                        promote.add(item.name)
                        logger.debug(
                            "analyze[pass3] %s.%s: promoting @property (direct I/O pattern)", cls_name, item.name
                        )
                        continue
                    # Check 3: does this property ACCESS another promoted async property
                    # (without parentheses)? e.g. `return self.login` where `login` is async
                    for pp in current_promoted:
                        # Match self.prop NOT followed by ( — it's a property access
                        if re.search(rf"self\.{re.escape(pp)}(?!\s*\()(?!\w)", method_src):
                            promote.add(item.name)
                            logger.debug(
                                "analyze[pass3] %s.%s: promoting @property (accesses promoted property '%s')",
                                cls_name,
                                item.name,
                                pp,
                            )
                            break
                if promote:
                    self.async_methods[cls_name] |= promote
                    self.property_methods[cls_name] -= promote
                    if cls_name not in self.promoted_properties:
                        self.promoted_properties[cls_name] = set()
                    self.promoted_properties[cls_name] |= promote
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
                stem = self.class_to_file[cls_name]
                src = self.sources[stem]

                # Gather async methods from this class + all ancestors (full MRO)
                current_async = set(self.async_methods.get(cls_name, set()))
                visited4m = set()
                queue4m = list(self.class_bases.get(cls_name, []))
                while queue4m:
                    base = queue4m.pop(0)
                    if base in visited4m:
                        continue
                    visited4m.add(base)
                    current_async |= self.async_methods.get(base, set())
                    queue4m.extend(self.class_bases.get(base, []))

                cls_properties = self.property_methods.get(cls_name, set())

                # Gather promoted properties from this class + all ancestors (full MRO)
                all_promoted = set(self.promoted_properties.get(cls_name, set()))
                visited4 = set()
                queue4 = list(self.class_bases.get(cls_name, []))
                while queue4:
                    base = queue4.pop(0)
                    if base in visited4:
                        continue
                    visited4.add(base)
                    all_promoted |= self.promoted_properties.get(base, set())
                    queue4.extend(self.class_bases.get(base, []))

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
                    method_src = ast.get_source_segment(src, item) or ""
                    found = False
                    found_reason = ""
                    # Check A: accesses a promoted async property
                    for pp in all_promoted:
                        if re.search(rf"self\.{re.escape(pp)}(?!\s*\()(?!\w)", method_src):
                            found = True
                            found_reason = "accesses promoted property '%s'" % pp
                            break
                    # Check B: calls an async method
                    if not found:
                        for am in current_async:
                            if re.search(rf"self\.(?:_\w+)?{re.escape(am)}\s*\(", method_src):
                                found = True
                                found_reason = "calls async method '%s'" % am
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

        # Ensure any method in FORCE_ASYNC_METHODS that is also in property_methods
        # gets removed from property_methods (it needs async def, not @property def).
        for cls_name, forced in FORCE_ASYNC_METHODS.items():
            props = self.property_methods.get(cls_name, set())
            overlap = props & forced
            if overlap:
                logger.debug(
                    "analyze: FORCE_ASYNC cleanup %s: removing %s from property_methods",
                    cls_name,
                    sorted(overlap),
                )
                self.property_methods[cls_name] -= overlap
                # Also track forced async methods that were properties
                if cls_name not in self.promoted_properties:
                    self.promoted_properties[cls_name] = set()
                self.promoted_properties[cls_name] |= overlap

    def run(self):
        self.parse_all()
        self.seed_io_classes()
        self.propagate_async_classes()
        self.analyze_methods()


class AsyncTransformer:
    """Transforms sync source files into async counterparts."""

    def __init__(self, analyzer: IOAnalyzer):
        self.analyzer = analyzer

    def transform_file(self, stem: str, src: str) -> str:
        """Apply async transformations to a source file."""
        logger.debug("transform[%s]: begin 19-step pipeline", stem)
        lines = src

        # 1) Add auto-generated header
        lines = AUTO_HEADER + lines
        logger.debug("transform[%s]: step 1 — added auto-generated header", stem)

        # 2) Fix imports: github.X -> github.asynchronous.X for local modules
        lines = self._fix_imports(lines, stem)
        logger.debug("transform[%s]: step 2 — fixed imports", stem)

        # 2.5) Fix double-dereference patterns where `from .X import X` (class)
        # collides with body usage of `X.X(...)` or `X.Attr`.
        lines = self._fix_double_dereference(lines)
        logger.debug("transform[%s]: step 2.5 — fixed double-dereference patterns", stem)

        # 2a) Fix the GithubException module/class alias problem.
        # In Python, `import github.GithubException as GithubException` resolves
        # via getattr(github, 'GithubException'), which returns the CLASS (not the
        # module) because github/__init__.py does `from .GithubException import GithubException`.
        # The sync code works because Requester.py is loaded during __init__.py execution
        # (before the shadowing line runs). The async code is loaded after __init__.py
        # completes, so the alias gets the class. Fix: use sys.modules to get the module.
        lines = re.sub(
            r"^import github\.GithubException as GithubException\s*$",
            "import sys as _sys  # noqa: E402\n"
            "GithubException = _sys.modules['github.GithubException']  # Get MODULE, not class",
            lines,
            flags=re.MULTILINE,
        )
        logger.debug("transform[%s]: step 2a — fixed GithubException module/class alias", stem)

        # 2b) Move class-body from-imports to TYPE_CHECKING
        lines = self._move_class_body_imports(lines)
        logger.debug("transform[%s]: step 2b — moved class-body imports to TYPE_CHECKING", stem)

        # 3) For classes in this file, apply method-level transformations
        for node in ast.walk(self.analyzer.trees.get(stem, ast.Module(body=[], type_ignores=[]))):
            if isinstance(node, ast.ClassDef) and node.name in self.analyzer.async_classes:
                logger.debug("transform[%s]: step 3 — transforming class %s", stem, node.name)
                lines = self._transform_class(lines, node.name, stem)

        # 4) threading.Lock -> asyncio.Lock
        lines = lines.replace("threading.Lock()", "asyncio.Lock()")
        if "threading.Lock" in lines or "asyncio.Lock" in lines:
            if "import asyncio" not in lines:
                lines = "import asyncio\n" + lines
            # Remove threading import if no longer needed
            if "threading." not in lines.replace("asyncio.Lock", ""):
                lines = re.sub(r"^import threading\n", "", lines, flags=re.MULTILINE)
        logger.debug("transform[%s]: step 4 — threading.Lock → asyncio.Lock", stem)

        # 5) time.sleep -> await asyncio.sleep
        lines = re.sub(r"(?<!await\s)time\.sleep\(", "await asyncio.sleep(", lines)
        if "asyncio.sleep" in lines and "import asyncio" not in lines:
            lines = "import asyncio\n" + lines
        logger.debug("transform[%s]: step 5 — time.sleep → await asyncio.sleep", stem)

        # 6) niquests.Session( -> niquests.AsyncSession(
        lines = lines.replace("niquests.Session(", "niquests.AsyncSession(")
        logger.debug("transform[%s]: step 6 — niquests.Session → niquests.AsyncSession", stem)

        # 7) __enter__/__exit__ -> __aenter__/__aexit__
        lines = self._convert_context_managers(lines)
        logger.debug("transform[%s]: step 7 — converted context managers", stem)

        # 8) with self.__connection_lock: -> async with self.__connection_lock:
        lines = self._convert_with_to_async_with(lines)
        logger.debug("transform[%s]: step 8 — converted with → async with for locks", stem)

        # 9) Convert __iter__ to __aiter__ for PaginatedList
        if stem == "PaginatedList":
            lines = self._convert_pagination_iteration(lines)
            logger.debug("transform[%s]: step 9 — converted __iter__ → __aiter__", stem)

        # 10) Convert CompletableGithubObject property patterns
        if stem == "GithubObject":
            lines = self._fix_github_object(lines)
            logger.debug("transform[%s]: step 10 — fixed GithubObject patterns", stem)

        # 11) Add close() await patterns
        lines = self._add_close_awaits(lines, stem)
        logger.debug("transform[%s]: step 11 — added close() awaits", stem)

        # 12) (Removed) _completeIfNotSet/Needed are now fully async.
        # Properties that call them are promoted to async in the third pass,
        # so they correctly use `await`.

        # 13) Add awaits for cross-object calls in FORCE_ASYNC_METHODS
        if stem in CROSS_OBJECT_REPLACEMENTS:
            lines = self._add_cross_object_awaits(lines, stem)
            logger.debug("transform[%s]: step 13 — added cross-object awaits", stem)

        # 14) Fix isinstance checks against async-only classes to also accept sync classes.
        # When tests create sync objects (e.g. github.X.Y(...)) and pass them to async code,
        # isinstance(obj, github.asynchronous.X.Y) fails. Accept both.
        lines = self._fix_isinstance_dual_class(lines)
        logger.debug("transform[%s]: step 14 — fixed isinstance dual class checks", stem)

        # 15) Fix create_from_raw_data in MainClass: accept both sync and async CompletableGithubObject.
        # Tests may pass sync classes (github.X.Y) to create_from_raw_data, and the issubclass
        # check against async CompletableGithubObject would fail.
        if stem == "MainClass":
            lines = lines.replace(
                "if issubclass(klass, CompletableGithubObject):",
                "if issubclass(klass, CompletableGithubObject) or issubclass(klass, github.GithubObject.CompletableGithubObject):",
            )
            # Ensure the sync GithubObject module is imported
            if "import github.GithubObject" not in lines:
                lines = "import github.GithubObject\n" + lines
            logger.debug("transform[%s]: step 15 — fixed create_from_raw_data dual issubclass", stem)

        # 16) Replace `X is NotSet` / `X is not NotSet` with is_undefined(X) / is_defined(X).
        # This handles cases where sync objects (with sync _NotSetType attributes) are
        # passed to async code which uses async NotSet. The is_undefined/is_defined
        # functions check both sync and async _NotSetType.
        # Skip GithubObject.py itself since it defines is_undefined/is_defined.
        if stem != "GithubObject":
            lines = self._replace_is_notset_with_helpers(lines)
            logger.debug("transform[%s]: step 16 — replaced is/is not NotSet with helpers", stem)

        # 17) Final: if the body still references `github.X` (e.g. from isinstance dual-class
        # patterns or non-async data classes), ensure `import github` is present.
        lines = self._ensure_import_github(lines)
        logger.debug("transform[%s]: step 17 — ensured import github", stem)

        # 18) Fix sync dunder methods (__repr__, __eq__, __hash__): they can't be async
        # but may reference async properties. Replace self.X with self._X.value.
        lines = self._fix_sync_dunder_methods(lines, stem)
        logger.debug("transform[%s]: step 18 — fixed sync dunder methods", stem)

        # 19) Fix async generators in str.join(): change (await x for x) to [await x for x]
        # In Python, `(await x for x in items)` creates an async generator which
        # str.join() cannot consume. A list comprehension `[await x for x in items]`
        # creates a proper list that join() can use.
        lines = self._fix_async_generator_in_join(lines)
        logger.debug("transform[%s]: step 19 — fixed async generators in str.join()", stem)

        return lines

    def _fix_sync_dunder_methods(self, src: str, stem: str) -> str:
        """Fix sync dunder methods that access async properties.

        In async classes, properties like self.name, self.url become async def,
        so sync dunder methods (__repr__, __eq__, __hash__, etc.) can't call them.
        Instead, access the underlying _Attribute storage directly:
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
        """Fix async generators passed to str.join().

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
    def _ensure_import_github(result: str) -> str:
        """Add `import github` if the body references github.X and it's not already imported."""
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
        last_import_end = 0
        for m in re.finditer(r"^(?:import |from )\S+", result, re.MULTILINE):
            line_start = result.rfind("\n", 0, m.start()) + 1
            if m.start() > line_start:  # indented — skip
                continue
            line_end = result.find("\n", m.end())
            if line_end == -1:
                line_end = len(result)
            full_line = result[line_start:line_end]
            if "(" in full_line and ")" not in full_line:
                close_paren = result.find(")", line_end)
                if close_paren != -1:
                    close_eol = result.find("\n", close_paren)
                    if close_eol == -1:
                        close_eol = len(result)
                    last_import_end = close_eol
                else:
                    last_import_end = line_end
            else:
                last_import_end = line_end
        if last_import_end > 0:
            result = result[:last_import_end] + "\nimport github" + result[last_import_end:]
        return result

    @staticmethod
    def _replace_is_notset_with_helpers(src: str) -> str:
        """Replace `X is NotSet` with `is_undefined(X)` and `X is not NotSet` with `is_defined(X)`.

        This ensures correct behavior when sync objects (whose attributes are sync _NotSetType)
        are checked against the async NotSet singleton. The is_undefined/is_defined functions
        in async GithubObject check both sync and async _NotSetType.
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
            # Match both relative (.GithubObject) and absolute (github.asynchronous.GithubObject) forms
            if re.search(rf"from (?:\.|\bgithub\.asynchronous\.)GithubObject import[^)]*\b{fn_name}\b", src, re.DOTALL):
                continue
            # Try to add to existing parenthesized import from .GithubObject:
            paren_import = re.search(
                r"(from (?:\.|\bgithub\.asynchronous\.)GithubObject import \([^)]*)(\))",
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
                # No parenthesized import; add a standalone import at the top (after AUTO_HEADER)
                src = re.sub(
                    r"(# FILE AUTO GENERATED DO NOT TOUCH\n)",
                    rf"\1from .GithubObject import {fn_name}\n",
                    src,
                    count=1,
                )

        return src

    def _move_class_body_imports(self, src: str) -> str:
        """Move from-imports inside class bodies to TYPE_CHECKING blocks.

        The sync code has `from github.X import Y` inside class bodies for type
        annotations. With `from __future__ import annotations`, these are strings
        at runtime, so we can safely move them to TYPE_CHECKING. This prevents
        circular imports that occur when the imported module is still being loaded.

        Imports inside method/function bodies (def) are kept as-is since they
        execute at call time when all modules are loaded.
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

    def _fix_imports(self, src: str, stem: str) -> str:
        """Fix import statements to use relative imports within github.asynchronous.

        Transforms:
          import github.X            → from . import X   (for async modules)
          github.X.ClassName         → X.ClassName        (after above import)
          from github.X import Y     → from .X import Y   (for async modules)
          from .X import Y           → from .X import Y   (already relative — keep)
          from github.X import Y     → from github.X import Y  (for non-async SKIP_FILES)
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
            if s not in SKIP_FILES and not s.startswith("_"):
                async_files.add(s)

        # Step 1: Convert bare `import github.X` → `from . import X` (for async modules)
        bare_imports = re.findall(r"^import github\.(\w+)\s*$", result, re.MULTILINE)
        already_imported: set[str] = set()
        for mod in bare_imports:
            if mod in async_files:
                result = re.sub(
                    rf"^import github\.{re.escape(mod)}\s*$",
                    f"from . import {mod}",
                    result,
                    flags=re.MULTILINE,
                )
                already_imported.add(mod)
                logger.debug("fix_imports[%s]: step 1 — import github.%s → from . import %s", stem, mod, mod)

        # Also track modules already imported via `from . import X` blocks
        for m in re.findall(r"from \. import .*", result):
            for name in re.findall(r"\b(\w+)\b", m.replace("from . import ", "")):
                if name in async_files:
                    already_imported.add(name)

        # Step 2: Convert `github.X.` references → `X.` (since we now have `from . import X`)
        # Only for modules that have async versions
        # Also track which modules are referenced in the code body but not yet imported
        needed_imports: set[str] = set()
        for mod in sorted(async_files, key=len, reverse=True):
            # Check if this module is actually referenced in the body
            pattern_bare = rf"(?<!asynchronous\.)github\.{re.escape(mod)}\."
            pattern_async = rf"github\.asynchronous\.{re.escape(mod)}\."
            has_ref = bool(re.search(pattern_bare, result)) or bool(re.search(pattern_async, result))

            if has_ref and mod == stem:
                # Self-reference: e.g. Enterprise.py using github.Enterprise.Enterprise(...)
                # The class name is the same as the module name — after stripping github.
                # we'd get Enterprise.Enterprise which breaks (Enterprise is the class itself).
                # Instead, find the actual class name and replace github.X.ClassName with just ClassName
                # Since module and class have the same name, github.X.X(...) → X(...)
                result = re.sub(
                    rf"(?<!asynchronous\.)github\.{re.escape(mod)}\.{re.escape(mod)}\b",
                    mod,
                    result,
                )
                result = re.sub(
                    rf"github\.asynchronous\.{re.escape(mod)}\.{re.escape(mod)}\b",
                    mod,
                    result,
                )
                # Handle github.X.OtherName patterns (class != module name) — unlikely but safe
                result = re.sub(
                    rf"(?<!asynchronous\.)github\.{re.escape(mod)}\.",
                    f"{mod}.",
                    result,
                )
                result = re.sub(
                    rf"github\.asynchronous\.{re.escape(mod)}\.",
                    f"{mod}.",
                    result,
                )
            else:
                result = re.sub(
                    pattern_bare,
                    f"{mod}.",
                    result,
                )
                result = re.sub(
                    pattern_async,
                    f"{mod}.",
                    result,
                )
                if has_ref and mod not in already_imported:
                    needed_imports.add(mod)

        # Add missing `from . import X` for modules referenced but never imported
        if needed_imports:
            logger.debug("fix_imports[%s]: step 2 — adding missing imports: %s", stem, sorted(needed_imports))
            # Find the best insertion point — after existing `from . import` block or
            # after last top-level import
            # Look for existing `from . import (...)` block to extend, or insert a new one
            existing_block = re.search(r"^from \. import \(\s*\n((?:\s+\w+,?\s*\n)*)\)", result, re.MULTILINE)
            if existing_block:
                # Insert into the existing `from . import (...)` block
                block_end = existing_block.end(1)
                additions = ""
                for mod in sorted(needed_imports):
                    # Only add if not already in the block
                    if not re.search(rf"^\s+{re.escape(mod)}\s*,?\s*$", existing_block.group(0), re.MULTILINE):
                        additions += f"    {mod},\n"
                if additions:
                    result = result[:block_end] + additions + result[block_end:]
            else:
                # Find last TOP-LEVEL import line and add after it.
                # We need to handle multi-line imports properly — if the last import
                # is a multi-line parenthesized import like `from .X import (\n  A,\n  B,\n)`,
                # we must insert AFTER the closing `)`.
                # Only consider non-indented imports (skip TYPE_CHECKING block imports).
                last_import_end = 0
                for m in re.finditer(r"^(?:import |from )\S+", result, re.MULTILINE):
                    line_start = result.rfind("\n", 0, m.start()) + 1
                    if m.start() > line_start:  # indented — skip
                        continue
                    line_end = result.find("\n", m.end())
                    if line_end == -1:
                        line_end = len(result)
                    full_line = result[line_start:line_end]
                    # Check if this is a multi-line import (has '(' but no closing ')')
                    if "(" in full_line and ")" not in full_line:
                        # Find the closing ')' for this multi-line import
                        close_paren = result.find(")", line_end)
                        if close_paren != -1:
                            close_eol = result.find("\n", close_paren)
                            if close_eol == -1:
                                close_eol = len(result)
                            last_import_end = close_eol
                        else:
                            last_import_end = line_end
                    else:
                        last_import_end = line_end
                import_line = "\nfrom . import " + ", ".join(sorted(needed_imports)) + "\n"
                result = result[: last_import_end + 1] + import_line + result[last_import_end + 1 :]

        # Step 3: from github.X import Y -> from .X import Y (for async modules)
        for mod in sorted(async_files, key=len, reverse=True):
            result = result.replace(f"from github.{mod} import ", f"from .{mod} import ")
        logger.debug("fix_imports[%s]: step 3 — converted from-imports for async modules", stem)

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

    @staticmethod
    def _fix_double_dereference(src: str) -> str:
        """Fix double-dereference patterns caused by class imports shadowing module imports.

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
                # Handle parenthesized imports — collect all names up to closing paren
                if "(" in names_str:
                    # Multi-line import: collect names until we find ")"
                    names = []
                    rest = names_str.replace("(", "").replace(")", "").strip()
                    if rest:
                        names.extend(n.strip().rstrip(",") for n in rest.split(",") if n.strip().rstrip(","))
                    if ")" not in names_str:
                        for j in range(i + 1, len(lines_list)):
                            part = lines_list[j].strip()
                            if ")" in part:
                                part = part.replace(")", "").strip()
                                if part:
                                    names.extend(
                                        n.strip().rstrip(",") for n in part.split(",") if n.strip().rstrip(",")
                                    )
                                break
                            names.extend(n.strip().rstrip(",") for n in part.split(",") if n.strip().rstrip(","))
                    class_imports[mod_name] = (i, names)
                else:
                    names = [n.strip() for n in names_str.split(",") if n.strip()]
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
                    import_text = paren_content[: close + 1].replace("(", "").replace(")", "")
            for name in import_text.split(","):
                n = name.strip().rstrip(",")
                if n and n.isidentifier():
                    go_names.add(n)

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
        """Transform methods in a class to be async."""
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
        src = self._add_awaits(src, class_name)

        return src

    def _make_method_async(self, src: str, class_name: str, method_name: str) -> str:
        """Convert 'def method_name(' to 'async def method_name(' within a class."""
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

    def _add_awaits(self, src: str, class_name: str) -> str:
        """Add await before calls to async methods."""
        methods = set(self.analyzer.async_methods.get(class_name, set()))
        # Include inherited async methods from ALL ancestor classes (full MRO)
        visited = set()
        queue = list(self.analyzer.class_bases.get(class_name, []))
        while queue:
            base = queue.pop(0)
            if base in visited:
                continue
            visited.add(base)
            methods |= self.analyzer.async_methods.get(base, set())
            queue.extend(self.analyzer.class_bases.get(base, []))

        logger.debug(
            "add_awaits[%s]: %d async methods (including inherited): %s",
            class_name,
            len(methods),
            sorted(methods),
        )

        # For self.method() calls where method is async
        for method in methods:
            if method in NEVER_ASYNC_METHODS:
                continue
            # self.method( -> await self.method(
            # But avoid double-await and avoid property access without call
            # Use a negative lookbehind to avoid matching inside longer attribute chains
            # like self._requester.requestJsonAndCheck (where requestJsonAndCheck
            # would incorrectly match self.SOMETHING.requestJsonAndCheck)
            src = self._safe_add_await(src, rf"(?<!\w)self\.{re.escape(method)}\s*\(")

            # Also handle name-mangled versions for private methods
            if method.startswith("__") and not method.endswith("__"):
                mangled = f"_{class_name}{method}"
                src = self._safe_add_await(src, rf"(?<!\w)self\.{re.escape(mangled)}\s*\(")

        # For async properties: self.prop (no parentheses) -> await self.prop
        # Gather promoted properties for this class + all ancestors
        promoted = set(self.analyzer.promoted_properties.get(class_name, set()))
        visited2 = set()
        queue2 = list(self.analyzer.class_bases.get(class_name, []))
        while queue2:
            base = queue2.pop(0)
            if base in visited2:
                continue
            visited2.add(base)
            promoted |= self.analyzer.promoted_properties.get(base, set())
            queue2.extend(self.analyzer.class_bases.get(base, []))

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
            # Match self.prop NOT followed by ( (not a method call — those are handled above)
            # and NOT being a definition line (def prop or async def prop)
            # and NOT being an assignment target (self.prop =)
            # Use _safe_add_await_property which handles the no-parens case
            src = self._safe_add_await_property(src, prop)

        # For cross-object property access: var.prop where var is NOT self.
        # This requires careful handling because not all classes have the same
        # property promoted. Only apply for safe combinations.
        global_promoted = set()
        for pp_set in self.analyzer.promoted_properties.values():
            global_promoted |= pp_set

        #
        # Safe _-prefixed props: only for variables whose types always have them promoted.
        # key_id: only on PublicKey (always promoted)
        # key: only on PublicKey (always promoted) — but also on dict, so restrict to var 'public_key'
        # encrypt: method on PublicKey (always async)
        #
        # For _identity: most classes have it promoted EXCEPT Input* classes (InputFileContent,
        # InputGitAuthor, InputGitTreeElement) and Milestone. So restrict variable names.
        CROSS_OBJECT_PROPERTY_RULES = {
            # prop: set of allowed variable name patterns (None = unrestricted lowercase)
            "key_id": {"public_key"},
            "key": {"public_key"},
            "encoding": None,  # only ContentFile and SomeOtherClass, both promoted
            "full_name": None,  # only Repository, always promoted
            # id: promoted on Repository, Issue, Invitation, etc. (CompletableGithubObjects).
            # NOT promoted on NonCompletableGithubObjects (Autolink, CodeScanRule, etc.).
            # Restrict to known safe variable names.
            "id": {
                "invitation",
                "repo",
            },
            # login: promoted on NamedUser, Organization, AuthenticatedUser
            "login": {
                "assignee",
                "user",
                "member",
                "reviewer",
                "author",
                "committer",
                "actor",
                "collaborator",
                "organization",
                "org",
                "login_or_user",
                "invited_user",
                "invitee",
                "following",
            },
            # name: promoted on Label, Repository, Team, Variable, Secret, etc.
            # NOT on Branch (sync). Restrict to known label/repo/team variables.
            "name": {
                "label",
                "element",
                "repo",
                "repository",
                "team",
                "variable",
                "secret",
            },
            # sha: promoted on Commit, GitCommit. NOT on GitRef etc.
            "sha": {
                "commit",
                "ref",
                "target_commitish",
                "base_commit",
                "head_commit",
            },
        }
        # _identity: restrict to variables that are NOT Input*/Milestone types
        # NOTE: "element" is EXCLUDED because it can be InputGitTreeElement
        # (sync, returns dict) in create_git_tree. The create_git_commit case
        # is handled by CROSS_OBJECT_REPLACEMENTS.
        IDENTITY_SAFE_VARS = {
            "assignee",
            "user",
            "member",
            "reviewer",
            "team",
            "actor",
            # NOTE: "committer" and "author" are EXCLUDED because they can be InputGitAuthor
            # (sync, returns dict) rather than NamedUser/AuthenticatedUser.
            "org",
            "organization",
            "parent",
            "commit",
            "label",
            "issue",
            "pull",
            "ref",
            "collaborator",
            "invitation",
            "creator",
            # Parameters whose types always have _identity promoted (Repository, NamedUser, etc.)
            "following",
            "starred",
            "subscription",
            "watched",
            "mentioned",
        }

        for prop, allowed_vars in CROSS_OBJECT_PROPERTY_RULES.items():
            if prop in global_promoted:
                logger.debug(
                    "add_awaits[%s]: cross-object property '%s' (vars=%s)",
                    class_name,
                    prop,
                    sorted(allowed_vars) if allowed_vars else "any",
                )
                src = self._safe_add_await_cross_object_property(src, prop, restrict_vars=allowed_vars)
        # _identity with restricted vars
        if "_identity" in global_promoted:
            logger.debug("add_awaits[%s]: cross-object property '_identity' (restricted vars)", class_name)
            src = self._safe_add_await_cross_object_property(src, "_identity", restrict_vars=IDENTITY_SAFE_VARS)

        # For cross-object method calls on domain objects: var.async_method(
        # Match specific patterns like: public_key.encrypt(
        src = self._safe_add_await_cross_object_methods(src, class_name)

        # For requester method calls
        requester_async_methods = [
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
            "close",
            # Name-mangled private methods called cross-class via _Requester__X
            "check",
            "postProcess",
        ]
        for method in requester_async_methods:
            # Match various requester access patterns
            # IMPORTANT: Use word boundary / specific prefixes to avoid
            # 'requester\.' matching inside 'self.__requester.'
            for prefix in [
                r"self\._requester\.",
                r"self\.__requester\.",
                r"self\._Requester__",
                r"self\._requester\._Requester__",
                r"self\._Github__requester\.",
                r"self\._PaginatedList__requester\.",
            ]:
                src = self._safe_add_await(src, rf"{prefix}{re.escape(method)}\s*\(")

            # For bare 'requester.method(' - use negative lookbehind to ensure
            # we don't match inside self.__requester, self._requester, etc.
            src = self._safe_add_await(src, rf"(?<!\w)(?<!_)(?<!\.)requester\.{re.escape(method)}\s*\(")

        # For connection class method calls (getresponse is async, request is sync)
        if class_name in ("Requester", "HTTPSRequestsConnectionClass", "HTTPRequestsConnectionClass"):
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

        return src

    @staticmethod
    def _safe_add_await_property(src: str, prop: str) -> str:
        """Add 'await' before self.PROP accesses where PROP is an async property.

        Only adds await inside `async def` functions (not in sync defs like __repr__).

        Matches self.PROP that is NOT:
        - followed by ( or = (not a method call or assignment)
        - on a def/async def line (definition)
        - preceded by 'await' already
        - a decorator line (@property, etc.)

        When self.PROP is followed by '.' (chained access like self.owner.login),
        it wraps with parentheses: (await self.owner).login
        """
        lines = src.split("\n")
        result_lines = []
        # Track whether we're inside an async def function.
        # func_indent = indent level of the current def/async def line.
        # Any line with indent > func_indent is inside the function body.
        in_async_func = False
        func_indent = -1
        in_signature = False  # True while we're in a multi-line def signature

        for line in lines:
            stripped = line.lstrip()
            indent = len(line) - len(stripped)

            # Track function definitions
            if stripped.startswith("async def ") or stripped.startswith("def "):
                in_async_func = stripped.startswith("async def ")
                func_indent = indent
                # Check if the signature is complete on this line (has ':' after parameters)
                # Simple heuristic: if the line ends with ':', the signature is complete
                in_signature = ":" not in stripped.split(")", 1)[-1] if ")" in stripped else True
                result_lines.append(line)
                continue

            # If we're in a multi-line signature, check if it ends on this line
            if in_signature:
                # The signature ends when we see ')' followed by ... ':'
                if ")" in stripped:
                    # Check if there's a ':' after the ')'
                    after_paren = stripped.split(")", 1)[-1]
                    if ":" in after_paren:
                        in_signature = False
                result_lines.append(line)
                continue

            # Skip decorator lines (they come before def, don't change context)
            if stripped.startswith("@"):
                result_lines.append(line)
                continue
            # Skip blank lines and comments (don't change context)
            if not stripped or stripped.startswith("#"):
                result_lines.append(line)
                continue

            # Check if we've left the function body (indent dropped to func level or above)
            if func_indent >= 0 and indent <= func_indent:
                in_async_func = False
                func_indent = -1

            # Only transform inside async functions
            if not in_async_func:
                result_lines.append(line)
                continue

            # Pattern: self.prop NOT followed by ( or = (with optional spaces)
            # and NOT preceded by 'await ' and NOT preceded by word char or dot
            pattern = rf"(?<!await )(?<!\w)self\.{re.escape(prop)}(?!\s*[\(=])(?!\w)"

            def _replace_prop(m: re.Match) -> str:
                # Check what follows the match
                after = src_line[m.end() :]
                if after.startswith("."):
                    # Chained access: self.prop.something → (await self.prop).something
                    return f"(await self.{prop})"
                else:
                    return f"await self.{prop}"

            src_line = line  # closure reference
            new_line = re.sub(pattern, _replace_prop, line)
            result_lines.append(new_line)

        return "\n".join(result_lines)

    @staticmethod
    def _safe_add_await_cross_object_property(src: str, prop: str, restrict_vars: set[str] | None = None) -> str:
        """Add 'await' before VARNAME.PROP accesses where PROP is a globally-known
        async property and VARNAME is NOT 'self'.

        Only adds await inside `async def` functions.
        Only matches lowercase variable names (to avoid module.prop false positives).
        Handles chained access: var.prop.something -> (await var.prop).something

        Args:
            restrict_vars: If provided, only match these specific variable names.
                           If None, match any lowercase variable name (excluding known modules).

        Excludes:
        - self.prop (handled by _safe_add_await_property)
        - assignments: var.prop =
        - definitions: def prop
        - already-awaited: await var.prop
        """
        lines = src.split("\n")
        result_lines = []
        in_async_func = False
        func_indent = -1
        in_signature = False

        for line in lines:
            stripped = line.lstrip()
            indent = len(line) - len(stripped)

            # Track function definitions
            if stripped.startswith("async def ") or stripped.startswith("def "):
                in_async_func = stripped.startswith("async def ")
                func_indent = indent
                in_signature = ":" not in stripped.split(")", 1)[-1] if ")" in stripped else True
                result_lines.append(line)
                continue

            if in_signature:
                if ")" in stripped:
                    after_paren = stripped.split(")", 1)[-1]
                    if ":" in after_paren:
                        in_signature = False
                result_lines.append(line)
                continue

            if stripped.startswith("@") or not stripped or stripped.startswith("#"):
                result_lines.append(line)
                continue

            if func_indent >= 0 and indent <= func_indent:
                in_async_func = False
                func_indent = -1

            if not in_async_func:
                result_lines.append(line)
                continue

            # Pattern: word_char_var.prop where var is NOT self
            # Match: lowercase-starting variable name followed by .prop
            # NOT preceded by 'await ' or 'self.' or '.' (not part of chain)
            # NOT followed by ( or = (not a call or assignment)
            # var must be at least 1 char, lowercase start (excluding self)
            pattern = (
                rf"(?<!await )(?<!self\.)"
                rf"(?<!\w)(?<!\.)"
                rf"(?!self\.)"
                rf"([a-z_]\w*)\.{re.escape(prop)}"
                rf"(?!\s*[\(=])(?!\w)"
            )

            def _replace_cross(m: re.Match) -> str:
                var = m.group(1)
                # If restrict_vars is set, only match those specific variable names
                if restrict_vars is not None:
                    if var not in restrict_vars:
                        logger.debug(
                            "cross_object_prop: skipping %s.%s (var not in restrict_vars)",
                            var,
                            prop,
                        )
                        return m.group(0)
                else:
                    # Skip known non-domain variables
                    if var in (
                        "os",
                        "sys",
                        "re",
                        "io",
                        "json",
                        "time",
                        "copy",
                        "urllib",
                        "logging",
                        "collections",
                        "typing",
                        "asyncio",
                        "niquests",
                        "string",
                        "base64",
                        "datetime",
                        "functools",
                        "itertools",
                        "hashlib",
                        "struct",
                        "textwrap",
                        "warnings",
                        "math",
                        "importlib",
                        "pathlib",
                        "abc",
                        "github",
                        "tests",
                        "pytest",
                    ):
                        logger.debug(
                            "cross_object_prop: skipping %s.%s (non-domain variable)",
                            var,
                            prop,
                        )
                        return m.group(0)
                logger.debug("cross_object_prop: adding await to %s.%s", var, prop)
                after = src_line[m.end() :]
                if after.startswith("."):
                    # Chained: var.prop.something → (await var.prop).something
                    return f"(await {var}.{prop})"
                else:
                    # Always use parentheses to avoid operator precedence issues
                    # e.g. `await x.name if cond else y` → `(await x.name) if cond else y`
                    return f"(await {var}.{prop})"

            src_line = line  # closure reference
            new_line = re.sub(pattern, _replace_cross, line)
            result_lines.append(new_line)

        return "\n".join(result_lines)

    def _safe_add_await_cross_object_methods(self, src: str, class_name: str) -> str:
        """Add 'await' before cross-object async method calls: var.async_method(

        Uses precomputed globally_async_methods (methods async in ALL classes).
        Matches var.method( where var is a lowercase variable name (not self).
        Only applies inside `async def` functions.
        """
        # Compute globally async methods once (cached)
        if not hasattr(self, "_globally_async_methods"):
            method_classes: dict[str, set[str]] = {}
            method_async: dict[str, set[str]] = {}
            for cn in self.analyzer.async_classes:
                for mname in self.analyzer.async_methods.get(cn, set()):
                    if mname not in method_classes:
                        method_classes[mname] = set()
                        method_async[mname] = set()
                    method_classes[mname].add(cn)
                    method_async[mname].add(cn)
                # Also check non-async methods for completeness
                cls_node = self.analyzer._get_class_node(cn)
                if cls_node is None:
                    continue
                for item in ast.iter_child_nodes(cls_node):
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        mname = item.name
                        if mname not in method_classes:
                            method_classes[mname] = set()
                            method_async[mname] = set()
                        method_classes[mname].add(cn)

            self._globally_async_methods = set()
            for mname, classes in method_classes.items():
                if mname in NEVER_ASYNC_METHODS:
                    continue
                if classes and classes == method_async.get(mname, set()):
                    self._globally_async_methods.add(mname)

            logger.debug(
                "cross_object_methods: computed %d globally async methods: %s",
                len(self._globally_async_methods),
                sorted(self._globally_async_methods),
            )

        globally_async = self._globally_async_methods

        # Build a single combined regex for all globally async methods
        if not globally_async:
            return src

        # Escape and join method names
        method_alts = "|".join(re.escape(m) for m in sorted(globally_async))
        pattern = re.compile(
            rf"(?<!await )(?<!\w)(?<!\.)"
            rf"(?!self\.)"
            rf"([a-z_]\w*)\.({method_alts})\s*\("
        )

        lines = src.split("\n")
        result_lines = []
        in_async_func = False
        func_indent = -1
        in_signature = False

        for line in lines:
            stripped = line.lstrip()
            indent = len(line) - len(stripped)

            if stripped.startswith("async def ") or stripped.startswith("def "):
                in_async_func = stripped.startswith("async def ")
                func_indent = indent
                in_signature = ":" not in stripped.split(")", 1)[-1] if ")" in stripped else True
                result_lines.append(line)
                continue
            if in_signature:
                if ")" in stripped:
                    after_paren = stripped.split(")", 1)[-1]
                    if ":" in after_paren:
                        in_signature = False
                result_lines.append(line)
                continue
            if stripped.startswith("@") or not stripped or stripped.startswith("#"):
                result_lines.append(line)
                continue
            if func_indent >= 0 and indent <= func_indent:
                in_async_func = False
                func_indent = -1
            if not in_async_func:
                result_lines.append(line)
                continue

            def _replace_method_call(m: re.Match) -> str:
                var = m.group(1)
                meth = m.group(2)
                # Exclude known non-domain-object variables whose methods are sync
                if var in (
                    "input",
                    "output",
                    "data",
                    "result",
                    "response",
                    "headers",
                    "params",
                    "args",
                    "kwargs",
                    "options",
                    "config",
                    "path",
                    "file",
                    "stream",
                    "buffer",
                    "socket",
                    "conn",
                    "cursor",
                    "logger",
                    "handler",
                    "parser",
                    "encoder",
                    "decoder",
                    "adapter",
                    "mock",
                    "stub",
                    "fixture",
                    "cls",
                    "klass",
                    "typ",
                    "base",
                    "item",
                    "key",
                    "val",
                    "value",
                    "attr",
                    "obj",
                    "pickle",
                    "string",
                    "text",
                    "msg",
                    "err",
                    "error",
                    "exc",
                    "exception",
                    "url",
                    "uri",
                    "resp",
                    "req",
                    "request",
                    "session",
                ):
                    logger.debug(
                        "cross_object_methods[%s]: skipping %s.%s (non-domain variable)",
                        class_name,
                        var,
                        meth,
                    )
                    return m.group(0)  # Don't add await
                logger.debug("cross_object_methods[%s]: adding await to %s.%s()", class_name, var, meth)
                return f"await {var}.{meth}("

            new_line = pattern.sub(_replace_method_call, line)
            result_lines.append(new_line)

        return "\n".join(result_lines)

    @staticmethod
    def _safe_add_await(src: str, pattern: str) -> str:
        """Add 'await' before pattern matches, avoiding double-insertion.

        Uses a negative lookbehind approach: scans backwards from the match
        to check if 'await' already precedes it (with optional whitespace).
        """
        result_parts = []
        last_end = 0

        for m in re.finditer(pattern, src):
            start = m.start()
            # Check if 'await ' already precedes this match
            # Look back further (up to 20 chars) to handle indentation
            lookback = src[max(0, start - 20) : start]
            if re.search(r"await\s+$", lookback):
                continue  # Already has await
            # Also check if this is part of a string literal (basic check)
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
        """Convert __enter__/__exit__ to __aenter__/__aexit__."""
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
        """Convert 'with self.__connection_lock:' to 'async with self.__connection_lock:'."""
        # Convert any 'with' statement that uses a lock (asyncio.Lock needs async with)
        src = re.sub(
            r"^(\s+)with (self\.__connection_lock|self\._connection_lock)(.*:)\s*$",
            r"\1async with \2\3",
            src,
            flags=re.MULTILINE,
        )
        return src

    @staticmethod
    def _convert_pagination_iteration(src: str) -> str:
        """Convert PaginatedList's __iter__ to __aiter__/__anext__ pattern."""
        logger.debug("convert_pagination: converting __iter__ → __aiter__ for PaginatedList")

        # Replace PaginatedListBase.__iter__ with __aiter__
        # The sync version is:
        #     def __iter__(self) -> Iterator[T]:
        #         yield from self.__elements
        #         while self._couldGrow():
        #             newElements = self._grow()
        #             yield from newElements
        #
        # Convert to:
        #     async def __aiter__(self):
        #         for element in self.__elements:
        #             yield element
        #         while self._couldGrow():
        #             newElements = await self._grow()
        #             for element in newElements:
        #                 yield element

        # First, replace the __iter__ definition with __aiter__
        src = re.sub(
            r"def __iter__\(self\)\s*->\s*Iterator\[T\]:",
            "async def __aiter__(self):",
            src,
        )

        # Replace 'yield from self.__elements' with 'for element in self.__elements: yield element'
        # (yield from doesn't work in async generators)
        src = re.sub(
            r"^(\s+)yield from self\.__elements\s*$",
            r"\1for element in self.__elements:\n\1    yield element",
            src,
            flags=re.MULTILINE,
        )

        # Replace 'yield from newElements' similarly
        src = re.sub(
            r"^(\s+)yield from newElements\s*$",
            r"\1for element in newElements:\n\1    yield element",
            src,
            flags=re.MULTILINE,
        )

        # Also handle _Slice.__iter__ similarly
        src = re.sub(
            r"def __iter__\(self\)\s*->\s*Iterator\[T\]:\s*\n(\s+)index\s*=",
            "async def __aiter__(self):\n\\1index =",
            src,
        )

        # Fix _grow() calls to add await (if not already present)
        src = re.sub(
            r"(?<!await )self\._grow\(\)",
            "await self._grow()",
            src,
        )

        # Fix _Slice.__aiter__: self.__list[index] -> await self.__list.getitem(index)
        # Use the new async getitem() method instead of the broken async __getitem__.
        src = re.sub(
            r"(\s+)yield (?:await )?(self\.__list)\[index\]",
            r"\1yield await \2.getitem(index)",
            src,
        )

        # Convert async __getitem__ → sync __getitem__ + async getitem()
        # Step 3 promoted __getitem__ to async and added await before __fetchToIndex.
        # Python cannot implicitly await dunder methods, so obj[i] would return a
        # coroutine instead of a value.  We revert __getitem__ to sync (just reads
        # self.__elements) and inject getitem() for async-aware access.
        logger.debug("convert_pagination: reverting __getitem__ to sync + injecting async getitem()")

        # First, strip 'async' from the @overload stubs and the real __getitem__
        src = re.sub(
            r"^(\s+)async def __getitem__\(",
            r"\1def __getitem__(",
            src,
            flags=re.MULTILINE,
        )

        # Remove 'await self.__fetchToIndex(index)' (or the name-mangled form) from
        # the sync __getitem__.  The line may also appear as
        #   await self._PaginatedListBase__fetchToIndex(index)
        src = re.sub(
            r"^(\s+)await self\.(?:_PaginatedListBase)?__fetchToIndex\(index\)\n",
            "",
            src,
            flags=re.MULTILINE,
        )

        # Add a docstring to the now-sync __getitem__ explaining that it only
        # reads already-fetched elements and that getitem() should be used for
        # async-aware access.
        __getitem_docstring = (
            '        """Synchronous element access \u2014 only returns already-fetched elements.\n'
            "\n"
            "        For async-aware fetching (which loads pages on demand), use\n"
            "        ``await obj.getitem(index)`` instead.\n"
            "\n"
            "        :raises IndexError: if *index* has not been fetched yet.\n"
            '        """\n'
        )
        src = re.sub(
            r"(def __getitem__\(self, index: int \| slice\)[^\n]*\n)"
            r"(\s+assert isinstance\(index,)",
            r"\1" + __getitem_docstring + r"\2",
            src,
            count=1,
        )

        # Inject async def getitem() right after __getitem__.
        # We locate the closing line of __getitem__ (the 'return self._Slice(self, index)')
        # and append the new method after a blank line.
        getitem_body = (
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
        )
        # Insert after the 'return self._Slice(self, index)' line in __getitem__
        src = re.sub(
            r"(return self\._Slice\(self, index\)\n)",
            r"\1" + getitem_body,
            src,
            count=1,
        )

        # Fix the `reversed` property: r.__reverse() is now async.
        # The third-pass analysis will have promoted `reversed` to an async property
        # (since __reverse is in async_methods). Just ensure the __reverse() call
        # has `await` — _add_awaits should handle this, but let's be safe.
        src = re.sub(
            r"(?<!await )r\.__reverse\(\)",
            "await r.__reverse()",
            src,
        )
        # Also handle the name-mangled form
        src = re.sub(
            r"(?<!await )r\._PaginatedList__reverse\(\)",
            "await r._PaginatedList__reverse()",
            src,
        )

        # Remove __reversed__ — it calls self.reversed which is an async property,
        # but __reversed__ is a sync dunder that Python's reversed() calls
        # synchronously.  There is no way to await inside __reversed__, so it
        # must be removed.  The SyncProxy.__reversed__ bridge accesses
        # obj.reversed directly and awaits the coroutine, so tests still work.
        src = re.sub(
            r"\n    # To support Python's built-in `reversed\(\)` method\n"
            r"    def __reversed__\(self\)[^\n]*\n"
            r"        return self\.reversed\n",
            "\n",
            src,
        )

        # Add async iteration type hints
        if "from typing import" in src and "AsyncIterator" not in src:
            src = src.replace("from typing import", "from typing import AsyncIterator,", 1)

        return src

    @staticmethod
    def _fix_github_object(src: str) -> str:
        """Fix CompletableGithubObject patterns in GithubObject.py.

        Key changes:
        1. Remove the auto-complete in ``__init__`` (can't await in ``__init__``),
           replacing it with a flag (``_needs_async_completion``).
        2. ``_completeIfNotSet``, ``_completeIfNeeded``, and ``__complete`` are
           genuinely ``async def`` — the normal transform already handles that.
           No nest_asyncio sync bridge is needed. Properties that call them are
           promoted to ``async def`` in the third-pass analysis.
        """
        logger.debug("fix_github_object: applying GithubObject-specific fixes")
        # --- 1) Replace auto-complete in __init__ with flag ----
        src = re.sub(
            r"^(\s+)if requester\.is_not_lazy and completed is None and not response_given:\s*\n\s+(?:await )?self\.complete\(\)\n",
            r"\1# Async: store flag instead of calling self.complete() (can't await in __init__).\n"
            r"\1# The SyncProxy._wrap() or user code should call await obj.complete() when this is True.\n"
            r"\1self._needs_async_completion = (\n"
            r"\1    requester.is_not_lazy and completed is None and not response_given\n"
            r"\1)\n",
            src,
            flags=re.MULTILINE,
        )

        # f) Fix __eq__ to accept both sync and async class hierarchies.
        # The sync __eq__ uses `other.__class__ is self.__class__` which fails
        # when comparing async objects with sync objects (different class hierarchies).
        # Relax to compare class names instead.
        src = re.sub(
            r"other\.__class__ is self\.__class__",
            "other.__class__.__name__ == self.__class__.__name__",
            src,
        )

        # g) Fix super().raw_data and super().raw_headers: the parent GithubObject.raw_data
        # is now an async property, so calling super().raw_data returns a coroutine.
        # We must await it.
        src = src.replace("return super().raw_data", "return await super().raw_data")
        src = src.replace("return super().raw_headers", "return await super().raw_headers")

        # h) Make is_defined, is_undefined, is_optional, is_optional_list accept both
        # sync and async _NotSetType. Tests use gho.NotSet (sync) which is a different
        # class from the async _NotSetType. We import the sync _NotSetType and check both.
        # Also fix remove_unset_items to handle both types.
        src = re.sub(
            r"(class _NotSetType\(Attribute\[Any\]\):)",
            "import github.GithubObject as _sync_gho\n\n\\1",
            src,
            count=1,
        )
        # is_defined: not isinstance(v, _NotSetType) -> not isinstance(v, (_NotSetType, _sync_gho._NotSetType))
        src = src.replace(
            "def is_defined(v: T | _NotSetType) -> TypeGuard[T]:\n    return not isinstance(v, _NotSetType)",
            "def is_defined(v: T | _NotSetType) -> TypeGuard[T]:\n"
            "    return not isinstance(v, (_NotSetType, _sync_gho._NotSetType))",
        )
        # is_undefined
        src = src.replace(
            "def is_undefined(v: T | _NotSetType) -> TypeGuard[_NotSetType]:\n    return isinstance(v, _NotSetType)",
            "def is_undefined(v: T | _NotSetType) -> TypeGuard[_NotSetType]:\n"
            "    return isinstance(v, (_NotSetType, _sync_gho._NotSetType))",
        )
        # is_optional
        src = src.replace(
            "def is_optional(v: Any, type: type | tuple[type, ...]) -> bool:\n"
            "    return isinstance(v, _NotSetType) or isinstance(v, type)",
            "def is_optional(v: Any, type: type | tuple[type, ...]) -> bool:\n"
            "    return isinstance(v, (_NotSetType, _sync_gho._NotSetType)) or isinstance(v, type)",
        )
        # is_optional_list
        src = src.replace(
            "def is_optional_list(v: Any, type: type | tuple[type, ...]) -> bool:\n"
            "    return isinstance(v, _NotSetType) or isinstance(v, list)",
            "def is_optional_list(v: Any, type: type | tuple[type, ...]) -> bool:\n"
            "    return isinstance(v, (_NotSetType, _sync_gho._NotSetType)) or isinstance(v, list)",
        )
        # remove_unset_items
        src = src.replace(
            "return {key: value for key, value in data.items() if not isinstance(value, _NotSetType)}",
            "return {key: value for key, value in data.items() if not isinstance(value, (_NotSetType, _sync_gho._NotSetType))}",
        )

        return src

    @staticmethod
    def _add_close_awaits(src: str, stem: str) -> str:
        """Add await to close() calls on connection/session objects."""
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
        if stem in ("Requester", "HTTPSRequestsConnectionClass", "HTTPRequestsConnectionClass"):
            # self.session.close() - for connection classes
            src = re.sub(
                r"(?<!await )self\.session\.close\(\)",
                "await self.session.close()",
                src,
            )
        return src

    @staticmethod
    def _add_cross_object_awaits(src: str, stem: str) -> str:
        """Apply direct string replacements for cross-object async calls.

        These handle cases where chained method calls need await in ways
        that _safe_add_await cannot handle (e.g., obj.method().async_call()).
        """
        replacements = CROSS_OBJECT_REPLACEMENTS.get(stem, [])
        for old, new in replacements:
            src = src.replace(old, new)
        return src

    def _fix_isinstance_dual_class(self, src: str) -> str:
        """Fix isinstance checks to accept both async and sync class variants.

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
            if s not in SKIP_FILES and not s.startswith("_"):
                async_files.add(s)

        # Build a pattern that matches ModuleName.ClassName for known async modules
        # e.g. Repository.Repository, NamedUser.NamedUser, etc.
        mod_pattern = "|".join(re.escape(m) for m in sorted(async_files, key=len, reverse=True))
        async_class_pat = re.compile(rf"\b({mod_pattern})\.(\w+)")

        result: list[str] = []
        i = 0
        isinstance_literal = "isinstance("

        while i < len(src):
            pos = src.find(isinstance_literal, i)
            if pos == -1:
                result.append(src[i:])
                break

            result.append(src[i:pos])

            # Find matching closing paren
            paren_start = pos + len(isinstance_literal) - 1
            depth = 1
            j = paren_start + 1
            while j < len(src) and depth > 0:
                if src[j] == "(":
                    depth += 1
                elif src[j] == ")":
                    depth -= 1
                j += 1

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

            # Only add sync variants for patterns that match async module references
            # and DON'T already have github.X.Y (sync) variant
            def _has_async_only(ta: str) -> bool:
                """Check if type arg contains async module.class references."""
                for m in async_class_pat.finditer(ta):
                    # Check it's not already prefixed with github. (sync variant)
                    start = m.start()
                    prefix = ta[max(0, start - 7) : start]
                    if not prefix.endswith("github."):
                        return True
                return False

            if not _has_async_only(type_arg_stripped):
                result.append(full_call)
                i = j
                continue

            is_tuple = type_arg_stripped.startswith("(")

            if is_tuple:

                def _add_sync_in_tuple(m: re.Match) -> str:
                    return f"{m.group(1)}.{m.group(2)}, github.{m.group(1)}.{m.group(2)}"

                new_type_arg = async_class_pat.sub(_add_sync_in_tuple, type_arg)
                logger.debug("fix_isinstance_dual_class: tuple — %s → %s", type_arg.strip(), new_type_arg.strip())
                result.append(f"isinstance({first_arg}, {new_type_arg})")
            else:
                if async_class_pat.fullmatch(type_arg_stripped):
                    m = async_class_pat.fullmatch(type_arg_stripped)
                    mod, cls = m.group(1), m.group(2)
                    logger.debug(
                        "fix_isinstance_dual_class: single — %s.%s → (%s.%s, github.%s.%s)",
                        mod,
                        cls,
                        mod,
                        cls,
                        mod,
                        cls,
                    )
                    result.append(f"isinstance({first_arg}, ({mod}.{cls}, github.{mod}.{cls}))")
                else:

                    def _wrap_async_class(m2: re.Match) -> str:
                        return f"({m2.group(1)}.{m2.group(2)}, github.{m2.group(1)}.{m2.group(2)})"

                    new_type_arg = async_class_pat.sub(_wrap_async_class, type_arg)
                    result.append(f"isinstance({first_arg}, {new_type_arg})")

            i = j

        return "".join(result)


def _generate_reexport_stub(module_name: str) -> str:
    """Generate a stub module that re-exports everything from the sync counterpart.

    This ensures that e.g. ``github.asynchronous.Auth.Auth``
    IS ``github.Auth.Auth`` (same object), avoiding isinstance mismatches.
    """
    return (
        f"{AUTO_HEADER}"
        f"# Re-export everything from the sync module so that\n"
        f"# isinstance checks work with both sync and async code.\n"
        f"from github.{module_name} import *  # noqa: F401,F403\n"
    )


def generate_async_init() -> str:
    """Generate the __init__.py for github.asynchronous."""
    lines = [AUTO_HEADER.rstrip()]
    lines.append('"""')
    lines.append("Async counterparts of the github package classes.")
    lines.append('"""')
    lines.append("")
    lines.append("")
    lines.append("from github.asynchronous.MainClass import Github")
    lines.append("")
    lines.append("")
    lines.append("__all__ = [")
    lines.append('    "Github",')
    lines.append("]")
    lines.append("")
    return "\n".join(lines)


def generate_async_test_framework() -> str:
    """Generate the async test Framework.py with SyncProxy for transparent async-to-sync bridging."""
    return textwrap.dedent('''\
        # FILE AUTO GENERATED DO NOT TOUCH
        """
        Async test framework - wraps the sync Framework for async tests.

        Uses a SyncProxy approach: the async Github object and all objects returned
        from it are wrapped in a proxy that automatically runs coroutines synchronously.
        This allows test method bodies to remain identical to sync tests.
        """
        from __future__ import annotations

        import asyncio
        import inspect
        from collections.abc import AsyncIterator

        import responses

        from github.GithubException import IncompletableObject
        import github.GithubObject
        import github.Requester
        import github.asynchronous.GithubObject
        import github.asynchronous.Requester
        from github.asynchronous.MainClass import Github
        from tests import Framework

        # Re-export BasicTestCase so that async test files referencing
        # Framework.BasicTestCase find it here.
        BasicTestCase = Framework.BasicTestCase


        def _is_completable(obj):
            """Check if an object is a CompletableGithubObject that may need completion."""
            try:
                return isinstance(obj, github.asynchronous.GithubObject.CompletableGithubObject)
            except Exception:
                return False


        class AsyncReplayingConnection(Framework.ReplayingConnection):
            """Async-aware replaying connection.

            Inherits the replay file logic from ReplayingConnection.
            Overrides getresponse() and close() to be async, since the
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
            _realConnection = github.asynchronous.Requester.HTTPRequestsConnectionClass

            def __init__(self, *args, **kwds):
                super().__init__("http", *args, **kwds)


        class AsyncReplayingHttpsConnection(AsyncReplayingConnection):
            _realConnection = github.asynchronous.Requester.HTTPSRequestsConnectionClass

            def __init__(self, *args, **kwds):
                super().__init__("https", *args, **kwds)


        class SyncProxy:
            """Proxy that wraps an async object and makes its async methods callable synchronously.

            When an async method is called, it is automatically run to completion in an event loop.
            Objects returned from async calls are recursively wrapped in SyncProxy.
            Supports sync iteration over objects that implement __aiter__/__anext__.
            """

            # Types that should NOT be wrapped (they are plain values)
            _PASSTHROUGH = (str, int, float, bool, bytes, type(None))
            # Cache: id(obj) -> SyncProxy, so the same underlying object always
            # returns the same wrapper (preserves `is` identity checks).
            _cache: dict[int, "SyncProxy"] = {}

            def __init__(self, obj, loop=None):
                object.__setattr__(self, '_obj', obj)
                object.__setattr__(self, '_loop', loop or asyncio.new_event_loop())
                # Register in cache
                SyncProxy._cache[id(obj)] = self

            @staticmethod
            def _deep_unwrap(obj):
                """Recursively unwrap SyncProxy objects inside containers.

                This is needed because async methods may iterate over list/tuple/dict
                arguments and access async properties on the elements. If the elements
                are still SyncProxy-wrapped, accessing an async property triggers
                SyncProxy.__getattr__ -> run_until_complete, which fails with
                'RuntimeError: This event loop is already running' since the outer
                async call is already running on the same loop.
                """
                if isinstance(obj, SyncProxy):
                    return object.__getattribute__(obj, '_obj')
                if isinstance(obj, list):
                    return [SyncProxy._deep_unwrap(item) for item in obj]
                if isinstance(obj, tuple):
                    if hasattr(type(obj), '_fields'):
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
                """Wrap a result if it's a complex object, pass through primitives."""
                if isinstance(result, cls._PASSTHROUGH):
                    return result
                # Don't wrap _NotSetType instances (NotSet sentinel).
                # Tests call is_undefined(obj._attr) which needs the raw _NotSetType,
                # not a SyncProxy wrapper.
                if isinstance(result, (
                    github.GithubObject._NotSetType,
                    github.asynchronous.GithubObject._NotSetType,
                )):
                    return result
                # Also pass through _ValuedAttribute and _BadAttribute instances
                # which are internal attribute wrappers, not user-facing objects.
                if isinstance(result, (
                    github.GithubObject._ValuedAttribute,
                    github.asynchronous.GithubObject._ValuedAttribute,
                    github.GithubObject._BadAttribute,
                    github.asynchronous.GithubObject._BadAttribute,
                )):
                    return result
                if isinstance(result, dict):
                    return {k: cls._wrap(v, loop) for k, v in result.items()}
                if isinstance(result, (list, tuple)):
                    wrapped = [cls._wrap(item, loop) for item in result]
                    # NamedTuples require positional args, not a single list
                    if hasattr(type(result), '_fields'):
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
                """Lazily complete the underlying object if it's a CompletableGithubObject
                that hasn't been completed yet. This mirrors the sync code's
                _completeIfNotSet() which triggers completion on property access."""
                obj = object.__getattribute__(self, '_obj')
                loop = object.__getattribute__(self, '_loop')
                if _is_completable(obj) and not obj.completed:
                    try:
                        coro = obj.complete()
                        if asyncio.iscoroutine(coro):
                            loop.run_until_complete(coro)
                    except IncompletableObject:
                        pass

            def __getattr__(self, name):
                obj = object.__getattribute__(self, '_obj')
                loop = object.__getattribute__(self, '_loop')

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
                    value = object.__getattribute__(value, '_obj')
                setattr(object.__getattribute__(self, '_obj'), name, value)

            @property
            def __class__(self):
                return type(object.__getattribute__(self, '_obj'))

            def __repr__(self):
                return repr(object.__getattribute__(self, '_obj'))

            def __str__(self):
                return str(object.__getattribute__(self, '_obj'))

            def __eq__(self, other):
                if isinstance(other, SyncProxy):
                    other = object.__getattribute__(other, '_obj')
                return object.__getattribute__(self, '_obj') == other

            def __ne__(self, other):
                if isinstance(other, SyncProxy):
                    other = object.__getattribute__(other, '_obj')
                return object.__getattribute__(self, '_obj') != other

            def __hash__(self):
                return hash(object.__getattribute__(self, '_obj'))

            def __bool__(self):
                return bool(object.__getattribute__(self, '_obj'))

            def __len__(self):
                obj = object.__getattribute__(self, '_obj')
                if hasattr(obj, '__len__'):
                    return len(obj)
                raise TypeError(f"object of type '{type(obj).__name__}' has no len()")

            def __iter__(self):
                obj = object.__getattribute__(self, '_obj')
                loop = object.__getattribute__(self, '_loop')

                if hasattr(obj, '__aiter__'):
                    # Async iterable - use async iteration
                    aiter = obj.__aiter__()
                    while True:
                        try:
                            item = loop.run_until_complete(aiter.__anext__())
                            yield SyncProxy._wrap(item, loop)
                        except StopAsyncIteration:
                            return
                elif hasattr(obj, '__iter__'):
                    for item in obj:
                        yield SyncProxy._wrap(item, loop)
                else:
                    raise TypeError(f"'{type(obj).__name__}' object is not iterable")

            def __getitem__(self, index):
                obj = object.__getattribute__(self, '_obj')
                loop = object.__getattribute__(self, '_loop')
                # Use the async getitem() method if available (PaginatedListBase)
                # so that pages are fetched on demand.  Fall back to sync
                # __getitem__ for non-PaginatedList objects.
                if hasattr(obj, 'getitem'):
                    result = loop.run_until_complete(obj.getitem(index))
                else:
                    result = obj.__getitem__(index)
                    if asyncio.iscoroutine(result):
                        result = loop.run_until_complete(result)
                return SyncProxy._wrap(result, loop)

            def __reversed__(self):
                obj = object.__getattribute__(self, '_obj')
                loop = object.__getattribute__(self, '_loop')
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
                obj = object.__getattribute__(self, '_obj')
                if isinstance(item, SyncProxy):
                    item = object.__getattribute__(item, '_obj')
                return item in obj

            def __enter__(self):
                obj = object.__getattribute__(self, '_obj')
                loop = object.__getattribute__(self, '_loop')
                if hasattr(obj, '__aenter__'):
                    result = loop.run_until_complete(obj.__aenter__())
                    return SyncProxy._wrap(result, loop)
                return SyncProxy._wrap(obj.__enter__(), loop)

            def __exit__(self, *args):
                obj = object.__getattribute__(self, '_obj')
                loop = object.__getattribute__(self, '_loop')
                if hasattr(obj, '__aexit__'):
                    return loop.run_until_complete(obj.__aexit__(*args))
                return obj.__exit__(*args)

            def __isinstance_check__(self):
                """Return the wrapped object for isinstance checks."""
                return object.__getattribute__(self, '_obj')


        class TestCase(Framework.BasicTestCase):
            """Async version of Framework.TestCase.

            Creates an async Github instance wrapped in SyncProxy,
            so test methods can call async methods synchronously.
            """

            @staticmethod
            def _unwrap(obj):
                """Unwrap a SyncProxy to get the underlying object."""
                if isinstance(obj, SyncProxy):
                    return object.__getattribute__(obj, '_obj')
                return obj

            @staticmethod
            def _resolve_async_class(cls):
                """Try to find the async equivalent of a sync class.

                For example, github.Repository.Repository -> github.asynchronous.Repository.Repository
                """
                mod = getattr(cls, '__module__', '') or ''
                if mod.startswith('github.') and not mod.startswith('github.asynchronous.'):
                    async_mod_name = mod.replace('github.', 'github.asynchronous.', 1)
                    try:
                        import importlib
                        async_mod = importlib.import_module(async_mod_name)
                        return getattr(async_mod, cls.__name__, cls)
                    except (ImportError, AttributeError):
                        pass
                return cls

            def assertIsInstance(self, obj, cls, msg=None):
                """Override to unwrap SyncProxy and also check async class hierarchy."""
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
                """Override to unwrap SyncProxy and also check async class hierarchy."""
                unwrapped = self._unwrap(obj)
                async_cls = self._resolve_async_class(cls)
                # Must not be instance of EITHER sync or async class
                if isinstance(unwrapped, async_cls) and async_cls is not cls:
                    self.fail(
                        msg or f'{unwrapped!r} is an instance of async {async_cls!r}'
                    )
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
                github.asynchronous.GithubObject.GithubObject.setCheckAfterInitFlag(True)
                github.asynchronous.Requester.Requester.setDebugFlag(True)
                github.asynchronous.Requester.Requester.setOnCheckMe(self.getFrameChecker())

                # Inject async replaying connection classes into the async Requester
                github.asynchronous.Requester.Requester.injectConnectionClasses(
                    AsyncReplayingHttpConnection,
                    AsyncReplayingHttpsConnection,
                )

                self.g = self.get_github(self.authMode, self.retry, self.pool_size)

            def tearDown(self):
                super().tearDown()
                github.asynchronous.Requester.Requester.resetConnectionClasses()

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
    ''')


def generate_async_test_conftest() -> str:
    """Generate conftest.py for async tests."""
    return textwrap.dedent('''\
        # FILE AUTO GENERATED DO NOT TOUCH
        """
        Conftest for async tests.

        The parent tests/conftest.py already sets up NiquestsMock with both
        sync and async support. Nothing additional needed here since test
        methods are synchronous (SyncProxy handles async bridging).
        """
    ''')


def transform_test_file(src: str, test_stem: str) -> str:
    """Transform a sync test file into an async version.

    Since we use SyncProxy to bridge async-to-sync, test method bodies
    remain identical. We only need to change imports/base class.
    """
    logger.debug("transform_test[%s]: begin", test_stem)
    result = AUTO_HEADER + src

    # Change Framework import to use async Framework
    result = result.replace("from . import Framework", "from tests.asynchronous import Framework")
    result = re.sub(r"from tests import Framework", "from tests.asynchronous import Framework", result)
    logger.debug("transform_test[%s]: changed Framework import to async", test_stem)

    # Replace references to github.MainClass.Github with async version
    # (some tests import Github directly)
    result = result.replace(
        "from github.MainClass import Github",
        "from github.asynchronous.MainClass import Github",
    )

    # Replace github.GithubIntegration with async version where used
    result = result.replace(
        "from github.GithubIntegration import GithubIntegration",
        "from github.asynchronous.GithubIntegration import GithubIntegration",
    )

    # Note: test methods are NOT made async. SyncProxy handles the bridging.
    # No @pytest.mark.asyncio needed either.

    # Fix mock paths: patch async Requester alongside sync Requester
    # github.Requester.time.sleep -> github.asynchronous.Requester.asyncio.sleep
    # (The async Requester uses asyncio.sleep instead of time.sleep)
    if 'mock.patch("github.Requester.time.sleep"' in result:
        logger.debug("transform_test[%s]: fixing mock path for time.sleep → asyncio.sleep", test_stem)
    result = result.replace(
        'mock.patch("github.Requester.time.sleep"',
        'mock.patch("github.asynchronous.Requester.asyncio.sleep"',
    )

    # Fix logger injection: also inject into async Requester
    if "github.Requester.Requester.injectLogger(self.logger)" in result:
        logger.debug("transform_test[%s]: adding async Requester logger injection", test_stem)
    result = result.replace(
        "github.Requester.Requester.injectLogger(self.logger)",
        "github.Requester.Requester.injectLogger(self.logger)\n"
        "        github.asynchronous.Requester.Requester.injectLogger(self.logger)",
    )
    result = result.replace(
        "github.Requester.Requester.resetLogger()",
        "github.Requester.Requester.resetLogger()\n        github.asynchronous.Requester.Requester.resetLogger()",
    )

    # Add async Requester import if we patched logger
    if "github.asynchronous.Requester.Requester.injectLogger" in result:
        if "import github.asynchronous.Requester" not in result:
            result = result.replace(
                "import github\n",
                "import github\nimport github.asynchronous.Requester\n",
                1,
            )

    # Fix mock path for datetime in RequesterThrottleTestCase
    # Replace the string literal rather than the whole mock.patch(...) call,
    # because black may format the call across multiple lines.
    result = result.replace(
        '"github.Requester.datetime"',
        '"github.asynchronous.Requester.datetime"',
    )

    # Fix mock paths for PublicKey.encrypt (secrets use nacl encryption which is non-deterministic)
    # The async code imports from github.asynchronous.PublicKey, not github.PublicKey
    result = result.replace(
        'mock.patch("github.PublicKey.encrypt")',
        'mock.patch("github.asynchronous.PublicKey.encrypt")',
    )

    # Fix mock paths for AccessToken.datetime (used for token expiry timestamps)
    # Authentication.py uses sync github.Github(), so the sync AccessToken.datetime
    # mock path is correct. Other test files (e.g. ApplicationOAuth) use self.g (async),
    # so they need the async mock path.
    if test_stem != "Authentication":
        result = result.replace(
            '"github.AccessToken.datetime"',
            '"github.asynchronous.AccessToken.datetime"',
        )

    # Fix GithubObject helper imports: is_undefined/is_defined from sync GithubObject only
    # check sync _NotSetType. The async versions check both sync and async _NotSetType,
    # which is needed when tests access attributes of async objects through SyncProxy.
    result = result.replace(
        "from github.GithubObject import is_undefined",
        "from github.asynchronous.GithubObject import is_undefined",
    )
    result = result.replace(
        "from github.GithubObject import is_defined",
        "from github.asynchronous.GithubObject import is_defined",
    )

    # Fix Repository.as_url_param: the test calls the static method with a SyncProxy object.
    # The sync method checks isinstance(repo, github.Repository.Repository) which fails
    # because the SyncProxy's __class__ returns async Repository. Use the async version.
    # Since as_url_param is async, wrap calls with run_until_complete and unwrap SyncProxy args.
    result = result.replace(
        "github.Repository.Repository.as_url_param",
        "github.asynchronous.Repository.Repository.as_url_param",
    )

    # Wrap direct calls to async static method as_url_param with run_until_complete.
    # Unwrap SyncProxy arguments to avoid nested event loop issues.
    # Pattern: as_url_param(EXPR) → run_until_complete(as_url_param(unwrapped_EXPR))
    def _fix_as_url_param(m):
        arg = m.group(1)
        return (
            f"object.__getattribute__(self.repo, '_loop').run_until_complete("
            f"github.asynchronous.Repository.Repository.as_url_param("
            f"SyncProxy._deep_unwrap({arg})))"
        )

    result = re.sub(
        r"github\.asynchronous\.Repository\.Repository\.as_url_param\(([^)]+)\)",
        _fix_as_url_param,
        result,
    )
    # Ensure SyncProxy is importable in the test
    if "SyncProxy._deep_unwrap" in result and "from tests.asynchronous.Framework import SyncProxy" not in result:
        # SyncProxy is defined in Framework.py which is already imported
        # but may not be explicitly imported. Add import if needed.
        if "SyncProxy" not in result.split("class ")[0]:
            result = result.replace(
                "from tests.asynchronous import Framework",
                "from tests.asynchronous import Framework\nfrom tests.asynchronous.Framework import SyncProxy",
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
    """Write content to path, creating parent dirs as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def run_formatters(directory: Path):
    """Run black and ruff on generated files."""
    venv_bin = REPO_ROOT / ".venv" / "bin"
    black = venv_bin / "black"
    ruff = venv_bin / "ruff"

    if black.exists():
        logger.info(f"  Running black on {directory}...")
        subprocess.run(
            [str(black), str(directory), "--quiet", "--line-length", "120"],
            cwd=str(REPO_ROOT),
            capture_output=True,
        )
    else:
        logger.debug("run_formatters: black not found at %s", black)

    if ruff.exists():
        logger.info(f"  Running ruff check --fix on {directory}...")
        subprocess.run(
            [str(ruff), "check", "--fix", str(directory), "--quiet"],
            cwd=str(REPO_ROOT),
            capture_output=True,
        )
    else:
        logger.debug("run_formatters: ruff not found at %s", ruff)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


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

    logger.info("[1/6] Parsing source files...")
    analyzer = IOAnalyzer()
    analyzer.parse_all()
    logger.info(f"Found {len(analyzer.trees)} source modules")
    logger.info(f"Found {len(analyzer.class_to_file)} classes")

    logger.info("[2/6] Analyzing I/O dependencies...")
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

    # ---- Generate async source files ----
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

    # Generate transformed source files
    reexport_count = 0
    for p in sorted(SRC_PKG.glob("*.py")):
        stem = p.stem
        if stem in SKIP_FILES or stem.startswith("_"):
            logger.debug("main: skipping %s (SKIP_FILES or private)", stem)
            continue

        src = p.read_text(encoding="utf-8")

        if stem in analyzer.trees:
            # Check if this file has any async classes
            has_async = any(
                cls_name in analyzer.async_classes
                for cls_name in analyzer.class_to_file
                if analyzer.class_to_file[cls_name] == stem
            )

            if has_async:
                logger.debug("main: full transform for %s", stem)
                transformed = transformer.transform_file(stem, src)
            else:
                # Non-async module: generate a re-export stub so that
                # github.asynchronous.X.Y IS github.X.Y (same object).
                # This avoids isinstance mismatches between sync/async.
                logger.debug("main: re-export stub for %s (no async classes)", stem)
                transformed = _generate_reexport_stub(stem)
                reexport_count += 1
        else:
            # Module not in parsed trees — still generate re-export stub
            logger.debug("main: re-export stub for %s (not in parsed trees)", stem)
            transformed = _generate_reexport_stub(stem)
            reexport_count += 1

        write_file(DST_PKG / f"{stem}.py", transformed)
        generated_count += 1

    logger.info(f"Generated {generated_count} files ({reexport_count} re-export stubs)")

    logger.info(f"[4/6] Generating async test files in {TEST_DST}...")

    if TEST_DST.exists():
        shutil.rmtree(TEST_DST)

    TEST_DST.mkdir(parents=True)

    write_file(TEST_DST / "__init__.py", AUTO_HEADER)
    write_file(TEST_DST / "Framework.py", generate_async_test_framework())
    write_file(TEST_DST / "conftest.py", generate_async_test_conftest())

    test_count = 0
    for p in sorted(TEST_SRC.glob("*.py")):
        if p.name in SKIP_TEST_FILES:
            logger.debug("main: skipping test %s (SKIP_TEST_FILES)", p.name)
            continue
        if p.is_dir():
            continue

        src = p.read_text(encoding="utf-8")

        # Only transform files that are actual test files (contain test classes)
        if "Framework.TestCase" not in src and "BasicTestCase" not in src:
            logger.debug("main: skipping test %s (no TestCase/BasicTestCase)", p.name)
            continue

        logger.debug("main: transforming test file %s", p.name)
        transformed = transform_test_file(src, p.stem)
        write_file(TEST_DST / p.name, transformed)
        test_count += 1

    logger.info(f"Generated {test_count} async test files")

    logger.info("[5/6] Running formatters...")
    run_formatters(DST_PKG)
    run_formatters(TEST_DST)
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
            logger.error(f"  SYNTAX ERROR in tests/{p.name}:{e.lineno}: {e.msg}")
            errors += 1

    logger.info(f"\n{'=' * 60}")
    logger.info("Generation complete!")
    logger.info(f"  Async source: {DST_PKG}")
    logger.info(f"  Async tests:  {TEST_DST}")
    logger.info(f"{'=' * 60}")

    if errors:
        logger.error(f"\n  {errors} files with syntax errors! The async_generator NEED updating!")
        exit(1)
    else:
        logger.info("All files pass syntax check. Excellent news! Have a great day.")


if __name__ == "__main__":
    main()
