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

## Automated tests

You can run the tests through `python -m github.tests`.
Run a specific test with `python -m github.tests TestCase` or `python -m github.tests TestCase.testMethod`.

If you add a new test, for example `Issue139.testCompletion`, you must add an import in `github/tests/AllTests.py`.
Then, you have to run `python -m github.tests Issue139.testCompletion --record` to create the `github/tests/ReplayData/*.txt` files needed for you new test.
Check them and commit them as well.
You will need a `GithubCredentials.py` file at the root of the project with the following contents:

```
login = "my_login"
password = "my_password"
oauth_token = "my_token"  # Can be left empty if not used
```

If you use 2 factor authentication on your Github account, tests that require a login/password authentication will fail.
You can use `python -m github.tests Issue139.testCompletion --record --auth_with_token` to use the `oauth_token` field specified in `GithubCredentials.py` when recording a unit test interaction. NB that the `password = ""` (empty string is ok) must still be present in `GithubCredentials.py` to run the tests even when the `--auth_with_token` arg is used.

## Coding conventions

PyGithub follows [pep8 Style Guide for Python Code](http://www.python.org/dev/peps/pep-0008/) except for line length.
Please check your code with [pep8 Python style guide checker](http://pypi.python.org/pypi/pep8), by running `pep8 --ignore=E501 github`.
