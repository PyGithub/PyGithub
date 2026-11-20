---
name: review
description: Review a PyGithub pull request (or local branch / diff) the way the PyGithub maintainer does, and decide whether it can be approved or which changes are required. Reviews GitHub API changes (PyGithub classes wrapping endpoints) in depth; identifies and highlights architectural changes for a maintainer decision on their direction. Use when asked to review a PR, check a contribution, or decide if a change is ready to merge.
---

# Reviewing PyGithub pull requests

This skill condenses what the maintainer actually asked for before approving ~100 recently merged community pull
requests. Most PRs get approved after one round of *minor* changes; the recurring themes below are what those
rounds were about. Check every item, in this order, and only approve when nothing is left.

A PR can contain two kinds of change, which are reviewed differently (step 2):

- **GitHub API changes** — PyGithub classes and methods wrapping specific GitHub REST API endpoints, built on the
  existing PyGithub architecture. These are **reviewed in depth** (steps 3–11).
- **Architectural changes** — changes to how PyGithub interacts with the GitHub REST API in general. These are
  **identified and highlighted, not reviewed in depth**: before anyone reviews their implementation, the maintainers
  have to judge whether PyGithub should go in that direction at all.

First read [ARCHITECTURE.md](../../../ARCHITECTURE.md). It is the canonical reference for code conventions, API design
conventions, test conventions and replay data. This skill tells you **what to look for**; ARCHITECTURE.md explains
**what correct looks like**.

## 1. Gather context

```bash
gh pr view <N> -R PyGithub/PyGithub --json title,body,author,files,commits,baseRefName,headRefName,statusCheckRollup
gh pr diff <N> -R PyGithub/PyGithub
gh pr checks <N> -R PyGithub/PyGithub
gh pr view <N> -R PyGithub/PyGithub --comments          # earlier discussion
```

For a local branch use `git diff origin/main...HEAD` instead.

- Read the linked issue(s). Understand the problem being solved, not just the diff.
- Search for **related / overlapping PRs and issues** (`gh pr list -R PyGithub/PyGithub --search "<keyword>"`,
  `gh issue list ... --search`). Reference them in the review. If another PR already fixes part of this (e.g. an
  allowed host in `Requester`, a dependency bump), ask to drop that part and say which PR covers it. If another PR
  (open or merged) already covers the whole change, the PR is closed "in favour of #N" / "Superseded by #N" / "Fixed
  in #N" — about a third of recently closed unmerged PRs ended this way.
- **Is the change needed at all?** Before reviewing details, check whether users can already achieve the goal:
  - lazy objects (`Github(lazy=True)`, `withLazy`) avoid requests without new code,
  - `Github(per_page=…)` controls page size for all `PaginatedList`s (no per-method `per_page` parameters),
  - `requests` honours `HTTP(S)_PROXY` environment variables,
  - the GitHub API may not support the parameter / value at all (check the docs),
  - an existing feature or a docs example (e.g. reading rate limits from response headers) may already answer the
    use case.
  If so, point the author to it instead of reviewing the code.
- **Fix the root cause, not the symptom.** Class-specific logic in a general place (e.g. release-by-tag URL
  handling in `Requester`) indicates a fix at the wrong level; ask where the problem originates (e.g. `GitRelease`
  using a non-canonical URL as lazy URL, or a base class like `Variable` not being initialised / reused properly).
- **General problems are fixed generally.** Piecemeal fixes of a problem that affects most classes (e.g. missing
  nullable annotations) should instead be done for all classes, usually via the OpenAPI tooling
  (`scripts/openapi.py`), not by hand in one class.
