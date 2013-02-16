Change log
==========

Stable versions
~~~~~~~~~~~~~~~

`Version 1.11.1 <https://github.com/jacquev6/PyGithub/issues?milestone=21&state=closed>`_ (February 9th, 2013) (London edition)
-------------------------------------------------------------------------------------------------------------------------------

* Fix `bug <https://github.com/jacquev6/PyGithub/issues/139#issuecomment-13280121>`_ in lazy completion. Thank you `ianozsvald <https://github.com/ianozsvald>`_ for pinpointing it

`Version 1.11.0 <https://github.com/jacquev6/PyGithub/issues?milestone=19&state=closed>`_ (February 7th, 2013)
--------------------------------------------------------------------------------------------------------------

* Fix bug in PaginatedList without url parameters. Thank you `llimllib <https://github.com/llimllib>`_ for the `contribution <https://github.com/jacquev6/PyGithub/pull/133>`_
* `Implement <https://github.com/jacquev6/PyGithub/issues/130>`_ :meth:`github.NamedUser.NamedUser.get_keys`
* `Support PubSubHub <https://github.com/jacquev6/PyGithub/issues/129>`_: :meth:`github.Repository.Repository.subscribe_to_hub` and :meth:`github.Repository.Repository.unsubscribe_from_hub`
* `Publish the oauth scopes <https://github.com/jacquev6/PyGithub/issues/134>`_ in :attr:`github.Github.Github.oauth_scopes`, thank you `bilderbuchi <https://github.com/bilderbuchi>`_ for asking

`Version 1.10.0 <https://github.com/jacquev6/PyGithub/issues?milestone=16&state=closed>`_ (December 25th, 2012) (Christmas 2012 edition)
----------------------------------------------------------------------------------------------------------------------------------------

* Major improvement: support Python 3! PyGithub is automaticaly tested on `Travis <http://travis-ci.org/jacquev6/PyGithub>`_ with versions 2.5, 2.6, 2.7, 3.1 and 3.2 of Python
* Add a shortcut function :meth:`github.Github.Github.get_repo` to get a repo directly from its full name. thank you `lwc <https://github.com/lwc>`_ for the contribution
* :meth:`github.Github.Github.get_gitignore_templates` and :meth:`github.Github.Github.get_gitignore_template` for APIs ``/gitignore/templates``
* Add the optional ``ref`` parameter to :meth:`github.Repository.Repository.get_contents` and :meth:`github.Repository.Repository.get_readme`. Thank you `fixxxeruk <https://github.com/fixxxeruk>`_ for the contribution
* Get comments for all issues and all pull requests on a repository (``GET /repos/:user/:repo/pulls/comments``: :meth:`github.Repository.Repository.get_pulls_comments` or :meth:`github.Repository.Repository.get_pulls_review_comments`; ``GET /repos/:user/:repo/issues/comments``: :meth:`github.Repository.Repository.get_issues_comments`)

`Version 1.9.1 <https://github.com/jacquev6/PyGithub/issues?milestone-17&state-closed>`_ (November 20th, 2012)
--------------------------------------------------------------------------------------------------------------

* Fix an assertion failure when integers returned by Github do not fit in a Python ``int``

`Version 1.9.0 <https://github.com/jacquev6/PyGithub/issues?milestone-14&state-closed>`_ (November 19th, 2012)
--------------------------------------------------------------------------------------------------------------

