Change log
==========

Stable versions
~~~~~~~~~~~~~~~

Version 1.43.7 (April 16, 2019)
-----------------------------------

* Exclude tests from PyPI distribution (#1031) (78d283b9)
* Add codecov badge (#1090) (4c0b54c0)

Version 1.43.6 (April 05, 2019)
-----------------------------------
**New features**

* Add support for Python 3.7 (#1028) (6faa00ac)
* Adding HTTP retry functionality via urllib3 (#1002) (5ae7af55)
* Add new dismiss() method on PullRequestReview (#1053) (8ef71b1b)
* Add since and before to `get_notifications` (#1074) (7ee6c417)
* Add url parameter to include anonymous contributors in `get_contributors` (#1075) (293846be)
* Provide option to extend expiration of jwt token (#1068) (86a9d8e9)

**Bug Fixes & Improvements**

* Fix the default parameter for `PullRequest.create_review` (#1058) (118def30)
* Fix `get_access_token` (#1042) (6a89eb64)
* Fix `Organization.add_to_members` role passing (#1039) (480f91cf)

**Deprecation**

* Remove Status API (6efd6318)

Version 1.43.5 (January 29, 2019)
-----------------------------------

* Add project column create card (#1003) (5f5c2764)
* Fix request got an unexpected keyword argument body (#1012) (ff789dcc)
* Add missing import to PullRequest (#1007) (b5122768)

Version 1.43.4 (December 21, 2018)
-----------------------------------

**New features**

* Add Migration API (#899) (b4d895ed)
* Add Traffic API (#977) (a433a2fe)
* New in Project API: create repository project, create project column (#995) (1c0fd97d)

**Bug Fixes & Improvements**

* Change type of GitRelease.author to NamedUser (#969) (aca50a75)
* Use total_count from data in PaginatedList (#963) (ec177610)

Version 1.43.3 (October 31, 2018)
-----------------------------------

**New features**

* Add support for JWT authentication (#948) (8ccf9a94)
* Added support for required signatures on protected branches (#939) (8ee75a28)
* Ability to filter repository collaborators (#938) (5687226b)
* Mark notification as read (#932) (0a10d7cd)
* Add highlight search to ``search_code`` function (#925) (1fa25670)
* Adding ``suspended_at`` property to NamedUSer (#922) (c13b43ea)
* Add since parameter for Gists (#914) (e18b1078)

**Bug Fixes & Improvements**

* Fix missing parameters when reversing ``PaginatedList`` (#946) (60a684c5)
* Fix unable to trigger ``RateLimitExceededException``. (#943) (972446d5)
* Fix inconsistent behavior of trailing slash usage in file path (#931) (ee9f098d)
* Fix handling of 301 redirects (#916) (6833245d)
* Fix missing attributes of ``get_repos`` for authenticated users (#915) (c411196f)
* Fix ``Repository.edit`` (#904) (7286eec0)
* Improve ``__repr__`` method of Milestone class (#921) (562908cb)
* Fix rate limit documentation change (#902) (974d1ec5)
* Fix comments not posted in create_review() (#909) (a18eeb3a)

Version 1.43.2 (September 12, 2018)
-----------------------------------

* Restore ``RateLimit.rate`` attribute, raise deprecation warning instead (d92389be)

Version 1.43.1 (September 11, 2018)
-----------------------------------

New feature:

* Add support for Projects (#854) (faca4ce1)

Version 1.43 (September 08, 2018)
-----------------------------------


**BUGFIX**

* ``Repository.get_archive_link`` will now NOT follow HTTP redirect and return the url instead (#858) (43d325a5)
* Fixed ``Gistfile.content`` (#486) (e1df09f7)
* Restored NamedUser.contributions attribute (#865) (b91dee8d)

**New features**

* Add support for repository topics (#832) (c6802b51)
* Add support for required approving review count (#888) (ef16702)
* Add ``Organization.invite_user`` (880)(eb80564)
* Add support for search/graphql rate limit (fd8a036)

  + Deprecated ``RateLimit.rate``
  + Add `RateLimit.core <https://pygithub.readthedocs.io/en/latest/github_objects/RateLimit.html#github.RateLimit.RateLimit.core>`__, `RateLimit.search <https://pygithub.readthedocs.io/en/latest/github_objects/RateLimit.html#github.RateLimit.RateLimit.search>`__ and `RateLimit.graphql <https://pygithub.readthedocs.io/en/latest/github_objects/RateLimit.html#github.RateLimit.RateLimit.graphql>`__
* Add Support search by topics (#893) (3ce0418)
* Branch Protection API overhaul (#790) (171cc567)

  + (**breaking**) Removed Repository.protect_branch
  + Add `BranchProtection <https://pygithub.readthedocs.io/en/latest/github_objects/BranchProtection.html>`__
  + Add `RequiredPullRequestReviews <https://pygithub.readthedocs.io/en/latest/github_objects/RequiredPullRequestReviews.html>`__
  + Add `RequiredStatusChecks <https://pygithub.readthedocs.io/en/latest/github_objects/RequiredStatusChecks.html>`__
  + Add ``Branch.get_protection``, ``Branch.get_required_pull_request_reviews``, ``Branch.get_required_status_checks``, etc

**Improvements**

* Add missing arguments to ``Repository.edit`` (#844) (29d23151)
* Add missing attributes to Repository (#842) (2b352fb3)
* Adding archival support for ``Repository.edit`` (#843) (1a90f5db)
* Add ``tag_name`` and ``target_commitish`` arguments to ``GitRelease.update_release`` (#834) (790f7dae)
* Allow editing of Team descriptions (#839) (c0021747)
* Add description to Organizations (#838) (1d918809)
* Add missing attributes for IssueEvent (#857) (7ac2a2a)
* Change ``MainClass.get_repo`` default laziness (#882) (6732517)

**Deprecation**

* Removed Repository.get_protected_branch (#871) (49db6f8)


Version 1.42 (August 19, 2018)
-----------------------------------

* Fix travis upload issue

**BUGFIX**

* ``Repository.get_archive_link`` will now NOT follow HTTP redirect and return the url instead (#858) (43d325a5)
* Fixed ``Gistfile.content`` (#486) (e1df09f7)
* Restored NamedUser.contributions attribute (#865) (b91dee8d)

New features

* Add support for repository topics (#832) (c6802b51)
* Branch Protection API overhaul (#790) (171cc567)

  + (**breaking**) Removed Repository.protect_branch
  + Add `BranchProtection <https://pygithub.readthedocs.io/en/latest/github_objects/BranchProtection.html>`__
  + Add `RequiredPullRequestReviews <https://pygithub.readthedocs.io/en/latest/github_objects/RequiredPullRequestReviews.html>`__
  + Add `RequiredStatusChecks <https://pygithub.readthedocs.io/en/latest/github_objects/RequiredStatusChecks.html>`__
  + Add ``Branch.get_protection``, ``Branch.get_required_pull_request_reviews``, ``Branch.get_required_status_checks``, etc

Improvements

* Add missing arguments to ``Repository.edit`` (#844) (29d23151)
* Add missing properties to Repository (#842) (2b352fb3)
* Adding archival support for ``Repository.edit`` (#843) (1a90f5db)
* Add ``tag_name`` and ``target_commitish`` arguments to ``GitRelease.update_release`` (#834) (790f7dae)
* Allow editing of Team descriptions (#839) (c0021747)
* Add description to Organizations (#838) (1d918809)

Version 1.41 (August 19, 2018)
-----------------------------------

**BUGFIX**

* ``Repository.get_archive_link`` will now NOT follow HTTP redirect and return the url instead (#858) (43d325a5)
* Fixed ``Gistfile.content`` (#486) (e1df09f7)
* Restored NamedUser.contributions attribute (#865) (b91dee8d)

New features

* Add support for repository topics (#832) (c6802b51)
* Branch Protection API overhaul (#790) (171cc567)

  + (**breaking**) Removed Repository.protect_branch
  + Add `BranchProtection <https://pygithub.readthedocs.io/en/latest/github_objects/BranchProtection.html>`__
  + Add `RequiredPullRequestReviews <https://pygithub.readthedocs.io/en/latest/github_objects/RequiredPullRequestReviews.html>`__
  + Add `RequiredStatusChecks <https://pygithub.readthedocs.io/en/latest/github_objects/RequiredStatusChecks.html>`__
  + Add ``Branch.get_protection``, ``Branch.get_required_pull_request_reviews``, ``Branch.get_required_status_checks``, etc

Improvements

* Add missing arguments to ``Repository.edit`` (#844) (29d23151)
* Add missing properties to Repository (#842) (2b352fb3)
* Adding archival support for ``Repository.edit`` (#843) (1a90f5db)
* Add ``tag_name`` and ``target_commitish`` arguments to ``GitRelease.update_release`` (#834) (790f7dae)
* Allow editing of Team descriptions (#839) (c0021747)
* Add description to Organizations (#838) (1d918809)

Version 1.40 (June 26, 2018)
-----------------------------------
* Major enhancement: use requests for HTTP instead of httplib (#664) (9aed19dd)
* Test Framework improvement (#795) (faa8f205)
* Handle HTTP 202 HEAD & GET with a retry (#791) (3aead158)
* Fix github API requests after asset upload (#771) (8bdac23c)
* Add remove_membership() method to Teams class (#807) (817f2230)
* Add check-in to projects using PyGithub (#814) (05f49a59)
* Include target_commitish in GitRelease (#788) (ba5bf2d7)
* Fix asset upload timeout, increase default timeout from 10s to 15s (#793) (140c6480)
* Fix Team.description (#797) (0e8ae376)
* Fix Content-Length invalid headers exception (#787) (23395f5f)
* Remove NamedUser.contributions (#774) (a519e467)
* Add ability to skip SSL cert verification for Github Enterprise (#758) (85a9124b)
* Correct Repository.get_git_tree recursive use (#767) (bd0cf309)
* Re-work PullRequest reviewer request (#765) (e2e29918)
* Add support for team privacy (#763) (1f23c06a)
* Add support for organization outside collaborators (#533) (c4446996)
* PullRequest labels should use Issues URL (#754) (678b6b20)
* Support labels for PullRequests (#752) (a308dc92)
* Add get_organizations() (#748) (1e0150b5)

Version 1.39 (April 10, 2018)
-----------------------------------

* Add documentation to github.Repository.Repository.create_git_release() (#747) (a769c2ff)
* Add add_to_members() and remove_from_membership() (#741) (4da483d1)
* Documentation: clarify semantics of get_comments (#743) (fec3c943)
* Add download_url to ContentFile, closes #575 (ca6fbc45)
* Add PullRequestComment.in_reply_to_id (#718) (eaa6a508)
* Add team privacy parameter to create team (#702) (5cb5ab71)
* Implement License API (#734) (b54ccc78)
* Fix delete method for RepositoryKey (911bf615)
* Remove edit for UserKey (722f2534)
* Labels API: support description (#738) (42e75938)
* Added Issue.as_pull_request() and PullReqest.as_issue() (#630) (6bf2acc7)
* Documentation: sort the Github Objects (#735) (1497e826)
* Add support for getting PR single review's comments. (#670) (612c3500)
* Update the RepositoryKey class (#530) (5e8c6832)
* Added since to PR review comments get (#577) (d8508285)
* Remove some duplicate attributes introduced in #522 (566b28d3)
* Added tarball_url, zipball_url, prerelease and draft property (#522) (c76e67b7)
* Source Import API (#673) (864c663a)

Version 1.38 (March 21, 2018)
-----------------------------------

* Updated readthedocs, PyPI to reflect latest version
* Added option to create review for Pull request (#662) (162f0397)
* Depreciate legacy search API (3cd176e3)
* Filter team members  by role (#491) (10ee17a2)
* Add url attribute to PullRequestReview object (#731) (0fb176fd)
* Added target_commitish option to Repository.create_git_release() (#625) (0f0a7d4e)
* Fix broken Github reference link in class docstrings (a32a17bf)
* Add hook support for organizations (#729) (c7f6563c)
* Get organization from the team (#590) (d9c5a07f)
* Added search_commits (#727) (aa556f85)
* Collaborator site admin (#719) (f8b23505)
* Fix add_to_watched for AuthenticatedUser (#716) (6109eb3c)

Version 1.37 (March 03, 2018)
-----------------------------------

* Add __eq__ and __hash__ to NamedUser (#706) (8a13b274)
* Add maintainer can modify flag to create pull request (#703) (0e5a1d1d)
* Fix typo in Design.md (#701) (98d32af4)
* Add role parameter to Team.add_membership method (#638) (01ab4cc6)
* Add add_membership testcase (#637) (5a1424bb)

Version 1.36 (February 02, 2018)
-----------------------------------

* Fix changelog generation (5d911e22)
* Add collaborator permission support (#699) (167f85ef)
* Use datetime object in create_milestone (#698) (cef98416)
* Fix date format for milestone creation (#593) (e671fdd0)
* Remove the default "null" input send during GET request (#691) (cbfe8d0f)
* Updated PullRequest reviewer request according to API changes (#690) (5c9c2f75)
* make created_at/published_at attrs available for Release objects (#689) (2f9b1e01)
* Add committer/author to Repository.delete_file (#678) (3baa682c)
* Add method to get latest release of a repository (#609) (45d18436)
* Add permissions field to NamedUser (#676) (6cfe46b7)
* Fix all pep8 coding conventions (6bc804dc)
* Add new params for /users/:user/repos endpoint (89834a9b)
* Add support for changing PR head commit (#632) (3f77e537)
* Use print() syntax in README (#681) (c5988c39)
* Add PyPI badge and installation instructions to README (#682) (3726f686)
* Drop support for EOL Python 2.5-2.6 and 3.2-3.3 (#674) (6735be49)
* Add Reactions feature (#671) (ba50af53)
* Add ping_url and ping to Hook (#669) (6169d8ea)
* Add Repository.archived property (#657) (35333e03)
* Add unit test for tree attribute of GitCommit (#668) (e5bfdbeb)
* Add read_only attribute to Deploy Keys (#570) (dbc6f5ab)
* Doc create instance from token (#667) (c33a3883)
* Fix uploading binary files on Python 3 (#621) (317079ef)
* Decode jwt bytes object in Python 3 (#633) (84b43da7)
* Remove broken downloads badge (#644) (15cdc2f8)
* Added missing parameters for repo creation (#623) (5c41120a)
* Add ability to access github Release Asset API. (#525) (52449649)
* Add 'submitted at' to PullRequestReview (#565) (ebe7277a)
* Quote path for /contents API (#614) (554c1ab1)
* Add Python 3.6 (2533bed9)
* Add Python 3.6 (e78f0ece)
* Updated references in introduction.rst (d2c72bb3)
* fix failing tests on py26 (291f6dde)
* Import missing exception (67b078e9)

Version 1.35 (July 10, 2017)
-----------------------------------

* Add Support for repository collaborator invitations.

Version 1.34 (abril 04, 2017)
-----------------------------------

* Add Support for Pull Request Reviews feature.

Version 1.32 (February 1, 2017)
-----------------------------------

* Support for Integrations installation endpoint (656e70e1)

Version 1.31 (January 30, 2017)
-----------------------------------

* Support HTTP 302 redirect in Organization.has_in_members (0154c6b)
* Add details of repo type for get_repos documentation (f119147)
* Note explicit support for Python 3.5 (3ae55f0)
* Fix README instructions (5b0224e)
* An easier to see link to the documentation in response to issue #480. (6039a4b)
* Encode GithubObject repr values in utf-8 when using Python2 (8ab9082)
* Updated documentation (4304ccd)
* Added a subscribers count field (a2da7f9)
* Added "add_to_assignees" & "remove_from_assignees" method to Issue object. (66430d7)
* Added "assignees" attribute to PullRequest object. (c0de6be)
* add html_url to GitRelease (ec633aa)
* Removed unused imports (65afc3f)
* Fix typo in a constant (10a28e0)
* Fix changelog formatting glitch (03a9227)
* Added "assignees" argument in Repository.create_issue() (ba007dc)
* Enhance support of "assignees" argument in Issue.edit() (14dd9f0)
* Added "assignees" attribute to Issue object. (e0e5fdf)

Version 1.30 (January 30, 2017)
-----------------------------------

* adds GitHub integrations (d60943d)

Version 1.29 (October 10, 2016)
-----------------------------------

* add issue assignee param (3a8edc7)
* Fix diffrerent case (fcf6cfb)
* DOC: remove easy_install suggestion; update links (45e76d9)
* Add permission param documentation (9347345)
* Add ability to set permission for team repo (5dddea7)
* Fix status check (073bb44)
* adds support for content dirs (0799753)

Version 1.28 (September 09, 2016)
-----------------------------------

* test against python 3.5 (5d35284)
* sort params and make them work on py3 (78374b9)
* adds a nicer __repr__ (8571d87)
* Add missing space (464259d)
* Properly handle HTTP Proxy authentication with Python 3 (d015154)
* Fix small typo (987bca0)
* push to 'origin' instead of 'github' (d640666)

Version 1.27.1 (August 12, 2016)
-----------------------------------

* upgrade release process based on travis (3c20a66)
* change file content encoding to support unicode(like chinese), py2 (5404030)
* adds missing testfile corrections (9134aa2)
* fixed file API return values (0f29a53)
* assert by str and unicode to make it more py3 friendly (7390827)
* Patch issue 358 status context (#428) (70e30c5)
* Adding "since" param to Issue.get_comments() (#426) (3c6f99f)
* update doc url everywhere (#420) (cb0cf0a)
* fix a couple typos to be clearer (#419) (23c0e75)
* Document how one gets an AuthenticatedUser object (ba66862)
* fix wrong expectance on requestJsonAndCheck() returning {} if no data (8985368)
* Add previous_filename property to File (e1be1e6)
* add changelog entry for 1.26.0 (a1f3de2)
* update project files (be2e98b)
* fix update/create/delete file api return value issue (8bb765a)
* fix typo (a7929ac)
* fix update/delete/create content return value invalid issue (a0a4511)
* Follow redirects in the case of a 301 status code (c29f533)
* Fix for pickling exception when deserializing GithubException. (8f8b455)
* add support for the head parameter in Repository.get_pulls (397a74d)
* Add:   - CommitCombinedStatus class   - get_combined_status() to Commit class to return combined status   - Add test for combined status. (5823ed7)
* fix python3 compatibility issue for using json/base64 (5b7f0bb)
* remove not covered API from readme (9c6f881)
* change replay data for update file test case (46895df)
* fix python3 compatability error in test case (00777db)
* Add repo content create/update/delete testcase (4aaeb9e)
* add MAINTAINERS file (a16b55b)
* travis: disable email (6347157)
* fix protect branch tests (65360b0)
* Add branch protection endpoint (737f0c3)
* fix request parameters issue (ae37d44)
* add content file create/update/delete api (b83ffbf)
* Add travis button on README. (a83649b)
* fix misspelling: https://github.com/PyGithub/PyGithub/issues/363 (a06b5ec)
* Adding base parameter to get_pulls() method. (71593a8)
* add support for the direction parameter in Repository.get_pulls (70bcb6d)
* added creator parameter (ca9af4f)

Version 1.27.0 (August 12, 2016)
-----------------------------------

* this version was never released to PyPi due to a problem with the deployment

Version 1.26.0 (November 5th, 2015)
-----------------------------------

* Added context parameter to Status API
* Changed InputGitAuthor to reflect that time is an optional parameter
* Added sort option to get_pulls
* Added api_preview parameter to Requester class
* Return empty list instead of None for pagination with no pages
* Removed URL scheme validation that broke GitHub Enterprise
* Added "add_membership" call to Teams
* Added support to lazily load repositories
* Updated test suite to record with oauth tokens
* Added support for http_proxy
* Add support for filter/role options in Organization.get_members()
* Changed Organization.get_members's filter parameter to _filter
* Fix escaping so that labels now support whitespaces
* Updated create_issue to support taking a list of strings for labels
* Added support for long integers in get_repo
* Fixed pagination to thread headers between requests
* Added repo.get_stargazers_with_dates()

Version 1.25.2 (October 7th, 2014)
----------------------------------

* `Work around <https://github.com/jacquev6/PyGithub/issues/278>`__ the GitHub API v3 returning `null`\s in some paginated responses, `erichaase <https://github.com/erichaase>`__ for the bug report

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
