You don't normaly create instances of any class but `Github`.
You obtain instances through calls to `get_` and `create_` methods.
Class `Github`
==============
* Constructed from user's login and password or OAuth token
* `get_user()`: `AuthenticatedUser`
* `get_user( login )`: `NamedUser`
* `get_organization( login )`: `Organization`
* `get_gist( id )`: `Gist`
* `get_gists()`: list of `Gist`
* `rate_limiting`: tuple of two integers: remaining and limit, as explained in [Rate Limiting](http://developer.github.com/v3/#rate-limiting)

Class `AuthenticatedUser`
=========================

Attributes
----------
* `avatar_url`: string
* `bio`: string
* `blog`: string
* `collaborators`: integer
* `company`: string
* `created_at`: string
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
    * `scopes`
    * `note`
    * `note_url`
* `get_authorization( id )`: `Authorization`
    * `id`
* `get_authorizations()`: list of `Authorization`

Emails
------
* `add_to_emails( email, ... )`
    * `email`: string
* `get_emails()`: list of string
* `remove_from_emails( email, ... )`
    * `email`: string

Events
------
* `get_events()`: list of `Event`
* `get_organization_events( org )`: list of `Event`
    * `org`: `Organization`

Followers
---------
* `get_followers()`: list of `NamedUser`

Following
---------
* `add_to_following( following )`
    * `following`: `NamedUser`
* `get_following()`: list of `NamedUser`
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
    * `files`: `dict`
    * `description`: string
* `get_gists()`: list of `Gist`
* `get_starred_gists()`: list of `Gist`

Issues
------
* `get_issues()`: list of `Issue`

Keys
----
* `create_key( title, key )`: `UserKey`
    * `title`
    * `key`
* `get_key( id )`: `UserKey`
    * `id`
* `get_keys()`: list of `UserKey`

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
* `get_orgs()`: list of `Organization`

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
* `get_repos( [type] )`: list of `Repository`
    * `type`

Watched
-------
* `add_to_watched( watched )`
    * `watched`: `Repository`
* `get_watched()`: list of `Repository`
* `has_in_watched( watched )`: bool
    * `watched`: `Repository`
* `remove_from_watched( watched )`
    * `watched`: `Repository`

Class `Authorization`
=====================

Attributes
----------
* `app`
* `created_at`
* `id`
* `note`
* `note_url`
* `scopes`
* `token`
* `updated_at`
* `url`

Deletion
--------
* `delete()`

Modification
------------
* `edit( [scopes, add_scopes, remove_scopes, note, note_url] )`
    * `scopes`
    * `add_scopes`
    * `remove_scopes`
    * `note`
    * `note_url`

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
* `files`: list of `CommitFile`
* `parents`: list of `Commit`
* `sha`: string
* `stats`: `CommitStats`
* `url`: string

Comments
--------
* `create_comment( body, [line, path, position] )`: `CommitComment`
    * `body`
    * `line`
    * `path`
    * `position`
* `get_comments()`: list of `CommitComment`

Class `CommitComment`
=====================

Attributes
----------
* `body`: string
* `commit_id`: string
* `created_at`: string
* `html_url`: string
* `id`: integer
* `line`: integer
* `path`: string
* `position`: integer
* `updated_at`: string
* `url`: string
* `user`: `NamedUser`

Deletion
--------
* `delete()`

Modification
------------
* `edit( body )`
    * `body`

Class `CommitFile`
==================

Attributes
----------
* `additions`
* `blob_url`
* `changes`
* `deletions`
* `filename`
* `patch`
* `raw_url`
* `sha`
* `status`

Class `CommitStats`
===================

Attributes
----------
* `additions`: integer
* `deletions`: integer
* `total`: integer

Class `Download`
================

Attributes
----------
* `accesskeyid`
* `acl`
* `bucket`
* `content_type`
* `created_at`
* `description`
* `download_count`
* `expirationdate`
* `html_url`
* `id`
* `mime_type`
* `name`
* `path`
* `policy`
* `prefix`
* `redirect`
* `s3_url`
* `signature`
* `size`
* `url`

Deletion
--------
* `delete()`

Class `Event`
=============

Attributes
----------
* `actor`: `NamedUser`
* `commit_id`
* `created_at`
* `event`
* `id`
* `issue`
* `org`: `Organization`
* `payload`
* `public`
* `repo`: `Repository`
* `type`
* `url`

Class `Gist`
============

Attributes
----------
* `comments`: integer
* `created_at`: string
* `description`: string
* `files`
* `fork_of`: `Gist`
* `forks`: list of `Gist`
* `git_pull_url`: string
* `git_push_url`: string
* `history`: list of `GistHistoryState`
* `html_url`: string
* `id`: string
* `public`: bool
* `updated_at`: string
* `url`: string
* `user`: `NamedUser`

Comments
--------
* `create_comment( body )`: `GistComment`
    * `body`
* `get_comment( id )`: `GistComment`
    * `id`
* `get_comments()`: list of `GistComment`

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
    * `files`

Starring
--------
* `is_starred()`: bool
* `reset_starred()`
* `set_starred()`

Class `GistComment`
===================

Attributes
----------
* `body`
* `created_at`
* `id`
* `updated_at`
* `url`
* `user`: `NamedUser`

Deletion
--------
* `delete()`

Modification
------------
* `edit( body )`
    * `body`

Class `GistHistoryState`
========================

Attributes
----------
* `change_status`: `CommitStats`
* `committed_at`: string
* `url`: string
* `user`: `NamedUser`
* `version`: string

Class `GitAuthor`
=================

Attributes
----------
* `date`: string
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
    * `sha`
    * `force`

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
* `active`
* `config`
* `created_at`
* `events`
* `id`
* `last_response`
* `name`
* `updated_at`
* `url`

Deletion
--------
* `delete()`

Modification
------------
* `edit( name, config, [events, add_events, remove_events, active] )`
    * `name`
    * `config`
    * `events`
    * `add_events`
    * `remove_events`
    * `active`

Testing
-------
* `test()`

Class `Issue`
=============

Attributes
----------
* `assignee`: `NamedUser`
* `body`: string
* `closed_at`: string
* `closed_by`: `NamedUser`
* `comments`: integer
* `created_at`: string
* `html_url`: string
* `id`: integer
* `labels`: list of `Label`
* `milestone`: `Milestone`
* `number`: integer
* `pull_request`
* `state`: string
* `title`: string
* `updated_at`: string
* `url`: string
* `user`: `NamedUser`

Comments
--------
* `create_comment( body )`: `IssueComment`
    * `body`: string
* `get_comment( id )`: `IssueComment`
    * `id`
* `get_comments()`: list of `IssueComment`

Events
------
* `get_events()`: list of `IssueEvent`

Labels
------
* `add_to_labels( label, ... )`
    * `label`: `Label`
* `delete_labels()`
* `get_labels()`: list of `Label`
* `remove_from_labels( label )`
    * `label`: `Label`
* `set_labels( label, ... )`
    * `label`: `Label`

Modification
------------
* `edit( [title, body, assignee, state, milestone, labels] )`
    * `title`
    * `body`
    * `assignee`
    * `state`
    * `milestone`
    * `labels`

Class `IssueComment`
====================

Attributes
----------
* `body`
* `created_at`
* `id`
* `updated_at`
* `url`
* `user`: `NamedUser`

Deletion
--------
* `delete()`

Modification
------------
* `edit( body )`
    * `body`

Class `IssueEvent`
==================

Attributes
----------
* `actor`: `NamedUser`
* `commit_id`: string
* `created_at`: string
* `event`: string
* `id`: integer
* `issue`: `Issue`
* `url`: string

Class `Label`
=============

Attributes
----------
* `color`
* `name`
* `url`

Deletion
--------
* `delete()`

Modification
------------
* `edit( name, color )`
    * `name`
    * `color`

Class `Milestone`
=================

Attributes
----------
* `closed_issues`: integer
* `created_at`: string
* `creator`: `NamedUser`
* `description`: string
* `due_on`: string
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
* `get_labels()`: list of `Label`

Modification
------------
* `edit( title, [state, description, due_on] )`
    * `title`
    * `state`
    * `description`
    * `due_on`

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
* `created_at`: string
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
* `get_events()`: list of `Event`
* `get_public_events()`: list of `Event`
* `get_received_events()`: list of `Event`
* `get_public_received_events()`: list of `Event`

Followers
---------
* `get_followers()`: list of `NamedUser`

Following
---------
* `get_following()`: list of `NamedUser`

Gists
-----
* `create_gist( public, files, [description] )`: `Gist`
    * `public`: bool
    * `files`: `dict`
    * `description`: string
* `get_gists()`: list of `Gist`

Orgs
----
* `get_orgs()`: list of `Organization`

Repos
-----
* `get_repo( name )`: `Repository`
    * `name`: string
* `get_repos( [type] )`: list of `Repository`
    * `type`

Watched
-------
* `get_watched()`: list of `Repository`

Class `Organization`
====================

Attributes
----------
* `avatar_url`: string
* `billing_email`: string
* `blog`: string
* `collaborators`: integer
* `company`: string
* `created_at`: string
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
* `get_events()`: list of `Event`

Forking
-------
* `create_fork( repo )`: `Repository`
    * `repo`: `Repository`

Members
-------
* `get_members()`: list of `NamedUser`
* `has_in_members( member )`: bool
    * `member`: `NamedUser`
* `remove_from_members( member )`
    * `member`: `NamedUser`

Modification
------------
* `edit( [billing_email, blog, company, email, location, name] )`
    * `billing_email`
    * `blog`
    * `company`
    * `email`
    * `location`
    * `name`

Public_members
--------------
* `add_to_public_members( public_member )`
    * `public_member`: `NamedUser`
* `get_public_members()`: list of `NamedUser`
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
    * `team_id`
* `get_repo( name )`: `Repository`
    * `name`: string
* `get_repos( [type] )`: list of `Repository`
    * `type`

Teams
-----
* `create_team( name, [repo_names, permission] )`: `Team`
    * `name`: string
    * `repo_names`: `list`
    * `permission`
* `get_teams()`: list of `Team`

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
* `additions`
* `base`
* `body`
* `changed_files`
* `closed_at`
* `comments`
* `commits`
* `created_at`
* `deletions`
* `diff_url`
* `head`
* `html_url`
* `id`
* `issue_url`
* `mergeable`
* `merged`
* `merged_at`
* `merged_by`
* `number`
* `patch_url`
* `review_comments`
* `state`
* `title`
* `updated_at`
* `url`
* `user`: `NamedUser`

Comments
--------
* `get_comment( id )`: `PullRequestComment`
    * `id`
* `get_comments()`: list of `PullRequestComment`

Commits
-------
* `get_commits()`: list of `Commit`

Files
-----
* `get_files()`: list of `PullRequestFile`

Merging
-------
* `is_merged()`: bool
* `merge( [commit_message] )`
    * `commit_message`: string

Modification
------------
* `edit( [title, body, state] )`
    * `title`
    * `body`
    * `state`

Class `PullRequestComment`
==========================

Attributes
----------
* `body`
* `commit_id`
* `created_at`
* `html_url`
* `id`
* `line`
* `path`
* `position`
* `updated_at`
* `url`
* `user`: `NamedUser`

Deletion
--------
* `delete()`

Modification
------------
* `edit( body )`
    * `body`

Class `PullRequestFile`
=======================

Attributes
----------
* `additions`
* `blob_url`
* `changes`
* `deletions`
* `filename`
* `patch`
* `raw_url`
* `sha`
* `status`

Class `Repository`
==================

Attributes
----------
* `clone_url`: string
* `created_at`: string
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
* `mirror_url`: string
* `name`: string
* `open_issues`: integer
* `organization`: `Organization`
* `owner`: `NamedUser`
* `parent`: `Repository`
* `permissions`: `Permissions`
* `private`: bool
* `pushed_at`: string
* `size`: integer
* `source`: `Repository`
* `ssh_url`: string
* `svn_url`: string
* `updated_at`: string
* `url`: string
* `watchers`: integer

Comparison
----------
* `compare( base, head )`
    * `base`
    * `head`

Branches
--------
* `get_branches()`: list of `Branch`

Collaborators
-------------
* `add_to_collaborators( collaborator )`
    * `collaborator`: `NamedUser`
* `get_collaborators()`: list of `NamedUser`
* `has_in_collaborators( collaborator )`: bool
    * `collaborator`: `NamedUser`
* `remove_from_collaborators( collaborator )`
    * `collaborator`: `NamedUser`

Comments
--------
* `get_comment( id )`: `CommitComment`
    * `id`
* `get_comments()`: list of `CommitComment`

Commits
-------
* `get_commit( sha )`: `Commit`
    * `sha`
* `get_commits( [sha, path] )`: list of `Commit`
    * `sha`
    * `path`

Contributors
------------
* `get_contributors()`: list of `NamedUser`

Downloads
---------
* `create_download( name, size, [description, content_type] )`: `Download`
    * `name`
    * `size`
    * `description`
    * `content_type`
* `get_download( id )`: `Download`
    * `id`
* `get_downloads()`: list of `Download`

Events
------
* `get_events()`: list of `Event`
* `get_network_events()`: list of `Event`

Forks
-----
* `get_forks()`: list of `Repository`

Git_blobs
---------
* `create_git_blob( content, encoding )`: `GitBlob`
    * `content`
    * `encoding`
* `get_git_blob( sha )`: `GitBlob`
    * `sha`

Git_commits
-----------
* `create_git_commit( message, tree, parents, [author, committer] )`: `GitCommit`
    * `message`
    * `tree`
    * `parents`
    * `author`
    * `committer`
* `get_git_commit( sha )`: `GitCommit`
    * `sha`

Git_refs
--------
* `create_git_ref( ref, sha )`: `GitRef`
    * `ref`
    * `sha`
* `get_git_ref( ref )`: `GitRef`
    * `ref`
* `get_git_refs()`: list of `GitRef`

Git_tags
--------
* `create_git_tag( tag, message, object, type, [tagger] )`: `GitTag`
    * `tag`
    * `message`
    * `object`
    * `type`
    * `tagger`
* `get_git_tag( sha )`: `GitTag`
    * `sha`

Git_trees
---------
* `create_git_tree( tree, [base_tree] )`: `GitTree`
    * `tree`
    * `base_tree`
* `get_git_tree( sha, [recursive] )`: `GitTree`
    * `sha`
    * `recursive`: bool

Hooks
-----
* `create_hook( name, config, [events, active] )`: `Hook`
    * `name`
    * `config`
    * `events`
    * `active`
* `get_hook( id )`: `Hook`
    * `id`
* `get_hooks()`: list of `Hook`

Issues
------
* `create_issue( title, [body, assignee, milestone, labels] )`: `Issue`
    * `title`
    * `body`
    * `assignee`
    * `milestone`
    * `labels`
* `get_issue( number )`: `Issue`
    * `number`
* `get_issues( [milestone, state, assignee, mentioned, labels, sort, direction, since] )`: list of `Issue`
    * `milestone`
    * `state`
    * `assignee`
    * `mentioned`
    * `labels`
    * `sort`
    * `direction`
    * `since`

Issues_events
-------------
* `get_issues_event( id )`: `IssueEvent`
    * `id`
* `get_issues_events()`: list of `IssueEvent`

Keys
----
* `create_key( title, key )`: `RepositoryKey`
    * `title`
    * `key`
* `get_key( id )`: `RepositoryKey`
    * `id`
* `get_keys()`: list of `RepositoryKey`

Labels
------
* `create_label( name, color )`: `Label`
    * `name`
    * `color`
* `get_label( name )`: `Label`
    * `name`
* `get_labels()`: list of `Label`

Languages
---------
* `get_languages()`

Milestones
----------
* `create_milestone( title, [state, description, due_on] )`: `Milestone`
    * `title`
    * `state`
    * `description`
    * `due_on`
* `get_milestone( number )`: `Milestone`
    * `number`
* `get_milestones( [state, sort, direction] )`: list of `Milestone`
    * `state`
    * `sort`
    * `direction`

Modification
------------
* `edit( name, [description, homepage, public, has_issues, has_wiki, has_downloads] )`
    * `name`
    * `description`
    * `homepage`
    * `public`
    * `has_issues`
    * `has_wiki`
    * `has_downloads`

Pulls
-----
* `get_pull( number )`: `PullRequest`
    * `number`
* `get_pulls( [state] )`: list of `PullRequest`
    * `state`

Tags
----
* `get_tags()`: list of `Tag`

Teams
-----
* `get_teams()`: list of `Team`

Watchers
--------
* `get_watchers()`: list of `NamedUser`

Class `RepositoryKey`
=====================

Attributes
----------
* `id`
* `key`
* `title`
* `url`

Deletion
--------
* `delete()`

Modification
------------
* `edit( title, key )`
    * `title`
    * `key`

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
* `id`
* `members_count`
* `name`
* `permission`
* `repos_count`
* `url`

Deletion
--------
* `delete()`

Members
-------
* `add_to_members( member )`
    * `member`: `NamedUser`
* `get_members()`: list of `NamedUser`
* `has_in_members( member )`: bool
    * `member`: `NamedUser`
* `remove_from_members( member )`
    * `member`: `NamedUser`

Modification
------------
* `edit( name, [permission] )`
    * `name`
    * `permission`

Repos
-----
* `add_to_repos( repo )`
    * `repo`: `Repository`
* `get_repos()`: list of `Repository`
* `has_in_repos( repo )`: bool
    * `repo`: `Repository`
* `remove_from_repos( repo )`
    * `repo`: `Repository`

Class `UserKey`
===============

Attributes
----------
* `id`
* `key`
* `title`
* `url`

Deletion
--------
* `delete()`

Modification
------------
* `edit( [title, key] )`
    * `title`
    * `key`