* You can now use your client_id and client_secret to increase rate limiting without authentication
* You can now send a custom User-Agent
* PullRequest now has its 'assignee' attribute, thank you `mstead <https://github.com/mstead>`_
* Repository.edit now has 'default_branch' parameter
* create_repo has 'auto_init' and 'gitignore_template' parameters
* GistComment URL is changed (see http://developer.github.com/changes/2012-10-31-gist-comment-uris)
* A typo in the readme was fixed by `tymofij <https://github.com/tymofij>`_, thank you
* Internal stuff:

  + Add encoding comment to Python files, thank you `Zearin <https://github.com/Zearin>`_
  + Restore support of Python 2.5
  + Restore coverage measurement in setup.py test
  + Small refactoring

`Version 1.8.1 <https://github.com/jacquev6/PyGithub/issues?milestone-15&state-closed>`_ (October 28th, 2012)
-------------------------------------------------------------------------------------------------------------

* Repository.get_git_ref prepends "refs/" to the requested references. Thank you `simon-weber <https://github.com/simon-weber>`_ for noting the incoherence between documentation and behavior. If you feel like it's a breaking change, please see `this issue <https://github.com/jacquev6/PyGithub/issues/104>`_

`Version 1.8.0 <https://github.com/jacquev6/PyGithub/issues?milestone-13&state-closed>`_ (September 30th, 2012)
---------------------------------------------------------------------------------------------------------------

* Enable `Travis CI <http://travis-ci.org/#!/jacquev6/PyGithub>`_
* Fix error 500 when json payload contains percent character (`%`). Thank you again `quixotique <https://github.com/quixotique>`_ for pointing that and reporting it to Github
* Enable debug logging. Logger name is `"github"`. Simple logging can be enabled by `github.enable_console_debug_logging()`. Thank you `quixotique <https://github.com/quixotique>`_ for the merge request and the advice
* Publish tests in the PyPi source archive to ease QA tests of the `FreeBSD port <http://www.freshports.org/devel/py-pygithub>`_. Thank you `koobs <https://github.com/koobs>`_ for maintaining this port
* Switch to `Semantic Versioning <http://semver.org/>`_
* Respect `pep8 Style Guide for Python Code <http://www.python.org/dev/peps/pep-0008>`_

`Version 1.7 <https://github.com/jacquev6/PyGithub/issues?milestone-12&state-closed>`_ (September 12th, 2012)
-------------------------------------------------------------------------------------------------------------

* Be able to clear the assignee and the milestone of an Issue. Thank you `quixotique <https://github.com/quixotique>`_ for the merge request
* Fix an AssertionFailure in `Organization.get_xxx` when using Github Enterprise. Thank you `mnsanghvi <https://github.com/mnsanghvi>`_ for pointing that
* Expose pagination to users needing it (`PaginatedList.get_page`). Thank you `kukuts <https://github.com/kukuts>`_ for asking
* Improve handling of legacy search APIs
* Small refactoring (documentation, removal of old code generation artifacts)

`Version 1.6 <https://github.com/jacquev6/PyGithub/issues?milestone-10&state-closed>`_ (September 8th, 2012)
------------------------------------------------------------------------------------------------------------

* Restore support for Python 2.5
* Implement new APIS:

  * /hooks (undocumented, but mentioned in http://developer.github.com/v3/repos/hooks/#create-a-hook)
  * `Merging <http://developer.github.com/v3/repos/merging>`_
  * `Starring <http://developer.github.com/v3/repos/starring>`_ and `subscriptions <http://developer.github.com/v3/repos/watching>`_
  * `Assignees <http://developer.github.com/v3/issues/assignees>`_
  * `Commit statuses <http://developer.github.com/v3/repos/statuses>`_
  * `Contents <http://developer.github.com/v3/repos/contents>`_, thank you `berndca <https://github.com/berndca>`_ for asking

* Clarify issue and review comments on PullRequest, thank you `nixoz2k7 <https://github.com/nixoz2k7>`_ for asking

`Version 1.5 <https://github.com/jacquev6/PyGithub/issues?milestone-9&state-closed>`_ (September 5th, 2012)
-----------------------------------------------------------------------------------------------------------

* Add a timeout option, thank you much `xobb1t <https://github.com/xobb1t>`_ for the merge request. *This drops Python 2.5 support*. I may be able to restore it in next version.
* Implement `Repository.delete`, thank you `pmchen <https://github.com/pmchen>`_ for asking

`Version 1.4 <https://github.com/jacquev6/PyGithub/issues?milestone-8&state-closed>`_ (August 4th, 2012)
--------------------------------------------------------------------------------------------------------

* Allow connection to a custom Github URL, for Github Enterprise, thank you very much `engie <https://github.com/engie>`_ for the merge request

`Version 1.3 <https://github.com/jacquev6/PyGithub/issues?milestone-7&state-closed>`_ (July 13th, 2012)
-------------------------------------------------------------------------------------------------------

* Implement `markdown rendering <http://developer.github.com/v3/markdown>`_
* `GitAuthor.date` is now a datetime, thank you `bilderbuchi <https://github.com/bilderbuchi>`_
* Fix documentation of `Github.get_gist`: `id` is a string, not an integer

`Version 1.2 <https://github.com/jacquev6/PyGithub/issues?milestone-6&state-closed>`_ (June 29th, 2012)
-------------------------------------------------------------------------------------------------------

* Implement `legacy search APIs <http://developer.github.com/v3/search>`_, thank you `kukuts <https://github.com/kukuts>`_ for telling me Github had released them
* Fix a bug with issue labels containing spaces, thank you `philipkimmey <https://github.com/philipkimmey>`_ for detecting the bug and fixing it
* Clarify how collections of objects are returned by `get_*` methods, thank you `bilderbuchi <https://github.com/bilderbuchi>`_ for asking

Version 1.1 (June 20th, 2012)
-----------------------------

* Restore compatibility with Python 2.5, thank you `pmuilu <https://github.com/pmuilu>`_
* Use `package_data` instead of `data_files` for documentation files in `setup.py`, thank you `malexw <https://github.com/malexw>`_ for reporting

`Version 1.0 <https://github.com/jacquev6/PyGithub/issues?milestone-2&state-closed>`_ (June 3rd, 2012)
------------------------------------------------------------------------------------------------------

* Complete rewrite, with no more complicated meta-description
* Full typing of attributes and parameters
* Full documentation of attributes and parameters
* More usable exceptions raised in case on problems with the API
* Some bugs and limitations fixed, special thanks to `bilderbuchi <https://github.com/bilderbuchi>`_, `roskakori <https://github.com/roskakori>`_ and `tallforasmurf <https://github.com/tallforasmurf>`_ for reporting them!

Pre-release versions
~~~~~~~~~~~~~~~~~~~~

`Version 0.7 <https://github.com/jacquev6/PyGithub/issues?milestone-5&state-closed>`_ (May 26th, 2012)
------------------------------------------------------------------------------------------------------

* Use PyGithub with OAuth authentication or with no authentication at all

`Version 0.6 <https://github.com/jacquev6/PyGithub/issues?milestone-4&state-closed>`_ (April 17th, 2012)
--------------------------------------------------------------------------------------------------------

* Fix `issue 21 <https://github.com/jacquev6/PyGithub/issues/21>`_ (KeyError when accessing repositories)
* Re-completed the API with NamedUser.create_gist


`Version 0.5 <https://github.com/jacquev6/PyGithub/issues?milestone-3&state-closed>`_ (March 19th, 2012)
--------------------------------------------------------------------------------------------------------

* Major achievement: **all APIs are implemented**
* More refactoring, of course

`Version 0.4 <https://github.com/jacquev6/PyGithub/issues?milestone-1&state-closed>`_ (March 12th, 2012)
--------------------------------------------------------------------------------------------------------

* The list of the not implemented APIs is shorter than the list of the implemented APIs
* APIs *not implemented*:

  * GET `/gists/public`
  * GET `/issues`
  * GET `/repos/:user/:repo/compare/:base...:head`
  * GET `/repos/:user/:repo/git/trees/:sha?recursive-1`
  * POST `/repos/:user/:repo/git/trees?base_tree-`

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
