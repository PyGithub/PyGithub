API `/authorizations`
=====================
* GET: `AuthenticatedUser.get_authorizations`
* POST: `AuthenticatedUser.create_authorization`

API `/authorizations/:id`
=========================
* GET: `AuthenticatedUser.get_authorization`
* PATCH: `Authorization.edit`
* DELETE: `Authorization.delete`

API `/events`
=============
* GET: `AuthenticatedUser.get_events`

API `/gists`
============
* GET: `AuthenticatedUser.get_gists`
* POST: `AuthenticatedUser.create_gist`

API `/gists/:id`
================
* GET: `Github.get_gist`
* PATCH: `Gist.edit`
* DELETE: `Gist.delete`

API `/gists/:id/comments`
=========================
* GET: `Gist.get_comments`
* POST: `Gist.create_comment`

API `/gists/:id/fork`
=====================
* POST: `Gist.create_fork`

API `/gists/:id/star`
=====================
* GET: `Gist.is_starred`
* PUT: `Gist.set_starred`
* DELETE: `Gist.reset_starred`

API `/gists/comments/:id`
=========================
* GET: `Gist.get_comment`
* PATCH: `GistComment.edit`
* DELETE: `GistComment.delete`

API `/gists/public`
===================
* GET: `Github.get_gists`

API `/gists/starred`
====================
* GET: `AuthenticatedUser.get_starred_gists`

API `/hooks`
====================
* GET: `Github.get_hooks`

API `/issues`
=============
* GET: `AuthenticatedUser.get_issues`

API `/legacy/issues/search/:owner/:repository/:state/:keyword`
==============================================================
* GET: `Repository.search_issues`

API `/legacy/repos/search/:keyword`
===================================
* GET: `Github.search_repos`

API `/legacy/user/email/:email`
===============================
* GET: `Github.search_user_by_email`

API `/legacy/user/search/:keyword`
==================================
* GET: `Github.search_users`

API `/markdown`
===============
* POST: `Github.render_markdown`

API `/markdown/raw`
===================
* POST: see API `/markdown`

API `/networks/:user/:repo/events`
==================================
* GET: `Repository.get_network_events`

API `/orgs/:org`
================
* GET: `Github.get_organization`
* PATCH: `Organization.edit`

API `/orgs/:org/events`
=======================
* GET: `Organization.get_events`

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

API `/rate_limit`
=================
* GET: Not implemented, see `Github.rate_limiting`

API `/repos/:user/:repo`
========================
* GET: `AuthenticatedUser.get_repo`, `NamedUser.get_repo` or `Organization.get_repo`
* PATCH: `Repository.edit`
* DELETE: `Repository.delete`

API `/repos/:user/:repo/:archive_format/:ref`
=============================================
* GET: `Repository.get_archive_link`

API `/repos/:user/:repo/assignees`
==================================
* GET: `Repository.get_assignees`

API `/repos/:user/:repo/assignees/:assignee`
============================================
* GET: `Repository.has_in_assignees`

API `/repos/:user/:repo/branches`
=================================
* GET: `Repository.get_branches`

API `/repos/:user/:repo/branches/:branch`
=========================================
* GET: `Repository.get_branch`

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
* GET: `Repository.compare`

API `/repos/:user/:repo/contents/:path`
=======================================
* GET: `Repository.get_contents`

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
* GET: `Repository.get_events`

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
* DELETE: `GitRef.delete`

API `/repos/:user/:repo/git/tags`
=================================
* POST: `Repository.create_git_tag`

API `/repos/:user/:repo/git/tags/:sha`
======================================
* GET: `Repository.get_git_tag`

API `/repos/:user/:repo/git/trees`
==================================
* POST: `Repository.create_git_tree`

API `/repos/:user/:repo/git/trees/:sha`
=======================================
* GET: `Repository.get_git_tree`

API `/repos/:user/:repo/hooks`
==============================
* GET: `Repository.get_hooks`
* POST: `Repository.create_hook`

API `/repos/:user/:repo/hooks/:id`
==================================
* GET: `Repository.get_hook`
* PATCH: `Hook.edit`
* DELETE: `Hook.delete`

API `/repos/:user/:repo/hooks/:id/test`
=======================================
* POST: `Hook.test`

API `/repos/:user/:repo/issues`
===============================
* GET: `Repository.get_issues`
* POST: `Repository.create_issue`

API `/repos/:user/:repo/issues/:number`
=======================================
* GET: `Repository.get_issue`
* PATCH: `Issue.edit`

API `/repos/:user/:repo/issues/:number/comments`
================================================
* GET: `Issue.get_comments` or `PullRequest.get_issue_comments`
* POST: `Issue.create_comment` or `PullRequest.create_issue_comment`

API `/repos/:user/:repo/issues/:number/events`
==============================================
* GET: `Issue.get_events`

API `/repos/:user/:repo/issues/:number/labels`
==============================================
* GET: `Issue.get_labels`
* POST: `Issue.add_to_labels`
* PUT: `Issue.set_labels`
* DELETE: `Issue.delete_labels`

API `/repos/:user/:repo/issues/:number/labels/:name`
====================================================
* DELETE: `Issue.remove_from_labels`

API `/repos/:user/:repo/issues/comments/:id`
============================================
* GET: `Issue.get_comment` or `PullRequest.get_issue_comment`
* PATCH: `IssueComment.edit`
* DELETE: `IssueComment.delete`

