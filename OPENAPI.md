# PyGithub ↔ GitHub OpenAPI Spec

A guide to navigating the GitHub OpenAPI specification alongside the PyGithub codebase — how to look up schemas, paths, and understand the mapping between JSON and Python.

---

## The JSON File

```
api.github.com.2022-11-28.20251114T1100.json
```

This is the full GitHub REST API OpenAPI 3.0 specification. It contains **737 paths** and **875 schemas**. The filename encodes the GitHub API version (`2022-11-28`) and the spec generation date.

---

## Top-Level Structure

```
{
  "paths": {
    "/repos/{owner}/{repo}/issues": { ... },   // 737 entries
    ...
  },
  "components": {
    "schemas": {                                // 875 entries
      "issue": { ... },
      "git-ref": { ... },
      ...
    },
    "parameters": { ... },   // reusable path/query params referenced via $ref
    "responses":  { ... },   // reusable HTTP responses referenced via $ref
    "examples":   { ... }    // reusable response examples referenced via $ref
  }
}
```

---

## Path Entries

Each key under `.paths` is a URL template, e.g. `/gists/{gist_id}/comments/{comment_id}`. The value is an object keyed by HTTP verb (`get`, `post`, `patch`, `put`, `delete`). Each verb object contains:

| Field | Description |
|---|---|
| `summary` | Short human-readable title |
| `description` | Longer description (may include media-type notes) |
| `operationId` | Unique identifier in `"category/operation-name"` form (e.g. `gists/update-comment`) |
| `tags` | Array of category tags (e.g. `["gists"]`) |
| `externalDocs.url` | Link to the GitHub REST API documentation page |
| `parameters` | Array of path/query parameters, often `$ref` to `.components.parameters` |
| `requestBody` | (POST/PATCH/PUT) Inline JSON Schema describing the request body |
| `responses` | Keyed by HTTP status code; each `200`/`201` entry has a schema ref for the response body |
| `x-github` | Extension object: `category`, `subcategory`, `githubCloudOnly`, `enabledForGitHubApps` |

### Example: PATCH `/gists/{gist_id}/comments/{comment_id}`

```json
"patch": {
  "summary": "Update a gist comment",
  "operationId": "gists/update-comment",
  "externalDocs": { "url": "https://docs.github.com/rest/gists/comments#update-a-gist-comment" },
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "properties": { "body": { "type": "string" } },
          "required": ["body"]
        }
      }
    }
  },
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "schema": { "$ref": "#/components/schemas/gist-comment" }
        }
      }
    }
  }
}
```

---

## Schema Entries

Each key under `.components.schemas` is a schema name (kebab-case). The value is an OpenAPI Schema Object:

| Field | Description |
|---|---|
| `title` | Human-readable name |
| `description` | What the object represents |
| `type` | Usually `"object"` for domain types; or `"string"` / `"integer"` etc. for primitives |
| `properties` | Object fields, each with their own type/format/description |
| `required` | List of property names that are always present |

### Property types

| JSON Schema | Format | PyGithub helper |
|---|---|---|
| `"type": "string"` | — | `_makeStringAttribute` |
| `"type": "integer"` | — | `_makeIntAttribute` |
| `"type": "boolean"` | — | `_makeBoolAttribute` |
| `"type": "number"` | — | `_makeFloatAttribute` |
| `"type": "string"` | `"date-time"` | `_makeDatetimeAttribute` |
| `"type": "integer"` | (Unix timestamp) | `_makeTimestampAttribute` |
| `"type": "object"` | — | `_makeDictAttribute` or a dedicated class |
| `"type": "array"`, `items.$ref` | — | `_makeListOfClassesAttribute(Klass, v)` |
| `"type": "array"`, `items.type: string` | — | `_makeListOfStringsAttribute` |
| `"type": "array"`, `items.type: integer` | — | `_makeListOfIntsAttribute` |
| `"$ref": "#/components/schemas/X"` | — | `_makeClassAttribute(X, v)` |

