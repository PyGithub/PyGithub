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
* GET: `Github.get_organization`
* PATCH: `Organization.edit`

API `/orgs/:org/events`
=======================
* GET: (TODO)

API `/orgs/:org/members`
========================
* GET: `Organization.get_members`

API `/orgs/:org/members/:user`
==============================
* GET: `Organization.has_in_members`
* DELETE: `Organization.remove_from_members`

API `/orgs/:org/public_members`
===============================
* GET: `Organization.get_public_members`

API `/orgs/:org/public_members/:user`
=====================================
* GET: `Organization.has_in_public_members`
* PUT: `Organization.add_to_public_members`
* DELETE: `Organization.remove_from_public_members`

API `/orgs/:org/repos`
======================
* GET: `Organization.get_repos`
* POST: `Organization.create_repo`

API `/orgs/:org/teams`
======================
* GET: `Organization.get_teams`
* POST: `Organization.create_team`

API `/repos/:user/:repo`
========================
* GET: `AuthenticatedUser.get_repo`, `NamedUser.get_repo` or `Organization.get_repo`
* PATCH: `Repository.edit`

API `/repos/:user/:repo/branches`
=================================
* GET: `Repository.get_branches`

API `/repos/:user/:repo/collaborators`
======================================
* GET: `Repository.get_collaborators`

API `/repos/:user/:repo/collaborators/:user`
============================================
* GET: `Repository.has_in_collaborators`
* PUT: `Repository.add_to_collaborators`
* DELETE: `Repository.remove_from_collaborators`

API `/repos/:user/:repo/comments`
=================================
* GET: `Repository.get_comments`

API `/repos/:user/:repo/comments/:id`
=====================================
* GET: `Repository.get_comment`
* PATCH: `CommitComment.edit`
* DELETE: `CommitComment.delete`

API `/repos/:user/:repo/commits`
================================
* GET: `Repository.get_commits`

API `/repos/:user/:repo/commits/:sha`
=====================================
* GET: `Repository.get_commit`

API `/repos/:user/:repo/commits/:sha/comments`
==============================================
* GET: `Commit.get_comments`
* POST: `Commit.create_comment`

API `/repos/:user/:repo/compare/:base...:head`
==============================================
* GET: (TODO)

API `/repos/:user/:repo/contributors`
=====================================
* GET: `Repository.get_contributors`

API `/repos/:user/:repo/downloads`
==================================
* GET: `Repository.get_downloads`
* POST: `Repository.create_download`

API `/repos/:user/:repo/downloads/:id`
======================================
* GET: `Repository.get_download`
* DELETE: `Download.delete`

API `/repos/:user/:repo/events`
===============================
* GET: (TODO)

API `/repos/:user/:repo/forks`
==============================
* GET: `Repository.get_forks`
* POST: `AuthenticatedUser.create_fork`

API `/repos/:user/:repo/git/blobs`
==================================
* POST: `Repository.create_git_blob`

API `/repos/:user/:repo/git/blobs/:sha`
=======================================
* GET: `Repository.get_git_blob`

API `/repos/:user/:repo/git/commits`
====================================
* POST: `Repository.create_git_commit`

API `/repos/:user/:repo/git/commits/:sha`
=========================================
* GET: `Repository.get_git_commit`

API `/repos/:user/:repo/git/refs`
=================================
* GET: `Repository.get_git_refs`
* POST: `Repository.create_git_ref`

API `/repos/:user/:repo/git/refs/:ref`
======================================
* GET: `Repository.get_git_ref`
* PATCH: `GitRef.edit`

API `/repos/:user/:repo/git/tags`
=================================
* POST: `Repository.create_git_tag`

API `/repos/:user/:repo/git/tags/:sha`
======================================
* GET: `Repository.get_git_tag`

API `/repos/:user/:repo/git/trees`
==================================
* POST: `Repository.create_git_tree`

API `/repos/:user/:repo/git/trees?base_tree=`
=============================================
* POST: `GitTree.create_update` (TODO)

API `/repos/:user/:repo/git/trees/:sha`
=======================================
* GET: `Repository.get_git_tree`

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
* GET: `Repository.get_issues`
* POST: `Repository.create_issue`

API `/repos/:user/:repo/issues/:id`
===================================
* GET: `Repository.get_issue`
* PATCH: `Issue.edit`

API `/repos/:user/:repo/issues/:id/comments`
============================================
* GET: `Issue.get_comments`
* POST: `Issue.create_comment`

API `/repos/:user/:repo/issues/:id/labels`
==========================================
* GET: `Issue.get_labels`
* POST: `Issue.add_to_labels`
* PUT: `Issue.set_labels`
* DELETE: `Issue.delete_labels`

API `/repos/:user/:repo/issues/:id/labels/:name`
================================================
* DELETE: `Issue.remove_from_labels`

