.. ########################################################################
   ###### This file is generated. Manual changes will likely be lost. #####
   ########################################################################

From Github API v3 to PyGithub
==============================

Here are all the end points I'm aware of, and if/where they are implemented in PyGithub.
If something is not listed here, please `open an issue <http://github.com/jacquev6/PyGithub/issues>`__ with a link to the corresponding documentation of Github API v3.

GET /api/last-message.json
--------------------------

(`Reference documentation of Github API v3 <https://status.github.com/api>`__)

Not yet implemented in PyGithub.

GET /api/messages.json
----------------------

(`Reference documentation of Github API v3 <https://status.github.com/api>`__)

Not yet implemented in PyGithub.

GET /api/status.json
--------------------

(`Reference documentation of Github API v3 <https://status.github.com/api>`__)

Not yet implemented in PyGithub.

GET /api/v3/enterprise/settings/license
---------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/enterprise/license#request>`__)

Not yet implemented in PyGithub.

GET /api/v3/enterprise/stats/:type
----------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/enterprise/admin_stats#request>`__)

Not yet implemented in PyGithub.

POST /api/v3/staff/indexing_jobs
--------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/enterprise/search_indexing#queue-an-indexing-job>`__)

Not yet implemented in PyGithub.

DELETE /applications/:client_id/tokens
--------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/oauth_authorizations#revoke-all-authorizations-for-an-application>`__)

Not yet implemented in PyGithub.

DELETE /applications/:client_id/tokens/:access_token
----------------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/oauth_authorizations#revoke-an-authorization-for-an-application>`__)

Not yet implemented in PyGithub.

GET /applications/:client_id/tokens/:access_token
-------------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/oauth_authorizations#check-an-authorization>`__)

Not yet implemented in PyGithub.

POST /applications/:client_id/tokens/:access_token
--------------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/oauth_authorizations#reset-an-authorization>`__)

Not yet implemented in PyGithub.

GET /authorizations
-------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/oauth_authorizations#list-your-authorizations>`__)

Not yet implemented in PyGithub.

POST /authorizations
--------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/oauth_authorizations#create-a-new-authorization>`__)

Not yet implemented in PyGithub.

DELETE /authorizations/:id
--------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/oauth_authorizations#delete-an-authorization>`__)

Not yet implemented in PyGithub.

GET /authorizations/:id
-----------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/oauth_authorizations#get-a-single-authorization>`__)

Not yet implemented in PyGithub.

PATCH /authorizations/:id
-------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/oauth_authorizations#update-an-existing-authorization>`__)

Not yet implemented in PyGithub.

PUT /authorizations/clients/:client_id
--------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/oauth_authorizations#get-or-create-an-authorization-for-a-specific-app>`__)

Not yet implemented in PyGithub.

GET /emojis
-----------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/emojis#emojis>`__)

Implemented in PyGithub by:
  * :meth:`.Github.get_emojis`

GET /events
-----------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/events#list-public-events>`__)

Not yet implemented in PyGithub.

GET /feeds
----------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/feeds#list-feeds>`__)

Not yet implemented in PyGithub.

GET /gists
----------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists#list-gists>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.get_gists`

POST /gists
-----------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists#create-a-gist>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.create_gist`
  * :meth:`.Github.create_anonymous_gist`

GET /gists/:gist_id/comments
----------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists/comments#list-comments-on-a-gist>`__)

Not yet implemented in PyGithub.

POST /gists/:gist_id/comments
-----------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists/comments#create-a-comment>`__)

Not yet implemented in PyGithub.

DELETE /gists/:gist_id/comments/:id
-----------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists/comments#delete-a-comment>`__)

Not yet implemented in PyGithub.

GET /gists/:gist_id/comments/:id
--------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists/comments#get-a-single-comment>`__)

Not yet implemented in PyGithub.

PATCH /gists/:gist_id/comments/:id
----------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists/comments#edit-a-comment>`__)

Not yet implemented in PyGithub.

DELETE /gists/:id
-----------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists#delete-a-gist>`__)

Implemented in PyGithub by:
  * :meth:`.Gist.delete`

GET /gists/:id
--------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists#get-a-single-gist>`__)

Implemented in PyGithub by:
  * :meth:`.Github.get_gist`

PATCH /gists/:id
----------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists#edit-a-gist>`__)

Implemented in PyGithub by:
  * :meth:`.Gist.edit`

