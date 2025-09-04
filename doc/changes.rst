Change log
==========

Stable versions
~~~~~~~~~~~~~~~

Version 2.8.1 (September 02, 2025)
----------------------------------

Bug Fixes
^^^^^^^^^
* Use default type if known type is not supported (`#3365 <https://github.com/PyGithub/PyGithub/pull/3365>`_) (`40506415 <https://github.com/PyGithub/PyGithub/commit/40506415>`_)

Version 2.8.0 (September 02, 2025)
----------------------------------

New Features
^^^^^^^^^^^^
* Add self hosted runner management to Organization (`#3203 <https://github.com/PyGithub/PyGithub/pull/3203>`_) (`4ea1c4e2 <https://github.com/PyGithub/PyGithub/commit/4ea1c4e2>`_)
* Add support to generate release notes (`#3022 <https://github.com/PyGithub/PyGithub/pull/3022>`_) (`e359b83a <https://github.com/PyGithub/PyGithub/commit/e359b83a>`_)

Improvements
^^^^^^^^^^^^
* Fix connection pooling to improve connection performance (`#3289 <https://github.com/PyGithub/PyGithub/pull/3289>`_)
* Add ``Repository.get_automated_security_fixes`` method (`#3303 <https://github.com/PyGithub/PyGithub/pull/3303>`_) (`22048d83 <https://github.com/PyGithub/PyGithub/commit/22048d83>`_)
* Sync ``Issue`` class with API spec (`#3338 <https://github.com/PyGithub/PyGithub/pull/3338>`_) (`62da467a <https://github.com/PyGithub/PyGithub/commit/62da467a>`_)
* Return more union classes like ``NamedUser | Organization | Enterprise`` (`#3224 <https://github.com/PyGithub/PyGithub/pull/3224>`_) (`aea64148 <https://github.com/PyGithub/PyGithub/commit/aea64148>`_)
* Sync ``Enterprise`` class with API spec (`#3342 <https://github.com/PyGithub/PyGithub/pull/3342>`_) (`01bb5ab1 <https://github.com/PyGithub/PyGithub/commit/01bb5ab1>`_)
* Sync ``GitReleaseAsset`` class with API spec (`#3343 <https://github.com/PyGithub/PyGithub/pull/3343>`_) (`74449fed <https://github.com/PyGithub/PyGithub/commit/74449fed>`_)
* Sync many class with OpenAPI spec (`#3344 <https://github.com/PyGithub/PyGithub/pull/3344>`_)
* Point deprecation warnings to the caller code rather than inner class (`#3275 <https://github.com/PyGithub/PyGithub/pull/3275>`_) (`99bb5270 <https://github.com/PyGithub/PyGithub/commit/99bb5270>`_)
* Allow for repo strings in all ``Team`` repo methods (`#3356 <https://github.com/PyGithub/PyGithub/pull/3356>`_) (`3234a21f <https://github.com/PyGithub/PyGithub/commit/3234a21f>`_)

Bug Fixes
^^^^^^^^^
* Fix  API path of ``Repository.get_git_ref`` (`#2992 <https://github.com/PyGithub/PyGithub/pull/2992>`_) (`a6965031 <https://github.com/PyGithub/PyGithub/commit/a6965031>`_)
* Rework redirection URL allowance check (`#3329 <https://github.com/PyGithub/PyGithub/pull/3329>`_) (`065b1319 <https://github.com/PyGithub/PyGithub/commit/065b1319>`_)
* Fix ``GitRelease.name``, deprecate ``GitRelease.title`` (`#3346 <https://github.com/PyGithub/PyGithub/pull/3346>`_) (`fb51957f <https://github.com/PyGithub/PyGithub/commit/fb51957f>`_)
* Remove ``"COMMENT"`` as the default event for ``create_review`` (`#3078 <https://github.com/PyGithub/PyGithub/pull/3078>`_) (`8494da5c <https://github.com/PyGithub/PyGithub/commit/8494da5c>`_)
* Add support for public release assets (`#3339 <https://github.com/PyGithub/PyGithub/pull/3339>`_) (`abad296e <https://github.com/PyGithub/PyGithub/commit/abad296e>`_)
* Fix GitHub breaking API change of ``maintainers`` in ``Organization.create_team`` (`#3291 <https://github.com/PyGithub/PyGithub/pull/3291>`_) (`17bc4df4 <https://github.com/PyGithub/PyGithub/commit/17bc4df4>`_)

Maintenance
^^^^^^^^^^^
* Minor fix to release.yml (`#3201 <https://github.com/PyGithub/PyGithub/pull/3201>`_) (`f1fc6e7c <https://github.com/PyGithub/PyGithub/commit/f1fc6e7c>`_)
* Reduce test replay data (`#3243 <https://github.com/PyGithub/PyGithub/pull/3243>`_) (`19426454 <https://github.com/PyGithub/PyGithub/commit/19426454>`_)
* Add check to OpenAPI script to check doc-string verbs (`#3332 <https://github.com/PyGithub/PyGithub/pull/3332>`_) (`3efde77d <https://github.com/PyGithub/PyGithub/commit/3efde77d>`_)
* Improve apply OpenAPI schemas (`#3333 <https://github.com/PyGithub/PyGithub/pull/3333>`_) (`ec189dd6 <https://github.com/PyGithub/PyGithub/commit/ec189dd6>`_)
* Add config to OpenAPI script to ignore schemas (`#3334 <https://github.com/PyGithub/PyGithub/pull/3334>`_) (`0478d33b <https://github.com/PyGithub/PyGithub/commit/0478d33b>`_)
* Add suggest and create method feature to OpenAPI script (`#3318 <https://github.com/PyGithub/PyGithub/pull/3318>`_)
* Fix CI OpenApi apply command (`#3341 <https://github.com/PyGithub/PyGithub/pull/3341>`_) (`cdc10a27 <https://github.com/PyGithub/PyGithub/commit/cdc10a27>`_)
* Improve OpenAPI scripts (`#3340 <https://github.com/PyGithub/PyGithub/pull/3340>`_) (`ad278c5f <https://github.com/PyGithub/PyGithub/commit/ad278c5f>`_)
* Improve OpenAPI CI (`#3347 <https://github.com/PyGithub/PyGithub/pull/3347>`_) (`8165bbc9 <https://github.com/PyGithub/PyGithub/commit/8165bbc9>`_)
* Rework test framework (`#3271 <https://github.com/PyGithub/PyGithub/pull/3271>`_) (`1b700187 <https://github.com/PyGithub/PyGithub/commit/1b700187>`_)
* Some minor fixes to OpenAPI scripts (`#3350 <https://github.com/PyGithub/PyGithub/pull/3350>`_) (`a813a945 <https://github.com/PyGithub/PyGithub/commit/a813a945>`_)
* Add manual workflow to fix auto-fixable issues (`#3351 <https://github.com/PyGithub/PyGithub/pull/3351>`_) (`0e6317d9 <https://github.com/PyGithub/PyGithub/commit/0e6317d9>`_)
* Bump actions/download-artifact from 4 to 5 (`#3330 <https://github.com/PyGithub/PyGithub/pull/3330>`_) (`5206d231 <https://github.com/PyGithub/PyGithub/commit/5206d231>`_)
* Use default per-page const in ``PaginatedList`` (`#3039 <https://github.com/PyGithub/PyGithub/pull/3039>`_) (`cffda3d7 <https://github.com/PyGithub/PyGithub/commit/cffda3d7>`_)
* Bump actions/setup-python from 4 to 5 (`#3283 <https://github.com/PyGithub/PyGithub/pull/3283>`_) (`f742be03 <https://github.com/PyGithub/PyGithub/commit/f742be03>`_)
* Bump actions/checkout from 3 to 5 (`#3348 <https://github.com/PyGithub/PyGithub/pull/3348>`_) (`2a1fd58d <https://github.com/PyGithub/PyGithub/commit/2a1fd58d>`_)
* Various minor OpenAPI scripts fixes (`#3353 <https://github.com/PyGithub/PyGithub/pull/3353>`_) (`8e40043e <https://github.com/PyGithub/PyGithub/commit/8e40043e>`_)
* Add union class support to OpenAPI script (`#3354 <https://github.com/PyGithub/PyGithub/pull/3354>`_) (`4a6bba93 <https://github.com/PyGithub/PyGithub/commit/4a6bba93>`_)
* Add ``github_actions`` label to Maintenance section (`#3357 <https://github.com/PyGithub/PyGithub/pull/3357>`_) (`0c31f848 <https://github.com/PyGithub/PyGithub/commit/0c31f848>`_)
* Upgrade docformatter pre-commit hook (`#3359 <https://github.com/PyGithub/PyGithub/pull/3359>`_) (`6ec3ca24 <https://github.com/PyGithub/PyGithub/commit/6ec3ca24>`_)
* Add warning about Checks API in doc-strings (`#3229 <https://github.com/PyGithub/PyGithub/pull/3229>`_) (`12d8d10c <https://github.com/PyGithub/PyGithub/commit/12d8d10c>`_)
* Update docs on development (`#3352 <https://github.com/PyGithub/PyGithub/pull/3352>`_) (`6f0d6efa <https://github.com/PyGithub/PyGithub/commit/6f0d6efa>`_)

Version 2.7.0 (July 31, 2025)
-----------------------------

Breaking Changes
^^^^^^^^^^^^^^^^

* Method ``Github.get_rate_limit()`` now returns ``RateLimitOverview`` rather than ``RateLimit`` (`#3205 <https://github.com/PyGithub/PyGithub/pull/3205>`_) (`56ee057a <https://github.com/PyGithub/PyGithub/commit/56ee057a>`_).

  Code like

  .. code-block:: python

    gh.get_rate_limit().core.remaining

  should be replaced with

  .. code-block:: python

    gh.get_rate_limit().resources.core.remaining

* Method ``GitTag.verification`` now returns ``GitCommitVerification`` rather than ``dict[str, Any]`` (`#3226 <https://github.com/PyGithub/PyGithub/pull/3226>`_) (`850932cc <https://github.com/PyGithub/PyGithub/commit/850932cc>`_).

  Code like

  .. code-block:: python

    tag.verification["reason"]
    tag.verification.get("reason")

  should be replaced with

  .. code-block:: python

    tag.verification.reason

Deprecations
^^^^^^^^^^^^

* Methods ``dismissal_users`` and ``dismissal_teams`` of ``RequiredPullRequestReviews`` are deprecated,
  use ``dismissal_restrictions.users`` and ``dismissal_restrictions.teams`` instead.

New Features
^^^^^^^^^^^^
* Add getting list of self-hosted runners of organization (`#3190 <https://github.com/PyGithub/PyGithub/pull/3190>`_) (`b4092b5d <https://github.com/PyGithub/PyGithub/commit/b4092b5d>`_)
* Apply OpenAPI spec (`#3317 <https://github.com/PyGithub/PyGithub/pull/3317>`_) (`858b9e5b <https://github.com/PyGithub/PyGithub/commit/858b9e5b>`_)
* Add support for Sub-Issues (`#3258 <https://github.com/PyGithub/PyGithub/pull/3258>`_) (`c7858c85 <https://github.com/PyGithub/PyGithub/commit/c7858c85>`_)

Improvement
^^^^^^^^^^^
* Refactor search results into separate classes (`#3204 <https://github.com/PyGithub/PyGithub/pull/3204>`_) (`938f80b1 <https://github.com/PyGithub/PyGithub/commit/938f80b1>`_)
* Add ``OrganizationInvitation`` (`#3207 <https://github.com/PyGithub/PyGithub/pull/3207>`_) (`038624c2 <https://github.com/PyGithub/PyGithub/commit/038624c2>`_)
* Add and apply missing schemas (`#3209 <https://github.com/PyGithub/PyGithub/pull/3209>`_) (`f4d586b4 <https://github.com/PyGithub/PyGithub/commit/f4d586b4>`_)
* Sync ``RepositoryAdvisory`` tests with OpenAPI spec (`#3215 <https://github.com/PyGithub/PyGithub/pull/3215>`_) (`6b77787a <https://github.com/PyGithub/PyGithub/commit/6b77787a>`_)
* Sync ``ProjectColumn`` and ``ProjectCard`` tests with OpenAPI spec (`#3216 <https://github.com/PyGithub/PyGithub/pull/3216>`_) (`e91c8379 <https://github.com/PyGithub/PyGithub/commit/e91c8379>`_)
* Sync ``CopilotSeat`` class with API spec (`#3232 <https://github.com/PyGithub/PyGithub/pull/3232>`_) (`45f26a1b <https://github.com/PyGithub/PyGithub/commit/45f26a1b>`_)
* Sync ``HookDeliverySummary`` class with API spec (`#3233 <https://github.com/PyGithub/PyGithub/pull/3233>`_) (`bc1c5375 <https://github.com/PyGithub/PyGithub/commit/bc1c5375>`_)
* Sync ``RequiredPullRequestReviews`` class with API spec (`#3234 <https://github.com/PyGithub/PyGithub/pull/3234>`_) (`2f991c48 <https://github.com/PyGithub/PyGithub/commit/2f991c48>`_)
* Sync ``RequiredStatusChecks`` class with API spec (`#3236 <https://github.com/PyGithub/PyGithub/pull/3236>`_) (`0474507f <https://github.com/PyGithub/PyGithub/commit/0474507f>`_)
* Sync ``Team`` class with API spec (`#3237 <https://github.com/PyGithub/PyGithub/pull/3237>`_) (`fa8f9dfe <https://github.com/PyGithub/PyGithub/commit/fa8f9dfe>`_)
* Replace ``deprecated.deprecated()`` with ``typing_extensions.deprecated()`` (`#3255 <https://github.com/PyGithub/PyGithub/pull/3255>`_) (`1ac8da70 <https://github.com/PyGithub/PyGithub/commit/1ac8da70>`_)
* fix(CodeScanAlert): add missing attributes (`#3274 <https://github.com/PyGithub/PyGithub/pull/3274>`_) (`bdc58c38 <https://github.com/PyGithub/PyGithub/commit/bdc58c38>`_)
* Allow SHAs when creating PR comments (`#3248 <https://github.com/PyGithub/PyGithub/pull/3248>`_) (`95a6d400 <https://github.com/PyGithub/PyGithub/commit/95a6d400>`_)
* Get collaborator role name (`#3295 <https://github.com/PyGithub/PyGithub/pull/3295>`_) (`2d4785dd <https://github.com/PyGithub/PyGithub/commit/2d4785dd>`_)
* Adding ``prevent_self_review`` property to ``Repository.createEnvironment`` (`#3246 <https://github.com/PyGithub/PyGithub/pull/3246>`_) (`e2a05ff2 <https://github.com/PyGithub/PyGithub/commit/e2a05ff2>`_)
* Add ``PullRequest.get_issue_timeline`` method (`#3259 <https://github.com/PyGithub/PyGithub/pull/3259>`_) (`23a5bad3 <https://github.com/PyGithub/PyGithub/commit/23a5bad3>`_)
* Support built-in ``reversed()`` on ``PaginatedList`` (`#3260 <https://github.com/PyGithub/PyGithub/pull/3260>`_) (`95f015c8 <https://github.com/PyGithub/PyGithub/commit/95f015c8>`_)
* Relax 404 condition in ``Requester`` exception handling (`#3299 <https://github.com/PyGithub/PyGithub/pull/3299>`_) (`e7110bf4 <https://github.com/PyGithub/PyGithub/commit/e7110bf4>`_)

Bug Fixes
^^^^^^^^^
* Fix broken pickle support for ``Auth`` classes (`#3211 <https://github.com/PyGithub/PyGithub/pull/3211>`_) (`a1f328df <https://github.com/PyGithub/PyGithub/commit/a1f328df>`_)
* Remove schema from ``Deployment``, remove ``message`` attribute (`#3223 <https://github.com/PyGithub/PyGithub/pull/3223>`_) (`e91713e9 <https://github.com/PyGithub/PyGithub/commit/e91713e9>`_)
* Fix incorrect deprecated import (`#3225 <https://github.com/PyGithub/PyGithub/pull/3225>`_) (`a2071d70 <https://github.com/PyGithub/PyGithub/commit/a2071d70>`_)
* Add ``CodeSecurityConfigRepository`` returned by ``get_repos_for_code_security_config`` (`#3219 <https://github.com/PyGithub/PyGithub/pull/3219>`_) (`dbb32eed <https://github.com/PyGithub/PyGithub/commit/dbb32eed>`_)
* Fix ``Branch.get_required_status_checks`` return type (`#3235 <https://github.com/PyGithub/PyGithub/pull/3235>`_) (`66a3cc1c <https://github.com/PyGithub/PyGithub/commit/66a3cc1c>`_)
* Adds ``multi_select`` and ``true_false`` options to ``CustomProperty.value_type`` (`#3173 <https://github.com/PyGithub/PyGithub/pull/3173>`_) (`f51a3f48 <https://github.com/PyGithub/PyGithub/commit/f51a3f48>`_)
* Fix url encoding of strings with slashes in URLs (`#3263 <https://github.com/PyGithub/PyGithub/pull/3263>`_) (`da73fc8a <https://github.com/PyGithub/PyGithub/commit/da73fc8a>`_)
* Fix side-effect when removing Authorization key from headers (`#3313 <https://github.com/PyGithub/PyGithub/pull/3313>`_) (`0378ccee <https://github.com/PyGithub/PyGithub/commit/0378ccee>`_)
* Make ``TimingData.run_duration_ms`` optional (`#3268 <https://github.com/PyGithub/PyGithub/pull/3268>`_) (`131949b3 <https://github.com/PyGithub/PyGithub/commit/131949b3>`_)
* Normalize App ID to String & Enhance JWT Issuer Verification (`#3272 <https://github.com/PyGithub/PyGithub/pull/3272>`_) (`01196d67 <https://github.com/PyGithub/PyGithub/commit/01196d67>`_)
* Add ``delete_self_hosted_runner`` to ``Organization`` (`#3306 <https://github.com/PyGithub/PyGithub/pull/3306>`_)

Dependencies
^^^^^^^^^^^^
* Bump actions/checkout from 3 to 4 (`#2754 <https://github.com/PyGithub/PyGithub/pull/2754>`_) (`3657eeb9 <https://github.com/PyGithub/PyGithub/commit/3657eeb9>`_)

Maintenance
^^^^^^^^^^^
* Mention removal of ``AppAuth.private_key`` in changelog (`#3212 <https://github.com/PyGithub/PyGithub/pull/3212>`_) (`fae8f25d <https://github.com/PyGithub/PyGithub/commit/fae8f25d>`_)
* Remove wrong schema from Repository (`#3220 <https://github.com/PyGithub/PyGithub/pull/3220>`_) (`aee3a350 <https://github.com/PyGithub/PyGithub/commit/aee3a350>`_)
* Rename ``HookDeliveryRequest`` and ``…Response`` private headers fields (`#3221 <https://github.com/PyGithub/PyGithub/pull/3221>`_) (`13236d5d <https://github.com/PyGithub/PyGithub/commit/13236d5d>`_)
* Sort classes' functions (`#3231 <https://github.com/PyGithub/PyGithub/pull/3231>`_) (`bb00062d <https://github.com/PyGithub/PyGithub/commit/bb00062d>`_)
* Move all Python files to future annotations (`#3241 <https://github.com/PyGithub/PyGithub/pull/3241>`_) (`3602345a <https://github.com/PyGithub/PyGithub/commit/3602345a>`_)
* Fix return type of ``PaginatedList[int]`` (`#3240 <https://github.com/PyGithub/PyGithub/pull/3240>`_)
* Sync with OpenAPI spec (`#3244 <https://github.com/PyGithub/PyGithub/pull/3244>`_) (`5cef2c3d <https://github.com/PyGithub/PyGithub/commit/5cef2c3d>`_)
* Make token auth default in tests (`#3242 <https://github.com/PyGithub/PyGithub/pull/3242>`_) (`7a11f840 <https://github.com/PyGithub/PyGithub/commit/7a11f840>`_)
* Add ``Organization.get_repos_for_code_security_config`` test (`#3239 <https://github.com/PyGithub/PyGithub/pull/3239>`_) (`4d45a4f4 <https://github.com/PyGithub/PyGithub/commit/4d45a4f4>`_)
* Add Python 3.13 to CI (`#3253 <https://github.com/PyGithub/PyGithub/pull/3253>`_) (`29e8a96b <https://github.com/PyGithub/PyGithub/commit/29e8a96b>`_)
* Enhance PyGithub webhook documentation (`#3267 <https://github.com/PyGithub/PyGithub/pull/3267>`_) (`63438b6a <https://github.com/PyGithub/PyGithub/commit/63438b6a>`_)
* Create codeql.yml (`#3277 <https://github.com/PyGithub/PyGithub/pull/3277>`_) (`78267263 <https://github.com/PyGithub/PyGithub/commit/78267263>`_)
* Add schema to ``TimingData`` (`#3206 <https://github.com/PyGithub/PyGithub/pull/3206>`_) (`20b8c477 <https://github.com/PyGithub/PyGithub/commit/20b8c477>`_)
* Remove error schemas from classes (`#3202 <https://github.com/PyGithub/PyGithub/pull/3202>`_) (`6ea33845 <https://github.com/PyGithub/PyGithub/commit/6ea33845>`_)

Version 2.6.0 (February 15, 2025)
---------------------------------

Breaking Changes
^^^^^^^^^^^^^^^^

* Rework ``Views`` and ``Clones`` (`#3168 <https://github.com/PyGithub/PyGithub/pull/3168>`_) (`f7d52249 <https://github.com/PyGithub/PyGithub/commit/f7d52249>`_):

  View and clones traffic information returned by ``Repository.get_views_traffic`` and ``Repository.get_clones_traffic``
  now return proper PyGithub objects, instead of a ``dict``, with all information that used to be provided by the ``dict``:

  Code like

  .. code-block:: python

    repo.get_views_traffic().["views"].timestamp
    repo.get_clones_traffic().["clones"].timestamp

  should be replaced with

  .. code-block:: python

    repo.get_views_traffic().views.timestamp
    repo.get_clones_traffic().clones.timestamp

* Add ``GitCommitVerification`` class (`#3028 <https://github.com/PyGithub/PyGithub/pull/3028>`_) (`822e6d71 <https://github.com/PyGithub/PyGithub/commit/822e6d71>`_):

  Changes the return value of ``GitTag.verification`` and ``GitCommit.verification`` from ``dict`` to ``GitCommitVerification``.

  Code like

  .. code-block:: python

    tag.verification["reason"]
    commit.verification["reason"]

  should be replaced with

  .. code-block:: python

    tag.verification.reason
    commit.verification.reason

* Property ``AppAuth.private_key`` has been removed (`#3065 <https://github.com/PyGithub/PyGithub/pull/3065>`_) (`36697b22 <https://github.com/PyGithub/PyGithub/commit/36697b22>`_)

* Fix typos (`#3086 <https://github.com/PyGithub/PyGithub/pull/3086>`_) (`a50ae51b <https://github.com/PyGithub/PyGithub/commit/a50ae51b>`_):

  Property ``OrganizationCustomProperty.respository_id`` renamed to ``OrganizationCustomProperty.repository_id``.

