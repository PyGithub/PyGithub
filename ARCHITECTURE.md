# PyGithub Architecture Overview

A guide for developers and AI coding agents to quickly understand the codebase structure, conventions, and design
principles.

---

## Entry Point

Everything starts from `github/MainClass.py`. The `Github` class is the user-facing entry point:

```python
import github

g = github.Github(auth=github.Auth.Token("your-token"))
repo = g.get_repo("PyGithub/PyGithub")
```

`Github` instantiates a `Requester` and exposes `get_*` methods that return PyGithub objects or `PaginatedList`
instances.

---

## Core Class Hierarchy

PyGithub classes — classes that model GitHub API response data — all inherit from one of three base classes defined in
`github/GithubObject.py`:

```
GithubObject                        (github/GithubObject.py)
├── CompletableGithubObject         — objects with their own endpoint and URL; support lazy loading (Repository, Issue, Label, …)
│   └── CompletableGithubObjectWithPaginatedProperty
│                                   — variant that injects page/per_page into completion requests
└── NonCompletableGithubObject      — embedded objects: no dedicated endpoint, always fully
                                      populated from the enclosing response (Reaction, CommitStats, …)
```

**`CompletableGithubObject`** is used for PyGithub classes that have their own URL and a dedicated API endpoint. They
can be partially populated (e.g. when returned as a nested field inside a list response) and complete themselves on
first attribute access by issuing a GET to their URL. Each lives in its own file named after the GitHub API resource it
wraps.

**`NonCompletableGithubObject`** is used for PyGithub classes that only ever appear embedded inside another resource's
JSON payload and have no dedicated API endpoint of their own. They are always fully populated from the enclosing
response and can never go back to the API for more data. Examples: `CommitStats`, `GitAuthor`, `Permissions`,
`Reaction`.

---

## Lazy Loading

Objects can be partially populated (e.g. only an ID and URL from a list response) and complete themselves on first
attribute access.

**Mechanics:**

1. Every attribute is initialized to the `NotSet` sentinel in `_initAttributes()`.
2. A property getter calls `self._completeIfNotSet(self._attr)` before returning the value.
3. If the attribute is still `NotSet`, `_complete()` fires a GET to `self._url`, populates all attributes, and sets
   `self.__completed = True`.

**Control:**

- `Github(lazy=True)` — all objects start lazy (no completion until attribute access).
- `Github(lazy=False)` (default) — objects complete immediately upon creation.
- `g.withLazy()` — context manager for temporary lazy mode.

---

## Attribute Definition Pattern

The terms "attribute" and "property" are used synonymously in this project. The refer to Python getter methods of
PyGithub classes decorated with `@property`.

Every PyGithub class implements exactly two methods. This is the canonical pattern to follow when adding new classes or
attributes:

```python
# github/SomeThing.py


class SomeThing(github.GithubObject.CompletableGithubObject):
    def _initAttributes(self) -> None:
        # Initialize ALL attributes to NotSet
        self._id: github.GithubObject.Attribute[int] = github.GithubObject.NotSet
        self._name: github.GithubObject.Attribute[str] = github.GithubObject.NotSet
        self._owner: github.GithubObject.Attribute[github.NamedUser.NamedUser] = github.GithubObject.NotSet

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        # Parse each key that is present in the API response
        if "id" in attributes:
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:
            self._name = self._makeStringAttribute(attributes["name"])
        if "owner" in attributes:
            self._owner = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["owner"])

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value  # type: ignore

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value  # type: ignore
```

**Attribute helper methods** (all defined on `GithubObject`):

| Helper                                                                                            | Output type                      |
|---------------------------------------------------------------------------------------------------|----------------------------------|
| `_makeStringAttribute(v)`                                                                         | `Attribute[str]`                 |
| `_makeIntAttribute(v)`                                                                            | `Attribute[int]`                 |
| `_makeBoolAttribute(v)`                                                                           | `Attribute[bool]`                |
| `_makeFloatAttribute(v)`                                                                          | `Attribute[float]`               |
| `_makeDictAttribute(v)`                                                                           | `Attribute[dict]`                |
| `_makeDatetimeAttribute(v)`                                                                       | `Attribute[datetime]` (ISO 8601) |
| `_makeTimestampAttribute(v)`                                                                      | `Attribute[datetime]` (Unix)     |
| `_makeListOfStringsAttribute(v)`                                                                  | `Attribute[list[str]]`           |
| `_makeListOfIntsAttribute(v)`                                                                     | `Attribute[list[int]]`           |
| `_makeListOfClassesAttribute(klass, v)`                                                           | `Attribute[list[klass]]`         |
| `_makeClassAttribute(klass, v)`                                                                   | `Attribute[klass]`               |
| `_makeDictOfStringsToClassesAttribute(klass, v)`                                                  | `Attribute[dict[str, klass]]`    |
| `_makeUnionClassAttributeFromTypeKey(type_key, default_type, v, (KlassA, "A"), (KlassB, "B"), …)` | `Attribute[KlassA \| KlassB]`    |
| `_makeUnionClassAttributeFromTypeKeyAndValueKey(type_key, value_key, default_type, v, …)`         | `Attribute[KlassA \| KlassB]`    |