GET /gists/:id/commits
----------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists#list-gist-commits>`__)

Implemented in PyGithub by:
  * :meth:`.Gist.get_commits`

GET /gists/:id/forks
--------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists#list-gist-forks>`__)

Implemented in PyGithub by:
  * :meth:`.Gist.get_forks`

POST /gists/:id/forks
---------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists#fork-a-gist>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.create_gist_fork`

DELETE /gists/:id/star
----------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists#unstar-a-gist>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.remove_from_starred_gists`

GET /gists/:id/star
-------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists#check-if-a-gist-is-starred>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.has_in_starred_gists`

PUT /gists/:id/star
-------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists#star-a-gist>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.add_to_starred_gists`

GET /gists/public
-----------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists#list-gists>`__)

Implemented in PyGithub by:
  * :meth:`.Github.get_public_gists`

GET /gists/starred
------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists#list-gists>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.get_starred_gists`

GET /gitignore/templates
------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gitignore#listing-available-templates>`__)

Implemented in PyGithub by:
  * :meth:`.Github.get_gitignore_templates`

GET /gitignore/templates/:name
------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gitignore#get-a-single-template>`__)

Implemented in PyGithub by:
  * :meth:`.Github.get_gitignore_template`

GET /hooks
----------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/hooks>`__)

Not yet implemented in PyGithub.

GET /hooks/:name
----------------

(`Reference documentation of Github API v3 <https://github.com/jacquev6/PyGithub/issues/196>`__)

Not yet implemented in PyGithub.

POST /hub
---------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/hooks#pubsubhubbub>`__)

Not yet implemented in PyGithub.

GET /issues
-----------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues#list-issues>`__)

Not yet implemented in PyGithub.

POST /markdown
--------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/markdown#render-an-arbitrary-markdown-document>`__)

Not yet implemented in PyGithub.

GET /meta
---------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/meta#meta>`__)

Implemented in PyGithub by:
  * :meth:`.Github.get_meta`

GET /networks/:owner/:repo/events
---------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/events#list-public-events-for-a-network-of-repositories>`__)

Not yet implemented in PyGithub.

GET /notifications
------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/notifications#list-your-notifications>`__)

Not yet implemented in PyGithub.

PUT /notifications
------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/notifications#mark-as-read>`__)

Not yet implemented in PyGithub.

GET /notifications/threads/:id
------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/notifications#view-a-single-thread>`__)

Not yet implemented in PyGithub.

PATCH /notifications/threads/:id
--------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/notifications#mark-a-thread-as-read>`__)

Not yet implemented in PyGithub.

DELETE /notifications/threads/:id/subscription
----------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/notifications#delete-a-thread-subscription>`__)

Not yet implemented in PyGithub.

GET /notifications/threads/:id/subscription
-------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/notifications#get-a-thread-subscription>`__)

Not yet implemented in PyGithub.

PUT /notifications/threads/:id/subscription
-------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/notifications#set-a-thread-subscription>`__)

Not yet implemented in PyGithub.

GET /orgs/:org
--------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs#get-an-organization>`__)

Implemented in PyGithub by:
  * :meth:`.Github.get_org`

PATCH /orgs/:org
----------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs#edit-an-organization>`__)

Implemented in PyGithub by:
  * :meth:`.Organization.edit`

GET /orgs/:org/events
---------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/events#list-public-events-for-an-organization>`__)

Not yet implemented in PyGithub.

GET /orgs/:org/issues
---------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues#list-issues>`__)

Not yet implemented in PyGithub.

GET /orgs/:org/members
----------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/members#members-list>`__)

Implemented in PyGithub by:
  * :meth:`.Organization.get_members`

DELETE /orgs/:org/members/:username
-----------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/members#remove-a-member>`__)

Implemented in PyGithub by:
  * :meth:`.Organization.remove_from_members`

GET /orgs/:org/members/:username
--------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/members#check-membership>`__)

Implemented in PyGithub by:
  * :meth:`.Organization.has_in_members`

GET /orgs/:org/public_members
-----------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/members#public-members-list>`__)

Implemented in PyGithub by:
  * :meth:`.Organization.get_public_members`

DELETE /orgs/:org/public_members/:username
------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/members#conceal-a-users-membership>`__)

Implemented in PyGithub by:
  * :meth:`.Organization.remove_from_public_members`

