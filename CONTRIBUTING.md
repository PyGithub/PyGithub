# Contributing

## Issues

A good issue includes a [short, self contained, correct example](http://sscce.org/) of the problem, something like:

```python
from github import Github
from github import Auth

g = Github(auth=Auth.Token("****"))
assert g.get_user("jacquev6").name == "Vincent Jacques"
```

It is even better if you provide the debug logs associated with your issue.
Enable them with `github.enable_console_debug_logging` and copy them in the body of the issue.
**Warning:** you may want to remove private information from the log.

If for any reason you are not able to do that, open your issue anyway and a maintainer or community member may be able to help.

## Pull Requests

Pull Requests should contain the following things:

1. Describe the problem the Pull Request attempts to solve
2. Explain how the you went about solving the problem
3. Provide a test that exemplifies the expected behaviour

Ideally, changes should be made in logical commits and tests added to improve the project's coverage of the GitHub API.

## Coding style

PyGithub adopts the black coding style.

To manually format the code:
```bash
tox -e lint
```

## Pre-commit plugin

To forget about coding style and let [pre-commit](https://pre-commit.com/#installation) fix your flake8/isort/black issue.

```
pre-commit install
```

That's it!

## Create and extend PyGithub using OpenAPI

Github provides an [OpenAPI specification for its v3 REST API](https://github.com/github/rest-api-description/).
This can be used to semi-automate the creation and maintenance of PyGithub classes.

### Setup OpenAPI support

Download the OpenAPI specification, e.g. version `2022-11-28` for the `api.github.com` API:
```bash
python scripts/openapi.py fetch api.github.com 2022-11-28 api.github.com.2022-11-28.json
```

Load the PyGithub sources into an index file, e.g. `openapi.index`:
```bash
python scripts/openapi.py index github openapi.index
```

### OpenAPI annotation in PyGithub classes

PyGithub classes have annotations that link those classes to the respective schemas in the OpenAPI.

For example, the `Repository` class has this header:
```python
class Repository(CompletableGithubObject):
    """
    This class represents Repositories.

    The reference can be found here
    https://docs.github.com/en/rest/reference/repos

    The OpenAPI schema can be found at
    - /components/schemas/event/properties/repo
    - /components/schemas/full-repository
    - /components/schemas/minimal-repository
    - /components/schemas/nullable-repository
    - /components/schemas/pull-request-minimal/properties/base/properties/repo
    - /components/schemas/pull-request-minimal/properties/head/properties/repo
    - /components/schemas/repository
    - /components/schemas/simple-repository

    """
```
The list of OpenAPI schemas can be find below the `The OpenAPI schema can be found at` line.

A schema can be quickly extracted from the OpenAPI spec as follows:

```bash
./scripts/get-openapi-schema.sh /components/schemas/minimal-repository < api.github.com.2022-11-28.json
```

```bash
{
  "title": "Minimal Repository",
  "description": "Minimal Repository",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer",
      "format": "int64",
      "example": 1296269
    },
    "node_id": {
      "type": "string",
      "example": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5"
    },
    "name": {
      "type": "string",
      "example": "Hello-World"
    },
    "full_name": {
      "type": "string",
      "example": "octocat/Hello-World"
    },
    ...
}
```

### Create a PyGithub class from an OpenAPI schema

PyGithub classes can be created via `openapi create class`:
```
usage: openapi.py create class [-h] [--completable] [--parent PARENT] [--tests] github_path spec index_filename class_name docs_url [schema ...]

positional arguments:
  github_path      Path to PyGithub Python files
  spec             Github API OpenAPI spec file
  index_filename   Path of index file
  class_name       PyGithub GithubObject class name
  docs_url         Github REST API documentation URL, for instance https://docs.github.com/en/rest/commits/commits#get-a-commit-object
  schema           Github API OpenAPI schema name

options:
  -h, --help       show this help message and exit
  --completable    New PyGithub class is completable, implies --parent CompletableGithubObject
  --parent PARENT  A parent PyGithub class
  --tests          Also create test file
```

For example, create completable class `Commit` including tests as follows:
```bash
python ../PyGithub-OpenAPI/scripts/openapi.py create class --completable --tests \
  github api.github.com.2022-11-28.json openapi.index \
  Commit https://docs.github.com/en/rest/commits/commits#get-a-commit-object \
  /components/schemas/commit /components/schemas/commit/properties/parents/items
```

### Add method to PyGithub class from OpenAPI path

Methods can be added to PyGithub classes via `openapi create method`:

```bash
usage: openapi.py create method [-h] [--return-property [RETURN_PROPERTY]] spec index_filename class_name method_name api_verb api_path [api_response]

positional arguments:
  spec                  Github API OpenAPI spec file
  index_filename        Path of index file
  class_name            PyGithub GithubObject class name
  method_name           PyGithub method name
  api_verb              OpenAPI verb
  api_path              OpenAPI path
  api_response          OpenAPI response, e.g. 200

options:
  -h, --help            show this help message and exit
  --return-property [RETURN_PROPERTY]
                        Return the value of this response property, instead of the entire response object
```

For example, create method `get_check_runs`_` class `Commit` including tests as follows:
```bash
python ../PyGithub-OpenAPI/scripts/openapi.py create class --completable --tests \
  github api.github.com.2022-11-28.json openapi.index \
  Commit https://docs.github.com/en/rest/commits/commits#get-a-commit-object \
  /components/schemas/commit /components/schemas/commit/properties/parents/items
```
/repos/{owner}/{repo}/commits/{sha}/check-runs
## Adding missing attributes for a GithubObject

```bash
$ python scripts/add_attribute.py [class_name] [attribute_name] [attribute_type]

# For example, if you want to add a `url` attribute of string type to the Commit class
# Note: adding multiple attributes you have to run the script multiple times

$ python scripts/add_attribute.py Commit url string
```

## Deprecation warning

Before removing attributes/methods, consider adding deprecation warnings instead. The [typing_extensions](https://pypi.org/project/typing-extensions/) package provides a handy decorator to add deprecation warnings.

```python
from typing_extensions import deprecated

@property
@deprecated("Use core instead")
def rate(self):
   pass

@deprecated("Deprecated in favor of the new branch protection")
def get_protected_branch(self):
   pass
```

## Automated tests

First you need to install the test dependencies:
```bash
pip install -r requirements/test.txt
```

Then you can run the tests through `pytest`.
Run a specific test with `pytest tests/tests_filename.py` or `pytest tests/tests_filename.py -k testMethod` or `pytest -k TestClass.testMethod`.

If you add or modify a test, for example `Repository.testCompare`, you have to run `pytest -k Repository.testCompare --record` to create or update the `tests/ReplayData/*.txt` files needed for your new test.
Check them in to git and commit them as well.

You will need a `GithubCredentials.py` file at the root of the project with the following contents:

```python
oauth_token = "my_token"
jwt = "my_json_web_token"               # Can be left empty if not used
app_id = "my_app_id"                    # Can be left empty if not used
app_private_key = "my_app_private_key"  # Can be left empty if not used
```

The `oauth_token` field in `GithubCredentials.py` is used by default to record test data.
Tests that require JWT (`jwt` field) or App authentication (`app_id` and `app_private_key` field)
have to enable `"jwt"` or `"app"` auth mode in their `setUp` method:

```python
def setUp(self):
    self.authMode = "jwt"
    super().setUp()
    ...
```

A test method that needs a different authentication than configured in `setUp` can simply
create a new `Github` object with the respective authentication:

```python
def testGetUserWithOAuth(self):
    # this test needs OAuth authentication
    g = self.get_github("oauth_token")
    self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

def testGetUserWithJwt(self):
    # this test needs JWT authentication
    g = self.get_github("jwt")
    self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

def testGetUserWithAppAuth(self):
    # this test needs App authentication
    g = self.get_github("app")
    self.assertEqual(g.get_user("jacquev6").name, "App name")
```

To run manual tests with external scripts that use the PyGithub package, you can install your development version with:

```bash
pip install --editable path/to/project
```

You may also want to investigate `tox` to run tests:

```bash
pip install tox
tox -epy310
```

## Build documentation locally

```bash
pip install -r requirements/docs.txt
sphinx-build doc build
```

If you use tox:

```bash
tox -edocs
```
