This is a Python (2 and 3) library to access the `Github API v3 <http://developer.github.com/v3>`_.
With it, you can manage `Github <http://github.com>`_ resources (repositories, user profiles, organizations, etc.) from Python scripts.

It covers almost the full API (see "What's missing" bellow), and all methods are tested against the real Github site.

Should you have any question, any remark, or if you find a bug, or if there is something you can do with the API but not with PyGithub, please `open an issue <https://github.com/jacquev6/PyGithub/issues>`_.

PyGithub 1.x.x is stable and I don't plan to spend time adding missing functionalities. I still accept your pull requests.
Here is the `references documentation <http://jacquev6.github.io/PyGithub/v1>`_.

I'm currently developing the `version 2 of PyGithub <https://github.com/jacquev6/PyGithub/tree/develop_v2>`_.
Here is the `documentation <http://jacquev6.github.io/PyGithub/v2/index.html#migration-strategy-and-maintenance-schedule>`_, including a migration planning.

What's new?
===========

Version 2.0.0-alpha.4 (August 5th, 2014)
----------------------------------------

It's now quicker to list what's *not* covered by v2! So, this is not covered by v2:

* comments
* events, hooks
* GitHub Enterprise specific APIs
* search
* authorizations, applications
* statuses, deployments, releases
* stats

You can see what's not covered in details in the `unimplemented.*.yml <https://github.com/jacquev6/PyGithub/tree/develop_v2/ApiDefinition>`__ files, or in the `reference documentation <http://jacquev6.github.io/PyGithub/v2/reference/apis.html>`__.

Do not hesitate to `open an issue <https://github.com/jacquev6/PyGithub/issues>`_ to discuss anything.

Version 1.25.1 (September 28th, 2014)
-------------------------------------

* `Fix <https://github.com/jacquev6/PyGithub/pull/275>`__ two-factor authentication header, hanks to `tradej <https://github.com/tradej>`__ for the pull request

`Version 1.25.0 <https://github.com/jacquev6/PyGithub/issues?milestone=38&state=closed>`_ (May 4th, 2014)
---------------------------------------------------------------------------------------------------------

* `Implement <https://github.com/jacquev6/PyGithub/pull/246>`__ getting repos by id, thanks to `tylertreat <https://github.com/tylertreat>`__ for the pull request
* `Add <https://github.com/jacquev6/PyGithub/pull/247>`__ ``Gist.owner``, thanks to `dalejung <https://github.com/dalejung>`__ for the pull request

Twitter
-------

I tweet each new release. I rarely tweet, and always about software development, so you might want to `follow me <https://twitter.com/jacquev6>`_ to stay informed.

What's missing in versions 1.x.x? Github API v3 URLs not covered by v1
======================================================================

A lot of things including the following URLs, and every new things published by GitHub recently. Being able to implement new GitHub features quicker is the main motivation for developing the v2 of PyGithub.

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
* ``/repos/:owner/:repo/releases`` (GET)
* ``/repos/:owner/:repo/releases`` (POST)
* ``/repos/:owner/:repo/releases/:id`` (DELETE)
* ``/repos/:owner/:repo/releases/:id`` (GET)
* ``/repos/:owner/:repo/releases/:id`` (PATCH)
* ``/repos/:owner/:repo/releases/:id/assets`` (GET)
* ``/repos/:owner/:repo/releases/assets/:id`` (DELETE)
* ``/repos/:owner/:repo/releases/assets/:id`` (GET)
* ``/repos/:owner/:repo/releases/assets/:id`` (PATCH)
* ``/repos/:owner/:repo/subscription`` (DELETE)
* ``/repos/:owner/:repo/subscription`` (GET)
* ``/repos/:owner/:repo/subscription`` (PUT)