GET /orgs/:org/public_members/:username
---------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/members#check-public-membership>`__)

Implemented in PyGithub by:
  * :meth:`.Organization.has_in_public_members`

PUT /orgs/:org/public_members/:username
---------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/members#publicize-a-users-membership>`__)

Implemented in PyGithub by:
  * :meth:`.Organization.add_to_public_members`

GET /orgs/:org/repos
--------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos#list-organization-repositories>`__)

Implemented in PyGithub by:
  * :meth:`.Organization.get_repos`

POST /orgs/:org/repos
---------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos#create>`__)

Implemented in PyGithub by:
  * :meth:`.Organization.create_repo`

GET /orgs/:org/teams
--------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/teams#list-teams>`__)

Implemented in PyGithub by:
  * :meth:`.Organization.get_teams`

POST /orgs/:org/teams
---------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/teams#create-team>`__)

Implemented in PyGithub by:
  * :meth:`.Organization.create_team`

GET /rate_limit
---------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/rate_limit#get-your-current-rate-limit-status>`__)

Implemented in PyGithub by:
  * :meth:`.Github.get_rate_limit`

DELETE /repos/:owner/:repo
--------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos#delete-a-repository>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.delete`

GET /repos/:owner/:repo
-----------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos#get>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.get_repo`
  * :meth:`.Github.get_repo`
  * :meth:`.Organization.get_repo`
  * :meth:`.User.get_repo`

PATCH /repos/:owner/:repo
-------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos#edit>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.edit`

GET /repos/:owner/:repo/:archive_format/:ref
--------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/contents#get-archive-link>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/assignees
---------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/assignees#list-assignees>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_assignees`

GET /repos/:owner/:repo/assignees/:assignee
-------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/assignees#check-assignee>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.has_in_assignees`

GET /repos/:owner/:repo/branches
--------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos#list-branches>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_branches`

GET /repos/:owner/:repo/branches/:branch
----------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos#get-branch>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_branch`

GET /repos/:owner/:repo/collaborators
-------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/collaborators#list>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_collaborators`

DELETE /repos/:owner/:repo/collaborators/:username
--------------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/collaborators#remove-collaborator>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.remove_from_collaborators`

GET /repos/:owner/:repo/collaborators/:username
-----------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/collaborators#get>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.has_in_collaborators`

PUT /repos/:owner/:repo/collaborators/:username
-----------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/collaborators#add-collaborator>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.add_to_collaborators`

GET /repos/:owner/:repo/comments
--------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/comments#list-commit-comments-for-a-repository>`__)

Not yet implemented in PyGithub.

DELETE /repos/:owner/:repo/comments/:id
---------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/comments#delete-a-commit-comment>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/comments/:id
------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/comments#get-a-single-commit-comment>`__)

Not yet implemented in PyGithub.

PATCH /repos/:owner/:repo/comments/:id
--------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/comments#update-a-commit-comment>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/commits
-------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/commits#list-commits-on-a-repository>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_commits`

GET /repos/:owner/:repo/commits/:ref/comments
---------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/comments#list-comments-for-a-single-commit>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/commits/:ref/status
-------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/statuses#get-the-combined-status-for-a-specific-ref>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/commits/:ref/statuses
---------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/statuses#list-statuses-for-a-specific-ref>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/commits/:sha
------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/commits#get-a-single-commit>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_commit`

POST /repos/:owner/:repo/commits/:sha/comments
----------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/comments#create-a-commit-comment>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/compare/:base...:head
---------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/commits#compare-two-commits>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/compare/user1:branchname...user2:branchname
-------------------------------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/commits#compare-two-commits>`__)

Not yet implemented in PyGithub.

DELETE /repos/:owner/:repo/contents/:path
-----------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/contents#delete-a-file>`__)

Implemented in PyGithub by:
  * :meth:`.File.delete`

GET /repos/:owner/:repo/contents/:path
--------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/contents#get-contents>`__)

Implemented in PyGithub by:
  * :meth:`.Dir.get_contents`
  * :meth:`.Repository.get_contents`

PUT /repos/:owner/:repo/contents/:path
--------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/contents#update-a-file>`__)

Implemented in PyGithub by:
  * :meth:`.File.edit`
  * :meth:`.Repository.create_file`

GET /repos/:owner/:repo/contributors
------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos#list-contributors>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_contributors`

GET /repos/:owner/:repo/deployments
-----------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/deployments#list-deployments>`__)

