You don't normaly create instances of any class but `Github`.
You obtain instances through calls to `search_`, `get_` and `create_` methods.

Methods returning an "iterator of `SomeType`" return an iterator which yields instances of `SomeType`.
This implements lazy [pagination requests](http://developer.github.com/v3/#pagination).
You can use this iterator in a `for f in user.get_followers():` loop or with any [itertools](http://docs.python.org/library/itertools.html) functions,
but you cannot know the number of objects returned before the end of the iteration.
If that's really what you need, you cant use `len( list( user.get_followers() ) )`, which does all the requests needed to enumerate the user's followers.
Note that there is often an attribute giving this value (in that case `user.followers`).

Class `Github`
==============

Constructed from user's login and password or OAuth token or nothing:

    g = Github( login, password )
    g = Github( token )
    g = Github()

You can add an argument `base_url = "http://my.enterprise.com:8080/path/to/github"` to connect to a local install of Github (ie. Github Enterprise).
Another argument, that can be passed is `timeout` which has default value `10`.

Attributes
----------
* `rate_limiting`: tuple of two integers: remaining and limit, as explained in [Rate Limiting](http://developer.github.com/v3/#rate-limiting)

Methods
-------
* `get_user()`: `AuthenticatedUser`
* `get_user( login )`: `NamedUser`
* `get_organization( login )`: `Organization`
* `get_gist( id )`: `Gist`
    * `id`: string
* `get_gists()`: iterator of `Gist`
* `get_hooks()`: iterator of `HookDescription`
* `search_repos( keyword )`: iterator of `Repository`
* `legacy_search_repos( keyword, [language] )`: iterator of `Repository`
    * `keyword`: string
    * `language`: string
* `legacy_search_users( keyword )`: iterator of `NamedUser`
    * `keyword`: string
* `legacy_search_user_by_email( email )`: `NamedUser`
    * `email`: string
* `render_markdown( text, [context] )`: string
    * `text`: string
    * `context`: `Repository`

Class `GithubException`
=======================

Attributes
----------
* `status`: integer
* `data`: dict

Class `AuthenticatedUser`
=========================

Attributes
----------
* `avatar_url`: string
* `bio`: string
* `blog`: string
* `collaborators`: integer
* `company`: string
* `created_at`: datetime.datetime
* `disk_usage`: integer
* `email`: string
* `followers`: integer
* `following`: integer
* `gravatar_id`: string
* `hireable`: bool
* `html_url`: string
* `id`: integer
* `location`: string
* `login`: string
* `name`: string
* `owned_private_repos`: integer
* `plan`: `Plan`
* `private_gists`: integer
* `public_gists`: integer
* `public_repos`: integer
* `total_private_repos`: integer
* `type`: string
* `url`: string

Authorizations
--------------
* `create_authorization( [scopes, note, note_url] )`: `Authorization`
    * `scopes`: list of string
    * `note`: string
    * `note_url`: string
* `get_authorization( id )`: `Authorization`
    * `id`: integer
* `get_authorizations()`: iterator of `Authorization`

Emails
------
* `add_to_emails( email, ... )`
    * `email`: string
* `get_emails()`: list of string
* `remove_from_emails( email, ... )`
    * `email`: string

Events
------
* `get_events()`: iterator of `Event`
* `get_organization_events( org )`: iterator of `Event`
    * `org`: `Organization`

Followers
---------
* `get_followers()`: iterator of `NamedUser`

Following
---------
* `add_to_following( following )`
    * `following`: `NamedUser`
* `get_following()`: iterator of `NamedUser`
* `has_in_following( following )`: bool
    * `following`: `NamedUser`
* `remove_from_following( following )`
    * `following`: `NamedUser`

Forking
-------
* `create_fork( repo )`: `Repository`
    * `repo`: `Repository`

Gists
-----
* `create_gist( public, files, [description] )`: `Gist`
    * `public`: bool
    * `files`: dict of string to `InputFileContent`
    * `description`: string
* `get_gists()`: iterator of `Gist`
* `get_starred_gists()`: iterator of `Gist`

Issues
------
* `get_issues()`: iterator of `Issue`

Keys
----
* `create_key( title, key )`: `UserKey`
    * `title`: string
    * `key`: string
* `get_key( id )`: `UserKey`
    * `id`: integer
* `get_keys()`: iterator of `UserKey`

Modification
------------
* `edit( [name, email, blog, company, location, hireable, bio] )`
    * `name`: string
    * `email`: string
    * `blog`: string
    * `company`: string
    * `location`: string
    * `hireable`: bool
    * `bio`: string

Orgs
----
* `get_orgs()`: iterator of `Organization`

Repos
-----
* `create_repo( name, [description, homepage, private, has_issues, has_wiki, has_downloads] )`: `Repository`
    * `name`: string
    * `description`: string
    * `homepage`: string
    * `private`: bool
    * `has_issues`: bool
    * `has_wiki`: bool
    * `has_downloads`: bool
* `get_repo( name )`: `Repository`
    * `name`: string
* `get_repos( [type, sort, direction] )`: iterator of `Repository`
    * `type`: string
    * `sort`: string
    * `direction`: string

Starred
-------
* `add_to_starred( starred )`
    * `starred`: `Repository`
* `get_starred()`: iterator of `Repository`
* `has_in_starred( starred )`: bool
    * `starred`: `Repository`
* `remove_from_starred( starred )`
    * `starred`: `Repository`

Subscriptions
-------------
* `add_to_subscriptions( subscription )`
    * `subscription`: `Repository`
* `get_subscriptions()`: iterator of `Repository`
* `has_in_subscriptions( subscription )`: bool
    * `subscription`: `Repository`
* `remove_from_subscriptions( subscription )`
    * `subscription`: `Repository`

Watched
-------
* `add_to_watched( watched )`
    * `watched`: `Repository`
* `get_watched()`: iterator of `Repository`
* `has_in_watched( watched )`: bool
    * `watched`: `Repository`
* `remove_from_watched( watched )`
    * `watched`: `Repository`

Class `Authorization`
=====================

Attributes
----------
* `app`: `AuthorizationApplication`
* `created_at`: datetime.datetime
* `id`: integer
* `note`: string
* `note_url`: string
* `scopes`: list of string
* `token`: string
* `updated_at`: datetime.datetime
* `url`: string

Deletion
--------
* `delete()`

Modification
------------
* `edit( [scopes, add_scopes, remove_scopes, note, note_url] )`
    * `scopes`: list of string
    * `add_scopes`: list of string
    * `remove_scopes`: list of string
    * `note`: string
    * `note_url`: string

Class `AuthorizationApplication`
================================

Attributes
----------
* `name`: string
* `url`: string

Class `Branch`
==============

Attributes
----------
* `commit`: `Commit`
* `name`: string

Class `Commit`
==============

Attributes
----------
* `author`: `NamedUser`
* `commit`: `GitCommit`
* `committer`: `NamedUser`
* `files`: list of `File`
* `parents`: list of `Commit`
* `sha`: string
* `stats`: `CommitStats`
* `url`: string

Comments
--------
* `create_comment( body, [line, path, position] )`: `CommitComment`
    * `body`: string
    * `line`: integer
    * `path`: string
    * `position`: integer
* `get_comments()`: iterator of `CommitComment`

Statuses
--------
* `create_status( state, [target_url, description] )`: `CommitStatus`
    * `state`: string
    * `target_url`: string
    * `description`: string
* `get_statuses()`: iterator of `CommitStatus`

Class `CommitComment`
=====================

Attributes
----------
* `body`: string
* `commit_id`: string
* `created_at`: datetime.datetime
* `html_url`: string
* `id`: integer
* `line`: integer
* `path`: string
* `position`: integer
* `updated_at`: datetime.datetime
* `url`: string
* `user`: `NamedUser`

Deletion
--------
* `delete()`

Modification
------------
* `edit( body )`
    * `body`: string

Class `CommitStats`
===================

Attributes
----------
* `additions`: integer
* `deletions`: integer
* `total`: integer

Class `CommitStatus`
====================

Attributes
----------
* `created_at`: datetime.datetime
* `creator`: `NamedUser`
* `description`: string
* `id`: integer
* `state`: string
* `target_url`: string
* `updated_at`: datetime.datetime

Class `Comparison`
==================

Attributes
----------
* `ahead_by`: integer
* `base_commit`: `Commit`
* `behind_by`: integer
* `commits`: list of `Commit`
* `diff_url`: string
* `files`: list of `File`
* `html_url`: string
* `patch_url`: string
* `permalink_url`: string
* `status`: string
* `total_commits`: integer
* `url`: string

Class `ContentFile`
===================

Attributes
----------
* `content`: string
* `encoding`: string
* `name`: string
* `path`: string
* `sha`: string
* `size`: integer
* `type`: string

Class `Download`
================

Attributes
----------
* `accesskeyid`: string
* `acl`: string
* `bucket`: string
* `content_type`: string
* `created_at`: datetime.datetime
* `description`: string
* `download_count`: integer
* `expirationdate`: datetime.datetime
* `html_url`: string
* `id`: integer
* `mime_type`: string
* `name`: string
* `path`: string
* `policy`: string
* `prefix`: string
* `redirect`: bool
* `s3_url`: string
* `signature`: string
* `size`: integer
* `url`: string

Deletion
--------
* `delete()`

Class `Event`
=============

Attributes
----------
* `actor`: `NamedUser`
* `created_at`: datetime.datetime
* `id`: string
* `org`: `Organization`
* `payload`: dict
* `public`: bool
* `repo`: `Repository`
* `type`: string

Class `File`
============

Attributes
----------
* `additions`: integer
* `blob_url`: string
* `changes`: integer
* `deletions`: integer
* `filename`: string
* `patch`: string
* `raw_url`: string
* `sha`: string
* `status`: string

Class `Gist`
============

Attributes
----------
* `comments`: integer
* `created_at`: datetime.datetime
* `description`: string
* `files`: dict of string to `GistFile`
* `fork_of`: `Gist`
* `forks`: list of `Gist`
* `git_pull_url`: string
* `git_push_url`: string
* `history`: list of `GistHistoryState`
* `html_url`: string
* `id`: string
* `public`: bool
* `updated_at`: datetime.datetime
* `url`: string
* `user`: `NamedUser`

Comments
--------
* `create_comment( body )`: `GistComment`
    * `body`: string
* `get_comment( id )`: `GistComment`
    * `id`: integer
* `get_comments()`: iterator of `GistComment`

Deletion
--------
* `delete()`

Forking
-------
* `create_fork()`: `Gist`

Modification
------------
* `edit( [description, files] )`
    * `description`: string
    * `files`: dict of string to `InputFileContent`

Starring
--------
* `is_starred()`: bool
* `reset_starred()`
* `set_starred()`

Class `GistComment`
===================

Attributes
----------
* `body`: string
* `created_at`: datetime.datetime
* `id`: integer
* `updated_at`: datetime.datetime
* `url`: string
* `user`: `NamedUser`

Deletion
--------
* `delete()`

Modification
------------
* `edit( body )`
    * `body`: string

Class `GistFile`
================

Attributes
----------
* `content`: string
* `filename`: string
* `language`: string
* `raw_url`: string
* `size`: integer

Class `GistHistoryState`
========================

Attributes
----------
* `change_status`: `CommitStats`
* `committed_at`: datetime.datetime
* `url`: string
* `user`: `NamedUser`
* `version`: string

Class `GitAuthor`
=================

Attributes
----------
* `date`: datetime.datetime
* `email`: string
* `name`: string

Class `GitBlob`
===============

Attributes
----------
* `content`: string
* `encoding`: string
* `sha`: string
* `size`: integer
* `url`: string

Class `GitCommit`
=================

Attributes
----------
* `author`: `GitAuthor`
* `committer`: `GitAuthor`
* `message`: string
* `parents`: list of `GitCommit`
* `sha`: string
* `tree`: `GitTree`
* `url`: string

Class `GitObject`
=================

Attributes
----------
* `sha`: string
* `type`: string
* `url`: string

Class `GitRef`
==============

Attributes
----------
* `object`: `GitObject`
* `ref`: string
* `url`: string

Deletion
--------
* `delete()`

Modification
------------
* `edit( sha, [force] )`
    * `sha`: string
    * `force`: bool

Class `GitTag`
==============

Attributes
----------
* `message`: string
* `object`: `GitObject`
* `sha`: string
* `tag`: string
* `tagger`: `GitAuthor`
* `url`: string

Class `GitTree`
===============

Attributes
----------
* `sha`: string
* `tree`: list of `GitTreeElement`
* `url`: string

Class `GitTreeElement`
======================

Attributes
----------
* `mode`: string
* `path`: string
* `sha`: string
* `size`: integer
* `type`: string
* `url`: string

Class `Hook`
============

Attributes
----------
* `active`: bool
* `config`: dict
* `created_at`: datetime.datetime
* `events`: list of string
* `id`: integer
* `last_response`: `HookResponse`
* `name`: string
* `updated_at`: datetime.datetime
* `url`: string

Deletion
--------
* `delete()`

Modification
------------
* `edit( name, config, [events, add_events, remove_events, active] )`
    * `name`: string
    * `config`: dict
    * `events`: list of string
    * `add_events`: list of string
    * `remove_events`: list of string
    * `active`: bool

Testing
-------
* `test()`

Class `HookDescription`
=======================

Attributes
----------
* `events`: list of string
* `name`: string
* `schema`: list of list of string
* `supported_events`: list of string

Class `HookResponse`
====================

Attributes
----------
* `code`: integer
* `message`: string
* `status`: string

Class `Issue`
=============

Attributes
----------
* `assignee`: `NamedUser`
* `body`: string
* `closed_at`: datetime.datetime
* `closed_by`: `NamedUser`
* `comments`: integer
* `created_at`: datetime.datetime
* `html_url`: string
* `id`: integer
* `labels`: list of `Label`
* `milestone`: `Milestone`
* `number`: integer
* `pull_request`: `IssuePullRequest`
* `repository`: `Repository`
* `state`: string
* `title`: string
* `updated_at`: datetime.datetime
* `url`: string
* `user`: `NamedUser`

Comments
--------
* `create_comment( body )`: `IssueComment`
    * `body`: string
* `get_comment( id )`: `IssueComment`
    * `id`: integer
* `get_comments()`: iterator of `IssueComment`

Events
------
* `get_events()`: iterator of `IssueEvent`

Labels
------
* `add_to_labels( label, ... )`
    * `label`: `Label`
* `delete_labels()`
* `get_labels()`: iterator of `Label`
* `remove_from_labels( label )`
    * `label`: `Label`
* `set_labels( label, ... )`
    * `label`: `Label`

Modification
------------
* `edit( [title, body, assignee, state, milestone, labels] )`
    * `title`: string
    * `body`: string
    * `assignee`: `NamedUser`
    * `state`: string
    * `milestone`: `Milestone`
    * `labels`: list of string

Class `IssueComment`
====================

Attributes
----------
* `body`: string
* `created_at`: datetime.datetime
* `id`: integer
* `updated_at`: datetime.datetime
* `url`: string
* `user`: `NamedUser`

Deletion
--------
* `delete()`

Modification
------------
* `edit( body )`
    * `body`: string

Class `IssueEvent`
==================

Attributes
----------
* `actor`: `NamedUser`
* `commit_id`: string
* `created_at`: datetime.datetime
* `event`: string
* `id`: integer
* `issue`: `Issue`
* `url`: string

Class `IssuePullRequest`
========================

Attributes
----------
* `diff_url`: string
* `html_url`: string
* `patch_url`: string

Class `Label`
=============

Attributes
----------
* `color`: string
* `name`: string
* `url`: string

Deletion
--------
* `delete()`

Modification
------------
* `edit( name, color )`
    * `name`: string
    * `color`: string

Class `Milestone`
=================

Attributes
----------
* `closed_issues`: integer
* `created_at`: datetime.datetime
* `creator`: `NamedUser`
* `description`: string
* `due_on`: datetime.datetime
* `id`: integer
* `number`: integer
* `open_issues`: integer
* `state`: string
* `title`: string
* `url`: string

Deletion
--------
* `delete()`

Labels
------
* `get_labels()`: iterator of `Label`

Modification
------------
* `edit( title, [state, description, due_on] )`
    * `title`: string
    * `state`: string
    * `description`: string
    * `due_on`: date

Class `NamedUser`
=================

Attributes
----------
* `avatar_url`: string
* `bio`: string
* `blog`: string
* `collaborators`: integer
* `company`: string
* `contributions`: integer
* `created_at`: datetime.datetime
* `disk_usage`: integer
* `email`: string
* `followers`: integer
* `following`: integer
* `gravatar_id`: string
* `hireable`: bool
* `html_url`: string
* `id`: integer
* `location`: string
* `login`: string
* `name`: string
* `owned_private_repos`: integer
* `plan`: `Plan`
* `private_gists`: integer
* `public_gists`: integer
* `public_repos`: integer
* `total_private_repos`: integer
* `type`: string
* `url`: string

Events
------
* `get_events()`: iterator of `Event`
* `get_public_events()`: iterator of `Event`
* `get_received_events()`: iterator of `Event`
* `get_public_received_events()`: iterator of `Event`

Followers
---------
* `get_followers()`: iterator of `NamedUser`

Following
---------
* `get_following()`: iterator of `NamedUser`

Gists
-----
* `create_gist( public, files, [description] )`: `Gist`
    * `public`: bool
    * `files`: dict of string to `InputFileContent`
    * `description`: string
* `get_gists()`: iterator of `Gist`

Orgs
----
* `get_orgs()`: iterator of `Organization`

Repos
-----
* `get_repo( name )`: `Repository`
    * `name`: string
* `get_repos( [type] )`: iterator of `Repository`
    * `type`: string

Starred
-------
* `get_starred()`: iterator of `Repository`

Subscriptions
-------------
* `get_subscriptions()`: iterator of `Repository`

Watched
-------
* `get_watched()`: iterator of `Repository`

Class `Organization`
====================

Attributes
----------
* `avatar_url`: string
* `billing_email`: string
* `blog`: string
* `collaborators`: integer
* `company`: string
* `created_at`: datetime.datetime
* `disk_usage`: integer
* `email`: string
* `followers`: integer
* `following`: integer
* `gravatar_id`: string
* `html_url`: string
* `id`: integer
* `location`: string
* `login`: string
* `name`: string
* `owned_private_repos`: integer
* `plan`: `Plan`
* `private_gists`: integer
* `public_gists`: integer
* `public_repos`: integer
* `total_private_repos`: integer
* `type`: string
* `url`: string

Events
------
* `get_events()`: iterator of `Event`

Forking
-------
* `create_fork( repo )`: `Repository`
    * `repo`: `Repository`

Members
-------
* `get_members()`: iterator of `NamedUser`
* `has_in_members( member )`: bool
    * `member`: `NamedUser`
* `remove_from_members( member )`
    * `member`: `NamedUser`

Modification
------------
* `edit( [billing_email, blog, company, email, location, name] )`
    * `billing_email`: string
    * `blog`: string
    * `company`: string
    * `email`: string
    * `location`: string
    * `name`: string

Public_members
--------------
* `add_to_public_members( public_member )`
    * `public_member`: `NamedUser`
* `get_public_members()`: iterator of `NamedUser`
* `has_in_public_members( public_member )`: bool
    * `public_member`: `NamedUser`
* `remove_from_public_members( public_member )`
    * `public_member`: `NamedUser`

Repos
-----
* `create_repo( name, [description, homepage, private, has_issues, has_wiki, has_downloads, team_id] )`: `Repository`
    * `name`: string
    * `description`: string
    * `homepage`: string
    * `private`: bool
    * `has_issues`: bool
    * `has_wiki`: bool
    * `has_downloads`: bool
    * `team_id`: `Team`
* `get_repo( name )`: `Repository`
    * `name`: string
* `get_repos( [type] )`: iterator of `Repository`
    * `type`: string

Teams
-----
* `create_team( name, [repo_names, permission] )`: `Team`
    * `name`: string
    * `repo_names`: list of `Repository`
    * `permission`: string
* `get_team( id )`: `Team`
    * `id`: integer
* `get_teams()`: iterator of `Team`

Class `Permissions`
===================

Attributes
----------
* `admin`: bool
* `pull`: bool
* `push`: bool

Class `Plan`
============

Attributes
----------
* `collaborators`: integer
* `name`: string
* `private_repos`: integer
* `space`: integer

Class `PullRequest`
===================

Attributes
----------
* `additions`: integer
* `base`: `PullRequestPart`
* `body`: string
* `changed_files`: integer
* `closed_at`: datetime.datetime
* `comments`: integer
* `commits`: integer
* `created_at`: datetime.datetime
* `deletions`: integer
* `diff_url`: string
* `head`: `PullRequestPart`
* `html_url`: string
* `id`: integer
* `issue_url`: string
* `mergeable`: bool
* `merged`: bool
* `merged_at`: datetime.datetime
* `merged_by`: `NamedUser`
* `number`: integer
* `patch_url`: string
* `review_comments`: integer
* `state`: string
* `title`: string
* `updated_at`: datetime.datetime
* `url`: string
* `user`: `NamedUser`

Review comments
---------------
* `create_comment( body, commit_id, path, position )` or `create_review_comment( body, commit_id, path, position )`: `PullRequestComment`
    * `body`: string
    * `commit_id`: `Commit`
    * `path`: string
    * `position`: integer
* `get_comment( id )` or `get_review_comment( id )`: `PullRequestComment`
    * `id`: integer
* `get_comments()` or `get_review_comments()`: iterator of `PullRequestComment`

Commits
-------
* `get_commits()`: iterator of `Commit`

Files
-----
* `get_files()`: iterator of `File`

Issue_comments
--------------
* `create_issue_comment( body )`: `IssueComment`
    * `body`: string
* `get_issue_comment( id )`: `IssueComment`
    * `id`: integer
* `get_issue_comments()`: iterator of `IssueComment`

Merging
-------
* `is_merged()`: bool
* `merge( [commit_message] )`: `PullRequestMergeStatus`
    * `commit_message`: string

Modification
------------
* `edit( [title, body, state] )`
    * `title`: string
    * `body`: string
    * `state`: string

Class `PullRequestComment`
==========================

Attributes
----------
* `body`: string
* `commit_id`: string
* `created_at`: datetime.datetime
* `id`: integer
* `original_commit_id`: string
* `original_position`: integer
* `path`: string
* `position`: integer
* `updated_at`: datetime.datetime
* `url`: string
* `user`: `NamedUser`

Deletion
--------
* `delete()`

Modification
------------
* `edit( body )`
    * `body`: string

Class `PullRequestMergeStatus`
==============================

Attributes
----------
* `merged`: bool
* `message`: string
* `sha`: string

Class `PullRequestPart`
=======================

Attributes
----------
* `label`: string
* `ref`: string
* `repo`: `Repository`
* `sha`: string
* `user`: `NamedUser`

Class `Repository`
==================

Attributes
----------
* `clone_url`: string
* `created_at`: datetime.datetime
* `description`: string
* `fork`: bool
* `forks`: integer
* `full_name`: string
* `git_url`: string
* `has_downloads`: bool
* `has_issues`: bool
* `has_wiki`: bool
* `homepage`: string
* `html_url`: string
* `id`: integer
* `language`: string
* `master_branch`: string
* `name`: string
* `open_issues`: integer
* `organization`: `Organization`
* `owner`: `NamedUser`
* `parent`: `Repository`
* `permissions`: `Permissions`
* `private`: bool
* `pushed_at`: datetime.datetime
* `size`: integer
* `source`: `Repository`
* `ssh_url`: string
* `svn_url`: string
* `updated_at`: datetime.datetime
* `url`: string
* `watchers`: integer

Comparison
----------
* `compare( base, head )`: `Comparison`
    * `base`: string
    * `head`: string

Assignees
---------
* `get_assignees()`: iterator of `NamedUser`
* `has_in_assignees( assignee )`: bool
    * `assignee`: `NamedUser`

Branches
--------
* `get_branch( branch )`: `Branch`
    * `branch`: string
* `get_branches()`: iterator of `Branch`

Collaborators
-------------
* `add_to_collaborators( collaborator )`
    * `collaborator`: `NamedUser`
* `get_collaborators()`: iterator of `NamedUser`
* `has_in_collaborators( collaborator )`: bool
    * `collaborator`: `NamedUser`
* `remove_from_collaborators( collaborator )`
    * `collaborator`: `NamedUser`

Comments
--------
* `get_comment( id )`: `CommitComment`
    * `id`: integer
* `get_comments()`: iterator of `CommitComment`

Commits
-------
* `get_commit( sha )`: `Commit`
    * `sha`: string
* `get_commits( [sha, path] )`: iterator of `Commit`
    * `sha`: string
    * `path`: string

Contents
--------
* `get_readme()`: `ContentFile`
* `get_contents( path )`: `ContentFile`
    * `path`: string
* `get_archive_link( archive_format, [ref] )`: string
    * `archive_format`: string
    * `ref`: string

Contributors
------------
* `get_contributors()`: iterator of `NamedUser`

Deletion
--------
* `delete()`

Downloads
---------
* `create_download( name, size, [description, content_type] )`: `Download`
    * `name`: string
    * `size`: integer
    * `description`: string
    * `content_type`: string
* `get_download( id )`: `Download`
    * `id`: integer
* `get_downloads()`: iterator of `Download`

Events
------
* `get_events()`: iterator of `Event`
* `get_network_events()`: iterator of `Event`

Forks
-----
* `get_forks()`: iterator of `Repository`

Git_blobs
---------
* `create_git_blob( content, encoding )`: `GitBlob`
    * `content`: string
    * `encoding`: string
* `get_git_blob( sha )`: `GitBlob`
    * `sha`: string

Git_commits
-----------
* `create_git_commit( message, tree, parents, [author, committer] )`: `GitCommit`
    * `message`: string
    * `tree`: `GitTree`
    * `parents`: list of `GitCommit`
    * `author`: `InputGitAuthor`
    * `committer`: `InputGitAuthor`
* `get_git_commit( sha )`: `GitCommit`
    * `sha`: string

Git_refs
--------
* `create_git_ref( ref, sha )`: `GitRef`
    * `ref`: string
    * `sha`: string
* `get_git_ref( ref )`: `GitRef`
    * `ref`: string
* `get_git_refs()`: iterator of `GitRef`

Git_tags
--------
* `create_git_tag( tag, message, object, type, [tagger] )`: `GitTag`
    * `tag`: string
    * `message`: string
    * `object`: string
    * `type`: string
    * `tagger`: `InputGitAuthor`
* `get_git_tag( sha )`: `GitTag`
    * `sha`: string

Git_trees
---------
* `create_git_tree( tree, [base_tree] )`: `GitTree`
    * `tree`: list of `InputGitTreeElement`
    * `base_tree`: `GitTree`
* `get_git_tree( sha, [recursive] )`: `GitTree`
    * `sha`: string
    * `recursive`: bool

Hooks
-----
* `create_hook( name, config, [events, active] )`: `Hook`
    * `name`: string
    * `config`: dict
    * `events`: list of string
    * `active`: bool
* `get_hook( id )`: `Hook`
    * `id`: integer
* `get_hooks()`: iterator of `Hook`

Issues
------
* `create_issue( title, [body, assignee, milestone, labels] )`: `Issue`
    * `title`: string
    * `body`: string
    * `assignee`: `NamedUser`
    * `milestone`: `Milestone`
    * `labels`: list of `Label`
* `get_issue( number )`: `Issue`
    * `number`: integer
* `get_issues( [milestone, state, assignee, mentioned, labels, sort, direction, since] )`: iterator of `Issue`
    * `milestone`: `Milestone` or "none" or "*"
    * `state`: string
    * `assignee`: `NamedUser` or "none" or "*"
    * `mentioned`: `NamedUser`
    * `labels`: list of `Label`
    * `sort`: string
    * `direction`: string
    * `since`: datetime.datetime
* `legacy_search_issues( state, keyword )`: iterator of `Issue`
    * `state`: "open" or "closed"
    * `keyword`: string

Issues_events
-------------
* `get_issues_event( id )`: `IssueEvent`
    * `id`: integer
* `get_issues_events()`: iterator of `IssueEvent`

Keys
----
* `create_key( title, key )`: `RepositoryKey`
    * `title`: string
    * `key`: string
* `get_key( id )`: `RepositoryKey`
    * `id`: integer
* `get_keys()`: iterator of `RepositoryKey`

Labels
------
* `create_label( name, color )`: `Label`
    * `name`: string
    * `color`: string
* `get_label( name )`: `Label`
    * `name`: string
* `get_labels()`: iterator of `Label`

Languages
---------
* `get_languages()`: dict of string to integer

Merging
-------
* `merge( base, head, [commit_message] )`: `Commit`
    * `base`: string
    * `head`: string
    * `commit_message`: string

Milestones
----------
* `create_milestone( title, [state, description, due_on] )`: `Milestone`
    * `title`: string
    * `state`: string
    * `description`: string
    * `due_on`: date
* `get_milestone( number )`: `Milestone`
    * `number`: integer
* `get_milestones( [state, sort, direction] )`: iterator of `Milestone`
    * `state`: string
    * `sort`: string
    * `direction`: string

Modification
------------
* `edit( name, [description, homepage, public, has_issues, has_wiki, has_downloads] )`
    * `name`: string
    * `description`: string
    * `homepage`: string
    * `public`: bool
    * `has_issues`: bool
    * `has_wiki`: bool
    * `has_downloads`: bool

Pulls
-----
* `create_pull( < title, body, base, head > or < issue, base, head > )`: `PullRequest`
    * `title`: string
    * `body`: string
    * `issue`: `Issue`
    * `base`: string
    * `head`: string
* `get_pull( number )`: `PullRequest`
    * `number`: integer
* `get_pulls( [state] )`: iterator of `PullRequest`
    * `state`: string

Stargazers
----------
* `get_stargazers()`: iterator of `NamedUser`

Subscribers
-----------
* `get_subscribers()`: iterator of `NamedUser`

Tags
----
* `get_tags()`: iterator of `Tag`

Teams
-----
* `get_teams()`: iterator of `Team`

Watchers
--------
* `get_watchers()`: iterator of `NamedUser`

Class `RepositoryKey`
=====================

Attributes
----------
* `id`: integer
* `key`: string
* `title`: string
* `url`: string
* `verified`: bool

Deletion
--------
* `delete()`

Modification
------------
* `edit( [title, key] )`
    * `title`: string
    * `key`: string

Class `Tag`
===========

Attributes
----------
* `commit`: `Commit`
* `name`: string
* `tarball_url`: string
* `zipball_url`: string

Class `Team`
============

Attributes
----------
* `id`: integer
* `members_count`: integer
* `name`: string
* `permission`: string
* `repos_count`: integer
* `url`: string

Deletion
--------
* `delete()`

Members
-------
* `add_to_members( member )`
    * `member`: `NamedUser`
* `get_members()`: iterator of `NamedUser`
* `has_in_members( member )`: bool
    * `member`: `NamedUser`
* `remove_from_members( member )`
    * `member`: `NamedUser`

Modification
------------
* `edit( name, [permission] )`
    * `name`: string
    * `permission`: string

Repos
-----
* `add_to_repos( repo )`
    * `repo`: `Repository`
* `get_repos()`: iterator of `Repository`
* `has_in_repos( repo )`: bool
    * `repo`: `Repository`
* `remove_from_repos( repo )`
    * `repo`: `Repository`

Class `UserKey`
===============

Attributes
----------
* `id`: integer
* `key`: string
* `title`: string
* `url`: string
* `verified`: bool

Deletion
--------
* `delete()`

Modification
------------
* `edit( [title, key] )`
    * `title`: string
    * `key`: string
