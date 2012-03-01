You don't normaly create instances of any class but `Github`.
You obtain instances through calls to `get_` and `create_` methods.

In this documentation:

* `login` is a string containing a user's or organization's login
* `user` is an instance of `AuthenticatedUser` or `NamedUser`
* `name` is a string containing the name of a repository
* `repo` is an instance of `Repository`

Class `Github`
==============
* Constructed from user's login and password
* `get_user()`: `AuthenticatedUser`
* `get_user( login )`: `NamedUser`
* `get_organization( login )`: `Organization`

Class `AuthenticatedUser`
=========================

Attributes
----------
* `login`
* `id`
* `avatar_url`
* `gravatar_id`
* `url`
* `name`
* `company`
* `blog`
* `location`
* `email`
* `hireable`
* `bio`
* `public_repos`
* `public_gists`
* `followers`
* `following`
* `html_url`
* `created_at`
* `type`
* `total_private_repos`
* `owned_private_repos`
* `private_gists`
* `disk_usage`
* `collaborators`
* `plan`

Modification
------------
* `edit( [name, email, blog, company, location, hireable, bio] )`

Emails
------
* `get_emails()`: list of string
* `add_to_emails( email, ... )`
    * `email`: string
* `remove_from_emails( email, ... )`
    * `email`: string

Authorizations
--------------
* `get_authorizations()`: list of `Authorization`
* `get_authorization( id )`: `Authorization`
* `create_authorization( [scopes, note, note_url] )`: `Authorization`

Keys
----
* `get_keys()`: list of `UserKey`
* `get_key( id )`: `UserKey`
* `create_key()`: `UserKey`

Followers
---------
* `get_followers()`: list of `NamedUser`

Following
---------
* `get_following()`: list of `NamedUser`
* `add_to_following( following )`
    * `following`: `NamedUser`
* `remove_from_following( following )`
    * `following`: `NamedUser`
* `has_in_following( following )`: `bool`
    * `following`: `NamedUser`

Orgs
----
* `get_orgs()`: list of `Organization`

Repos
-----
* `get_repos( [type] )`: list of `Repository`
* `get_repo( name )`: `Repository`
* `create_repo( name, [description, homepage, private, has_issues, has_wiki, has_downloads, team_id] )`: `Repository`

Watched
-------
* `get_watched()`: list of `Repository`
* `add_to_watched( watched )`
    * `watched`: `Repository`
* `remove_from_watched( watched )`
    * `watched`: `Repository`
* `has_in_watched( watched )`: `bool`
    * `watched`: `Repository`

Forking
-------
* `create_fork( repo )`: `Repository`

Gists
-----
* `get_gists()`: list of `Gist`
* `create_gist( public, files, [description] )`: `Gist`
* `get_starred_gists()`: list of `Gist`

Class `Authorization`
=====================

Attributes
----------
* `id`
* `url`
* `scopes`
* `token`
* `app`
* `note`
* `note_url`
* `updated_at`
* `created_at`

Modification
------------
* `edit( [scopes, add_scopes, remove_scopes, note, note_url] )`

Deletion
--------
* `delete()`

Class `Branch`
==============

Attributes
----------
* `name`
* `commit`: `Commit`

Class `Commit`
==============

Attributes
----------
* `sha`
* `url`
* `parents`
* `stats`
* `files`
* `commit`: `GitCommit`
* `author`: `NamedUser`
* `committer`: `NamedUser`

Comments
--------
* `get_comments()`: list of `CommitComment`
* `create_comment( body, commit_id, line, path, position )`: `CommitComment`

Class `CommitComment`
=====================

Attributes
----------
* `url`
* `id`
* `body`
* `path`
* `position`
* `commit_id`
* `created_at`
* `updated_at`
* `html_url`
* `line`
* `user`: `NamedUser`

Modification
------------
* `edit( body )`

Deletion
--------
* `delete()`

Class `Download`
================