Not yet implemented in PyGithub.

POST /repos/:owner/:repo/deployments
------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/deployments#create-a-deployment>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/deployments/:id/statuses
------------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/deployments#list-deployment-statuses>`__)

Not yet implemented in PyGithub.

POST /repos/:owner/:repo/deployments/:id/statuses
-------------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/deployments#create-a-deployment-status>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/downloads
---------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/downloads#list-downloads-for-a-repository>`__)

Not yet implemented in PyGithub.

DELETE /repos/:owner/:repo/downloads/:id
----------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/downloads#delete-a-download>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/downloads/:id
-------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/downloads#get-a-single-download>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/events
------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/events#list-repository-events>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/forks
-----------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/forks#list-forks>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_forks`

POST /repos/:owner/:repo/forks
------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/forks#create-a-fork>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.create_fork`
  * :meth:`.Organization.create_fork`

POST /repos/:owner/:repo/git/blobs
----------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/git/blobs#create-a-blob>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.create_git_blob`

GET /repos/:owner/:repo/git/blobs/:sha
--------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/git/blobs#get-a-blob>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_git_blob`

POST /repos/:owner/:repo/git/commits
------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/git/commits#create-a-commit>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.create_git_commit`

GET /repos/:owner/:repo/git/commits/:sha
----------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/git/commits#get-a-commit>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_git_commit`

GET /repos/:owner/:repo/git/refs
--------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/git/refs#get-all-references>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_git_refs`

POST /repos/:owner/:repo/git/refs
---------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/git/refs#create-a-reference>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.create_git_ref`

DELETE /repos/:owner/:repo/git/refs/:ref
----------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/git/refs#delete-a-reference>`__)

Implemented in PyGithub by:
  * :meth:`.GitRef.delete`

GET /repos/:owner/:repo/git/refs/:ref
-------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/git/refs#get-a-reference>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_git_ref`

PATCH /repos/:owner/:repo/git/refs/:ref
---------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/git/refs#update-a-reference>`__)

Implemented in PyGithub by:
  * :meth:`.GitRef.edit`

POST /repos/:owner/:repo/git/tags
---------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/git/tags#create-a-tag-object>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.create_git_tag`

GET /repos/:owner/:repo/git/tags/:sha
-------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/git/tags#get-a-tag>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_git_tag`

POST /repos/:owner/:repo/git/trees
----------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/git/trees#create-a-tree>`__)

Implemented in PyGithub by:
  * :meth:`.GitTree.create_modified_copy`
  * :meth:`.Repository.create_git_tree`

GET /repos/:owner/:repo/git/trees/:sha
--------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/git/trees#get-a-tree>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_git_tree`

GET /repos/:owner/:repo/hooks
-----------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/hooks#list-hooks>`__)

Not yet implemented in PyGithub.

POST /repos/:owner/:repo/hooks
------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/hooks#create-a-hook>`__)

Not yet implemented in PyGithub.

DELETE /repos/:owner/:repo/hooks/:id
------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/hooks#delete-a-hook>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/hooks/:id
---------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/hooks#get-single-hook>`__)

Not yet implemented in PyGithub.

PATCH /repos/:owner/:repo/hooks/:id
-----------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/hooks#edit-a-hook>`__)

Not yet implemented in PyGithub.

POST /repos/:owner/:repo/hooks/:id/pings
----------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/hooks#ping-a-hook>`__)

Not yet implemented in PyGithub.

POST /repos/:owner/:repo/hooks/:id/tests
----------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/hooks#test-a-push-hook>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/issues
------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues#list-issues-for-a-repository>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_issues`

POST /repos/:owner/:repo/issues
-------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues#create-an-issue>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.create_issue`

GET /repos/:owner/:repo/issues/:issue_number/events
---------------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/events#list-events-for-an-issue>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/issues/:number
--------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues#get-a-single-issue>`__)

Implemented in PyGithub by:
  * :meth:`.PullRequest.get_issue`
  * :meth:`.Repository.get_issue`

PATCH /repos/:owner/:repo/issues/:number
----------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues#edit-an-issue>`__)

Implemented in PyGithub by:
  * :meth:`.Issue.edit`

GET /repos/:owner/:repo/issues/:number/comments
-----------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/comments#list-comments-on-an-issue>`__)

Not yet implemented in PyGithub.

POST /repos/:owner/:repo/issues/:number/comments
------------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/comments#create-a-comment>`__)

