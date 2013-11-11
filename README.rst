This is a Python (2 and 3) library to access the `Github API v3 <http://developer.github.com/v3>`_.
With it, you can manage your `Github <http://github.com>`_ resources (repositories, user profiles, organizations, etc.) from Python scripts.

It covers the **full** API (except recent additions, see "What's missing" bellow), and all methods are tested against the real Github site.

Should you have any question, any remark, or if you find a bug, or if there is something you can do with the API but not with PyGithub, please `open an issue <https://github.com/jacquev6/PyGithub/issues>`_.

PyGithub is stable. I will maintain it up to date with the API, and fix bugs if any, but I don't plan new heavy developments.


What's new?
===========

Thank you, dear stargazers!
---------------------------

Starting today (September 5th, 2013), we now need more than 8 bits to store the number of `stargazers <https://github.com/jacquev6/PyGithub/stargazers>`_! Thank you so much!

`Version 1.21.0 <https://github.com/jacquev6/PyGithub/issues?milestone=33&state=closed>`_ (November ??th, 2013)
---------------------------------------------------------------------------------------------------------------

* `Accept <https://github.com/jacquev6/PyGithub/issues/202>`__ strings as well as ``Label`` objects in ``Issue.add_to_labels``, ``Issue.remove_from_labels`` and ``Issue.set_labels``. Thank you `acdha <https://github.com/acdha>`__ for asking
* `Implement <https://github.com/jacquev6/PyGithub/issues/201>`__ equality comparison for *completable* github objects (ie. those who have a ``url`` attribute). Warning, comparison is still not implemented for non-completable objects. This will be done in version 2.0 of PyGithub. Thank you `OddBloke <https://github.com/OddBloke>`__ for asking
* `Add <https://github.com/jacquev6/PyGithub/issues/204>`__ parameter ``author`` to ``Repository.get_commits``. Thank you `naorrosenberg <https://github.com/naorrosenberg>`__ for asking

Twitter
-------

Starting with version 1.21.0, I'm going to twitt each new release. I rarelly twitt, and always about software development, so you might want to `follow me <https://twitter.com/jacquev6>`_ to stay informed.

What's missing?
===============

We now have automated ways to list URLs documented in `the reference of Github API v3 <http://developer.github.com>`_ and not covered by PyGithub.

Github API v3 URLs not (yet) covered by PyGithub
------------------------------------------------

* ``/applications/:client_id/tokens/:access_token`` (GET)
* ``/authorizations/clients/:client_id`` (PUT)
* ``/emojis`` (GET)
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
* ``/repos/:owner/:repo/stats/code_frequency`` (GET)
* ``/repos/:owner/:repo/stats/commit_activity`` (GET)
* ``/repos/:owner/:repo/stats/contributors`` (GET)
* ``/repos/:owner/:repo/stats/participation`` (GET)
* ``/repos/:owner/:repo/stats/punch_card`` (GET)
* ``/repos/:owner/:repo/subscription`` (DELETE)
* ``/repos/:owner/:repo/subscription`` (GET)
* ``/repos/:owner/:repo/subscription`` (PUT)
* ``/search/code`` (GET)
* ``/search/issues`` (GET)
* ``/search/repositories`` (GET)
* ``/search/users`` (GET)
* ``/user/teams`` (GET)

Documentation
=============

All the documentation is here: http://jacquev6.github.com/PyGithub.