New Features
^^^^^^^^^^^^
* Add capability for global laziness (`#2746 <https://github.com/PyGithub/PyGithub/pull/2746>`_) (`f23da453 <https://github.com/PyGithub/PyGithub/commit/f23da453>`_)
* Add Support for GitHub Copilot Seat Management in Organizations (`#3082 <https://github.com/PyGithub/PyGithub/pull/3082>`_) (`b5f8f078 <https://github.com/PyGithub/PyGithub/commit/b5f8f078>`_)
* Get branches where commit is head (`#3083 <https://github.com/PyGithub/PyGithub/pull/3083>`_) (`3d84a47a <https://github.com/PyGithub/PyGithub/commit/3d84a47a>`_)
* Support downloading a Release Asset (`#3060 <https://github.com/PyGithub/PyGithub/pull/3060>`_) (`67cfdb21 <https://github.com/PyGithub/PyGithub/commit/67cfdb21>`_)
* Add ``Repository.merge_upstream`` method (`#3175 <https://github.com/PyGithub/PyGithub/pull/3175>`_) (`2f95352e <https://github.com/PyGithub/PyGithub/commit/2f95352e>`_)
* Support updating pull request draft status (`#3104 <https://github.com/PyGithub/PyGithub/pull/3104>`_) (`5ec7b775 <https://github.com/PyGithub/PyGithub/commit/5ec7b775>`_)
* Add transfer ownership method to Repository (`#3091 <https://github.com/PyGithub/PyGithub/pull/3091>`_) (`b3ccd105 <https://github.com/PyGithub/PyGithub/commit/b3ccd105>`_)
* Add enable and disable a Workflow (`#3088 <https://github.com/PyGithub/PyGithub/pull/3088>`_) (`7f7d2282 <https://github.com/PyGithub/PyGithub/commit/7f7d2282>`_)
* Add support for managing Code Security Configurations (`#3095 <https://github.com/PyGithub/PyGithub/pull/3095>`_) (`ee5d1da3 <https://github.com/PyGithub/PyGithub/commit/ee5d1da3>`_)
* Allow for private_key / sign function in AppAuth (`#3065 <https://github.com/PyGithub/PyGithub/pull/3065>`_) (`36697b22 <https://github.com/PyGithub/PyGithub/commit/36697b22>`_)
* Add ``GitCommitVerification`` class (`#3028 <https://github.com/PyGithub/PyGithub/pull/3028>`_) (`822e6d71 <https://github.com/PyGithub/PyGithub/commit/822e6d71>`_)

Improvements
^^^^^^^^^^^^
* Update RateLimit object with all the new categories GitHub added. (`#3096 <https://github.com/PyGithub/PyGithub/pull/3096>`_) (`152429d9 <https://github.com/PyGithub/PyGithub/commit/152429d9>`_)
* Add support for make-latest to create_git_release and create_git_tag_and_release (`#3067 <https://github.com/PyGithub/PyGithub/pull/3067>`_) (`8ed5635f <https://github.com/PyGithub/PyGithub/commit/8ed5635f>`_)
* Add branch protection support for ``required_status_checks.checks`` object (`#2884 <https://github.com/PyGithub/PyGithub/pull/2884>`_) (`764540d3 <https://github.com/PyGithub/PyGithub/commit/764540d3>`_)
* Use id and tree_id from simple-commit to populate GitCommit.sha and GitCommit.tree (`#3167 <https://github.com/PyGithub/PyGithub/pull/3167>`_) (`04887640 <https://github.com/PyGithub/PyGithub/commit/04887640>`_)
* Use message of response in GithubException (`#3185 <https://github.com/PyGithub/PyGithub/pull/3185>`_) (`bd35f7dd <https://github.com/PyGithub/PyGithub/commit/bd35f7dd>`_)
* Sync Advisory classes with API spec (`#3193 <https://github.com/PyGithub/PyGithub/pull/3193>`_) (`d9d93c03 <https://github.com/PyGithub/PyGithub/commit/d9d93c03>`_)
* Sync Branch class with API spec (`#3109 <https://github.com/PyGithub/PyGithub/pull/3109>`_) (`5570eba1 <https://github.com/PyGithub/PyGithub/commit/5570eba1>`_)
* Sync BranchProtection class with API spec (`#3110 <https://github.com/PyGithub/PyGithub/pull/3110>`_) (`936b3ef5 <https://github.com/PyGithub/PyGithub/commit/936b3ef5>`_)
* Sync CheckRunAnnotation class with API spec (`#3112 <https://github.com/PyGithub/PyGithub/pull/3112>`_) (`29eb0f58 <https://github.com/PyGithub/PyGithub/commit/29eb0f58>`_)
* Sync CheckRun class with API spec (`#3111 <https://github.com/PyGithub/PyGithub/pull/3111>`_) (`3837c7df <https://github.com/PyGithub/PyGithub/commit/3837c7df>`_)
* Sync CheckSuite class with API spec (`#3113 <https://github.com/PyGithub/PyGithub/pull/3113>`_) (`fa75d667 <https://github.com/PyGithub/PyGithub/commit/fa75d667>`_)
* Sync Commit class with API spec (`#3116 <https://github.com/PyGithub/PyGithub/pull/3116>`_) (`b2748ed9 <https://github.com/PyGithub/PyGithub/commit/b2748ed9>`_)
* Sync CommitComment class with API spec (`#3117 <https://github.com/PyGithub/PyGithub/pull/3117>`_) (`51945360 <https://github.com/PyGithub/PyGithub/commit/51945360>`_)
* Sync CommitStatus class with API spec (`#3118 <https://github.com/PyGithub/PyGithub/pull/3118>`_) (`9a455056 <https://github.com/PyGithub/PyGithub/commit/9a455056>`_)
* Sync ContentFile class with API spec (`#3119 <https://github.com/PyGithub/PyGithub/pull/3119>`_) (`a9aa872f <https://github.com/PyGithub/PyGithub/commit/a9aa872f>`_)
* Sync DependabotAlert class with API spec (`#3120 <https://github.com/PyGithub/PyGithub/pull/3120>`_) (`79b4fc7c <https://github.com/PyGithub/PyGithub/commit/79b4fc7c>`_)
* Sync Deployment class with API spec (`#3121 <https://github.com/PyGithub/PyGithub/pull/3121>`_) (`c2d3b5e2 <https://github.com/PyGithub/PyGithub/commit/c2d3b5e2>`_)
* Sync DeploymentStatus class with API spec (`#3122 <https://github.com/PyGithub/PyGithub/pull/3122>`_) (`b3a06f07 <https://github.com/PyGithub/PyGithub/commit/b3a06f07>`_)
* Sync Gist class with API spec (`#3123 <https://github.com/PyGithub/PyGithub/pull/3123>`_) (`6764017b <https://github.com/PyGithub/PyGithub/commit/6764017b>`_)
* Sync GistComment class with API spec (`#3124 <https://github.com/PyGithub/PyGithub/pull/3124>`_) (`eb6019a4 <https://github.com/PyGithub/PyGithub/commit/eb6019a4>`_)
* Sync GitBlob class with API spec (`#3125 <https://github.com/PyGithub/PyGithub/pull/3125>`_) (`876ff10d <https://github.com/PyGithub/PyGithub/commit/876ff10d>`_)
* Sync GitCommit class with API spec (`#3126 <https://github.com/PyGithub/PyGithub/pull/3126>`_) (`6276e20f <https://github.com/PyGithub/PyGithub/commit/6276e20f>`_)
* Sync GithubApp class with API spec (`#3127 <https://github.com/PyGithub/PyGithub/pull/3127>`_) (`5327617e <https://github.com/PyGithub/PyGithub/commit/5327617e>`_)
* Sync GitRef class with API spec (`#3128 <https://github.com/PyGithub/PyGithub/pull/3128>`_) (`a69f1d6f <https://github.com/PyGithub/PyGithub/commit/a69f1d6f>`_)
* Sync GitReleaseAsset class with API spec (`#3130 <https://github.com/PyGithub/PyGithub/pull/3130>`_) (`c5ab18f1 <https://github.com/PyGithub/PyGithub/commit/c5ab18f1>`_)
* Sync GitRelease class with API spec (`#3129 <https://github.com/PyGithub/PyGithub/pull/3129>`_) (`ebf3fe8e <https://github.com/PyGithub/PyGithub/commit/ebf3fe8e>`_)
* Sync GitTag class with API spec (`#3131 <https://github.com/PyGithub/PyGithub/pull/3131>`_) (`58f26d85 <https://github.com/PyGithub/PyGithub/commit/58f26d85>`_)
* Sync GitTree class with API spec (`#3132 <https://github.com/PyGithub/PyGithub/pull/3132>`_) (`a38cb5ad <https://github.com/PyGithub/PyGithub/commit/a38cb5ad>`_)
* Sync Hook class with API spec (`#3133 <https://github.com/PyGithub/PyGithub/pull/3133>`_) (`2e477f8c <https://github.com/PyGithub/PyGithub/commit/2e477f8c>`_)
* Sync HookDelivery class with API spec (`#3134 <https://github.com/PyGithub/PyGithub/pull/3134>`_) (`15d57595 <https://github.com/PyGithub/PyGithub/commit/15d57595>`_)
* Sync InstallationAuthorization class with API spec (`#3136 <https://github.com/PyGithub/PyGithub/pull/3136>`_) (`649de20b <https://github.com/PyGithub/PyGithub/commit/649de20b>`_)
* Sync Installation class with API spec (`#3135 <https://github.com/PyGithub/PyGithub/pull/3135>`_) (`3e4185d8 <https://github.com/PyGithub/PyGithub/commit/3e4185d8>`_)
* Sync Invitation class with API spec (`#3139 <https://github.com/PyGithub/PyGithub/pull/3139>`_) (`0df2e394 <https://github.com/PyGithub/PyGithub/commit/0df2e394>`_)
* Sync Issue class with API spec (`#3140 <https://github.com/PyGithub/PyGithub/pull/3140>`_) (`769c6967 <https://github.com/PyGithub/PyGithub/commit/769c6967>`_)
* Sync IssueComment class with API spec (`#3141 <https://github.com/PyGithub/PyGithub/pull/3141>`_) (`bb3353b4 <https://github.com/PyGithub/PyGithub/commit/bb3353b4>`_)
* Sync IssueEvent class with API spec (`#3142 <https://github.com/PyGithub/PyGithub/pull/3142>`_) (`be44bb58 <https://github.com/PyGithub/PyGithub/commit/be44bb58>`_)
* Sync IssuePullRequest class with API spec (`#3143 <https://github.com/PyGithub/PyGithub/pull/3143>`_) (`1836b073 <https://github.com/PyGithub/PyGithub/commit/1836b073>`_)
* Sync Label class with API spec (`#3144 <https://github.com/PyGithub/PyGithub/pull/3144>`_) (`4535b9e1 <https://github.com/PyGithub/PyGithub/commit/4535b9e1>`_)
* Sync License class with API spec (`#3145 <https://github.com/PyGithub/PyGithub/pull/3145>`_) (`dda13366 <https://github.com/PyGithub/PyGithub/commit/dda13366>`_)
* Sync Membership class with API spec (`#3146 <https://github.com/PyGithub/PyGithub/pull/3146>`_) (`bc643cc8 <https://github.com/PyGithub/PyGithub/commit/bc643cc8>`_)
* Sync Migration class with API spec (`#3147 <https://github.com/PyGithub/PyGithub/pull/3147>`_) (`dabc1fb2 <https://github.com/PyGithub/PyGithub/commit/dabc1fb2>`_)
* Sync Milestone class with API spec (`#3148 <https://github.com/PyGithub/PyGithub/pull/3148>`_) (`12aee396 <https://github.com/PyGithub/PyGithub/commit/12aee396>`_)
* Sync NamedUser class with API spec (`#3149 <https://github.com/PyGithub/PyGithub/pull/3149>`_) (`b481fab0 <https://github.com/PyGithub/PyGithub/commit/b481fab0>`_)
* Sync Organization class with API spec (`#3150 <https://github.com/PyGithub/PyGithub/pull/3150>`_) (`5b36bc40 <https://github.com/PyGithub/PyGithub/commit/5b36bc40>`_)
* Sync OrganizationCustomProperty class with API spec (`#3151 <https://github.com/PyGithub/PyGithub/pull/3151>`_) (`519b61b0 <https://github.com/PyGithub/PyGithub/commit/519b61b0>`_)
* Sync Project class with API spec (`#3194 <https://github.com/PyGithub/PyGithub/pull/3194>`_) (`6ed83964 <https://github.com/PyGithub/PyGithub/commit/6ed83964>`_)
* Sync PublicKey class with API spec (`#3152 <https://github.com/PyGithub/PyGithub/pull/3152>`_) (`26c284bc <https://github.com/PyGithub/PyGithub/commit/26c284bc>`_)
* Sync PullRequest class with API spec (`#3153 <https://github.com/PyGithub/PyGithub/pull/3153>`_) (`563bdbb4 <https://github.com/PyGithub/PyGithub/commit/563bdbb4>`_)
* Sync PullRequestComment class with API spec (`#3154 <https://github.com/PyGithub/PyGithub/pull/3154>`_) (`e262c2ee <https://github.com/PyGithub/PyGithub/commit/e262c2ee>`_)
* Sync RateLimit class with API spec (`#3155 <https://github.com/PyGithub/PyGithub/pull/3155>`_) (`db1e8797 <https://github.com/PyGithub/PyGithub/commit/db1e8797>`_)
* Sync Repository class with API spec (`#3156 <https://github.com/PyGithub/PyGithub/pull/3156>`_) (`f03b3163 <https://github.com/PyGithub/PyGithub/commit/f03b3163>`_)
* Sync RepositoryKey class with API spec (`#3157 <https://github.com/PyGithub/PyGithub/pull/3157>`_) (`365f9899 <https://github.com/PyGithub/PyGithub/commit/365f9899>`_)
* Sync SecurityAndAnalysis class with API spec (`#3158 <https://github.com/PyGithub/PyGithub/pull/3158>`_) (`65546abd <https://github.com/PyGithub/PyGithub/commit/65546abd>`_)
* Sync SelfHostedActionsRunner class with API spec (`#3159 <https://github.com/PyGithub/PyGithub/pull/3159>`_) (`ea4a8d1d <https://github.com/PyGithub/PyGithub/commit/ea4a8d1d>`_)
* Sync SourceImport class with API spec (`#3160 <https://github.com/PyGithub/PyGithub/pull/3160>`_) (`4d989733 <https://github.com/PyGithub/PyGithub/commit/4d989733>`_)
* Sync Tag class with API spec (`#3161 <https://github.com/PyGithub/PyGithub/pull/3161>`_) (`a0a25bce <https://github.com/PyGithub/PyGithub/commit/a0a25bce>`_)
* Sync Team class with API spec (`#3162 <https://github.com/PyGithub/PyGithub/pull/3162>`_) (`a1e68550 <https://github.com/PyGithub/PyGithub/commit/a1e68550>`_)
* Sync Topic class with API spec (`#3163 <https://github.com/PyGithub/PyGithub/pull/3163>`_) (`67eced78 <https://github.com/PyGithub/PyGithub/commit/67eced78>`_)
* Sync UserKey class with API spec (`#3164 <https://github.com/PyGithub/PyGithub/pull/3164>`_) (`9d04305a <https://github.com/PyGithub/PyGithub/commit/9d04305a>`_)
* Sync Workflow class with API spec (`#3165 <https://github.com/PyGithub/PyGithub/pull/3165>`_) (`b656a311 <https://github.com/PyGithub/PyGithub/commit/b656a311>`_)
* Sync WorkflowRun class with API spec (`#3166 <https://github.com/PyGithub/PyGithub/pull/3166>`_) (`468fa1b3 <https://github.com/PyGithub/PyGithub/commit/468fa1b3>`_)

Bug Fixes
^^^^^^^^^
* Patch httpretty socket for latest urllib3 release (`#3102 <https://github.com/PyGithub/PyGithub/pull/3102>`_) (`81f8f05b <https://github.com/PyGithub/PyGithub/commit/81f8f05b>`_)
* Fix API break when contents not found (`#3181 <https://github.com/PyGithub/PyGithub/pull/3181>`_) (`d90323fa <https://github.com/PyGithub/PyGithub/commit/d90323fa>`_)
* Change ``start_side`` argument of ``PullRequest.create_review_comment`` from ``int`` to ``str`` (`#3170 <https://github.com/PyGithub/PyGithub/pull/3170>`_) (`f814de7d <https://github.com/PyGithub/PyGithub/commit/f814de7d>`_)
* Create Review Request - transform string params to a list (`#3099 <https://github.com/PyGithub/PyGithub/pull/3099>`_) (`8aef11c0 <https://github.com/PyGithub/PyGithub/commit/8aef11c0>`_)
* Fix ``Repository.get_contents`` redirection (`#3183 <https://github.com/PyGithub/PyGithub/pull/3183>`_) (`193f6991 <https://github.com/PyGithub/PyGithub/commit/193f6991>`_)

Others
^^^^^^
* Fix typos (`#3086 <https://github.com/PyGithub/PyGithub/pull/3086>`_) (`a50ae51b <https://github.com/PyGithub/PyGithub/commit/a50ae51b>`_)
* Make ``conclusion`` nullable in ``WorkflowJob.py`` (`#3171 <https://github.com/PyGithub/PyGithub/pull/3171>`_) (`8d8eb06d <https://github.com/PyGithub/PyGithub/commit/8d8eb06d>`_)
* Rename ``Github.get_organization`` argument ``login`` to ``org`` (`#3187 <https://github.com/PyGithub/PyGithub/pull/3187>`_) (`9e3cf209 <https://github.com/PyGithub/PyGithub/commit/9e3cf209>`_)
* Make ``NotSet`` an ``Attribute[Any]`` (`#3057 <https://github.com/PyGithub/PyGithub/pull/3057>`_)

Maintenance
^^^^^^^^^^^
* Sort attributes and properties in GitHub classes (`#3105 <https://github.com/PyGithub/PyGithub/pull/3105>`_) (`f3986b57 <https://github.com/PyGithub/PyGithub/commit/f3986b57>`_)
* Preparations for maintaining Github classes by code (`#3106 <https://github.com/PyGithub/PyGithub/pull/3106>`_) (`842a1b02 <https://github.com/PyGithub/PyGithub/commit/842a1b02>`_)
* Annotate Github classes with API schemas (`#3107 <https://github.com/PyGithub/PyGithub/pull/3107>`_) (`d092f478 <https://github.com/PyGithub/PyGithub/commit/d092f478>`_)
* Make Pickle test use recorded data (`#3137 <https://github.com/PyGithub/PyGithub/pull/3137>`_) (`1990eb92 <https://github.com/PyGithub/PyGithub/commit/1990eb92>`_)
* Add tests for file and stream downloads (`#3182 <https://github.com/PyGithub/PyGithub/pull/3182>`_) (`d483fe25 <https://github.com/PyGithub/PyGithub/commit/d483fe25>`_)
* Use ``responses`` instead of ``httpretty`` in tests (`#3087 <https://github.com/PyGithub/PyGithub/pull/3087>`_) (`9b293d44 <https://github.com/PyGithub/PyGithub/commit/9b293d44>`_)
* [CI] Publish test results (`#3195 <https://github.com/PyGithub/PyGithub/pull/3195>`_)
* Link Commit to correct upstream documentation (`#2936 <https://github.com/PyGithub/PyGithub/pull/2936>`_) (`4d307a7c <https://github.com/PyGithub/PyGithub/commit/4d307a7c>`_)
* Replace release drafter with Github release note generation (`#3196 <https://github.com/PyGithub/PyGithub/pull/3196>`_) (`6f9a2983 <https://github.com/PyGithub/PyGithub/commit/6f9a2983>`_)
* Add maintenance label to release.yml (`#3197 <https://github.com/PyGithub/PyGithub/pull/3197>`_) (`cab8d078 <https://github.com/PyGithub/PyGithub/commit/cab8d078>`_)

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

* Rework GraphQL mutations (`#3046 <https://github.com/PyGithub/PyGithub/pull/3046>`_) (`27222251 <https://github.com/PyGithub/PyGithub/commit/27222251>`_)
* Make pagination work with GraphQL response data (`#3047 <https://github.com/PyGithub/PyGithub/pull/3047>`_) (`cd30e379 <https://github.com/PyGithub/PyGithub/commit/cd30e379>`_)
* Add `RepositoryDiscussion` powered by GraphQL API (`#3048 <https://github.com/PyGithub/PyGithub/pull/3048>`_) (`29359f3c <https://github.com/PyGithub/PyGithub/commit/29359f3c>`_)
* Add `Repository.get_discussion()` to get a single Discussion (`#3072 <https://github.com/PyGithub/PyGithub/pull/3072>`_) (`44120b1e <https://github.com/PyGithub/PyGithub/commit/44120b1e>`_)

Improvements
^^^^^^^^^^^^

* Adds List organization memberships for the authenticated user (`#3040 <https://github.com/PyGithub/PyGithub/pull/3040>`_) (`cf443955 <https://github.com/PyGithub/PyGithub/commit/cf443955>`_)
* Add `actor` property to WorkflowRun (`#2764 <https://github.com/PyGithub/PyGithub/pull/2764>`_) (`612ba68e <https://github.com/PyGithub/PyGithub/commit/612ba68e>`_)
* Make requester a public attribute (`#3056 <https://github.com/PyGithub/PyGithub/pull/3056>`_) (`c44ec523 <https://github.com/PyGithub/PyGithub/commit/c44ec523>`_)

Bug Fixes
^^^^^^^^^

* Fix requesting urls containing parameters with parameters dict (`#2929 <https://github.com/PyGithub/PyGithub/pull/2929>`_) (`e1d67ada <https://github.com/PyGithub/PyGithub/commit/e1d67ada>`_)
* PullRequest.delete_branch: fix the remaining pull requests check (`#3063 <https://github.com/PyGithub/PyGithub/pull/3063>`_) (`72fa6278 <https://github.com/PyGithub/PyGithub/commit/72fa6278>`_)

Maintenance
^^^^^^^^^^^

* Remove stale bot (`510c1402 <https://github.com/PyGithub/PyGithub/commit/510c1402>`_)
* Upgrade Github actions (`#3075 <https://github.com/PyGithub/PyGithub/pull/3075>`_) (`323e2828 <https://github.com/PyGithub/PyGithub/commit/323e2828>`_)
* Add top issues dashboard action (`#3049 <https://github.com/PyGithub/PyGithub/pull/3049>`_) (`c91f26a7 <https://github.com/PyGithub/PyGithub/commit/c91f26a7>`_)
* Make tests pass some more years (`#3045 <https://github.com/PyGithub/PyGithub/pull/3045>`_) (`352c55aa <https://github.com/PyGithub/PyGithub/commit/352c55aa>`_)
* Run top issues workflow only in PyGithub repo (`0d395d4e <https://github.com/PyGithub/PyGithub/commit/0d395d4e>`_)
* Replace pre-commit Github action in order to pin pre-commit version (`#3059 <https://github.com/PyGithub/PyGithub/pull/3059>`_) (`1a05b43d <https://github.com/PyGithub/PyGithub/commit/1a05b43d>`_)

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

* Allow custom authentication (`#2987 <https://github.com/PyGithub/PyGithub/pull/2987>`_) (`32b826fd <https://github.com/PyGithub/PyGithub/commit/32b826fd>`_)