Not yet implemented in PyGithub.

DELETE /repos/:owner/:repo/issues/:number/labels
------------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/labels#remove-all-labels-from-an-issue>`__)

Implemented in PyGithub by:
  * :meth:`.Issue.remove_all_labels`

GET /repos/:owner/:repo/issues/:number/labels
---------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/labels#list-labels-on-an-issue>`__)

Implemented in PyGithub by:
  * :meth:`.Issue.get_labels`

POST /repos/:owner/:repo/issues/:number/labels
----------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/labels#add-labels-to-an-issue>`__)

Implemented in PyGithub by:
  * :meth:`.Issue.add_to_labels`

PUT /repos/:owner/:repo/issues/:number/labels
---------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/labels#replace-all-labels-for-an-issue>`__)

Implemented in PyGithub by:
  * :meth:`.Issue.set_labels`

DELETE /repos/:owner/:repo/issues/:number/labels/:name
------------------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/labels#remove-a-label-from-an-issue>`__)

Implemented in PyGithub by:
  * :meth:`.Issue.remove_from_labels`

GET /repos/:owner/:repo/issues/comments
---------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/comments#list-comments-in-a-repository>`__)

Not yet implemented in PyGithub.

DELETE /repos/:owner/:repo/issues/comments/:id
----------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/comments#delete-a-comment>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/issues/comments/:id
-------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/comments#get-a-single-comment>`__)

Not yet implemented in PyGithub.

PATCH /repos/:owner/:repo/issues/comments/:id
---------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/comments#edit-a-comment>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/issues/events
-------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/events#list-events-for-a-repository>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/issues/events/:id
-----------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/events#get-a-single-event>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/keys
----------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/keys#list>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_keys`

POST /repos/:owner/:repo/keys
-----------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/keys#create>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.create_key`

DELETE /repos/:owner/:repo/keys/:id
-----------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/keys#delete>`__)

Implemented in PyGithub by:
  * :meth:`.PublicKey.delete`

GET /repos/:owner/:repo/keys/:id
--------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/keys#get>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_key`

GET /repos/:owner/:repo/labels
------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/labels#list-all-labels-for-this-repository>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_labels`

POST /repos/:owner/:repo/labels
-------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/labels#create-a-label>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.create_label`

DELETE /repos/:owner/:repo/labels/:name
---------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/labels#delete-a-label>`__)

Implemented in PyGithub by:
  * :meth:`.Label.delete`

GET /repos/:owner/:repo/labels/:name
------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/labels#get-a-single-label>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_label`

PATCH /repos/:owner/:repo/labels/:name
--------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/labels#update-a-label>`__)

Implemented in PyGithub by:
  * :meth:`.Label.edit`

GET /repos/:owner/:repo/languages
---------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos#list-languages>`__)

Not yet implemented in PyGithub.

POST /repos/:owner/:repo/merges
-------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/merging#perform-a-merge>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/milestones
----------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/milestones#list-milestones-for-a-repository>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_milestones`

POST /repos/:owner/:repo/milestones
-----------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/milestones#create-a-milestone>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.create_milestone`

DELETE /repos/:owner/:repo/milestones/:number
---------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/milestones#delete-a-milestone>`__)

Implemented in PyGithub by:
  * :meth:`.Milestone.delete`

GET /repos/:owner/:repo/milestones/:number
------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/milestones#get-a-single-milestone>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_milestone`

PATCH /repos/:owner/:repo/milestones/:number
--------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/milestones#update-a-milestone>`__)

Implemented in PyGithub by:
  * :meth:`.Milestone.edit`

GET /repos/:owner/:repo/milestones/:number/labels
-------------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues/labels#get-labels-for-every-issue-in-a-milestone>`__)

Implemented in PyGithub by:
  * :meth:`.Milestone.get_labels`

GET /repos/:owner/:repo/notifications
-------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/notifications#list-your-notifications-in-a-repository>`__)

Not yet implemented in PyGithub.

PUT /repos/:owner/:repo/notifications
-------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/notifications#mark-notifications-as-read-in-a-repository>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/pages
-----------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/pages#get-information-about-a-pages-site>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/pages/builds
------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/pages#list-pages-builds>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/pages/builds/latest
-------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/pages#list-latest-pages-build>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/pulls
-----------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/pulls#list-pull-requests>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_pulls`

