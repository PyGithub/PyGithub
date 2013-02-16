APIs
====

* ``/authorizations``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_authorizations`
  * POST: :meth:`github.AuthenticatedUser.AuthenticatedUser.create_authorization`

* ``/authorizations/:id``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_authorization`
  * PATCH: :meth:`github.Authorization.Authorization.edit`
  * DELETE: :meth:`github.Authorization.Authorization.delete`

* ``/events``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_events`

* ``/gists``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_gists`
  * POST: :meth:`github.AuthenticatedUser.AuthenticatedUser.create_gist`

* ``/gists/:id``

  * GET: :meth:`github.Github.Github.get_gist`
  * PATCH: :meth:`github.Gist.Gist.edit`
  * DELETE: :meth:`github.Gist.Gist.delete`

* ``/gists/:id/comments``

  * GET: :meth:`github.Gist.Gist.get_comments`
  * POST: :meth:`github.Gist.Gist.create_comment`

* ``/gists/:id/fork``

  * POST: :meth:`github.Gist.Gist.create_fork`

* ``/gists/:id/star``

  * GET: :meth:`github.Gist.Gist.is_starred`
  * PUT: :meth:`github.Gist.Gist.set_starred`
  * DELETE: :meth:`github.Gist.Gist.reset_starred`

* ``/gists/comments/:id``

  * GET: :meth:`github.Gist.Gist.get_comment`
  * PATCH: :meth:`github.GistComment.GistComment.edit`
  * DELETE: :meth:`github.GistComment.GistComment.delete`

* ``/gists/public``

  * GET: :meth:`github.Github.Github.get_gists`

* ``/gists/starred``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_starred_gists`

* ``/gitignore/templates``

  * GET: :meth:`github.Github.Github.get_gitignore_templates`

* ``/gitignore/templates/:name``

  * GET: :meth:`github.Github.Github.get_gitignore_template`

* ``/hooks``

  * GET: :meth:`github.Github.Github.get_hooks`

* ``/hub``

  * POST: :meth:`github.Repository.Repository.subscribe_to_hub` or :meth:`github.Repository.Repository.unsubscribe_to_hub`

* ``/issues``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_issues`

* ``/legacy/issues/search/:owner/:repository/:state/:keyword``

  * GET: :meth:`github.Repository.Repository.legacy_search_issues`

* ``/legacy/repos/search/:keyword``

  * GET: :meth:`github.Github.Github.legacy_search_repos`

* ``/legacy/user/email/:email``

  * GET: :meth:`github.Github.Github.legacy_search_user_by_email`

* ``/legacy/user/search/:keyword``

  * GET: :meth:`github.Github.Github.legacy_search_users`

* ``/markdown``

  * POST: :meth:`github.Github.Github.render_markdown`

* ``/markdown/raw``

  * POST: see ``/markdown``

* ``/networks/:user/:repo/events``

  * GET: :meth:`github.Repository.Repository.get_network_events`

* ``/orgs/:org``

  * GET: :meth:`github.Github.Github.get_organization`
  * PATCH: :meth:`github.Organization.Organization.edit`

* ``/orgs/:org/events``

  * GET: :meth:`github.Organization.Organization.get_events`

* ``/orgs/:org/members``

  * GET: :meth:`github.Organization.Organization.get_members`

* ``/orgs/:org/members/:user``

  * GET: :meth:`github.Organization.Organization.has_in_members`
  * DELETE: :meth:`github.Organization.Organization.remove_from_members`

* ``/orgs/:org/public_members``

  * GET: :meth:`github.Organization.Organization.get_public_members`

* ``/orgs/:org/public_members/:user``

  * GET: :meth:`github.Organization.Organization.has_in_public_members`
  * PUT: :meth:`github.Organization.Organization.add_to_public_members`
  * DELETE: :meth:`github.Organization.Organization.remove_from_public_members`

* ``/orgs/:org/repos``

  * GET: :meth:`github.Organization.Organization.get_repos`
  * POST: :meth:`github.Organization.Organization.create_repo`

* ``/orgs/:org/teams``

  * GET: :meth:`github.Organization.Organization.get_teams`
  * POST: :meth:`github.Organization.Organization.create_team`

