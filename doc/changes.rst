Change log
==========

Stable versions
~~~~~~~~~~~~~~~

Version 2.5.0 (November 06, 2024)
---------------------------------

Breaking Changes
^^^^^^^^^^^^^^^^

* Parameters of method ``github.Requester.Requester.graphql_named_mutation`` have been renamed:

  * Parameter ``variables`` renamed to ``mutation_input``
  * Parameter ``output`` renamed to ``output_schema``
  * Default value of parameter ``output`` has been removed

New features
^^^^^^^^^^^^

* Rework GraphQL mutations (#3046) (27222251)
* Make pagination work with GraphQL response data (#3047) (cd30e379)
* Add `RepositoryDiscussion` powered by GraphQL API (#3048) (29359f3c)
* Add `Repository.get_discussion()` to get a single Discussion (#3072) (44120b1e)

Improvements
^^^^^^^^^^^^

* Adds List organization memberships for the authenticated user (#3040) (cf443955)
* Add `actor` property to WorkflowRun (#2764) (612ba68e)
* Make requester a public attribute (#3056) (c44ec523)

Bug Fixes
^^^^^^^^^

* Fix requesting urls containing parameters with parameters dict (#2929) (e1d67ada)
* PullRequest.delete_branch: fix the remaining pull requests check (#3063) (72fa6278)

Maintenance
^^^^^^^^^^^

* Remove stale bot (510c1402)
* Upgrade Github actions (#3075) (323e2828)
* Add top issues dashboard action (#3049) (c91f26a7)
* Make tests pass some more years (#3045) (352c55aa)
* Run top issues workflow only in PyGithub repo (0d395d4e)
* Replace pre-commit Github action in order to pin pre-commit version (#3059) (1a05b43d)

Version 2.4.0 (August 26, 2024)
-------------------------------

Breaking Changes
^^^^^^^^^^^^^^^^

* The ``github.Commit.Commit`` class provides a ``files`` property that used to return a ``list[github.File.File]``,
  which has now been changed to ``PaginatedList[github.File.File]``. This breaks user code that assumes a ``list``:

.. code-block:: python

    files = repo.get_commit("7266e812ed2976ea36a4303edecfe5d75522343f").files
    no_of_files = len(files)

This will raise a ``TypeError: object of type 'PaginatedList' has no len()``, as the returned ``PaginatedList``
does not support the ``len()`` method. Use the ``totalCount`` property instead:

.. code-block:: python

    files = repo.get_commit("7266e812ed2976ea36a4303edecfe5d75522343f").files
    no_of_files = files.totalCount

* Removed support for Python 3.7.

New features
^^^^^^^^^^^^

* Allow custom authentication (#2987) (32b826fd)

Improvements
^^^^^^^^^^^^

* Add `has_discussions` to `AuthenticatedUser` and `Repository` classes (#3020) (75224167)
* Update more `SecurityAndAnalysis` attributes (#3025) (fa168279)
* Implement support for re-running only failed workflow jobs. (#2983) (23e87563)
* Add possibility to mark a thread/notification as done (#2985) (5ba24379)
* Add "pull_request_review_id" to PullRequestComment object (#3000) (6a59cf82)
* Add minimize and unminimize functions for IssueComment class (#3005) (09c4f58e)
* Support Organization/Repository custom properties (#2968) (c5e6b702)
* Add `dict` type to `add_attribute` script (#2977) (2a04f9cc)
* Allow for deleting and restoring branch associated with PR (#1784) (4ba1e412)
* Add "archived_at" to Organization object. (#2974) (cc766a6f)
* Adds Security & Analysis To Repository (#2960) (f22af54d)
* Add added_by and last_used attributes to RepositoryKey (#2952) (5dffa64d)
* Add `make_latest` to `GitRelease.update_release` (#2888) (60136105)
* Make Commit.files return PaginatedList (#2939) (fa885f00)

Bug Fixes
^^^^^^^^^

* Fix GraphQL Queries with Variables (#3002) (4324a3d9)

Maintenance
^^^^^^^^^^^

* Remove support for Python 3.7 (#2975, #3008) (d0e05072, 6d60b754)
* docs: add missing code-block (#2982) (c93e73e2)
* Update README.md (#2961) (5d9f90d2)
* CI: Fix test success job (#3010) (61d37dce)

Version 2.3.0 (March 21, 2024)
------------------------------

New features
^^^^^^^^^^^^

* Support OAuth for enterprise (#2780) (e4106e00)
* Support creation of Dependabot Organization and Repository Secrets (#2874) (0784f835)

Improvements
^^^^^^^^^^^^

* Create release with optional name and message when generate_release_notes is true (#2868) (d65fc30d)
* Add missing attributes to WorkflowJob (#2921) (9e092458)
* Add `created` and `check_suite_id` filter for Repository WorkflowRuns (#2891) (c788985c)
* Assert requester argument type in Auth (#2912) (0b8435fc)

Bug Fixes
^^^^^^^^^

* Revert having allowed values for add_to_collaborators (#2905) (b542438e)

Maintenance
^^^^^^^^^^^

* Fix imports in authentication docs (#2923) (e3d36535)
* CI: add docformatter to precommit (#2614) (96ad19ae)
* Add .swp files to gitignore (#2903) (af529abe)
* Fix instructions building docs in CONTRIBUTING.md (#2900) (cd8e528d)
* Explicitly name the modules built in pyproject.toml (#2894) (4d461734)

Version 2.2.0 (January 28, 2024)
--------------------------------

Breaking Changes
^^^^^^^^^^^^^^^^

* The ``github.Comparison.Comparison`` instance returned by ``Repository.compare`` provides a ``commits``
  property that used to return a ``list[github.Commit.Commit]``, which has now been changed
  to ``PaginatedList[github.Commit.Commit]``. This breaks user code that assumes a ``list``:

.. code-block:: python

    commits = repo.compare("v0.6", "v0.7").commits
    no_of_commits = len(commits)

This will raise a ``TypeError: object of type 'PaginatedList' has no len()``, as the returned ``PaginatedList``
does not support the ``len()`` method. Use the ``totalCount`` property instead:

.. code-block:: python

    commits = repo.compare("v0.6", "v0.7").commits
    no_of_commits = commits.totalCount


New features
^^^^^^^^^^^^

* Add support to call GraphQL API

Improvements
^^^^^^^^^^^^

* Add parent_team_id, maintainers and notification_setting for creating and updating teams. (#2863) (49d07d16)
* Add support for issue reactions summary (#2866) (cc4c5269)
* Support for DependabotAlert APIs (#2879) (14af7051)
* Derive GraphQL URL from base_url (#2880) (d0caa3c3)
* Make ``Repository.compare().commits`` return paginated list (#2882) (2d284d1e)
* Add missing branch protection fields (#2873) (e47c153b)
* Add ``include_all_branches`` to ``create_repo_from_template`` of ``AuthenticatedUser`` and ``Organization`` (#2871) (34c4642e)
* Add and update organisation dependabot secrets (#2316) (603896f4)
* Add missing params to ``Organization.create_repo`` (#2700) (9c61a2a4)
* Update allowed values for ``Repository`` collaborator permissions (#1996) (b5b66da8)
* Support editing PullRequestReview (#2851) (b1c4c561)
* Update attributes after calling ``PullRequestReview.dismiss`` (#2854) (6f3d714c)
* Add ``request_cve`` on ``RepositoryAdvisories`` (#2855) (41b617b7)
* Filter collaborators of a repository by permissions (#2792) (702c127a)
* Set pull request to auto merge via GraphQL API (#2816) (232df79a)
* Support Environment Variables and Secrets (#2848) (7df97398)
* Update workflow.get_runs & pullrequest.add_to_assignees function signature (#2799) (26eedbb0)
* Add ``GithubObject.last_modified_datetime`` to have ``last_modified`` as a ``datetime`` (#2772) (e7ce8189)
* Add support for global advisories and unify some shared logic with repository advisories (#2702) (c8b4fcbe)
* Add internal as valid Repository visibility value (#2806) (d4a5a40f)
* Add support for issue comments reactions summary (#2813) (67397491)

Bug Fixes
^^^^^^^^^

* Add a bunch of missing urllib.parse.quote calls (#1976) (13194be2)
* Fix Variable and Secret URL (#2835) (aa763431)

Maintenance
^^^^^^^^^^^

* Update the class name for NetrcAuth in the examples (#2860) (2f44b2e8)
* Move build to PEP517 (#2800) (c589bf9e)
* Use new type assert functions in ``Repository`` (#2798) (2783e671)
* PyTest: Move config to pyproject.toml (#2859) (61fb728b)
* codespell: ignore-words-list (#2858) (dcf6d8a1)
* Improve fix-headers.py script (#2728) (a48c37fa)
* Remove dependency on python-dateutil (#2804) (ab131a2f)
* CI: update precommit & apply (#2600) (d92cfba2)
* Fix parameter order according to Version 2.1.0 (#2786) (dc37d5c1)
* Add missing GitHub classes to docs (#2783) (9af9b6e5)
* Fix mypy error with urllib3>=2.0.0a1 by ignoring (#2779) (64b1cdea)

Version 2.1.1 (September 29, 2023)
-----------------------------------

Bug Fixes
^^^^^^^^^

* Require urllib 1.26.0 or greater (#2774) (001c0852)

Maintenance
^^^^^^^^^^^

* Fix pypi-release workflow, allow for manual run (#2771) (035c88f1)

Version 2.1.0 (September 29, 2023)
-----------------------------------

Important
^^^^^^^^^

**Request throttling**

This release introduces a default throttling mechanism to mitigate secondary rate limit errors and comply with Github's best practices:
https://docs.github.com/en/rest/guides/best-practices-for-integrators?apiVersion=2022-11-28#dealing-with-secondary-rate-limits

The default throttling of 1 second between writes and 0.25 second between any requests can be configured
for ``github.Github`` and ``github.GithubIntegration``:

.. code-block:: python

    g = github.Github(seconds_between_requests=0.25, seconds_between_writes=1)

Set these parameters to ``None`` to disable throttling and restore earlier behavior.

**Request retry**

This release introduces a default retry mechanism to retry retry-able 403 responses (primary and secondary rate limit errors only) and any 5xx response.

Class ``github.GithubRetry`` implements this behavior, and can be configured via the ``retry`` argument of ``github.Github`` and ``github.GithubIntegration``.
Retry behavior is configured similar to ``urllib3.Retry``: https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.html

.. code-block:: python

    g = github.Github(retry=github.GithubRetry())

Set this parameter to ``None`` to disable retry mechanism and restore earlier behaviour.

Breaking Changes
^^^^^^^^^^^^^^^^

**Timestamps**

Any timestamps returned by this library are ``datetime`` with timezone information, usually UTC.
Before this release, timestamps used to be naive ``datetime`` instances without timezone.
Comparing (other than ``==``) these timestamps with naive ``datetime`` instances used to work but will now break.
Add a timezone information to your ``datetime`` instances before comparison:

.. code-block:: python

    if g.get_repo("PyGithub/PyGithub").created_at < datetime(2012, 2, 26, tzinfo=timezone.utc):
        ...

**Netrc authentication**

A Netrc file (e.g. ``~/.netrc``) does not override PyGithub authentication, anymore.
If you require authentication through Netrc, then this is a breaking change.
Use a ``github.Auth.NetrcAuth`` instance to use Netrc credentials:

.. code-block:: python

    >>> auth = Auth.NetrcAuth()
    >>> g = Github(auth=auth)
    >>> g.get_user().login
    'login'

**Repository.create_pull**

Merged overloaded ``create_pull`` methods

.. code-block:: python

    def create_pull(self, issue, base, head)
    def create_pull(self, title, body, base, head, maintainer_can_modify=NotSet, draft=False)

into

.. code-block:: python

    def create_pull(self, base, head, *, title=NotSet, body=NotSet, maintainer_can_modify=NotSet, draft=NotSet, issue=NotSet)

Please update your usage of ``Repository.create_pull`` accordingly.

New features
^^^^^^^^^^^^

* Throttle requests to mitigate RateLimitExceededExceptions (#2145) (99155806)
* Retry retryable 403 (rate limit) (#2387) (0bb72ca0)
* Close connections after use (#2724) (73236e23)

Improvements
^^^^^^^^^^^^

* Make datetime objects timezone-aware (#2565) (0177f7c5)
* Make ``Branch.edit_*`` functions return objects (#2748) (8dee53a8)
* Add ``license`` attribute to ``Repository`` (#2721) (26d353e7)
* Add missing attributes to ``Repository``  (#2742) (65cfeb1b)
* Add ``is_alphanumeric`` attribute to ``Autolink`` and ``Repository.create_autolink`` (#2630) (b6a28a26)
* Suppress ``requests`` fallback to netrc, provide ``github.Auth.NetrcAuth`` (#2739) (ac36f6a9)
* Pass Requester arguments to ``AppInstallationAuth.__integration`` (#2695) (8bf542ae)
* Adding feature for enterprise consumed license (#2626) (a7bfdf2d)
* Search Workflows by Name (#2711) (eadc241e)
* Add ``Secret`` and ``Variable`` classes (#2623) (bcca758d)
* Add Autolink API link (#2632) (aedfa0b9)
* Add ``required_linear_history`` attribute to ``BranchProtection`` (#2643) (7a80fad9)
* Add retry issue to ``GithubException``, don't log it (#2611) (de80ff4b)
* Add ``message`` property to ``GithubException`` (#2591) (f087cad3)
* Add support for repo and org level actions variables (#2580) (91b3f40f)
* Add missing arguments to ``Workflow.get_runs()`` (#2346) (766df993)
* Add ``github.Rate.used`` field (#2531) (c4c2e527)

Bug Fixes
^^^^^^^^^

* Fix ``Branch.bypass_pull_request_allowances`` failing with "nil is not an object" (#2535) (c5542a6a)
* Fix ``required_conversation_resolution`` assertion (#2715) (54f22267)
* Fix assertion creating pull request review comment (#2641) (2fa568b6)
* Safely coerce ``responseHeaders`` to ``int`` (#2697) (adbfce92)
* Fix assertion for ``subject_type`` in creating pull request review comment (#2642) (4933459e)
* Use timezone-aware reset datetime in ``GithubRetry.py`` (#2610) (950a6949)
* Fix ``Branch.bypass_pull_request_allowances`` failing with "nil is not an object" (#2535) (c5542a6a)

Maintenance
^^^^^^^^^^^

* Epic mass-merge ``.pyi`` type stubs back to ``.py`` sources (#2636)
* Move to main default branch (#2566) (e66c163a)
* Force Unix EOL (#2573) (094538e1)
* Close replay test data file silently when test is failing already (#2747) (6d871d56)
* CI: Make CI support merge queue (#2644) (a91debf1)
* CI: Run CI on release branches (#2708) (9a88b6b1)
* CI: remove conflict label workflow (#2669) (95d8b83c)
* Fix pip install command in README.md (#2731) (2cc1ba2c)
* Update ``add_attribute.py`` to latest conding style (#2631) (e735972e)
* CI: Improve ruff DX (#2667) (48d2009c)
* CI: Increase wait and retries of labels action (#2670) (ff0f31c2)
* Replace ``flake8`` with ``ruff`` (#2617) (42c3b47c)
* CI: update labels action name and version (#2654) (c5c83eb5)
* CI: label PRs that have conflicts (#2622) (1d637e4b)
* Unify requirements files location & source in setup.py (#2598) (2edc0f8f)
* Enable mypy ``disallow_untyped_defs`` (#2609) (294c0cc9)
* Enable mypy ``check_untyped_defs`` (#2607) (8816889a)
* Set line length to 120 characters (#2599) (13e178a3)
* CI: Build and check package before release (#2593) (3c880e76)
* Use ``typing_extensions`` for ``TypedDict`` (#2592) (5fcb0c7d)
* CI: Update action actions/setup-python (#2382) (2e5cd31e)
* Add more methods and attributes to Repository.pyi (#2581) (72840de4)
* CI: Make pytest color logs (#2597) (73241102)
* precommit: move ``flake8`` as last (#2595) (11bb6bd7)
* Test on Windows and macOS, don't fail fast (#2590) (5c600894)
* Remove symlinks from test data (#2588) (8d3b9057)

Version 1.59.1 (July 03, 2023)
-----------------------------------

Bug Fixes
^^^^^^^^^

* Safely coerce responseHeaders to int (#2697) (adbfce92)

Version 1.59.0 (June 22, 2023)
-----------------------------------

Important
^^^^^^^^^

This release introduces new way of authentication. All authentication-related arguments ``github.Github(login_or_token=…, password=…, jwt=…, app_auth=…)``
and ``github.GithubIntegration(integration_id=…, private_key=…, jwt_expiry=…, jwt_issued_at=…, jwt_algorithm=…)`` are replaced by a single ``auth=…`` argument.
Module ``github.Auth`` provides classes for all supported ways of authentication: ``Login``, ``Token``, ``AppAuth``, ``AppAuthToken``, ``AppInstallationAuth``, ``AppUserAuth``.
Old arguments are deprecated but continue to work. They are scheduled for removal for version 2.0 release.

This project has decided to move all typing information from ``.pyi`` files into the respective ``.py`` source files.
This will happen gradually over time.

Breaking Changes
^^^^^^^^^^^^^^^^

* The ``position`` argument in ``github.PullRequest.create_review_comment(position=…)`` has been renamed to ``line``.
  This breaks user code that calls ``create_review_comment`` with keyword argument ``position``. Call with ``line=…`` instead.
  Calling this method with positional arguments is not breaking.
* The ``jwt_expiry``, ``jwt_issued_at`` and ``jwt_algorithm`` arguments in ``github.GithubIntegration()`` have changed their position.
  User code calling ``github.GithubIntegration(…)`` with these arguments as positional arguments breaks.
  Please use keyword arguments: ``github.GithubIntegration(…, jwt_expiry=…, jwt_issued_at=…, jwt_algorithm=…)``.
* The ``since`` argument in ``github.PullRequest.get_review_comments(…)`` has changed position.``
  User code calling ``github.PullRequest.get_review_comments(…)`` with this argument as positional argument breaks.
  Please use keyword argument: ``github.PullRequest.get_review_comments(since=…)``.

Deprecation
^^^^^^^^^^^

* The use of ``github.Github(login_or_token=…)`` is deprecated, use ``github.Github(auth=github.Auth.Login(…))`` or ``github.Github(auth=github.Auth.Token(…))`` instead.
* The use of ``github.Github(password=…)`` is deprecated, use ``github.Github(auth=github.Auth.Login(…))`` instead.
* The use of ``github.Github(jwt=…)`` is deprecated, use ``github.Github(auth=github.AppAuth(…))`` or ``github.Github(auth=github.AppAuthToken(…))`` instead.
* The use of ``github.Github(app_auth=…)`` is deprecated, use ``github.Github(auth=github.Auth.AppInstallationAuth(…))`` instead.
* The use of ``github.GithubIntegration(integration_id=…, private_key=…, jwt_expiry=…, jwt_issued_at=…, jwt_algorithm=…)`` is deprecated, use ``github.GithubIntegration(auth=github.Auth.AppAuth(…))`` instead.
* The use of ``github.GithubIntegration.create_jwt`` is deprecated, use ``github.Github(auth=github.Auth.AppAuth)``, ``github.Auth.AppAuth.token`` or ``github.Auth.AppAuth.create_jwt(expiration)`` instead.
* The use of ``AppAuthentication`` is deprecated, use ``github.Auth.AppInstallationAuth`` instead.
* The use of ``github.Github.get_app()`` without providing argument ``slug`` is deprecated, use ``github.GithubIntegration(auth=github.Auth.AppAuth(…)).get_app()``.

Bug Fixes
^^^^^^^^^

* Test and fix UTC issue with AppInstallationAuth (#2561) (ff3b80f8)
* Make Requester.__createException robust against missing message and body (#2159) (7be3f763)
* Fix auth issues with `Installation.get_repos` (#2547) (64075120)
* Fix broken urls in docstrings (#2393) (f82ad61c)
* Raise error on unsupported redirects, log supported redirects (#2524) (17cd0b79)
* Fix GithubIntegration that uses expiring jwt (#2460) (5011548c)
* Add expiration argument back to GithubIntegration.create_jwt (#2439) (822fc05c)
* Add crypto extras to pyjwt, which pulls in cryptogaphy package (#2443) (554b2b28)
* Remove RLock from Requester (#2446) (45f3d723)
* Move CI to Python 3.11 release and 3.12 dev (#2434) (e414c322)
* Pass Requester base URL to integration (#2420) (bdceae2f)

Improvements
^^^^^^^^^^^^

* Add Webhook Deliveries (#2508) (517ad336)
* Add support for workflow jobs and steps (#1951) (804c3107)
* Add support for get_app() with App authentication (#2549) (6d4b6d14)
* Allow multiline comments in PullRequest (#2540) (6a21761e)
* Implement `AppUserAuth` for Github App user tokens (#2546) (f291a368)
* Add support for environments (#2223) (0384e2fd)
* Add support for new RepositoryAdvisories API :tada: (#2483) (daf62bd4)
* Make `MainClass.get_app` return completed `GithubApp` when slug is given (#2543) (84912a67)
* Add authentication classes, move auth logic there (#2528) (fc2d0e15)
* Add sort order and direction for getting comments (#2544) (a8e7c423)
* Add `name` filter to `Repository.get_artifacts()` (#2459) (9f52e948)
* Add `name`, `display_title` and `path` attributes to `WorkflowRun` (#2397) (10816389)
* Add new `create_fork` arguments (#2493) (b94a83cb)
* add `ref` to Deployment (#2489) (e8075c41)
* Add query `check_suite_id` integer to `Workflow.get_runs` (#2466) (a4854519)
* Add `generate_release_notes` parameter to `create_git_release` and `create_git_tag_and_release` (#2417) (49b3ae16)
* Add example for Pull Request comments to documentation (#2390) (c2f12bdc)
* Add allow_auto_merge support to Repository (#2477) (8c4b9465)
* Add `artifact_id` argument to `Repository.get_artifact()` (#2458) (4fa0a5f3)
* Add missing attributes to Branch (#2512) (e296dbdb)
* Add allow_update_branch option to Organization (#2465) (bab4180f)
* Add support for Issue.state_reason #2370 (#2392) (5aa544a1)
* Add parameters to Repository.get_workflow_runs (#2408) (4198dbfb)

Maintenance
^^^^^^^^^^^

* Add type stub for MainClass.get_project_column (#2502) (d514222c)
* Sync GithubIntegration __init__ arguments with github.Github (#2556) (ea45237d)
* Update MAINTAINERS (#2545) (f4e9dcb3)
* Link to stable docs, update introduction in package used by pypi, move auth arg front (#2557) (006766f9)
* Merge PaginatedList.pyi back to source (#2555) (cb50dec5)
* Merge GithubObject.pyi/Requester.pyi stubs back to source (#2463) (b6258f4b)
* [CI] Moving linting into separate workflow (#2522) (52fc1077)
* Merging 1.58.x patch release notes into master (#2525) (217d4241)
* Merge AppAuthentication.pyi to source (#2519) (8e8cfb30)
* Merge GithubException.pyi stubs back to source (#2464) (03a2f696)
* Add missing fields from `GithubCredentials.py` to CONTRIBUTING.md (#2482) (297317ba)
* Update docstring and typing for allow_forking and allow_update_branch (Repository) (#2529) (600217f0)
* Bump actions/checkout from 2 to 3.1.0 (#2327) (300c5015)
* RTD: install current project (def5223c)
* Add current dir sys.path as well (9c96faa7)
* Use use_scm_version to get current version from git tag (#2429) (3ea91a3a)

Version 1.58.2 (May 09, 2023)
-----------------------------------

Bug Fixes
^^^^^^^^^

* Fix GithubIntegration that uses expiring jwt (#2460) (5011548c)

Version 1.58.1 (March 18, 2023)
-----------------------------------

Bug Fixes
^^^^^^^^^

* Add expiration argument back to GithubIntegration.create_jwt (#2439) (822fc05c)
* Add crypto extras to pyjwt, which pulls in cryptogaphy package (#2443) (554b2b28)
* Remove RLock from Requester (#2446) (45f3d723)
* Move CI to Python 3.11 release and 3.12 dev (#2434) (e414c322)
* pass requester base URL to integration (#2420) (bdceae2f)
* RTD: install current project (def5223c)
* Add current dir sys.path as well (9c96faa7)
* Use use_scm_version to get current version from git tag (#2429) (3ea91a3a)

Version 1.58.0 (February 19, 2023)
-----------------------------------

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Add unarchiving support @Tsuesun (#2391)
* Support full GitHub app authentication @dblanchette (#1986)
* Continue the PR #1899 @Felixoid (#2386)
* feat: add allow\_forking to Repository @IbrahimAH (#2380)
* Add code scanning alerts @eric-nieuwland (#2227)

Version 1.57 (November 05, 2022)
-----------------------------------

Breaking Changes
^^^^^^^^^^^^^^^^

* Add support for Python 3.11, drop support for Python 3.6 (#2332) (1e2f10dc)

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Speed up get requested reviewers and teams for pr (#2349) (6725eceb)
* [WorkflowRun] - Add missing attributes (`run_started_at` & `run_attempt`), remove deprecated `unicode` type (#2273) (3a6235b5)
* Add support for repository autolink references (#2016) (0fadd6be)
* Add retry and pool_size to typing (#2151) (784a3efd)
* Fix/types for repo topic team (#2341) (db9337a4)
* Add class Artifact (#2313) (#2319) (437ff845)

Version 1.56 (October 13, 2022)
-----------------------------------

Important
^^^^^^^^^

This is the last release that will support Python 3.6.

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Create repo from template (#2090) (b50283a7)
* Improve signature of Repository.create_repo (#2118) (001970d4)
* Add support for 'visibility' attribute preview for Repositories (#1872) (8d1397af)
* Add Repository.rename_branch method (#2089) (6452ddfe)
* Add function to delete pending reviews on a pull request (#1897) (c8a945bb)
* Cover all code paths in search_commits (#2087) (f1faf941)
* Correctly deal when PaginatedList's data is a dict (#2084) (93b92cd2)
* Add two_factor_authentication in AuthenticatedUser. (#1972) (4f00cbf2)
* Add ProjectCard.edit() to the type stub (#2080) (d417e4c4)
* Add method to delete Workflow runs (#2078) (b1c8eec5)
* Implement organization.cancel_invitation() (#2072) (53fb4988)
* Feat: Add `html_url` property in Team Class. (#1983) (6570892a)
* Add support for Python 3.10 (#2073) (aa694f8e)
* Add github actions secrets to org (#2006) (bc5e5950)
* Correct replay for Organization.create_project() test (#2075) (fcc12368)
* Fix install command example (#2043) (99e00a28)
* Fix: #1671 Convert Python Bool to API Parameter for Authenticated User Notifications (#2001) (1da600a3)
* Do not transform requestHeaders when logging (#1965) (1265747e)
* Add type to OrderedDict (#1954) (ed7d0fe9)
* Add Commit.get_pulls() to pyi (#1958) (b4664705)
* Adding headers in GithubException is a breaking change (#1931) (d1644e33)

Version 1.55 (April 26, 2021)
-----------------------------------

Breaking Changes
^^^^^^^^^^^^^^^^

* Remove client_id/client_secret authentication (#1888) (901af8c8)
* Adjust to Github API changes regarding emails (#1890) (2c77cfad)
  - This impacts what AuthenticatedUser.get_emails() returns
* PublicKey.key_id could be int on Github Enterprise (#1894) (ad124ef4)
* Export headers in GithubException (#1887) (ddd437a7)

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Do not import from unpackaged paths in typing (#1926) (27ba7838)
* Implement hash for CompletableGithubObject (#1922) (4faff23c)
* Use property decorator to improve typing compatibility (#1925) (e4168109)
* Fix :rtype: directive (#1927) (54b6a97b)
* Update most URLs to docs.github.com (#1896) (babcbcd0)
* Tighten asserts for new Permission tests (#1893) (5aab6f5d)
* Adding attributes "maintain" and "triage" to class "Permissions" (#1810) (76879613)
* Add default arguments to Workflow method type annotations (#1857) (7d6bac9e)
* Re-raise the exception when failing to parse JSON (#1892) (916da53b)
* Allow adding attributes at the end of the list (#1807) (0245b758)
* Updating links to Github documentation for deploy keys (#1850) (c27fb919)
* Update PyJWT Version to 2.0+ (#1891) (a68577b7)
* Use right variable in both get_check_runs() (#1889) (3003e065)
* fix bad assertions in github.Project.edit (#1817) (6bae9e5c)
* Test repr() for PublicKey (#1879) (e0acd8f4)
* Add support for deleting repository secrets (#1868) (696793de)
* Switch repository secrets to using f-strings (#1867) (aa240304)
* Manually fixing paths for codecov.io to cover all project files (#1813) (b2232c89)
* Add missing links to project metadata (#1789) (64f532ae)
* No longer show username and password examples (#1866) (55d98373)
* Adding github actions secrets (#1681) (c90c050e)
* fix get_user_issues (#1842) (7db1b0c9)
* Switch all string addition to using f-strings (#1774) (290b6272)
* Enabling connection pool_size definition (a77d4f48)
* Always define the session adapter (aaec0a0f)

Version 1.54.1 (December 24, 2020)
-----------------------------------

* Pin pyjwt version (#1797) (31a1c007)
* Add pyupgrade to pre-commit configuration (#1783) (e113e37d)
* Fix #1731: Incorrect annotation (82c349ce)
* Drop support for Python 3.5 (#1770) (63e4fae9)
* Revert "Pin requests to <2.25 as well (#1757)" (#1763) (a806b523)
* Fix stubs file for Repository (fab682a5)

Version 1.54 (November 30, 2020)
-----------------------------------

Important
^^^^^^^^^

This is the last release that will support Python 3.5.

Breaking Changes
^^^^^^^^^^^^^^^^

The Github.get_installation(integer) method has been removed.
Repository.create_deployment()'s payload parameter is now a dictionary.

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Add support for Check Suites (#1764) (6d501b28)
* Add missing preview features of Deployment and Deployment Statuses API (#1674) (197e0653)
* Correct typing for Commit.get_comments() (#1765) (fcdd9eae)
* Pin requests to <2.25 as well (#1757) (d159425f)
* Add Support for Check Runs (#1727) (c77c0676)
* Added a method for getting a user by their id (#1691) (4cfc9912)
* Fix #1742 - incorrect typehint for `Installation.id` (#1743) (546f6495)
* Add WorkflowRun.workflow_id (#1737) (78a29a7c)
* Add support for Python 3.9 (#1735) (1bb18ab5)
* Added support for the Self-Hosted actions runners API (#1684) (24251f4b)
* Fix Branch protection status in the examples (#1729) (88800844)
* Filter the DeprecationWarning in Team tests (#1728) (23f47539)
* Added get_installations() to Organizations (#1695) (b42fb244)
* Fix #1507: Add new Teams: Add or update team repository endpoint (#1509) (1c55be51)
* Added support for `Repository.get_workflow_runs` parameters (#1682) (c23564dd)
* feat(pullrequest): add the rebaseable attribute (#1690) (ee4c7a7e)
* Add support for deleting reactions (#1708) (f7d203c0)
* Correct type hint for InputGitTreeElement.sha (08b72b48)
* Ignore new black formatting commit for git blame (#1680) (7ec4f155)
* Format with new black (#1679) (07e29fe0)
* Add get_timeline() to Issue's type stubs (#1663) (6bc9ecc8)

Version 1.53 (August 18, 2020)
-----------------------------------

* Test Organization.get_hook() (#1660) (2646a98c)
* Add method get_team_membership for user to Team  (#1658) (749e8d35)
* Add typing files for OAuth classes (#1656) (429fcc73)
* Fix Repository.create_repository_dispatch type signature (#1643) (f891bd61)
* PaginatedList's totalCount is 0 if no last page (#1641) (69b37b4a)
* Add initial support for Github Apps. (#1631) (260558c1)
* Correct ``**kwargs`` typing for ``search_*`` (#1636) (165d995d)
* Add delete_branch_on_merge arg to Repository.edit type stub (#1639) (15b5ae0c)
* Fix type stub for MainClass.get_user (#1637) (8912be64)
* Add type stub for Repository.create_fork (#1638) (de386dfb)
* Correct Repository.create_pull typing harder (#1635) (5ad091d0)

Version 1.52 (August 03, 2020)
-----------------------------------

* upload_asset with data in memory (#1601) (a7786393)
* Make Issue.closed_by nullable (#1629) (06dae387)
* Add support for workflow dispatch event (#1625) (16850ef1)
* Do not check reaction_type before sending (#1592) (136a3e80)
* Various Github Action improvement (#1610) (416f2d0f)
* more flexible header splitting (#1616) (85e71361)
* Create Dependabot config file (#1607) (e272f117)
* Add support for deployment statuses (#1588) (048c8a1d)
* Adds the 'twitter_username' attribute to NamedUser. (#1585) (079f75a7)
* Create WorkflowRun.timing namedtuple from the dict (#1587) (1879518e)
* Add missing properties to PullRequest.pyi (#1577) (c84fad81)
* Add support for Workflow Runs (#1583) (4fb1d23f)
* More precise typing for Repository.create_pull (#1581) (4ed7aaf8)
* Update sphinx-rtd-theme requirement from <0.5 to <0.6 (#1563) (f9e4feeb)
* More precise typing for MainClass.get_user() (#1575) (3668f866)
* Small documentation correction in Repository.py (#1565) (f0f6ec83)
* Remove "api_preview" parameter from type stubs and docstrings
  (#1559) (cc1b884c)
* Upgrade actions/setup-python to v2 (#1555) (6f1640d2)
* Clean up tests for GitReleaseAsset (#1546) (925764ad)
* Repository.update_file() content also accepts bytes (#1543) (9fb8588b)
* Fix Repository.get_issues stub (#1540) (b40b75f8)
* Check all arguments of NamedUser.get_repos() (#1532) (69bfc325)
* Correct Workflow typing (#1533) (f41c046f)
* Remove RateLimit.rate (#1529) (7abf6004)
* PullRequestReview is not a completable object (#1528) (19fc43ab)
* Test more attributes (#1526) (52ec366b)
* Remove pointless setters in GitReleaseAsset (#1527) (1dd1cf9c)
* Drop some unimplemented methods in GitRef (#1525) (d4b61311)
* Remove unneeded duplicate string checks in Branch (#1524) (61b61092)
* Turn on coverage reporting for codecov (#1522) (e79b9013)
* Drastically increase coverage by checking repr() (#1521) (291c4630)
* Fixed formatting of docstrings for `Repository.create_git_tag_and_release()`
  and `StatsPunchCard`. (#1520) (ce400bc7)
* Remove Repository.topics (#1505) (53d58d2b)
* Small improvements to typing (#1517) (7b20b13d)
* Correct Repository.get_workflows() (#1518) (8727003f)
* docs(repository): correct releases link (#1514) (f7cc534d)
* correct Repository.stargazers_count return type to int (#1513) (b5737d41)
* Fix two RST warnings in Webhook.rst (#1512) (5a8bc203)
* Filter FutureWarning for 2 test cases (#1510) (09a1d9e4)
* Raise a FutureWarning on use of client_{id,secret} (#1506) (2475fa66)
* Improve type signature for create_from_raw_data (#1503) (c7b5eff0)
* feat(column): move, edit and delete project columns (#1497) (a32a8965)
* Add support for Workflows (#1496) (a1ed7c0e)
* Add create_repository_dispatch to typing files (#1502) (ba9d59c2)
* Add OAuth support for GitHub applications (4b437110)
* Create AccessToken entity (4a6468aa)
* Extend installation attributes (61808da1)

Version 1.51 (May 03, 2020)
-----------------------------------

* Type stubs are now packaged with the build (#1489) (6eba4506)
* Travis CI is now dropped in favor of Github workflow (#1488) (d6e77ba1)
* Get the project column by id (#1466) (63855409)

Version 1.50 (April 26, 2020)
-----------------------------------

New features
^^^^^^^^^^^^

* PyGithub now supports type checking thanks to (#1231) (91433fe9)
* Slack is now the main channel of communication rather than Gitter (6a6e7c26)
* Ability to retrieve public events (#1481) (5cf9950b)
* Add and handle the maintainer_can_modify attribute in PullRequest (#1465) (e0997b43)
* List matching references (#1471) (d3bc6a5c)
* Add create_repository_dispatch (#1449) (edcbdfda)
* Add some Organization and Repository attributes. (#1468) (3ab97d61)
* Add create project method (801ea385)

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Drop use of shadow-cat for draft PRs (#1469) (84bb69ab)
* AuthenticatedUser.get_organization_membership() should be str (#1473) (38b34db5)
* Drop documentation for len() of PaginatedList (#1470) (70462598)
* Fix param name of projectcard's move function (#1451) (bafc4efc)
* Correct typos found with codespell (#1467) (83bef0f7)
* Export IncompletableObject in the github namespace (#1450) (0ebdbb26)
* Add GitHub Action workflow for checks (#1464) (f1401c15)
* Drop unneeded ignore rule for flake8 (#1454) (b4ca9177)
* Use pytest to parametrize tests (#1438) (d2e9bd69)

Version 1.47 (March 15, 2020)
-----------------------------------

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Add support to edit and delete a project (#1434) (f11f7395)
* Add method for fetching pull requests associated with a commit (#1433) (0c55381b)
* Add "get_repo_permission" to Team class (#1416) (219bde53)
* Add list projects support, update tests (#1431) (e44d11d5)
* Don't transform completely in PullRequest.*assignees (#1428) (b1c35499)
* Add create_project support, add tests (#1429) (bf62f752)
* Add draft attribute, update test (bd285248)
* Docstring for Repository.create_git_tag_and_release (#1425) (bfeacded)
* Create a tox docs environment (#1426) (b30c09aa)
* Add Deployments API (#1424) (3d93ee1c)
* Add support for editing project cards (#1418) (425280ce)
* Add draft flag parameter, update tests (bd0211eb)
* Switch to using pytest (#1423) (c822dd1c)
* Fix GitMembership with a hammer (#1420) (f2939eb7)
* Add support to reply to a Pull request comment (#1374) (1c82573d)
* PullRequest.update_branch(): allow expected_head_sha to be empty (#1412) (806130e9)
* Implement ProjectCard.delete() (#1417) (aeb27b78)
* Add pre-commit plugin for black/isort/flake8 (#1398) (08b1c474)
* Add tox (#1388) (125536fe)
* Open file in text mode in scripts/add_attribute.py (#1396) (0396a493)
* Silence most ResourceWarnings (#1393) (dd31a706)
* Assert more attributes in Membership (#1391) (d6dee016)
* Assert on changed Repository attributes (#1390) (6e3ceb19)
* Add reset to the repr for Rate (#1389) (0829af81)

Version 1.46 (February 11, 2020)
-----------------------------------
Important
^^^^^^^^^

Python 2 support has been removed. If you still require Python 2, use 1.45.

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Add repo edit support for delete_branch_on_merge (#1381) (9564cd4d)
* Fix mistake in Repository.create_fork() (#1383) (ad040baf)
* Correct two attributes in Invitation (#1382) (882fe087)
* Search repo issues by string label (#1379) (4ae1a1e5)
* Correct Repository.create_git_tag_and_release() (#1362) (ead565ad)
* exposed seats and filled_seats for Github Organization Plan (#1360) (06a300ae)
* Repository.create_project() body is optional (#1359) (0e09983d)
* Implement move action for ProjectCard (#1356) (b11add41)
* Tidy up ProjectCard.get_content() (#1355) (dd80a6c0)
* Added nested teams and parent (#1348) (eacabb2f)
* Correct parameter for Label.edit (#1350) (16e5f989)
* doc: example of Pull Request creation (#1344) (d5ad09ae)
* Fix PyPI wheel deployment (#1330) (4561930b)

Version 1.45 (December 29, 2019)
-----------------------------------
Important
^^^^^^^^^

* This is the last release of PyGithub that will support Python 2.

Breaking Changes
^^^^^^^^^^^^^^^^

* Branch.edit_{user,team}_push_restrictions() have been removed
* The new API is:
  - Branch.add_{user,team}_push_restrictions() to add new members
  - Branch.replace_{user,team}_push_restrictions() to replace all members
  - Branch.remove_{user,team}_push_restrictions() to remove members
* The api_preview parameter to Github() has been removed.

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Allow sha=None for InputGitTreeElement (#1327) (60464f65)
* Support github timeline events. (#1302) (732fd26a)
* Update link to GitHub Enterprise in README (#1324) (e1537f79)
* Cleanup travis config (#1322) (8189a538)
* Add support for update branch  (#1317) (baddb719)
* Refactor Logging tests (#1315) (b0ef1909)
* Fix rtd build (b797cac0)
* Add .git-blame-ignore-revs (573c674b)
* Apply black to whole codebase (#1303) (6ceb9e9a)
* Fix class used returning pull request comments (#1307) (f8e33620)
* Support for create_fork (#1306) (2ad51f35)
* Use Repository.get_contents() in tests (#1301) (e40768e0)
* Allow GithubObject.update() to be passed headers (#1300) (989b635e)
* Correct URL for assignees on PRs (#1296) (3170cafc)
* Use inclusive ordered comparison for 'parameterized' requirement (#1281) (fb19d2f2)
* Deprecate Repository.get_dir_contents() (#1285) (21e89ff1)
* Apply some polish to manage.sh (#1284) (3a723252)

Version 1.44.1 (November 07, 2019)
-----------------------------------

* Add Python 3.8 to classifiers list (#1280) (fec6034a)
* Expand Topic class and add test coverage (#1252) (ac682742)
* Add support for team discussions (#1246) (#1249) (ec3c8d7b)
* Correct API for NamedUser.get_organization_membership (#1277) (077c80ba)
* Correct header check for 2FA required (#1274) (6ad592b1)
* Use replay framework for Issue142 test (#1271) (4d258d93)
* Sync httpretty version requirement with setup.py (#1265) (99d38468)
* Handle unicode strings when recording responses (#1253) (#1254) (faa1bbd6)
* Add assignee removal/addition support to PRs (#1241) (a163ba15)
* Check if the version is empty in manage.sh (#1268) (db294837)
* Encode content for {create,update}_file (#1267) (bc225f9d)
* Update changes.rst (#1263) (d7947d82)

Version 1.44 (October 19, 2019)
-----------------------------------

New features
^^^^^^^^^^^^

* This version supports running under Python 3 directly, and the test suite
  passes under both 2.7 and recent 3.x's.

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Stop ignoring unused imports and remove them (#1250) (a0765083)
* Bump httpretty to be a greater or equal to (#1262) (27092fb0)
* Add close all issues example (#1256) (13e2c7c7)
* Add six to install_requires (#1245) (a840a906)
* Implemented user organization membership. Added test case. (#1237) (e50420f7)
* Create DEPLOY.md (c9ed82b2)
* Support non-default URLs in GithubIntegration (#1229) (e33858a3)
* Cleanup try/except import in PaginatedList (#1228) (89c967bb)
* Add an IncompletableObject exception (#1227) (f91cbac2)
* Fix redundant int checks (#1226) (850da5af)
* Jump from notifications to related PRs/issues. (#1168) (020fbebc)
* Code review bodies are optional in some cases. (#1169) (b84d9b19)
* Update changes.rst (#1223) (2df7269a)
* Do not auto-close issues with high priority tag (ab27ba4d)
* Fix bug in repository create new file example PyGithub#1210 (#1211) (74cd6856)
* Remove more Python version specific code (#1193) (a0f01cf9)
* Drop use of assertEquals (#1194) (7bac694a)
* Fix PR review creation. (#1184) (e90cdab0)
* Add support to vulnerability alert and automated security fixes APIs (#1195) (8abd50e2)
* Delete Legacy submodule (#1192) (7ddb657d)
* Remove some uses of atLeastPython3 (#1191) (cca8e3a5)
* Run flake8 in Travis (#1163) (f93207b4)
* Fix directories for coverage in Travis (#1190) (657f87b5)
* Switch to using six (#1189) (dc2f2ad8)
* Update Repository.update_file() docstring (#1186) (f1ae7200)
* Correct return type of MainClass.get_organizations (#1179) (6e79d270)
* Add cryptography to test-requirements.txt (#1165) (9b1c1e09)

Version 1.43.8 (July 20, 2019)
-----------------------------------

New features
^^^^^^^^^^^^

* Add two factor attributes on organizations (#1132) (a0731685)
* Add Repository methods for pending invitations (#1159) (57af1e05)
* Adds `get_issue_events` to `PullRequest` object (#1154) (acd515aa)
* Add invitee and inviter to Invitation (#1156) (0f2beaca)
* Adding support for pending team invitations (#993) (edab176b)
* Add support for custom base_url in GithubIntegration class (#1093) (6cd0d644)
* GithubIntegration: enable getting installation (#1135) (18187045)
* Add sorting capability to Organization.get_repos() (#1139) (ef6f009d)
* Add new Organization.get_team_by_slug method (#1144) (4349bca1)
* Add description field when creating a new team (#1125) (4a37860b)
* Handle a path of / in Repository.get_contents() (#1070) (102c8208)
* Add issue lock/unlock (#1107) (ec7bbcf5)

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Fix bug in recursive repository contents example (#1166) (8b6b4505)
* Allow name to be specified for upload_asset (#1151) (8d2a6b53)
* Fixes #1106 for GitHub Enterprise API (#1110) (54065792)

Deprecation
^^^^^^^^^^^

* Repository.get_file_contents() no longer works use Repository.get_contents() instead

Version 1.43.7 (April 16, 2019)
-----------------------------------

* Exclude tests from PyPI distribution (#1031) (78d283b9)
* Add codecov badge (#1090) (4c0b54c0)

Version 1.43.6 (April 05, 2019)
-----------------------------------

New features
^^^^^^^^^^^^

* Add support for Python 3.7 (#1028) (6faa00ac)
* Adding HTTP retry functionality via urllib3 (#1002) (5ae7af55)
* Add new dismiss() method on PullRequestReview (#1053) (8ef71b1b)
* Add since and before to `get_notifications` (#1074) (7ee6c417)
* Add url parameter to include anonymous contributors in `get_contributors` (#1075) (293846be)
* Provide option to extend expiration of jwt token (#1068) (86a9d8e9)

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Fix the default parameter for `PullRequest.create_review` (#1058) (118def30)
* Fix `get_access_token` (#1042) (6a89eb64)
* Fix `Organization.add_to_members` role passing (#1039) (480f91cf)

Deprecation
^^^^^^^^^^^

* Remove Status API (6efd6318)

Version 1.43.5 (January 29, 2019)
-----------------------------------

* Add project column create card (#1003) (5f5c2764)
* Fix request got an unexpected keyword argument body (#1012) (ff789dcc)
* Add missing import to PullRequest (#1007) (b5122768)

Version 1.43.4 (December 21, 2018)
-----------------------------------

New features
^^^^^^^^^^^^

* Add Migration API (#899) (b4d895ed)
* Add Traffic API (#977) (a433a2fe)
* New in Project API: create repository project, create project column (#995) (1c0fd97d)

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Change type of GitRelease.author to NamedUser (#969) (aca50a75)
* Use total_count from data in PaginatedList (#963) (ec177610)

Version 1.43.3 (October 31, 2018)
-----------------------------------

New features
^^^^^^^^^^^^

* Add support for JWT authentication (#948) (8ccf9a94)
* Added support for required signatures on protected branches (#939) (8ee75a28)
* Ability to filter repository collaborators (#938) (5687226b)
* Mark notification as read (#932) (0a10d7cd)
* Add highlight search to ``search_code`` function (#925) (1fa25670)
* Adding ``suspended_at`` property to NamedUSer (#922) (c13b43ea)
* Add since parameter for Gists (#914) (e18b1078)

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

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


Bug Fixes
^^^^^^^^^

* ``Repository.get_archive_link`` will now NOT follow HTTP redirect and return the url instead (#858) (43d325a5)
* Fixed ``Gistfile.content`` (#486) (e1df09f7)
* Restored NamedUser.contributions attribute (#865) (b91dee8d)

New features
^^^^^^^^^^^^

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

Improvements
^^^^^^^^^^^^

* Add missing arguments to ``Repository.edit`` (#844) (29d23151)
* Add missing attributes to Repository (#842) (2b352fb3)
* Adding archival support for ``Repository.edit`` (#843) (1a90f5db)
* Add ``tag_name`` and ``target_commitish`` arguments to ``GitRelease.update_release`` (#834) (790f7dae)
* Allow editing of Team descriptions (#839) (c0021747)
* Add description to Organizations (#838) (1d918809)
* Add missing attributes for IssueEvent (#857) (7ac2a2a)
* Change ``MainClass.get_repo`` default laziness (#882) (6732517)

Deprecation
^^^^^^^^^^^

* Removed Repository.get_protected_branch (#871) (49db6f8)


Version 1.42 (August 19, 2018)
-----------------------------------

* Fix travis upload issue

Bug Fixes
^^^^^^^^^

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

Bug Fixes
^^^^^^^^^

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
* Fix different case (fcf6cfb)
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
* fix python3 compatibility error in test case (00777db)
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
* Remove ``Repository.create_download`` and ``NamedUser.create_gist`` as the corresponding APIs are not documented anymore

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

* Major improvement: support Python 3! PyGithub is automatically tested on `Travis <http://travis-ci.org/jacquev6/PyGithub>`__ with versions 2.5, 2.6, 2.7, 3.1 and 3.2 of Python
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
* Authorizations
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