POST /repos/:owner/:repo/pulls
------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/pulls#create-a-pull-request>`__)

Implemented in PyGithub by:
  * :meth:`.Issue.create_pull`
  * :meth:`.Repository.create_pull`

GET /repos/:owner/:repo/pulls/:number
-------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/pulls#get-a-single-pull-request>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_pull`

PATCH /repos/:owner/:repo/pulls/:number
---------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/pulls#update-a-pull-request>`__)

Implemented in PyGithub by:
  * :meth:`.PullRequest.edit`

GET /repos/:owner/:repo/pulls/:number/comments
----------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/pulls/comments#list-comments-on-a-pull-request>`__)

Not yet implemented in PyGithub.

POST /repos/:owner/:repo/pulls/:number/comments
-----------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/pulls/comments#create-a-comment>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/pulls/:number/commits
---------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/pulls#list-commits-on-a-pull-request>`__)

Implemented in PyGithub by:
  * :meth:`.PullRequest.get_commits`

GET /repos/:owner/:repo/pulls/:number/files
-------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/pulls#list-pull-requests-files>`__)

Implemented in PyGithub by:
  * :meth:`.PullRequest.get_files`

GET /repos/:owner/:repo/pulls/:number/merge
-------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/pulls#get-if-a-pull-request-has-been-merged>`__)

Implemented in PyGithub by:
  * :meth:`.PullRequest.get_is_merged`

PUT /repos/:owner/:repo/pulls/:number/merge
-------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/pulls#merge-a-pull-request-merge-button>`__)

Implemented in PyGithub by:
  * :meth:`.PullRequest.merge`

GET /repos/:owner/:repo/pulls/comments
--------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/pulls/comments#list-comments-in-a-repository>`__)

Not yet implemented in PyGithub.

DELETE /repos/:owner/:repo/pulls/comments/:number
-------------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/pulls/comments#delete-a-comment>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/pulls/comments/:number
----------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/pulls/comments#get-a-single-comment>`__)

Not yet implemented in PyGithub.

PATCH /repos/:owner/:repo/pulls/comments/:number
------------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/pulls/comments#edit-a-comment>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/readme
------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/contents#get-the-readme>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_readme`

GET /repos/:owner/:repo/releases
--------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/releases#list-releases-for-a-repository>`__)

Not yet implemented in PyGithub.

POST /repos/:owner/:repo/releases
---------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/releases#create-a-release>`__)

Not yet implemented in PyGithub.

DELETE /repos/:owner/:repo/releases/:id
---------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/releases#delete-a-release>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/releases/:id
------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/releases#get-a-single-release>`__)

Not yet implemented in PyGithub.

PATCH /repos/:owner/:repo/releases/:id
--------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/releases#edit-a-release>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/releases/:id/assets
-------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/releases#list-assets-for-a-release>`__)

Not yet implemented in PyGithub.

DELETE /repos/:owner/:repo/releases/assets/:id
----------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/releases#delete-a-release-asset>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/releases/assets/:id
-------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/releases#get-a-single-release-asset>`__)

Not yet implemented in PyGithub.

PATCH /repos/:owner/:repo/releases/assets/:id
---------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/releases#edit-a-release-asset>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/stargazers
----------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/starring#list-stargazers>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_stargazers`

GET /repos/:owner/:repo/stats/code_frequency
--------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/statistics#code-frequency>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/stats/commit_activity
---------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/statistics#commit-activity>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/stats/contributors
------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/statistics#contributors>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/stats/participation
-------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/statistics#participation>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/stats/punch_card
----------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/statistics#punch-card>`__)

Not yet implemented in PyGithub.

POST /repos/:owner/:repo/statuses/:sha
--------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos/statuses#create-a-status>`__)

Not yet implemented in PyGithub.

GET /repos/:owner/:repo/subscribers
-----------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/watching#list-watchers>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_subscribers`

DELETE /repos/:owner/:repo/subscription
---------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/watching#delete-a-repository-subscription>`__)

Implemented in PyGithub by:
  * :meth:`.Subscription.delete`

GET /repos/:owner/:repo/subscription
------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/watching#get-a-repository-subscription>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.get_subscription`

PUT /repos/:owner/:repo/subscription
------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/watching#set-a-repository-subscription>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.create_subscription`
  * :meth:`.Subscription.edit`

GET /repos/:owner/:repo/tags
----------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos#list-tags>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_tags`

