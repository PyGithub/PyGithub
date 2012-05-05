# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
import GitCommit
import Team
import PullRequest
import GitBlob
import Repository
import IssueEvent
import Milestone
import RepositoryKey
import GitTag
import CommitComment
import Hook
import Tag
import Branch
import GitRef
import Download
import Commit
import NamedUser
import Issue
import Event
import GitTree
import Label
# This allows None as a valid value for an optional parameter

class DefaultValueForOptionalParametersType:
    pass
DefaultValueForOptionalParameters = DefaultValueForOptionalParametersType()

class Repository( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def clone_url( self ):
        self.__completeIfNeeded( self.__clone_url )
        return self.__clone_url

    @property
    def created_at( self ):
        self.__completeIfNeeded( self.__created_at )
        return self.__created_at

    @property
    def description( self ):
        self.__completeIfNeeded( self.__description )
        return self.__description

    @property
    def fork( self ):
        self.__completeIfNeeded( self.__fork )
        return self.__fork

    @property
    def forks( self ):
        self.__completeIfNeeded( self.__forks )
        return self.__forks

    @property
    def git_url( self ):
        self.__completeIfNeeded( self.__git_url )
        return self.__git_url

    @property
    def has_downloads( self ):
        self.__completeIfNeeded( self.__has_downloads )
        return self.__has_downloads

    @property
    def has_issues( self ):
        self.__completeIfNeeded( self.__has_issues )
        return self.__has_issues

    @property
    def has_wiki( self ):
        self.__completeIfNeeded( self.__has_wiki )
        return self.__has_wiki

    @property
    def homepage( self ):
        self.__completeIfNeeded( self.__homepage )
        return self.__homepage

    @property
    def html_url( self ):
        self.__completeIfNeeded( self.__html_url )
        return self.__html_url

    @property
    def id( self ):
        self.__completeIfNeeded( self.__id )
        return self.__id

    @property
    def language( self ):
        self.__completeIfNeeded( self.__language )
        return self.__language

    @property
    def master_branch( self ):
        self.__completeIfNeeded( self.__master_branch )
        return self.__master_branch

    @property
    def mirror_url( self ):
        self.__completeIfNeeded( self.__mirror_url )
        return self.__mirror_url

    @property
    def name( self ):
        self.__completeIfNeeded( self.__name )
        return self.__name

    @property
    def open_issues( self ):
        self.__completeIfNeeded( self.__open_issues )
        return self.__open_issues

    @property
    def organization( self ):
        self.__completeIfNeeded( self.__organization )
        return self.__organization

    @property
    def owner( self ):
        self.__completeIfNeeded( self.__owner )
        return self.__owner

    @property
    def parent( self ):
        self.__completeIfNeeded( self.__parent )
        return self.__parent

    @property
    def permissions( self ):
        self.__completeIfNeeded( self.__permissions )
        return self.__permissions

    @property
    def private( self ):
        self.__completeIfNeeded( self.__private )
        return self.__private

    @property
    def pushed_at( self ):
        self.__completeIfNeeded( self.__pushed_at )
        return self.__pushed_at

    @property
    def size( self ):
        self.__completeIfNeeded( self.__size )
        return self.__size

    @property
    def source( self ):
        self.__completeIfNeeded( self.__source )
        return self.__source

    @property
    def ssh_url( self ):
        self.__completeIfNeeded( self.__ssh_url )
        return self.__ssh_url

    @property
    def svn_url( self ):
        self.__completeIfNeeded( self.__svn_url )
        return self.__svn_url

    @property
    def updated_at( self ):
        self.__completeIfNeeded( self.__updated_at )
        return self.__updated_at

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    @property
    def watchers( self ):
        self.__completeIfNeeded( self.__watchers )
        return self.__watchers

    def add_to_collaborators( self, collaborator ):
        status, headers, data = self.__requester.request(
            "PUT",
            str( self.url ) + "/collaborators" + "/" + str( collaborator._identity ),
            None,
            None
        )

    def compare( self, base, head ):
        pass

    def create_download( self, name, size, description = DefaultValueForOptionalParameters, content_type = DefaultValueForOptionalParameters ):
        post_parameters = {
            "name": name,
            "size": size,
        }
        if description is not DefaultValueForOptionalParameters:
            post_parameters[ "description" ] = description
        if content_type is not DefaultValueForOptionalParameters:
            post_parameters[ "content_type" ] = content_type
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/downloads",
            None,
            post_parameters
        )
        return Download.Download( self.__requester, data, lazy = True )

    def create_git_blob( self, content, encoding ):
        post_parameters = {
            "content": content,
            "encoding": encoding,
        }
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/git_blobs",
            None,
            post_parameters
        )
        return GitBlob.GitBlob( self.__requester, data, lazy = True )

    def create_git_commit( self, message, tree, parents, author = DefaultValueForOptionalParameters, committer = DefaultValueForOptionalParameters ):
        post_parameters = {
            "message": message,
            "tree": tree,
            "parents": parents,
        }
        if author is not DefaultValueForOptionalParameters:
            post_parameters[ "author" ] = author
        if committer is not DefaultValueForOptionalParameters:
            post_parameters[ "committer" ] = committer
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/git_commits",
            None,
            post_parameters
        )
        return GitCommit.GitCommit( self.__requester, data, lazy = True )

    def create_git_ref( self, ref, sha ):
        post_parameters = {
            "ref": ref,
            "sha": sha,
        }
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/git_refs",
            None,
            post_parameters
        )
        return GitRef.GitRef( self.__requester, data, lazy = True )

    def create_git_tag( self, tag, message, object, type, tagger = DefaultValueForOptionalParameters ):
        post_parameters = {
            "tag": tag,
            "message": message,
            "object": object,
            "type": type,
        }
        if tagger is not DefaultValueForOptionalParameters:
            post_parameters[ "tagger" ] = tagger
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/git_tags",
            None,
            post_parameters
        )
        return GitTag.GitTag( self.__requester, data, lazy = True )

    def create_git_tree( self, tree, base_tree = DefaultValueForOptionalParameters ):
        post_parameters = {
            "tree": tree,
        }
        if base_tree is not DefaultValueForOptionalParameters:
            post_parameters[ "base_tree" ] = base_tree
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/git_trees",
            None,
            post_parameters
        )
        return GitTree.GitTree( self.__requester, data, lazy = True )

    def create_hook( self, name, config, events = DefaultValueForOptionalParameters, active = DefaultValueForOptionalParameters ):
        post_parameters = {
            "name": name,
            "config": config,
        }
        if events is not DefaultValueForOptionalParameters:
            post_parameters[ "events" ] = events
        if active is not DefaultValueForOptionalParameters:
            post_parameters[ "active" ] = active
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/hooks",
            None,
            post_parameters
        )
        return Hook.Hook( self.__requester, data, lazy = True )

    def create_issue( self, title, body = DefaultValueForOptionalParameters, assignee = DefaultValueForOptionalParameters, milestone = DefaultValueForOptionalParameters, labels = DefaultValueForOptionalParameters ):
        post_parameters = {
            "title": title,
        }
        if body is not DefaultValueForOptionalParameters:
            post_parameters[ "body" ] = body
        if assignee is not DefaultValueForOptionalParameters:
            post_parameters[ "assignee" ] = assignee
        if milestone is not DefaultValueForOptionalParameters:
            post_parameters[ "milestone" ] = milestone
        if labels is not DefaultValueForOptionalParameters:
            post_parameters[ "labels" ] = labels
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/issues",
            None,
            post_parameters
        )
        return Issue.Issue( self.__requester, data, lazy = True )

    def create_key( self, title, key ):
        post_parameters = {
            "title": title,
            "key": key,
        }
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/keys",
            None,
            post_parameters
        )
        return RepositoryKey.RepositoryKey( self.__requester, data, lazy = True )

    def create_label( self, name, color ):
        post_parameters = {
            "name": name,
            "color": color,
        }
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/labels",
            None,
            post_parameters
        )
        return Label.Label( self.__requester, data, lazy = True )

    def create_milestone( self, title, state = DefaultValueForOptionalParameters, description = DefaultValueForOptionalParameters, due_on = DefaultValueForOptionalParameters ):
        post_parameters = {
            "title": title,
        }
        if state is not DefaultValueForOptionalParameters:
            post_parameters[ "state" ] = state
        if description is not DefaultValueForOptionalParameters:
            post_parameters[ "description" ] = description
        if due_on is not DefaultValueForOptionalParameters:
            post_parameters[ "due_on" ] = due_on
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/milestones",
            None,
            post_parameters
        )
        return Milestone.Milestone( self.__requester, data, lazy = True )

    def edit( self, name, description = DefaultValueForOptionalParameters, homepage = DefaultValueForOptionalParameters, public = DefaultValueForOptionalParameters, has_issues = DefaultValueForOptionalParameters, has_wiki = DefaultValueForOptionalParameters, has_downloads = DefaultValueForOptionalParameters ):
        post_parameters = {
            "name": name,
        }
        if description is not DefaultValueForOptionalParameters:
            post_parameters[ "description" ] = description
        if homepage is not DefaultValueForOptionalParameters:
            post_parameters[ "homepage" ] = homepage
        if public is not DefaultValueForOptionalParameters:
            post_parameters[ "public" ] = public
        if has_issues is not DefaultValueForOptionalParameters:
            post_parameters[ "has_issues" ] = has_issues
        if has_wiki is not DefaultValueForOptionalParameters:
            post_parameters[ "has_wiki" ] = has_wiki
        if has_downloads is not DefaultValueForOptionalParameters:
            post_parameters[ "has_downloads" ] = has_downloads
        status, headers, data = self.__requester.request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self.__useAttributes( data )

    def get_branches( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/branches",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Branch.Branch,
            self.__requester,
            headers,
            data
        )

    def get_collaborators( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/collaborators",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self.__requester,
            headers,
            data
        )

    def get_comment( self, id ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/comments" + "/" + str( id ),
            None,
            None
        )
        return CommitComment.CommitComment( self.__requester, data, lazy = True )

    def get_comments( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/comments",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            CommitComment.CommitComment,
            self.__requester,
            headers,
            data
        )

    def get_commit( self, sha ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/commits" + "/" + str( sha ),
            None,
            None
        )
        return Commit.Commit( self.__requester, data, lazy = True )

    def get_commits( self, sha = DefaultValueForOptionalParameters, path = DefaultValueForOptionalParameters ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/commits",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Commit.Commit,
            self.__requester,
            headers,
            data
        )

    def get_contributors( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/contributors",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self.__requester,
            headers,
            data
        )

    def get_download( self, id ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/downloads" + "/" + str( id ),
            None,
            None
        )
        return Download.Download( self.__requester, data, lazy = True )

    def get_downloads( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/downloads",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Download.Download,
            self.__requester,
            headers,
            data
        )

    def get_events( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/events",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Event.Event,
            self.__requester,
            headers,
            data
        )

    def get_forks( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/forks",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Repository,
            self.__requester,
            headers,
            data
        )

    def get_git_blob( self, sha ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/git_blobs" + "/" + str( sha ),
            None,
            None
        )
        return GitBlob.GitBlob( self.__requester, data, lazy = True )

    def get_git_commit( self, sha ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/git_commits" + "/" + str( sha ),
            None,
            None
        )
        return GitCommit.GitCommit( self.__requester, data, lazy = True )

    def get_git_ref( self, ref ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/git_refs" + "/" + str( ref ),
            None,
            None
        )
        return GitRef.GitRef( self.__requester, data, lazy = True )

    def get_git_refs( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/git_refs",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            GitRef.GitRef,
            self.__requester,
            headers,
            data
        )

    def get_git_tag( self, sha ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/git_tags" + "/" + str( sha ),
            None,
            None
        )
        return GitTag.GitTag( self.__requester, data, lazy = True )

    def get_git_tree( self, sha, recursive = DefaultValueForOptionalParameters ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/git_trees" + "/" + str( sha ),
            None,
            None
        )
        return GitTree.GitTree( self.__requester, data, lazy = True )

    def get_hook( self, id ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/hooks" + "/" + str( id ),
            None,
            None
        )
        return Hook.Hook( self.__requester, data, lazy = True )

    def get_hooks( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/hooks",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Hook.Hook,
            self.__requester,
            headers,
            data
        )

    def get_issue( self, number ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/issues" + "/" + str( number ),
            None,
            None
        )
        return Issue.Issue( self.__requester, data, lazy = True )

    def get_issues( self, milestone = DefaultValueForOptionalParameters, state = DefaultValueForOptionalParameters, assignee = DefaultValueForOptionalParameters, mentioned = DefaultValueForOptionalParameters, labels = DefaultValueForOptionalParameters, sort = DefaultValueForOptionalParameters, direction = DefaultValueForOptionalParameters, since = DefaultValueForOptionalParameters ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/issues",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Issue.Issue,
            self.__requester,
            headers,
            data
        )

    def get_issues_event( self, id ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/issues/events" + "/" + str( id ),
            None,
            None
        )
        return IssueEvent.IssueEvent( self.__requester, data, lazy = True )

    def get_issues_events( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/issues/events",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            IssueEvent.IssueEvent,
            self.__requester,
            headers,
            data
        )

    def get_key( self, id ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/keys" + "/" + str( id ),
            None,
            None
        )
        return RepositoryKey.RepositoryKey( self.__requester, data, lazy = True )

    def get_keys( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/keys",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            RepositoryKey.RepositoryKey,
            self.__requester,
            headers,
            data
        )

    def get_label( self, name ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/labels" + "/" + str( name ),
            None,
            None
        )
        return Label.Label( self.__requester, data, lazy = True )

    def get_labels( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/labels",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Label.Label,
            self.__requester,
            headers,
            data
        )

    def get_languages( self ):
        pass

    def get_milestone( self, number ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/milestones" + "/" + str( number ),
            None,
            None
        )
        return Milestone.Milestone( self.__requester, data, lazy = True )

    def get_milestones( self, state = DefaultValueForOptionalParameters, sort = DefaultValueForOptionalParameters, direction = DefaultValueForOptionalParameters ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/milestones",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Milestone.Milestone,
            self.__requester,
            headers,
            data
        )

    def get_network_events( self ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/networks/" + str( self.owner.login ) + "/" + str( self.name ) + "/events",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Event.Event,
            self.__requester,
            headers,
            data
        )

    def get_pull( self, number ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/pulls" + "/" + str( number ),
            None,
            None
        )
        return PullRequest.PullRequest( self.__requester, data, lazy = True )

    def get_pulls( self, state = DefaultValueForOptionalParameters ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/pulls",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            PullRequest.PullRequest,
            self.__requester,
            headers,
            data
        )

    def get_tags( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/tags",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Tag.Tag,
            self.__requester,
            headers,
            data
        )

    def get_teams( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/teams",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Team.Team,
            self.__requester,
            headers,
            data
        )

    def get_watchers( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/watchers",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self.__requester,
            headers,
            data
        )

    def has_in_collaborators( self, collaborator ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/collaborators" + "/" + str( collaborator._identity ),
            None,
            None
        )
        return status == 204

    def remove_from_collaborators( self, collaborator ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ) + "/collaborators" + "/" + str( collaborator._identity ),
            None,
            None
        )

    # @todo Remove '_identity' from the normalized json description
    @property
    def _identity( self ):
        return str( self.owner.login ) + "/" + str( self.name )

    def __initAttributes( self ):
        self.__clone_url = None
        self.__created_at = None
        self.__description = None
        self.__fork = None
        self.__forks = None
        self.__git_url = None
        self.__has_downloads = None
        self.__has_issues = None
        self.__has_wiki = None
        self.__homepage = None
        self.__html_url = None
        self.__id = None
        self.__language = None
        self.__master_branch = None
        self.__mirror_url = None
        self.__name = None
        self.__open_issues = None
        self.__organization = None
        self.__owner = None
        self.__parent = None
        self.__permissions = None
        self.__private = None
        self.__pushed_at = None
        self.__size = None
        self.__source = None
        self.__ssh_url = None
        self.__svn_url = None
        self.__updated_at = None
        self.__url = None
        self.__watchers = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete()

    # @todo Do not generate __complete if type has no url attribute
    def __complete( self ):
        status, headers, data = self.__requester.request(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( data )
        self.__completed = True

    def __useAttributes( self, attributes ):
         #@todo No need to check if attribute is in attributes when attribute is mandatory
        if "clone_url" in attributes and attributes[ "clone_url" ] is not None:
            self.__clone_url = attributes[ "clone_url" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None:
            self.__created_at = attributes[ "created_at" ]
        if "description" in attributes and attributes[ "description" ] is not None:
            self.__description = attributes[ "description" ]
        if "fork" in attributes and attributes[ "fork" ] is not None:
            self.__fork = attributes[ "fork" ]
        if "forks" in attributes and attributes[ "forks" ] is not None:
            self.__forks = attributes[ "forks" ]
        if "git_url" in attributes and attributes[ "git_url" ] is not None:
            self.__git_url = attributes[ "git_url" ]
        if "has_downloads" in attributes and attributes[ "has_downloads" ] is not None:
            self.__has_downloads = attributes[ "has_downloads" ]
        if "has_issues" in attributes and attributes[ "has_issues" ] is not None:
            self.__has_issues = attributes[ "has_issues" ]
        if "has_wiki" in attributes and attributes[ "has_wiki" ] is not None:
            self.__has_wiki = attributes[ "has_wiki" ]
        if "homepage" in attributes and attributes[ "homepage" ] is not None:
            self.__homepage = attributes[ "homepage" ]
        if "html_url" in attributes and attributes[ "html_url" ] is not None:
            self.__html_url = attributes[ "html_url" ]
        if "id" in attributes and attributes[ "id" ] is not None:
            self.__id = attributes[ "id" ]
        if "language" in attributes and attributes[ "language" ] is not None:
            self.__language = attributes[ "language" ]
        if "master_branch" in attributes and attributes[ "master_branch" ] is not None:
            self.__master_branch = attributes[ "master_branch" ]
        if "mirror_url" in attributes and attributes[ "mirror_url" ] is not None:
            self.__mirror_url = attributes[ "mirror_url" ]
        if "name" in attributes and attributes[ "name" ] is not None:
            self.__name = attributes[ "name" ]
        if "open_issues" in attributes and attributes[ "open_issues" ] is not None:
            self.__open_issues = attributes[ "open_issues" ]
        if "organization" in attributes and attributes[ "organization" ] is not None:
            self.__organization = attributes[ "organization" ]
        if "owner" in attributes and attributes[ "owner" ] is not None:
            self.__owner = NamedUser.NamedUser( self.__requester, attributes[ "owner" ], lazy = True )
        if "parent" in attributes and attributes[ "parent" ] is not None:
            self.__parent = Repository( self.__requester, attributes[ "parent" ], lazy = True )
        if "permissions" in attributes and attributes[ "permissions" ] is not None:
            self.__permissions = attributes[ "permissions" ]
        if "private" in attributes and attributes[ "private" ] is not None:
            self.__private = attributes[ "private" ]
        if "pushed_at" in attributes and attributes[ "pushed_at" ] is not None:
            self.__pushed_at = attributes[ "pushed_at" ]
        if "size" in attributes and attributes[ "size" ] is not None:
            self.__size = attributes[ "size" ]
        if "source" in attributes and attributes[ "source" ] is not None:
            self.__source = Repository( self.__requester, attributes[ "source" ], lazy = True )
        if "ssh_url" in attributes and attributes[ "ssh_url" ] is not None:
            self.__ssh_url = attributes[ "ssh_url" ]
        if "svn_url" in attributes and attributes[ "svn_url" ] is not None:
            self.__svn_url = attributes[ "svn_url" ]
        if "updated_at" in attributes and attributes[ "updated_at" ] is not None:
            self.__updated_at = attributes[ "updated_at" ]
        if "url" in attributes and attributes[ "url" ] is not None:
            self.__url = attributes[ "url" ]
        if "watchers" in attributes and attributes[ "watchers" ] is not None:
            self.__watchers = attributes[ "watchers" ]
