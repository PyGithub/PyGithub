This is a Python (2 and 3) library to access the [Github API v3](http://developer.github.com/v3).

With it, you can manage your [Github](http://github.com) resources (repositories, user profiles, organizations, etc.) from Python scripts.

It covers the **full** API, and all methods are tested against the real Github site.

Should you have any question, or if you find a bug, or if there is something you can do with the API but not with PyGithub, please [open an issue](https://github.com/jacquev6/PyGithub/issues).

PyGithub is stable. I will maintain it up to date with the API, and fix bugs if any, but I don't plan new heavy developments.

What's new?
===========

[![Build Status](https://travis-ci.org/jacquev6/PyGithub.png?branch=master)](https://travis-ci.org/jacquev6/PyGithub)

[Version 1.11.1](https://github.com/jacquev6/PyGithub/issues?milestone=21&state=closed) (February 9th, 2013) (London edition)
-----------------------------------------------------------------------------------------------------------------------------

* Fix [bug](https://github.com/jacquev6/PyGithub/issues/139#issuecomment-13280121) in lazy completion. Thank you [ianozsvald](https://github.com/ianozsvald) for pinpointing it

[Version 1.11.0](https://github.com/jacquev6/PyGithub/issues?milestone=19&state=closed) (February 7th, 2013)
------------------------------------------------------------------------------------------------------------

* Fix bug in PaginatedList without url parameters. Thank you [llimllib](https://github.com/llimllib) for the [contribution](https://github.com/jacquev6/PyGithub/pull/133)
* [Implement](https://github.com/jacquev6/PyGithub/issues/130) `NamedUser.get_keys`
* [Support PubSubHub](https://github.com/jacquev6/PyGithub/issues/129): `Repository.subscribe_to_hub` and `Repository.unsubscribe_from_hub`
* [Publish the oauth scopes](https://github.com/jacquev6/PyGithub/issues/134) in Github.oauth_scopes, thank you [ bilderbuchi](https://github.com/ bilderbuchi) for asking

Previous versions
-----------------

See [ChangeLog](doc/ChangeLog.md).

Download and install
====================

This package is in the [Python Package Index](http://pypi.python.org/pypi/PyGithub), so `easy_install PyGithub` or `pip install PyGithub` should be enough.
You can also clone it on [Github](http://github.com/jacquev6/PyGithub).

Tutorial
========

First create a Github instance:

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

You need to use a Github API and wonder which class implements it? [Reference of APIs](doc/ReferenceOfApis.md)

You want all the details about PyGithub classes? [Reference of classes](doc/ReferenceOfClasses.md)

Licensing
=========

PyGithub is distributed under the GNU Lesser General Public Licence.
See files COPYING and COPYING.LESSER, as requested by [GNU](http://www.gnu.org/licenses/gpl-howto.html).

Contributing
============

Please see [Contributing.md](Contributing.md).

Projects using PyGithub
=======================

([Open an issue](https://github.com/jacquev6/PyGithub/issues) if you want to be listed here, I'll be glad to add your project)

* [Upverter](https://upverter.com) is a web-based schematic capture and PCB layout tool for people who design electronics. Designers can attach a Github project to an Upverter project.
* [Notifico](http://n.tkte.ch) receives messages (such as commits and issues) from services and scripts and delivers them to IRC channels. It can import/sync from Github.
* [Tratihubis](http://pypi.python.org/pypi/tratihubis/) converts Trac tickets to Github issues
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
