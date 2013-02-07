This is a Python (2 and 3) library to access the `Github API v3 <http://developer.github.com/v3>`_.

With it, you can manage your `Github <http://github.com>`_ resources (repositories, user profiles, organizations, etc.) from Python scripts.

It covers the **full** API, and all methods are tested against the real Github site.

Should you have any question, any remark, or if you find a bug, or if there is something you can do with the API but not with PyGithub, please `open an issue <https://github.com/jacquev6/PyGithub/issues>`_.

PyGithub is stable. I will maintain it up to date with the API, and fix bugs if any, but I don't plan new heavy developments.

What's new?
===========

`![Build Status](https://secure.travis-ci.org/jacquev6/PyGithub.png)] <http://travis-ci.org/jacquev6/PyGithub>`_

Next version
------------

* Much better documentation http://jacquev6.github.com/PyGithub.

`Version 1.10.0 <https://github.com/jacquev6/PyGithub/issues?milestone=16&state=closed>`_ (December 25th, 2012) (Christmas 2012 edition)
----------------------------------------------------------------------------------------------------------------------------------------

* Major improvement: support Python 3! PyGithub is automaticaly tested on `Travis <http://travis-ci.org/jacquev6/PyGithub>`_ with versions 2.5, 2.6, 2.7, 3.1 and 3.2 of Python
* Add a shortcut function 'Github.get_repo' to get a repo directly from its full name. thank you `lwc <https://github.com/lwc>`_ for the contribution
* 'Github.get_gitignore_templates' and 'Github.get_gitignore_template' for APIs '/gitignore/templates'
* Add the optional 'ref' parameter to 'Repository.get_contents' and 'get_readme'. Thank you `fixxxeruk <https://github.com/fixxxeruk>`_ for the contribution
* Get comments for all issues and all pull requests on a repository ('GET /repos/:user/:repo/pulls/comments': 'Repository.get_pulls_comments' or 'Repository.get_pulls_review_comments'; 'GET /repos/:user/:repo/issues/comments': 'Repository.get_issues_comments')

Previous versions
-----------------

See `ChangeLog <https://github.com/jacquev6/PyGithub/blob/master/doc/ChangeLog.md>`_.

Dcumentation
============

All the documentation is here: http://jacquev6.github.com/PyGithub.

Licensing
=========

PyGithub is distributed under the GNU Lesser General Public Licence.
See files COPYING and COPYING.LESSER, as requested by `GNU <http://www.gnu.org/licenses/gpl-howto.html>`_.

Projects using PyGithub
=======================

(`Open an issue <https://github.com/jacquev6/PyGithub/issues>`_ if you want to be listed here, I'll be glad to add your project)

* `Upverter <https://upverter.com>`_ is a web-based schematic capture and PCB layout tool for people who design electronics. Designers can attach a Github project to an Upverter project.
* `Tratihubis <http://pypi.python.org/pypi/tratihubis/>`_ converts Trac tickets to Github issues
* https://github.com/CMB/cligh
* https://github.com/natduca/quickopen uses PyGithub to automaticaly create issues
* https://gist.github.com/3433798
* https://github.com/zsiciarz/aquila-dsp.org
* https://github.com/robcowie/virtualenvwrapper.github

They talk about PyGithub
========================

* http://stackoverflow.com/questions/10625190/most-suitable-python-library-for-github-api-v3
* http://stackoverflow.com/questions/12379637/django-social-auth-github-authentication
* http://www.freebsd.org/cgi/cvsweb.cgi/ports/devel/py-pygithub/
* http://oddshocks.com/blog/2012/08/02/developing-charsheet/
