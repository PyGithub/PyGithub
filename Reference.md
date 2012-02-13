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
 - GET: `Github.get_organization( login )`: `Organization`
 - PATCH: `Organization.edit( ... )`

/orgs/:org/events
=================
 - GET: `` (TODO)

/orgs/:org/members
==================
 - GET: `Organization.get_members()`: list of `NamedUser`

/orgs/:org/members/:user
========================
 - GET: `` (TODO)
 - DELETE: `` (TODO)

/orgs/:org/public_members
=========================
 - GET: `Organization.get_public_members()`: list of `NamedUser`

/orgs/:org/public_members/:user
===============================
 - GET: `` (TODO)
 - PUT: `` (TODO)
 - DELETE: `` (TODO)

/orgs/:org/repos
================
 - GET: `Organization.get_repos()`: list of `Repository`
 - POST: `` (TODO)

/orgs/:org/teams
================
 - GET: `` (TODO)
 - POST: `` (TODO)

/repos/:user/:repo
==================
 - GET: `` (TODO)
 - PATCH: `Repository.edit( ... )`

/repos/:user/:repo/branches
===========================
 - GET: `` (TODO)

/repos/:user/:repo/collaborators
================================
 - GET: `Repository.get_collaborators()`: list of `NamedUser`

/repos/:user/:repo/collaborators/:user
======================================
 - GET: `` (TODO)
 - PUT: `` (TODO)
 - DELETE: `` (TODO)

/repos/:user/:repo/comments
===========================
 - GET: `` (TODO)

/repos/:user/:repo/comments/:id
===============================
 - GET: `` (TODO)
 - PATCH: `` (TODO)
 - DELETE: `` (TODO)

/repos/:user/:repo/commits
==========================
 - GET: `` (TODO)

/repos/:user/:repo/commits/:sha
===============================
 - GET: `` (TODO)

/repos/:user/:repo/commits/:sha/comments
========================================
 - GET: `` (TODO)
 - POST: `` (TODO)

/repos/:user/:repo/compare/:base...:head
========================================
 - GET: `` (TODO)

/repos/:user/:repo/contributors
===============================
 - GET: `Repository.get_contributors()`: list of `NamedUser`

/repos/:user/:repo/downloads
============================
 - GET: `` (TODO)
 - POST: `` (TODO)

/repos/:user/:repo/downloads/:id
================================
 - GET: `` (TODO)
 - DELETE: `` (TODO)

/repos/:user/:repo/events
=========================
 - GET: `` (TODO)

/repos/:user/:repo/forks
========================
 - GET: `Repository.get_forks()`: list of `Repository`
 - POST: `` (TODO)

/repos/:user/:repo/git/blobs
============================
 - POST: `` (TODO)

/repos/:user/:repo/git/blobs/:sha
=================================
 - GET: `` (TODO)

/repos/:user/:repo/git/commits
==============================
 - POST: `` (TODO)

/repos/:user/:repo/git/commits/:sha
===================================
 - GET: `` (TODO)

/repos/:user/:repo/git/refs
===========================
 - GET: `` (TODO)
 - POST: `` (TODO)

/repos/:user/:repo/git/refs/:ref
================================
 - GET: `` (TODO)
 - PATCH: `` (TODO)

/repos/:user/:repo/git/tags
===========================
 - POST: `` (TODO)

/repos/:user/:repo/git/tags/:sha
================================
 - GET: `` (TODO)

/repos/:user/:repo/git/trees
============================
 - POST: `` (TODO)

/repos/:user/:repo/git/trees/:sha
=================================
 - GET: `` (TODO)

/repos/:user/:repo/git/trees/:sha?recursive=1
=============================================
 - GET: `` (TODO)

/repos/:user/:repo/hooks
========================
 - GET: `` (TODO)
 - POST: `` (TODO)

/repos/:user/:repo/hooks/:id
============================
 - GET: `` (TODO)
 - PATCH: `` (TODO)
 - DELETE: `` (TODO)

/repos/:user/:repo/hooks/:id/test
=================================
 - POST: `` (TODO)

/repos/:user/:repo/issues
=========================
 - GET: `` (TODO)
 - POST: `` (TODO)

/repos/:user/:repo/issues/:id
=============================
 - GET: `` (TODO)
 - PATCH: `` (TODO)

/repos/:user/:repo/issues/:id/comments
======================================
 - GET: `` (TODO)
 - POST: `` (TODO)

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

/repos/:user/:repo/milestones/:id
=================================
 - GET: `` (TODO)
 - PATCH: `` (TODO)
 - DELETE: `` (TODO)

/repos/:user/:repo/milestones/:id/labels
========================================
 - GET: `` (TODO)

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
 - GET: `Repository.get_watchers()`: list of `NamedUser`

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
 - GET: `Github.get_user()`: `AuthenticatedUser`
 - PATCH: `AuthenticatedUser.edit( ... )`

/user/emails
============
 - GET: `` (TODO)
 - POST: `` (TODO)
 - DELETE: `` (TODO)

/user/followers
===============
 - GET: `AuthenticatedUser.get_followers()` : list of `NamedUser`

/user/following
===============
 - GET: `AuthenticatedUser.get_following()` : list of `NamedUser`

/user/following/:user
=====================
 - GET: `` (TODO)
 - PUT: `AuthenticatedUser.add_following( user )`
 - DELETE: `AuthenticatedUser.remove_following( user )`

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
 - GET: `AuthenticatedUser.get_orgs()` : list of `Organization`

/user/repos
===========
 - GET: `AuthenticatedUser.get_repos()`: list of `Repository`
 - POST: `` (TODO)

/user/watched
=============
 - GET: `AuthenticatedUser.get_watched()`: list of `Repository`

/user/watched/:user/:repo
=========================
 - GET: `` (TODO)
 - PUT: `AuthenticatedUser.add_watched( repo )`
 - DELETE: `AuthenticatedUser.remove_watched( repo )`

/users/:user
============
 - GET: `Github.get_user( login )`: `NamedUser`

/users/:user/events
===================
 - GET: `` (TODO)

/users/:user/events/orgs/:org
=============================
 - GET: `` (TODO)

/users/:user/events/public
==========================
 - GET: `` (TODO)

/users/:user/followers
======================
 - GET: `NamedUser.get_followers()` : list of `NamedUser`

/users/:user/following
======================
 - GET: `NamedUser.get_following()` : list of `NamedUser`

/users/:user/gists
==================
 - GET: `` (TODO)

/users/:user/orgs
=================
 - GET: `NamedUser.get_orgs()` : list of `Organization`

/users/:user/received_events
============================
 - GET: `` (TODO)

/users/:user/received_events/public
===================================
 - GET: `` (TODO)

/users/:user/repos
==================
 - GET: `NamedUser.get_repos()`: list of `Repository`

/users/:user/watched
====================
 - GET: `NamedUser.get_watched()`: list of `Repository`
