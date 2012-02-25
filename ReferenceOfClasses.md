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
* Attributes: see [API](http://developer.github.com/v3/users/#get-the-authenticated-user)
* `edit( ... )`: see [API](http://developer.github.com/v3/users/#update-the-authenticated-user) for parameters

Repositories
------------
* `get_repos()`: list of `Repository`: see [API](http://developer.github.com/v3/repos/#list-your-repositories) for `type` parameter
* `get_repo( name )`: `Repository`
* `create_repo( ... )`: `Repository`: see [API](http://developer.github.com/v3/repos/#create) for parameters
* `create_fork( repo )`: `Repository`

Watching
--------
* `get_watched()`: list of `Repository`
* `has_in_watched( repo )`: `bool`
* `add_to_watched( repo )`
* `remove_from_watched( repo )`

Organizations
-------------
* `get_orgs()` : list of `Organization`

Following
---------
* `get_followers()` : list of `NamedUser`
* `get_following()` : list of `NamedUser`
* `has_in_following( user )`: `bool`
* `add_to_following( user )`
* `remove_from_following( user )`

Emails
------
* `get_emails()` list of strings
* `add_to_emails( email, ... )`
* `remove_from_emails( email, ... )`

Class `NamedUser`
=================
* Attributes: see [API](http://developer.github.com/v3/users/#get-a-single-user)

Repositories
------------
* `get_repos()`: list of `Repository`: see [API](http://developer.github.com/v3/repos/#list-user-repositories) for `type` parameter
* `get_repo( name )`: `Repository`

Watching
--------
* `get_watched()`: list of `Repository`

Organizations
-------------
* `get_orgs()` : list of `Organization`

Following
---------
* `get_followers()` : list of `NamedUser`
* `get_following()` : list of `NamedUser`

Class `Organization`
====================
* Attributes: see [API](http://developer.github.com/v3/orgs/#get)
* `edit( ... )`: see [API](http://developer.github.com/v3/orgs/#edit) for parameters

Repositories
------------
* `get_repos()`: list of `Repository`: see [API](http://developer.github.com/v3/repos/#list-organization-repositories) for `type` parameter
* `get_repo( name )`: `Repository`
* `create_repo( ... )`: `Repository`: see [API](http://developer.github.com/v3/repos/#create) for parameters
* `create_fork( repo )`: `Repository`

Members
-------
* `get_members()`: list of `NamedUser`
* `has_in_members( user )`: `bool`
* `remove_from_members( user )`
* `get_public_members()`: list of `NamedUser`
* `has_in_public_members( user )`: `bool`
* `add_to_public_members( user )`
* `remove_from_public_members( user )`

Teams
-----
* `get_teams()`: list of `Team`
* `create_team( ... )`: `Team`: see [API](http://developer.github.com/v3/orgs/teams/#create-team) for parameters

Class `Repository`
==================
* Attributes: see [API](http://developer.github.com/v3/repos/#get)
* `edit( ... )`: see [API](http://developer.github.com/v3/repos/#edit) for parameters
* `get_languages()`: dictionary of strings to integers

Collaborators
-------------
* `get_collaborators()`: list of `NamedUser`
* `has_in_collaborators( user )`: `bool`
* `add_to_collaborators( user )`
* `remove_from_collaborators( user )`

Contributors
------------
* `get_contributors()`: list of `NamedUser`

Watching
--------
* `get_watchers()`: list of `NamedUser`

Forks
-----
* `get_forks()`: list of `Repository`

Git objects
-----------
* `get_git_refs()`: list of `GitRef`
* `get_git_ref( ref )`: `GitRef`
* `create_git_ref( ... )`: `GitRef`: see [API](http://developer.github.com/v3/git/refs/#create-a-reference) for parameters
* `get_git_blob( sha )`: `GitBlob`
* `create_git_blob( ... )`: `GitBlob`: see [API](http://developer.github.com/v3/git/blobs/#create-a-blob) for parameters
* `get_git_commit( sha )`: `GitCommit`
* `create_git_commit( ... )`: `GitCommit`: see [API](http://developer.github.com/v3/git/commits/#create-a-commit) for parameters
* `get_git_tree( sha )`: `GitTree`
* `create_git_tree( ... )`: `GitTree`: see [API](http://developer.github.com/v3/git/trees/#create-a-tree) for parameters
* `get_git_tag( sha )`: `GitTag`
* `create_git_tag( ... )`: `GitTag`: see [API](http://developer.github.com/v3/git/tags/#create-a-tag-object) for parameters

Tags, branches, commits
-----------------------
* `get_tags()`: list of `Tag`
* `get_branches()`: list of `Branch`
* `get_commits( ... )`: list of `Commit`: see [API](http://developer.github.com/v3/repos/commits/#list-commits-on-a-repository) for parameters
* `get_commit( sha )`: `Commit`
* `get_comments()`: list of `CommitComment`
* `get_comment( id )`: `CommitComment`

Teams
-----
* `get_teams()`: list of `Team`

Issues and milestones
---------------------
* `get_labels()`: list of `Label`
* `create_label( ... )`: `Label`: see [API](http://developer.github.com/v3/issues/labels/#create-a-label) for parameters
* `get_label( id )`: `Label`
* `get_issues( ... )`: list of `Issue`: see [API](http://developer.github.com/v3/issues/#list-issues-for-a-repository) for parameters
* `create_issue( ... )`: `Issue`: see [API](http://developer.github.com/v3/issues/#create-an-issue) for parameters
* `get_issue( id )`: `Issue`
* `get_milestones( ... )`: list of `Milestone`: see [API](http://developer.github.com/v3/issues/milestones/#list-milestones-for-a-repository) for parameters
* `create_milestone( ... )`: `Milestone`: see [API](http://developer.github.com/v3/issues/milestones/#create-a-milestone) for parameters
* `get_milestone( number )`: `Milestone`

Downloads
---------
`Repository.get_downloads()` list of `Download`
`Repository.create_download( ... )`: `Download`: see [API](http://developer.github.com/v3/repos/downloads/#create-a-new-download-part-1-create-the-resource)
`Repository.get_download( id )`: `Download`

Class `Tag`
===========
* Attributes: see [API](http://developer.github.com/v3/repos/#list-tags)

Class `Branch`
==============
* Attributes: see [API](http://developer.github.com/v3/repos/#list-branches)

Class `Commit`
==============
* Attributes: see [API](http://developer.github.com/v3/repos/commits/#get-a-single-commit)
* `get_comments()`: list of `CommitComment`
* `create_comment( ... )`: `CommitComment`: see [API](http://developer.github.com/v3/repos/commits/#create-a-commit-comment) for parameters

Class `CommitComment`
=====================
* Attributes: see [API](http://developer.github.com/v3/repos/commits/#get-a-single-commit-comment)
* `edit( ... )`: see [API](http://developer.github.com/v3/repos/commits/#update-a-commit-comment) for parameters
* `delete()`

Class `Download`
================
* Attributes: see [API](http://developer.github.com/v3/repos/downloads/#get-a-single-download)
* `delete()`

Class `Label`
=============
* Attributes: see [API](http://developer.github.com/v3/issues/labels/#get-a-single-label)
* `edit( ... )`: see [API](http://developer.github.com/v3/issues/labels/#update-a-label) for parameters
* `delete()`

Class `Issue`
=============
* Attributes: see [API](http://developer.github.com/v3/issues/#get-a-single-issue)
* `edit( ... )`: see [API](http://developer.github.com/v3/issues/#edit-an-issue) for parameters
* `get_labels()`: list of `Label`
* `add_to_labels( label, ... )`
* `set_labels( label, ... )`
* `delete_labels()`
* `remove_from_labels( label )`
* `get_comments()`: list of `IssueComment`
* `create_comment( ... )`: `IssueComment`: see [API](http://developer.github.com/v3/issues/comments/#create-a-comment) for parameters
* `get_comment( id )`: `IssueComment`

Class `IssueComment`
====================
* Attributes: see [API](http://developer.github.com/v3/issues/comments/#get-a-single-comment)
* `edit( ... )`: see [API](http://developer.github.com/v3/issues/comments/#edit-a-comment) for parameters
* `delete()`

Class `Milestone`
================
* Attributes: see [API](http://developer.github.com/v3/issues/milestones/#get-a-single-milestone)
* `edit( ... )`: see [API](http://developer.github.com/v3/issues/milestones/#update-a-milestone) for parameters
* `delete()`
* `get_labels()`: list of `Label`

Class `Team`
============
* Attributes: see [API](http://developer.github.com/v3/orgs/teams/#get-team)
* `edit( ... )`: see [API](http://developer.github.com/v3/orgs/teams/#edit-team) for parameters
* `delete()`

Members
-------
* `get_members()`: list of `NamedUser`
* `has_in_members( user )`: `bool`
* `add_to_members( user )`
* `remove_from_members( user )`

Repositories
------------
* `get_repos()`: list of `Repository`
* `has_in_repos( user )`: `bool`
* `add_to_repos( user )`
* `remove_from_repos( user )`

Class `GitRef`
==============
* Attributes: see [API](http://developer.github.com/v3/git/refs/#get-a-reference)
* `edit( ... )`: see [API](http://developer.github.com/v3/git/refs/#update-a-reference) for parameters

Class `GitBlob`
===============
* Attributes: see [API](http://developer.github.com/v3/git/blobs/#get-a-blob)

Class `GitCommit`
=================
* Attributes: see [API](http://developer.github.com/v3/git/commits/#get-a-commit)

Class `GitTree`
===============
* Attributes: see [API](http://developer.github.com/v3/git/trees/#get-a-tree)

Class `GitTag`
==============
* Attributes: see [API](http://developer.github.com/v3/git/tags/#get-a-tag)

