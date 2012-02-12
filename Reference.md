In this documentation:

 - `repository` is an instance of `Repository`
 - `name_or_User` is either a string (the name of the user) or an instance of `User`
 - `sha` is a string (the hash of the git object)

/authorizations
===============
 - GET: `` (TODO)
 - POST: `` (TODO)

/authorizations/:id
===================
 - GET: `` (TODO)
 - PATCH: `` (TODO)
 - DELETE: `` (TODO)

/events
=======
 - GET: `` (TODO)

/gists
======
 - GET: `` (TODO)
 - POST: `` (TODO)

/gists/:gist_id/comments
========================
 - GET: `` (TODO)
 - POST: `` (TODO)

/gists/:id
==========
 - GET: `` (TODO)
 - PATCH: `` (TODO)
 - DELETE: `` (TODO)

/gists/:id/fork
===============
 - POST: `` (TODO)

/gists/:id/star
===============
 - GET: `` (TODO)
 - PUT: `` (TODO)
 - DELETE: `` (TODO)

/gists/comments/:id
===================
 - GET: `` (TODO)
 - PATCH: `` (TODO)
 - DELETE: `` (TODO)

/gists/public
=============
 - GET: `` (TODO)

/gists/starred
==============
 - GET: `` (TODO)

/issues
=======
 - GET: `` (TODO)

/networks/:user/:repo/events
============================
 - GET: `` (TODO)

/orgs/:org
==========
 - GET: `Github.organization( name )`: `Organization`
 - PATCH: `Organization.edit( ... )` (TODO)

/orgs/:org/events
=================
 - GET: `Organization.events()`: list of `Event` (TODO)

/orgs/:org/members
==================
 - GET: `Organization.members()`: list of `User`

/orgs/:org/members/:user
========================
 - GET: `Organization.hasMember( name_or_User )`: `boolean` (TODO)
 - DELETE: `Organization.removeMember( name_or_User )` (TODO)

/orgs/:org/public_members
=========================
 - GET: `Organization.publicMembers()`: list of `User`

/orgs/:org/public_members/:user
===============================
 - GET: `Organization.hasPublicMember( name_or_User )`: `boolean` (TODO)
 - PUT: `Organization.addPublicMember( name_or_User )` (TODO)
 - DELETE: `Organization.removePublicMember( name_or_User )` (TODO)

/orgs/:org/repos
================
 - GET: `Organization.repositories()`: list of `Repository`
 - POST: `Organization.createRepository( ... )`: `Repository`

/orgs/:org/teams
================
 - GET: `Organization.teams()`: list of `Team` (TODO)
 - POST: `Organization.createTeam( ... )`: `Team` (TODO)

/repos/:user/:repo
==================
 - GET: `User.repository( name )`: `Repository`
 - PATCH: `Repository.edit( ... )`

/repos/:user/:repo/branches
===========================
 - GET: `Repository.branches()`: list of `Branch` (TODO)

/repos/:user/:repo/collaborators
================================
 - GET: `Repository.collaborators()`: list of `User`

/repos/:user/:repo/collaborators/:user
======================================
 - GET: `Repository.hasCollaborator( name_or_User )`: `boolean` (TODO)
 - PUT: `Repository.addCollaborator( name_or_User )` (TODO)
 - DELETE: `Repository.removeCollaborator( name_or_User )` (TODO)

/repos/:user/:repo/comments
===========================
 - GET: `Repository.comments()`: list of `Comment` (TODO)

/repos/:user/:repo/comments/:id
===============================
 - GET: `Repository.comment( id )`: `Comment` (TODO)
 - PATCH: `Comment.edit( ... )` (TODO)
 - DELETE: `Comment.delete()` (TODO)

/repos/:user/:repo/commits
==========================
 - GET: `Repository.commits()`: list of `Commit` (TODO)

/repos/:user/:repo/commits/:sha
===============================
 - GET: `Repository.commit( sha )`: `Commit` (TODO)

/repos/:user/:repo/commits/:sha/comments
========================================
 - GET: `Commit.comments()`: list of `Comment` (TODO)
 - POST: `Commit.addComment( ... )`: `Comment` (TODO)

/repos/:user/:repo/compare/:base...:head
========================================
 - GET: `` (TODO)

/repos/:user/:repo/contributors
===============================
 - GET: `Repository.contributors()`: list of `User`

/repos/:user/:repo/downloads
============================
 - GET: `Repository.downloads()`: list of `Download` (TODO)
 - POST: `Repository.createDownload( ... )`: `Download` (TODO)

