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

Version 2.0.0-alpha.2 (March 23rd, 2014)
----------------------------------------

What's now covered by v2:

* Interaction between Repositories, Users, Organizations, Teams. Start with `the user guide <http://jacquev6.github.io/PyGithub/v2/user_guide.html#access-to-common-resources>`__.
* Getting and modifiying repository contents. Start with `Repository.get_contents <http://jacquev6.github.io/PyGithub/v2/reference/classes/Repository.html#PyGithub.Blocking.Repository.Repository.get_contents>`__.

Please comment on `those issues <https://github.com/jacquev6/PyGithub/issues?labels=Prioritization%2Cv2&milestone=&page=1&state=open>`_
to help me prioritize the next developments. And do not heasitate to `open an issue <https://github.com/jacquev6/PyGithub/issues>`_ to discuss anything.

`Version 1.25.0 <https://github.com/jacquev6/PyGithub/issues?milestone=38&state=closed>`_ (May 4th, 2014)
---------------------------------------------------------------------------------------------------------

* `Implement <https://github.com/jacquev6/PyGithub/pull/246>`__ getting repos by id, thanks to `tylertreat <https://github.com/tylertreat>`__ for the pull request
* `Add <https://github.com/jacquev6/PyGithub/pull/247>`__ ``Gist.owner``, thanks to `dalejung <https://github.com/dalejung>`__ for the pull request

Twitter
-------

I tweet each new release. I rarely tweet, and always about software development, so you might want to `follow me <https://twitter.com/jacquev6>`_ to stay informed.

What's missing in versions 1.x.x? Github API v3 URLs not covered by v1
======================================================================

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