- **Semantic questions first.** When a PR changes the meaning of an existing value (e.g. `PaginatedList.totalCount`
  being the number of items when fully iterated vs. GitHub's capped `total_count`), resolve the intended semantics
  (and link the related issues) before reviewing the implementation; both semantics may be useful and need different
  APIs.
- Look up the endpoint in the GitHub REST docs and in the OpenAPI spec (`api.github.com.*.json`, query with `jq` or
  the `openapi` skill) to verify paths, verbs, parameter names, response schemas, nullability and status codes. Do
  not trust the PR description for this; reviewers have found methods whose response schema did not match the
  implementation at all.
- **Find prior art.** Before judging how something is done, search for how the same thing is already done in other
  PyGithub classes (`grep -rn` in `github/` and `tests/`): the same endpoint shape at another level (repo vs. org vs.
  enterprise, e.g. `Repository.get_self_hosted_runners` for `Organization.get_self_hosted_runners`, repo vs. org
  secrets / variables / code scanning alerts), similar parameters (`Opt[...]` lists, `Commit | str`, `NamedUser | str`),
  similar return shapes (`list_item=` for wrapped lists, `NonCompletableGithubObject` result classes), streaming /
  downloads, deprecations, and the matching tests and replay data. The PR should reuse the existing pattern, naming
  and practices; deviations need a reason. Point the author to the concrete prior art (file:line or method name) in the
  review.

## 2. Classify the changes: architecture vs. GitHub API

Go through the diff and assign every change to one of two kinds. The question is not "which file is touched", but
"does this change how PyGithub talks to the GitHub REST API **in general**, or does it wrap **specific endpoints**
using the existing general mechanisms?"

**GitHub API changes** — reviewed in depth in steps 3–11:

- New or changed PyGithub classes in `github/<Class>.py` wrapping endpoints or OpenAPI schemas: attributes,
  properties, `_initAttributes` / `_useAttributes`, methods calling endpoints, `:calls:` docstrings, class
  docstrings.
- Their deprecations, breaking changes and `doc/changes.rst` entries.
- Their tests in `tests/<Class>.py`, replay data in `tests/ReplayData/`, and examples in `doc/examples/`.
- Endpoint-specific constants (e.g. a new media type in `github/Consts.py` used by one method).
- Bulk changes produced by the **existing** OpenAPI tooling (`scripts/openapi.py apply …`), since they apply the
  current architecture to more classes.

**Architectural changes** — identified and highlighted, not reviewed in depth:

- The HTTP layer: `Requester` (request encoding, headers incl. API version / media types sent with every request,
  redirects, retries, rate-limit handling, timeouts, connection pooling, streaming, base URL / host handling).
- The object model: `GithubObject`, `CompletableGithubObject`, `NonCompletableGithubObject`, `Attribute`, lazy
  loading and completion semantics, `NotSet` / `Opt`, `PaginatedList` (paging, `totalCount`, slicing), the
  `GithubException` hierarchy and how status codes map to exceptions.
- Entry points and authentication: `Github` / `GithubIntegration` constructor options, `Auth` classes, `GithubRetry`,
  `Pickle` support of these classes.
- Dependencies and packaging: runtime dependencies, extras, supported Python versions, `pyproject.toml`,
  `requirements/*.txt`, package layout, generated code, async support.
- Tooling and infrastructure: `scripts/openapi.py`, `scripts/sort_class.py`, CI workflows, pre-commit configuration,
  the test framework (`tests/Framework.py`, replay mechanism), doc build.
- Changes to the conventions themselves (ARCHITECTURE.md, a new pattern applied across all classes such as a
  different annotation style or a new base-class hook), even when every individual edit is in a class file.
- **Sub-class relations between PyGithub classes**: making one PyGithub class derive from another (e.g.
  `CommitSearchResult(Commit)`, `SubIssue(Issue)`), introducing a new shared base class (`AdvisoryBase`,
  `DiscussionBase`), or changing / removing an existing relation. This decides how GitHub schemas map onto PyGithub
  classes, `isinstance` semantics, which attributes and methods a class inherits (and whether they are valid for its
  schema and URL), completion / lazy loading behaviour, and what future changes to the base class affect. Adding
  another member to an existing shared base class (a new `…Advisory(AdvisoryBase)`) follows prior art and is an API
  change; flag it if in doubt.

Grey zones — classify as architectural and flag them:

- A GitHub API change whose implementation adds a capability to the general layer (e.g. streaming downloads in
  `Requester` for `GitReleaseAsset.download_asset`): the `Requester` part is architectural, the class method is an API
  change.
- Class-specific logic placed in a general place (e.g. release-by-tag URL handling in `Requester`): this is an
  architectural change *in effect* — highlight it and ask whether the problem should be fixed in the class instead
  (see "Fix the root cause" in step 1).
- A small bug fix in the general layer is still architectural: it changes the behaviour of every request it touches.

**For architectural changes, do not review the implementation in depth** — no line-level convention findings, no
suggestion blocks, no test-mutation checks on that code. The maintainers first have to decide whether PyGithub should
go in that direction at all; a detailed review of code that may be rejected wastes everyone's time. Instead, for each
architectural change, prepare for the maintainers:

1. **What changes** — the files / components touched, and the behaviour before vs. after in plain words.
2. **Who is affected** — every request / every class, or only users opting in (new option, new method).
3. **Implications** — as far as visible from the diff:
   - backward compatibility (changed defaults, changed behaviour of existing calls, changed exceptions, need for a
     major release),
   - defaults: does the change keep today's behaviour by default (`None` → nothing sent), or would it change every
     request and require touching all replay data?
   - new runtime dependencies or extras, supported Python versions,
   - maintenance cost, code duplication (e.g. sync / async), consistency with existing patterns,
   - `Requester` specifics: bypassing the existing infrastructure (`__requestEncode` / `__requestRaw`: error handling,
     rate limit headers, retries) by calling `requests` directly; changes to code guarded by `__connection_lock`
     (thread safety); risky optimisations of correct-but-slow code,
   - pickling of `Github`, `Requester`, `PaginatedList` or `Auth` (new unpicklable state, step 8),
   - effect on tooling and CI (OpenAPI scripts, class sorting, replay data).
4. **Alternatives** — can users already achieve the goal without it (step 1, "Is the change needed at all?")? Is there
   a smaller or opt-in variant, or a class-level fix instead?
5. **Prior discussion** — linked issues, earlier PRs and maintainer comments on the same direction. If a maintainer
   has already decided on the direction (in the PR, a linked issue or a discussion), cite that decision; the in-depth
   review of the architectural code is then a separate maintainer task, not part of this review unless the user
   explicitly asks for it.
6. **Question for the maintainers** — the concrete direction decision needed (e.g. "Should PyGithub send an API
   version header with every request, and with which default?", "Should `CommitSearchResult` derive from `Commit`, or
   be a separate class implementing the `commit-search-result-item` schema?").

**Architectural suggestions are welcome, but they are not requests.** The reviewer may itself propose an architectural
direction, e.g. a sub-class relation or shared base class for classes the PR adds with largely duplicated attributes,
or dropping a relation the PR introduces. Present it in the architectural section as a suggestion for the maintainers,
with its trade-offs; do not ask the contributor to implement it until the maintainers have made the call.

Then:

- **Pure GitHub API PR**: continue with steps 3–11 for everything.
- **Pure architectural PR**: skip the in-depth steps; the review consists of the highlighted architectural changes
  (step 12). Still point out obvious blockers that need no direction decision (e.g. CI cannot run, the PR is a
  duplicate, unrelated changes mixed in).
- **Mixed PR**: review the GitHub API part in depth (steps 3–11), highlight the architectural part, and propose a
  split (step 3): the architectural change as its own PR, the API change stacked on top of it — or, if the API change
  does not really need the architectural change, rewritten to use the existing architecture.

## 3. Scope and hygiene

**One PR, one scope.** Identify the distinct concerns in the PR (e.g. a new endpoint + a `Requester` fix + a
docs improvement + a dependency bump). Each distinct concern goes into its own PR:

- Independent concerns → separate PRs against `main`.
- A concern that builds on another (e.g. a `Requester` streaming capability, then `GitReleaseAsset.download_asset`
  using it; or a deprecation PR followed by the breaking-change PR) → separate PRs **stacked** on GitHub: the
  dependent PR's base branch is the branch of the PR it builds on, so each PR shows only its own diff and they are
  merged in order. When the base branch cannot be used (e.g. both branches live in a fork), the dependent PR targets
  `main`, states "Depends on #N" in its description, and is reviewed on its own commits only and merged after #N.

Architectural changes identified in step 2 are always a concern of their own: they are split out of a GitHub API PR
(the API PR stacked on top when it needs them), so the maintainers can decide on the architectural direction without
blocking, or being blocked by, the endpoint work.

Name the concerns you found and propose the split in the review.

Then request the removal of anything not needed for the PR's purpose. Look for:

- Unrelated formatting / whitespace changes, re-quoted comments (`'Pending' members won't` → `"Pending" members
  won"t"`), broken license-header alignment, added blank lines.
- Unrelated functional changes (e.g. `encoding="utf-8"` in `doc/conf.py` in a PR that adds a Sphinx extension) — ask
  "Is this related to …?" and move them into a separate PR.
- Changes to unrelated method signatures / typing.
- Dependency or tool version changes (`requirements/*.txt`, `.pre-commit-config.yaml` revs) that are not the point of
  the PR → separate PR.
- Modified files that should be reverted (e.g. a shared `tests/ReplayData/<Class>.setUp.txt`).
- Copyright lines copied from another file into a new file. New files need the license header block, but the
  `Copyright …` lines are generated automatically at release time — contributors do not add themselves or others.
- Leftovers: `print(...)`, `# TODO`, stub methods with `pass`, placeholder comments like
  `# New file named github/X.py`, a bare `return` at the end of a function, empty `if TYPE_CHECKING: pass` blocks,
  unused imports, committed build / test artifacts (`pytest.xml`, coverage files).
- Redundant code: methods that are equivalent to a combination of existing ones (`Repository.update_ruleset(id, …)`
  ≡ `Repository.get_ruleset(id).edit(…)` when `get_ruleset` is lazy) are removed.
- **Generated / mechanical contributions**: when content looks generated (AI-written code, bulk docstring changes,
  tool-driven refactorings), ask "Is this auto-generated or hand-crafted?" and for the commands to reproduce it.
  Scrutinise such PRs extra carefully: wrong license headers, invented API parameters, mocked tests, claims about
  response fields that are not in the replay data (ask for evidence, e.g. the field in
  `tests/ReplayData/<Class>.setUp.txt`).

## 4. API design

See "API Design Conventions" in ARCHITECTURE.md. Compare everything below against the prior art found in step 1 —
if another class already solves the same problem, the PR must follow that solution. Check:

- **Placement**: does each new method live on the class of the resource it operates on? A method on a parent that takes
  the child's id (`Environment.delete_deployment_branch_policy(id)`, `Repository.get_workflow_run_attempt(run_id, n)`)
  should move to the child (`DeploymentBranchPolicy.delete()`, `WorkflowRun.get_attempt(n)`).
- **Naming**: `get_*` (not `list_*`), `edit_*` (not `update_*`), plural for batch operations (`add_seats`),
  parameter names as in the GitHub API docs, consistent with sibling methods in other classes.
- **One method, flexible arguments**: instead of a second method (`create_review_comment_with_primitives`) accept
  `Commit | str`, `int | Issue`, etc.
- **Return types**: a useful response payload should be returned as a PyGithub class (new
  `NonCompletableGithubObject` if it has no endpoint), not discarded or returned as `dict`. Action-only methods return
  `None` (a `delete_*` must not be annotated as returning `PaginatedList`). No `bool` "success" returns where an
  exception already signals failure.
- **Explicit API calls always call the API**; they do not fall back to a cached property, and they update the object's
  attributes from the response when appropriate.
- **Unknown vs. false**: a value that is unknown until a request happens is `T | None`.
- **No client-side validation of enum values** (`allowed_states = [...]`): these go stale; the API validates.
- **Precise types**: `Opt[dict[str, Any]]` not `Opt[dict[Any]]`; `bool` parameters, not `"true"` strings;
  `Opt[NamedUser | str]` rather than `NamedUser | Opt[str]`.
- **Nested objects are classes, not dicts**: attributes like `bypass_actors: list[dict[str, Any]]` should be a list
  of a dedicated PyGithub class implementing the OpenAPI schema (bootstrap it with
  `python scripts/openapi.py create class …`, see the `openapi` skill). New classes list their OpenAPI schema in the
  docstring.
- **Parameters match the API docs**: remove parameters the endpoint does not document (and `per_page`, which is
  global), add documented parameters that are missing while touching the method; for GraphQL, support all arguments
  of the field (e.g. `orderBy`, `userLinkedOnly`).
- **GraphQL-backed methods** follow `Repository.get_discussions`: let the caller pass the GraphQL schema of returned
  objects (`…_graphql_schema: str = "…"`), always include the fields needed to construct the REST `url` (e.g.
  `number`) so the object can be completed via REST, and keep GraphQL's HTML `url` as `html_url`. Test with an empty
  schema, a custom schema, and completing a returned object.
- **Status codes**: do not turn `requestJsonAndCheck` into `requestJson` + `return status == 204` (bad practice,
  #2760 — errors get swallowed). Use `requestJson` and inspect `status` only where a status is a documented result
  (e.g. 404 meaning "not enabled"), and still raise for any other unexpected status; then check all methods using
  the same pattern.
- **Defaults keep current behaviour**: a new parameter of an existing method defaults to the behaviour users have
  today (`NotSet` → nothing sent); a default that changes the request would also require touching that method's
  replay data. (New options that affect every request, e.g. an API version header, are architectural, step 2.)
- **Keyword-only for internal / trailing arguments**: arguments that user code should not pass positionally (e.g.
  `requester`) go after `*`, so new public arguments can be added before them without breaking callers. `:param:`
  docs follow the signature order.
- **Accurate messages**: exception and log messages must describe the actual situation (e.g. a redirect loop is not
  "you may need to correct your base_url" when both URLs are identical).
- **Generality**: does the change fix the whole class of problem? When a PR fixes one occurrence of a pattern
  (missing `urllib.parse.quote(..., safe="")`, `warnings.warn` without `stacklevel`, mutating a caller's headers dict),
  `grep` the code base and ask to fix all occurrences.

## 5. Backward compatibility

PyGithub has many users; any break must be deliberate. See ARCHITECTURE.md "Backward compatibility" and
"Deprecations".

**Find every break.** Walk through each changed public signature, property, return type and default and ask "does
existing user code still run and behave the same?":

- New parameter inserted in the **middle** of an existing signature → must be appended at the end (callers pass
  positionally), unless it is keyword-only.
- Renamed parameters break keyword callers → keep the old name; at most add a `# v3: …` comment.
- Removed / renamed methods, properties or classes; changed return types (e.g. `dict` → PyGithub object, `str` →
  object); changed defaults that are sent to the API (e.g. dropping `event="COMMENT"`) — ask what GitHub does when
  the value is omitted.
- Nullable fields: when an attribute becomes `Attribute[T | None]`, the property return type must also become
  `T | None` (a common miss; this is a typing fix, not a break).

**Split breaking changes out.** For every break found, check whether it can be moved into a subsequent PR, leaving
this PR with the new API plus a proper deprecation of the old one. Request that split unless a non-breaking
intermediate step is genuinely impossible; in that case the PR must say so and the break must be documented with
"code like … should be replaced with …" (as in the "Breaking Changes" sections of `doc/changes.rst`).

**Check every deprecation:**

- Uses `@deprecated("…")` from `typing_extensions` (methods, properties, classes) or
  `warnings.warn("…", category=DeprecationWarning, stacklevel=2)` (parameters / values). `stacklevel` makes the
  warning point at the caller; check all `warnings.warn` calls in the touched module.
- The message names an **alternative**, and the alternative provides **identical, or as similar as possible,
  behaviour**. Verify this by comparing old and new code paths: same returned data, same laziness, same number of API
  calls. If the alternative needs an extra request, the deprecation / description must show how to avoid it (e.g. a
  lazy `Github` instance: `Github(..., lazy=True).get_organization(...).get_hook(id).edit(...)`). If the alternative
  does not exist yet, it must be added in the same PR.
- The deprecated API still works unchanged (preferably delegating to the alternative) and remains tested; tests
  assert the `DeprecationWarning`.
- **The PR description enumerates all deprecations** (and breaking changes), each with its alternative, in a form
  that can be copied into the "Deprecations" section of `doc/changes.rst`. Compare the list against the diff
  (`grep` the diff for `deprecated` and `DeprecationWarning`); ask the author to add missing entries.

## 6. Implementation conventions

Compare against ARCHITECTURE.md "Naming and Structuring Conventions". The most frequent findings:

- Runtime references to other PyGithub classes use `github.<File>.<Class>` (incl. `isinstance` checks:
  `isinstance(x, (github.NamedUser.NamedUser, str))`); annotations use the short name imported under
  `if TYPE_CHECKING:` (`-> PublicKey`, not `-> github.PublicKey.PublicKey`). `from typing import TYPE_CHECKING, Any`.
- `from __future__ import annotations` in every module.
- Request bodies built with `NotSet.remove_unset_items({...})`; omitted values must be `NotSet`, **not `None`**
  (`None` is sent as JSON `null`). No `if is_defined(x): params["x"] = str(x)` chains, no needless `str(...)`.
- `get_X(id)` constructs the object lazily from a URL (no `requestJsonAndCheck` in the method).
- `NonCompletableGithubObject` is constructed without `completed=True`; a class without its own endpoint must not
  derive from `CompletableGithubObject`.
- `assert` for each parameter, in parameter order.
- `data.get("key")` instead of `data.get("key", None)`; `isinstance(x, (A, B))` instead of `isinstance(x, A) or
  isinstance(x, B)`.
- New media type constants in `github/Consts.py` go next to the existing media type constants, not at the end.
- Methods use the existing `Requester` API (`requestJsonAndCheck`, `requestJson`, …) rather than calling `requests`
  directly or reaching into `Requester` internals. Any change *to* `Requester` is architectural (step 2).
- `_useAttributes` must set every attribute declared in `_initAttributes` (look for missing ones, e.g.
  `dismissal_approved_by`).
- **Member order** (ARCHITECTURE.md "Internal Class Order", enforced by `scripts/sort_class.py`): prolog →
  `__init__` → `_initAttributes` → dunders (alphabetical) → `@property`s (alphabetical) → other methods →
  `_useAttributes` last. Attribute assignments in `_initAttributes` and the `if "key" in attributes` blocks in
  `_useAttributes` are alphabetical (ASCII: `repo_name` before `repository`). Check in particular:
  - a new property / attribute / `if` block inserted at the right alphabetical position in **all three** places
    (`_initAttributes`, properties, `_useAttributes`) — the most common CI "sort classes" failure;
  - classes that subclass another PyGithub class (`SubIssue(Issue)`, `RepositoryAdvisory(AdvisoryBase)`) are not
    sorted by the script, so check their order by hand;
  - no class-level statements between methods (the script fails on them);
  - new regular methods are not sorted by the script: they belong next to related methods (`get_x` / `create_x` /
    `delete_x` together), not appended at the end of the class or after `_useAttributes`.

  Run `python scripts/sort_class.py --dry-run openapi.index <Class> …` (needs `libcst`, from
  `requirements/scripts.txt`, and an index from `python scripts/openapi.py index github openapi.index`); any diff it
  prints is a required change.

## 7. Documentation

- Every API-calling method has a `:calls:` line with the HTTP verb, the path template using the **docs'
  placeholders** (`/orgs/{org}/...`, not `/orgs/{owner}/{repo}/...`), and a link to the **exact** docs anchor of that
  endpoint (not a generic `rest/reference/...` page or an anchor of a different endpoint). Check the backtick/quote
  syntax: `` :calls: `GET /path <url>`_ ``.
- Class docstrings: reference URL plus `The OpenAPI schema can be found at`, followed by a **blank line** and then the
  `- /components/schemas/...` list (Sphinx needs the blank line). A blank line before the closing `"""` when the
  docstring ends with prose.
- Parameter docs explain non-obvious interactions (e.g. `max_rate_limit_wait < secondary_rate_wait` means secondary
  rate limits always raise).
- Files under `doc/` are reStructuredText, not Markdown (`### Overview` is wrong). Check the Read the Docs preview
  (`https://pygithub--<N>.org.readthedocs.build/en/<N>/`) for rendering problems.
- GraphQL references link to an anchor that exists.
- **Example code must work.** Check every code snippet the PR adds or touches — in docstrings
  (`.. code-block:: python`, inline ``` ``…`` ```), in plain strings such as `@deprecated(...)`, `warnings.warn(...)` and
  exception messages, and in `doc/` (`doc/examples/*.rst`, `doc/changes.rst`). It must be syntactically valid Python
  and use methods, properties and arguments that exist with those names, types and return types in the code after this
  PR (e.g. a `PaginatedList` is iterated, not indexed like a `dict`; the alternative named in a deprecation message
  actually exists). When in doubt, run the snippet against replay data or write a quick test; doc examples should
  ideally be backed by a test.

## 8. Pickling

See ARCHITECTURE.md "Pickling".

- Pickling must keep working: look for new attributes on PyGithub classes holding unpicklable state (locks, sessions /
  connections, open files, generators, lambdas, local functions). Such state must be excluded in `__getstate__` and
  recreated in `__setstate__`; new objects with extra runtime state need a pickle round-trip test in `tests/Pickle.py`.
- New state on `Github`, `Requester`, `PaginatedList` or `Auth` classes is architectural (step 2): list its pickling
  impact among the implications for the maintainers instead of reviewing it here. (Once that direction is agreed, a
  new `Auth` class must be added to `Pickle.auths` in `tests/Pickle.py`.)
- Do **not** request changes because objects pickled with a different PyGithub release can no longer be unpickled
  (renamed private attributes, changed class layouts) — compatibility across releases is not guaranteed.

## 9. Tests

A behavioural change without a test is not approvable. Ask for one (offer guidance on how to record / hand-craft
replay data if the contributor struggles). Check against ARCHITECTURE.md "Test Conventions":

- Test is in `tests/<Class>.py` in the existing test class. A new test class / file is only acceptable for a new
  PyGithub class or one that has no tests yet. Request moving tests out of per-issue / per-PR test classes or files
  (`tests/IssueNNNN.py`, `tests/PullRequestNNNN.py`, `class InstallationGetRepos`) and out of ad-hoc classes into the
  class' main test class (and rename the replay data files accordingly). Legacy `tests/Issue*.py` files are not a
  precedent.
- **New tests must fail without the contribution — for the right reason.** Check it out and revert only the
  non-test changes, then run the new / changed tests:

  ```bash
  # fetch upstream main and the PR head, independent of how remotes are named locally
  git fetch https://github.com/PyGithub/PyGithub.git \
    +refs/heads/main:refs/remotes/pygithub/main +refs/pull/<N>/head:refs/remotes/pygithub/pr-<N>
  # use a separate worktree, so the current checkout is not disturbed
  git worktree add --detach ../pr-<N> pygithub/pr-<N> && cd ../pr-<N>
  BASE=$(git merge-base pygithub/main HEAD)
  git diff --name-only $BASE -- github/                         # production changes of the PR
  git checkout $BASE -- github/                                 # revert them, keep tests + replay data
  pytest tests/<Class>.py -k "<newTest1> or <newTest2>"
  git checkout HEAD -- github/                                  # restore
  ```

  (Remove the worktree afterwards with `git worktree remove ../pr-<N>`.)

  - **Bug fixes**: every new test must fail with an assertion error or a replay data mismatch (e.g. the request does
    not match the recorded one). A test that still passes does not cover the fix.
  - A failure that is *only* due to the new code not existing (`AttributeError` / `ImportError` / `NameError` /
    `TypeError: unexpected keyword argument`) proves nothing. This is always the case for new methods, classes or
    parameters, so check that the assertions would catch a **wrong** implementation instead: e.g. temporarily drop
    the new parameter from the request body, return a wrong attribute, skip the `_useAttributes` branch, or break the
    URL — the test must then fail. Typical misses: asserting `pull.id` instead of the attribute that the new
    argument affects, asserting only the type of a result, or a replay data file that does not contain the new
    parameter at all.
  - Ask the author to strengthen the test when it passes without the fix or survives a broken implementation.
- camelCase `testXxx` names.
- Assertions verify what changed: the new argument's effect, the reordered order, the removed item, every field of a
  new result class, both `status` and `message` of expected exceptions (`assertEqual`, not `assertIsNone(x, msg)`).
- If an existing test already exercises the method, extend it instead of duplicating.
- No `print`, no loops-with-`break` to get the first item, `assertIsNone` for `None`.
- **Replay data, not mocks**: tests must use the replay data framework. Mocking `requestJsonAndCheck`, `responses`
  / `httpretty` decorators or hand-written JSON responses in the test are not accepted; ask to record replay data or
  to copy and hand-edit an existing replay data file (e.g. copy `Milestone.testEditWithAllParameters.txt` and change
  `due_on`).
- **Positive and negative cases**: a test with invalid input only is not enough — require a test with valid values
  and recorded data. Use distinct values in tests so that "unchanged" vs. "overwritten" is observable (e.g. pass
  `start_side="RIGHT"` when the default would be `"LEFT"`).
- New tests sit next to related tests in the file (e.g. a slice test next to the other slice tests).
- Tests that only repeat what `setUp` or another test already covers (e.g. `Repository.testGetRuleset` when
  `Ruleset.setUp` calls `get_ruleset`) are removed.
- Parent objects fetched with `lazy=True` to avoid unrelated recorded requests.
- Windows-safe (temp files, no symlinks — use `self.replayData("Other.test.txt")` to share replay data).
- Organisation-level variants: when an endpoint exists for repos and orgs, both are implemented and tested.
- Doc examples (`doc/examples/*.rst`) ideally get a test proving they work.

## 10. Replay data

See ARCHITECTURE.md "Replay Data". Check:

- Every new/changed test has its `tests/ReplayData/<Class>.<test>.txt`; renamed tests have renamed files.
- If the PR changes what is sent (query encoding, request body defaults, parameter names, strings asserted in tests),
  the **existing** replay data files that contain the old request must be updated — CI failures in otherwise
  untouched tests usually mean exactly this.
- Anonymisation / normalisation: org `BeaverSoftware`, the test class' standard repo (`PyGithub/PyGithub`), the
  `Authorization` header matching the test's auth mode (`token private_token_removed` by default), no personal
  account names, tokens, emails, or ids that leak the contributor's org (e.g. in `Link` headers).
- No superfluous requests (a GET that disappears when the parent is obtained lazily).
- Hand-crafted files must be consistent with what the code sends (path, query, body).

## 11. CI

Open each failing check and translate it into a concrete request:

- **pre-commit / lint** (ruff check, ruff format, codespell, whitespace): ask the contributor to run
  `pre-commit run --all-files`, or to run the `auto-fix` workflow on their fork
  (`https://github.com/<user>/PyGithub/actions/workflows/auto-fix.yml`), which applies pre-commit fixes and class
  sorting and pushes them to the branch.
- **mypy** (`mypy github tests`): type errors are blocking.
- **docs** (`sphinx-build doc build`): new warnings/errors are blocking.
- **OpenAPI / code-structure checks** ("Check verbs", "Add schemas", "Implement schemas", "Sort classes"): never
  just report pass/fail — read the output and judge whether it is relevant to this PR (see below).
- **Tests** on all supported Pythons and on Windows. New optional dependencies / extras are architectural (step 2);
  once agreed, they must be tested in CI and tox both with and without the extra installed, and installation docs
  (`README.md`, `doc/introduction.rst` "Download and install") updated.
- If CI does not run or fails for reasons fixed on `main`, ask to merge `main` (and resolve conflicts).

Locally, for the touched files:

```bash
pytest tests/<Class>.py
pre-commit run --files <changed files>
mypy github tests
```

### Evaluating "Check verbs", "Add schemas", "Implement schemas" and "Sort classes"

These jobs (`.github/workflows/ci.yml`) run `scripts/openapi.py` / `scripts/sort_class.py` against the target
branch (**base**) and the feature branch (**head**) and fail if the outputs differ ("Sort classes" checks that sorting
the head changes nothing; `main` is kept sorted by the same job on push). The diff therefore shows exactly **what the
feature branch changes** in the scripts' view of the code base: anything that is already present on `main` (an
unsorted class, a missing schema, an unimplemented property) does not show up unless the feature branch changes it.
Every entry in the diff is caused by the PR — the question is whether it is **intended and desirable**, not whether it
belongs to the PR. For each of the four jobs, whether green or red, fetch the log and evaluate it:

```bash
gh pr checks <N> -R PyGithub/PyGithub                      # job names, states and links
gh run view <run-id> -R PyGithub/PyGithub --json jobs -q '.jobs[] | "\(.databaseId) \(.name) \(.conclusion)"'
gh run view <run-id> -R PyGithub/PyGithub --job <job-id> --log | cut -f3- | sed -E 's/^\xEF\xBB\xBF//; s/^[0-9-]+T[0-9:.]+Z //' > job.log
awk '/^Difference:|^Changes:/{p=1} /^Run the following commands|^To fix this/{p=0} p' job.log   # the relevant part
```

If CI has not run (fork PRs awaiting approval), reproduce locally (needs `requirements/scripts.txt`):

```bash
python scripts/openapi.py fetch api.github.com 2022-11-28 openapi.json
python scripts/openapi.py index github openapi.json openapi.index           # on the PR checkout
python scripts/openapi.py --verbose index --check-verbs github verbs.index  # Check verbs
python scripts/openapi.py suggest schemas openapi.json openapi.index        # Add schemas
python scripts/openapi.py --dry-run apply properties --tests github openapi.json openapi.index <Class> …  # Implement schemas
python scripts/sort_class.py --dry-run openapi.index <Class> …              # Sort classes
```

Run the same on the base commit and compare the outputs, as CI does (for "Sort classes", any change on head counts,
as base is sorted).

**How to read the diff.** In `diff base head` output, lines starting with `<` exist only on base, lines starting
with `>` only on head:

- `>` lines are findings the PR **introduces** (a new schema suggestion, a missing property, a verb mismatch, an
  unsorted member). They usually require a change in the PR.
- `<` lines are findings the PR **removes**. Usually good (the PR implemented a suggested schema or property, fixed a
  `:calls:` verb) — the job is still red because the output differs; confirm the removal is intended (e.g. not caused
  by deleting a schema reference or a method) and say in the review that this part is fine.
- Entries for classes or methods that the diff of the PR does not visibly touch are still caused by the PR: e.g. a
  changed return type or new method changes which classes a schema is returned by, a changed base class affects all
  subclasses, a new class changes the class count (`Applying API schemas to 230 … classes` vs. `235`). Trace each
  such entry back to the change that causes it. If the cause is a change that does not belong to the PR's scope
  (e.g. the branch contains unrelated commits), that is a scope problem (section 3).

**Per job:**

- **Check verbs** — compares the verb in each method's `:calls:` line with the HTTP verbs the method actually uses.
  Relevant if a method touched by the PR is listed: the `:calls:` docstring names a wrong verb or path, or the method
  calls the API in a way the index does not recognise ("Not found any … call in …" / "Method … is known to call …").
  Ask to fix the docstring (or, for legitimate indirect calls, the known-verbs section of
  `github/openapi.index.json`). A `<` entry means the PR fixed a pre-existing mismatch.
- **Add schemas** — lists OpenAPI schemas that classes should declare in their docstring (`Class X: - should
  implement schema /components/schemas/…`, with methods/paths returning them). A `> Class X:` entry means the PR
  made a schema applicable to `X` (new class, new method returning the schema, changed return type): ask to add the
  schema to the class docstring after checking it really matches (e.g. via "Methods returning the schema" / "Paths
  returning the class"); if it does not match, the PR's return type or class choice is probably wrong. A `<` entry
  means the PR resolved a suggestion — check it was added to the right class.
- **Implement schemas** — shows which properties the declared schemas would add to / change in each class
  (`Applying schema …`, followed by a `Diff:` that is empty when the class matches the schema). For entries the PR
  introduces:
  - a non-empty `Diff:` means the class misses attributes of its schema (or types differ, e.g. nullability) — ask to
    implement them (`python scripts/openapi.py apply properties --tests … <Class>`), or to justify omitting them;
  - `Schema not implemented: …/properties/<name>` means a nested object has no PyGithub class yet — consider asking
    for a dedicated class instead of `dict[str, Any]`, or accept it as a known gap for a later PR;
  - `<` entries mean the PR implemented properties that were missing before — check they follow the conventions.
- **Sort classes** — the diff shows how members of a class would be reordered (see ARCHITECTURE.md "Internal Class
  Order"). Since `main` is sorted, any diff is caused by the PR and must be fixed (`python scripts/sort_class.py
  openapi.index <Class>`, or the `auto-fix` workflow on the fork). Remember that the script does not reorder regular
  methods, so a green job does not prove new methods are placed next to related ones.

**Tool crashes.** A Python traceback from `scripts/openapi.py` or `scripts/sort_class.py` (e.g. `AttributeError:
'Attribute' object has no attribute 'left'` in `update_use_attrs` / `leave_FunctionDef`) is not a diff. Find the code
in the PR that triggers it — typically an unusual statement in `_useAttributes` (an `if` whose condition is not of the
form `"key" in attributes [and …]`) or `_initAttributes`, or class-level statements between methods. If that code
deviates from the conventions, ask the author to follow them; if the code is legitimate, the script needs fixing
(separate PR, by maintainers) and the job can be ignored for this PR — say so explicitly. Since base passes, the
crash is always triggered by code the PR adds or changes.

**In the review**, state for each of these jobs: relevant or not, why, and (if relevant) the concrete change, citing
the class / method and the log lines. For `<` entries (findings the PR removes), confirm they are fine so the
contributor knows the red job needs no action for them.

## 12. Writing the review

Mirror the maintainer's style: friendly, short, concrete.

- Start the summary with thanks and a one-line assessment, e.g. "Thanks for the contribution! Minor structural changes
  needed." / "Great work, just minor convention issues." / "LGTM!".
- **Architectural changes come first, clearly separated.** If step 2 found any, open the review with a section
  "Architectural changes — maintainer decision needed", addressed to the maintainers, listing each change with the
  points from step 2 (what changes, who is affected, implications, alternatives, prior discussion, the question to
  decide). Keep it neutral and factual: present the trade-offs, do not argue for or against the direction. Tell the
  contributor that this part is waiting for a maintainer decision on the direction and will be reviewed in detail
  afterwards, so they do not polish code that may change. No inline findings on architectural code.
- Then the GitHub API review: put each finding as an inline comment on the exact line. Prefer GitHub
  ```` ```suggestion ```` blocks with the exact replacement text, so the contributor can apply them with one click (also
  for replay data lines). Use a plain comment with the reasoning when the change is structural ("Please move to
  `DeploymentBranchPolicy.delete` (removing `id` parameter).").
- Ask questions where intent is unclear ("Is this related to …?", "What is the current behaviour of GitHub with
  `make_latest` omitted?", "Are these test files hand crafted?") rather than assuming.
- Link the failing CI step or the related PR / issue / docs page.
- Help the contributor get unstuck: explain how to record replay data on a fork (record, revert `setUp` replay data,
  rename the fork owner), offer a patch or a PR against their branch for larger fixes, and ask them to "allow edits
  by maintainers" when a stale PR should be taken over and finished.
- When recommending to close: name the PR / commit / docs that supersede or answer it ("Closing in favour of #N",
  "Fixed in #N", "Would this example work for you?").
- PRs that remove deprecated API are kept as drafts until the next major release; they must also delete the
  corresponding tests and replay data files.
- Verdict:
  - **APPROVE** ("LGTM!") only when every section above is clean, CI is green, and the PR contains no architectural
    change whose direction has not been decided by a maintainer.
  - **REQUEST_CHANGES** for anything in sections 3–11 that must change in the GitHub API part (including a requested
    split of architectural changes into a separate PR); say whether the changes are minor.
  - **COMMENT** for design discussion without a blocking request — in particular for a purely architectural PR
    awaiting the maintainers' direction decision.
- Do not post anything to GitHub unless the user asked for it; by default present the review (architectural changes
  for the maintainers, verdict, summary, inline findings with file:line and suggestions) to the user.
