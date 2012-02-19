API `/authorizations`
=====================
* GET: (TODO)
* POST: (TODO)

API `/authorizations/:id`
=========================
* GET: (TODO)
* PATCH: (TODO)
* DELETE: (TODO)

API `/events`
=============
* GET: (TODO)

API `/gists`
============
* GET: (TODO)
* POST: (TODO)

API `/gists/:gist_id/comments`
==============================
* GET: (TODO)
* POST: (TODO)

API `/gists/:id`
================
* GET: (TODO)
* PATCH: (TODO)
* DELETE: (TODO)

API `/gists/:id/fork`
=====================
* POST: (TODO)

API `/gists/:id/star`
=====================
* GET: (TODO)
* PUT: (TODO)
* DELETE: (TODO)

API `/gists/comments/:id`
=========================
* GET: (TODO)
* PATCH: (TODO)
* DELETE: (TODO)

API `/gists/public`
===================
* GET: (TODO)

API `/gists/starred`
====================
* GET: (TODO)

API `/issues`
=============
* GET: (TODO)

API `/networks/:user/:repo/events`
==================================
* GET: (TODO)

API `/orgs/:org`
================
* GET: `Github.get_organization( login )`: `Organization`
* PATCH: `Organization.edit( ... )`

API `/orgs/:org/events`
=======================
* GET: (TODO)

API `/orgs/:org/members`
========================
* GET: `Organization.get_members()`: list of `NamedUser`

API `/orgs/:org/members/:user`
==============================
* GET: `Organization.has_in_members( user )`: `bool`
* DELETE: `Organization.remove_from_members( user )`

API `/orgs/:org/public_members`
===============================
* GET: `Organization.get_public_members()`: list of `NamedUser`

API `/orgs/:org/public_members/:user`
=====================================
* GET: `Organization.has_in_public_members( user )`: `bool`
* PUT: `Organization.add_to_public_members( user )`
* DELETE: `Organization.remove_from_public_members( user )`

API `/orgs/:org/repos`
======================
* GET: `Organization.get_repos()`: list of `Repository`
* POST: `Organization.create_repo( ... )`: `Repository`

