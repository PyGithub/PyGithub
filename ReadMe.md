This is a Python library to access the [Github API v3](http://developer.github.com/v3).

With it, you can manage your [Github](http://github.com) resources (repositories, user profiles, organizations, etc.) from Python scripts.

It covers the **full** API, and all methods are tested against the real Github site.

Should you have any question, or if you find a bug, or if there is something you can do with the API but not with PyGithub, please [open an issue](https://github.com/jacquev6/PyGithub/issues).

PyGithub is stable. I will maintain it up to date with the API, and fix bugs if any, but I don't plan new heavy developments.

What's new?
===========

[Version 1.7](https://github.com/jacquev6/PyGithub/issues?milestone=12&state=closed) (September 12th, 2012)
-----------------------------------------------------------------------------------------------------------

* Be able to clear the assignee and the milestone of an Issue. Thank you [quixotique](https://github.com/quixotique) for the merge request
* Fix an AssertionFailure in `Organization.get_xxx` when using Github Enterprise. Thank you [mnsanghvi](https://github.com/mnsanghvi) for pointing that
* Expose pagination to users needing it (`PaginatedList.get_page`). Thank you [kukuts](https://github.com/kukuts) for asking
* Improve handling of legacy search APIs
* Small refactoring (documentation, removal of old code generation artifacts)

Previous versions
-----------------

See [ChangeLog](https://github.com/jacquev6/PyGithub/blob/master/doc/ChangeLog.md).

Download and install
====================

This package is in the [Python Package Index](http://pypi.python.org/pypi/PyGithub), so `easy_install PyGithub` or `pip install PyGithub` should be enough.
You can also clone it on [Github](http://github.com/jacquev6/PyGithub).

Tutorial
========

First create a Gihtub instance:

    from github import Github

    g = Github( "user", "password" )

Then play with your Github objects:

    for repo in g.get_user().get_repos():
        print repo.name
        repo.edit( has_wiki = False )

You can also create a Github instance with an OAuth token:

    g = Github( token )

Or without authentication:

    g = Github()

Reference documentation
=======================

You need to use a Github API and wonder which class implements it? [Reference of APIs](https://github.com/jacquev6/PyGithub/blob/master/doc/ReferenceOfApis.md)

You want all the details about PyGithub classes? [Reference of classes](https://github.com/jacquev6/PyGithub/blob/master/doc/ReferenceOfClasses.md)

Licensing
=========

PyGithub is distributed under the GNU Lesser General Public Licence.
See files COPYING and COPYING.LESSER, as requested by [GNU](http://www.gnu.org/licenses/gpl-howto.html).

Projects using PyGithub
=======================

([Open an issue](https://github.com/jacquev6/PyGithub/issues) if you want to be listed here, I'll be glad to add your project)

* [Upverter](https://upverter.com) is a web-based schematic capture and PCB layout tool for people who design electronics. Designers can attach a Github project to an Upverter project.
* [Tratihubis](http://pypi.python.org/pypi/tratihubis/) converts Trac tickets to Github issues
