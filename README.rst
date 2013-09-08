This is a Python (2 and 3) library to access the `Github API v3 <http://developer.github.com/v3>`_.
With it, you can manage your `Github <http://github.com>`_ resources (repositories, user profiles, organizations, etc.) from Python scripts.

It covers the **full** API (except recent additions, see "What's missing" bellow), and all methods are tested against the real Github site.

Should you have any question, any remark, or if you find a bug, or if there is something you can do with the API but not with PyGithub, please `open an issue <https://github.com/jacquev6/PyGithub/issues>`_.

PyGithub is stable. I will maintain it up to date with the API, and fix bugs if any, but I don't plan new heavy developments.


What's new?
===========

Thank you, dear stargazers!
---------------------------

Starting today (September 05th, 2013), we now need more than 8 bits to store the number of `stargazers <https://github.com/jacquev6/PyGithub/stargazers>`_! Thank you so much!

`Version 1.19.0 <https://github.com/jacquev6/PyGithub/issues?milestone=31&state=closed>`_ (September 8th, 2013) (AKFish's edition)
----------------------------------------------------------------------------------------------------------------------------------

* Implement `conditional requests <http://developer.github.com/guides/getting-started/#conditional-requests>`_ by the method ``GithubObject.update``. Thank you very much `akfish <https://github.com/akfish>`_ for the pull request and your collaboration!
* Implement persistence of PyGithub objects: ``Github.save`` and ``Github.load``. Don't forget to ``update`` your objects after loading them, it won't decrease your rate limiting quota if nothing has changed. Again, thank you `akfish <https://github.com/akfish>`_
* Implement ``Github.get_repos`` to get all public repositories
* Implement ``NamedUser.has_in_following``
* `Implement <https://github.com/jacquev6/PyGithub/issues/188>`_ ``Github.get_api_status``, ``Github.get_last_api_status_message`` and ``Github.get_api_status_messages``. Thank you `ruxandraburtica <https://github.com/ruxandraburtica>`_ for asking
* Implement ``Github.get_rate_limit``
* Add many missing attributes
* Technical change: HTTP headers are now stored in retrieved objects. This is a base for new functionalities. Thank you `akfish <https://github.com/akfish>`_ for the pull request
* Use the new URL to fork gists (minor change)
* Use the new URL to test hooks (minor change)

What's missing?
===============

We now have automated ways to list URLs documented in `the reference of Github API v3 <http://developer.github.com>`_ and not covered by PyGithub.

Github API v3 URLs not (yet) covered by PyGithub
------------------------------------------------

* ``/applications/:client_id/tokens/:access_token`` (GET)
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

Documentation
=============

All the documentation is here: http://jacquev6.github.com/PyGithub.
