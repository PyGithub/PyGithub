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

## Development

See our [Development guide](https://pygithub.readthedocs.io/en/stable/development.html) for details.
