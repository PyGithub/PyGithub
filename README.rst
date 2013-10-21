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

`Version 1.20.0 <https://github.com/jacquev6/PyGithub/issues?milestone=32&state=closed>`_ (October 20th, 2013) (First Seattle edition)
--------------------------------------------------------------------------------------------------------------------------------------

* `Implement <https://github.com/jacquev6/PyGithub/issues/196>`_ ``Github.get_hook(name)``. Thank you `klmitch <https://github.com/klmitch>`_ for asking
* In case bad data is returned by Github API v3, `raise <https://github.com/jacquev6/PyGithub/issues/195>`_ an exception only when the user accesses the faulty attribute, not when constructing the object containing this attribute. Thank you `klmitch <https://github.com/klmitch>`_ for asking
* `Fix <https://github.com/jacquev6/PyGithub/issues/199>`_ parameter public/private of ``Repository.edit``. Thank you `daireobroin449 <https://github.com/daireobroin449>`_ for reporting the issue
* Remove ``Repository.create_download`` and ``NamedUser.create_gist`` as the corrensponding APIs are not documented anymore

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