GET /repos/:owner/:repo/teams
-----------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos#list-teams>`__)

Implemented in PyGithub by:
  * :meth:`.Repository.get_teams`

GET /repositories
-----------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos#list-all-public-repositories>`__)

Implemented in PyGithub by:
  * :meth:`.Github.get_repos`

GET /search/code
----------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/search#search-code>`__)

Not yet implemented in PyGithub.

GET /search/issues
------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/search#search-issues>`__)

Not yet implemented in PyGithub.

GET /search/repositories
------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/search#search-repositories>`__)

Not yet implemented in PyGithub.

GET /search/users
-----------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/search#search-users>`__)

Not yet implemented in PyGithub.

GET /setup/api/configcheck
--------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/enterprise/management_console#check-configuration-status>`__)

Not yet implemented in PyGithub.

POST /setup/api/configure
-------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/enterprise/management_console#start-a-configuration-process>`__)

Not yet implemented in PyGithub.

GET /setup/api/maintenance
--------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/enterprise/management_console#check-maintenance-status>`__)

Not yet implemented in PyGithub.

POST /setup/api/maintenance
---------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/enterprise/management_console#enable-or-disable-maintenance-mode>`__)

Not yet implemented in PyGithub.

GET /setup/api/settings
-----------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/enterprise/management_console#retrieve-settings>`__)

Not yet implemented in PyGithub.

PUT /setup/api/settings
-----------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/enterprise/management_console#modify-settings>`__)

Not yet implemented in PyGithub.

DELETE /setup/api/settings/authorized-keys
------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/enterprise/management_console#remove-an-authorized-ssh-key>`__)

Not yet implemented in PyGithub.

GET /setup/api/settings/authorized-keys
---------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/enterprise/management_console#retrieve-authorized-ssh-keys>`__)

Not yet implemented in PyGithub.

POST /setup/api/settings/authorized-keys
----------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/enterprise/management_console#add-a-new-authorized-ssh-key>`__)

Not yet implemented in PyGithub.

POST /setup/api/start
---------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/enterprise/management_console#upload-a-license-and-software-package-for-the-first-time>`__)

Not yet implemented in PyGithub.

POST /setup/api/upgrade
-----------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/enterprise/management_console#upgrade-a-license-or-software-package>`__)

Not yet implemented in PyGithub.

DELETE /teams/:id
-----------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/teams#delete-team>`__)

Implemented in PyGithub by:
  * :meth:`.Team.delete`

GET /teams/:id
--------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/teams#get-team>`__)

Implemented in PyGithub by:
  * :meth:`.Github.get_team`

PATCH /teams/:id
----------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/teams#edit-team>`__)

Implemented in PyGithub by:
  * :meth:`.Team.edit`

GET /teams/:id/members
----------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/teams#list-team-members>`__)

Implemented in PyGithub by:
  * :meth:`.Team.get_members`

DELETE /teams/:id/members/:username
-----------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/teams#remove-team-member>`__)

Implemented in PyGithub by:
  * :meth:`.Team.remove_from_members`

GET /teams/:id/members/:username
--------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/teams#get-team-member>`__)

Implemented in PyGithub by:
  * :meth:`.Team.has_in_members`

PUT /teams/:id/members/:username
--------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/teams#add-team-member>`__)

Implemented in PyGithub by:
  * :meth:`.Team.add_to_members`

GET /teams/:id/repos
--------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/teams#list-team-repos>`__)

Implemented in PyGithub by:
  * :meth:`.Team.get_repos`

PUT /teams/:id/repos/:org/:repo
-------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/teams#add-team-repo>`__)

Implemented in PyGithub by:
  * :meth:`.Team.add_to_repos`

DELETE /teams/:id/repos/:owner/:repo
------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/teams#remove-team-repo>`__)

Implemented in PyGithub by:
  * :meth:`.Team.remove_from_repos`

GET /teams/:id/repos/:owner/:repo
---------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/teams#get-team-repo>`__)

Implemented in PyGithub by:
  * :meth:`.Team.has_in_repos`

GET /user
---------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users#get-the-authenticated-user>`__)

Implemented in PyGithub by:
  * :meth:`.Github.get_authenticated_user`

PATCH /user
-----------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users#update-the-authenticated-user>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.edit`

DELETE /user/emails
-------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users/emails#delete-email-addresses>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.remove_from_emails`

GET /user/emails
----------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users/emails#list-email-addresses-for-a-user>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.get_emails`

