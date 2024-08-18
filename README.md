# PyGitHub

[![PyPI](https://img.shields.io/pypi/v/PyGithub.svg)](https://pypi.python.org/pypi/PyGithub)
![CI](https://github.com/PyGithub/PyGithub/workflows/CI/badge.svg)
[![readthedocs](https://img.shields.io/badge/docs-stable-brightgreen.svg?style=flat)](https://pygithub.readthedocs.io/en/stable/?badge=stable)
[![License](https://img.shields.io/badge/license-LGPL-blue.svg)](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)
[![Slack](https://img.shields.io/badge/Slack%20channel-%20%20-blue.svg)](https://join.slack.com/t/pygithub-project/shared_invite/zt-duj89xtx-uKFZtgAg209o6Vweqm8xeQ)
[![Open Source Helpers](https://www.codetriage.com/pygithub/pygithub/badges/users.svg)](https://www.codetriage.com/pygithub/pygithub)
[![codecov](https://codecov.io/gh/PyGithub/PyGithub/branch/master/graph/badge.svg)](https://codecov.io/gh/PyGithub/PyGithub)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

PyGitHub is a Python library to access the [GitHub REST API].
This library enables you to manage [GitHub] resources such as repositories, user profiles, and organizations in your Python applications.

[GitHub REST API]: https://docs.github.com/en/rest
[GitHub]: https://github.com

## Install

```bash
pip install PyGithub
```

## Simple Demo

```python
from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("access_token")

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", auth=auth)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)

# To close connections after use
g.close()
```

## Documentation

More information can be found on the [PyGitHub documentation site.](https://pygithub.readthedocs.io/en/stable/introduction.html)

## Development

### Contributing

Long-term discussion and bug reports are maintained via GitHub Issues.
Code review is done via GitHub Pull Requests.

For more information read [CONTRIBUTING.md].

[CONTRIBUTING.md]: https://github.com/PyGithub/PyGithub/blob/main/CONTRIBUTING.md

### Maintainership

We're actively seeking maintainers that will triage issues and pull requests and cut releases.
If you work on a project that leverages PyGitHub and have a vested interest in keeping the code alive and well, send an email to someone in the MAINTAINERS file.