* ``/rate_limit``

  * GET: :meth:Ngithub.ot ot implemented, see `Github.rate_limiting`

* ``/repos/:user/:repo``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_repo` or :meth:`github.NamedUser.NamedUser.get_repo` or :meth:`github.Organization.Organization.get_repo` or :meth:`github.Github.Github.get_repo`
  * PATCH: :meth:`github.Repository.Repository.edit`
  * DELETE: :meth:`github.Repository.Repository.delete`

* ``/repos/:user/:repo/:archive_format/:ref``

  * GET: :meth:`github.Repository.Repository.get_archive_link`

* ``/repos/:user/:repo/assignees``

  * GET: :meth:`github.Repository.Repository.get_assignees`

* ``/repos/:user/:repo/assignees/:assignee``

  * GET: :meth:`github.Repository.Repository.has_in_assignees`

* ``/repos/:user/:repo/branches``

  * GET: :meth:`github.Repository.Repository.get_branches`

* ``/repos/:user/:repo/branches/:branch``

  * GET: :meth:`github.Repository.Repository.get_branch`

* ``/repos/:user/:repo/collaborators``

  * GET: :meth:`github.Repository.Repository.get_collaborators`

* ``/repos/:user/:repo/collaborators/:user``

  * GET: :meth:`github.Repository.Repository.has_in_collaborators`
  * PUT: :meth:`github.Repository.Repository.add_to_collaborators`
  * DELETE: :meth:`github.Repository.Repository.remove_from_collaborators`

* ``/repos/:user/:repo/comments``

  * GET: :meth:`github.Repository.Repository.get_comments`

* ``/repos/:user/:repo/comments/:id``

  * GET: :meth:`github.Repository.Repository.get_comment`
  * PATCH: :meth:`github.CommitComment.CommitComment.edit`
  * DELETE: :meth:`github.CommitComment.CommitComment.delete`

* ``/repos/:user/:repo/commits``

  * GET: :meth:`github.Repository.Repository.get_commits`

* ``/repos/:user/:repo/commits/:sha``

  * GET: :meth:`github.Repository.Repository.get_commit`

* ``/repos/:user/:repo/commits/:sha/comments``

  * GET: :meth:`github.Commit.Commit.get_comments`
  * POST: :meth:`github.Commit.Commit.create_comment`

* ``/repos/:user/:repo/compare/:base...:head``

  * GET: :meth:`github.Repository.Repository.compare`

* ``/repos/:user/:repo/contents/:path``

  * GET: :meth:`github.Repository.Repository.get_contents` or :meth:`github.Repository.Repository.get_file_contents` or :meth:`github.Repository.Repository.get_dir_contents`

* ``/repos/:user/:repo/contributors``

  * GET: :meth:`github.Repository.Repository.get_contributors`

* ``/repos/:user/:repo/downloads``

  * GET: :meth:`github.Repository.Repository.get_downloads`
  * POST: :meth:`github.Repository.Repository.create_download`

* ``/repos/:user/:repo/downloads/:id``

  * GET: :meth:`github.Repository.Repository.get_download`
  * DELETE: :meth:`github.Download.Download.delete`

* ``/repos/:user/:repo/events``

  * GET: :meth:`github.Repository.Repository.get_events`

* ``/repos/:user/:repo/forks``

  * GET: :meth:`github.Repository.Repository.get_forks`
  * POST: :meth:`github.AuthenticatedUser.AuthenticatedUser.create_fork` or `Organization.create_fork`

* ``/repos/:user/:repo/git/blobs``

  * POST: :meth:`github.Repository.Repository.create_git_blob`

* ``/repos/:user/:repo/git/blobs/:sha``

  * GET: :meth:`github.Repository.Repository.get_git_blob`

* ``/repos/:user/:repo/git/commits``

  * POST: :meth:`github.Repository.Repository.create_git_commit`

* ``/repos/:user/:repo/git/commits/:sha``

  * GET: :meth:`github.Repository.Repository.get_git_commit`

* ``/repos/:user/:repo/git/refs``

  * GET: :meth:`github.Repository.Repository.get_git_refs`
  * POST: :meth:`github.Repository.Repository.create_git_ref`

* ``/repos/:user/:repo/git/refs/:ref``

  * GET: :meth:`github.Repository.Repository.get_git_ref`
  * PATCH: :meth:`github.GitRef.GitRef.edit`
  * DELETE: :meth:`github.GitRef.GitRef.delete`

* ``/repos/:user/:repo/git/tags``

  * POST: :meth:`github.Repository.Repository.create_git_tag`

* ``/repos/:user/:repo/git/tags/:sha``

  * GET: :meth:`github.Repository.Repository.get_git_tag`

* ``/repos/:user/:repo/git/trees``

  * POST: :meth:`github.Repository.Repository.create_git_tree`

* ``/repos/:user/:repo/git/trees/:sha``

  * GET: :meth:`github.Repository.Repository.get_git_tree`

* ``/repos/:user/:repo/hooks``

  * GET: :meth:`github.Repository.Repository.get_hooks`
  * POST: :meth:`github.Repository.Repository.create_hook`

* ``/repos/:user/:repo/hooks/:id``

  * GET: :meth:`github.Repository.Repository.get_hook`
  * PATCH: :meth:`github.Hook.Hook.edit`
  * DELETE: :meth:`github.Hook.Hook.delete`

* ``/repos/:user/:repo/hooks/:id/test``

  * POST: :meth:`github.Hook.Hook.test`

* ``/repos/:user/:repo/issues``

  * GET: :meth:`github.Repository.Repository.get_issues`
  * POST: :meth:`github.Repository.Repository.create_issue`

* ``/repos/:user/:repo/issues/:number``

  * GET: :meth:`github.Repository.Repository.get_issue`
  * PATCH: :meth:`github.Issue.Issue.edit`

* ``/repos/:user/:repo/issues/:number/comments``

  * GET: :meth:`github.Issue.Issue.get_comments` or :meth:`gituhub.PullRequest.PullRequest.get_issue_comments`
  * POST: :meth:`github.Issue.Issue.create_comment` or :meth:`gituhub.PullRequest.PullRequest.create_issue_comment`

* ``/repos/:user/:repo/issues/:number/events``

  * GET: :meth:`github.Issue.Issue.get_events`

* ``/repos/:user/:repo/issues/:number/labels``

  * GET: :meth:`github.Issue.Issue.get_labels`
  * POST: :meth:`github.Issue.Issue.add_to_labels`
  * PUT: :meth:`github.Issue.Issue.set_labels`
  * DELETE: :meth:`github.Issue.Issue.delete_labels`

* ``/repos/:user/:repo/issues/:number/labels/:name``

  * DELETE: :meth:`github.Issue.Issue.remove_from_labels`

* ``/repos/:user/:repo/issues/comments``

  * GET: :meth:`github.Repository.Repository.get_issues_comments`

* ``/repos/:user/:repo/issues/comments/:id``

  * GET: :meth:`github.Issue.Issue.get_comment` or :meth:`gituhub.PullRequest.PullRequest.get_issue_comment`
  * PATCH: :meth:`github.IssueComment.IssueComment.edit`
  * DELETE: :meth:`github.IssueComment.IssueComment.delete`

* ``/repos/:user/:repo/issues/events``

  * GET: :meth:`github.Repository.Repository.get_issues_events`

* ``/repos/:user/:repo/issues/events/:id``

  * GET: :meth:`github.Repository.Repository.get_issues_event`

* ``/repos/:user/:repo/keys``

  * GET: :meth:`github.Repository.Repository.get_keys`
  * POST: :meth:`github.Repository.Repository.create_key`

* ``/repos/:user/:repo/keys/:id``

  * GET: :meth:`github.Repository.Repository.get_key`
  * PATCH: :meth:`github.RepositoryKey.RepositoryKey.edit`
  * DELETE: :meth:`github.RepositoryKey.RepositoryKey.delete`

* ``/repos/:user/:repo/labels``

  * GET: :meth:`github.Repository.Repository.get_labels`
  * POST: :meth:`github.Repository.Repository.create_label`

* ``/repos/:user/:repo/labels/:name``

  * GET: :meth:`github.Repository.Repository.get_label`
  * PATCH: :meth:`github.Label.Label.edit`
  * DELETE: :meth:`github.Label.Label.delete`

* ``/repos/:user/:repo/languages``

  * GET: :meth:`github.Repository.Repository.get_languages`

* ``/repos/:user/:repo/merges``

  * POST: :meth:`github.Repository.Repository.merge`

* ``/repos/:user/:repo/milestones``

  * GET: :meth:`github.Repository.Repository.get_milestones`
  * POST: :meth:`github.Repository.Repository.create_milestone`

* ``/repos/:user/:repo/milestones/:number``

  * GET: :meth:`github.Repository.Repository.get_milestone`
  * PATCH: :meth:`github.Milestone.Milestone.edit`
  * DELETE: :meth:`github.Milestone.Milestone.delete`

* ``/repos/:user/:repo/milestones/:number/labels``

  * GET: :meth:`github.Milestone.Milestone.get_labels`

* ``/repos/:user/:repo/pulls``

  * GET: :meth:`github.Repository.Repository.get_pulls`
  * POST: :meth:`github.Repository.Repository.create_pull`

* ``/repos/:user/:repo/pulls/:number``

  * GET: :meth:`github.Repository.Repository.get_pull`
  * PATCH: :meth:`github.PullRequest.PullRequest.edit`

* ``/repos/:user/:repo/pulls/:number/comments``

  * GET: :meth:`github.PullRequest.PullRequest.get_comments` or :meth:`github.PullRequest.PullRequest.get_review_comments`
  * POST: :meth:`github.PullRequest.PullRequest.create_comment` or :meth:`github.PullRequest.PullRequest.create_review_comment`

* ``/repos/:user/:repo/pulls/:number/commits``

  * GET: :meth:`github.PullRequest.PullRequest.get_commits`

* ``/repos/:user/:repo/pulls/:number/files``

  * GET: :meth:`github.PullRequest.PullRequest.get_files`

* ``/repos/:user/:repo/pulls/:number/merge``

  * GET: :meth:`github.PullRequest.PullRequest.is_merged`
  * PUT: :meth:`github.PullRequest.PullRequest.merge`

* ``/repos/:user/:repo/pulls/comments``

  * GET: :meth:`github.Repository.Repository.get_pulls_comments` or :meth:`github.Repository.Repository.get_pulls_review_comments`

* ``/repos/:user/:repo/pulls/comments/:number``

  * GET: :meth:`github.PullRequest.PullRequest.get_comment` or :meth:`github.PullRequest.PullRequest.get_review_comment`
  * PATCH: :meth:`github.PullRequestComment.PullRequestComment.edit`
  * DELETE: :meth:`github.PullRequestComment.PullRequestComment.delete`

* ``/repos/:user/:repo/readme``

  * GET: :meth:`github.Repository.Repository.get_readme`

* ``/repos/:user/:repo/stargazers``

  * GET: :meth:`github.Repository.Repository.get_stargazers`

* ``/repos/:user/:repo/statuses/:sha``

  * GET: :meth:`github.Commit.Commit.get_statuses`
  * POST: :meth:`github.Commit.Commit.create_status`

* ``/repos/:user/:repo/subscribers``

  * GET: :meth:`github.Repository.Repository.get_subscribers`

* ``/repos/:user/:repo/tags``

  * GET: :meth:`github.Repository.Repository.get_tags`

* ``/repos/:user/:repo/teams``

  * GET: :meth:`github.Repository.Repository.get_teams`

* ``/repos/:user/:repo/watchers``

  * GET: :meth:`github.Repository.Repository.get_watchers`

* ``/teams/:id``

  * GET: :meth:`github.Organization.Organization.get_team`
  * PATCH: :meth:`github.Team.Team.edit`
  * DELETE: :meth:`github.Team.Team.delete`

* ``/teams/:id/members``

  * GET: :meth:`github.Team.Team.get_members`

* ``/teams/:id/members/:user``

  * GET: :meth:`github.Team.Team.has_in_members`
  * PUT: :meth:`github.Team.Team.add_to_members`
  * DELETE: :meth:`github.Team.Team.remove_from_members`

* ``/teams/:id/repos``

  * GET: :meth:`github.Team.Team.get_repos`

* ``/teams/:id/repos/:user/:repo``

  * GET: :meth:`github.Team.Team.has_in_repos`
  * PUT: :meth:`github.Team.Team.add_to_repos`
  * DELETE: :meth:`github.Team.Team.remove_from_repos`

* ``/user``

  * GET: :meth:`github.Github.Github.get_user`
  * PATCH: :meth:`github.AuthenticatedUser.AuthenticatedUser.edit`

* ``/user/emails``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_emails`
  * POST: :meth:`github.AuthenticatedUser.AuthenticatedUser.add_to_emails`
  * DELETE: :meth:`github.AuthenticatedUser.AuthenticatedUser.remove_from_emails`

