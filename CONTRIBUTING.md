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

Further guidelines:

- **One scope per Pull Request.** Distinct changes (e.g. a new endpoint, an unrelated fix, a dependency bump) go into
  separate Pull Requests. If one change builds on top of another, open them as stacked Pull Requests (the dependent one
  based on the branch of the other, or targeting `main` with "Depends on #N" in its description).
- **Follow prior art.** Check how the same kind of problem is already solved in other PyGithub classes (e.g. the
  repository-level variant of an organization-level endpoint) and reuse that pattern, naming and tests.
- **Tests must fail without your change** — because of a failing assertion or mismatching replay data, not merely
  because the new method or parameter does not exist.
- **Breaking changes** should be split into a Pull Request that deprecates the old API (naming an equivalent
  alternative) and a subsequent one that removes it. List all deprecations in the Pull Request description.

See [ARCHITECTURE.md](ARCHITECTURE.md) for code, API design and test conventions.

## Development

See our [Development guide](https://pygithub.readthedocs.io/en/stable/development.html) for details.
