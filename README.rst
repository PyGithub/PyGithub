This is a Python (2 and 3) library to access the `Github API v3 <http://developer.github.com/v3>`_.
With it, you can manage your `Github <http://github.com>`_ resources (repositories, user profiles, organizations, etc.) from Python scripts.

It covers the **full** API, and all methods are tested against the real Github site.

Should you have any question, any remark, or if you find a bug, or if there is something you can do with the API but not with PyGithub, please `open an issue <https://github.com/jacquev6/PyGithub/issues>`_.

PyGithub is stable. I will maintain it up to date with the API, and fix bugs if any, but I don't plan new heavy developments.

What's new?
===========

Version 1.13.1 (March 28nd, 2013)
---------------------------------

* `Fix <https://github.com/jacquev6/PyGithub/issues/153>`_ login/password authentication for Python 3. Thank you `sebastianstigler <https://github.com/sebastianstigler>`_ for reporting

`Version 1.13.0 <https://github.com/jacquev6/PyGithub/issues?milestone=23&state=closed>`_ (March 22nd, 2013)
------------------------------------------------------------------------------------------------------------

* `Fix <https://github.com/jacquev6/PyGithub/issues/143>`_ for Python 3 on case-insensitive file-systems. Thank you `ptwobrussell <https://github.com/ptwobrussell>`_ for reporting
* `Expose <https://github.com/jacquev6/PyGithub/issues/144>`_ raw data returned by Github for all objects. Thank you `ptwobrussell <https://github.com/ptwobrussell>`_ for asking
* `Add <https://github.com/jacquev6/PyGithub/issues/145>`_ a property ``Github.per_page`` (and a parameter to the constructor) to change the number of items requested in paginated requests. Thank you again `ptwobrussell <https://github.com/ptwobrussell>`_ for asking
* `Implement <https://github.com/jacquev6/PyGithub/pull/148>`_ the first part of the `Notifications <http://developer.github.com/changes/2012-10-26-notifications-api/>`_ API. Thank you `pgolm <https://github.com/pgolm>`_
* `Fix <https://github.com/jacquev6/PyGithub/issues/149>`_ automated tests on Python 3.3. Thank you `bkabrda <https://github.com/bkabrda>`_ for reporting

Documentation
=============

All the documentation is here: http://jacquev6.github.com/PyGithub.