Attributes
----------
* `url`
* `html_url`
* `id`
* `name`
* `description`
* `size`
* `download_count`
* `content_type`
* `policy`
* `signature`
* `bucket`
* `accesskeyid`
* `path`
* `acl`
* `expirationdate`
* `prefix`
* `mime_type`
* `redirect`
* `s3_url`
* `created_at`

Deletion
--------
* `delete()`

Class `Gist`
============

Attributes
----------
* `url`
* `id`
* `description`
* `public`
* `files`
* `comments`
* `html_url`
* `git_pull_url`
* `git_push_url`
* `created_at`
* `forks`
* `history`
* `updated_at`
* `user`: `NamedUser`

Modification
------------
* `edit( [description, files] )`

Deletion
--------
* `delete()`

Comments
--------
* `get_comments()`: list of `GistComment`
* `get_comment( id )`: `GistComment`
* `create_comment( body )`: `GistComment`

Starring
--------
* `is_starred()`: bool
* `set_starred()`
* `reset_starred()`

Forking
-------
* `create_fork()`: `Gist`

Class `GistComment`
===================

Attributes
----------
* `id`
* `url`
* `body`
* `created_at`
* `updated_at`
* `user`: `NamedUser`

Modification
------------
* `edit( body )`

Deletion
--------
* `delete()`

Class `GitBlob`
===============

Attributes
----------
* `sha`
* `size`
* `url`
* `content`
* `encoding`

Class `GitCommit`
=================

Attributes
----------
* `sha`
* `url`
* `message`
* `author`
* `committer`
* `tree`
* `parents`

Class `GitRef`
==============

Attributes
----------
* `ref`
* `url`
* `object`

Modification
------------
* `edit( sha, [force] )`

Class `GitTag`
==============

Attributes
----------
* `tag`
* `sha`
* `url`
* `message`
* `tagger`
* `object`

Class `GitTree`
===============

Attributes
----------
* `sha`
* `url`
* `tree`

Class `Issue`
=============

Attributes
----------
* `url`
* `html_url`
* `number`
* `state`
* `title`
* `body`
* `labels`
* `comments`
* `closed_at`
* `created_at`
* `updated_at`
* `id`
* `closed_by`
* `pull_request`
* `user`: `NamedUser`
* `assignee`: `NamedUser`
* `milestone`: `Milestone`

Modification
------------
* `edit( [title, body, assignee, state, milestone, labels] )`

Labels
------
* `get_labels()`: list of `Label`
* `add_to_labels( label, ... )`
    * `label`: `Label`
* `set_labels( label, ... )`
    * `label`: `Label`
* `delete_labels()`
* `remove_from_labels( label )`
    * `label`: `Label`

Comments
--------
* `get_comments()`: list of `IssueComment`
* `get_comment( id )`: `IssueComment`
* `create_comment( body )`: `IssueComment`

Class `IssueComment`
====================

Attributes
----------
* `url`
* `body`
* `created_at`
* `updated_at`
* `id`
* `user`: `NamedUser`

Modification
------------
* `edit( body )`

Deletion
--------
* `delete()`

Class `Label`
=============

Attributes
----------
* `url`
* `name`
* `color`

Modification
------------
* `edit( name, color )`

Deletion
--------
* `delete()`

Class `Milestone`
=================

Attributes
----------
* `url`
* `number`
* `state`
* `title`
* `description`
* `open_issues`
* `closed_issues`
* `created_at`
* `due_on`
* `creator`: `NamedUser`

Modification
------------
* `edit( title, [state, description, due_on] )`

Deletion
--------
* `delete()`

Labels
------
* `get_labels()`: list of `Label`

Class `NamedUser`
=================

Attributes
----------
* `login`
* `id`
* `avatar_url`
* `gravatar_id`
* `url`
* `name`
* `company`
* `blog`
* `location`
* `email`
* `hireable`
* `bio`
* `public_repos`
* `public_gists`
* `followers`
* `following`
* `html_url`
* `created_at`
* `type`
* `contributions`
* `disk_usage`
* `collaborators`
* `plan`
* `total_private_repos`
* `owned_private_repos`
* `private_gists`

Followers
---------
* `get_followers()`: list of `NamedUser`