The union helpers select the concrete class by reading a discriminator key inside the JSON value. Use them when a field
can be one of several types at runtime — e.g. `creator` can be a `NamedUser` or an `Organization` depending on
`value["type"]`:

```python
self._creator = self._makeUnionClassAttributeFromTypeKey(
    "type",  # discriminator key in the JSON object
    "User",  # default type name if key is absent
    attributes["creator"],  # the raw value dict
    (github.NamedUser.NamedUser, "User"),
    (github.Organization.Organization, "Organization"),
)
```

`_makeUnionClassAttributeFromTypeKeyAndValueKey` is the same but the discriminator and the payload live at different
keys within the outer dict.

---

## HTTP Layer — Requester

`github/Requester.py` owns all HTTP communication.

- Uses `requests` with pooled sessions; retry behavior configured via `github/GithubRetry.py`.
- Primary call used by PyGithub objects: `requestJsonAndCheck(verb, url, parameters, headers, input)` →
  `(headers, data)`.
- Tracks rate limit (`rate_limiting`, `rate_limiting_resettime`) and OAuth scopes from response headers.
- Supports conditional GET with ETag / If-Modified-Since (`update()` on `CompletableGithubObject`).

**Authentication** (`github/Auth.py`):

| Auth class                 | Use case                                                    |
|----------------------------|-------------------------------------------------------------|
| `Auth.Token`               | Personal access token or fine-grained token                 |
| `Auth.Login`               | Username + password (deprecated by GitHub)                  |
| `Auth.AppAuth`             | GitHub App — signs JWTs, auto-refreshes installation tokens |
| `Auth.AppInstallationAuth` | App installation token                                      |
| `Auth.AppUserAuth`         | OAuth user-to-server token for Apps                         |

---

## Pagination

`github/PaginatedList.py` — one class handles both REST and GraphQL pagination.

- **REST**: follows `Link` headers (`next`, `prev`, `last`).
- **GraphQL**: cursor-based via `pageInfo.hasNextPage` / `endCursor`.
- Pages are fetched lazily on iteration or index access.
- `totalCount` fires a `per_page=1` probe to get the count without fetching all items.
- `reversed` property returns a backward-iterating list (REST only).
- `get_page(n)` fetches an arbitrary page directly (REST only).

---

## Optional Parameters — `NotSet` vs `None`

PyGithub distinguishes between "the caller did not pass this parameter" and "the caller explicitly passed `None`":

```python
# Opt[T] = T | _NotSetType
def create_issue(
    self,
    title: str,
    body: Opt[str] = NotSet,  # omitted → not sent to API
    assignee: Opt[str] = NotSet,  # None → sent as null, clearing the field
) -> Issue: ...
```

`NotSet` parameters are excluded from the request payload entirely. `None` is serialized and sent.

---

## Exception Hierarchy

All exceptions are defined in `github/GithubException.py`.

```
Exception
├── GithubException(status, data, headers)   — base for all HTTP errors
│   ├── BadCredentialsException              — 401/403 auth failure
│   ├── UnknownObjectException               — 404
│   ├── RateLimitExceededException           — 403 rate limit
│   ├── TwoFactorException                   — 401 + OTP required
│   └── BadUserAgentException                — 403 bad user-agent
├── BadAttributeException                    — type mismatch parsing an API response field
└── IncompletableObject                      — lazy object has no URL to complete against
```

---

## Documentation Conventions

