This is a Python (2 and 3) library to access the `Github API v3 <http://developer.github.com/v3>`_.
With it, you can manage your `Github <http://github.com>`_ resources (repositories, user profiles, organizations, etc.) from Python scripts.

It covers the **full** API (except recent additions, see "What's missing" bellow), and all methods are tested against the real Github site.

Should you have any question, any remark, or if you find a bug, or if there is something you can do with the API but not with PyGithub, please `open an issue <https://github.com/jacquev6/PyGithub/issues>`_.

PyGithub is stable. I will maintain it up to date with the API, and fix bugs if any, but I don't plan new heavy developments.


What's new?
===========

Version 2 is comming
--------------------

As of December 15th, 2013, I plan to spend more time on version 2. I'll continue to maintain version 1, investigating and fixing bugs, but I'm not going to actively implement missing features. I'll still be glad to accept pull requests.

More info on version 2 in the comming weeks, and here is an issue to discuss the topic: https://github.com/jacquev6/PyGithub/issues/217

`Version 1.22.0 <https://github.com/jacquev6/PyGithub/issues?milestone=34&state=closed>`_ (December 15th, 2013)
---------------------------------------------------------------------------------------------------------------

* `Emojis <https://github.com/jacquev6/PyGithub/pull/209>`__, thanks to `evolvelight <https://github.com/evolvelight>`__
* `Repository.stargazers_count <https://github.com/jacquev6/PyGithub/pull/212>`__, thanks to `cameronbwhite <https://github.com/cameronbwhite>`__
* `User.get_teams <https://github.com/jacquev6/PyGithub/pull/213>`__, thanks to `poulp <https://github.com/poulp>`__

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
* ``/search/code`` (GET)
* ``/search/issues`` (GET)
* ``/search/repositories`` (GET)
* ``/search/users`` (GET)

Documentation
=============

All the documentation is here: http://jacquev6.github.com/PyGithub.