POST /user/emails
-----------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users/emails#add-email-addresses>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.add_to_emails`

GET /user/followers
-------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users/followers#list-followers-of-a-user>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.get_followers`

GET /user/following
-------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users/followers#list-users-followed-by-another-user>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.get_following`

DELETE /user/following/:username
--------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users/followers#unfollow-a-user>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.remove_from_following`

GET /user/following/:username
-----------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users/followers#check-if-you-are-following-a-user>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.has_in_following`

PUT /user/following/:username
-----------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users/followers#follow-a-user>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.add_to_following`

GET /user/issues
----------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/issues#list-issues>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.get_issues`

GET /user/keys
--------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users/keys#list-your-public-keys>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.get_keys`

POST /user/keys
---------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users/keys#create-a-public-key>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.create_key`

DELETE /user/keys/:id
---------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users/keys#delete-a-public-key>`__)

Implemented in PyGithub by:
  * :meth:`.PublicKey.delete`

GET /user/keys/:id
------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users/keys#get-a-single-public-key>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.get_key`

GET /user/orgs
--------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs#list-user-organizations>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.get_orgs`

GET /user/repos
---------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos#list-your-repositories>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.get_repos`

POST /user/repos
----------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos#create>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.create_repo`

GET /user/starred
-----------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/starring#list-repositories-being-starred>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.get_starred`

DELETE /user/starred/:owner/:repo
---------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/starring#unstar-a-repository>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.remove_from_starred`

GET /user/starred/:owner/:repo
------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/starring#check-if-you-are-starring-a-repository>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.has_in_starred`

PUT /user/starred/:owner/:repo
------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/starring#star-a-repository>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.add_to_starred`

GET /user/subscriptions
-----------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/watching#list-repositories-being-watched>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.get_subscriptions`

GET /user/teams
---------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs/teams#list-user-teams>`__)

Implemented in PyGithub by:
  * :meth:`.AuthenticatedUser.get_teams`

GET /users
----------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users#get-all-users>`__)

Implemented in PyGithub by:
  * :meth:`.Github.get_users`

GET /users/:username
--------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users#get-a-single-user>`__)

Implemented in PyGithub by:
  * :meth:`.Github.get_user`

GET /users/:username/events
---------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/events#list-events-performed-by-a-user>`__)

Not yet implemented in PyGithub.

GET /users/:username/events/orgs/:org
-------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/events#list-events-for-an-organization>`__)

Not yet implemented in PyGithub.

GET /users/:username/events/public
----------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/events#list-public-events-performed-by-a-user>`__)

Not yet implemented in PyGithub.

GET /users/:username/followers
------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users/followers#list-followers-of-a-user>`__)

Implemented in PyGithub by:
  * :meth:`.User.get_followers`

GET /users/:username/following
------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users/followers#list-users-followed-by-another-user>`__)

Implemented in PyGithub by:
  * :meth:`.User.get_following`

GET /users/:username/following/:target_user
-------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users/followers#check-if-one-user-follows-another>`__)

Implemented in PyGithub by:
  * :meth:`.User.has_in_following`

GET /users/:username/gists
--------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/gists#list-gists>`__)

Implemented in PyGithub by:
  * :meth:`.User.get_gists`

GET /users/:username/keys
-------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/users/keys#list-public-keys-for-a-user>`__)

Implemented in PyGithub by:
  * :meth:`.User.get_keys`

GET /users/:username/orgs
-------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/orgs#list-user-organizations>`__)

Implemented in PyGithub by:
  * :meth:`.User.get_orgs`

GET /users/:username/received_events
------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/events#list-events-that-a-user-has-received>`__)

Not yet implemented in PyGithub.

GET /users/:username/received_events/public
-------------------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/events#list-public-events-that-a-user-has-received>`__)

Not yet implemented in PyGithub.

GET /users/:username/repos
--------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/repos#list-user-repositories>`__)

Implemented in PyGithub by:
  * :meth:`.User.get_repos`

GET /users/:username/starred
----------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/starring#list-repositories-being-starred>`__)

Implemented in PyGithub by:
  * :meth:`.User.get_starred`

GET /users/:username/subscriptions
----------------------------------

(`Reference documentation of Github API v3 <http://developer.github.com/v3/activity/watching#list-repositories-being-watched>`__)

Implemented in PyGithub by:
  * :meth:`.User.get_subscriptions`