Following
---------
* `get_following()`: list of `NamedUser`

Orgs
----
* `get_orgs()`: list of `Organization`

Repos
-----
* `get_repos( [type] )`: list of `Repository`
* `get_repo( name )`: `Repository`

Watched
-------
* `get_watched()`: list of `Repository`

Gists
-----
* `get_gists()`: list of `Gist`

Class `Organization`
====================

Attributes
----------
* `login`
* `id`
* `url`
* `avatar_url`
* `name`
* `company`
* `blog`
* `location`
* `email`
* `public_repos`
* `public_gists`
* `followers`
* `following`
* `html_url`
* `created_at`
* `type`
* `disk_usage`
* `collaborators`
* `billing_email`
* `plan`
* `private_gists`
* `total_private_repos`
* `owned_private_repos`

Modification
------------
* `edit( [billing_email, blog, company, email, location, name] )`

Public members
--------------
* `get_public_members()`: list of `NamedUser`
* `add_to_public_members( public_member )`
    * `public_member`: `NamedUser`
* `remove_from_public_members( public_member )`
    * `public_member`: `NamedUser`
* `has_in_public_members( public_member )`: `bool`
    * `public_member`: `NamedUser`

Members
-------
* `get_members()`: list of `NamedUser`
* `remove_from_members( member )`
    * `member`: `NamedUser`
* `has_in_members( member )`: `bool`
    * `member`: `NamedUser`

Repos
-----
* `get_repos( [type] )`: list of `Repository`
* `get_repo( name )`: `Repository`
* `create_repo( name, [description, homepage, private, has_issues, has_wiki, has_downloads, team_id] )`: `Repository`

Forking
-------
* `create_fork( repo )`: `Repository`

Teams
-----
* `get_teams()`: list of `Team`
* `create_team( name, [repo_names, permission] )`: `Team`

Class `PullRequest`
===================

Attributes
----------
* `id`
* `url`
* `html_url`
* `diff_url`
* `patch_url`
* `issue_url`
* `number`
* `state`
* `title`
* `body`
* `created_at`
* `updated_at`
* `closed_at`
* `merged_at`
* `merged`
* `mergeable`
* `comments`
* `commits`
* `additions`
* `deletions`
* `changed_files`
* `head`
* `base`
* `merged_by`
* `review_comments`
* `user`: `NamedUser`

Modification
------------
* `edit( [title, body, state] )`

Commits
-------
* `get_commits()`: list of `Commit`

Files
-----
* `get_files()`: list of `PullRequestFile`

Comments
--------
* `get_comments()`: list of `PullRequestComment`
* `get_comment( id )`: `PullRequestComment`
* `create_comment( body, commit_id, path, position )`: `PullRequestComment`

Class `PullRequestComment`
==========================

Attributes
----------
* `url`
* `id`
* `body`
* `path`
* `position`
* `commit_id`
* `created_at`
* `updated_at`
* `html_url`
* `line`
* `user`: `NamedUser`

Modification
------------
* `edit( body )`

Deletion
--------
* `delete()`

Class `PullRequestFile`
=======================

Attributes
----------
* `sha`
* `filename`
* `status`
* `additions`
* `deletions`
* `changes`
* `blob_url`
* `raw_url`
* `patch`

Class `Repository`
==================

Attributes
----------
* `url`
* `html_url`
* `clone_url`
* `git_url`
* `ssh_url`
* `svn_url`
* `name`
* `description`
* `homepage`
* `language`
* `private`
* `fork`
* `forks`
* `watchers`
* `size`
* `master_branch`
* `open_issues`
* `pushed_at`
* `created_at`
* `organization`
* `has_issues`
* `has_wiki`
* `has_downloads`
* `mirror_url`
* `updated_at`
* `id`
* `owner`: `NamedUser`
* `parent`: `Repository`
* `source`: `Repository`

Forks
-----
* `get_forks()`: list of `Repository`

Modification
------------
* `edit( name, [description, homepage, public, has_issues, has_wiki, has_downloads] )`

