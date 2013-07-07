This is a Python (2 and 3) library to access the `Github API v3 <http://developer.github.com/v3>`_.
With it, you can manage your `Github <http://github.com>`_ resources (repositories, user profiles, organizations, etc.) from Python scripts.

It covers the **full** API, and all methods are tested against the real Github site.

Should you have any question, any remark, or if you find a bug, or if there is something you can do with the API but not with PyGithub, please `open an issue <https://github.com/jacquev6/PyGithub/issues>`_.

PyGithub is stable. I will maintain it up to date with the API, and fix bugs if any, but I don't plan new heavy developments.

What's new?
===========

Summer 2013 - I'm traveling
---------------------------

You may have noticed I'm a bit slower than usual to manage your issues and pull requests.
That's because I'm traveling a lot this summer. Please be patient.

`Version 1.17.0 <https://github.com/jacquev6/PyGithub/issues?milestone=29&state=closed>`_ (Jully 7th, 2013) (Hamburg edition)
-----------------------------------------------------------------------------------------------------------------------------

* `Fix <https://github.com/jacquev6/PyGithub/pull/176>`_ bug in ``Repository.get_comment`` when using custom ``per_page``. Thank you `davidbrai <https://github.com/davidbrai>`_
* `Handle <https://github.com/jacquev6/PyGithub/pull/174>`_ Http redirects in ``Repository.get_dir_contents``. Thank you `MarkRoddy <https://github.com/MarkRoddy>`_
* `Implement <https://github.com/jacquev6/PyGithub/issues/173>`_ API ``/user`` in ``Github.get_users``. Thank you `rakeshcusat <https://github.com/rakeshcusat>`_ for asking
* `Improve <https://github.com/jacquev6/PyGithub/pull/171>`_ the documentation. Thank you `martinqt <https://github.com/martinqt>`_

Documentation
=============

All the documentation is here: http://jacquev6.github.com/PyGithub.