- **`:calls:` tag**: every public method that makes an API request documents it:
  ```python
  def get_issues(self) -> PaginatedList[Issue]:
      """
      :calls: `GET /repos/{owner}/{repo}/issues <https://docs.github.com/...>`_
      """
  ```
- **Type hints**: full PEP 484 annotations on all public APIs.
- **`TYPE_CHECKING` guards**: used for imports that would cause circular dependencies.
- **No `.pyi` stubs**: types live directly in source files.
- **Examples must work**: example code in docstrings (`.. code-block:: python`, inline ``` ``…`` ``` snippets),
  in deprecation / warning / exception messages ("Use `Organization.get_hook(id).edit(…)` instead"), and in `doc/`
  must be valid Python that works against the current API: correct syntax, existing method and property names,
  correct argument names and types, correct return types (e.g. iterating a `PaginatedList`, not indexing a `dict`).
  Where possible, examples in `doc/examples/` are backed by a test.

---

## Pickling

PyGithub objects can be pickled, either directly with `pickle` or via `Github.dump(obj, file)` /
`Github.load(file)` (`github/MainClass.py`; the latter only pickles `(class, raw_data, raw_headers)`).
`tests/Pickle.py` covers `Github`, PyGithub objects (e.g. `Repository`), `PaginatedList` and all `Auth` classes.

- **Pickling must not break**: every PyGithub class, `Github`, `Requester`, `PaginatedList` and every `Auth` class
  must remain picklable. Do not store unpicklable state (locks, sessions / connections, open files, generators,
  lambdas or locally defined functions, module objects) in their attributes. If such state is unavoidable, exclude it
  in `__getstate__` and recreate it in `__setstate__`, as `Requester` does for `__connection_lock`, `__connection`
  and `__custom_connections`.
- New `Auth` classes must be added to `Pickle.auths` (`testPickleAuthSetup` fails otherwise); new kinds of objects
  that hold extra runtime state should get a pickle round-trip test in `tests/Pickle.py`.
- **Compatibility across releases is not guaranteed**: unpickling an object that was pickled with a different
  PyGithub release may break (private attribute names and class layouts change between releases). Changes that only
  affect unpickling of objects pickled by another release are therefore acceptable.

---

## Testing

Tests live in `tests/`, one file per PyGithub class (e.g. `tests/Repository.py`).

- Framework: `unittest` + [`vcrpy`](https://github.com/kevin1024/vcrpy) for HTTP mocking, via a custom serializer
  (`tests/VcrSerializer.py`) that reads/writes the pre-existing `tests/ReplayData/*.txt` cassette format unchanged.
- Shared base class: `tests/Framework.py`.
- A frame-buffer debug system in `Requester` (`NEW_DEBUG_FRAME()`) records request/response pairs for low-level
  inspection.

Running the suite:

```bash
pytest tests/
```

### Test Conventions

- **Where tests go**: tests for `github/Foo.py` go into the existing `tests/Foo.py`, inside the existing test class
  (e.g. `class Foo(Framework.TestCase)`). Methods that live on a class are tested in that class' test file (e.g.
  `WorkflowRun.get_attempt` → `tests/WorkflowRun.py`).
- **New test classes / files only for new or untested PyGithub classes**: a new `tests/Foo.py` with
  `class Foo(Framework.TestCase)` is created only when `github/Foo.py` is a new PyGithub class or has no tests yet.
  Do not create per-issue / per-pull-request test classes or files (`tests/Issue3278.py`,
  `tests/PullRequest2989.py`, `class InstallationGetRepos`). The existing legacy files of that kind
  (`tests/Issue*.py`, `tests/PullRequest1168.py`, …) are not a pattern to follow and should not be extended.
- **Naming**: test methods are camelCase and start with `test` (`testGetReposForCodeSecurityConfig`, not
  `test_get_repos_for_code_security_config`). The method name determines the replay data file name.
- **Prefer extending existing tests**: if an existing test (e.g. `testCreateTeamWithAllArguments`) already covers the
  method, extend its assertions and replay data rather than adding a near-duplicate test.
- **Assert the effect, not a proxy**: assert the attribute that the change is about (e.g.
  `pull.head.repo.full_name` for a new `head_repo` argument, not `pull.id`), that a reorder actually changed the
  order, that a removal actually removed, and every field of a newly introduced result class.
- **Exceptions**: assert both status and message:
  ```python
  with self.assertRaises(github.GithubException) as raisedexp:
      repo.merge_upstream("doesNotExist")
  self.assertEqual(raisedexp.exception.status, 404)
  self.assertEqual(raisedexp.exception.message, "Branch not found")
  ```
- Use `assertIsNone(x)` rather than `assertEqual(x, None)`, `assertListKeyEqual(...)` for lists, and index access
  (`items[0]`) rather than `for … : … break`. No `print()` statements in tests.
- **Avoid needless requests**: obtain parent objects lazily (`self.g.get_repo("PyGithub/PyGithub", lazy=True)`) so
  that `setUp` / tests do not record GET requests that are irrelevant to what is being tested.
- **Reusing replay data**: use `with self.replayData("Other.testName.txt"):` to reuse another test's replay data.
  Symlinks do not work on Windows (CI runs tests on Windows).
- **Platform independence**: tests run on Linux, macOS and Windows; e.g. do not re-open a
  `tempfile.NamedTemporaryFile` while it is still open (use `tempfile.TemporaryDirectory()` instead).
- **Auth modes**: tests use token auth by default; set `self.authMode = "jwt" | "app" | "none"` before
  `super().setUp()` when needed (see `doc/testing.rst`).

### Replay Data

Every test that talks to the GitHub API has a replay data file `tests/ReplayData/<TestClass>.<testMethod>.txt`
(`<TestClass>.setUp.txt` for `setUp`). Requests are replayed **in recorded order**, and a test fails if not all
recorded requests were used ("Not all replay data was used"). Each request is a block of lines:

```
https                                  # protocol
GET                                    # verb
api.github.com                         # host
None                                   # port
/repos/PyGithub/PyGithub/pulls?per_page=1   # path + query
{'Authorization': 'token private_token_removed', 'User-Agent': 'PyGithub/Python'}   # request headers
None                                   # request body (JSON) or None
200                                    # status
[('Date', '…'), …]                     # response headers
{"id": 1, …}                           # response body
                                       # empty line
```

Rules:

- Record with `pytest -k Class.testMethod --record` (needs `GithubCredentials.py`, see `doc/testing.rst`); commit the
  resulting files. Hand-crafted or hand-edited replay data is acceptable for small changes, but it must be consistent
  with what the code sends.
- **Code changes that alter requests require replay data changes**: e.g. encoding booleans as `true`/`false` in query
  strings, removing a default request body field, renaming a parameter, or fixing a typo in a string that is part of
  a request or an asserted response. Edit the existing files by hand in such cases.
- **Anonymise / normalise**: organisations are renamed to `BeaverSoftware` (the org used by `tests/Organization.py`),
  repositories to the test class' established repo (typically `PyGithub/PyGithub`), and the `Authorization` header is
  normalised according to the auth mode (`token private_token_removed`, `Basic login_and_password_removed`,
  `Bearer jwt_removed`). Organisation ids in `Link` headers should be consistent with the renamed organisation.
- Remove requests that are not needed by the test (e.g. a GET of the organisation when it can be obtained lazily).
- When a test is renamed, rename its replay data file as well. Revert unrelated changes to shared files such as
  `<Class>.setUp.txt`.

---

## File Organization

```
github/
├── GithubObject.py          # Base classes, attribute helpers, NotSet sentinel
├── MainClass.py             # Github entry point
├── Requester.py             # HTTP layer
├── PaginatedList.py         # Pagination abstraction
├── Auth.py                  # Authentication strategies
├── GithubException.py       # Exception hierarchy
├── GithubRetry.py           # Retry configuration
├── Consts.py                # Shared constants (headers, default values)
│
├── Repository.py            # ~150 more PyGithub classes, one per file
├── Issue.py
├── PullRequest.py
├── NamedUser.py
├── AuthenticatedUser.py
├── Organization.py
├── Commit.py
├── Workflow.py
│   …
tests/
├── Framework.py             # Shared test base class
├── Repository.py            # Per-object test files
├── Issue.py
│   …
```

---

## Naming and Structuring Conventions

### File Layout (top to bottom)

Every PyGithub class file follows this exact order:

```
1. Copyright/license block
2. from __future__ import annotations
3. Standard library imports — alphabetical (datetime, urllib.parse, …)
4. from typing import TYPE_CHECKING, Any   (or just Any if no TYPE_CHECKING needed)
5. import github.X   — one per class used at runtime in _useAttributes (alphabetical)
6. from github.GithubObject import Attribute, <BaseClass>, NotSet[, Opt, is_optional, …]
7. from github.X import X   — direct imports with no circular-dependency risk
8. if TYPE_CHECKING:
       from github.X import X   — type-annotation-only imports (avoids circular imports)
9. (blank line)
10. class definition
```

### Class Docstring

```python
class Foo(CompletableGithubObject):
    """
    This class represents <plural resource description>.

    The reference can be found here
    https://docs.github.com/en/rest/...

    The OpenAPI schema can be found at

    - /components/schemas/schema-name

    """
```

A class that maps to more than one OpenAPI schema lists all of them:

```
    - /components/schemas/hook
    - /components/schemas/org-hook
```

### Internal Class Order

The order of members of a PyGithub class is enforced by `scripts/sort_class.py` (CI job "sort classes" in
`.github/workflows/auto-fix.yml` / `.github/actions/sort-classes`, see also the `sorted-classes` skill). A class body
is laid out as:

```
1. prolog           class docstring, class-level constants / annotations — everything before the first `def`
2. __init__()       only if the class overrides the constructor
3. _initAttributes()
4. dunder methods   alphabetical: __eq__, __hash__, __repr__, __str__, …
5. @property        alphabetical by property name
6. other methods    public and private methods, in the order chosen by the author (NOT sorted)
7. _useAttributes()
8. epilog           anything after the last `def`
```

`_useAttributes` is always the last method in the class.

Exact rules implemented by the script:

- **Which classes**: only classes whose *direct* base class name ends with `GithubObject` (`GithubObject`,
  `CompletableGithubObject`, `NonCompletableGithubObject`, `CompletableGithubObjectWithPaginatedProperty`, also when
  written as `github.GithubObject.X`). Subclasses of other PyGithub classes (e.g. `SubIssue(Issue)`,
  `RepositoryAdvisory(AdvisoryBase)`, `IssueSearchResult(Issue)`) are **not** touched by the script — they must
  follow the same order by hand.
- **One block of methods**: all `def`s of the class must form one consecutive block. A class-level statement between
  two methods makes the script fail ("There is no consecutive block of functions"); put class-level constants before
  the first method.
- **Unique names**: `__init__`, `_initAttributes` and `_useAttributes` may each exist only once.
- **Properties** are methods decorated with a plain `@property` (also when stacked with other decorators, e.g.
  `@property` + `@deprecated(...)`; deprecated properties stay in alphabetical position, they are not moved to the
  end). `@x.setter` methods are not recognised as properties and end up among the other methods.
- **Sort key** is the plain Python string order of the name (ASCII): uppercase < `_` < lowercase, so `repo_name`
  comes before `repository`, and `created_at` before `creator`.
- **`_initAttributes`**: the block from the first to the last annotated assignment (`self._x: Attribute[T] = NotSet`)
  is sorted by attribute name. Keep all attribute initialisations as one contiguous block of annotated assignments
  (no un-annotated assignments or other statements in between); statements before the first or after the last one
  stay where they are.
- **`_useAttributes`**: the block from the first to the last top-level `if` statement is sorted by the key in the
  condition: `if "key" in attributes:` and `if "key" in attributes and …:` sort by `"key"`. An `elif` / `else` belongs
  to its `if` and moves with it. Statements before the first `if` (e.g. `super()._useAttributes(attributes)`) stay
  first.
- **Other methods are never reordered** by the script. New methods should be placed next to the methods they relate
  to (see "Public method ordering" below), e.g. `get_x` / `create_x` / `delete_x` together, rather than appended at
  the end of the class.

Run `python scripts/sort_class.py --dry-run openapi.index <ClassName> …` to see the diff the script would apply
(`openapi.index` is created by `python scripts/openapi.py index github openapi.index`). Contributors can run the
`auto-fix` workflow on their fork to apply the sort (and pre-commit fixes) to their branch.

**Dunder methods** are Python special methods (`__name__`). All dunder methods of a class go immediately after
`_initAttributes()`, in alphabetical order. The most common ones in PyGithub classes:

| Method                | When to add                                                                            |
|-----------------------|----------------------------------------------------------------------------------------|
| `__eq__(self, other)` | Custom equality (e.g. `NamedUser` compares by `login` and `id`)                        |
| `__hash__(self)`      | Always add alongside `__eq__`                                                          |
| `__repr__(self)`      | Present in every class — use `self.get__repr__({"key": self._key.value})`              |
| `__str__(self)`       | When a human-readable one-line string is useful (e.g. `CodeScanAlertInstanceLocation`) |

Example with several dunders, alphabetically ordered:

```python
def _initAttributes(self) -> None:
    self._id: Attribute[int] = NotSet
    self._login: Attribute[str] = NotSet


def __eq__(self, other: Any) -> bool:
    return isinstance(other, type(self)) and self.login == other.login and self.id == other.id


def __hash__(self) -> int:
    return hash((self.id, self.login))


def __repr__(self) -> str:
    return self.get__repr__({"login": self._login.value})
```

**Public method ordering**

Classes with many methods sometimes group related operations together as a cluster placed after the main methods — for
example, all reaction methods (`get_reactions` → `create_reaction` → `delete_reaction`) or all sub-issue methods appear
as a block.

### `_initAttributes`

All private attribute fields, **alphabetical**, each typed and initialised to `NotSet`:

```python
def _initAttributes(self) -> None:
    self._created_at: Attribute[datetime] = NotSet
    self._id: Attribute[int] = NotSet
    self._name: Attribute[str] = NotSet
    self._url: Attribute[str] = NotSet
```

### `__repr__`

Uses `self.get__repr__({...})` with the most identifying fields. Access the raw `._attr.value` directly — not the
property — to avoid triggering lazy completion:

```python
def __repr__(self) -> str:
    return self.get__repr__({"id": self._id.value})


# multiple identifying fields:
def __repr__(self) -> str:
    return self.get__repr__({"id": self._id.value, "state": self._state.value})
```

### `@property` Accessors

For `CompletableGithubObject` — always call `_completeIfNotSet` before returning:

```python
@property
def name(self) -> str:
    self._completeIfNotSet(self._name)
    return self._name.value
```

For `NonCompletableGithubObject` — return value directly (no lazy loading):

```python
@property
def name(self) -> str:
    return self._name.value
```

Older files have a `:type:` docstring on each property; newer files omit it.

### Method Docstrings

Every method that makes an HTTP call has a `:calls:` docstring. Methods that take parameters and return something also
have `:param:` and `:rtype:` lines:

```python
def create_issue(self, title: str, body: Opt[str] = NotSet) -> Issue:
    """
    :calls: `POST /repos/{owner}/{repo}/issues <https://docs.github.com/...>`_
    :param title: string
    :param body: string
    :rtype: :class:`github.Issue.Issue`
    """
```

Methods that cover multiple endpoints (e.g. `delete()` on a class that is shared between repo-level and org-level
secrets) list multiple `:calls:` lines.

### Parameter Validation (`assert`)

Every public method validates its arguments with `assert` statements at the top of the body — one `assert` per
parameter, before any other logic:

```python
def edit(self, sha: str, force: Opt[bool] = NotSet) -> None:
    assert isinstance(sha, str), sha  # required param
    assert is_optional(force, bool), force  # Opt[T] param
```

Validation helpers (all imported from `github.GithubObject`):

| Situation                      | Helper                                    |
|--------------------------------|-------------------------------------------|
| Required, single type          | `assert isinstance(v, SomeType), v`       |
| Optional (`Opt[T]`)            | `assert is_optional(v, SomeType), v`      |
| Optional list (`Opt[list[T]]`) | `assert is_optional_list(v, SomeType), v` |
| Enum string                    | `assert v in ["a", "b"], "msg"`           |

Two additional guards are available for branching on `NotSet` inside method bodies (not for assertions):

```python
if is_defined(value):  # True when value is not NotSet — narrows type to T
    ...
if is_undefined(value):  # True when value is NotSet
    ...
```

### Building Request Bodies

Use `NotSet.remove_unset_items({...})` to strip any `NotSet` values from the dict before passing to the requester:

```python
post_parameters = NotSet.remove_unset_items(
    {
        "title": title,
        "body": body,  # omitted if NotSet
    }
)
headers, data = self._requester.requestJsonAndCheck("POST", self.url, input=post_parameters)
```

If all parameters are required (no `NotSet`), build the dict directly without `remove_unset_items`.

### Making HTTP Calls

Use `requestJsonAndCheck` for all calls that should raise on HTTP errors:

```python
headers, data = self._requester.requestJsonAndCheck("DELETE", self.url)
headers, data = self._requester.requestJsonAndCheck("PATCH", self.url, input=params)
headers, data = self._requester.requestJsonAndCheck("POST", f"{self.url}/comments", input=params)
```

Use `requestJson` (without `AndCheck`) only when you need to inspect the raw status code yourself, e.g. to return a
`bool`:

```python
status, _, _ = self._requester.requestJson("PATCH", self.url, input=params)
return status == 204
```

### After `edit()` — updating the object in place

After a PATCH call that returns the updated resource, call `_useAttributes` then `_set_complete`:

```python
headers, data = self._requester.requestJsonAndCheck("PATCH", self.url, input=params)
self._useAttributes(data)
self._set_complete()
```

### Constructing and Returning New Instances

**`get_X(id)` methods — lazy-safe construction (no API call in the method)**

A `get_X(id)` method must construct the object from the URL alone and let the constructor decide whether to fetch:

Assert the type of every variable before using it in the URL. String arguments must also be percent-encoded with
`urllib.parse.quote(name, safe="")` so that special characters (spaces, slashes, …) do not corrupt the path:

```python
def get_label(self, name: str) -> Label:
    assert isinstance(name, str), name
    label_name = urllib.parse.quote(name, safe="")
    url = f"{self.url}/labels/{label_name}"
    return github.Label.Label(self._requester, url=url)
```

**Do not call `requestJsonAndCheck` inside a `get_X` method** and then pass the result to the constructor. That would
bypass lazy mode entirely and always issue a GET.

If a few attributes are already known (e.g. derived from the URL or passed as arguments), pre-populate them to avoid
redundant fetching in non-lazy mode:

```python
url = f"{self.url}/git/refs/{ref}"
return github.GitRef.GitRef(self._requester, url=url, attributes={"ref": ref})
```

**`create_X` / `edit` / other methods that already have the full response**

When the method has made an API call and holds the complete response, pass it directly and mark the object complete:

```python
headers, data = self._requester.requestJsonAndCheck("POST", f"{self.url}/issues", input=params)
return github.Issue.Issue(self._requester, headers, data, completed=True)
```

**Partially populated objects from a known-incomplete response**

When a response is available but known to be a summary (e.g. a file entry inside a directory listing), pass
`completed=False` so the object will fetch itself on next attribute access:

```python
github.ContentFile.ContentFile(self._requester, headers, item, completed=False)
```

**`PaginatedList` returns**

```python
return PaginatedList(
    github.Foo.Foo,
    self._requester,
    f"{self.url}/foos",
    url_parameters,  # query params dict, or None
)
```

When the API returns items under a JSON key other than the default, pass `list_item="key"`. When items need extra
attributes injected (e.g. a parent URL), pass `attributesTransformer=PaginatedList.override_attributes({...})`.

### `_useAttributes`

Process every attribute key **alphabetically**, guarding with `if "key" in attributes:`:

```python
def _useAttributes(self, attributes: dict[str, Any]) -> None:
    if "id" in attributes:  # pragma no branch
        self._id = self._makeIntAttribute(attributes["id"])
    if "name" in attributes:  # pragma no branch
        self._name = self._makeStringAttribute(attributes["name"])
    if "url" in attributes:  # pragma no branch
        self._url = self._makeStringAttribute(attributes["url"])
```

The `# pragma no branch` comment suppresses coverage warnings for branches that can't be reached in practice. It appears
consistently in older files; some newer files omit it.

When a key is absent but can be derived from another (e.g. extracting an id from a URL), use `elif`:

```python
if "id" in attributes:  # pragma no branch
    self._id = self._makeIntAttribute(attributes["id"])
elif "url" in attributes and attributes["url"]:
    id = attributes["url"].split("/")[-1]
    if id.isnumeric():
        self._id = self._makeIntAttribute(int(id))
```

### Module Exports

Only a small set of fundamental classes and exceptions are exported from `github/__init__.py`. PyGithub classes (
`Issue`, `Autolink`, etc.) are **not** directly exported. Users receive instances from method calls; they do not
`import github.Issue` directly. When referencing a PyGithub class from within the package at runtime, use the
`github.<File>.<Class>` form (see [Type Annotations vs. Runtime References](#type-annotations-vs-runtime-references-the-two-import-pattern)).

### Type Annotations vs. Runtime References (the Two-Import Pattern)

Every module begins with `from __future__ import annotations`, so **all type annotations are lazy
strings** — read by the type checker (mypy) and linters, but never evaluated at runtime. This splits
every reference to another PyGithub class into two cases, each with its own import:

| Use | What it covers | Form | Import |
| --- | --- | --- | --- |
| **Runtime** | constructor calls, `isinstance`, `_makeClassAttribute`, `is_optional_list`, base classes — any executed expression | `github.<File>.<Class>` | `import github.<File>` (module level) |
| **Annotation only** | parameter / return / attribute types — checked, never executed | `<Class>` | `from github.<File> import <Class>` under `if TYPE_CHECKING:` |

`<File>` is the module (the `.py` file name without extension) and `<Class>` is the class defined in
it. **The two are often but not always equal** — a single file may define several classes
(`HookDelivery.py` defines both `HookDelivery` and `HookDeliverySummary`; `NamedUser.py` defines
`NamedUser` and `OrganizationInvitation`; `Repository.py` also defines `RepositorySearchResult`). So
qualify the runtime reference with the *file*, not by repeating the class name.

Referencing classes by module path (`github.<File>.<Class>`) at runtime instead of importing the name
directly is what avoids the circular-import errors that arise when two classes reference each other.

```python
import github.HookDelivery  # runtime: used as github.HookDelivery.HookDelivery / .HookDeliverySummary

if TYPE_CHECKING:
    from github.HookDelivery import HookDelivery, HookDeliverySummary  # type-checker only: annotations
```

```python
# runtime — full module path (note the class differs from the file here):
return [github.HookDelivery.HookDeliverySummary(self._requester, headers, attr) for attr in data]


# annotation — short name from the TYPE_CHECKING import:
@property
def delivery(self) -> HookDelivery:
    self._completeIfNotSet(self._delivery)
    return self._delivery.value
```

**The rule (enforced):** a module that defines a PyGithub class (anything derived from
`GithubObject`) must not import another PyGithub class with `from github.SomeFile import SomeClass`
outside the `if TYPE_CHECKING:` block.

**The one exception — base classes.** A class you inherit from must be a real object at
class-definition time, so it *has* to be a runtime import — you cannot subclass a name that only
exists under `TYPE_CHECKING`:

```python
from github.GithubObject import CompletableGithubObject  # base class — runtime import required
from github.AdvisoryBase import AdvisoryBase  # domain base class — same
```

Infrastructure that is not a `GithubObject` data class (e.g. `PaginatedList`, `Requester`, `Consts`,
and the `Attribute` / `NotSet` helpers from `GithubObject`) is likewise imported normally and used at
runtime.

This convention applies to every module that references PyGithub classes, including non-`GithubObject`
entry points such as `Github` in `MainClass.py`.

---

## API Design Conventions

### Where a method belongs

A method that operates on a specific resource lives on the PyGithub class of that resource, not on its parent. The
parent only gets the `get_X` / `get_Xs` / `create_X` accessors:

| Endpoint                                                     | Method                                    |
|--------------------------------------------------------------|-------------------------------------------|
| `PUT .../environments/{env}/deployment-branch-policies/{id}` | `DeploymentBranchPolicy.edit(...)`        |
| `DELETE .../deployment-branch-policies/{id}`                 | `DeploymentBranchPolicy.delete()`         |
| `GET .../actions/runs/{run_id}/attempts/{attempt}`           | `WorkflowRun.get_attempt(attempt_number)` |
| `GET .../actions/jobs/{job_id}`                              | `Repository.get_workflow_job(id)`         |

The id of the object the method lives on is not a parameter (it is part of `self.url`).

### Method names

- Use the established verbs: `get_x(id)` / `get_xs()` (never `list_xs`), `create_x`, `edit` / `edit_x` (never
  `update_x`), `delete` / `delete_x`, `add_x` / `remove_x`, `add_to_x` / `remove_from_x`.
- Use the plural when a method acts on several items (`add_seats(usernames)`, `remove_seats(...)`).
- Name parameters after the GitHub API (e.g. `org`, as in the REST docs), and keep names consistent across classes.
  Where the same operation exists on several classes, the name may reflect the context
  (`Organization.attach_security_config_to_repositories(...)` vs. `Repository.attach_security_config(...)`).

### Arguments

- Accept either a PyGithub object or its identifier rather than adding a second method:
  `add_sub_issue(sub_issue: int | Issue)`, `create_review_comment(commit: Commit | str, ...)`. Check with
  `assert isinstance(x, (github.Issue.Issue, int)), x`.
- Use precise types (`Opt[dict[str, Any]]`, `Opt[bool]` rather than `Opt[str]` holding `"true"`). Convert to the wire
  format inside the method.
- Do not hard-code lists of allowed values for API enums (states, secret types, …) — they go out of date quickly; the
  GitHub API validates values and returns a meaningful error.

### Return values

- When the API returns a useful payload, return a PyGithub class rather than `None` or a raw `dict` (e.g.
  `Repository.merge_upstream` → `MergedUpstream`, `GitCommit.verification` → `GitCommitVerification`). Payloads
  without their own endpoint become a `NonCompletableGithubObject`.
- Methods that only perform an action (`delete_x`, `disable`, …) return `None`, not a `bool` or a `PaginatedList`.
  Rely on exceptions to signal failures.
- A method that explicitly calls the API must always make the call; it must not fall back to an already known
  property value (callers can do that themselves). If the response updates known state, update the attributes.
- When a value can be unknown (not fetched yet), type it as `T | None` so that "unknown" is distinguishable from
  `False` / `0`.
- Nullable API fields are typed `Attribute[T | None]` and the property returns `T | None`.

### Backward compatibility

PyGithub is widely used; changes must not break user code:

- New parameters of existing public methods are appended at the **end** of the parameter list (callers may pass
  arguments positionally) unless they are keyword-only.
- Do not rename existing parameters (callers may pass them by keyword). If a rename is desirable, leave a comment like
  `# v3: sha should be renamed to ref, which breaks user code like get_commit(sha=...)`.
- Changing a default that is sent to the API (e.g. removing a default `event="COMMENT"`) changes behaviour; it needs
  justification against the GitHub API docs and adjusted replay data.
- **Split breaking changes out**: a PR that would break user code (removed / renamed methods, properties or
  parameters, changed return types, changed parameter order or semantics) should, wherever possible, be split into:
  1. a PR that adds the new API and **deprecates** the old one, keeping the old one working, and
  2. a subsequent PR that removes the deprecated API / makes the breaking change, merged for a later major release.

  Only when no non-breaking intermediate step is possible does a breaking change go in directly; it is then listed
  under "Breaking Changes" in `doc/changes.rst` together with "code like … should be replaced with …" examples.

### Deprecations

- Deprecate methods, properties and classes with `@deprecated("<alternative>")` from `typing_extensions` (stacked
  below `@property` for properties). Deprecate parameters (or individual values) with
  `warnings.warn("<alternative>", category=DeprecationWarning, stacklevel=2)` inside the method, so the warning points
  at the caller's code.
- **Every deprecation names an alternative** in its message, and that alternative must provide **identical** or **as
  similar as possible** behaviour — same data, same number of API calls where it matters, same laziness. Where the
  alternative differs (e.g. needs an extra GET), the deprecation (and changelog) explains how to get the old
  behaviour, e.g. via a lazy `Github` instance:

  ```python
  @deprecated("Use Organization.get_hook(id).edit(…) instead")
  def edit_hook(self, id: int, ...) -> Hook: ...


  # equivalent without the extra GET of the hook:
  Github(..., lazy=True).get_organization(...).get_hook(id).edit(...)
  ```

  Messages like "This is deprecated" without an alternative are not acceptable. If no alternative exists yet, add it
  in the same PR.
- The deprecated code keeps working unchanged (ideally implemented by delegating to the alternative) and keeps its
  tests; tests of deprecated API assert the warning (`with self.assertWarns(DeprecationWarning)` /
  `self.assertWarning(...)`).
- **The PR description enumerates all deprecations** (and any breaking changes), each with its alternative. These
  entries become the "Deprecations" / "Breaking Changes" sections in `doc/changes.rst`, e.g.:

  ```
  Deprecations
  * Method `Organization.edit_hook` is deprecated, use `Organization.get_hook(id).edit(…)` instead.
  * Method `Issue.assignee` and parameter `Issue.edit(assignee=…)` are deprecated,
    use `Issue.assignees` and `Issue.edit(assignees=…)` instead.
  ```

### Consistency across the code base

When fixing a bug pattern (e.g. URL-encoding with `urllib.parse.quote`, `del headers[...]` side effects,
`warnings.warn` without `stacklevel`), search the code base for all other occurrences and fix them in the same PR.

---

## Quick Reference: Adding a New PyGithub Class

1. Create `github/MyThing.py` inheriting `CompletableGithubObject` (or `NonCompletableGithubObject` if the class has no
   dedicated endpoint and only appears embedded in other responses).
2. Implement `_initAttributes()` — set every attribute to `NotSet`.
3. Implement `_useAttributes()` — parse each key with the appropriate `_makeXAttribute()` helper.
4. Add a `@property` per attribute calling `_completeIfNotSet()` before returning `.value`.
5. Add factory/accessor methods to `Github`, `Repository`, or the relevant parent class.
6. Add a corresponding `tests/MyThing.py` using `tests/Framework.py` as the base.
