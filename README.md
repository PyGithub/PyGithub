# PyGitHub

[![PyPI](https://img.shields.io/pypi/v/PyGithub.svg)](https://pypi.python.org/pypi/PyGithub)
[![Build Status](https://travis-ci.org/PyGithub/PyGithub.svg?branch=master)](https://travis-ci.org/PyGithub/PyGithub)
[![readthedocs](https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat)](https://pygithub.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/badge/license-LGPL-blue.svg)](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)
[![Join the chat at https://gitter.im/PyGithub/PyGithub](https://badges.gitter.im/PyGithub/PyGithub.svg)](https://gitter.im/PyGithub/PyGithub?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Open Source Helpers](https://www.codetriage.com/pygithub/pygithub/badges/users.svg)](https://www.codetriage.com/pygithub/pygithub)
[![codecov](https://codecov.io/gh/PyGithub/PyGithub/branch/master/graph/badge.svg)](https://codecov.io/gh/PyGithub/PyGithub)

PyGitHub is a Python (2 and 3) library to access the [GitHub API v3] and [Github Enterprise API v3].
This library enables you to manage [GitHub] resources such as repositories, user profiles, and organizations in your Python applications.

[GitHub API v3]: https://developer.github.com/v3
[Github Enterprise API v3]: https://developer.github.com/enterprise/2.13/v3/
[GitHub]: https://github.com

## Install

```bash
$ pip install PyGithub
```

## Simple Demo

```python
from github import Github

# First create a Github instance:

# using username and password
g = Github("user", "password")

# or using an access token
g = Github("access_token")

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
```

## Documentation

More information can be found on the [PyGitHub documentation site.](https://pygithub.readthedocs.io/en/latest/introduction.html)

## Development

### Contributing

Long-term discussion and bug reports are maintained via GitHub Issues.
Code review is done via GitHub Pull Requests.

For more information read [CONTRIBUTING.md].

[CONTRIBUTING.md]: /CONTRIBUTING.md

### Maintainership

We're actively seeking maintainers that will triage issues and pull requests and cut releases.
If you work on a project that leverages PyGitHub and have a vested interest in keeping the code alive and well, send an email to someone in the MAINTAINERS file.
