# Contributing

## Issues

A good issue includes a [short, self contained, correct example](http://sscce.org/) of the problem, something like:

```python
assert github.Github().get_user("jacquev6").name == "Vincent Jacques"
```

It is even better if you provide the debug logs associated with your issue.
Enable them with `github.enable_console_debug_logging` and copy them in the body of the issue.
**Warning:** you may want to remove some private information (authentication information is removed, but there may be private stuff in the messages)

If for any reason you are not able to do that, open your issue anyway and a maintainer will see what is needed to solve your problem.

## Pull Requests

Pull Requests should clearly describe two things:

1. The problem they attempt to solve
2. How the author went about solving the problem

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
