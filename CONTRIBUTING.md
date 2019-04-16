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

## Adding missing attributes for a GithubObject

```bash
$ python scripts/add_attribute.py [class_name] [attribute_name] [attribute_type]

# For example, if you want to add a `url` attribute of string type to the Commit class
# Note: adding multiple attributes you have to run the script multiple times

$ python scripts/add_attribute.py Commit url string
```

## Deprecation warning

Before removing attributes/methods, consider adding deprecation warnings instead. The [Deprecated](https://github.com/tantale/deprecated) packages provides a handy decorator to add deprecation warnings with an optional reason.

```python
from deprecated import deprecated

@property
@deprecated
def rate(self):
   pass

@deprecated(reason="Deprecated in favor of the new branch protection")
def get_protected_branch(self):
   pass
```

## Automated tests

First you need to install the test dependencies:
```bash
pip install -r test-requirements.txt
```

Then you can run the tests through `python -m tests`.
Run a specific test with `python -m tests TestCase` or `python -m tests TestCase.testMethod`.

If you add a new test, for example `Issue139.testCompletion`, you must add an import in `tests/AllTests.py`.
Then, you have to run `python -m tests Issue139.testCompletion --record` to create the `tests/ReplayData/*.txt` files needed for your new test.
Check them and commit them as well.
You will need a `GithubCredentials.py` file at the root of the project with the following contents:

```
login = "my_login"
password = "my_password"  # Can be left empty if not used
oauth_token = "my_token"  # Can be left empty if not used
jwt = "my_json_web_token"  # Can be left empty if not used
```

If you use 2 factor authentication on your Github account, tests that require a login/password authentication will fail.
You can use `python -m tests Issue139.testCompletion --record --auth_with_token` to use the `oauth_token` field specified in `GithubCredentials.py` when recording a unit test interaction. Note that the `password = ""` (empty string is ok) must still be present in `GithubCredentials.py` to run the tests even when the `--auth_with_token` arg is used. (Also note that if you record your test data with `--auth_with_token` then you also need to be in token authentication mode when running the test. A simple alternative is to replace `token private_token_removed` with `Basic login_and_password_removed` in all your newly generated ReplayData files.)

Similarly, you can use `python -m tests Issue139.testCompletion --record --auth_with_jwt` to use the `jwt` field specified in `GithubCredentials.py` to access endpoints that require JWT.

To run manual tests with external scripts that use the PyGithub package, you can install your development version with:

```
pip install --editable path/to/project
```

## Coding conventions

PyGithub follows [pep8 Style Guide for Python Code](http://www.python.org/dev/peps/pep-0008/) except for line length.
Please check your code with [pep8 Python style guide checker](http://pypi.python.org/pypi/pep8), by running `pep8 --ignore=E501 github`.

## Build documentation locally

Note: only Python 2 is supported as of now

```
pip install -r requirements.txt
sphinx-build doc build
```