API `/repos/:user/:repo/issues/:id/events`
==========================================
* GET: (TODO)

API `/repos/:user/:repo/issues/comments/:id`
============================================
* GET: `Issue.get_comment`
* PATCH: `IssueComment.edit`
* DELETE: `IssueComment.delete`

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
* GET: `Repository.get_labels`
* POST: `Repository.create_label`

API `/repos/:user/:repo/labels/:id`
===================================
* GET: `Repository.get_label`
* PATCH: `Label.edit`
* DELETE: `Label.delete`

API `/repos/:user/:repo/languages`
==================================
* GET: `Repository.get_languages`

API `/repos/:user/:repo/milestones`
===================================
* GET: `Repository.get_milestones`
* POST: `Repository.create_milestone`

API `/repos/:user/:repo/milestones/:number`
=======================================
* GET: `Repository.get_milestone`
* PATCH: `Milestone.edit`
* DELETE: `Milestone.delete`

API `/repos/:user/:repo/milestones/:number/labels`
==============================================
* GET: `Milestone.get_labels`

API `/repos/:user/:repo/pulls`
==============================
* GET: `Repository.get_pulls`
* POST: `Repository.create_pull` (TODO: alternative input)

API `/repos/:user/:repo/pulls/:id`
==================================
* GET: `Repository.get_pull`
* PATCH: `PullRequest.edit`

API `/repos/:user/:repo/pulls/:id/comments`
===========================================
* GET: `PullRequest.get_comments`
* POST: `PullRequest.create_comment` (TODO: alternative input)

API `/repos/:user/:repo/pulls/:id/commits`
==========================================
* GET: `PullRequest.get_commits`

API `/repos/:user/:repo/pulls/:id/files`
========================================
* GET: `PullRequest.get_files`

API `/repos/:user/:repo/pulls/:id/merge`
========================================
* GET: (TODO)
* PUT: (TODO)

API `/repos/:user/:repo/pulls/comments/:id`
===========================================
* GET: `PullRequest.get_comment`
* PATCH: `PullRequestComment.edit`
* DELETE: `PullRequestComment.delete`

API `/repos/:user/:repo/tags`
=============================
* GET: `Repository.get_tags`

API `/repos/:user/:repo/teams`
==============================
* GET: `Repository.get_teams`

API `/repos/:user/:repo/watchers`
=================================
* GET: `Repository.get_watchers`

API `/teams/:id`
================
* GET: Lazy completion of `Team`
* PATCH: `Team.edit`
* DELETE: `Team.delete`

API `/teams/:id/members`
========================
* GET: `Team.get_members`

API `/teams/:id/members/:user`
==============================
* GET: `Team.has_in_members`
* PUT: `Team.add_to_members`
* DELETE: `Team.remove_from_members`

API `/teams/:id/repos`
======================
* GET: `Team.get_repos`

API `/teams/:id/repos/:user/:repo`
==================================
* GET: `Team.has_in_repos`
* PUT: `Team.add_to_repos`
* DELETE: `Team.remove_from_repos`

API `/user`
===========
* GET: `Github.get_user`
* PATCH: `AuthenticatedUser.edit`

API `/user/emails`
==================
* GET: `AuthenticatedUser.get_emails`
* POST: `AuthenticatedUser.add_to_emails`
* DELETE: `AuthenticatedUser.remove_from_emails`

API `/user/followers`
=====================
* GET: `AuthenticatedUser.get_followers`

API `/user/following`
=====================
* GET: `AuthenticatedUser.get_following`

API `/user/following/:user`
===========================
* GET: `AuthenticatedUser.has_in_following`
* PUT: `AuthenticatedUser.add_to_following`
* DELETE: `AuthenticatedUser.remove_from_following`

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
* GET: `AuthenticatedUser.get_orgs`

API `/user/repos`
=================
* GET: `AuthenticatedUser.get_repos`
* POST: `AuthenticatedUser.create_repo`

API `/user/watched`
===================
* GET: `AuthenticatedUser.get_watched`

API `/user/watched/:user/:repo`
===============================
* GET: `AuthenticatedUser.has_in_watched`
* PUT: `AuthenticatedUser.add_to_watched`
* DELETE: `AuthenticatedUser.remove_from_watched`

API `/users/:user`
==================
* GET: `Github.get_user`

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
* GET: `NamedUser.get_followers`

API `/users/:user/following`
============================
* GET: `NamedUser.get_following`

API `/users/:user/gists`
========================
* GET: (TODO)

API `/users/:user/orgs`
=======================
* GET: `NamedUser.get_orgs`

API `/users/:user/received_events`
==================================
* GET: (TODO)

API `/users/:user/received_events/public`
=========================================
* GET: (TODO)

API `/users/:user/repos`
========================
* GET: `NamedUser.get_repos`

API `/users/:user/watched`
==========================
* GET: `NamedUser.get_watched`