Improvements
^^^^^^^^^^^^

* Add `has_discussions` to `AuthenticatedUser` and `Repository` classes (`#3020 <https://github.com/PyGithub/PyGithub/pull/3020>`_) (`75224167 <https://github.com/PyGithub/PyGithub/commit/75224167>`_)
* Update more `SecurityAndAnalysis` attributes (`#3025 <https://github.com/PyGithub/PyGithub/pull/3025>`_) (`fa168279 <https://github.com/PyGithub/PyGithub/commit/fa168279>`_)
* Implement support for re-running only failed workflow jobs. (`#2983 <https://github.com/PyGithub/PyGithub/pull/2983>`_) (`23e87563 <https://github.com/PyGithub/PyGithub/commit/23e87563>`_)
* Add possibility to mark a thread/notification as done (`#2985 <https://github.com/PyGithub/PyGithub/pull/2985>`_) (`5ba24379 <https://github.com/PyGithub/PyGithub/commit/5ba24379>`_)
* Add "pull_request_review_id" to PullRequestComment object (`#3000 <https://github.com/PyGithub/PyGithub/pull/3000>`_) (`6a59cf82 <https://github.com/PyGithub/PyGithub/commit/6a59cf82>`_)
* Add minimize and unminimize functions for IssueComment class (`#3005 <https://github.com/PyGithub/PyGithub/pull/3005>`_) (`09c4f58e <https://github.com/PyGithub/PyGithub/commit/09c4f58e>`_)
* Support Organization/Repository custom properties (`#2968 <https://github.com/PyGithub/PyGithub/pull/2968>`_) (`c5e6b702 <https://github.com/PyGithub/PyGithub/commit/c5e6b702>`_)
* Add `dict` type to `add_attribute` script (`#2977 <https://github.com/PyGithub/PyGithub/pull/2977>`_) (`2a04f9cc <https://github.com/PyGithub/PyGithub/commit/2a04f9cc>`_)
* Allow for deleting and restoring branch associated with PR (`#1784 <https://github.com/PyGithub/PyGithub/pull/1784>`_) (`4ba1e412 <https://github.com/PyGithub/PyGithub/commit/4ba1e412>`_)
* Add "archived_at" to Organization object. (`#2974 <https://github.com/PyGithub/PyGithub/pull/2974>`_) (`cc766a6f <https://github.com/PyGithub/PyGithub/commit/cc766a6f>`_)
* Adds Security & Analysis To Repository (`#2960 <https://github.com/PyGithub/PyGithub/pull/2960>`_) (`f22af54d <https://github.com/PyGithub/PyGithub/commit/f22af54d>`_)
* Add added_by and last_used attributes to RepositoryKey (`#2952 <https://github.com/PyGithub/PyGithub/pull/2952>`_) (`5dffa64d <https://github.com/PyGithub/PyGithub/commit/5dffa64d>`_)
* Add `make_latest` to `GitRelease.update_release` (`#2888 <https://github.com/PyGithub/PyGithub/pull/2888>`_) (`60136105 <https://github.com/PyGithub/PyGithub/commit/60136105>`_)
* Make Commit.files return PaginatedList (`#2939 <https://github.com/PyGithub/PyGithub/pull/2939>`_) (`fa885f00 <https://github.com/PyGithub/PyGithub/commit/fa885f00>`_)

Bug Fixes
^^^^^^^^^

* Fix GraphQL Queries with Variables (`#3002 <https://github.com/PyGithub/PyGithub/pull/3002>`_) (`4324a3d9 <https://github.com/PyGithub/PyGithub/commit/4324a3d9>`_)

Maintenance
^^^^^^^^^^^

