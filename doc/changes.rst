Change log
==========

Stable versions
~~~~~~~~~~~~~~~

Version 1.25.2 (October 7th, 2014)
----------------------------------

* `Work around <https://github.com/jacquev6/PyGithub/issues/278>`__ the GitHub API v3 returning `null`s in some paginated responses, `erichaase <https://github.com/erichaase>`__ for the bug report

Version 1.25.1 (September 28th, 2014)
-------------------------------------

* `Fix <https://github.com/jacquev6/PyGithub/pull/275>`__ two-factor authentication header, thanks to `tradej <https://github.com/tradej>`__ for the pull request

`Version 1.25.0 <https://github.com/jacquev6/PyGithub/issues?milestone=38&state=closed>`_ (May 4th, 2014)
---------------------------------------------------------------------------------------------------------

* `Implement <https://github.com/jacquev6/PyGithub/pull/246>`__ getting repos by id, thanks to `tylertreat <https://github.com/tylertreat>`__ for the pull request
* `Add <https://github.com/jacquev6/PyGithub/pull/247>`__ ``Gist.owner``, thanks to `dalejung <https://github.com/dalejung>`__ for the pull request

`Version 1.24.1 <https://github.com/jacquev6/PyGithub/issues?milestone=37&state=closed>`_ (March 16th, 2014)
---------------------------------------------------------------------------------------------------------------

* `Fix <https://github.com/jacquev6/PyGithub/pull/237>`__ urlquoting in search, thanks to `cro <https://github.com/cro>`__ for the pull request

`Version 1.24.0 <https://github.com/jacquev6/PyGithub/issues?milestone=36&state=closed>`_ (March 2nd, 2014)
---------------------------------------------------------------------------------------------------------------

* `Implement <https://github.com/jacquev6/PyGithub/pull/224>`__ search, thanks to `thialfihar <https://github.com/thialfihar>`__ for the pull request

`Version 1.23.0 <https://github.com/jacquev6/PyGithub/issues?milestone=35&state=closed>`_ (December 23th, 2013)
---------------------------------------------------------------------------------------------------------------

* `Fix <https://github.com/jacquev6/PyGithub/issues/216>`__ all that is based on headers in Python 3 (pagination, conditional request, rate_limit...), huge thanks to `cwarren-mw <https://github.com/cwarren-mw>`__ for finding the bug
* `Accept <https://github.com/jacquev6/PyGithub/pull/218>`__ strings for assignees and collaborators, thanks to `farrd <https://github.com/farrd>`__
* `Ease <https://github.com/jacquev6/PyGithub/pull/220>`__ two-factor authentication by adding 'onetime_password' to AuthenticatedUser.create_authorization, thanks to `cameronbwhite <https://github.com/cameronbwhite>`__

`Version 1.22.0 <https://github.com/jacquev6/PyGithub/issues?milestone=34&state=closed>`_ (December 15th, 2013)
---------------------------------------------------------------------------------------------------------------

* `Emojis <https://github.com/jacquev6/PyGithub/pull/209>`__, thanks to `evolvelight <https://github.com/evolvelight>`__
* `Repository.stargazers_count <https://github.com/jacquev6/PyGithub/pull/212>`__, thanks to `cameronbwhite <https://github.com/cameronbwhite>`__
* `User.get_teams <https://github.com/jacquev6/PyGithub/pull/213>`__, thanks to `poulp <https://github.com/poulp>`__

`Version 1.21.0 <https://github.com/jacquev6/PyGithub/issues?milestone=33&state=closed>`__ (November ??th, 2013)
----------------------------------------------------------------------------------------------------------------

* `Accept <https://github.com/jacquev6/PyGithub/issues/202>`__ strings as well as ``Label`` objects in ``Issue.add_to_labels``, ``Issue.remove_from_labels`` and ``Issue.set_labels``. Thank you `acdha <https://github.com/acdha>`__ for asking
* `Implement <https://github.com/jacquev6/PyGithub/issues/201>`__ equality comparison for *completable* github objects (ie. those who have a ``url`` attribute). Warning, comparison is still not implemented for non-completable objects. This will be done in version 2.0 of PyGithub. Thank you `OddBloke <https://github.com/OddBloke>`__ for asking
* `Add <https://github.com/jacquev6/PyGithub/issues/204>`__ parameter ``author`` to ``Repository.get_commits``. Thank you `naorrosenberg <https://github.com/naorrosenberg>`__ for asking
* `Implement <https://github.com/jacquev6/PyGithub/issues/203>`__ the statistics end points. Thank you `naorrosenberg <https://github.com/naorrosenberg>`__ for asking