/repos/:user/:repo/downloads/:id
================================
 - GET: `Repository.download( id )`: `Download` (TODO)
 - DELETE: `Download.delete()` (TODO)

/repos/:user/:repo/events
=========================
 - GET: `Repository.events`: list of `Event` (TODO)

/repos/:user/:repo/forks
========================
 - GET: `Repository.forks()`: list of `Repository`
 - POST: `User.createFork( repository )`: `Repository`

/repos/:user/:repo/git/blobs
============================
 - POST: `Repository.createBlob( ... )`: `GitBlob` (TODO)

/repos/:user/:repo/git/blobs/:sha
=================================
 - GET: `Repository.gitBlob( sha )`: `GitBlob` (TODO)

/repos/:user/:repo/git/commits
==============================
 - POST: `Repository.createCommit( ... )`: `GitCommit` (TODO)

/repos/:user/:repo/git/commits/:sha
===================================
 - GET: `Repository.gitCommit( sha )`: `GitCommit` (TODO)

/repos/:user/:repo/git/refs
===========================
 - GET: `Repository.gitReferences()`: list of `GitReference` (TODO)
 - POST: `Repository.createReference( ... )`: `GitReference` (TODO)

/repos/:user/:repo/git/refs/:ref
================================
 - GET: `Repository.gitReference( ... )`: `GitReference` (TODO)
 - PATCH: `GitReference.edit( ... )` (TODO)

/repos/:user/:repo/git/tags
===========================
 - POST: `Repository.gitTags()`: list of `GitTag` (TODO)

/repos/:user/:repo/git/tags/:sha
================================
 - GET: `Repository.gitTag( sha )`: `GitTag` (TODO)

/repos/:user/:repo/git/trees
============================
 - POST: `Repository.createTree( ... )`: `GitTree` (TODO)

/repos/:user/:repo/git/trees/:sha
=================================
 - GET: `Repository.gitTree( sha )`: `GitTree` (TODO)

/repos/:user/:repo/git/trees/:sha?recursive=1
=============================================
 - GET: `` (TODO)

/repos/:user/:repo/hooks
========================
 - GET: `Repository.hooks()`: list of `Hook` (TODO)
 - POST: `Repository.addHook( ... )`: `Hook` (TODO)

/repos/:user/:repo/hooks/:id
============================
 - GET: `Repository.Hook( id )`: `Hook` (TODO)
 - PATCH: `Hook.edit( ... )` (TODO)
 - DELETE: `Hook.delete()` (TODO)

/repos/:user/:repo/hooks/:id/test
=================================
 - POST: `Hook.test()` (TODO)

/repos/:user/:repo/issues
=========================
 - GET: `Repository.issues()`: list of `Issue` (TODO)
 - POST: `Repository.addIssue( ... )`: `Issue` (TODO)

/repos/:user/:repo/issues/:id
=============================
 - GET: `Repository.get_issue( id )`: `Issue` (TODO)
 - PATCH: `Issue.edit( ... )` (TODO)

/repos/:user/:repo/issues/:id/comments
======================================
 - GET: `Issue.comments()`: list of `Comment` (TODO)
 - POST: `Issue.addComment( ... )`: `Comment` (TODO)

/repos/:user/:repo/issues/:id/labels
====================================
 - GET: `` (TODO)
 - POST: `` (TODO)
 - PUT: `` (TODO)
 - DELETE: `` (TODO)

/repos/:user/:repo/issues/:id/labels/:id
========================================
 - DELETE: `` (TODO)

/repos/:user/:repo/issues/:issue_id/events
==========================================
 - GET: `` (TODO)

/repos/:user/:repo/issues/comments/:id
======================================
 - GET: `` (TODO)
 - PATCH: `` (TODO)
 - DELETE: `` (TODO)

/repos/:user/:repo/issues/events
================================
 - GET: `` (TODO)

/repos/:user/:repo/issues/events/:id
====================================
 - GET: `` (TODO)

/repos/:user/:repo/keys
=======================
 - GET: `` (TODO)
 - POST: `` (TODO)

/repos/:user/:repo/keys/:id
===========================
 - GET: `` (TODO)
 - PATCH: `` (TODO)
 - DELETE: `` (TODO)

/repos/:user/:repo/labels
=========================
 - GET: `` (TODO)
 - POST: `` (TODO)