API `/orgs/:org/teams`
======================
* GET: `Organization.get_teams()`: list of `Team` (TODO SOON)
* POST: `Organization.create_team( ... ): `Team` (TODO SOON)

API `/repos/:user/:repo`
========================
* GET: `AuthenticatedUser.get_repo( name )`, `NamedUser.get_repo( name )` or `Organization.get_repo( name )`: `Repository`
* PATCH: `Repository.edit( ... )`

API `/repos/:user/:repo/branches`
=================================
* GET: (TODO)

API `/repos/:user/:repo/collaborators`
======================================
* GET: `Repository.get_collaborators()`: list of `NamedUser`

API `/repos/:user/:repo/collaborators/:user`
============================================
* GET: `Repository.has_in_collaborators( user )`: `bool`
* PUT: `Repository.add_to_collaborators( user )`
* DELETE: `Repository.remove_from_collaborators( user )`

API `/repos/:user/:repo/comments`
=================================
* GET: (TODO)

API `/repos/:user/:repo/comments/:id`
=====================================
* GET: (TODO)
* PATCH: (TODO)
* DELETE: (TODO)

API `/repos/:user/:repo/commits`
================================
* GET: (TODO)

API `/repos/:user/:repo/commits/:sha`
=====================================
* GET: (TODO)

API `/repos/:user/:repo/commits/:sha/comments`
==============================================
* GET: (TODO)
* POST: (TODO)

API `/repos/:user/:repo/compare/:base...:head`
==============================================
* GET: (TODO)

API `/repos/:user/:repo/contributors`
=====================================
* GET: `Repository.get_contributors()`: list of `NamedUser`

API `/repos/:user/:repo/downloads`
==================================
* GET: (TODO)
* POST: (TODO)

API `/repos/:user/:repo/downloads/:id`
======================================
* GET: (TODO)
* DELETE: (TODO)

API `/repos/:user/:repo/events`
===============================
* GET: (TODO)

API `/repos/:user/:repo/forks`
==============================
* GET: `Repository.get_forks()`: list of `Repository`
* POST: `AuthenticatedUser.create_fork( repo )` or `Organization.create_fork( repo )`: `Repository`

API `/repos/:user/:repo/git/blobs`
==================================
* POST: `Repository.create_git_blob( ... )`: `GitBlob`

API `/repos/:user/:repo/git/blobs/:sha`
=======================================
* GET: `Repository.get_git_blob( sha )`: `GitBlob`

API `/repos/:user/:repo/git/commits`
====================================
* POST: `Repository.create_git_commit( ... )`: `GitCommit`

API `/repos/:user/:repo/git/commits/:sha`
=========================================
* GET: `Repository.get_git_commit( sha )`: `GitCommit`

API `/repos/:user/:repo/git/refs`
=================================
* GET: `Repository.get_git_refs()`: list of `GitRef`
* POST: `Repository.create_git_ref( ... )`: `GitRef`

API `/repos/:user/:repo/git/refs/:ref`
======================================
* GET: `Repository.get_git_ref( ref )`: `GitRef`
* PATCH: `GitRef.edit( ... )`

API `/repos/:user/:repo/git/tags`
=================================
* POST: `Repository.create_git_tag( ... )`: `GitTag`

API `/repos/:user/:repo/git/tags/:sha`
======================================
* GET: `Repository.get_git_tag( sha )`: `GitTag`

API `/repos/:user/:repo/git/trees`
==================================
* POST: `Repository.create_git_tree( ... )`: `GitTree`

API `/repos/:user/:repo/git/trees?base_tree=`
=============================================
* POST: `GitTree.create_update( ... )`: `GitTree` (TODO)

API `/repos/:user/:repo/git/trees/:sha`
=======================================
* GET: `Repository.get_git_tree( sha )`: `GitTree`

API `/repos/:user/:repo/git/trees/:sha?recursive=1`
===================================================
* GET: (TODO)

API `/repos/:user/:repo/hooks`
==============================
* GET: (TODO)
* POST: (TODO)

API `/repos/:user/:repo/hooks/:id`
==================================
* GET: (TODO)
* PATCH: (TODO)
* DELETE: (TODO)

API `/repos/:user/:repo/hooks/:id/test`
=======================================
* POST: (TODO)

API `/repos/:user/:repo/issues`
===============================
* GET: (TODO)
* POST: (TODO)

API `/repos/:user/:repo/issues/:id`
===================================
* GET: (TODO)
* PATCH: (TODO)

API `/repos/:user/:repo/issues/:id/comments`
============================================
* GET: (TODO)
* POST: (TODO)

API `/repos/:user/:repo/issues/:id/labels`
==========================================
* GET: (TODO)
* POST: (TODO)
* PUT: (TODO)
* DELETE: (TODO)

API `/repos/:user/:repo/issues/:id/labels/:id`
==============================================
* DELETE: (TODO)

API `/repos/:user/:repo/issues/:issue_id/events`
================================================
* GET: (TODO)

API `/repos/:user/:repo/issues/comments/:id`
============================================
* GET: (TODO)
* PATCH: (TODO)
* DELETE: (TODO)

API `/repos/:user/:repo/issues/events`
======================================
* GET: (TODO)

API `/repos/:user/:repo/issues/events/:id`
==========================================
* GET: (TODO)

API `/repos/:user/:repo/keys`
=============================
* GET: (TODO)
* POST: (TODO)

API `/repos/:user/:repo/keys/:id`
=================================
* GET: (TODO)
* PATCH: (TODO)
* DELETE: (TODO)

API `/repos/:user/:repo/labels`
===============================
* GET: (TODO)
* POST: (TODO)

API `/repos/:user/:repo/labels/:id`
===================================
* GET: (TODO)
* PATCH: (TODO)
* DELETE: (TODO)

API `/repos/:user/:repo/languages`
==================================
* GET: (TODO)

API `/repos/:user/:repo/milestones`
===================================
* GET: (TODO)
* POST: (TODO)

API `/repos/:user/:repo/milestones/:id`
=======================================
* GET: (TODO)
* PATCH: (TODO)
* DELETE: (TODO)

API `/repos/:user/:repo/milestones/:id/labels`
==============================================
* GET: (TODO)

API `/repos/:user/:repo/pulls`
==============================
* GET: (TODO)
* POST: (TODO)

API `/repos/:user/:repo/pulls/:id`
==================================
* GET: (TODO)
* PATCH: (TODO)

API `/repos/:user/:repo/pulls/:id/comments`
===========================================
* GET: (TODO)
* POST: (TODO)

API `/repos/:user/:repo/pulls/:id/commits`
==========================================
* GET: (TODO)

API `/repos/:user/:repo/pulls/:id/files`
========================================
* GET: (TODO)

API `/repos/:user/:repo/pulls/:id/merge`
========================================
* GET: (TODO)
* PUT: (TODO)

API `/repos/:user/:repo/pulls/comments/:id`
===========================================
* GET: (TODO)
* PATCH: (TODO)
* DELETE: (TODO)

API `/repos/:user/:repo/tags`
=============================
* GET: (TODO)

API `/repos/:user/:repo/teams`
==============================
* GET: `Repository.get_teams()`: list of `Team` (TODO SOON)

API `/repos/:user/:repo/watchers`
=================================
* GET: `Repository.get_watchers()`: list of `NamedUser`

API `/teams/:id`
================
* GET: Lazy completion of `Team` (TODO SOON)
* PATCH: `Team.edit( ... )` (TODO SOON)
* DELETE: `Team.delete()` (TODO SOON)

API `/teams/:id/members`
========================
* GET: `Team.get_members()`: list of `NamedUser` (TODO SOON)

API `/teams/:id/members/:user`
==============================
* GET: `Team.has_in_members( user )`: `bool` (TODO SOON)
* PUT: `Team.add_to_members( user )` (TODO SOON)
* DELETE: `Team.remove_from_members( user )` (TODO SOON)

API `/teams/:id/repos`
======================
* GET: `Team.get_repos()`: list of `Repository` (TODO SOON)

API `/teams/:id/repos/:user/:repo`
==================================
* GET: `Team.has_in_repos( repo )`: `bool` (TODO SOON)
* PUT: `Team.add_to_repos( repo )` (TODO SOON)
* DELETE: `Team.remove_from_repos( repo )` (TODO SOON)

API `/user`
===========
* GET: `Github.get_user()`: `AuthenticatedUser`
* PATCH: `AuthenticatedUser.edit( ... )`

API `/user/emails`
==================
* GET: (TODO)
* POST: (TODO)
* DELETE: (TODO)

API `/user/followers`
=====================
* GET: `AuthenticatedUser.get_followers()` : list of `NamedUser`

API `/user/following`
=====================
* GET: `AuthenticatedUser.get_following()` : list of `NamedUser`

API `/user/following/:user`
===========================
* GET: `AuthenticatedUser.has_in_following( user )`: `bool`
* PUT: `AuthenticatedUser.add_to_following( user )`
* DELETE: `AuthenticatedUser.remove_from_following( user )`

API `/user/keys`
================
* GET: (TODO)
* POST: (TODO)

API `/user/keys/:id`
====================
* GET: (TODO)
* PATCH: (TODO)
* DELETE: (TODO)

API `/user/orgs`
================
* GET: `AuthenticatedUser.get_orgs()` : list of `Organization`

API `/user/repos`
=================
* GET: `AuthenticatedUser.get_repos()`: list of `Repository`
* POST: `AuthenticatedUser.create_repo( ... )`: `Repository`

API `/user/watched`
===================
* GET: `AuthenticatedUser.get_watched()`: list of `Repository`

API `/user/watched/:user/:repo`
===============================
* GET: `AuthenticatedUser.has_in_watched( repo )`: `bool`
* PUT: `AuthenticatedUser.add_to_watched( repo )`
* DELETE: `AuthenticatedUser.remove_from_watched( repo )`

API `/users/:user`
==================
* GET: `Github.get_user( login )`: `NamedUser`

API `/users/:user/events`
=========================
* GET: (TODO)

API `/users/:user/events/orgs/:org`
===================================
* GET: (TODO)

API `/users/:user/events/public`
================================
* GET: (TODO)

API `/users/:user/followers`
============================
* GET: `NamedUser.get_followers()` : list of `NamedUser`

API `/users/:user/following`
============================
* GET: `NamedUser.get_following()` : list of `NamedUser`

API `/users/:user/gists`
========================
* GET: (TODO)

API `/users/:user/orgs`
=======================
* GET: `NamedUser.get_orgs()` : list of `Organization`

API `/users/:user/received_events`
==================================
* GET: (TODO)

API `/users/:user/received_events/public`
=========================================
* GET: (TODO)

API `/users/:user/repos`
========================
* GET: `NamedUser.get_repos()`: list of `Repository`

API `/users/:user/watched`
==========================
* GET: `NamedUser.get_watched()`: list of `Repository`