* Remove support for Python 3.7 (#2975, #3008) (d0e05072, 6d60b754)
* docs: add missing code-block (`#2982 <https://github.com/PyGithub/PyGithub/pull/2982>`_) (`c93e73e2 <https://github.com/PyGithub/PyGithub/commit/c93e73e2>`_)
* Update README.md (`#2961 <https://github.com/PyGithub/PyGithub/pull/2961>`_) (`5d9f90d2 <https://github.com/PyGithub/PyGithub/commit/5d9f90d2>`_)
* CI: Fix test success job (`#3010 <https://github.com/PyGithub/PyGithub/pull/3010>`_) (`61d37dce <https://github.com/PyGithub/PyGithub/commit/61d37dce>`_)

Version 2.3.0 (March 21, 2024)
------------------------------

New features
^^^^^^^^^^^^

* Support OAuth for enterprise (`#2780 <https://github.com/PyGithub/PyGithub/pull/2780>`_) (`e4106e00 <https://github.com/PyGithub/PyGithub/commit/e4106e00>`_)
* Support creation of Dependabot Organization and Repository Secrets (`#2874 <https://github.com/PyGithub/PyGithub/pull/2874>`_) (`0784f835 <https://github.com/PyGithub/PyGithub/commit/0784f835>`_)

Improvements
^^^^^^^^^^^^

* Create release with optional name and message when generate_release_notes is true (`#2868 <https://github.com/PyGithub/PyGithub/pull/2868>`_) (`d65fc30d <https://github.com/PyGithub/PyGithub/commit/d65fc30d>`_)
* Add missing attributes to WorkflowJob (`#2921 <https://github.com/PyGithub/PyGithub/pull/2921>`_) (`9e092458 <https://github.com/PyGithub/PyGithub/commit/9e092458>`_)
* Add `created` and `check_suite_id` filter for Repository WorkflowRuns (`#2891 <https://github.com/PyGithub/PyGithub/pull/2891>`_) (`c788985c <https://github.com/PyGithub/PyGithub/commit/c788985c>`_)
* Assert requester argument type in Auth (`#2912 <https://github.com/PyGithub/PyGithub/pull/2912>`_) (`0b8435fc <https://github.com/PyGithub/PyGithub/commit/0b8435fc>`_)

Bug Fixes
^^^^^^^^^

* Revert having allowed values for add_to_collaborators (`#2905 <https://github.com/PyGithub/PyGithub/pull/2905>`_) (`b542438e <https://github.com/PyGithub/PyGithub/commit/b542438e>`_)

Maintenance
^^^^^^^^^^^

* Fix imports in authentication docs (`#2923 <https://github.com/PyGithub/PyGithub/pull/2923>`_) (`e3d36535 <https://github.com/PyGithub/PyGithub/commit/e3d36535>`_)
* CI: add docformatter to precommit (`#2614 <https://github.com/PyGithub/PyGithub/pull/2614>`_) (`96ad19ae <https://github.com/PyGithub/PyGithub/commit/96ad19ae>`_)
* Add .swp files to gitignore (`#2903 <https://github.com/PyGithub/PyGithub/pull/2903>`_) (`af529abe <https://github.com/PyGithub/PyGithub/commit/af529abe>`_)
* Fix instructions building docs in CONTRIBUTING.md (`#2900 <https://github.com/PyGithub/PyGithub/pull/2900>`_) (`cd8e528d <https://github.com/PyGithub/PyGithub/commit/cd8e528d>`_)
* Explicitly name the modules built in pyproject.toml (`#2894 <https://github.com/PyGithub/PyGithub/pull/2894>`_) (`4d461734 <https://github.com/PyGithub/PyGithub/commit/4d461734>`_)

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

* Add parent_team_id, maintainers and notification_setting for creating and updating teams. (`#2863 <https://github.com/PyGithub/PyGithub/pull/2863>`_) (`49d07d16 <https://github.com/PyGithub/PyGithub/commit/49d07d16>`_)
* Add support for issue reactions summary (`#2866 <https://github.com/PyGithub/PyGithub/pull/2866>`_) (`cc4c5269 <https://github.com/PyGithub/PyGithub/commit/cc4c5269>`_)
* Support for DependabotAlert APIs (`#2879 <https://github.com/PyGithub/PyGithub/pull/2879>`_) (`14af7051 <https://github.com/PyGithub/PyGithub/commit/14af7051>`_)
* Derive GraphQL URL from base_url (`#2880 <https://github.com/PyGithub/PyGithub/pull/2880>`_) (`d0caa3c3 <https://github.com/PyGithub/PyGithub/commit/d0caa3c3>`_)
* Make ``Repository.compare().commits`` return paginated list (`#2882 <https://github.com/PyGithub/PyGithub/pull/2882>`_) (`2d284d1e <https://github.com/PyGithub/PyGithub/commit/2d284d1e>`_)
* Add missing branch protection fields (`#2873 <https://github.com/PyGithub/PyGithub/pull/2873>`_) (`e47c153b <https://github.com/PyGithub/PyGithub/commit/e47c153b>`_)
* Add ``include_all_branches`` to ``create_repo_from_template`` of ``AuthenticatedUser`` and ``Organization`` (`#2871 <https://github.com/PyGithub/PyGithub/pull/2871>`_) (`34c4642e <https://github.com/PyGithub/PyGithub/commit/34c4642e>`_)
* Add and update organisation dependabot secrets (`#2316 <https://github.com/PyGithub/PyGithub/pull/2316>`_) (`603896f4 <https://github.com/PyGithub/PyGithub/commit/603896f4>`_)
* Add missing params to ``Organization.create_repo`` (`#2700 <https://github.com/PyGithub/PyGithub/pull/2700>`_) (`9c61a2a4 <https://github.com/PyGithub/PyGithub/commit/9c61a2a4>`_)
* Update allowed values for ``Repository`` collaborator permissions (`#1996 <https://github.com/PyGithub/PyGithub/pull/1996>`_) (`b5b66da8 <https://github.com/PyGithub/PyGithub/commit/b5b66da8>`_)
* Support editing PullRequestReview (`#2851 <https://github.com/PyGithub/PyGithub/pull/2851>`_) (`b1c4c561 <https://github.com/PyGithub/PyGithub/commit/b1c4c561>`_)
* Update attributes after calling ``PullRequestReview.dismiss`` (`#2854 <https://github.com/PyGithub/PyGithub/pull/2854>`_) (`6f3d714c <https://github.com/PyGithub/PyGithub/commit/6f3d714c>`_)
* Add ``request_cve`` on ``RepositoryAdvisories`` (`#2855 <https://github.com/PyGithub/PyGithub/pull/2855>`_) (`41b617b7 <https://github.com/PyGithub/PyGithub/commit/41b617b7>`_)
* Filter collaborators of a repository by permissions (`#2792 <https://github.com/PyGithub/PyGithub/pull/2792>`_) (`702c127a <https://github.com/PyGithub/PyGithub/commit/702c127a>`_)
* Set pull request to auto merge via GraphQL API (`#2816 <https://github.com/PyGithub/PyGithub/pull/2816>`_) (`232df79a <https://github.com/PyGithub/PyGithub/commit/232df79a>`_)
* Support Environment Variables and Secrets (`#2848 <https://github.com/PyGithub/PyGithub/pull/2848>`_) (`7df97398 <https://github.com/PyGithub/PyGithub/commit/7df97398>`_)
* Update workflow.get_runs & pullrequest.add_to_assignees function signature (`#2799 <https://github.com/PyGithub/PyGithub/pull/2799>`_) (`26eedbb0 <https://github.com/PyGithub/PyGithub/commit/26eedbb0>`_)
* Add ``GithubObject.last_modified_datetime`` to have ``last_modified`` as a ``datetime`` (`#2772 <https://github.com/PyGithub/PyGithub/pull/2772>`_) (`e7ce8189 <https://github.com/PyGithub/PyGithub/commit/e7ce8189>`_)
* Add support for global advisories and unify some shared logic with repository advisories (`#2702 <https://github.com/PyGithub/PyGithub/pull/2702>`_) (`c8b4fcbe <https://github.com/PyGithub/PyGithub/commit/c8b4fcbe>`_)
* Add internal as valid Repository visibility value (`#2806 <https://github.com/PyGithub/PyGithub/pull/2806>`_) (`d4a5a40f <https://github.com/PyGithub/PyGithub/commit/d4a5a40f>`_)
* Add support for issue comments reactions summary (`#2813 <https://github.com/PyGithub/PyGithub/pull/2813>`_) (`67397491 <https://github.com/PyGithub/PyGithub/commit/67397491>`_)

Bug Fixes
^^^^^^^^^

* Add a bunch of missing urllib.parse.quote calls (`#1976 <https://github.com/PyGithub/PyGithub/pull/1976>`_) (`13194be2 <https://github.com/PyGithub/PyGithub/commit/13194be2>`_)
* Fix Variable and Secret URL (`#2835 <https://github.com/PyGithub/PyGithub/pull/2835>`_) (`aa763431 <https://github.com/PyGithub/PyGithub/commit/aa763431>`_)

Maintenance
^^^^^^^^^^^

* Update the class name for NetrcAuth in the examples (`#2860 <https://github.com/PyGithub/PyGithub/pull/2860>`_) (`2f44b2e8 <https://github.com/PyGithub/PyGithub/commit/2f44b2e8>`_)
* Move build to PEP517 (`#2800 <https://github.com/PyGithub/PyGithub/pull/2800>`_) (`c589bf9e <https://github.com/PyGithub/PyGithub/commit/c589bf9e>`_)
* Use new type assert functions in ``Repository`` (`#2798 <https://github.com/PyGithub/PyGithub/pull/2798>`_) (`2783e671 <https://github.com/PyGithub/PyGithub/commit/2783e671>`_)
* PyTest: Move config to pyproject.toml (`#2859 <https://github.com/PyGithub/PyGithub/pull/2859>`_) (`61fb728b <https://github.com/PyGithub/PyGithub/commit/61fb728b>`_)
* codespell: ignore-words-list (`#2858 <https://github.com/PyGithub/PyGithub/pull/2858>`_) (`dcf6d8a1 <https://github.com/PyGithub/PyGithub/commit/dcf6d8a1>`_)
* Improve fix-headers.py script (`#2728 <https://github.com/PyGithub/PyGithub/pull/2728>`_) (`a48c37fa <https://github.com/PyGithub/PyGithub/commit/a48c37fa>`_)
* Remove dependency on python-dateutil (`#2804 <https://github.com/PyGithub/PyGithub/pull/2804>`_) (`ab131a2f <https://github.com/PyGithub/PyGithub/commit/ab131a2f>`_)
* CI: update precommit & apply (`#2600 <https://github.com/PyGithub/PyGithub/pull/2600>`_) (`d92cfba2 <https://github.com/PyGithub/PyGithub/commit/d92cfba2>`_)
* Fix parameter order according to Version 2.1.0 (`#2786 <https://github.com/PyGithub/PyGithub/pull/2786>`_) (`dc37d5c1 <https://github.com/PyGithub/PyGithub/commit/dc37d5c1>`_)
* Add missing GitHub classes to docs (`#2783 <https://github.com/PyGithub/PyGithub/pull/2783>`_) (`9af9b6e5 <https://github.com/PyGithub/PyGithub/commit/9af9b6e5>`_)
* Fix mypy error with urllib3>=2.0.0a1 by ignoring (`#2779 <https://github.com/PyGithub/PyGithub/pull/2779>`_) (`64b1cdea <https://github.com/PyGithub/PyGithub/commit/64b1cdea>`_)

Version 2.1.1 (September 29, 2023)
-----------------------------------

Bug Fixes
^^^^^^^^^

* Require urllib 1.26.0 or greater (`#2774 <https://github.com/PyGithub/PyGithub/pull/2774>`_) (`001c0852 <https://github.com/PyGithub/PyGithub/commit/001c0852>`_)

Maintenance
^^^^^^^^^^^

* Fix pypi-release workflow, allow for manual run (`#2771 <https://github.com/PyGithub/PyGithub/pull/2771>`_) (`035c88f1 <https://github.com/PyGithub/PyGithub/commit/035c88f1>`_)

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

* Throttle requests to mitigate RateLimitExceededExceptions (`#2145 <https://github.com/PyGithub/PyGithub/pull/2145>`_) (`99155806 <https://github.com/PyGithub/PyGithub/commit/99155806>`_)
* Retry retryable 403 (rate limit) (`#2387 <https://github.com/PyGithub/PyGithub/pull/2387>`_) (`0bb72ca0 <https://github.com/PyGithub/PyGithub/commit/0bb72ca0>`_)
* Close connections after use (`#2724 <https://github.com/PyGithub/PyGithub/pull/2724>`_) (`73236e23 <https://github.com/PyGithub/PyGithub/commit/73236e23>`_)

Improvements
^^^^^^^^^^^^

* Make datetime objects timezone-aware (`#2565 <https://github.com/PyGithub/PyGithub/pull/2565>`_) (`0177f7c5 <https://github.com/PyGithub/PyGithub/commit/0177f7c5>`_)
* Make ``Branch.edit_*`` functions return objects (`#2748 <https://github.com/PyGithub/PyGithub/pull/2748>`_) (`8dee53a8 <https://github.com/PyGithub/PyGithub/commit/8dee53a8>`_)
* Add ``license`` attribute to ``Repository`` (`#2721 <https://github.com/PyGithub/PyGithub/pull/2721>`_) (`26d353e7 <https://github.com/PyGithub/PyGithub/commit/26d353e7>`_)
* Add missing attributes to ``Repository``  (`#2742 <https://github.com/PyGithub/PyGithub/pull/2742>`_) (`65cfeb1b <https://github.com/PyGithub/PyGithub/commit/65cfeb1b>`_)
* Add ``is_alphanumeric`` attribute to ``Autolink`` and ``Repository.create_autolink`` (`#2630 <https://github.com/PyGithub/PyGithub/pull/2630>`_) (`b6a28a26 <https://github.com/PyGithub/PyGithub/commit/b6a28a26>`_)
* Suppress ``requests`` fallback to netrc, provide ``github.Auth.NetrcAuth`` (`#2739 <https://github.com/PyGithub/PyGithub/pull/2739>`_) (`ac36f6a9 <https://github.com/PyGithub/PyGithub/commit/ac36f6a9>`_)
* Pass Requester arguments to ``AppInstallationAuth.__integration`` (`#2695 <https://github.com/PyGithub/PyGithub/pull/2695>`_) (`8bf542ae <https://github.com/PyGithub/PyGithub/commit/8bf542ae>`_)
* Adding feature for enterprise consumed license (`#2626 <https://github.com/PyGithub/PyGithub/pull/2626>`_) (`a7bfdf2d <https://github.com/PyGithub/PyGithub/commit/a7bfdf2d>`_)
* Search Workflows by Name (`#2711 <https://github.com/PyGithub/PyGithub/pull/2711>`_) (`eadc241e <https://github.com/PyGithub/PyGithub/commit/eadc241e>`_)
* Add ``Secret`` and ``Variable`` classes (`#2623 <https://github.com/PyGithub/PyGithub/pull/2623>`_) (`bcca758d <https://github.com/PyGithub/PyGithub/commit/bcca758d>`_)
* Add Autolink API link (`#2632 <https://github.com/PyGithub/PyGithub/pull/2632>`_) (`aedfa0b9 <https://github.com/PyGithub/PyGithub/commit/aedfa0b9>`_)
* Add ``required_linear_history`` attribute to ``BranchProtection`` (`#2643 <https://github.com/PyGithub/PyGithub/pull/2643>`_) (`7a80fad9 <https://github.com/PyGithub/PyGithub/commit/7a80fad9>`_)
* Add retry issue to ``GithubException``, don't log it (`#2611 <https://github.com/PyGithub/PyGithub/pull/2611>`_) (`de80ff4b <https://github.com/PyGithub/PyGithub/commit/de80ff4b>`_)
* Add ``message`` property to ``GithubException`` (`#2591 <https://github.com/PyGithub/PyGithub/pull/2591>`_) (`f087cad3 <https://github.com/PyGithub/PyGithub/commit/f087cad3>`_)
* Add support for repo and org level actions variables (`#2580 <https://github.com/PyGithub/PyGithub/pull/2580>`_) (`91b3f40f <https://github.com/PyGithub/PyGithub/commit/91b3f40f>`_)
* Add missing arguments to ``Workflow.get_runs()`` (`#2346 <https://github.com/PyGithub/PyGithub/pull/2346>`_) (`766df993 <https://github.com/PyGithub/PyGithub/commit/766df993>`_)
* Add ``github.Rate.used`` field (`#2531 <https://github.com/PyGithub/PyGithub/pull/2531>`_) (`c4c2e527 <https://github.com/PyGithub/PyGithub/commit/c4c2e527>`_)

Bug Fixes
^^^^^^^^^

* Fix ``Branch.bypass_pull_request_allowances`` failing with "nil is not an object" (`#2535 <https://github.com/PyGithub/PyGithub/pull/2535>`_) (`c5542a6a <https://github.com/PyGithub/PyGithub/commit/c5542a6a>`_)
* Fix ``required_conversation_resolution`` assertion (`#2715 <https://github.com/PyGithub/PyGithub/pull/2715>`_) (`54f22267 <https://github.com/PyGithub/PyGithub/commit/54f22267>`_)
* Fix assertion creating pull request review comment (`#2641 <https://github.com/PyGithub/PyGithub/pull/2641>`_) (`2fa568b6 <https://github.com/PyGithub/PyGithub/commit/2fa568b6>`_)
* Safely coerce ``responseHeaders`` to ``int`` (`#2697 <https://github.com/PyGithub/PyGithub/pull/2697>`_) (`adbfce92 <https://github.com/PyGithub/PyGithub/commit/adbfce92>`_)
* Fix assertion for ``subject_type`` in creating pull request review comment (`#2642 <https://github.com/PyGithub/PyGithub/pull/2642>`_) (`4933459e <https://github.com/PyGithub/PyGithub/commit/4933459e>`_)
* Use timezone-aware reset datetime in ``GithubRetry.py`` (`#2610 <https://github.com/PyGithub/PyGithub/pull/2610>`_) (`950a6949 <https://github.com/PyGithub/PyGithub/commit/950a6949>`_)
* Fix ``Branch.bypass_pull_request_allowances`` failing with "nil is not an object" (`#2535 <https://github.com/PyGithub/PyGithub/pull/2535>`_) (`c5542a6a <https://github.com/PyGithub/PyGithub/commit/c5542a6a>`_)

Maintenance
^^^^^^^^^^^

* Epic mass-merge ``.pyi`` type stubs back to ``.py`` sources (`#2636 <https://github.com/PyGithub/PyGithub/pull/2636>`_)
* Move to main default branch (`#2566 <https://github.com/PyGithub/PyGithub/pull/2566>`_) (`e66c163a <https://github.com/PyGithub/PyGithub/commit/e66c163a>`_)
* Force Unix EOL (`#2573 <https://github.com/PyGithub/PyGithub/pull/2573>`_) (`094538e1 <https://github.com/PyGithub/PyGithub/commit/094538e1>`_)
* Close replay test data file silently when test is failing already (`#2747 <https://github.com/PyGithub/PyGithub/pull/2747>`_) (`6d871d56 <https://github.com/PyGithub/PyGithub/commit/6d871d56>`_)
* CI: Make CI support merge queue (`#2644 <https://github.com/PyGithub/PyGithub/pull/2644>`_) (`a91debf1 <https://github.com/PyGithub/PyGithub/commit/a91debf1>`_)
* CI: Run CI on release branches (`#2708 <https://github.com/PyGithub/PyGithub/pull/2708>`_) (`9a88b6b1 <https://github.com/PyGithub/PyGithub/commit/9a88b6b1>`_)
* CI: remove conflict label workflow (`#2669 <https://github.com/PyGithub/PyGithub/pull/2669>`_) (`95d8b83c <https://github.com/PyGithub/PyGithub/commit/95d8b83c>`_)
* Fix pip install command in README.md (`#2731 <https://github.com/PyGithub/PyGithub/pull/2731>`_) (`2cc1ba2c <https://github.com/PyGithub/PyGithub/commit/2cc1ba2c>`_)
* Update ``add_attribute.py`` to latest conding style (`#2631 <https://github.com/PyGithub/PyGithub/pull/2631>`_) (`e735972e <https://github.com/PyGithub/PyGithub/commit/e735972e>`_)
* CI: Improve ruff DX (`#2667 <https://github.com/PyGithub/PyGithub/pull/2667>`_) (`48d2009c <https://github.com/PyGithub/PyGithub/commit/48d2009c>`_)
* CI: Increase wait and retries of labels action (`#2670 <https://github.com/PyGithub/PyGithub/pull/2670>`_) (`ff0f31c2 <https://github.com/PyGithub/PyGithub/commit/ff0f31c2>`_)
* Replace ``flake8`` with ``ruff`` (`#2617 <https://github.com/PyGithub/PyGithub/pull/2617>`_) (`42c3b47c <https://github.com/PyGithub/PyGithub/commit/42c3b47c>`_)
* CI: update labels action name and version (`#2654 <https://github.com/PyGithub/PyGithub/pull/2654>`_) (`c5c83eb5 <https://github.com/PyGithub/PyGithub/commit/c5c83eb5>`_)
* CI: label PRs that have conflicts (`#2622 <https://github.com/PyGithub/PyGithub/pull/2622>`_) (`1d637e4b <https://github.com/PyGithub/PyGithub/commit/1d637e4b>`_)
* Unify requirements files location & source in setup.py (`#2598 <https://github.com/PyGithub/PyGithub/pull/2598>`_) (`2edc0f8f <https://github.com/PyGithub/PyGithub/commit/2edc0f8f>`_)
* Enable mypy ``disallow_untyped_defs`` (`#2609 <https://github.com/PyGithub/PyGithub/pull/2609>`_) (`294c0cc9 <https://github.com/PyGithub/PyGithub/commit/294c0cc9>`_)
* Enable mypy ``check_untyped_defs`` (`#2607 <https://github.com/PyGithub/PyGithub/pull/2607>`_) (`8816889a <https://github.com/PyGithub/PyGithub/commit/8816889a>`_)
* Set line length to 120 characters (`#2599 <https://github.com/PyGithub/PyGithub/pull/2599>`_) (`13e178a3 <https://github.com/PyGithub/PyGithub/commit/13e178a3>`_)
* CI: Build and check package before release (`#2593 <https://github.com/PyGithub/PyGithub/pull/2593>`_) (`3c880e76 <https://github.com/PyGithub/PyGithub/commit/3c880e76>`_)
* Use ``typing_extensions`` for ``TypedDict`` (`#2592 <https://github.com/PyGithub/PyGithub/pull/2592>`_) (`5fcb0c7d <https://github.com/PyGithub/PyGithub/commit/5fcb0c7d>`_)
* CI: Update action actions/setup-python (`#2382 <https://github.com/PyGithub/PyGithub/pull/2382>`_) (`2e5cd31e <https://github.com/PyGithub/PyGithub/commit/2e5cd31e>`_)
* Add more methods and attributes to Repository.pyi (`#2581 <https://github.com/PyGithub/PyGithub/pull/2581>`_) (`72840de4 <https://github.com/PyGithub/PyGithub/commit/72840de4>`_)
* CI: Make pytest color logs (`#2597 <https://github.com/PyGithub/PyGithub/pull/2597>`_) (`73241102 <https://github.com/PyGithub/PyGithub/commit/73241102>`_)
* precommit: move ``flake8`` as last (`#2595 <https://github.com/PyGithub/PyGithub/pull/2595>`_) (`11bb6bd7 <https://github.com/PyGithub/PyGithub/commit/11bb6bd7>`_)
* Test on Windows and macOS, don't fail fast (`#2590 <https://github.com/PyGithub/PyGithub/pull/2590>`_) (`5c600894 <https://github.com/PyGithub/PyGithub/commit/5c600894>`_)
* Remove symlinks from test data (`#2588 <https://github.com/PyGithub/PyGithub/pull/2588>`_) (`8d3b9057 <https://github.com/PyGithub/PyGithub/commit/8d3b9057>`_)

Version 1.59.1 (July 03, 2023)
-----------------------------------

Bug Fixes
^^^^^^^^^

* Safely coerce responseHeaders to int (`#2697 <https://github.com/PyGithub/PyGithub/pull/2697>`_) (`adbfce92 <https://github.com/PyGithub/PyGithub/commit/adbfce92>`_)

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

* Test and fix UTC issue with AppInstallationAuth (`#2561 <https://github.com/PyGithub/PyGithub/pull/2561>`_) (`ff3b80f8 <https://github.com/PyGithub/PyGithub/commit/ff3b80f8>`_)
* Make Requester.__createException robust against missing message and body (`#2159 <https://github.com/PyGithub/PyGithub/pull/2159>`_) (`7be3f763 <https://github.com/PyGithub/PyGithub/commit/7be3f763>`_)
* Fix auth issues with `Installation.get_repos` (`#2547 <https://github.com/PyGithub/PyGithub/pull/2547>`_) (`64075120 <https://github.com/PyGithub/PyGithub/commit/64075120>`_)
* Fix broken urls in docstrings (`#2393 <https://github.com/PyGithub/PyGithub/pull/2393>`_) (`f82ad61c <https://github.com/PyGithub/PyGithub/commit/f82ad61c>`_)
* Raise error on unsupported redirects, log supported redirects (`#2524 <https://github.com/PyGithub/PyGithub/pull/2524>`_) (`17cd0b79 <https://github.com/PyGithub/PyGithub/commit/17cd0b79>`_)
* Fix GithubIntegration that uses expiring jwt (`#2460 <https://github.com/PyGithub/PyGithub/pull/2460>`_) (`5011548c <https://github.com/PyGithub/PyGithub/commit/5011548c>`_)
* Add expiration argument back to GithubIntegration.create_jwt (`#2439 <https://github.com/PyGithub/PyGithub/pull/2439>`_) (`822fc05c <https://github.com/PyGithub/PyGithub/commit/822fc05c>`_)
* Add crypto extras to pyjwt, which pulls in cryptogaphy package (`#2443 <https://github.com/PyGithub/PyGithub/pull/2443>`_) (`554b2b28 <https://github.com/PyGithub/PyGithub/commit/554b2b28>`_)
* Remove RLock from Requester (`#2446 <https://github.com/PyGithub/PyGithub/pull/2446>`_) (`45f3d723 <https://github.com/PyGithub/PyGithub/commit/45f3d723>`_)
* Move CI to Python 3.11 release and 3.12 dev (`#2434 <https://github.com/PyGithub/PyGithub/pull/2434>`_) (`e414c322 <https://github.com/PyGithub/PyGithub/commit/e414c322>`_)
* Pass Requester base URL to integration (`#2420 <https://github.com/PyGithub/PyGithub/pull/2420>`_) (`bdceae2f <https://github.com/PyGithub/PyGithub/commit/bdceae2f>`_)

Improvements
^^^^^^^^^^^^

* Add Webhook Deliveries (`#2508 <https://github.com/PyGithub/PyGithub/pull/2508>`_) (`517ad336 <https://github.com/PyGithub/PyGithub/commit/517ad336>`_)
* Add support for workflow jobs and steps (`#1951 <https://github.com/PyGithub/PyGithub/pull/1951>`_) (`804c3107 <https://github.com/PyGithub/PyGithub/commit/804c3107>`_)
* Add support for get_app() with App authentication (`#2549 <https://github.com/PyGithub/PyGithub/pull/2549>`_) (`6d4b6d14 <https://github.com/PyGithub/PyGithub/commit/6d4b6d14>`_)
* Allow multiline comments in PullRequest (`#2540 <https://github.com/PyGithub/PyGithub/pull/2540>`_) (`6a21761e <https://github.com/PyGithub/PyGithub/commit/6a21761e>`_)
* Implement `AppUserAuth` for Github App user tokens (`#2546 <https://github.com/PyGithub/PyGithub/pull/2546>`_) (`f291a368 <https://github.com/PyGithub/PyGithub/commit/f291a368>`_)
* Add support for environments (`#2223 <https://github.com/PyGithub/PyGithub/pull/2223>`_) (`0384e2fd <https://github.com/PyGithub/PyGithub/commit/0384e2fd>`_)
* Add support for new RepositoryAdvisories API :tada: (`#2483 <https://github.com/PyGithub/PyGithub/pull/2483>`_) (`daf62bd4 <https://github.com/PyGithub/PyGithub/commit/daf62bd4>`_)
* Make `MainClass.get_app` return completed `GithubApp` when slug is given (`#2543 <https://github.com/PyGithub/PyGithub/pull/2543>`_) (`84912a67 <https://github.com/PyGithub/PyGithub/commit/84912a67>`_)
* Add authentication classes, move auth logic there (`#2528 <https://github.com/PyGithub/PyGithub/pull/2528>`_) (`fc2d0e15 <https://github.com/PyGithub/PyGithub/commit/fc2d0e15>`_)
* Add sort order and direction for getting comments (`#2544 <https://github.com/PyGithub/PyGithub/pull/2544>`_) (`a8e7c423 <https://github.com/PyGithub/PyGithub/commit/a8e7c423>`_)
* Add `name` filter to `Repository.get_artifacts()` (`#2459 <https://github.com/PyGithub/PyGithub/pull/2459>`_) (`9f52e948 <https://github.com/PyGithub/PyGithub/commit/9f52e948>`_)
* Add `name`, `display_title` and `path` attributes to `WorkflowRun` (`#2397 <https://github.com/PyGithub/PyGithub/pull/2397>`_) (`10816389 <https://github.com/PyGithub/PyGithub/commit/10816389>`_)
* Add new `create_fork` arguments (`#2493 <https://github.com/PyGithub/PyGithub/pull/2493>`_) (`b94a83cb <https://github.com/PyGithub/PyGithub/commit/b94a83cb>`_)
* add `ref` to Deployment (`#2489 <https://github.com/PyGithub/PyGithub/pull/2489>`_) (`e8075c41 <https://github.com/PyGithub/PyGithub/commit/e8075c41>`_)
* Add query `check_suite_id` integer to `Workflow.get_runs` (`#2466 <https://github.com/PyGithub/PyGithub/pull/2466>`_) (`a4854519 <https://github.com/PyGithub/PyGithub/commit/a4854519>`_)
* Add `generate_release_notes` parameter to `create_git_release` and `create_git_tag_and_release` (`#2417 <https://github.com/PyGithub/PyGithub/pull/2417>`_) (`49b3ae16 <https://github.com/PyGithub/PyGithub/commit/49b3ae16>`_)
* Add example for Pull Request comments to documentation (`#2390 <https://github.com/PyGithub/PyGithub/pull/2390>`_) (`c2f12bdc <https://github.com/PyGithub/PyGithub/commit/c2f12bdc>`_)
* Add allow_auto_merge support to Repository (`#2477 <https://github.com/PyGithub/PyGithub/pull/2477>`_) (`8c4b9465 <https://github.com/PyGithub/PyGithub/commit/8c4b9465>`_)
* Add `artifact_id` argument to `Repository.get_artifact()` (`#2458 <https://github.com/PyGithub/PyGithub/pull/2458>`_) (`4fa0a5f3 <https://github.com/PyGithub/PyGithub/commit/4fa0a5f3>`_)
* Add missing attributes to Branch (`#2512 <https://github.com/PyGithub/PyGithub/pull/2512>`_) (`e296dbdb <https://github.com/PyGithub/PyGithub/commit/e296dbdb>`_)
* Add allow_update_branch option to Organization (`#2465 <https://github.com/PyGithub/PyGithub/pull/2465>`_) (`bab4180f <https://github.com/PyGithub/PyGithub/commit/bab4180f>`_)
* Add support for Issue.state_reason #2370 (`#2392 <https://github.com/PyGithub/PyGithub/pull/2392>`_) (`5aa544a1 <https://github.com/PyGithub/PyGithub/commit/5aa544a1>`_)
* Add parameters to Repository.get_workflow_runs (`#2408 <https://github.com/PyGithub/PyGithub/pull/2408>`_) (`4198dbfb <https://github.com/PyGithub/PyGithub/commit/4198dbfb>`_)

Maintenance
^^^^^^^^^^^

* Add type stub for MainClass.get_project_column (`#2502 <https://github.com/PyGithub/PyGithub/pull/2502>`_) (`d514222c <https://github.com/PyGithub/PyGithub/commit/d514222c>`_)
* Sync GithubIntegration __init__ arguments with github.Github (`#2556 <https://github.com/PyGithub/PyGithub/pull/2556>`_) (`ea45237d <https://github.com/PyGithub/PyGithub/commit/ea45237d>`_)
* Update MAINTAINERS (`#2545 <https://github.com/PyGithub/PyGithub/pull/2545>`_) (`f4e9dcb3 <https://github.com/PyGithub/PyGithub/commit/f4e9dcb3>`_)
* Link to stable docs, update introduction in package used by pypi, move auth arg front (`#2557 <https://github.com/PyGithub/PyGithub/pull/2557>`_) (`006766f9 <https://github.com/PyGithub/PyGithub/commit/006766f9>`_)
* Merge PaginatedList.pyi back to source (`#2555 <https://github.com/PyGithub/PyGithub/pull/2555>`_) (`cb50dec5 <https://github.com/PyGithub/PyGithub/commit/cb50dec5>`_)
* Merge GithubObject.pyi/Requester.pyi stubs back to source (`#2463 <https://github.com/PyGithub/PyGithub/pull/2463>`_) (`b6258f4b <https://github.com/PyGithub/PyGithub/commit/b6258f4b>`_)
* [CI] Moving linting into separate workflow (`#2522 <https://github.com/PyGithub/PyGithub/pull/2522>`_) (`52fc1077 <https://github.com/PyGithub/PyGithub/commit/52fc1077>`_)
* Merging 1.58.x patch release notes into master (`#2525 <https://github.com/PyGithub/PyGithub/pull/2525>`_) (`217d4241 <https://github.com/PyGithub/PyGithub/commit/217d4241>`_)
* Merge AppAuthentication.pyi to source (`#2519 <https://github.com/PyGithub/PyGithub/pull/2519>`_) (`8e8cfb30 <https://github.com/PyGithub/PyGithub/commit/8e8cfb30>`_)
* Merge GithubException.pyi stubs back to source (`#2464 <https://github.com/PyGithub/PyGithub/pull/2464>`_) (`03a2f696 <https://github.com/PyGithub/PyGithub/commit/03a2f696>`_)
* Add missing fields from `GithubCredentials.py` to CONTRIBUTING.md (`#2482 <https://github.com/PyGithub/PyGithub/pull/2482>`_) (`297317ba <https://github.com/PyGithub/PyGithub/commit/297317ba>`_)
* Update docstring and typing for allow_forking and allow_update_branch (Repository) (`#2529 <https://github.com/PyGithub/PyGithub/pull/2529>`_) (`600217f0 <https://github.com/PyGithub/PyGithub/commit/600217f0>`_)
* Bump actions/checkout from 2 to 3.1.0 (`#2327 <https://github.com/PyGithub/PyGithub/pull/2327>`_) (`300c5015 <https://github.com/PyGithub/PyGithub/commit/300c5015>`_)
* RTD: install current project (`def5223c <https://github.com/PyGithub/PyGithub/commit/def5223c>`_)
* Add current dir sys.path as well (`9c96faa7 <https://github.com/PyGithub/PyGithub/commit/9c96faa7>`_)
* Use use_scm_version to get current version from git tag (`#2429 <https://github.com/PyGithub/PyGithub/pull/2429>`_) (`3ea91a3a <https://github.com/PyGithub/PyGithub/commit/3ea91a3a>`_)

Version 1.58.2 (May 09, 2023)
-----------------------------------

Bug Fixes
^^^^^^^^^

* Fix GithubIntegration that uses expiring jwt (`#2460 <https://github.com/PyGithub/PyGithub/pull/2460>`_) (`5011548c <https://github.com/PyGithub/PyGithub/commit/5011548c>`_)

Version 1.58.1 (March 18, 2023)
-----------------------------------

Bug Fixes
^^^^^^^^^

* Add expiration argument back to GithubIntegration.create_jwt (`#2439 <https://github.com/PyGithub/PyGithub/pull/2439>`_) (`822fc05c <https://github.com/PyGithub/PyGithub/commit/822fc05c>`_)
* Add crypto extras to pyjwt, which pulls in cryptogaphy package (`#2443 <https://github.com/PyGithub/PyGithub/pull/2443>`_) (`554b2b28 <https://github.com/PyGithub/PyGithub/commit/554b2b28>`_)
* Remove RLock from Requester (`#2446 <https://github.com/PyGithub/PyGithub/pull/2446>`_) (`45f3d723 <https://github.com/PyGithub/PyGithub/commit/45f3d723>`_)
* Move CI to Python 3.11 release and 3.12 dev (`#2434 <https://github.com/PyGithub/PyGithub/pull/2434>`_) (`e414c322 <https://github.com/PyGithub/PyGithub/commit/e414c322>`_)
* pass requester base URL to integration (`#2420 <https://github.com/PyGithub/PyGithub/pull/2420>`_) (`bdceae2f <https://github.com/PyGithub/PyGithub/commit/bdceae2f>`_)
* RTD: install current project (`def5223c <https://github.com/PyGithub/PyGithub/commit/def5223c>`_)
* Add current dir sys.path as well (`9c96faa7 <https://github.com/PyGithub/PyGithub/commit/9c96faa7>`_)
* Use use_scm_version to get current version from git tag (`#2429 <https://github.com/PyGithub/PyGithub/pull/2429>`_) (`3ea91a3a <https://github.com/PyGithub/PyGithub/commit/3ea91a3a>`_)

Version 1.58.0 (February 19, 2023)
-----------------------------------

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Add unarchiving support @Tsuesun (`#2391 <https://github.com/PyGithub/PyGithub/pull/2391>`_)
* Support full GitHub app authentication @dblanchette (`#1986 <https://github.com/PyGithub/PyGithub/pull/1986>`_)
* Continue the PR #1899 @Felixoid (`#2386 <https://github.com/PyGithub/PyGithub/pull/2386>`_)
* feat: add allow\_forking to Repository @IbrahimAH (`#2380 <https://github.com/PyGithub/PyGithub/pull/2380>`_)
* Add code scanning alerts @eric-nieuwland (`#2227 <https://github.com/PyGithub/PyGithub/pull/2227>`_)

Version 1.57 (November 05, 2022)
-----------------------------------

Breaking Changes
^^^^^^^^^^^^^^^^

* Add support for Python 3.11, drop support for Python 3.6 (`#2332 <https://github.com/PyGithub/PyGithub/pull/2332>`_) (`1e2f10dc <https://github.com/PyGithub/PyGithub/commit/1e2f10dc>`_)

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Speed up get requested reviewers and teams for pr (`#2349 <https://github.com/PyGithub/PyGithub/pull/2349>`_) (`6725eceb <https://github.com/PyGithub/PyGithub/commit/6725eceb>`_)
* [WorkflowRun] - Add missing attributes (`run_started_at` & `run_attempt`), remove deprecated `unicode` type (`#2273 <https://github.com/PyGithub/PyGithub/pull/2273>`_) (`3a6235b5 <https://github.com/PyGithub/PyGithub/commit/3a6235b5>`_)
* Add support for repository autolink references (`#2016 <https://github.com/PyGithub/PyGithub/pull/2016>`_) (`0fadd6be <https://github.com/PyGithub/PyGithub/commit/0fadd6be>`_)
* Add retry and pool_size to typing (`#2151 <https://github.com/PyGithub/PyGithub/pull/2151>`_) (`784a3efd <https://github.com/PyGithub/PyGithub/commit/784a3efd>`_)
* Fix/types for repo topic team (`#2341 <https://github.com/PyGithub/PyGithub/pull/2341>`_) (`db9337a4 <https://github.com/PyGithub/PyGithub/commit/db9337a4>`_)
* Add class Artifact (`#2313 <https://github.com/PyGithub/PyGithub/pull/2313>`_) (#2319) (`437ff845 <https://github.com/PyGithub/PyGithub/commit/437ff845>`_)

Version 1.56 (October 13, 2022)
-----------------------------------

Important
^^^^^^^^^

This is the last release that will support Python 3.6.

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Create repo from template (`#2090 <https://github.com/PyGithub/PyGithub/pull/2090>`_) (`b50283a7 <https://github.com/PyGithub/PyGithub/commit/b50283a7>`_)
* Improve signature of Repository.create_repo (`#2118 <https://github.com/PyGithub/PyGithub/pull/2118>`_) (`001970d4 <https://github.com/PyGithub/PyGithub/commit/001970d4>`_)
* Add support for 'visibility' attribute preview for Repositories (`#1872 <https://github.com/PyGithub/PyGithub/pull/1872>`_) (`8d1397af <https://github.com/PyGithub/PyGithub/commit/8d1397af>`_)
* Add Repository.rename_branch method (`#2089 <https://github.com/PyGithub/PyGithub/pull/2089>`_) (`6452ddfe <https://github.com/PyGithub/PyGithub/commit/6452ddfe>`_)
* Add function to delete pending reviews on a pull request (`#1897 <https://github.com/PyGithub/PyGithub/pull/1897>`_) (`c8a945bb <https://github.com/PyGithub/PyGithub/commit/c8a945bb>`_)
* Cover all code paths in search_commits (`#2087 <https://github.com/PyGithub/PyGithub/pull/2087>`_) (`f1faf941 <https://github.com/PyGithub/PyGithub/commit/f1faf941>`_)
* Correctly deal when PaginatedList's data is a dict (`#2084 <https://github.com/PyGithub/PyGithub/pull/2084>`_) (`93b92cd2 <https://github.com/PyGithub/PyGithub/commit/93b92cd2>`_)
* Add two_factor_authentication in AuthenticatedUser. (`#1972 <https://github.com/PyGithub/PyGithub/pull/1972>`_) (`4f00cbf2 <https://github.com/PyGithub/PyGithub/commit/4f00cbf2>`_)
* Add ProjectCard.edit() to the type stub (`#2080 <https://github.com/PyGithub/PyGithub/pull/2080>`_) (`d417e4c4 <https://github.com/PyGithub/PyGithub/commit/d417e4c4>`_)
* Add method to delete Workflow runs (`#2078 <https://github.com/PyGithub/PyGithub/pull/2078>`_) (`b1c8eec5 <https://github.com/PyGithub/PyGithub/commit/b1c8eec5>`_)
* Implement organization.cancel_invitation() (`#2072 <https://github.com/PyGithub/PyGithub/pull/2072>`_) (`53fb4988 <https://github.com/PyGithub/PyGithub/commit/53fb4988>`_)
* Feat: Add `html_url` property in Team Class. (`#1983 <https://github.com/PyGithub/PyGithub/pull/1983>`_) (`6570892a <https://github.com/PyGithub/PyGithub/commit/6570892a>`_)
* Add support for Python 3.10 (`#2073 <https://github.com/PyGithub/PyGithub/pull/2073>`_) (`aa694f8e <https://github.com/PyGithub/PyGithub/commit/aa694f8e>`_)
* Add github actions secrets to org (`#2006 <https://github.com/PyGithub/PyGithub/pull/2006>`_) (`bc5e5950 <https://github.com/PyGithub/PyGithub/commit/bc5e5950>`_)
* Correct replay for Organization.create_project() test (`#2075 <https://github.com/PyGithub/PyGithub/pull/2075>`_) (`fcc12368 <https://github.com/PyGithub/PyGithub/commit/fcc12368>`_)
* Fix install command example (`#2043 <https://github.com/PyGithub/PyGithub/pull/2043>`_) (`99e00a28 <https://github.com/PyGithub/PyGithub/commit/99e00a28>`_)
* Fix: #1671 Convert Python Bool to API Parameter for Authenticated User Notifications (`#2001 <https://github.com/PyGithub/PyGithub/pull/2001>`_) (`1da600a3 <https://github.com/PyGithub/PyGithub/commit/1da600a3>`_)
* Do not transform requestHeaders when logging (`#1965 <https://github.com/PyGithub/PyGithub/pull/1965>`_) (`1265747e <https://github.com/PyGithub/PyGithub/commit/1265747e>`_)
* Add type to OrderedDict (`#1954 <https://github.com/PyGithub/PyGithub/pull/1954>`_) (`ed7d0fe9 <https://github.com/PyGithub/PyGithub/commit/ed7d0fe9>`_)
* Add Commit.get_pulls() to pyi (`#1958 <https://github.com/PyGithub/PyGithub/pull/1958>`_) (`b4664705 <https://github.com/PyGithub/PyGithub/commit/b4664705>`_)
* Adding headers in GithubException is a breaking change (`#1931 <https://github.com/PyGithub/PyGithub/pull/1931>`_) (`d1644e33 <https://github.com/PyGithub/PyGithub/commit/d1644e33>`_)

Version 1.55 (April 26, 2021)
-----------------------------------

Breaking Changes
^^^^^^^^^^^^^^^^

* Remove client_id/client_secret authentication (`#1888 <https://github.com/PyGithub/PyGithub/pull/1888>`_) (`901af8c8 <https://github.com/PyGithub/PyGithub/commit/901af8c8>`_)
* Adjust to Github API changes regarding emails (`#1890 <https://github.com/PyGithub/PyGithub/pull/1890>`_) (`2c77cfad <https://github.com/PyGithub/PyGithub/commit/2c77cfad>`_)
  - This impacts what AuthenticatedUser.get_emails() returns
* PublicKey.key_id could be int on Github Enterprise (`#1894 <https://github.com/PyGithub/PyGithub/pull/1894>`_) (`ad124ef4 <https://github.com/PyGithub/PyGithub/commit/ad124ef4>`_)
* Export headers in GithubException (`#1887 <https://github.com/PyGithub/PyGithub/pull/1887>`_) (`ddd437a7 <https://github.com/PyGithub/PyGithub/commit/ddd437a7>`_)

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Do not import from unpackaged paths in typing (`#1926 <https://github.com/PyGithub/PyGithub/pull/1926>`_) (`27ba7838 <https://github.com/PyGithub/PyGithub/commit/27ba7838>`_)
* Implement hash for CompletableGithubObject (`#1922 <https://github.com/PyGithub/PyGithub/pull/1922>`_) (`4faff23c <https://github.com/PyGithub/PyGithub/commit/4faff23c>`_)
* Use property decorator to improve typing compatibility (`#1925 <https://github.com/PyGithub/PyGithub/pull/1925>`_) (`e4168109 <https://github.com/PyGithub/PyGithub/commit/e4168109>`_)
* Fix :rtype: directive (`#1927 <https://github.com/PyGithub/PyGithub/pull/1927>`_) (`54b6a97b <https://github.com/PyGithub/PyGithub/commit/54b6a97b>`_)
* Update most URLs to docs.github.com (`#1896 <https://github.com/PyGithub/PyGithub/pull/1896>`_) (`babcbcd0 <https://github.com/PyGithub/PyGithub/commit/babcbcd0>`_)
* Tighten asserts for new Permission tests (`#1893 <https://github.com/PyGithub/PyGithub/pull/1893>`_) (`5aab6f5d <https://github.com/PyGithub/PyGithub/commit/5aab6f5d>`_)
* Adding attributes "maintain" and "triage" to class "Permissions" (`#1810 <https://github.com/PyGithub/PyGithub/pull/1810>`_) (`76879613 <https://github.com/PyGithub/PyGithub/commit/76879613>`_)
* Add default arguments to Workflow method type annotations (`#1857 <https://github.com/PyGithub/PyGithub/pull/1857>`_) (`7d6bac9e <https://github.com/PyGithub/PyGithub/commit/7d6bac9e>`_)
* Re-raise the exception when failing to parse JSON (`#1892 <https://github.com/PyGithub/PyGithub/pull/1892>`_) (`916da53b <https://github.com/PyGithub/PyGithub/commit/916da53b>`_)
* Allow adding attributes at the end of the list (`#1807 <https://github.com/PyGithub/PyGithub/pull/1807>`_) (`0245b758 <https://github.com/PyGithub/PyGithub/commit/0245b758>`_)
* Updating links to Github documentation for deploy keys (`#1850 <https://github.com/PyGithub/PyGithub/pull/1850>`_) (`c27fb919 <https://github.com/PyGithub/PyGithub/commit/c27fb919>`_)
* Update PyJWT Version to 2.0+ (`#1891 <https://github.com/PyGithub/PyGithub/pull/1891>`_) (`a68577b7 <https://github.com/PyGithub/PyGithub/commit/a68577b7>`_)
* Use right variable in both get_check_runs() (`#1889 <https://github.com/PyGithub/PyGithub/pull/1889>`_) (`3003e065 <https://github.com/PyGithub/PyGithub/commit/3003e065>`_)
* fix bad assertions in github.Project.edit (`#1817 <https://github.com/PyGithub/PyGithub/pull/1817>`_) (`6bae9e5c <https://github.com/PyGithub/PyGithub/commit/6bae9e5c>`_)
* Test repr() for PublicKey (`#1879 <https://github.com/PyGithub/PyGithub/pull/1879>`_) (`e0acd8f4 <https://github.com/PyGithub/PyGithub/commit/e0acd8f4>`_)
* Add support for deleting repository secrets (`#1868 <https://github.com/PyGithub/PyGithub/pull/1868>`_) (`696793de <https://github.com/PyGithub/PyGithub/commit/696793de>`_)
* Switch repository secrets to using f-strings (`#1867 <https://github.com/PyGithub/PyGithub/pull/1867>`_) (`aa240304 <https://github.com/PyGithub/PyGithub/commit/aa240304>`_)
* Manually fixing paths for codecov.io to cover all project files (`#1813 <https://github.com/PyGithub/PyGithub/pull/1813>`_) (`b2232c89 <https://github.com/PyGithub/PyGithub/commit/b2232c89>`_)
* Add missing links to project metadata (`#1789 <https://github.com/PyGithub/PyGithub/pull/1789>`_) (`64f532ae <https://github.com/PyGithub/PyGithub/commit/64f532ae>`_)
* No longer show username and password examples (`#1866 <https://github.com/PyGithub/PyGithub/pull/1866>`_) (`55d98373 <https://github.com/PyGithub/PyGithub/commit/55d98373>`_)
* Adding github actions secrets (`#1681 <https://github.com/PyGithub/PyGithub/pull/1681>`_) (`c90c050e <https://github.com/PyGithub/PyGithub/commit/c90c050e>`_)
* fix get_user_issues (`#1842 <https://github.com/PyGithub/PyGithub/pull/1842>`_) (`7db1b0c9 <https://github.com/PyGithub/PyGithub/commit/7db1b0c9>`_)
* Switch all string addition to using f-strings (`#1774 <https://github.com/PyGithub/PyGithub/pull/1774>`_) (`290b6272 <https://github.com/PyGithub/PyGithub/commit/290b6272>`_)
* Enabling connection pool_size definition (`a77d4f48 <https://github.com/PyGithub/PyGithub/commit/a77d4f48>`_)
* Always define the session adapter (`aaec0a0f <https://github.com/PyGithub/PyGithub/commit/aaec0a0f>`_)

Version 1.54.1 (December 24, 2020)
-----------------------------------

* Pin pyjwt version (`#1797 <https://github.com/PyGithub/PyGithub/pull/1797>`_) (`31a1c007 <https://github.com/PyGithub/PyGithub/commit/31a1c007>`_)
* Add pyupgrade to pre-commit configuration (`#1783 <https://github.com/PyGithub/PyGithub/pull/1783>`_) (`e113e37d <https://github.com/PyGithub/PyGithub/commit/e113e37d>`_)
* Fix #1731: Incorrect annotation (`82c349ce <https://github.com/PyGithub/PyGithub/commit/82c349ce>`_)
* Drop support for Python 3.5 (`#1770 <https://github.com/PyGithub/PyGithub/pull/1770>`_) (`63e4fae9 <https://github.com/PyGithub/PyGithub/commit/63e4fae9>`_)
* Revert "Pin requests to <2.25 as well (`#1757 <https://github.com/PyGithub/PyGithub/pull/1757>`_)" (#1763) (`a806b523 <https://github.com/PyGithub/PyGithub/commit/a806b523>`_)
* Fix stubs file for Repository (`fab682a5 <https://github.com/PyGithub/PyGithub/commit/fab682a5>`_)

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

* Add support for Check Suites (`#1764 <https://github.com/PyGithub/PyGithub/pull/1764>`_) (`6d501b28 <https://github.com/PyGithub/PyGithub/commit/6d501b28>`_)
* Add missing preview features of Deployment and Deployment Statuses API (`#1674 <https://github.com/PyGithub/PyGithub/pull/1674>`_) (`197e0653 <https://github.com/PyGithub/PyGithub/commit/197e0653>`_)
* Correct typing for Commit.get_comments() (`#1765 <https://github.com/PyGithub/PyGithub/pull/1765>`_) (`fcdd9eae <https://github.com/PyGithub/PyGithub/commit/fcdd9eae>`_)
* Pin requests to <2.25 as well (`#1757 <https://github.com/PyGithub/PyGithub/pull/1757>`_) (`d159425f <https://github.com/PyGithub/PyGithub/commit/d159425f>`_)
* Add Support for Check Runs (`#1727 <https://github.com/PyGithub/PyGithub/pull/1727>`_) (`c77c0676 <https://github.com/PyGithub/PyGithub/commit/c77c0676>`_)
* Added a method for getting a user by their id (`#1691 <https://github.com/PyGithub/PyGithub/pull/1691>`_) (`4cfc9912 <https://github.com/PyGithub/PyGithub/commit/4cfc9912>`_)
* Fix #1742 - incorrect typehint for `Installation.id` (`#1743 <https://github.com/PyGithub/PyGithub/pull/1743>`_) (`546f6495 <https://github.com/PyGithub/PyGithub/commit/546f6495>`_)
* Add WorkflowRun.workflow_id (`#1737 <https://github.com/PyGithub/PyGithub/pull/1737>`_) (`78a29a7c <https://github.com/PyGithub/PyGithub/commit/78a29a7c>`_)
* Add support for Python 3.9 (`#1735 <https://github.com/PyGithub/PyGithub/pull/1735>`_) (`1bb18ab5 <https://github.com/PyGithub/PyGithub/commit/1bb18ab5>`_)
* Added support for the Self-Hosted actions runners API (`#1684 <https://github.com/PyGithub/PyGithub/pull/1684>`_) (`24251f4b <https://github.com/PyGithub/PyGithub/commit/24251f4b>`_)
* Fix Branch protection status in the examples (`#1729 <https://github.com/PyGithub/PyGithub/pull/1729>`_) (`88800844 <https://github.com/PyGithub/PyGithub/commit/88800844>`_)
* Filter the DeprecationWarning in Team tests (`#1728 <https://github.com/PyGithub/PyGithub/pull/1728>`_) (`23f47539 <https://github.com/PyGithub/PyGithub/commit/23f47539>`_)
* Added get_installations() to Organizations (`#1695 <https://github.com/PyGithub/PyGithub/pull/1695>`_) (`b42fb244 <https://github.com/PyGithub/PyGithub/commit/b42fb244>`_)
* Fix #1507: Add new Teams: Add or update team repository endpoint (`#1509 <https://github.com/PyGithub/PyGithub/pull/1509>`_) (`1c55be51 <https://github.com/PyGithub/PyGithub/commit/1c55be51>`_)
* Added support for `Repository.get_workflow_runs` parameters (`#1682 <https://github.com/PyGithub/PyGithub/pull/1682>`_) (`c23564dd <https://github.com/PyGithub/PyGithub/commit/c23564dd>`_)
* feat(pullrequest): add the rebaseable attribute (`#1690 <https://github.com/PyGithub/PyGithub/pull/1690>`_) (`ee4c7a7e <https://github.com/PyGithub/PyGithub/commit/ee4c7a7e>`_)
* Add support for deleting reactions (`#1708 <https://github.com/PyGithub/PyGithub/pull/1708>`_) (`f7d203c0 <https://github.com/PyGithub/PyGithub/commit/f7d203c0>`_)
* Correct type hint for InputGitTreeElement.sha (`08b72b48 <https://github.com/PyGithub/PyGithub/commit/08b72b48>`_)
* Ignore new black formatting commit for git blame (`#1680 <https://github.com/PyGithub/PyGithub/pull/1680>`_) (`7ec4f155 <https://github.com/PyGithub/PyGithub/commit/7ec4f155>`_)
* Format with new black (`#1679 <https://github.com/PyGithub/PyGithub/pull/1679>`_) (`07e29fe0 <https://github.com/PyGithub/PyGithub/commit/07e29fe0>`_)
* Add get_timeline() to Issue's type stubs (`#1663 <https://github.com/PyGithub/PyGithub/pull/1663>`_) (`6bc9ecc8 <https://github.com/PyGithub/PyGithub/commit/6bc9ecc8>`_)

Version 1.53 (August 18, 2020)
-----------------------------------

* Test Organization.get_hook() (`#1660 <https://github.com/PyGithub/PyGithub/pull/1660>`_) (`2646a98c <https://github.com/PyGithub/PyGithub/commit/2646a98c>`_)
* Add method get_team_membership for user to Team  (`#1658 <https://github.com/PyGithub/PyGithub/pull/1658>`_) (`749e8d35 <https://github.com/PyGithub/PyGithub/commit/749e8d35>`_)
* Add typing files for OAuth classes (`#1656 <https://github.com/PyGithub/PyGithub/pull/1656>`_) (`429fcc73 <https://github.com/PyGithub/PyGithub/commit/429fcc73>`_)
* Fix Repository.create_repository_dispatch type signature (`#1643 <https://github.com/PyGithub/PyGithub/pull/1643>`_) (`f891bd61 <https://github.com/PyGithub/PyGithub/commit/f891bd61>`_)
* PaginatedList's totalCount is 0 if no last page (`#1641 <https://github.com/PyGithub/PyGithub/pull/1641>`_) (`69b37b4a <https://github.com/PyGithub/PyGithub/commit/69b37b4a>`_)
* Add initial support for Github Apps. (`#1631 <https://github.com/PyGithub/PyGithub/pull/1631>`_) (`260558c1 <https://github.com/PyGithub/PyGithub/commit/260558c1>`_)
* Correct ``**kwargs`` typing for ``search_*`` (`#1636 <https://github.com/PyGithub/PyGithub/pull/1636>`_) (`165d995d <https://github.com/PyGithub/PyGithub/commit/165d995d>`_)
* Add delete_branch_on_merge arg to Repository.edit type stub (`#1639 <https://github.com/PyGithub/PyGithub/pull/1639>`_) (`15b5ae0c <https://github.com/PyGithub/PyGithub/commit/15b5ae0c>`_)
* Fix type stub for MainClass.get_user (`#1637 <https://github.com/PyGithub/PyGithub/pull/1637>`_) (`8912be64 <https://github.com/PyGithub/PyGithub/commit/8912be64>`_)
* Add type stub for Repository.create_fork (`#1638 <https://github.com/PyGithub/PyGithub/pull/1638>`_) (`de386dfb <https://github.com/PyGithub/PyGithub/commit/de386dfb>`_)
* Correct Repository.create_pull typing harder (`#1635 <https://github.com/PyGithub/PyGithub/pull/1635>`_) (`5ad091d0 <https://github.com/PyGithub/PyGithub/commit/5ad091d0>`_)

Version 1.52 (August 03, 2020)
-----------------------------------

* upload_asset with data in memory (`#1601 <https://github.com/PyGithub/PyGithub/pull/1601>`_) (`a7786393 <https://github.com/PyGithub/PyGithub/commit/a7786393>`_)
* Make Issue.closed_by nullable (`#1629 <https://github.com/PyGithub/PyGithub/pull/1629>`_) (`06dae387 <https://github.com/PyGithub/PyGithub/commit/06dae387>`_)
* Add support for workflow dispatch event (`#1625 <https://github.com/PyGithub/PyGithub/pull/1625>`_) (`16850ef1 <https://github.com/PyGithub/PyGithub/commit/16850ef1>`_)
* Do not check reaction_type before sending (`#1592 <https://github.com/PyGithub/PyGithub/pull/1592>`_) (`136a3e80 <https://github.com/PyGithub/PyGithub/commit/136a3e80>`_)
* Various Github Action improvement (`#1610 <https://github.com/PyGithub/PyGithub/pull/1610>`_) (`416f2d0f <https://github.com/PyGithub/PyGithub/commit/416f2d0f>`_)
* more flexible header splitting (`#1616 <https://github.com/PyGithub/PyGithub/pull/1616>`_) (`85e71361 <https://github.com/PyGithub/PyGithub/commit/85e71361>`_)
* Create Dependabot config file (`#1607 <https://github.com/PyGithub/PyGithub/pull/1607>`_) (`e272f117 <https://github.com/PyGithub/PyGithub/commit/e272f117>`_)
* Add support for deployment statuses (`#1588 <https://github.com/PyGithub/PyGithub/pull/1588>`_) (`048c8a1d <https://github.com/PyGithub/PyGithub/commit/048c8a1d>`_)
* Adds the 'twitter_username' attribute to NamedUser. (`#1585 <https://github.com/PyGithub/PyGithub/pull/1585>`_) (`079f75a7 <https://github.com/PyGithub/PyGithub/commit/079f75a7>`_)
* Create WorkflowRun.timing namedtuple from the dict (`#1587 <https://github.com/PyGithub/PyGithub/pull/1587>`_) (`1879518e <https://github.com/PyGithub/PyGithub/commit/1879518e>`_)
* Add missing properties to PullRequest.pyi (`#1577 <https://github.com/PyGithub/PyGithub/pull/1577>`_) (`c84fad81 <https://github.com/PyGithub/PyGithub/commit/c84fad81>`_)
* Add support for Workflow Runs (`#1583 <https://github.com/PyGithub/PyGithub/pull/1583>`_) (`4fb1d23f <https://github.com/PyGithub/PyGithub/commit/4fb1d23f>`_)
* More precise typing for Repository.create_pull (`#1581 <https://github.com/PyGithub/PyGithub/pull/1581>`_) (`4ed7aaf8 <https://github.com/PyGithub/PyGithub/commit/4ed7aaf8>`_)
* Update sphinx-rtd-theme requirement from <0.5 to <0.6 (`#1563 <https://github.com/PyGithub/PyGithub/pull/1563>`_) (`f9e4feeb <https://github.com/PyGithub/PyGithub/commit/f9e4feeb>`_)
* More precise typing for MainClass.get_user() (`#1575 <https://github.com/PyGithub/PyGithub/pull/1575>`_) (`3668f866 <https://github.com/PyGithub/PyGithub/commit/3668f866>`_)
* Small documentation correction in Repository.py (`#1565 <https://github.com/PyGithub/PyGithub/pull/1565>`_) (`f0f6ec83 <https://github.com/PyGithub/PyGithub/commit/f0f6ec83>`_)
* Remove "api_preview" parameter from type stubs and docstrings
  (`#1559 <https://github.com/PyGithub/PyGithub/pull/1559>`_) (`cc1b884c <https://github.com/PyGithub/PyGithub/commit/cc1b884c>`_)
* Upgrade actions/setup-python to v2 (`#1555 <https://github.com/PyGithub/PyGithub/pull/1555>`_) (`6f1640d2 <https://github.com/PyGithub/PyGithub/commit/6f1640d2>`_)
* Clean up tests for GitReleaseAsset (`#1546 <https://github.com/PyGithub/PyGithub/pull/1546>`_) (`925764ad <https://github.com/PyGithub/PyGithub/commit/925764ad>`_)
* Repository.update_file() content also accepts bytes (`#1543 <https://github.com/PyGithub/PyGithub/pull/1543>`_) (`9fb8588b <https://github.com/PyGithub/PyGithub/commit/9fb8588b>`_)
* Fix Repository.get_issues stub (`#1540 <https://github.com/PyGithub/PyGithub/pull/1540>`_) (`b40b75f8 <https://github.com/PyGithub/PyGithub/commit/b40b75f8>`_)
* Check all arguments of NamedUser.get_repos() (`#1532 <https://github.com/PyGithub/PyGithub/pull/1532>`_) (`69bfc325 <https://github.com/PyGithub/PyGithub/commit/69bfc325>`_)
* Correct Workflow typing (`#1533 <https://github.com/PyGithub/PyGithub/pull/1533>`_) (`f41c046f <https://github.com/PyGithub/PyGithub/commit/f41c046f>`_)
* Remove RateLimit.rate (`#1529 <https://github.com/PyGithub/PyGithub/pull/1529>`_) (`7abf6004 <https://github.com/PyGithub/PyGithub/commit/7abf6004>`_)
* PullRequestReview is not a completable object (`#1528 <https://github.com/PyGithub/PyGithub/pull/1528>`_) (`19fc43ab <https://github.com/PyGithub/PyGithub/commit/19fc43ab>`_)
* Test more attributes (`#1526 <https://github.com/PyGithub/PyGithub/pull/1526>`_) (`52ec366b <https://github.com/PyGithub/PyGithub/commit/52ec366b>`_)
* Remove pointless setters in GitReleaseAsset (`#1527 <https://github.com/PyGithub/PyGithub/pull/1527>`_) (`1dd1cf9c <https://github.com/PyGithub/PyGithub/commit/1dd1cf9c>`_)
* Drop some unimplemented methods in GitRef (`#1525 <https://github.com/PyGithub/PyGithub/pull/1525>`_) (`d4b61311 <https://github.com/PyGithub/PyGithub/commit/d4b61311>`_)
* Remove unneeded duplicate string checks in Branch (`#1524 <https://github.com/PyGithub/PyGithub/pull/1524>`_) (`61b61092 <https://github.com/PyGithub/PyGithub/commit/61b61092>`_)
* Turn on coverage reporting for codecov (`#1522 <https://github.com/PyGithub/PyGithub/pull/1522>`_) (`e79b9013 <https://github.com/PyGithub/PyGithub/commit/e79b9013>`_)
* Drastically increase coverage by checking repr() (`#1521 <https://github.com/PyGithub/PyGithub/pull/1521>`_) (`291c4630 <https://github.com/PyGithub/PyGithub/commit/291c4630>`_)
* Fixed formatting of docstrings for `Repository.create_git_tag_and_release()`
  and `StatsPunchCard`. (`#1520 <https://github.com/PyGithub/PyGithub/pull/1520>`_) (`ce400bc7 <https://github.com/PyGithub/PyGithub/commit/ce400bc7>`_)
* Remove Repository.topics (`#1505 <https://github.com/PyGithub/PyGithub/pull/1505>`_) (`53d58d2b <https://github.com/PyGithub/PyGithub/commit/53d58d2b>`_)
* Small improvements to typing (`#1517 <https://github.com/PyGithub/PyGithub/pull/1517>`_) (`7b20b13d <https://github.com/PyGithub/PyGithub/commit/7b20b13d>`_)
* Correct Repository.get_workflows() (`#1518 <https://github.com/PyGithub/PyGithub/pull/1518>`_) (`8727003f <https://github.com/PyGithub/PyGithub/commit/8727003f>`_)
* docs(repository): correct releases link (`#1514 <https://github.com/PyGithub/PyGithub/pull/1514>`_) (`f7cc534d <https://github.com/PyGithub/PyGithub/commit/f7cc534d>`_)
* correct Repository.stargazers_count return type to int (`#1513 <https://github.com/PyGithub/PyGithub/pull/1513>`_) (`b5737d41 <https://github.com/PyGithub/PyGithub/commit/b5737d41>`_)
* Fix two RST warnings in Webhook.rst (`#1512 <https://github.com/PyGithub/PyGithub/pull/1512>`_) (`5a8bc203 <https://github.com/PyGithub/PyGithub/commit/5a8bc203>`_)
* Filter FutureWarning for 2 test cases (`#1510 <https://github.com/PyGithub/PyGithub/pull/1510>`_) (`09a1d9e4 <https://github.com/PyGithub/PyGithub/commit/09a1d9e4>`_)
* Raise a FutureWarning on use of client_{id,secret} (`#1506 <https://github.com/PyGithub/PyGithub/pull/1506>`_) (`2475fa66 <https://github.com/PyGithub/PyGithub/commit/2475fa66>`_)
* Improve type signature for create_from_raw_data (`#1503 <https://github.com/PyGithub/PyGithub/pull/1503>`_) (`c7b5eff0 <https://github.com/PyGithub/PyGithub/commit/c7b5eff0>`_)
* feat(column): move, edit and delete project columns (`#1497 <https://github.com/PyGithub/PyGithub/pull/1497>`_) (`a32a8965 <https://github.com/PyGithub/PyGithub/commit/a32a8965>`_)
* Add support for Workflows (`#1496 <https://github.com/PyGithub/PyGithub/pull/1496>`_) (`a1ed7c0e <https://github.com/PyGithub/PyGithub/commit/a1ed7c0e>`_)
* Add create_repository_dispatch to typing files (`#1502 <https://github.com/PyGithub/PyGithub/pull/1502>`_) (`ba9d59c2 <https://github.com/PyGithub/PyGithub/commit/ba9d59c2>`_)
* Add OAuth support for GitHub applications (`4b437110 <https://github.com/PyGithub/PyGithub/commit/4b437110>`_)
* Create AccessToken entity (`4a6468aa <https://github.com/PyGithub/PyGithub/commit/4a6468aa>`_)
* Extend installation attributes (`61808da1 <https://github.com/PyGithub/PyGithub/commit/61808da1>`_)

Version 1.51 (May 03, 2020)
-----------------------------------

* Type stubs are now packaged with the build (`#1489 <https://github.com/PyGithub/PyGithub/pull/1489>`_) (`6eba4506 <https://github.com/PyGithub/PyGithub/commit/6eba4506>`_)
* Travis CI is now dropped in favor of Github workflow (`#1488 <https://github.com/PyGithub/PyGithub/pull/1488>`_) (`d6e77ba1 <https://github.com/PyGithub/PyGithub/commit/d6e77ba1>`_)
* Get the project column by id (`#1466 <https://github.com/PyGithub/PyGithub/pull/1466>`_) (`63855409 <https://github.com/PyGithub/PyGithub/commit/63855409>`_)

Version 1.50 (April 26, 2020)
-----------------------------------

New features
^^^^^^^^^^^^

* PyGithub now supports type checking thanks to (`#1231 <https://github.com/PyGithub/PyGithub/pull/1231>`_) (`91433fe9 <https://github.com/PyGithub/PyGithub/commit/91433fe9>`_)
* Slack is now the main channel of communication rather than Gitter (`6a6e7c26 <https://github.com/PyGithub/PyGithub/commit/6a6e7c26>`_)
* Ability to retrieve public events (`#1481 <https://github.com/PyGithub/PyGithub/pull/1481>`_) (`5cf9950b <https://github.com/PyGithub/PyGithub/commit/5cf9950b>`_)
* Add and handle the maintainer_can_modify attribute in PullRequest (`#1465 <https://github.com/PyGithub/PyGithub/pull/1465>`_) (`e0997b43 <https://github.com/PyGithub/PyGithub/commit/e0997b43>`_)
* List matching references (`#1471 <https://github.com/PyGithub/PyGithub/pull/1471>`_) (`d3bc6a5c <https://github.com/PyGithub/PyGithub/commit/d3bc6a5c>`_)
* Add create_repository_dispatch (`#1449 <https://github.com/PyGithub/PyGithub/pull/1449>`_) (`edcbdfda <https://github.com/PyGithub/PyGithub/commit/edcbdfda>`_)
* Add some Organization and Repository attributes. (`#1468 <https://github.com/PyGithub/PyGithub/pull/1468>`_) (`3ab97d61 <https://github.com/PyGithub/PyGithub/commit/3ab97d61>`_)
* Add create project method (`801ea385 <https://github.com/PyGithub/PyGithub/commit/801ea385>`_)

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Drop use of shadow-cat for draft PRs (`#1469 <https://github.com/PyGithub/PyGithub/pull/1469>`_) (`84bb69ab <https://github.com/PyGithub/PyGithub/commit/84bb69ab>`_)
* AuthenticatedUser.get_organization_membership() should be str (`#1473 <https://github.com/PyGithub/PyGithub/pull/1473>`_) (`38b34db5 <https://github.com/PyGithub/PyGithub/commit/38b34db5>`_)
* Drop documentation for len() of PaginatedList (`#1470 <https://github.com/PyGithub/PyGithub/pull/1470>`_) (`70462598 <https://github.com/PyGithub/PyGithub/commit/70462598>`_)
* Fix param name of projectcard's move function (`#1451 <https://github.com/PyGithub/PyGithub/pull/1451>`_) (`bafc4efc <https://github.com/PyGithub/PyGithub/commit/bafc4efc>`_)
* Correct typos found with codespell (`#1467 <https://github.com/PyGithub/PyGithub/pull/1467>`_) (`83bef0f7 <https://github.com/PyGithub/PyGithub/commit/83bef0f7>`_)
* Export IncompletableObject in the github namespace (`#1450 <https://github.com/PyGithub/PyGithub/pull/1450>`_) (`0ebdbb26 <https://github.com/PyGithub/PyGithub/commit/0ebdbb26>`_)
* Add GitHub Action workflow for checks (`#1464 <https://github.com/PyGithub/PyGithub/pull/1464>`_) (`f1401c15 <https://github.com/PyGithub/PyGithub/commit/f1401c15>`_)
* Drop unneeded ignore rule for flake8 (`#1454 <https://github.com/PyGithub/PyGithub/pull/1454>`_) (`b4ca9177 <https://github.com/PyGithub/PyGithub/commit/b4ca9177>`_)
* Use pytest to parametrize tests (`#1438 <https://github.com/PyGithub/PyGithub/pull/1438>`_) (`d2e9bd69 <https://github.com/PyGithub/PyGithub/commit/d2e9bd69>`_)

Version 1.47 (March 15, 2020)
-----------------------------------

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Add support to edit and delete a project (`#1434 <https://github.com/PyGithub/PyGithub/pull/1434>`_) (`f11f7395 <https://github.com/PyGithub/PyGithub/commit/f11f7395>`_)
* Add method for fetching pull requests associated with a commit (`#1433 <https://github.com/PyGithub/PyGithub/pull/1433>`_) (`0c55381b <https://github.com/PyGithub/PyGithub/commit/0c55381b>`_)
* Add "get_repo_permission" to Team class (`#1416 <https://github.com/PyGithub/PyGithub/pull/1416>`_) (`219bde53 <https://github.com/PyGithub/PyGithub/commit/219bde53>`_)
* Add list projects support, update tests (`#1431 <https://github.com/PyGithub/PyGithub/pull/1431>`_) (`e44d11d5 <https://github.com/PyGithub/PyGithub/commit/e44d11d5>`_)
* Don't transform completely in PullRequest.*assignees (`#1428 <https://github.com/PyGithub/PyGithub/pull/1428>`_) (`b1c35499 <https://github.com/PyGithub/PyGithub/commit/b1c35499>`_)
* Add create_project support, add tests (`#1429 <https://github.com/PyGithub/PyGithub/pull/1429>`_) (`bf62f752 <https://github.com/PyGithub/PyGithub/commit/bf62f752>`_)
* Add draft attribute, update test (`bd285248 <https://github.com/PyGithub/PyGithub/commit/bd285248>`_)
* Docstring for Repository.create_git_tag_and_release (`#1425 <https://github.com/PyGithub/PyGithub/pull/1425>`_) (`bfeacded <https://github.com/PyGithub/PyGithub/commit/bfeacded>`_)
* Create a tox docs environment (`#1426 <https://github.com/PyGithub/PyGithub/pull/1426>`_) (`b30c09aa <https://github.com/PyGithub/PyGithub/commit/b30c09aa>`_)
* Add Deployments API (`#1424 <https://github.com/PyGithub/PyGithub/pull/1424>`_) (`3d93ee1c <https://github.com/PyGithub/PyGithub/commit/3d93ee1c>`_)
* Add support for editing project cards (`#1418 <https://github.com/PyGithub/PyGithub/pull/1418>`_) (`425280ce <https://github.com/PyGithub/PyGithub/commit/425280ce>`_)
* Add draft flag parameter, update tests (`bd0211eb <https://github.com/PyGithub/PyGithub/commit/bd0211eb>`_)
* Switch to using pytest (`#1423 <https://github.com/PyGithub/PyGithub/pull/1423>`_) (`c822dd1c <https://github.com/PyGithub/PyGithub/commit/c822dd1c>`_)
* Fix GitMembership with a hammer (`#1420 <https://github.com/PyGithub/PyGithub/pull/1420>`_) (`f2939eb7 <https://github.com/PyGithub/PyGithub/commit/f2939eb7>`_)
* Add support to reply to a Pull request comment (`#1374 <https://github.com/PyGithub/PyGithub/pull/1374>`_) (`1c82573d <https://github.com/PyGithub/PyGithub/commit/1c82573d>`_)
* PullRequest.update_branch(): allow expected_head_sha to be empty (`#1412 <https://github.com/PyGithub/PyGithub/pull/1412>`_) (`806130e9 <https://github.com/PyGithub/PyGithub/commit/806130e9>`_)
* Implement ProjectCard.delete() (`#1417 <https://github.com/PyGithub/PyGithub/pull/1417>`_) (`aeb27b78 <https://github.com/PyGithub/PyGithub/commit/aeb27b78>`_)
* Add pre-commit plugin for black/isort/flake8 (`#1398 <https://github.com/PyGithub/PyGithub/pull/1398>`_) (`08b1c474 <https://github.com/PyGithub/PyGithub/commit/08b1c474>`_)
* Add tox (`#1388 <https://github.com/PyGithub/PyGithub/pull/1388>`_) (`125536fe <https://github.com/PyGithub/PyGithub/commit/125536fe>`_)
* Open file in text mode in scripts/add_attribute.py (`#1396 <https://github.com/PyGithub/PyGithub/pull/1396>`_) (`0396a493 <https://github.com/PyGithub/PyGithub/commit/0396a493>`_)
* Silence most ResourceWarnings (`#1393 <https://github.com/PyGithub/PyGithub/pull/1393>`_) (`dd31a706 <https://github.com/PyGithub/PyGithub/commit/dd31a706>`_)
* Assert more attributes in Membership (`#1391 <https://github.com/PyGithub/PyGithub/pull/1391>`_) (`d6dee016 <https://github.com/PyGithub/PyGithub/commit/d6dee016>`_)
* Assert on changed Repository attributes (`#1390 <https://github.com/PyGithub/PyGithub/pull/1390>`_) (`6e3ceb19 <https://github.com/PyGithub/PyGithub/commit/6e3ceb19>`_)
* Add reset to the repr for Rate (`#1389 <https://github.com/PyGithub/PyGithub/pull/1389>`_) (`0829af81 <https://github.com/PyGithub/PyGithub/commit/0829af81>`_)

Version 1.46 (February 11, 2020)
-----------------------------------
Important
^^^^^^^^^

Python 2 support has been removed. If you still require Python 2, use 1.45.

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Add repo edit support for delete_branch_on_merge (`#1381 <https://github.com/PyGithub/PyGithub/pull/1381>`_) (`9564cd4d <https://github.com/PyGithub/PyGithub/commit/9564cd4d>`_)
* Fix mistake in Repository.create_fork() (`#1383 <https://github.com/PyGithub/PyGithub/pull/1383>`_) (`ad040baf <https://github.com/PyGithub/PyGithub/commit/ad040baf>`_)
* Correct two attributes in Invitation (`#1382 <https://github.com/PyGithub/PyGithub/pull/1382>`_) (`882fe087 <https://github.com/PyGithub/PyGithub/commit/882fe087>`_)
* Search repo issues by string label (`#1379 <https://github.com/PyGithub/PyGithub/pull/1379>`_) (`4ae1a1e5 <https://github.com/PyGithub/PyGithub/commit/4ae1a1e5>`_)
* Correct Repository.create_git_tag_and_release() (`#1362 <https://github.com/PyGithub/PyGithub/pull/1362>`_) (`ead565ad <https://github.com/PyGithub/PyGithub/commit/ead565ad>`_)
* exposed seats and filled_seats for Github Organization Plan (`#1360 <https://github.com/PyGithub/PyGithub/pull/1360>`_) (`06a300ae <https://github.com/PyGithub/PyGithub/commit/06a300ae>`_)
* Repository.create_project() body is optional (`#1359 <https://github.com/PyGithub/PyGithub/pull/1359>`_) (`0e09983d <https://github.com/PyGithub/PyGithub/commit/0e09983d>`_)
* Implement move action for ProjectCard (`#1356 <https://github.com/PyGithub/PyGithub/pull/1356>`_) (`b11add41 <https://github.com/PyGithub/PyGithub/commit/b11add41>`_)
* Tidy up ProjectCard.get_content() (`#1355 <https://github.com/PyGithub/PyGithub/pull/1355>`_) (`dd80a6c0 <https://github.com/PyGithub/PyGithub/commit/dd80a6c0>`_)
* Added nested teams and parent (`#1348 <https://github.com/PyGithub/PyGithub/pull/1348>`_) (`eacabb2f <https://github.com/PyGithub/PyGithub/commit/eacabb2f>`_)
* Correct parameter for Label.edit (`#1350 <https://github.com/PyGithub/PyGithub/pull/1350>`_) (`16e5f989 <https://github.com/PyGithub/PyGithub/commit/16e5f989>`_)
* doc: example of Pull Request creation (`#1344 <https://github.com/PyGithub/PyGithub/pull/1344>`_) (`d5ad09ae <https://github.com/PyGithub/PyGithub/commit/d5ad09ae>`_)
* Fix PyPI wheel deployment (`#1330 <https://github.com/PyGithub/PyGithub/pull/1330>`_) (`4561930b <https://github.com/PyGithub/PyGithub/commit/4561930b>`_)

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

* Allow sha=None for InputGitTreeElement (`#1327 <https://github.com/PyGithub/PyGithub/pull/1327>`_) (`60464f65 <https://github.com/PyGithub/PyGithub/commit/60464f65>`_)
* Support github timeline events. (`#1302 <https://github.com/PyGithub/PyGithub/pull/1302>`_) (`732fd26a <https://github.com/PyGithub/PyGithub/commit/732fd26a>`_)
* Update link to GitHub Enterprise in README (`#1324 <https://github.com/PyGithub/PyGithub/pull/1324>`_) (`e1537f79 <https://github.com/PyGithub/PyGithub/commit/e1537f79>`_)
* Cleanup travis config (`#1322 <https://github.com/PyGithub/PyGithub/pull/1322>`_) (`8189a538 <https://github.com/PyGithub/PyGithub/commit/8189a538>`_)
* Add support for update branch  (`#1317 <https://github.com/PyGithub/PyGithub/pull/1317>`_) (`baddb719 <https://github.com/PyGithub/PyGithub/commit/baddb719>`_)
* Refactor Logging tests (`#1315 <https://github.com/PyGithub/PyGithub/pull/1315>`_) (`b0ef1909 <https://github.com/PyGithub/PyGithub/commit/b0ef1909>`_)
* Fix rtd build (`b797cac0 <https://github.com/PyGithub/PyGithub/commit/b797cac0>`_)
* Add .git-blame-ignore-revs (`573c674b <https://github.com/PyGithub/PyGithub/commit/573c674b>`_)
* Apply black to whole codebase (`#1303 <https://github.com/PyGithub/PyGithub/pull/1303>`_) (`6ceb9e9a <https://github.com/PyGithub/PyGithub/commit/6ceb9e9a>`_)
* Fix class used returning pull request comments (`#1307 <https://github.com/PyGithub/PyGithub/pull/1307>`_) (`f8e33620 <https://github.com/PyGithub/PyGithub/commit/f8e33620>`_)
* Support for create_fork (`#1306 <https://github.com/PyGithub/PyGithub/pull/1306>`_) (`2ad51f35 <https://github.com/PyGithub/PyGithub/commit/2ad51f35>`_)
* Use Repository.get_contents() in tests (`#1301 <https://github.com/PyGithub/PyGithub/pull/1301>`_) (`e40768e0 <https://github.com/PyGithub/PyGithub/commit/e40768e0>`_)
* Allow GithubObject.update() to be passed headers (`#1300 <https://github.com/PyGithub/PyGithub/pull/1300>`_) (`989b635e <https://github.com/PyGithub/PyGithub/commit/989b635e>`_)
* Correct URL for assignees on PRs (`#1296 <https://github.com/PyGithub/PyGithub/pull/1296>`_) (`3170cafc <https://github.com/PyGithub/PyGithub/commit/3170cafc>`_)
* Use inclusive ordered comparison for 'parameterized' requirement (`#1281 <https://github.com/PyGithub/PyGithub/pull/1281>`_) (`fb19d2f2 <https://github.com/PyGithub/PyGithub/commit/fb19d2f2>`_)
* Deprecate Repository.get_dir_contents() (`#1285 <https://github.com/PyGithub/PyGithub/pull/1285>`_) (`21e89ff1 <https://github.com/PyGithub/PyGithub/commit/21e89ff1>`_)
* Apply some polish to manage.sh (`#1284 <https://github.com/PyGithub/PyGithub/pull/1284>`_) (`3a723252 <https://github.com/PyGithub/PyGithub/commit/3a723252>`_)

Version 1.44.1 (November 07, 2019)
-----------------------------------

* Add Python 3.8 to classifiers list (`#1280 <https://github.com/PyGithub/PyGithub/pull/1280>`_) (`fec6034a <https://github.com/PyGithub/PyGithub/commit/fec6034a>`_)
* Expand Topic class and add test coverage (`#1252 <https://github.com/PyGithub/PyGithub/pull/1252>`_) (`ac682742 <https://github.com/PyGithub/PyGithub/commit/ac682742>`_)
* Add support for team discussions (`#1246 <https://github.com/PyGithub/PyGithub/pull/1246>`_) (#1249) (`ec3c8d7b <https://github.com/PyGithub/PyGithub/commit/ec3c8d7b>`_)
* Correct API for NamedUser.get_organization_membership (`#1277 <https://github.com/PyGithub/PyGithub/pull/1277>`_) (`077c80ba <https://github.com/PyGithub/PyGithub/commit/077c80ba>`_)
* Correct header check for 2FA required (`#1274 <https://github.com/PyGithub/PyGithub/pull/1274>`_) (`6ad592b1 <https://github.com/PyGithub/PyGithub/commit/6ad592b1>`_)
* Use replay framework for Issue142 test (`#1271 <https://github.com/PyGithub/PyGithub/pull/1271>`_) (`4d258d93 <https://github.com/PyGithub/PyGithub/commit/4d258d93>`_)
* Sync httpretty version requirement with setup.py (`#1265 <https://github.com/PyGithub/PyGithub/pull/1265>`_) (`99d38468 <https://github.com/PyGithub/PyGithub/commit/99d38468>`_)
* Handle unicode strings when recording responses (`#1253 <https://github.com/PyGithub/PyGithub/pull/1253>`_) (#1254) (`faa1bbd6 <https://github.com/PyGithub/PyGithub/commit/faa1bbd6>`_)
* Add assignee removal/addition support to PRs (`#1241 <https://github.com/PyGithub/PyGithub/pull/1241>`_) (`a163ba15 <https://github.com/PyGithub/PyGithub/commit/a163ba15>`_)
* Check if the version is empty in manage.sh (`#1268 <https://github.com/PyGithub/PyGithub/pull/1268>`_) (`db294837 <https://github.com/PyGithub/PyGithub/commit/db294837>`_)
* Encode content for {create,update}_file (`#1267 <https://github.com/PyGithub/PyGithub/pull/1267>`_) (`bc225f9d <https://github.com/PyGithub/PyGithub/commit/bc225f9d>`_)
* Update changes.rst (`#1263 <https://github.com/PyGithub/PyGithub/pull/1263>`_) (`d7947d82 <https://github.com/PyGithub/PyGithub/commit/d7947d82>`_)

Version 1.44 (October 19, 2019)
-----------------------------------

New features
^^^^^^^^^^^^

* This version supports running under Python 3 directly, and the test suite
  passes under both 2.7 and recent 3.x's.

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Stop ignoring unused imports and remove them (`#1250 <https://github.com/PyGithub/PyGithub/pull/1250>`_) (`a0765083 <https://github.com/PyGithub/PyGithub/commit/a0765083>`_)
* Bump httpretty to be a greater or equal to (`#1262 <https://github.com/PyGithub/PyGithub/pull/1262>`_) (`27092fb0 <https://github.com/PyGithub/PyGithub/commit/27092fb0>`_)
* Add close all issues example (`#1256 <https://github.com/PyGithub/PyGithub/pull/1256>`_) (`13e2c7c7 <https://github.com/PyGithub/PyGithub/commit/13e2c7c7>`_)
* Add six to install_requires (`#1245 <https://github.com/PyGithub/PyGithub/pull/1245>`_) (`a840a906 <https://github.com/PyGithub/PyGithub/commit/a840a906>`_)
* Implemented user organization membership. Added test case. (`#1237 <https://github.com/PyGithub/PyGithub/pull/1237>`_) (`e50420f7 <https://github.com/PyGithub/PyGithub/commit/e50420f7>`_)
* Create DEPLOY.md (`c9ed82b2 <https://github.com/PyGithub/PyGithub/commit/c9ed82b2>`_)
* Support non-default URLs in GithubIntegration (`#1229 <https://github.com/PyGithub/PyGithub/pull/1229>`_) (`e33858a3 <https://github.com/PyGithub/PyGithub/commit/e33858a3>`_)
* Cleanup try/except import in PaginatedList (`#1228 <https://github.com/PyGithub/PyGithub/pull/1228>`_) (`89c967bb <https://github.com/PyGithub/PyGithub/commit/89c967bb>`_)
* Add an IncompletableObject exception (`#1227 <https://github.com/PyGithub/PyGithub/pull/1227>`_) (`f91cbac2 <https://github.com/PyGithub/PyGithub/commit/f91cbac2>`_)
* Fix redundant int checks (`#1226 <https://github.com/PyGithub/PyGithub/pull/1226>`_) (`850da5af <https://github.com/PyGithub/PyGithub/commit/850da5af>`_)
* Jump from notifications to related PRs/issues. (`#1168 <https://github.com/PyGithub/PyGithub/pull/1168>`_) (`020fbebc <https://github.com/PyGithub/PyGithub/commit/020fbebc>`_)
* Code review bodies are optional in some cases. (`#1169 <https://github.com/PyGithub/PyGithub/pull/1169>`_) (`b84d9b19 <https://github.com/PyGithub/PyGithub/commit/b84d9b19>`_)
* Update changes.rst (`#1223 <https://github.com/PyGithub/PyGithub/pull/1223>`_) (`2df7269a <https://github.com/PyGithub/PyGithub/commit/2df7269a>`_)
* Do not auto-close issues with high priority tag (`ab27ba4d <https://github.com/PyGithub/PyGithub/commit/ab27ba4d>`_)
* Fix bug in repository create new file example PyGithub#1210 (`#1211 <https://github.com/PyGithub/PyGithub/pull/1211>`_) (`74cd6856 <https://github.com/PyGithub/PyGithub/commit/74cd6856>`_)
* Remove more Python version specific code (`#1193 <https://github.com/PyGithub/PyGithub/pull/1193>`_) (`a0f01cf9 <https://github.com/PyGithub/PyGithub/commit/a0f01cf9>`_)
* Drop use of assertEquals (`#1194 <https://github.com/PyGithub/PyGithub/pull/1194>`_) (`7bac694a <https://github.com/PyGithub/PyGithub/commit/7bac694a>`_)
* Fix PR review creation. (`#1184 <https://github.com/PyGithub/PyGithub/pull/1184>`_) (`e90cdab0 <https://github.com/PyGithub/PyGithub/commit/e90cdab0>`_)
* Add support to vulnerability alert and automated security fixes APIs (`#1195 <https://github.com/PyGithub/PyGithub/pull/1195>`_) (`8abd50e2 <https://github.com/PyGithub/PyGithub/commit/8abd50e2>`_)
* Delete Legacy submodule (`#1192 <https://github.com/PyGithub/PyGithub/pull/1192>`_) (`7ddb657d <https://github.com/PyGithub/PyGithub/commit/7ddb657d>`_)
* Remove some uses of atLeastPython3 (`#1191 <https://github.com/PyGithub/PyGithub/pull/1191>`_) (`cca8e3a5 <https://github.com/PyGithub/PyGithub/commit/cca8e3a5>`_)
* Run flake8 in Travis (`#1163 <https://github.com/PyGithub/PyGithub/pull/1163>`_) (`f93207b4 <https://github.com/PyGithub/PyGithub/commit/f93207b4>`_)
* Fix directories for coverage in Travis (`#1190 <https://github.com/PyGithub/PyGithub/pull/1190>`_) (`657f87b5 <https://github.com/PyGithub/PyGithub/commit/657f87b5>`_)
* Switch to using six (`#1189 <https://github.com/PyGithub/PyGithub/pull/1189>`_) (`dc2f2ad8 <https://github.com/PyGithub/PyGithub/commit/dc2f2ad8>`_)
* Update Repository.update_file() docstring (`#1186 <https://github.com/PyGithub/PyGithub/pull/1186>`_) (`f1ae7200 <https://github.com/PyGithub/PyGithub/commit/f1ae7200>`_)
* Correct return type of MainClass.get_organizations (`#1179 <https://github.com/PyGithub/PyGithub/pull/1179>`_) (`6e79d270 <https://github.com/PyGithub/PyGithub/commit/6e79d270>`_)
* Add cryptography to test-requirements.txt (`#1165 <https://github.com/PyGithub/PyGithub/pull/1165>`_) (`9b1c1e09 <https://github.com/PyGithub/PyGithub/commit/9b1c1e09>`_)

Version 1.43.8 (July 20, 2019)
-----------------------------------

New features
^^^^^^^^^^^^

* Add two factor attributes on organizations (`#1132 <https://github.com/PyGithub/PyGithub/pull/1132>`_) (`a0731685 <https://github.com/PyGithub/PyGithub/commit/a0731685>`_)
* Add Repository methods for pending invitations (`#1159 <https://github.com/PyGithub/PyGithub/pull/1159>`_) (`57af1e05 <https://github.com/PyGithub/PyGithub/commit/57af1e05>`_)
* Adds `get_issue_events` to `PullRequest` object (`#1154 <https://github.com/PyGithub/PyGithub/pull/1154>`_) (`acd515aa <https://github.com/PyGithub/PyGithub/commit/acd515aa>`_)
* Add invitee and inviter to Invitation (`#1156 <https://github.com/PyGithub/PyGithub/pull/1156>`_) (`0f2beaca <https://github.com/PyGithub/PyGithub/commit/0f2beaca>`_)
* Adding support for pending team invitations (`#993 <https://github.com/PyGithub/PyGithub/pull/993>`_) (`edab176b <https://github.com/PyGithub/PyGithub/commit/edab176b>`_)
* Add support for custom base_url in GithubIntegration class (`#1093 <https://github.com/PyGithub/PyGithub/pull/1093>`_) (`6cd0d644 <https://github.com/PyGithub/PyGithub/commit/6cd0d644>`_)
* GithubIntegration: enable getting installation (`#1135 <https://github.com/PyGithub/PyGithub/pull/1135>`_) (`18187045 <https://github.com/PyGithub/PyGithub/commit/18187045>`_)
* Add sorting capability to Organization.get_repos() (`#1139 <https://github.com/PyGithub/PyGithub/pull/1139>`_) (`ef6f009d <https://github.com/PyGithub/PyGithub/commit/ef6f009d>`_)
* Add new Organization.get_team_by_slug method (`#1144 <https://github.com/PyGithub/PyGithub/pull/1144>`_) (`4349bca1 <https://github.com/PyGithub/PyGithub/commit/4349bca1>`_)
* Add description field when creating a new team (`#1125 <https://github.com/PyGithub/PyGithub/pull/1125>`_) (`4a37860b <https://github.com/PyGithub/PyGithub/commit/4a37860b>`_)
* Handle a path of / in Repository.get_contents() (`#1070 <https://github.com/PyGithub/PyGithub/pull/1070>`_) (`102c8208 <https://github.com/PyGithub/PyGithub/commit/102c8208>`_)
* Add issue lock/unlock (`#1107 <https://github.com/PyGithub/PyGithub/pull/1107>`_) (`ec7bbcf5 <https://github.com/PyGithub/PyGithub/commit/ec7bbcf5>`_)

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Fix bug in recursive repository contents example (`#1166 <https://github.com/PyGithub/PyGithub/pull/1166>`_) (`8b6b4505 <https://github.com/PyGithub/PyGithub/commit/8b6b4505>`_)
* Allow name to be specified for upload_asset (`#1151 <https://github.com/PyGithub/PyGithub/pull/1151>`_) (`8d2a6b53 <https://github.com/PyGithub/PyGithub/commit/8d2a6b53>`_)
* Fixes #1106 for GitHub Enterprise API (`#1110 <https://github.com/PyGithub/PyGithub/pull/1110>`_) (`54065792 <https://github.com/PyGithub/PyGithub/commit/54065792>`_)

Deprecation
^^^^^^^^^^^

* Repository.get_file_contents() no longer works use Repository.get_contents() instead

Version 1.43.7 (April 16, 2019)
-----------------------------------

* Exclude tests from PyPI distribution (`#1031 <https://github.com/PyGithub/PyGithub/pull/1031>`_) (`78d283b9 <https://github.com/PyGithub/PyGithub/commit/78d283b9>`_)
* Add codecov badge (`#1090 <https://github.com/PyGithub/PyGithub/pull/1090>`_) (`4c0b54c0 <https://github.com/PyGithub/PyGithub/commit/4c0b54c0>`_)

Version 1.43.6 (April 05, 2019)
-----------------------------------

New features
^^^^^^^^^^^^

* Add support for Python 3.7 (`#1028 <https://github.com/PyGithub/PyGithub/pull/1028>`_) (`6faa00ac <https://github.com/PyGithub/PyGithub/commit/6faa00ac>`_)
* Adding HTTP retry functionality via urllib3 (`#1002 <https://github.com/PyGithub/PyGithub/pull/1002>`_) (`5ae7af55 <https://github.com/PyGithub/PyGithub/commit/5ae7af55>`_)
* Add new dismiss() method on PullRequestReview (`#1053 <https://github.com/PyGithub/PyGithub/pull/1053>`_) (`8ef71b1b <https://github.com/PyGithub/PyGithub/commit/8ef71b1b>`_)
* Add since and before to `get_notifications` (`#1074 <https://github.com/PyGithub/PyGithub/pull/1074>`_) (`7ee6c417 <https://github.com/PyGithub/PyGithub/commit/7ee6c417>`_)
* Add url parameter to include anonymous contributors in `get_contributors` (`#1075 <https://github.com/PyGithub/PyGithub/pull/1075>`_) (`293846be <https://github.com/PyGithub/PyGithub/commit/293846be>`_)
* Provide option to extend expiration of jwt token (`#1068 <https://github.com/PyGithub/PyGithub/pull/1068>`_) (`86a9d8e9 <https://github.com/PyGithub/PyGithub/commit/86a9d8e9>`_)

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Fix the default parameter for `PullRequest.create_review` (`#1058 <https://github.com/PyGithub/PyGithub/pull/1058>`_) (`118def30 <https://github.com/PyGithub/PyGithub/commit/118def30>`_)
* Fix `get_access_token` (`#1042 <https://github.com/PyGithub/PyGithub/pull/1042>`_) (`6a89eb64 <https://github.com/PyGithub/PyGithub/commit/6a89eb64>`_)
* Fix `Organization.add_to_members` role passing (`#1039 <https://github.com/PyGithub/PyGithub/pull/1039>`_) (`480f91cf <https://github.com/PyGithub/PyGithub/commit/480f91cf>`_)

Deprecation
^^^^^^^^^^^

* Remove Status API (`6efd6318 <https://github.com/PyGithub/PyGithub/commit/6efd6318>`_)

Version 1.43.5 (January 29, 2019)
-----------------------------------

* Add project column create card (`#1003 <https://github.com/PyGithub/PyGithub/pull/1003>`_) (`5f5c2764 <https://github.com/PyGithub/PyGithub/commit/5f5c2764>`_)
* Fix request got an unexpected keyword argument body (`#1012 <https://github.com/PyGithub/PyGithub/pull/1012>`_) (`ff789dcc <https://github.com/PyGithub/PyGithub/commit/ff789dcc>`_)
* Add missing import to PullRequest (`#1007 <https://github.com/PyGithub/PyGithub/pull/1007>`_) (`b5122768 <https://github.com/PyGithub/PyGithub/commit/b5122768>`_)

Version 1.43.4 (December 21, 2018)
-----------------------------------

New features
^^^^^^^^^^^^

* Add Migration API (`#899 <https://github.com/PyGithub/PyGithub/pull/899>`_) (`b4d895ed <https://github.com/PyGithub/PyGithub/commit/b4d895ed>`_)
* Add Traffic API (`#977 <https://github.com/PyGithub/PyGithub/pull/977>`_) (`a433a2fe <https://github.com/PyGithub/PyGithub/commit/a433a2fe>`_)
* New in Project API: create repository project, create project column (`#995 <https://github.com/PyGithub/PyGithub/pull/995>`_) (`1c0fd97d <https://github.com/PyGithub/PyGithub/commit/1c0fd97d>`_)

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Change type of GitRelease.author to NamedUser (`#969 <https://github.com/PyGithub/PyGithub/pull/969>`_) (`aca50a75 <https://github.com/PyGithub/PyGithub/commit/aca50a75>`_)
* Use total_count from data in PaginatedList (`#963 <https://github.com/PyGithub/PyGithub/pull/963>`_) (`ec177610 <https://github.com/PyGithub/PyGithub/commit/ec177610>`_)

Version 1.43.3 (October 31, 2018)
-----------------------------------

New features
^^^^^^^^^^^^

* Add support for JWT authentication (`#948 <https://github.com/PyGithub/PyGithub/pull/948>`_) (`8ccf9a94 <https://github.com/PyGithub/PyGithub/commit/8ccf9a94>`_)
* Added support for required signatures on protected branches (`#939 <https://github.com/PyGithub/PyGithub/pull/939>`_) (`8ee75a28 <https://github.com/PyGithub/PyGithub/commit/8ee75a28>`_)
* Ability to filter repository collaborators (`#938 <https://github.com/PyGithub/PyGithub/pull/938>`_) (`5687226b <https://github.com/PyGithub/PyGithub/commit/5687226b>`_)
* Mark notification as read (`#932 <https://github.com/PyGithub/PyGithub/pull/932>`_) (`0a10d7cd <https://github.com/PyGithub/PyGithub/commit/0a10d7cd>`_)
* Add highlight search to ``search_code`` function (`#925 <https://github.com/PyGithub/PyGithub/pull/925>`_) (`1fa25670 <https://github.com/PyGithub/PyGithub/commit/1fa25670>`_)
* Adding ``suspended_at`` property to NamedUSer (`#922 <https://github.com/PyGithub/PyGithub/pull/922>`_) (`c13b43ea <https://github.com/PyGithub/PyGithub/commit/c13b43ea>`_)
* Add since parameter for Gists (`#914 <https://github.com/PyGithub/PyGithub/pull/914>`_) (`e18b1078 <https://github.com/PyGithub/PyGithub/commit/e18b1078>`_)

Bug Fixes & Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

* Fix missing parameters when reversing ``PaginatedList`` (`#946 <https://github.com/PyGithub/PyGithub/pull/946>`_) (`60a684c5 <https://github.com/PyGithub/PyGithub/commit/60a684c5>`_)
* Fix unable to trigger ``RateLimitExceededException``. (`#943 <https://github.com/PyGithub/PyGithub/pull/943>`_) (`972446d5 <https://github.com/PyGithub/PyGithub/commit/972446d5>`_)
* Fix inconsistent behavior of trailing slash usage in file path (`#931 <https://github.com/PyGithub/PyGithub/pull/931>`_) (`ee9f098d <https://github.com/PyGithub/PyGithub/commit/ee9f098d>`_)
* Fix handling of 301 redirects (`#916 <https://github.com/PyGithub/PyGithub/pull/916>`_) (`6833245d <https://github.com/PyGithub/PyGithub/commit/6833245d>`_)
* Fix missing attributes of ``get_repos`` for authenticated users (`#915 <https://github.com/PyGithub/PyGithub/pull/915>`_) (`c411196f <https://github.com/PyGithub/PyGithub/commit/c411196f>`_)
* Fix ``Repository.edit`` (`#904 <https://github.com/PyGithub/PyGithub/pull/904>`_) (`7286eec0 <https://github.com/PyGithub/PyGithub/commit/7286eec0>`_)
* Improve ``__repr__`` method of Milestone class (`#921 <https://github.com/PyGithub/PyGithub/pull/921>`_) (`562908cb <https://github.com/PyGithub/PyGithub/commit/562908cb>`_)
* Fix rate limit documentation change (`#902 <https://github.com/PyGithub/PyGithub/pull/902>`_) (`974d1ec5 <https://github.com/PyGithub/PyGithub/commit/974d1ec5>`_)
* Fix comments not posted in create_review() (`#909 <https://github.com/PyGithub/PyGithub/pull/909>`_) (`a18eeb3a <https://github.com/PyGithub/PyGithub/commit/a18eeb3a>`_)

Version 1.43.2 (September 12, 2018)
-----------------------------------

* Restore ``RateLimit.rate`` attribute, raise deprecation warning instead (`d92389be <https://github.com/PyGithub/PyGithub/commit/d92389be>`_)

Version 1.43.1 (September 11, 2018)
-----------------------------------

New feature:

* Add support for Projects (`#854 <https://github.com/PyGithub/PyGithub/pull/854>`_) (`faca4ce1 <https://github.com/PyGithub/PyGithub/commit/faca4ce1>`_)

Version 1.43 (September 08, 2018)
-----------------------------------


Bug Fixes
^^^^^^^^^

* ``Repository.get_archive_link`` will now NOT follow HTTP redirect and return the url instead (`#858 <https://github.com/PyGithub/PyGithub/pull/858>`_) (`43d325a5 <https://github.com/PyGithub/PyGithub/commit/43d325a5>`_)
* Fixed ``Gistfile.content`` (`#486 <https://github.com/PyGithub/PyGithub/pull/486>`_) (`e1df09f7 <https://github.com/PyGithub/PyGithub/commit/e1df09f7>`_)
* Restored NamedUser.contributions attribute (`#865 <https://github.com/PyGithub/PyGithub/pull/865>`_) (`b91dee8d <https://github.com/PyGithub/PyGithub/commit/b91dee8d>`_)

New features
^^^^^^^^^^^^

* Add support for repository topics (`#832 <https://github.com/PyGithub/PyGithub/pull/832>`_) (`c6802b51 <https://github.com/PyGithub/PyGithub/commit/c6802b51>`_)
* Add support for required approving review count (`#888 <https://github.com/PyGithub/PyGithub/pull/888>`_) (ef16702)
* Add ``Organization.invite_user`` (880)(eb80564)
* Add support for search/graphql rate limit (fd8a036)

  + Deprecated ``RateLimit.rate``
  + Add `RateLimit.core <https://pygithub.readthedocs.io/en/latest/github_objects/RateLimit.html#github.RateLimit.RateLimit.core>`__, `RateLimit.search <https://pygithub.readthedocs.io/en/latest/github_objects/RateLimit.html#github.RateLimit.RateLimit.search>`__ and `RateLimit.graphql <https://pygithub.readthedocs.io/en/latest/github_objects/RateLimit.html#github.RateLimit.RateLimit.graphql>`__
* Add Support search by topics (`#893 <https://github.com/PyGithub/PyGithub/pull/893>`_) (3ce0418)
* Branch Protection API overhaul (`#790 <https://github.com/PyGithub/PyGithub/pull/790>`_) (`171cc567 <https://github.com/PyGithub/PyGithub/commit/171cc567>`_)

  + (**breaking**) Removed Repository.protect_branch
  + Add `BranchProtection <https://pygithub.readthedocs.io/en/latest/github_objects/BranchProtection.html>`__
  + Add `RequiredPullRequestReviews <https://pygithub.readthedocs.io/en/latest/github_objects/RequiredPullRequestReviews.html>`__
  + Add `RequiredStatusChecks <https://pygithub.readthedocs.io/en/latest/github_objects/RequiredStatusChecks.html>`__
  + Add ``Branch.get_protection``, ``Branch.get_required_pull_request_reviews``, ``Branch.get_required_status_checks``, etc

Improvements
^^^^^^^^^^^^

* Add missing arguments to ``Repository.edit`` (`#844 <https://github.com/PyGithub/PyGithub/pull/844>`_) (`29d23151 <https://github.com/PyGithub/PyGithub/commit/29d23151>`_)
* Add missing attributes to Repository (`#842 <https://github.com/PyGithub/PyGithub/pull/842>`_) (`2b352fb3 <https://github.com/PyGithub/PyGithub/commit/2b352fb3>`_)
* Adding archival support for ``Repository.edit`` (`#843 <https://github.com/PyGithub/PyGithub/pull/843>`_) (`1a90f5db <https://github.com/PyGithub/PyGithub/commit/1a90f5db>`_)
* Add ``tag_name`` and ``target_commitish`` arguments to ``GitRelease.update_release`` (`#834 <https://github.com/PyGithub/PyGithub/pull/834>`_) (`790f7dae <https://github.com/PyGithub/PyGithub/commit/790f7dae>`_)
* Allow editing of Team descriptions (`#839 <https://github.com/PyGithub/PyGithub/pull/839>`_) (`c0021747 <https://github.com/PyGithub/PyGithub/commit/c0021747>`_)
* Add description to Organizations (`#838 <https://github.com/PyGithub/PyGithub/pull/838>`_) (`1d918809 <https://github.com/PyGithub/PyGithub/commit/1d918809>`_)
* Add missing attributes for IssueEvent (`#857 <https://github.com/PyGithub/PyGithub/pull/857>`_) (7ac2a2a)
* Change ``MainClass.get_repo`` default laziness (`#882 <https://github.com/PyGithub/PyGithub/pull/882>`_) (6732517)

Deprecation
^^^^^^^^^^^

* Removed Repository.get_protected_branch (`#871 <https://github.com/PyGithub/PyGithub/pull/871>`_) (49db6f8)


Version 1.42 (August 19, 2018)
-----------------------------------

* Fix travis upload issue

Bug Fixes
^^^^^^^^^

* ``Repository.get_archive_link`` will now NOT follow HTTP redirect and return the url instead (`#858 <https://github.com/PyGithub/PyGithub/pull/858>`_) (`43d325a5 <https://github.com/PyGithub/PyGithub/commit/43d325a5>`_)
* Fixed ``Gistfile.content`` (`#486 <https://github.com/PyGithub/PyGithub/pull/486>`_) (`e1df09f7 <https://github.com/PyGithub/PyGithub/commit/e1df09f7>`_)
* Restored NamedUser.contributions attribute (`#865 <https://github.com/PyGithub/PyGithub/pull/865>`_) (`b91dee8d <https://github.com/PyGithub/PyGithub/commit/b91dee8d>`_)

New features

* Add support for repository topics (`#832 <https://github.com/PyGithub/PyGithub/pull/832>`_) (`c6802b51 <https://github.com/PyGithub/PyGithub/commit/c6802b51>`_)
* Branch Protection API overhaul (`#790 <https://github.com/PyGithub/PyGithub/pull/790>`_) (`171cc567 <https://github.com/PyGithub/PyGithub/commit/171cc567>`_)

  + (**breaking**) Removed Repository.protect_branch
  + Add `BranchProtection <https://pygithub.readthedocs.io/en/latest/github_objects/BranchProtection.html>`__
  + Add `RequiredPullRequestReviews <https://pygithub.readthedocs.io/en/latest/github_objects/RequiredPullRequestReviews.html>`__
  + Add `RequiredStatusChecks <https://pygithub.readthedocs.io/en/latest/github_objects/RequiredStatusChecks.html>`__
  + Add ``Branch.get_protection``, ``Branch.get_required_pull_request_reviews``, ``Branch.get_required_status_checks``, etc

Improvements

* Add missing arguments to ``Repository.edit`` (`#844 <https://github.com/PyGithub/PyGithub/pull/844>`_) (`29d23151 <https://github.com/PyGithub/PyGithub/commit/29d23151>`_)
* Add missing properties to Repository (`#842 <https://github.com/PyGithub/PyGithub/pull/842>`_) (`2b352fb3 <https://github.com/PyGithub/PyGithub/commit/2b352fb3>`_)
* Adding archival support for ``Repository.edit`` (`#843 <https://github.com/PyGithub/PyGithub/pull/843>`_) (`1a90f5db <https://github.com/PyGithub/PyGithub/commit/1a90f5db>`_)
* Add ``tag_name`` and ``target_commitish`` arguments to ``GitRelease.update_release`` (`#834 <https://github.com/PyGithub/PyGithub/pull/834>`_) (`790f7dae <https://github.com/PyGithub/PyGithub/commit/790f7dae>`_)
* Allow editing of Team descriptions (`#839 <https://github.com/PyGithub/PyGithub/pull/839>`_) (`c0021747 <https://github.com/PyGithub/PyGithub/commit/c0021747>`_)
* Add description to Organizations (`#838 <https://github.com/PyGithub/PyGithub/pull/838>`_) (`1d918809 <https://github.com/PyGithub/PyGithub/commit/1d918809>`_)

Version 1.41 (August 19, 2018)
-----------------------------------

Bug Fixes
^^^^^^^^^

* ``Repository.get_archive_link`` will now NOT follow HTTP redirect and return the url instead (`#858 <https://github.com/PyGithub/PyGithub/pull/858>`_) (`43d325a5 <https://github.com/PyGithub/PyGithub/commit/43d325a5>`_)
* Fixed ``Gistfile.content`` (`#486 <https://github.com/PyGithub/PyGithub/pull/486>`_) (`e1df09f7 <https://github.com/PyGithub/PyGithub/commit/e1df09f7>`_)
* Restored NamedUser.contributions attribute (`#865 <https://github.com/PyGithub/PyGithub/pull/865>`_) (`b91dee8d <https://github.com/PyGithub/PyGithub/commit/b91dee8d>`_)

New features

* Add support for repository topics (`#832 <https://github.com/PyGithub/PyGithub/pull/832>`_) (`c6802b51 <https://github.com/PyGithub/PyGithub/commit/c6802b51>`_)
* Branch Protection API overhaul (`#790 <https://github.com/PyGithub/PyGithub/pull/790>`_) (`171cc567 <https://github.com/PyGithub/PyGithub/commit/171cc567>`_)

  + (**breaking**) Removed Repository.protect_branch
  + Add `BranchProtection <https://pygithub.readthedocs.io/en/latest/github_objects/BranchProtection.html>`__
  + Add `RequiredPullRequestReviews <https://pygithub.readthedocs.io/en/latest/github_objects/RequiredPullRequestReviews.html>`__
  + Add `RequiredStatusChecks <https://pygithub.readthedocs.io/en/latest/github_objects/RequiredStatusChecks.html>`__
  + Add ``Branch.get_protection``, ``Branch.get_required_pull_request_reviews``, ``Branch.get_required_status_checks``, etc

Improvements

* Add missing arguments to ``Repository.edit`` (`#844 <https://github.com/PyGithub/PyGithub/pull/844>`_) (`29d23151 <https://github.com/PyGithub/PyGithub/commit/29d23151>`_)
* Add missing properties to Repository (`#842 <https://github.com/PyGithub/PyGithub/pull/842>`_) (`2b352fb3 <https://github.com/PyGithub/PyGithub/commit/2b352fb3>`_)
* Adding archival support for ``Repository.edit`` (`#843 <https://github.com/PyGithub/PyGithub/pull/843>`_) (`1a90f5db <https://github.com/PyGithub/PyGithub/commit/1a90f5db>`_)
* Add ``tag_name`` and ``target_commitish`` arguments to ``GitRelease.update_release`` (`#834 <https://github.com/PyGithub/PyGithub/pull/834>`_) (`790f7dae <https://github.com/PyGithub/PyGithub/commit/790f7dae>`_)
* Allow editing of Team descriptions (`#839 <https://github.com/PyGithub/PyGithub/pull/839>`_) (`c0021747 <https://github.com/PyGithub/PyGithub/commit/c0021747>`_)
* Add description to Organizations (`#838 <https://github.com/PyGithub/PyGithub/pull/838>`_) (`1d918809 <https://github.com/PyGithub/PyGithub/commit/1d918809>`_)

Version 1.40 (June 26, 2018)
-----------------------------------
* Major enhancement: use requests for HTTP instead of httplib (`#664 <https://github.com/PyGithub/PyGithub/pull/664>`_) (`9aed19dd <https://github.com/PyGithub/PyGithub/commit/9aed19dd>`_)
* Test Framework improvement (`#795 <https://github.com/PyGithub/PyGithub/pull/795>`_) (`faa8f205 <https://github.com/PyGithub/PyGithub/commit/faa8f205>`_)
* Handle HTTP 202 HEAD & GET with a retry (`#791 <https://github.com/PyGithub/PyGithub/pull/791>`_) (`3aead158 <https://github.com/PyGithub/PyGithub/commit/3aead158>`_)
* Fix github API requests after asset upload (`#771 <https://github.com/PyGithub/PyGithub/pull/771>`_) (`8bdac23c <https://github.com/PyGithub/PyGithub/commit/8bdac23c>`_)
* Add remove_membership() method to Teams class (`#807 <https://github.com/PyGithub/PyGithub/pull/807>`_) (`817f2230 <https://github.com/PyGithub/PyGithub/commit/817f2230>`_)
* Add check-in to projects using PyGithub (`#814 <https://github.com/PyGithub/PyGithub/pull/814>`_) (`05f49a59 <https://github.com/PyGithub/PyGithub/commit/05f49a59>`_)
* Include target_commitish in GitRelease (`#788 <https://github.com/PyGithub/PyGithub/pull/788>`_) (`ba5bf2d7 <https://github.com/PyGithub/PyGithub/commit/ba5bf2d7>`_)
* Fix asset upload timeout, increase default timeout from 10s to 15s (`#793 <https://github.com/PyGithub/PyGithub/pull/793>`_) (`140c6480 <https://github.com/PyGithub/PyGithub/commit/140c6480>`_)
* Fix Team.description (`#797 <https://github.com/PyGithub/PyGithub/pull/797>`_) (`0e8ae376 <https://github.com/PyGithub/PyGithub/commit/0e8ae376>`_)
* Fix Content-Length invalid headers exception (`#787 <https://github.com/PyGithub/PyGithub/pull/787>`_) (`23395f5f <https://github.com/PyGithub/PyGithub/commit/23395f5f>`_)
* Remove NamedUser.contributions (`#774 <https://github.com/PyGithub/PyGithub/pull/774>`_) (`a519e467 <https://github.com/PyGithub/PyGithub/commit/a519e467>`_)
* Add ability to skip SSL cert verification for Github Enterprise (`#758 <https://github.com/PyGithub/PyGithub/pull/758>`_) (`85a9124b <https://github.com/PyGithub/PyGithub/commit/85a9124b>`_)
* Correct Repository.get_git_tree recursive use (`#767 <https://github.com/PyGithub/PyGithub/pull/767>`_) (`bd0cf309 <https://github.com/PyGithub/PyGithub/commit/bd0cf309>`_)
* Re-work PullRequest reviewer request (`#765 <https://github.com/PyGithub/PyGithub/pull/765>`_) (`e2e29918 <https://github.com/PyGithub/PyGithub/commit/e2e29918>`_)
* Add support for team privacy (`#763 <https://github.com/PyGithub/PyGithub/pull/763>`_) (`1f23c06a <https://github.com/PyGithub/PyGithub/commit/1f23c06a>`_)
* Add support for organization outside collaborators (`#533 <https://github.com/PyGithub/PyGithub/pull/533>`_) (`c4446996 <https://github.com/PyGithub/PyGithub/commit/c4446996>`_)
* PullRequest labels should use Issues URL (`#754 <https://github.com/PyGithub/PyGithub/pull/754>`_) (`678b6b20 <https://github.com/PyGithub/PyGithub/commit/678b6b20>`_)
* Support labels for PullRequests (`#752 <https://github.com/PyGithub/PyGithub/pull/752>`_) (`a308dc92 <https://github.com/PyGithub/PyGithub/commit/a308dc92>`_)
* Add get_organizations() (`#748 <https://github.com/PyGithub/PyGithub/pull/748>`_) (`1e0150b5 <https://github.com/PyGithub/PyGithub/commit/1e0150b5>`_)

Version 1.39 (April 10, 2018)
-----------------------------------

* Add documentation to github.Repository.Repository.create_git_release() (`#747 <https://github.com/PyGithub/PyGithub/pull/747>`_) (`a769c2ff <https://github.com/PyGithub/PyGithub/commit/a769c2ff>`_)
* Add add_to_members() and remove_from_membership() (`#741 <https://github.com/PyGithub/PyGithub/pull/741>`_) (`4da483d1 <https://github.com/PyGithub/PyGithub/commit/4da483d1>`_)
* Documentation: clarify semantics of get_comments (`#743 <https://github.com/PyGithub/PyGithub/pull/743>`_) (`fec3c943 <https://github.com/PyGithub/PyGithub/commit/fec3c943>`_)
* Add download_url to ContentFile, closes #575 (`ca6fbc45 <https://github.com/PyGithub/PyGithub/commit/ca6fbc45>`_)
* Add PullRequestComment.in_reply_to_id (`#718 <https://github.com/PyGithub/PyGithub/pull/718>`_) (`eaa6a508 <https://github.com/PyGithub/PyGithub/commit/eaa6a508>`_)
* Add team privacy parameter to create team (`#702 <https://github.com/PyGithub/PyGithub/pull/702>`_) (`5cb5ab71 <https://github.com/PyGithub/PyGithub/commit/5cb5ab71>`_)
* Implement License API (`#734 <https://github.com/PyGithub/PyGithub/pull/734>`_) (`b54ccc78 <https://github.com/PyGithub/PyGithub/commit/b54ccc78>`_)
* Fix delete method for RepositoryKey (`911bf615 <https://github.com/PyGithub/PyGithub/commit/911bf615>`_)
* Remove edit for UserKey (`722f2534 <https://github.com/PyGithub/PyGithub/commit/722f2534>`_)
* Labels API: support description (`#738 <https://github.com/PyGithub/PyGithub/pull/738>`_) (`42e75938 <https://github.com/PyGithub/PyGithub/commit/42e75938>`_)
* Added Issue.as_pull_request() and PullReqest.as_issue() (`#630 <https://github.com/PyGithub/PyGithub/pull/630>`_) (`6bf2acc7 <https://github.com/PyGithub/PyGithub/commit/6bf2acc7>`_)
* Documentation: sort the Github Objects (`#735 <https://github.com/PyGithub/PyGithub/pull/735>`_) (`1497e826 <https://github.com/PyGithub/PyGithub/commit/1497e826>`_)
* Add support for getting PR single review's comments. (`#670 <https://github.com/PyGithub/PyGithub/pull/670>`_) (`612c3500 <https://github.com/PyGithub/PyGithub/commit/612c3500>`_)
* Update the RepositoryKey class (`#530 <https://github.com/PyGithub/PyGithub/pull/530>`_) (`5e8c6832 <https://github.com/PyGithub/PyGithub/commit/5e8c6832>`_)
* Added since to PR review comments get (`#577 <https://github.com/PyGithub/PyGithub/pull/577>`_) (`d8508285 <https://github.com/PyGithub/PyGithub/commit/d8508285>`_)
* Remove some duplicate attributes introduced in #522 (`566b28d3 <https://github.com/PyGithub/PyGithub/commit/566b28d3>`_)
* Added tarball_url, zipball_url, prerelease and draft property (`#522 <https://github.com/PyGithub/PyGithub/pull/522>`_) (`c76e67b7 <https://github.com/PyGithub/PyGithub/commit/c76e67b7>`_)
* Source Import API (`#673 <https://github.com/PyGithub/PyGithub/pull/673>`_) (`864c663a <https://github.com/PyGithub/PyGithub/commit/864c663a>`_)

Version 1.38 (March 21, 2018)
-----------------------------------

* Updated readthedocs, PyPI to reflect latest version
* Added option to create review for Pull request (`#662 <https://github.com/PyGithub/PyGithub/pull/662>`_) (`162f0397 <https://github.com/PyGithub/PyGithub/commit/162f0397>`_)
* Depreciate legacy search API (`3cd176e3 <https://github.com/PyGithub/PyGithub/commit/3cd176e3>`_)
* Filter team members  by role (`#491 <https://github.com/PyGithub/PyGithub/pull/491>`_) (`10ee17a2 <https://github.com/PyGithub/PyGithub/commit/10ee17a2>`_)
* Add url attribute to PullRequestReview object (`#731 <https://github.com/PyGithub/PyGithub/pull/731>`_) (`0fb176fd <https://github.com/PyGithub/PyGithub/commit/0fb176fd>`_)
* Added target_commitish option to Repository.create_git_release() (`#625 <https://github.com/PyGithub/PyGithub/pull/625>`_) (`0f0a7d4e <https://github.com/PyGithub/PyGithub/commit/0f0a7d4e>`_)
* Fix broken Github reference link in class docstrings (`a32a17bf <https://github.com/PyGithub/PyGithub/commit/a32a17bf>`_)
* Add hook support for organizations (`#729 <https://github.com/PyGithub/PyGithub/pull/729>`_) (`c7f6563c <https://github.com/PyGithub/PyGithub/commit/c7f6563c>`_)
* Get organization from the team (`#590 <https://github.com/PyGithub/PyGithub/pull/590>`_) (`d9c5a07f <https://github.com/PyGithub/PyGithub/commit/d9c5a07f>`_)
* Added search_commits (`#727 <https://github.com/PyGithub/PyGithub/pull/727>`_) (`aa556f85 <https://github.com/PyGithub/PyGithub/commit/aa556f85>`_)
* Collaborator site admin (`#719 <https://github.com/PyGithub/PyGithub/pull/719>`_) (`f8b23505 <https://github.com/PyGithub/PyGithub/commit/f8b23505>`_)
* Fix add_to_watched for AuthenticatedUser (`#716 <https://github.com/PyGithub/PyGithub/pull/716>`_) (`6109eb3c <https://github.com/PyGithub/PyGithub/commit/6109eb3c>`_)

Version 1.37 (March 03, 2018)
-----------------------------------

* Add __eq__ and __hash__ to NamedUser (`#706 <https://github.com/PyGithub/PyGithub/pull/706>`_) (`8a13b274 <https://github.com/PyGithub/PyGithub/commit/8a13b274>`_)
* Add maintainer can modify flag to create pull request (`#703 <https://github.com/PyGithub/PyGithub/pull/703>`_) (`0e5a1d1d <https://github.com/PyGithub/PyGithub/commit/0e5a1d1d>`_)
* Fix typo in Design.md (`#701 <https://github.com/PyGithub/PyGithub/pull/701>`_) (`98d32af4 <https://github.com/PyGithub/PyGithub/commit/98d32af4>`_)
* Add role parameter to Team.add_membership method (`#638 <https://github.com/PyGithub/PyGithub/pull/638>`_) (`01ab4cc6 <https://github.com/PyGithub/PyGithub/commit/01ab4cc6>`_)
* Add add_membership testcase (`#637 <https://github.com/PyGithub/PyGithub/pull/637>`_) (`5a1424bb <https://github.com/PyGithub/PyGithub/commit/5a1424bb>`_)

Version 1.36 (February 02, 2018)
-----------------------------------

* Fix changelog generation (`5d911e22 <https://github.com/PyGithub/PyGithub/commit/5d911e22>`_)
* Add collaborator permission support (`#699 <https://github.com/PyGithub/PyGithub/pull/699>`_) (`167f85ef <https://github.com/PyGithub/PyGithub/commit/167f85ef>`_)
* Use datetime object in create_milestone (`#698 <https://github.com/PyGithub/PyGithub/pull/698>`_) (`cef98416 <https://github.com/PyGithub/PyGithub/commit/cef98416>`_)
* Fix date format for milestone creation (`#593 <https://github.com/PyGithub/PyGithub/pull/593>`_) (`e671fdd0 <https://github.com/PyGithub/PyGithub/commit/e671fdd0>`_)
* Remove the default "null" input send during GET request (`#691 <https://github.com/PyGithub/PyGithub/pull/691>`_) (`cbfe8d0f <https://github.com/PyGithub/PyGithub/commit/cbfe8d0f>`_)
* Updated PullRequest reviewer request according to API changes (`#690 <https://github.com/PyGithub/PyGithub/pull/690>`_) (`5c9c2f75 <https://github.com/PyGithub/PyGithub/commit/5c9c2f75>`_)
* make created_at/published_at attrs available for Release objects (`#689 <https://github.com/PyGithub/PyGithub/pull/689>`_) (`2f9b1e01 <https://github.com/PyGithub/PyGithub/commit/2f9b1e01>`_)
* Add committer/author to Repository.delete_file (`#678 <https://github.com/PyGithub/PyGithub/pull/678>`_) (`3baa682c <https://github.com/PyGithub/PyGithub/commit/3baa682c>`_)
* Add method to get latest release of a repository (`#609 <https://github.com/PyGithub/PyGithub/pull/609>`_) (`45d18436 <https://github.com/PyGithub/PyGithub/commit/45d18436>`_)
* Add permissions field to NamedUser (`#676 <https://github.com/PyGithub/PyGithub/pull/676>`_) (`6cfe46b7 <https://github.com/PyGithub/PyGithub/commit/6cfe46b7>`_)
* Fix all pep8 coding conventions (`6bc804dc <https://github.com/PyGithub/PyGithub/commit/6bc804dc>`_)
* Add new params for /users/:user/repos endpoint (`89834a9b <https://github.com/PyGithub/PyGithub/commit/89834a9b>`_)
* Add support for changing PR head commit (`#632 <https://github.com/PyGithub/PyGithub/pull/632>`_) (`3f77e537 <https://github.com/PyGithub/PyGithub/commit/3f77e537>`_)
* Use print() syntax in README (`#681 <https://github.com/PyGithub/PyGithub/pull/681>`_) (`c5988c39 <https://github.com/PyGithub/PyGithub/commit/c5988c39>`_)
* Add PyPI badge and installation instructions to README (`#682 <https://github.com/PyGithub/PyGithub/pull/682>`_) (`3726f686 <https://github.com/PyGithub/PyGithub/commit/3726f686>`_)
* Drop support for EOL Python 2.5-2.6 and 3.2-3.3 (`#674 <https://github.com/PyGithub/PyGithub/pull/674>`_) (`6735be49 <https://github.com/PyGithub/PyGithub/commit/6735be49>`_)
* Add Reactions feature (`#671 <https://github.com/PyGithub/PyGithub/pull/671>`_) (`ba50af53 <https://github.com/PyGithub/PyGithub/commit/ba50af53>`_)
* Add ping_url and ping to Hook (`#669 <https://github.com/PyGithub/PyGithub/pull/669>`_) (`6169d8ea <https://github.com/PyGithub/PyGithub/commit/6169d8ea>`_)
* Add Repository.archived property (`#657 <https://github.com/PyGithub/PyGithub/pull/657>`_) (`35333e03 <https://github.com/PyGithub/PyGithub/commit/35333e03>`_)
* Add unit test for tree attribute of GitCommit (`#668 <https://github.com/PyGithub/PyGithub/pull/668>`_) (`e5bfdbeb <https://github.com/PyGithub/PyGithub/commit/e5bfdbeb>`_)
* Add read_only attribute to Deploy Keys (`#570 <https://github.com/PyGithub/PyGithub/pull/570>`_) (`dbc6f5ab <https://github.com/PyGithub/PyGithub/commit/dbc6f5ab>`_)
* Doc create instance from token (`#667 <https://github.com/PyGithub/PyGithub/pull/667>`_) (`c33a3883 <https://github.com/PyGithub/PyGithub/commit/c33a3883>`_)
* Fix uploading binary files on Python 3 (`#621 <https://github.com/PyGithub/PyGithub/pull/621>`_) (`317079ef <https://github.com/PyGithub/PyGithub/commit/317079ef>`_)
* Decode jwt bytes object in Python 3 (`#633 <https://github.com/PyGithub/PyGithub/pull/633>`_) (`84b43da7 <https://github.com/PyGithub/PyGithub/commit/84b43da7>`_)
* Remove broken downloads badge (`#644 <https://github.com/PyGithub/PyGithub/pull/644>`_) (`15cdc2f8 <https://github.com/PyGithub/PyGithub/commit/15cdc2f8>`_)
* Added missing parameters for repo creation (`#623 <https://github.com/PyGithub/PyGithub/pull/623>`_) (`5c41120a <https://github.com/PyGithub/PyGithub/commit/5c41120a>`_)
* Add ability to access github Release Asset API. (`#525 <https://github.com/PyGithub/PyGithub/pull/525>`_) (`52449649 <https://github.com/PyGithub/PyGithub/commit/52449649>`_)
* Add 'submitted at' to PullRequestReview (`#565 <https://github.com/PyGithub/PyGithub/pull/565>`_) (`ebe7277a <https://github.com/PyGithub/PyGithub/commit/ebe7277a>`_)
* Quote path for /contents API (`#614 <https://github.com/PyGithub/PyGithub/pull/614>`_) (`554c1ab1 <https://github.com/PyGithub/PyGithub/commit/554c1ab1>`_)
* Add Python 3.6 (`2533bed9 <https://github.com/PyGithub/PyGithub/commit/2533bed9>`_)
* Add Python 3.6 (`e78f0ece <https://github.com/PyGithub/PyGithub/commit/e78f0ece>`_)
* Updated references in introduction.rst (`d2c72bb3 <https://github.com/PyGithub/PyGithub/commit/d2c72bb3>`_)
* fix failing tests on py26 (`291f6dde <https://github.com/PyGithub/PyGithub/commit/291f6dde>`_)
* Import missing exception (`67b078e9 <https://github.com/PyGithub/PyGithub/commit/67b078e9>`_)

Version 1.35 (July 10, 2017)
-----------------------------------

* Add Support for repository collaborator invitations.

Version 1.34 (abril 04, 2017)
-----------------------------------

* Add Support for Pull Request Reviews feature.

Version 1.32 (February 1, 2017)
-----------------------------------

* Support for Integrations installation endpoint (`656e70e1 <https://github.com/PyGithub/PyGithub/commit/656e70e1>`_)

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
* Patch issue 358 status context (`#428 <https://github.com/PyGithub/PyGithub/pull/428>`_) (70e30c5)
* Adding "since" param to Issue.get_comments() (`#426 <https://github.com/PyGithub/PyGithub/pull/426>`_) (3c6f99f)
* update doc url everywhere (`#420 <https://github.com/PyGithub/PyGithub/pull/420>`_) (cb0cf0a)
* fix a couple typos to be clearer (`#419 <https://github.com/PyGithub/PyGithub/pull/419>`_) (23c0e75)
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