`Version 1.20.0 <https://github.com/jacquev6/PyGithub/issues?milestone=32&state=closed>`__ (October 20th, 2013) (First Seattle edition)
---------------------------------------------------------------------------------------------------------------------------------------

* `Implement <https://github.com/jacquev6/PyGithub/issues/196>`__ ``Github.get_hook(name)``. Thank you `klmitch <https://github.com/klmitch>`__ for asking
* In case bad data is returned by Github API v3, `raise <https://github.com/jacquev6/PyGithub/issues/195>`__ an exception only when the user accesses the faulty attribute, not when constructing the object containing this attribute. Thank you `klmitch <https://github.com/klmitch>`__ for asking
* `Fix <https://github.com/jacquev6/PyGithub/issues/199>`__ parameter public/private of ``Repository.edit``. Thank you `daireobroin449 <https://github.com/daireobroin449>`__ for reporting the issue
* Remove ``Repository.create_download`` and ``NamedUser.create_gist`` as the corrensponding APIs are not documented anymore

`Version 1.19.0 <https://github.com/jacquev6/PyGithub/issues?milestone=31&state=closed>`__ (September 8th, 2013) (AKFish's edition)
-----------------------------------------------------------------------------------------------------------------------------------

* Implement `conditional requests <http://developer.github.com/guides/getting-started/#conditional-requests>`__ by the method ``GithubObject.update``. Thank you very much `akfish <https://github.com/akfish>`__ for the pull request and your collaboration!
* Implement persistence of PyGithub objects: ``Github.save`` and ``Github.load``. Don't forget to ``update`` your objects after loading them, it won't decrease your rate limiting quota if nothing has changed. Again, thank you `akfish <https://github.com/akfish>`_
* Implement ``Github.get_repos`` to get all public repositories
* Implement ``NamedUser.has_in_following``
* `Implement <https://github.com/jacquev6/PyGithub/issues/188>`__ ``Github.get_api_status``, ``Github.get_last_api_status_message`` and ``Github.get_api_status_messages``. Thank you `ruxandraburtica <https://github.com/ruxandraburtica>`__ for asking
* Implement ``Github.get_rate_limit``
* Add many missing attributes
* Technical change: HTTP headers are now stored in retrieved objects. This is a base for new functionalities. Thank you `akfish <https://github.com/akfish>`__ for the pull request
* Use the new URL to fork gists (minor change)
* Use the new URL to test hooks (minor change)

`Version 1.18.0 <https://github.com/jacquev6/PyGithub/issues?milestone=30&state=closed>`__ (August 21st, 2013) (Bénodet edition)
--------------------------------------------------------------------------------------------------------------------------------

* `Issues <https://github.com/jacquev6/PyGithub/pull/181>`_' ``repository`` attribute will never be ``None``. Thank you `stuglaser <https://github.com/stuglaser>`__ for the pull request
* No more false assumption on `rate_limiting <https://github.com/jacquev6/PyGithub/pull/186>`_, and creation of ``rate_limiting_resettime``. Thank you `edjackson <https://github.com/edjackson>`__ for the pull request
* `New <https://github.com/jacquev6/PyGithub/pull/187>`__ parameters ``since`` and ``until`` to ``Repository.get_commits``. Thank you `apetresc <https://github.com/apetresc>`__ for the pull request
* `Catch <https://github.com/jacquev6/PyGithub/pull/182>`__ Json parsing exception for some internal server errors, and throw a better exception. Thank you `MarkRoddy <https://github.com/MarkRoddy>`__ for the pull request
* `Allow <https://github.com/jacquev6/PyGithub/pull/184>`__ reversed iteration of ``PaginatedList``. Thank you `davidbrai <https://github.com/davidbrai>`__ for the pull request

`Version 1.17.0 <https://github.com/jacquev6/PyGithub/issues?milestone=29&state=closed>`__ (Jully 7th, 2013) (Hamburg edition)
------------------------------------------------------------------------------------------------------------------------------

* `Fix <https://github.com/jacquev6/PyGithub/pull/176>`__ bug in ``Repository.get_comment`` when using custom ``per_page``. Thank you `davidbrai <https://github.com/davidbrai>`_
* `Handle <https://github.com/jacquev6/PyGithub/pull/174>`__ Http redirects in ``Repository.get_dir_contents``. Thank you `MarkRoddy <https://github.com/MarkRoddy>`_
* `Implement <https://github.com/jacquev6/PyGithub/issues/173>`__ API ``/user`` in ``Github.get_users``. Thank you `rakeshcusat <https://github.com/rakeshcusat>`__ for asking
* `Improve <https://github.com/jacquev6/PyGithub/pull/171>`__ the documentation. Thank you `martinqt <https://github.com/martinqt>`_

Version 1.16.0 (May 31th, 2013) (Concarneau edition)
----------------------------------------------------

* `Add <https://github.com/jacquev6/PyGithub/pull/170>`__ the html_url attribute to IssueComment and PullRequestComment

`Version 1.15.0 <https://github.com/jacquev6/PyGithub/issues?milestone=25&state=closed>`__ (May 17th, 2013) (Switzerland edition)
---------------------------------------------------------------------------------------------------------------------------------

* `Implement <https://github.com/jacquev6/PyGithub/issues/166>`__ listing of user issues with all parameters. Thank you Daehyok Shin for reporting
* `Raise <https://github.com/jacquev6/PyGithub/issues/152>`__ two new specific exceptions

`Version 1.14.2 <https://github.com/jacquev6/PyGithub/issues?milestone=27&state=closed>`__ (April 25th, 2013)
-------------------------------------------------------------------------------------------------------------

* `Fix <https://github.com/jacquev6/PyGithub/issues/158>`__ paginated requests when using secret-key oauth. Thank you `jseabold <https://github.com/jseabold>`__ for analysing the bug

`Version 1.14.1 <https://github.com/jacquev6/PyGithub/issues?milestone=26&state=closed>`__ (April 25th, 2013)
-------------------------------------------------------------------------------------------------------------

* Set the default User-Agent header to "PyGithub/Python". (Github has `enforced the User Agent header <http://developer.github.com/changes/2013-04-24-user-agent-required/>`__ yesterday.) Thank you `jjh42 <https://github.com/jjh42>`__ for `the fix <https://github.com/jacquev6/PyGithub/pull/161>`_, thank you `jasenmh <https://github.com/jasenmh>`__ and `pconrad <https://github.com/pconrad>`__ for reporting `the issue <https://github.com/jacquev6/PyGithub/issues/160>`_.

`Version 1.14.0 <https://github.com/jacquev6/PyGithub/issues?milestone=24&state=closed>`__ (April 22nd, 2013)
-------------------------------------------------------------------------------------------------------------

* `Improve <https://github.com/jacquev6/PyGithub/issues/156>`__ gist edition. Thank you `jasonwiener <https://github.com/jasonwiener>`__ for asking:

  * Delete a file with ``gist.edit(files={"name.txt": None})``
  * Rename a file with ``gist.edit(files={"old_name.txt": github.InputFileContent(gist.files["old_name.txt"].content, new_name="new_name.txt")})``

* `Raise <https://github.com/jacquev6/PyGithub/issues/152>`__ specific exceptions. Thank you `pconrad <https://github.com/pconrad>`__ for giving me the idea

Version 1.13.1 (March 28nd, 2013)
---------------------------------

* `Fix <https://github.com/jacquev6/PyGithub/issues/153>`__ login/password authentication for Python 3. Thank you `sebastianstigler <https://github.com/sebastianstigler>`__ for reporting

`Version 1.13.0 <https://github.com/jacquev6/PyGithub/issues?milestone=23&state=closed>`__ (March 22nd, 2013)
-------------------------------------------------------------------------------------------------------------

* `Fix <https://github.com/jacquev6/PyGithub/issues/143>`__ for Python 3 on case-insensitive file-systems. Thank you `ptwobrussell <https://github.com/ptwobrussell>`__ for reporting
* `Expose <https://github.com/jacquev6/PyGithub/issues/144>`__ raw data returned by Github for all objects. Thank you `ptwobrussell <https://github.com/ptwobrussell>`__ for asking
* `Add <https://github.com/jacquev6/PyGithub/issues/145>`__ a property :attr:`github.MainClass.Github.per_page` (and a parameter to the constructor) to change the number of items requested in paginated requests. Thank you again `ptwobrussell <https://github.com/ptwobrussell>`__ for asking
* `Implement <https://github.com/jacquev6/PyGithub/pull/148>`__ the first part of the `Notifications <http://developer.github.com/changes/2012-10-26-notifications-api/>`__ API. Thank you `pgolm <https://github.com/pgolm>`_
* `Fix <https://github.com/jacquev6/PyGithub/issues/149>`__ automated tests on Python 3.3. Thank you `bkabrda <https://github.com/bkabrda>`__ for reporting

Version 1.12.2 (March 3rd, 2013)
--------------------------------

* `Fix <https://github.com/jacquev6/PyGithub/issues/142>`__ major issue with Python 3: Json decoding was broken. Thank you `bilderbuchi <https://github.com/bilderbuchi>`__ for reporting

Version 1.12.1 (February 20th, 2013)
------------------------------------

* Nothing, but packaging/upload of 1.12.0 failed

`Version 1.12.0 <https://github.com/jacquev6/PyGithub/issues?milestone=22&state=closed>`__ (February 20th, 2013)
----------------------------------------------------------------------------------------------------------------

* Much better documentation: http://jacquev6.github.com/PyGithub
* `Implement <https://github.com/jacquev6/PyGithub/issues/140>`__ :meth:`github.Repository.Repository.get_dir_contents`. Thank you `ksookocheff-va <https://github.com/ksookocheff-va>`__ for asking

`Version 1.11.1 <https://github.com/jacquev6/PyGithub/issues?milestone=21&state=closed>`__ (February 9th, 2013) (London edition)
--------------------------------------------------------------------------------------------------------------------------------

* Fix `bug <https://github.com/jacquev6/PyGithub/issues/139#issuecomment-13280121>`__ in lazy completion. Thank you `ianozsvald <https://github.com/ianozsvald>`__ for pinpointing it

`Version 1.11.0 <https://github.com/jacquev6/PyGithub/issues?milestone=19&state=closed>`__ (February 7th, 2013)
---------------------------------------------------------------------------------------------------------------

* Fix bug in PaginatedList without url parameters. Thank you `llimllib <https://github.com/llimllib>`__ for the `contribution <https://github.com/jacquev6/PyGithub/pull/133>`_
* `Implement <https://github.com/jacquev6/PyGithub/issues/130>`__ :meth:`github.NamedUser.NamedUser.get_keys`
* `Support PubSubHub <https://github.com/jacquev6/PyGithub/issues/129>`_: :meth:`github.Repository.Repository.subscribe_to_hub` and :meth:`github.Repository.Repository.unsubscribe_from_hub`
* `Publish the oauth scopes <https://github.com/jacquev6/PyGithub/issues/134>`__ in :attr:`github.MainClass.Github.oauth_scopes`, thank you `bilderbuchi <https://github.com/bilderbuchi>`__ for asking

`Version 1.10.0 <https://github.com/jacquev6/PyGithub/issues?milestone=16&state=closed>`__ (December 25th, 2012) (Christmas 2012 edition)
-----------------------------------------------------------------------------------------------------------------------------------------

* Major improvement: support Python 3! PyGithub is automaticaly tested on `Travis <http://travis-ci.org/jacquev6/PyGithub>`__ with versions 2.5, 2.6, 2.7, 3.1 and 3.2 of Python
* Add a shortcut function :meth:`github.MainClass.Github.get_repo` to get a repo directly from its full name. thank you `lwc <https://github.com/lwc>`__ for the contribution
* :meth:`github.MainClass.Github.get_gitignore_templates` and :meth:`github.MainClass.Github.get_gitignore_template` for APIs ``/gitignore/templates``
* Add the optional ``ref`` parameter to :meth:`github.Repository.Repository.get_contents` and :meth:`github.Repository.Repository.get_readme`. Thank you `fixxxeruk <https://github.com/fixxxeruk>`__ for the contribution
* Get comments for all issues and all pull requests on a repository (``GET /repos/:owner/:repo/pulls/comments``: :meth:`github.Repository.Repository.get_pulls_comments` or :meth:`github.Repository.Repository.get_pulls_review_comments`; ``GET /repos/:owner/:repo/issues/comments``: :meth:`github.Repository.Repository.get_issues_comments`)

`Version 1.9.1 <https://github.com/jacquev6/PyGithub/issues?milestone-17&state-closed>`__ (November 20th, 2012)
---------------------------------------------------------------------------------------------------------------

* Fix an assertion failure when integers returned by Github do not fit in a Python ``int``

`Version 1.9.0 <https://github.com/jacquev6/PyGithub/issues?milestone-14&state-closed>`__ (November 19th, 2012)
---------------------------------------------------------------------------------------------------------------

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

`Version 1.8.1 <https://github.com/jacquev6/PyGithub/issues?milestone-15&state-closed>`__ (October 28th, 2012)
--------------------------------------------------------------------------------------------------------------

* Repository.get_git_ref prepends "refs/" to the requested references. Thank you `simon-weber <https://github.com/simon-weber>`__ for noting the incoherence between documentation and behavior. If you feel like it's a breaking change, please see `this issue <https://github.com/jacquev6/PyGithub/issues/104>`_

`Version 1.8.0 <https://github.com/jacquev6/PyGithub/issues?milestone-13&state-closed>`__ (September 30th, 2012)
----------------------------------------------------------------------------------------------------------------

* Enable `Travis CI <http://travis-ci.org/#!/jacquev6/PyGithub>`_
* Fix error 500 when json payload contains percent character (`%`). Thank you again `quixotique <https://github.com/quixotique>`__ for pointing that and reporting it to Github
* Enable debug logging. Logger name is `"github"`. Simple logging can be enabled by `github.enable_console_debug_logging()`. Thank you `quixotique <https://github.com/quixotique>`__ for the merge request and the advice
* Publish tests in the PyPi source archive to ease QA tests of the `FreeBSD port <http://www.freshports.org/devel/py-pygithub>`_. Thank you `koobs <https://github.com/koobs>`__ for maintaining this port
* Switch to `Semantic Versioning <http://semver.org/>`_
* Respect `pep8 Style Guide for Python Code <http://www.python.org/dev/peps/pep-0008>`_

`Version 1.7 <https://github.com/jacquev6/PyGithub/issues?milestone-12&state-closed>`__ (September 12th, 2012)
--------------------------------------------------------------------------------------------------------------

* Be able to clear the assignee and the milestone of an Issue. Thank you `quixotique <https://github.com/quixotique>`__ for the merge request
* Fix an AssertionFailure in `Organization.get_xxx` when using Github Enterprise. Thank you `mnsanghvi <https://github.com/mnsanghvi>`__ for pointing that
* Expose pagination to users needing it (`PaginatedList.get_page`). Thank you `kukuts <https://github.com/kukuts>`__ for asking
* Improve handling of legacy search APIs
* Small refactoring (documentation, removal of old code generation artifacts)

`Version 1.6 <https://github.com/jacquev6/PyGithub/issues?milestone-10&state-closed>`__ (September 8th, 2012)
-------------------------------------------------------------------------------------------------------------

* Restore support for Python 2.5
* Implement new APIS:

  * /hooks (undocumented, but mentioned in http://developer.github.com/v3/repos/hooks/#create-a-hook)
  * `Merging <http://developer.github.com/v3/repos/merging>`_
  * `Starring <http://developer.github.com/v3/repos/starring>`__ and `subscriptions <http://developer.github.com/v3/repos/watching>`_
  * `Assignees <http://developer.github.com/v3/issues/assignees>`_
  * `Commit statuses <http://developer.github.com/v3/repos/statuses>`_
  * `Contents <http://developer.github.com/v3/repos/contents>`_, thank you `berndca <https://github.com/berndca>`__ for asking

* Clarify issue and review comments on PullRequest, thank you `nixoz2k7 <https://github.com/nixoz2k7>`__ for asking

`Version 1.5 <https://github.com/jacquev6/PyGithub/issues?milestone-9&state-closed>`__ (September 5th, 2012)
------------------------------------------------------------------------------------------------------------

* Add a timeout option, thank you much `xobb1t <https://github.com/xobb1t>`__ for the merge request. *This drops Python 2.5 support*. I may be able to restore it in next version.
* Implement `Repository.delete`, thank you `pmchen <https://github.com/pmchen>`__ for asking

`Version 1.4 <https://github.com/jacquev6/PyGithub/issues?milestone-8&state-closed>`__ (August 4th, 2012)
---------------------------------------------------------------------------------------------------------

* Allow connection to a custom Github URL, for Github Enterprise, thank you very much `engie <https://github.com/engie>`__ for the merge request

`Version 1.3 <https://github.com/jacquev6/PyGithub/issues?milestone-7&state-closed>`__ (July 13th, 2012)
--------------------------------------------------------------------------------------------------------

* Implement `markdown rendering <http://developer.github.com/v3/markdown>`_
* `GitAuthor.date` is now a datetime, thank you `bilderbuchi <https://github.com/bilderbuchi>`_
* Fix documentation of `Github.get_gist`: `id` is a string, not an integer

`Version 1.2 <https://github.com/jacquev6/PyGithub/issues?milestone-6&state-closed>`__ (June 29th, 2012)
--------------------------------------------------------------------------------------------------------

* Implement `legacy search APIs <http://developer.github.com/v3/search>`_, thank you `kukuts <https://github.com/kukuts>`__ for telling me Github had released them
* Fix a bug with issue labels containing spaces, thank you `philipkimmey <https://github.com/philipkimmey>`__ for detecting the bug and fixing it
* Clarify how collections of objects are returned by `get_*` methods, thank you `bilderbuchi <https://github.com/bilderbuchi>`__ for asking

Version 1.1 (June 20th, 2012)
-----------------------------

* Restore compatibility with Python 2.5, thank you `pmuilu <https://github.com/pmuilu>`_
* Use `package_data` instead of `data_files` for documentation files in `setup.py`, thank you `malexw <https://github.com/malexw>`__ for reporting

`Version 1.0 <https://github.com/jacquev6/PyGithub/issues?milestone-2&state-closed>`__ (June 3rd, 2012)
-------------------------------------------------------------------------------------------------------

* Complete rewrite, with no more complicated meta-description
* Full typing of attributes and parameters
* Full documentation of attributes and parameters
* More usable exceptions raised in case on problems with the API
* Some bugs and limitations fixed, special thanks to `bilderbuchi <https://github.com/bilderbuchi>`_, `roskakori <https://github.com/roskakori>`__ and `tallforasmurf <https://github.com/tallforasmurf>`__ for reporting them!

Pre-release versions
~~~~~~~~~~~~~~~~~~~~

`Version 0.7 <https://github.com/jacquev6/PyGithub/issues?milestone-5&state-closed>`__ (May 26th, 2012)
-------------------------------------------------------------------------------------------------------

* Use PyGithub with OAuth authentication or with no authentication at all

`Version 0.6 <https://github.com/jacquev6/PyGithub/issues?milestone-4&state-closed>`__ (April 17th, 2012)
---------------------------------------------------------------------------------------------------------

* Fix `issue 21 <https://github.com/jacquev6/PyGithub/issues/21>`__ (KeyError when accessing repositories)
* Re-completed the API with NamedUser.create_gist


`Version 0.5 <https://github.com/jacquev6/PyGithub/issues?milestone-3&state-closed>`__ (March 19th, 2012)
---------------------------------------------------------------------------------------------------------

* Major achievement: **all APIs are implemented**
* More refactoring, of course

`Version 0.4 <https://github.com/jacquev6/PyGithub/issues?milestone-1&state-closed>`__ (March 12th, 2012)
---------------------------------------------------------------------------------------------------------

* The list of the not implemented APIs is shorter than the list of the implemented APIs
* APIs *not implemented*:

  * GET `/gists/public`
  * GET `/issues`
  * GET `/repos/:owner/:repo/compare/:base...:head`
  * GET `/repos/:owner/:repo/git/trees/:sha?recursive-1`
  * POST `/repos/:owner/:repo/git/trees?base_tree-`

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