API `/repos/:user/:repo/issues/events`
======================================
* GET: `Repository.get_issues_events`

API `/repos/:user/:repo/issues/events/:id`
==========================================
* GET: `Repository.get_issues_event`

API `/repos/:user/:repo/keys`
=============================
* GET: `Repository.get_keys`
* POST: `Repository.create_key`

API `/repos/:user/:repo/keys/:id`
=================================
* GET: `Repository.get_key`
* PATCH: `RepositoryKey.edit`
* DELETE: `RepositoryKey.delete`

API `/repos/:user/:repo/labels`
===============================
* GET: `Repository.get_labels`
* POST: `Repository.create_label`

API `/repos/:user/:repo/labels/:name`
=====================================
* GET: `Repository.get_label`
* PATCH: `Label.edit`
* DELETE: `Label.delete`

API `/repos/:user/:repo/languages`
==================================
* GET: `Repository.get_languages`

API `/repos/:user/:repo/merges`
===============================
* POST: `Repository.merge`

API `/repos/:user/:repo/milestones`
===================================
* GET: `Repository.get_milestones`
* POST: `Repository.create_milestone`

API `/repos/:user/:repo/milestones/:number`
===========================================
* GET: `Repository.get_milestone`
* PATCH: `Milestone.edit`
* DELETE: `Milestone.delete`

API `/repos/:user/:repo/milestones/:number/labels`
==================================================
* GET: `Milestone.get_labels`

API `/repos/:user/:repo/pulls`
==============================
* GET: `Repository.get_pulls`
* POST: `Repository.create_pull`

API `/repos/:user/:repo/pulls/:number`
======================================
* GET: `Repository.get_pull`
* PATCH: `PullRequest.edit`

API `/repos/:user/:repo/pulls/:number/comments`
===============================================
* GET: `PullRequest.get_comments` or `PullRequest.get_review_comments`
* POST: `PullRequest.create_comment` or `PullRequest.create_review_comment`

API `/repos/:user/:repo/pulls/:number/commits`
==============================================
* GET: `PullRequest.get_commits`

API `/repos/:user/:repo/pulls/:number/files`
============================================
* GET: `PullRequest.get_files`

API `/repos/:user/:repo/pulls/:number/merge`
============================================
* GET: `PullRequest.is_merged`
* PUT: `PullRequest.merge`

API `/repos/:user/:repo/pulls/comments/:number`
===============================================
* GET: `PullRequest.get_comment` or `PullRequest.get_review_comment`
* PATCH: `PullRequestComment.edit`
* DELETE: `PullRequestComment.delete`

API `/repos/:user/:repo/readme`
===============================
* GET: `Repository.get_readme`

API `/repos/:user/:repo/stargazers`
===================================
* GET: `Repository.get_stargazers`

API `/repos/:user/:repo/statuses/:sha`
======================================
* GET: `Commit.get_statuses`
* POST: `Commit.create_status`

API `/repos/:user/:repo/subscribers`
====================================
* GET: `Repository.get_subscribers`

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
* GET: `AuthenticatedUser.get_keys`
* POST: `AuthenticatedUser.create_key`

API `/user/keys/:id`
====================
* GET: `AuthenticatedUser.get_key`
* PATCH: `UserKey.edit`
* DELETE: `UserKey.delete`

API `/user/orgs`
================
* GET: `AuthenticatedUser.get_orgs`

API `/user/repos`
=================
* GET: `AuthenticatedUser.get_repos`
* POST: `AuthenticatedUser.create_repo`

API `/user/starred`
===================
* GET: `AuthenticatedUser.get_starred`

API `/user/starred/:user/:repo`
===============================
* GET: `AuthenticatedUser.has_in_starred`
* PUT: `AuthenticatedUser.add_to_starred`
* DELETE: `AuthenticatedUser.remove_from_starred`

API `/user/subscriptions`
=========================
* GET: `AuthenticatedUser.get_subscriptions`

API `/user/subscriptions/:user/:repo`
=====================================
* GET: `AuthenticatedUser.has_in_subscriptions`
* PUT: `AuthenticatedUser.add_to_subscriptions`
* DELETE: `AuthenticatedUser.remove_from_subscriptions`

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
* GET: `NamedUser.get_events`

API `/users/:user/events/orgs/:org`
===================================
* GET: `AuthenticatedUser.get_organization_events`

API `/users/:user/events/public`
================================
* GET: `NamedUser.get_public_events`

API `/users/:user/followers`
============================
* GET: `NamedUser.get_followers`

API `/users/:user/following`
============================
* GET: `NamedUser.get_following`

API `/users/:user/gists`
========================
* GET: `NamedUser.get_gists`
* POST: `NamedUser.create_gist`

API `/users/:user/orgs`
=======================
* GET: `NamedUser.get_orgs`

API `/users/:user/received_events`
==================================
* GET: `NamedUser.get_received_events`

API `/users/:user/received_events/public`
=========================================
* GET: `NamedUser.get_public_received_events`

API `/users/:user/repos`
========================
* GET: `NamedUser.get_repos`

API `/users/:user/starred`
==========================
* GET: `NamedUser.get_starred`

API `/users/:user/subscriptions`
================================
* GET: `NamedUser.get_subscriptions`

API `/users/:user/watched`
==========================
* GET: `NamedUser.get_watched`

