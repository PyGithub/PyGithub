This is a Python (2 and 3) library to access the `Github API v3 <http://developer.github.com/v3>`_.
With it, you can manage your `Github <http://github.com>`_ resources (repositories, user profiles, organizations, etc.) from Python scripts.

It covers the **full** API, and all methods are tested against the real Github site.

Should you have any question, any remark, or if you find a bug, or if there is something you can do with the API but not with PyGithub, please `open an issue <https://github.com/jacquev6/PyGithub/issues>`_.

PyGithub is stable. I will maintain it up to date with the API, and fix bugs if any, but I don't plan new heavy developments.

What's new?
===========

`Version 1.14.2 <https://github.com/jacquev6/PyGithub/issues?milestone=27&state=closed>`_ (April 25th, 2013)
------------------------------------------------------------------------------------------------------------

* `Fix <https://github.com/jacquev6/PyGithub/issues/158>`_ paginated requests when using secret-key oauth. Thank you `jseabold <https://github.com/jseabold>`_ for analysing the bug

`Version 1.14.1 <https://github.com/jacquev6/PyGithub/issues?milestone=26&state=closed>`_ (April 25th, 2013)
------------------------------------------------------------------------------------------------------------

* Set the default User-Agent header to "PyGithub/Python". (Github has `enforced the User Agent header <http://developer.github.com/changes/2013-04-24-user-agent-required/>`_ yesterday.) Thank you `jjh42 <https://github.com/jjh42>`_ for `the fix <https://github.com/jacquev6/PyGithub/pull/161>`_, thank you `jasenmh <https://github.com/jasenmh>`_ and `pconrad <https://github.com/pconrad>`_ for reporting `the issue <https://github.com/jacquev6/PyGithub/issues/160>`_.

`Version 1.14.0 <https://github.com/jacquev6/PyGithub/issues?milestone=24&state=closed>`_ (April 22nd, 2013)
------------------------------------------------------------------------------------------------------------

* `Improve <https://github.com/jacquev6/PyGithub/issues/156>`_ gist edition. Thank you `jasonwiener <https://github.com/jasonwiener>`_ for asking:

  * Delete a file with ``gist.edit(files={"name.txt": None})``
  * Rename a file with ``gist.edit(files={"old_name.txt": github.InputFileContent(gist.files["old_name.txt"].content, new_name="new_name.txt")})``

* `Raise <https://github.com/jacquev6/PyGithub/issues/152>`_ specific exceptions. Thank you `pconrad <https://github.com/pconrad>`_ for giving me the idea

Documentation
=============

All the documentation is here: http://jacquev6.github.com/PyGithub.