### `$ref` — reusing schemas

Schemas reference each other with `"$ref": "#/components/schemas/schema-name"`. There are three common patterns:

1. **Nested object** — a field whose value is another full domain object:
   ```json
   "user": { "$ref": "#/components/schemas/nullable-simple-user" }
   ```
   → `_makeClassAttribute(github.NamedUser.NamedUser, attributes["user"])`

2. **Enum** — a string field whose allowed values are defined in a shared schema:
   ```json
   "author_association": { "$ref": "#/components/schemas/author-association" }
   ```
   where `author-association` is `{ "type": "string", "enum": [...] }`.
   → `_makeStringAttribute` (PyGithub does not enforce the enum, just stores the string)

3. **Inheritance via `allOf`** — a schema that extends another:
   ```json
   { "allOf": [ { "$ref": "#/components/schemas/base-schema" }, { "type": "object", "properties": { ... } } ] }
   ```
   → In PyGithub, properties from all members are merged into one class.

---

## Scripts

Two helper scripts extract information from the JSON file. Both read the JSON from **stdin** and take one argument.

### `scripts/get-openapi-path.sh <path>`

Extracts a single path entry.

```bash
cat api.github.com.*.json | scripts/get-openapi-path.sh '/repos/{owner}/{repo}/git/refs/{ref}'
```

Internally runs: `jq '.paths."/repos/{owner}/{repo}/git/refs/{ref}"'`

### `scripts/get-openapi-schema.sh <schema-path>`

Extracts a schema by its JSON Pointer path (the value in `"The OpenAPI schema can be found at"` comments).

```bash
cat api.github.com.*.json | scripts/get-openapi-schema.sh /components/schemas/autolink
```

The script transforms `/components/schemas/autolink` into a jq expression by replacing the leading `/` with `."` and all subsequent `/` with `"."`, producing `."components"."schemas"."autolink"`, then runs `jq '."components"."schemas"."autolink"'`.

The schema path argument must start with `/` (not `#/`). Strip the leading `#` from `$ref` values before passing them to the script.

---

## PyGithub ↔ OpenAPI Mapping

### Class → Schema

Every PyGithub class that has a corresponding OpenAPI schema documents it in the class docstring:

```python
class Autolink(NonCompletableGithubObject):
    """
    The OpenAPI schema can be found at

    - /components/schemas/autolink
    """
```

Pass the listed path directly to `get-openapi-schema.sh` to retrieve the schema.

### Method → Path

Every PyGithub method that makes an HTTP request documents it with `:calls:`:

