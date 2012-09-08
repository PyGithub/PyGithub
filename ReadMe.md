This is a Python library to access the [Github API v3](http://developer.github.com/v3).

With it, you can manage your [Github](http://github.com) resources (repositories, user profiles, organizations, etc.) from Python scripts.

It covers the **full** API, and all methods are tested against the real Github site.

Should you have any question, or if you find a bug, or if there is something you can do with the API but not with PyGithub, please [open an issue](https://github.com/jacquev6/PyGithub/issues).

PyGithub is stable. I will maintain it up to date with the API, and fix bugs if any, but I don't plan new heavy developments.

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

Licensing
=========

PyGithub is distributed under the GNU Lesser General Public Licence.
See files COPYING and COPYING.LESSER, as requested by [GNU](http://www.gnu.org/licenses/gpl-howto.html).

Projects using PyGithub
=======================

([Open an issue](https://github.com/jacquev6/PyGithub/issues) if you want to be listed here, I'll be glad to add your project)

* [Upverter](https://upverter.com) is a web-based schematic capture and PCB layout tool for people who design electronics. Designers can attach a Github project to an Upverter project.
* [Tratihubis](http://pypi.python.org/pypi/tratihubis/) converts Trac tickets to Github issues

History
=======

[Version 1.6](https://github.com/jacquev6/PyGithub/issues?milestone=10&state=closed) (September 8th, 2012)
----------------------------------------------------------------------------------------------------------

* Restore support for Python 2.5
* Implement new APIS:
    * /hooks (undocumented, but mentioned in http://developer.github.com/v3/repos/hooks/#create-a-hook)
    * [Merging](http://developer.github.com/v3/repos/merging/)
    * [Starring](http://developer.github.com/v3/repos/starring/) and [subscriptions](http://developer.github.com/v3/repos/watching/)
    * [Assignees](http://developer.github.com/v3/issues/assignees/)
    * [Commit statuses](http://developer.github.com/v3/repos/statuses/)
    * [Contents](http://developer.github.com/v3/repos/contents/), thank you [berndca](https://github.com/berndca) for asking
* Clarify issue and review comments on PullRequest, thank you [nixoz2k7](https://github.com/nixoz2k7) for asking

[Version 1.5](https://github.com/jacquev6/PyGithub/issues?milestone=9&state=closed) (September 5th, 2012)
---------------------------------------------------------------------------------------------------------

* Add a timeout option, thank you much [xobb1t](https://github.com/xobb1t) for the merge request. *This drops Python 2.5 support*. I may be able to restore it in next version.
* Implement `Repository.delete`, thank you [pmchen](https://github.com/pmchen) for asking

[Version 1.4](https://github.com/jacquev6/PyGithub/issues?milestone=8&state=closed) (August 4th, 2012)
------------------------------------------------------------------------------------------------------

* Allow connection to a custom Github URL, for Github Enterprise, thank you very much [engie](https://github.com/engie) for the merge request

[Version 1.3](https://github.com/jacquev6/PyGithub/issues?milestone=7&state=closed) (July 13th, 2012)
-----------------------------------------------------------------------------------------------------

* Implement [markdown rendering](http://developer.github.com/v3/markdown/)
* `GitAuthor.date` is now a datetime, thank you [bilderbuchi](https://github.com/bilderbuchi)
* Fix documentation of `Github.get_gist`: `id` is a string, not an integer

[Version 1.2](https://github.com/jacquev6/PyGithub/issues?milestone=6&state=closed) (June 29th, 2012)
-----------------------------------------------------------------------------------------------------

* Implement [legacy search APIs](http://developer.github.com/v3/search/), thank you [kukuts](https://github.com/kukuts) for telling me Github had released them
* Fix a bug with issue labels containing spaces, thank you [philipkimmey](https://github.com/philipkimmey) for detecting the bug and fixing it
* Clarify how collections of objects are returned by `get_*` methods, thank you [bilderbuchi](https://github.com/bilderbuchi) for asking

Version 1.1 (June 20th, 2012)
-----------------------------

* Restore compatibility with Python 2.5, thank you [pmuilu](https://github.com/pmuilu)
* Use `package_data` instead of `data_files` for documentation files in `setup.py`, thank you [malexw](https://github.com/malexw) for reporting

[Version 1.0](https://github.com/jacquev6/PyGithub/issues?milestone=2&state=closed) (June 3rd, 2012)
----------------------------------------------------------------------------------------------------

* Complete rewrite, with no more complicated meta-description
* Full typing of attributes and parameters
* Full documentation of attributes and parameters
* More usable exceptions raised in case on problems with the API
* Some bugs and limitations fixed, special thanks to [bilderbuchi](https://github.com/bilderbuchi), [roskakori](https://github.com/roskakori) and [tallforasmurf](https://github.com/tallforasmurf) for reporting them!

[Version 0.7](https://github.com/jacquev6/PyGithub/issues?milestone=5&state=closed) (May 26th, 2012)
----------------------------------------------------------------------------------------------------

* Use PyGithub with OAuth authentication or with no authentication at all

[Version 0.6](https://github.com/jacquev6/PyGithub/issues?milestone=4&state=closed) (April 17th, 2012)
------------------------------------------------------------------------------------------------------

* Fix [issue 21](https://github.com/jacquev6/PyGithub/issues/21) (KeyError when accessing repositories)
* Re-completed the API with NamedUser.create_gist


[Version 0.5](https://github.com/jacquev6/PyGithub/issues?milestone=3&state=closed) (March 19th, 2012)
------------------------------------------------------------------------------------------------------

* Major achievement: **all APIs are implemented**
* More refactoring, of course

[Version 0.4](https://github.com/jacquev6/PyGithub/issues?milestone=1&state=closed) (March 12th, 2012)
------------------------------------------------------------------------------------------------------

* The list of the not implemented APIs is shorter than the list of the implemented APIs
* APIs *not implemented*:
    * GET `/gists/public`
    * GET `/issues`
    * GET `/repos/:user/:repo/compare/:base...:head`
    * GET `/repos/:user/:repo/git/trees/:sha?recursive=1`
    * POST `/repos/:user/:repo/git/trees?base_tree=`
* Gists
* Autorizations
* Keys
* Hooks
* Events
* Merge pull requests
* More refactoring, one more time

Version 0.3 (February 26th, 2012)
---------------------------------

* More refactoring
* Issues, milestones and their labels
* NamedUser:
    * emails
* Repository:
    * downloads
    * tags, branches, commits and comments (not the same as "Git objects" of version 0.2)
    * pull requests (no automatic merge yet)
* Automatic generation of the reference documentation of classes, with less "see API"s, and less errors

Version 0.2 (February 23rd, 2012)
---------------------------------

* Refactoring
* Teams details and modification
    * basic attributes
    * list teams in organizations, on repositories
* Git objects
    * create and get tags, references, commits, trees, blobs
    * list and edit references

Version 0.1 (February 19th, 2012)
---------------------------------

* User details and modification
    * basic attributes
    * followers, following, watching
    * organizations
    * repositories
* Repository details and modification
    * basic attributes
    * forking
    * collaborators, contributors, watchers
* Organization details and modification
    * basic attributes
    * members and public members