/repos/:user/:repo/labels/:id
=============================
 - GET: `` (TODO)
 - PATCH: `` (TODO)
 - DELETE: `` (TODO)

/repos/:user/:repo/languages
============================
 - GET: `` (TODO)

/repos/:user/:repo/milestones
=============================
 - GET: `` (TODO)
 - POST: `` (TODO)

/repos/:user/:repo/milestones/:id/labels
========================================
 - GET: `` (TODO)

/repos/:user/:repo/milestones/:number
=====================================
 - GET: `` (TODO)
 - PATCH: `` (TODO)
 - DELETE: `` (TODO)

/repos/:user/:repo/pulls
========================
 - GET: `` (TODO)
 - POST: `` (TODO)

/repos/:user/:repo/pulls/:id
============================
 - GET: `` (TODO)
 - PATCH: `` (TODO)

/repos/:user/:repo/pulls/:id/comments
=====================================
 - GET: `` (TODO)
 - POST: `` (TODO)

/repos/:user/:repo/pulls/:id/commits
====================================
 - GET: `` (TODO)

/repos/:user/:repo/pulls/:id/files
==================================
 - GET: `` (TODO)

/repos/:user/:repo/pulls/:id/merge
==================================
 - GET: `` (TODO)
 - PUT: `` (TODO)

/repos/:user/:repo/pulls/comments/:id
=====================================
 - GET: `` (TODO)
 - PATCH: `` (TODO)
 - DELETE: `` (TODO)

/repos/:user/:repo/tags
=======================
 - GET: `` (TODO)

/repos/:user/:repo/teams
========================
 - GET: `` (TODO)

/repos/:user/:repo/watchers
===========================
 - GET: `Repository.watchers()` : list of `User`

/teams/:id
==========
 - GET: `` (TODO)
 - PATCH: `` (TODO)
 - DELETE: `` (TODO)

/teams/:id/members
==================
 - GET: `` (TODO)

/teams/:id/members/:user
========================
 - GET: `` (TODO)
 - PUT: `` (TODO)
 - DELETE: `` (TODO)

/teams/:id/repos
================
 - GET: `` (TODO)

/teams/:id/repos/:user/:repo
============================
 - GET: `` (TODO)
 - PUT: `` (TODO)
 - DELETE: `` (TODO)

/user
=====
 - GET: `User` (TODO)
 - PATCH: `User.edit( ... )`

/user/emails
============
 - GET: `` (TODO)
 - POST: `` (TODO)
 - DELETE: `` (TODO)

/user/followers
===============
 - GET: `User.followers()`: list of `User`

/user/following
===============
 - GET: `User.following()`: list of `User`

/user/following/:user
=====================
 - GET: `User.isFollowing( name_or_User )`: `boolean` (TODO)
 - PUT: `User.startFollowing( name_or_User )` (TODO)
 - DELETE: `User.stopFollowing( name_or_User )` (TODO)

/user/keys
==========
 - GET: `` (TODO)
 - POST: `` (TODO)

/user/keys/:id
==============
 - GET: `` (TODO)
 - PATCH: `` (TODO)
 - DELETE: `` (TODO)

/user/orgs
==========
 - GET: `` (TODO)

/user/repos
===========
 - GET: `User.repositories()`: list of `Repository`
 - POST: `User.createRepository( ... )`: `Repository`

/user/watched
=============
 - GET: `User.watched()`: list of `Repository`

/user/watched/:user/:repo
=========================
 - GET: `User.isWatching( repository )`: `boolean` (TODO)
 - PUT: `User.startWatching( repository )` (TODO)
 - DELETE: `User.stopWatching( repository )` (TODO)

/users/:user
============
 - GET: `Github.user()`: `User`

/users/:user/events
===================
 - GET: `User.events()`: list of `Event` (TODO)

/users/:user/events/orgs/:org
=============================
 - GET: `` (TODO)

/users/:user/events/public
==========================
 - GET: `` (TODO)

/users/:user/followers
======================
 - GET: `User.followers()`: list of `User`

/users/:user/following
======================
 - GET: `User.following()`: list of `User`

/users/:user/gists
==================
 - GET: `` (TODO)

/users/:user/orgs
=================
 - GET: `` (TODO)

/users/:user/received_events
============================
 - GET: `` (TODO)

/users/:user/received_events/public
===================================
 - GET: `` (TODO)

/users/:user/repos
==================
 - GET: `User.repositories`: list of `Repository`

/users/:user/watched
====================
 - GET: `User.watched()`: list of `Repository`