```python
def edit(self, sha: str, force: Opt[bool] = NotSet) -> None:
    """
    :calls: `PATCH /repos/{owner}/{repo}/git/refs/{ref} <https://docs.github.com/...>`_
    """
```

The format is: **VERB PATH "documentation URL"** (RST hyperlink syntax). Pass the PATH to `get-openapi-path.sh`, then look up the verb key in the result.

---

## Mapping an API Path to a PyGithub Class and Method

Given a path from the OpenAPI spec, follow these four steps to identify (or design) the right PyGithub class and method.

---

### Step 1 — Identify the Owning Class

The owning class is determined by the **deepest named resource** in the path.

#### Collection vs item operations — the core rule

| Path form | Operation type | Method goes on |
|---|---|---|
| `GET /A/{a_id}/Bs` | list Bs belonging to A | **A** class (e.g. `A.get_Bs()`) |
| `POST /A/{a_id}/Bs` | create a B under A | **A** class (e.g. `A.create_B()`) |
| `GET /A/{a_id}/Bs/{b_id}` | get a specific B | **A** class (e.g. `A.get_B(id)`) |
| `PATCH /A/{a_id}/Bs/{b_id}` | update a specific B | **B** class (`B.edit()`) |
| `DELETE /A/{a_id}/Bs/{b_id}` | delete a specific B | **B** class (`B.delete()`) |

B instances are always created by A (never via a `B.get()` — PyGithub has no such pattern). When B has its own class, its self-mutating methods (`edit`, `delete`) live on B. Read operations (`get_B`, `get_Bs`) always live on A.

#### Path prefix → class mapping

| Path prefix | PyGithub class | File |
|---|---|---|
| `/repos/{owner}/{repo}` | `Repository` | `github/Repository.py` |
| `/repos/{owner}/{repo}/issues/{issue_number}` | `Issue` | `github/Issue.py` |
| `/repos/{owner}/{repo}/pulls/{pull_number}` | `PullRequest` | `github/PullRequest.py` |
| `/repos/{owner}/{repo}/branches/{branch}` | `Branch` | `github/Branch.py` |
| `/repos/{owner}/{repo}/git/refs/{ref}` | `GitRef` | `github/GitRef.py` |
| `/repos/{owner}/{repo}/git/commits/{sha}` | `GitCommit` | `github/GitCommit.py` |
| `/repos/{owner}/{repo}/commits/{sha}` | `Commit` | `github/Commit.py` |
| `/repos/{owner}/{repo}/releases/{release_id}` | `GitRelease` | `github/GitRelease.py` |
| `/repos/{owner}/{repo}/actions/workflows/{id}` | `Workflow` | `github/Workflow.py` |
| `/repos/{owner}/{repo}/actions/runs/{run_id}` | `WorkflowRun` | `github/WorkflowRun.py` |
| `/orgs/{org}` | `Organization` | `github/Organization.py` |
| `/orgs/{org}/teams/{team_slug}` | `Team` | `github/Team.py` |
| `/gists/{gist_id}` | `Gist` | `github/Gist.py` |
| `/gists/{gist_id}/comments/{comment_id}` | `GistComment` | `github/GistComment.py` |
| `/user` (authenticated user) | `AuthenticatedUser` | `github/AuthenticatedUser.py` |
| `/user/*` (authenticated user's collections) | `AuthenticatedUser` | `github/AuthenticatedUser.py` |
| `/users/{username}` | `NamedUser` | `github/NamedUser.py` |
| `/search/*` | `Github` (MainClass) | `github/MainClass.py` |
| `/repos`, `/orgs`, `/users` (top-level) | `Github` (MainClass) | `github/MainClass.py` |

---

### Step 2 — Identify the Method Name

The method name is derived from **HTTP verb + path suffix after the resource ID**. The tables below cover every established pattern.

#### GET

| Path suffix after resource ID | Returns | Method name pattern | Example |
|---|---|---|---|
| *(none — the resource itself)* | object | `get_X(id)` on parent | `Repository.get_issue(number)` |
| `/sub-collection` | `PaginatedList[X]` | `get_Xs()` | `Issue.get_comments()` |
| `/sub-collection/{id}` | object | `get_X(id)` on parent | `Issue.get_comment(id)` |
| `/sub-collection` with 204 check | `bool` | `has_in_X(item)` | `Organization.has_in_members(user)` |
| `/star`, `/merge` — state check | `bool` | `is_X()` | `PullRequest.is_merged()`, `Gist.is_starred()` |
| `/stats/{name}` | `list[X] or None` | `get_stats_X()` | `Repository.get_stats_contributors()` |
| `/traffic/{name}` | `list[X] or None` | `get_top_X()` / `get_views()` | `Repository.get_top_referrers()` |
| `/languages`, `/topics`, etc. | `dict` / primitive | `get_X()` | `Repository.get_languages()` |

#### POST

| Path suffix | Returns | Method name pattern | Example |
|---|---|---|---|
| `/sub-collection` (creates item) | new object | `create_X(...)` | `Repository.create_issue(...)` |
| `/sub-collection` (adds members) | `None` | `add_to_X(*items)` | `Issue.add_to_labels(*labels)` |
| `/forks` | new object | `create_fork()` | `Repository.create_fork()` |
| `/{action}` (verb-like suffix) | varies | name after action | `Repository.create_dispatch(...)` |

#### PUT

| Path suffix | Returns | Method name pattern | Example |
|---|---|---|---|
| `/star` (set flag on resource) | `None` | `set_starred()` | `Gist.set_starred()` |
| `/{collection}/{item}` (idempotent add) | `None` | `add_to_X(item)` | `AuthenticatedUser.add_to_starred(repo)` |
| `/merge` | `PullRequestMergeStatus` | `merge(...)` | `PullRequest.merge(...)` |
| `/{sub-resource}/dismissals` | `None` | `dismiss(msg)` | `PullRequestReview.dismiss(msg)` |
| `/protection/restrictions/{type}` (replace all) | `None` | `replace_X(*items)` | `Branch.replace_user_push_restrictions(...)` |
| `/update-branch` | `bool` | `update_branch()` | `PullRequest.update_branch()` |
| `/vulnerability-alerts` (enable) | `bool` | `enable_X()` | `Repository.enable_vulnerability_alert()` |
| `/collaborators/{user}` (membership) | `Invitation or None` | `add_to_collaborators(user)` | `Repository.add_to_collaborators(user)` |

#### PATCH

| Path suffix | Returns | Method name pattern | Example |
|---|---|---|---|
| *(none — update self)* | `None` (in-place) | `edit(...)` | `Repository.edit(...)`, `GistComment.edit(body)` |
| `/protection` | `BranchProtection` | `edit_protection(...)` | `Branch.edit_protection(...)` |
| `/protection/required_status_checks` | `RequiredStatusChecks` | `edit_required_status_checks(...)` | `Branch.edit_required_status_checks(...)` |

#### DELETE

| Path suffix | Returns | Method name pattern | Example |
|---|---|---|---|
| *(none — delete self)* | `None` | `delete()` | `Repository.delete()`, `GistComment.delete()` |
| `/sub-collection/{id}` (specific item) | `None` | `remove_X(item)` | `Repository.remove_autolink(id)` |
| `/{collection}/{item}` (membership) | `None` | `remove_from_X(item)` | `AuthenticatedUser.remove_from_starred(repo)` |
| `/sub-collection` (clear all) | `None` | `delete_X()` | `Issue.delete_labels()` |
| `/star` (unset flag on resource) | `None` | `reset_starred()` | `Gist.reset_starred()` |
| `/vulnerability-alerts` (disable) | `bool` | `disable_X()` | `Repository.disable_vulnerability_alert()` |
| `/protection` (remove) | `None` | `remove_protection()` | `Branch.remove_protection()` |

---

### Step 3 — Identify the Return Type

| API response | PyGithub return type |
|---|---|
| `200` with `$ref` to a schema | instance of the corresponding class |
| `200`/`201` with `"type": "array"` | `PaginatedList[X]` |
| `201 Created` with `$ref` | instance of the created class |
| `204 No Content` (action/delete) | `None` |
| `204 No Content` (GET existence check) | `bool` (204 → `True`, 404 → `False`) |
| `202 Accepted` (async) | `bool` (202 → `True`) |
| Nullable schema (`nullable: true`) | `X or None` |
| Statistics endpoints | `list[X] or None` (None = GitHub still computing) |
| Endpoint returning two typed collections | `tuple[PaginatedList[X], PaginatedList[Y]]` |
| Membership invitation endpoint | `Invitation or None` (None = immediately effective) |

---

### Step 4 — Identify Method Parameters

| Source | Becomes | Python convention |
|---|---|---|
| Path parameter (e.g. `{issue_number}`) | positional arg | `number: int` |
| `requestBody` required field | positional arg | `title: str` |
| `requestBody` optional field | keyword arg with `NotSet` default | `body: Opt[str] = NotSet` |
| Optional field where `None` clears the value | keyword arg accepting `None` | `assignee: Opt[str or None] = NotSet` |

Common parameter names follow the JSON field names verbatim (`state`, `since`, `per_page`, `direction`, `sort`).

---

### `add_to_X()` vs `set_X()` — disambiguation

Both use PUT, but the naming depends on **whose perspective** the method is written from:

- **`add_to_X(item)` / `remove_from_X(item)`** — used when the *caller* is managing a collection they own.
  E.g. `AuthenticatedUser.add_to_starred(repo)` — the user adds to their own starred-repos collection.

- **`set_X()` / `reset_X()`** — used when the *resource itself* has a boolean state flag.
  E.g. `Gist.set_starred()` — the gist has a "starred" state that the caller sets or clears.

---

### `@property` vs `get_X()` method

| Use `@property` when | Use `get_X()` method when |
|---|---|
| Value comes from the object's own JSON payload (no extra API call) | Value requires a separate API call to a sub-resource |
| No parameters needed | Any parameters are needed (filters, IDs, etc.) |
| Read-only scalar or embedded object | Returns `PaginatedList` or a freshly-fetched object |

---

### Worked example — predicting the implementation of a new path

**Path:** `POST /repos/{owner}/{repo}/issues/{issue_number}/sub-issues`
**Response:** `201` with `$ref: issue` schema

1. Deepest resource: `{issue_number}` → **`Issue`** class
2. HTTP verb POST + suffix `/sub-issues` (creates items) → `Issue.create_sub_issue(...)`
3. Response is `201` with single `$ref` to `issue` → returns **`Issue`** instance
4. Check `requestBody` schema for required/optional fields → map to positional/`Opt` params

---

## Complete Example: `Autolink`

### PyGithub class (`github/Autolink.py`)

- Schema: `/components/schemas/autolink`
- Inherits `NonCompletableGithubObject` (no lazy loading — returned inline in list responses)
- No methods of its own; lifecycle is managed by `Repository`

### Schema in JSON

```json
{
  "title": "Autolink reference",
  "type": "object",
  "properties": {
    "id":             { "type": "integer" },
    "key_prefix":     { "type": "string" },
    "url_template":   { "type": "string" },
    "is_alphanumeric":{ "type": "boolean" },
    "updated_at":     { "type": "string", "format": "date-time", "nullable": true }
  },
  "required": ["id", "key_prefix", "url_template", "is_alphanumeric"]
}
```

### Related paths in `Repository.py`

| PyGithub method | Verb + Path |
|---|---|
| `get_autolinks()` | `GET /repos/{owner}/{repo}/autolinks` → returns `PaginatedList[Autolink]` |
| `create_autolink(...)` | `POST /repos/{owner}/{repo}/autolinks` → returns `Autolink` |
| `remove_autolink(...)` | `DELETE /repos/{owner}/{repo}/autolinks/{autolink_id}` → `204 No Content` |

The `GET` response schema is `{ "type": "array", "items": { "$ref": "#/components/schemas/autolink" } }` — an array, so PyGithub wraps it in `PaginatedList`. The `POST` response schema is `{ "$ref": "#/components/schemas/autolink" }` — a single object, so PyGithub returns one `Autolink` instance directly.

---

## Complete Example: `GistComment`

### PyGithub class (`github/GistComment.py`)

- Schema: `/components/schemas/gist-comment`
- Inherits `CompletableGithubObject` (supports lazy loading via `self.url`)
- Has `delete()` and `edit()` methods

### Schema in JSON (abbreviated)

```json
{
  "title": "Gist Comment",
  "properties": {
    "id":               { "type": "integer" },
    "node_id":          { "type": "string" },
    "url":              { "type": "string", "format": "uri" },
    "body":             { "type": "string" },
    "user":             { "$ref": "#/components/schemas/nullable-simple-user" },
    "created_at":       { "type": "string", "format": "date-time" },
    "updated_at":       { "type": "string", "format": "date-time" },
    "author_association":{ "$ref": "#/components/schemas/author-association" }
  }
}
```

- `user` → `_makeClassAttribute(github.NamedUser.NamedUser, ...)`
- `author_association` resolves to an enum schema → `_makeStringAttribute`

### Path `/gists/{gist_id}/comments/{comment_id}`

| Verb | `operationId` | PyGithub method |
|---|---|---|
| `GET` | `gists/get-comment` | (lazy completion of the object) |
| `PATCH` | `gists/update-comment` | `edit(body)` |
| `DELETE` | `gists/delete-comment` | `delete()` |

---

## Complete Example: `GitRef`

### PyGithub class (`github/GitRef.py`)

- Schema: `/components/schemas/git-ref`
- Inherits `CompletableGithubObject`
- The `object` property is an inline nested object in the schema, not a `$ref` — PyGithub wraps it in the separate `github.GitObject.GitObject` class

### Schema in JSON (abbreviated)

```json
{
  "title": "Git Reference",
  "properties": {
    "ref":     { "type": "string" },
    "node_id": { "type": "string" },
    "url":     { "type": "string", "format": "uri" },
    "object":  {
      "type": "object",
      "properties": {
        "type": { "type": "string" },
        "sha":  { "type": "string" },
        "url":  { "type": "string", "format": "uri" }
      }
    }
  }
}
```

### Path `/repos/{owner}/{repo}/git/refs/{ref}`

| Verb | `operationId` | PyGithub method |
|---|---|---|
| `PATCH` | `git/update-ref` | `edit(sha, force=NotSet)` |
| `DELETE` | `git/delete-ref` | `delete()` |

`PATCH` `requestBody` has `{ "sha": string (required), "force": boolean (optional) }` → matches `edit(sha: str, force: Opt[bool] = NotSet)`.

---

## Quick Reference: Looking Up a Schema or Path

```bash
JSON=api.github.com.*.json

# Look up a schema by path from the class docstring
cat $JSON | scripts/get-openapi-schema.sh /components/schemas/issue

# Look up a path from a :calls: docstring
cat $JSON | scripts/get-openapi-path.sh '/repos/{owner}/{repo}/issues'

# Resolve a $ref from a schema property (strip leading '#')
cat $JSON | scripts/get-openapi-schema.sh /components/schemas/nullable-simple-user

# List all paths for a given tag/category
jq '.paths | to_entries[] | select(.value | to_entries[].value.tags[]? == "gists") | .key' $JSON | sort -u

# List all schema names
jq '.components.schemas | keys[]' $JSON

# Extract all (VERB PATH) pairs from the spec
jq -r '.paths | to_entries[] | .key as $p | .value | to_entries[] |
  select(.key | test("^(get|post|put|patch|delete)$")) |
  [(.key | ascii_upcase), $p] | @tsv' $JSON | sort -u > /tmp/spec_paths.txt

# Extract all implemented (VERB PATH) pairs from :calls: docstrings
grep -rh ':calls:' github/ | grep -oP '(?<=:calls: `)[A-Z]+ [^\s<`]+' \
  | sed 's/ /\t/' | sort -u > /tmp/impl_paths.txt

# Find spec operations not yet implemented
comm -23 <(sort /tmp/spec_paths.txt) <(sort /tmp/impl_paths.txt)
```

---

## Implementation Coverage

As of the spec snapshot `api.github.com.2022-11-28.20251114T1100.json`:

- **1 111** total verb+path operations in the spec
- **535** implemented via `:calls:` docstrings in `github/`
- **~629** unimplemented (see `OPENAPI.MISSING.md`)

The gap is tracked in these files in the project root:

| File | Purpose |
|---|---|
| `OPENAPI.MISSING.md` | Table of every unimplemented operation with suggested class + method |
| `OPENAPI.MISSING.UPDATE.md` | Step-by-step instructions for regenerating `OPENAPI.MISSING.md` |
| `classify_missing_paths.py` | Script that maps each missing path to a class and method name |
| `missing_with_desc.txt` | Intermediate input for the script (verb, path, description) |