Languages
---------
* `get_languages()`: dictionary of strings to integers

Keys
----
* `get_keys()`: list of `RepositoryKey`
* `get_key( id )`: `RepositoryKey`
* `create_key()`: `RepositoryKey`

Collaborators
-------------
* `get_collaborators()`: list of `NamedUser`
* `add_to_collaborators( collaborator )`
    * `collaborator`: `NamedUser`
* `remove_from_collaborators( collaborator )`
    * `collaborator`: `NamedUser`
* `has_in_collaborators( collaborator )`: `bool`
    * `collaborator`: `NamedUser`

Contributors
------------
* `get_contributors()`: list of `NamedUser`

Watchers
--------
* `get_watchers()`: list of `NamedUser`

Git refs
--------
* `get_git_refs()`: list of `GitRef`
* `get_git_ref( ref )`: `GitRef`
* `create_git_ref( ref, sha )`: `GitRef`

Git commits
-----------
* `get_git_commit( sha )`: `GitCommit`
* `create_git_commit( message, tree, parents, [author, committer] )`: `GitCommit`

Git trees
---------
* `get_git_tree( sha )`: `GitTree`
* `create_git_tree( tree )`: `GitTree`

Git blobs
---------
* `get_git_blob( sha )`: `GitBlob`
* `create_git_blob( content, encoding )`: `GitBlob`

Git tags
--------
* `get_git_tag( sha )`: `GitTag`
* `create_git_tag( tag, message, object, type, [tagger] )`: `GitTag`

Labels
------
* `get_labels()`: list of `Label`
* `get_label( name )`: `Label`
* `create_label( name, color )`: `Label`

Milestones
----------
* `get_milestones( [state, sort, direction] )`: list of `Milestone`
* `get_milestone( number )`: `Milestone`
* `create_milestone( title, [state, description, due_on] )`: `Milestone`

Issues
------
* `get_issues( [milestone, state, assignee, mentioned, labels, sort, direction, since] )`: list of `Issue`
* `get_issue( number )`: `Issue`
* `create_issue( title, [body, assignee, milestone, labels] )`: `Issue`

Downloads
---------
* `get_downloads()`: list of `Download`
* `get_download( id )`: `Download`
* `create_download( name, size, [description, content_type] )`: `Download`

Comments
--------
* `get_comments()`: list of `CommitComment`
* `get_comment( id )`: `CommitComment`

Commits
-------
* `get_commits( [sha, path] )`: list of `Commit`
* `get_commit( sha )`: `Commit`

Tags
----
* `get_tags()`: list of `Tag`

Branches
--------
* `get_branches()`: list of `Branch`

Pulls
-----
* `get_pulls( [state] )`: list of `PullRequest`
* `get_pull( id )`: `PullRequest`
* `create_pull( title, body, base, head )`: `PullRequest`

Teams
-----
* `get_teams()`: list of `Team`

Class `RepositoryKey`
=====================

Attributes
----------

Modification
------------
* `edit()`

Deletion
--------
* `delete()`

Class `Tag`
===========

Attributes
----------
* `name`
* `zipball_url`
* `tarball_url`
* `commit`: `Commit`

Class `Team`
============

Attributes
----------
* `url`
* `name`
* `id`
* `permission`
* `members_count`
* `repos_count`

Modification
------------
* `edit( name, [permission] )`

Deletion
--------
* `delete()`

Members
-------
* `get_members()`: list of `NamedUser`
* `add_to_members( member )`
    * `member`: `NamedUser`
* `remove_from_members( member )`
    * `member`: `NamedUser`
* `has_in_members( member )`: `bool`
    * `member`: `NamedUser`

Repos
-----
* `get_repos()`: list of `Repository`
* `add_to_repos( repo )`
    * `repo`: `Repository`
* `remove_from_repos( repo )`
    * `repo`: `Repository`
* `has_in_repos( repo )`: `bool`
    * `repo`: `Repository`

Class `UserKey`
===============

Attributes
----------

Modification
------------
* `edit()`

Deletion
--------
* `delete()`


