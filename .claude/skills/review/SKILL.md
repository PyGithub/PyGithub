---
name: review
description: Review a PyGithub pull request (or local branch / diff) the way the PyGithub maintainer does, and decide whether it can be approved or which changes are required. Use when asked to review a PR, check a contribution, or decide if a change is ready to merge.
---

# Reviewing PyGithub pull requests

This skill condenses what the maintainer actually asked for before approving ~100 recently merged community pull
requests. Most PRs get approved after one round of *minor* changes; the recurring themes below are what those
rounds were about. Check every item, in this order, and only approve when nothing is left.

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
  allowed host in `Requester`, a dependency bump), ask to drop that part and say which PR covers it.
- Look up the endpoint in the GitHub REST docs and in the OpenAPI spec (`api.github.com.*.json`, query with `jq` or
  the `openapi` skill) to verify paths, verbs, parameter names, response schemas, nullability and status codes. Do
  not trust the PR description for this; reviewers have found methods whose response schema did not match the
  implementation at all.

## 2. Scope and hygiene

Request the removal of anything not needed for the PR's purpose. Look for:

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
  `# New file named github/X.py`, a bare `return` at the end of a function.

## 3. API design

See "API Design Conventions" in ARCHITECTURE.md. Check:

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
- **Precise types**: `Opt[dict[str, Any]]` not `Opt[dict[Any]]`; `bool` parameters, not `"true"` strings.
- **Generality**: does the change fix the whole class of problem? When a PR fixes one occurrence of a pattern
  (missing `urllib.parse.quote(..., safe="")`, `warnings.warn` without `stacklevel`, mutating a caller's headers dict),
  `grep` the code base and ask to fix all occurrences.

## 4. Backward compatibility

PyGithub has many users; any break must be deliberate.

- New parameter inserted in the **middle** of an existing signature → must be appended at the end (callers pass
  positionally), unless it is keyword-only.
- Renamed parameters break keyword callers → keep the old name; at most add a `# v3: …` comment.
- Changed defaults that are sent to the API (e.g. dropping `event="COMMENT"`), changed return types, removed methods:
  ask what GitHub does when the value is omitted, and require deprecation (`typing_extensions.deprecated`) instead of
  removal.
- Nullable fields: when an attribute becomes `Attribute[T | None]`, the property return type must also become
  `T | None` (a common miss).
- Deprecation warnings point at the caller (`stacklevel=2`); check all `warnings.warn` calls in the touched module.

## 5. Implementation conventions

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
- `Requester` changes: new request paths must go through the existing infrastructure (`__requestEncode` /
  `__requestRaw`: error handling, rate limit headers, retries) rather than calling `requests` directly. Scrutinise
  changes to code guarded by `__connection_lock` for thread safety; prefer leaving correct-but-slow code alone over a
  risky optimisation.
- `_useAttributes` must set every attribute declared in `_initAttributes` (look for missing ones, e.g.
  `dismissal_approved_by`); attributes and methods sorted as required (the `sorted-classes` skill /
  `scripts/sort_class.py`).

## 6. Documentation

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

## 7. Tests

A behavioural change without a test is not approvable. Ask for one (offer guidance on how to record / hand-craft
replay data if the contributor struggles). Check against ARCHITECTURE.md "Test Conventions":

- Test is in `tests/<Class>.py` in the existing test class; no new `IssueNNNN` / ad-hoc test classes or files.
- camelCase `testXxx` names.
- Assertions verify what changed: the new argument's effect, the reordered order, the removed item, every field of a
  new result class, both `status` and `message` of expected exceptions (`assertEqual`, not `assertIsNone(x, msg)`).
- If an existing test already exercises the method, extend it instead of duplicating.
- No `print`, no loops-with-`break` to get the first item, `assertIsNone` for `None`.
- Parent objects fetched with `lazy=True` to avoid unrelated recorded requests.
- Windows-safe (temp files, no symlinks — use `self.replayData("Other.test.txt")` to share replay data).
- Organisation-level variants: when an endpoint exists for repos and orgs, both are implemented and tested.
- Doc examples (`doc/examples/*.rst`) ideally get a test proving they work.

## 8. Replay data

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

## 9. CI

Open each failing check and translate it into a concrete request:

- **pre-commit / lint** (ruff check, ruff format, codespell, whitespace): ask the contributor to run
  `pre-commit run --all-files`, or to run the `auto-fix` workflow on their fork
  (`https://github.com/<user>/PyGithub/actions/workflows/auto-fix.yml`), which applies pre-commit fixes and class
  sorting and pushes them to the branch.
- **mypy** (`mypy github tests`): type errors are blocking.
- **docs** (`sphinx-build doc build`): new warnings/errors are blocking.
- **OpenAPI checks** ("Check verbs", "Add schemas", "Add implementations"): when the job suggests schemas for a new
  class, ask to add them to the class docstring. "Check verbs" differences that are side-effects of the PR are fine.
- **Tests** on all supported Pythons and on Windows.

Locally, for the touched files:

```bash
pytest tests/<Class>.py
pre-commit run --files <changed files>
mypy github tests
```

## 10. Writing the review

Mirror the maintainer's style: friendly, short, concrete.

- Start the summary with thanks and a one-line assessment, e.g. "Thanks for the contribution! Minor structural changes
  needed." / "Great work, just minor convention issues." / "LGTM!".
- Put each finding as an inline comment on the exact line. Prefer GitHub ```` ```suggestion ```` blocks with the exact
  replacement text, so the contributor can apply them with one click (also for replay data lines). Use a plain comment
  with the reasoning when the change is structural ("Please move to `DeploymentBranchPolicy.delete` (removing `id`
  parameter).").
- Ask questions where intent is unclear ("Is this related to …?", "What is the current behaviour of GitHub with
  `make_latest` omitted?", "Are these test files hand crafted?") rather than assuming.
- Link the failing CI step or the related PR / issue / docs page.
- Verdict:
  - **APPROVE** ("LGTM!") only when every section above is clean and CI is green.
  - **REQUEST_CHANGES** for anything in sections 2–9 that must change; say whether the changes are minor.
  - **COMMENT** for design discussion without a blocking request.
- Do not post anything to GitHub unless the user asked for it; by default present the review (verdict, summary,
  inline findings with file:line and suggestions) to the user.