* ``/user/followers``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_followers`

* ``/user/following``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_following`

* ``/user/following/:user``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.has_in_following`
  * PUT: :meth:`github.AuthenticatedUser.AuthenticatedUser.add_to_following`
  * DELETE: :meth:`github.AuthenticatedUser.AuthenticatedUser.remove_from_following`

* ``/user/keys``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_keys`
  * POST: :meth:`github.AuthenticatedUser.AuthenticatedUser.create_key`

* ``/user/keys/:id``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_key`
  * PATCH: :meth:`github.UserKey.UserKey.edit`
  * DELETE: :meth:`github.UserKey.UserKey.delete`

* ``/user/orgs``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_orgs`

* ``/user/repos``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_repos`
  * POST: :meth:`github.AuthenticatedUser.AuthenticatedUser.create_repo`

* ``/user/starred``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_starred`

* ``/user/starred/:user/:repo``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.has_in_starred`
  * PUT: :meth:`github.AuthenticatedUser.AuthenticatedUser.add_to_starred`
  * DELETE: :meth:`github.AuthenticatedUser.AuthenticatedUser.remove_from_starred`

* ``/user/subscriptions``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_subscriptions`

* ``/user/subscriptions/:user/:repo``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.has_in_subscriptions`
  * PUT: :meth:`github.AuthenticatedUser.AuthenticatedUser.add_to_subscriptions`
  * DELETE: :meth:`github.AuthenticatedUser.AuthenticatedUser.remove_from_subscriptions`

* ``/user/watched``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_watched`

