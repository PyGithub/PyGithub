This is a Python (2 and 3) library to access the `Github API v3 <http://developer.github.com/v3>`_.
With it, you can manage `Github <http://github.com>`_ resources (repositories, user profiles, organizations, etc.) from Python scripts.

It covers almost the full API (see "What's missing" below), and all methods are tested against the real Github site.

Should you have any question, any remark, or if you find a bug, or if there is something you can do with the API but not with PyGithub, please `open an issue <https://github.com/jacquev6/PyGithub/issues>`_.

For further details, please refer to the `reference documentation <http://pygithub.readthedocs.org/en/stable/>`_ at ``readthedocs.org``.

Looking for maintainers (February 22nd, 2015)
=============================================

My current priorities are not compatible with doing a good job maintaining PyGithub, so I'm looking for volunteers to take over.
Please see `#297 <https://github.com/jacquev6/PyGithub/issues/297>`__.

What's new?
===========

Version 1.26.0 (November 5th, 2015)
-----------------------------------

* Added context parameter to Status API
* Changed InputGitAuthor to reflect that time is an optional parameter
* Added sort option to get_pulls
* Added api_preview parameter to Requester class
* Return empty list instead of None for pagination with no pages
* Removed URL scheme validation that broke GitHub Enterprise
* Added "add_membership" call to Teams
* Added support to lazily load repositories
* Updated test suite to record with oauth tokens
* Added support for http_proxy
* Add support for filter/role options in Organization.get_members()
* Changed Organization.get_members's filter parameter to _filter
* Fix escaping so that labels now support whitespaces
* Updated create_issue to support taking a list of strings for labels
* Added support for long integers in get_repo
* Fixed pagination to thread headers between requests
* Added repo.get_stargazers_with_dates()

Version 1.25.2 (October 7th, 2014)
----------------------------------

* `Work around <https://github.com/jacquev6/PyGithub/issues/278>`__ the API v3 returning ``null`` in some paginated responses, thanks `erichaase <https://github.com/erichaase>`__ for the bug report

Version 1.25.1 (September 28th, 2014)
-------------------------------------

* `Fix <https://github.com/jacquev6/PyGithub/pull/275>`__ two-factor authentication header, thanks to `tradej <https://github.com/tradej>`__ for the pull request

`Version 1.25.0 <https://github.com/jacquev6/PyGithub/issues?milestone=38&state=closed>`_ (May 4th, 2014)
---------------------------------------------------------------------------------------------------------

* `Implement <https://github.com/jacquev6/PyGithub/pull/246>`__ getting repos by id, thanks to `tylertreat <https://github.com/tylertreat>`__ for the pull request
* `Add <https://github.com/jacquev6/PyGithub/pull/247>`__ ``Gist.owner``, thanks to `dalejung <https://github.com/dalejung>`__ for the pull request

What's missing? Github API v3 URLs not covered by PyGithub
==========================================================

A lot of things including the following URLs, and every new things published by GitHub recently.

* ``/applications/:client_id/tokens/:access_token`` (GET)
* ``/authorizations/clients/:client_id`` (PUT)
* ``/feeds`` (GET)
* ``/meta`` (GET)
* ``/notifications`` (PUT)
* ``/notifications/emails`` (GET)
* ``/notifications/emails`` (PATCH)
* ``/notifications/global/emails`` (GET)
* ``/notifications/global/emails`` (PUT)
* ``/notifications/organization/:org/emails`` (GET)
* ``/notifications/organization/:org/emails`` (PUT)
* ``/notifications/settings`` (GET)
* ``/notifications/settings`` (PATCH)
* ``/notifications/threads/:id`` (PATCH)
* ``/notifications/threads/:id/subscription`` (DELETE)
* ``/notifications/threads/:id/subscription`` (GET)
* ``/notifications/threads/:id/subscription`` (PUT)
* ``/repos/:owner/:repo/contents/:path`` (DELETE)
* ``/repos/:owner/:repo/contents/:path`` (PUT)
* ``/repos/:owner/:repo/notifications`` (GET)
* ``/repos/:owner/:repo/notifications`` (PUT)
* ``/repos/:owner/:repo/releases/:id/assets`` (GET)
* ``/repos/:owner/:repo/releases/assets/:id`` (DELETE)
* ``/repos/:owner/:repo/releases/assets/:id`` (GET)
* ``/repos/:owner/:repo/releases/assets/:id`` (PATCH)
* ``/repos/:owner/:repo/subscription`` (DELETE)
* ``/repos/:owner/:repo/subscription`` (GET)
* ``/repos/:owner/:repo/subscription`` (PUT)
