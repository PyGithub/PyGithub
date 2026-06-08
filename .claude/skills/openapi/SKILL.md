---
name: OpenAPI
description: Script to create or modify PyGithub classes according to Github REST API OpenAPI specification.
---

# OpenAPI script

First read [OPENAPI.md](../../../OPENAPI.md).

The script lives at `scripts/openapi.py`. Invoke the script with `python3 scripts/openapi.py ...`

Generated code is not guaranteed to compile and work. It merely represents a suggestion and best practice.

## Contents
- Commands
- Notable files

## Commands
- help: provide help on using the script
- init: run before the first use of the OpenAPI Python script
- fetch: fetch an OpenAPI spec file
- index: index the OpenAPI spec file and PyGithub code base
- suggest: suggest paths or schemas
- apply: apply schema to class' properties (add/update attributes) or class' paths (add/update methods)
- create: create a new PyGithub class or method

Use option `--dry-run` to make a command read-only.

The index command creates a JSON file that is used by almost all other commands. Any change to PyGithub source code
requires to rerun (re-index) the index command and update the [OpenAPI index JSON file](#OpenAPI index JSON file). A index file is tightly
connected with the [OpenAPI spec JSON file](#OpenAPI spec JSON file) that was used in the index command. Using a different spect JSON file
requires a different index file.

Any code and test changes require fixing linting issues by running `pre-commit` and `mypy`.

Suggest updating this skill whenever interactions with the `openapi.py` script fail and
inspection of inner mechanics or invocation are needed. Add your findings to this skill
to avoid such inspections in the future.

### Invocation cheat sheet

Argument placement matters because of argparse:
- **Global flags** (`--dry-run`, `--verbose`, `--exit-code`) go **before** the command:
  `openapi.py --dry-run apply ...`
- **command flags** (e.g. `--new-schemas`, `--tests`, `--add`) go **after** the command but **before** the positional arguments:
  `openapi.py apply --new-schemas as-dict github/ <spec> <index> <Class>`
  Placing a command flag after the trailing positional class names fails with `error: unrecognized arguments`.

### help
Provides input on how to use commands, shows full set of options.

```bash
openapi.py --help
openapi.py COMMAND --help
openapi.py COMMAND SUB-COMMAND --help
```

### init
If no [OpenAPI spec JSON file](#OpenAPI spec JSON file) and no [OpenAPI index JSON file](#OpenAPI index JSON file) exists,
run the following sequence of commands (generates those files):
- fetch
- index

### fetch
Fetches the [OpenAPI spec JSON file](#OpenAPI spec JSON file) from the github.com. It is good practice to
use the time of retrieval as part of the filename to never overwrite an existing local spec file.
Create a symbolic link from `api.github.com.YYYY-MM-DD.json` to the latest `api.github.com.YYYY-MM-DD.YYYYMMDDTHHMMSS.json`
to simplify subsequent reference of the latest spec file.

```
usage: openapi.py fetch [-h] [--commit [COMMIT]] api api_version spec

positional arguments:
  api                Github API, e.g. api.github.com, ghec, ghes-3.15. See https://github.com/github/rest-api-description/tree/main/descriptions
  api_version        Github API version date, e.g. 2022-11-28
  spec               Github API OpenAPI spec file to be written

options:
  -h, --help         show this help message and exit
  --commit [COMMIT]  Specific commit to fetch file from
```

### index
Index the spec file and PyGithub codebase and store information in the [OpenAPI index JSON file](#OpenAPI index JSON file).
```
usage: openapi.py index [-h] [--check-verbs] github_path [spec] index_filename
```
Overwrite an existing index file if needed without asking for approval.

### suggest
These sub-commands exist:
- suggest paths
- suggest schemas

Ask user what to suggest if the sub-command is not clear.

#### suggest paths
Suggests which paths a class should implement.

```
usage: openapi.py suggest paths [-h] spec index_filename [class_name ...]
```

Example output:
```
Class Artifact
- Implements schema /components/schemas/artifact
  - Returned by path /repos/{owner}/{repo}/actions/artifacts/{artifact_id}
    - get /repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format} should be implemented as Artifact.download() or Artifact.get_download_link()
      python scripts/openapi.py create method api.github.com.2022-11-28.json openapi.index Artifact download get /repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format}
      python scripts/openapi.py create method api.github.com.2022-11-28.json openapi.index Artifact get_download_link get /repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format}

```
The output provides evidence for the suggestion ("Implements schema", "Returned by path"), the path and verb, suggested method name alternatives ("download", "get_download_link") and a list of openapi.py commands that would create those method alternatives.

This does not modify any files.

#### suggest schemas
Suggests which schemas a class should implement.

```
usage: openapi.py suggest schemas [-h] [--add] spec index_filename [class_name ...]
```
Example output:
```
Class Commit:
- should implement schema /components/schemas/commit
  Methods returning the schema:
  - PullRequest.get_commits
  - Repository.get_commit
  - Repository.merge
  - Repository.get_commits
Paths returning the class:
- GET /repos/{owner}/{repo}/commits
- GET /repos/{owner}/{repo}/commits/{ref}
- GET /repos/{owner}/{repo}/pulls/{pull_number}/commits
- POST /repos/{owner}/{repo}/merges
```
The output provides evidence which methods return the schema / paths and vers return the class. Those paths have response schemas defined in the OpenAPI spect JSON file.

Option `--add` adds the schemas to the classes.

Only option `--add` modifies files, unless `--dry-run` is given.

### apply
These sub-commands exist:
- apply properties
- apply methods

Ask user what to suggest if the sub-command is not clear.

#### apply properties
Applies a schema to a class' source code: adds/updates the `_initAttributes`, `@property` accessors and
`_useAttributes` entries for every property of the schema(s) the class implements. The class' docstring
lists all OpenAPI schemas it implements.

```
usage: openapi.py apply properties [-h] [--tests] [--new-schemas {ignore,create-class,as-dict}] github_path spec index_filename [class_name ...]

positional arguments:
  github_path           Path to PyGithub Python files
  spec                  Github API OpenAPI spec file
  index_filename        Path of index file
  class_name            PyGithub GithubObject class name

options:
  -h, --help            show this help message and exit
  --tests               Also apply spec to test files
  --new-schemas {ignore,create-class,as-dict}
                        How to handle attributes that return schemas that are not implemented by any PyGithub: 'ignore', 'create-class' crates class implementation drafts, 'as-dict'
                        return dict[str, Any]). Option 'create-class' does not support --dry-run.
```

Flag `--new-schemas` controls attributes whose schema is not implemented by any PyGithub class:
- `ignore` (default): the attribute is skipped (logged as `Schema not implemented: ...`, only with `--verbose`).
- `as-dict`: the attribute becomes `dict[str, Any]` via `_makeDictAttribute`. Good for nested objects that
  existing classes already model as a dict (check for precedent before inventing new classes).
- `create-class`: drafts new class files. Those classes may recursively create more new classes for other new schemas.
  **Does not support `--dry-run`.**

Preview with `--dry-run` (prints a unified diff). Add `--verbose` to see which properties were skipped as not-implemented.

#### apply methods
Applies OpenAPI path schemas to existing methods: adds/updates method arguments, docstrings, assertions and web calls.

```
usage: openapi.py apply methods [-h] [--rewrite] spec index_filename [class_or_class_method_name ...]

positional arguments:
  spec                  Github API OpenAPI spec file
  index_filename        Path of index file
  class_or_class_method_name
                        PyGithub GithubObject class name (like 'Commit') or class method name (like 'Commit.edit')

options:
  -h, --help            show this help message and exit
  --rewrite             Applying schema to methods is free to rewrite existing code. No care is taken to preserve existing documentation or avoid breaking changes.
```

Flag `--rewrite` (`apply methods` specific) for allows the script to rewrite existing code. No care is taken to preserve existing documentation or avoid breaking changes.
Without `--rewrite`, no attributes are removed or breaking changes introduced.

### create
Creates a new PyGithub class or method.

These sub-commands:
- create class
- create method

#### create class
Create a new PyGithub class from an OpenAPI schema.

```
usage: openapi.py create class [-h] [--completable] [--parent PARENT] [--tests] [--new-schemas {ignore,create-class,as-dict}]
                               github_path spec index_filename class_name docs_url [schema ...]

positional arguments:
  github_path           Path to PyGithub Python files
  spec                  Github API OpenAPI spec file
  index_filename        Path of index file
  class_name            PyGithub GithubObject class name
  docs_url              Github REST API documentation URL, for instance https://docs.github.com/en/rest/commits/commits#get-a-commit-object
  schema                Github API OpenAPI schema name

options:
  -h, --help            show this help message and exit
  --completable         New PyGithub class is completable, implies --parent CompletableGithubObject
  --parent PARENT       A parent PyGithub class
  --tests               Also create test file
  --new-schemas {ignore,create-class,as-dict}
                        How to handle attributes that return schemas that are not implemented by any PyGithub: 'ignore', 'create-class' crates class implementation drafts, 'as-dict'
                        return dict[str, Any]). Option 'create-class' does not support --dry-run.
```

#### create method
Create a new method from an OpenAPI path.

```
usage: openapi.py create method [-h] [--new-schemas {ignore,create-class,as-dict}] [--return-property [RETURN_PROPERTY]]
                                github_path spec index_filename class_name method_name api_verb api_path [api_response]

positional arguments:
  github_path           Path to PyGithub Python files
  spec                  Github API OpenAPI spec file
  index_filename        Path of index file
  class_name            PyGithub GithubObject class name
  method_name           PyGithub method name
  api_verb              OpenAPI verb
  api_path              OpenAPI path
  api_response          OpenAPI response, e.g. 200

options:
  -h, --help            show this help message and exit
  --new-schemas {ignore,create-class,as-dict}
                        How to return schemas that are not implemented by any PyGithub: 'ignore', 'create-class' crates class implementation drafts, 'as-dict' return dict[str, Any]).
                        Option 'create-class' does not support --dry-run.
  --return-property [RETURN_PROPERTY]
                        Return the value of this response property, instead of the entire response object
```

Command `suggest paths` prints ready-to-run `create method` command lines for the alternatives it proposes.

Check for similar methods to find the appropriate class and method name for the respective path.


## Notable files
### OpenAPI spec JSON file
An OpenAPI spec JSON file is usually named like `api.github.com.YYYY-MM-DD.json` or better `api.github.com.YYYY-MM-DD.YYYYMMDDTHHMMSS.json`,
where:
- `api.github.com`: the Github API name
- `YYYY-MM-DD`: the API version
- `YYYYMMDDTHHMMSS`: the time of retrieval

### OpenAPI index JSON file
An OpenAPI index JSON file is usually named `openapi.index`.