* ``/user/watched/:user/:repo``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.has_in_watched`
  * PUT: :meth:`github.AuthenticatedUser.AuthenticatedUser.add_to_watched`
  * DELETE: :meth:`github.AuthenticatedUser.AuthenticatedUser.remove_from_watched`

* ``/users/:user``

  * GET: :meth:`github.Github.Github.get_user`

* ``/users/:user/events``

  * GET: :meth:`github.NamedUser.NamedUser.get_events`

* ``/users/:user/events/orgs/:org``

  * GET: :meth:`github.AuthenticatedUser.AuthenticatedUser.get_organization_events`

* ``/users/:user/events/public``

  * GET: :meth:`github.NamedUser.NamedUser.get_public_events`

* ``/users/:user/followers``

  * GET: :meth:`github.NamedUser.NamedUser.get_followers`

* ``/users/:user/following``

  * GET: :meth:`github.NamedUser.NamedUser.get_following`

* ``/users/:user/gists``

  * GET: :meth:`github.NamedUser.NamedUser.get_gists`
  * POST: :meth:`github.NamedUser.NamedUser.create_gist`

* ``/users/:user/keys``

  * GET: :meth:`github.NamedUser.NamedUser.get_keys`

* ``/users/:user/orgs``

  * GET: :meth:`github.NamedUser.NamedUser.get_orgs`

* ``/users/:user/received_events``

  * GET: :meth:`github.NamedUser.NamedUser.get_received_events`

* ``/users/:user/received_events/public``

  * GET: :meth:`github.NamedUser.NamedUser.get_public_received_events`

* ``/users/:user/repos``

  * GET: :meth:`github.NamedUser.NamedUser.get_repos`

* ``/users/:user/starred``

  * GET: :meth:`github.NamedUser.NamedUser.get_starred`

* ``/users/:user/subscriptions``

  * GET: :meth:`github.NamedUser.NamedUser.get_subscriptions`

* ``/users/:user/watched``

  * GET: :meth:`github.NamedUser.NamedUser.get_watched`

