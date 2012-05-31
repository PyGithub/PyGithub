# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import urllib
##########
import GithubObject
import PaginatedList
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters
##########
import Branch
import IssueEvent
import Label
import GitBlob
import Commit
import GitRef
import Issue
import Repository
import PullRequest
import RepositoryKey
import NamedUser
import Milestone
import Permissions
import CommitComment
import GitCommit
import Team
import Organization
import GitTree
import Hook
import Tag
import GitTag
import Download
import Event

class Repository( GithubObject.GithubObject ):
    @property
    def clone_url( self ):
        self._completeIfNeeded( self._clone_url )
        return self._clone_url

    @property
    def created_at( self ):
        self._completeIfNeeded( self._created_at )
        return self._created_at

    @property
    def description( self ):
        self._completeIfNeeded( self._description )
        return self._description

    @property
    def fork( self ):
        self._completeIfNeeded( self._fork )
        return self._fork

    @property
    def forks( self ):
        self._completeIfNeeded( self._forks )
        return self._forks

    @property
    def full_name( self ):
        self._completeIfNeeded( self._full_name )
        return self._full_name

    @property
    def git_url( self ):
        self._completeIfNeeded( self._git_url )
        return self._git_url

    @property
    def has_downloads( self ):
        self._completeIfNeeded( self._has_downloads )
        return self._has_downloads

    @property
    def has_issues( self ):
        self._completeIfNeeded( self._has_issues )
        return self._has_issues

    @property
    def has_wiki( self ):
        self._completeIfNeeded( self._has_wiki )
        return self._has_wiki

    @property
    def homepage( self ):
        self._completeIfNeeded( self._homepage )
        return self._homepage

    @property
    def html_url( self ):
        self._completeIfNeeded( self._html_url )
        return self._html_url

    @property
    def id( self ):
        self._completeIfNeeded( self._id )
        return self._id

    @property
    def language( self ):
        self._completeIfNeeded( self._language )
        return self._language

    @property
    def master_branch( self ):
        self._completeIfNeeded( self._master_branch )
        return self._master_branch

    @property
    def name( self ):
        self._completeIfNeeded( self._name )
        return self._name

    @property
    def open_issues( self ):
        self._completeIfNeeded( self._open_issues )
        return self._open_issues

    @property
    def organization( self ):
        self._completeIfNeeded( self._organization )
        return self._organization

    @property
    def owner( self ):
        self._completeIfNeeded( self._owner )
        return self._owner

    @property
    def parent( self ):
        self._completeIfNeeded( self._parent )
        return self._parent

    @property
    def permissions( self ):
        self._completeIfNeeded( self._permissions )
        return self._permissions

    @property
    def private( self ):
        self._completeIfNeeded( self._private )
        return self._private

    @property
    def pushed_at( self ):
        self._completeIfNeeded( self._pushed_at )
        return self._pushed_at

    @property
    def size( self ):
        self._completeIfNeeded( self._size )
        return self._size

    @property
    def source( self ):
        self._completeIfNeeded( self._source )
        return self._source

    @property
    def ssh_url( self ):
        self._completeIfNeeded( self._ssh_url )
        return self._ssh_url

    @property
    def svn_url( self ):
        self._completeIfNeeded( self._svn_url )
        return self._svn_url

    @property
    def updated_at( self ):
        self._completeIfNeeded( self._updated_at )
        return self._updated_at

    @property
    def url( self ):
        self._completeIfNeeded( self._url )
        return self._url

    @property
    def watchers( self ):
        self._completeIfNeeded( self._watchers )
        return self._watchers

    def add_to_collaborators( self, collaborator ):
        assert isinstance( collaborator, NamedUser.NamedUser ), collaborator
        status, headers, data = self._request(
            "PUT",
            str( self.url ) + "/collaborators/" + str( collaborator._identity ),
            None,
            None
        )
        self._checkStatus( status, data )

    def compare( self, base, head ):
        assert isinstance( base, ( str, unicode ) ), base
        assert isinstance( head, ( str, unicode ) ), head
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/compare/" + str( base ) + "..." + str( head ),
            None,
            None
        )
        self._checkStatus( status, data )
        return data

    def create_download( self, name, size, description = DefaultValueForOptionalParameters, content_type = DefaultValueForOptionalParameters ):
        assert isinstance( name, ( str, unicode ) ), name
        assert isinstance( size, int ), size
        if description is not DefaultValueForOptionalParameters:
            assert isinstance( description, ( str, unicode ) ), description
        if content_type is not DefaultValueForOptionalParameters:
            assert isinstance( content_type, ( str, unicode ) ), content_type
        post_parameters = {
            "name": name,
            "size": size,
        }
        if description is not DefaultValueForOptionalParameters:
            post_parameters[ "description" ] = description
        if content_type is not DefaultValueForOptionalParameters:
            post_parameters[ "content_type" ] = content_type
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/downloads",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return Download.Download( self._requester, data, completed = True )

    def create_git_blob( self, content, encoding ):
        assert isinstance( content, ( str, unicode ) ), content
        assert isinstance( encoding, ( str, unicode ) ), encoding
        post_parameters = {
            "content": content,
            "encoding": encoding,
        }
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/git/blobs",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return GitBlob.GitBlob( self._requester, data, completed = True )

    def create_git_commit( self, message, tree, parents, author = DefaultValueForOptionalParameters, committer = DefaultValueForOptionalParameters ):
        assert isinstance( message, ( str, unicode ) ), message
        assert all( isinstance( element, GitCommit.GitCommit ) for element in parents ), parents
        post_parameters = {
            "message": message,
            "tree": tree,
            "parents": parents,
        }
        if author is not DefaultValueForOptionalParameters:
            post_parameters[ "author" ] = author
        if committer is not DefaultValueForOptionalParameters:
            post_parameters[ "committer" ] = committer
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/git/commits",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return GitCommit.GitCommit( self._requester, data, completed = True )

    def create_git_ref( self, ref, sha ):
        assert isinstance( ref, ( str, unicode ) ), ref
        assert isinstance( sha, ( str, unicode ) ), sha
        post_parameters = {
            "ref": ref,
            "sha": sha,
        }
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/git/refs",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return GitRef.GitRef( self._requester, data, completed = True )

    def create_git_tag( self, tag, message, object, type, tagger = DefaultValueForOptionalParameters ):
        assert isinstance( tag, ( str, unicode ) ), tag
        assert isinstance( message, ( str, unicode ) ), message
        assert isinstance( object, ( str, unicode ) ), object
        assert isinstance( type, ( str, unicode ) ), type
        post_parameters = {
            "tag": tag,
            "message": message,
            "object": object,
            "type": type,
        }
        if tagger is not DefaultValueForOptionalParameters:
            post_parameters[ "tagger" ] = tagger
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/git/tags",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return GitTag.GitTag( self._requester, data, completed = True )

    def create_git_tree( self, tree, base_tree = DefaultValueForOptionalParameters ):
        post_parameters = {
            "tree": tree,
        }
        if base_tree is not DefaultValueForOptionalParameters:
            post_parameters[ "base_tree" ] = base_tree
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/git/trees",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return GitTree.GitTree( self._requester, data, completed = True )

    def create_hook( self, name, config, events = DefaultValueForOptionalParameters, active = DefaultValueForOptionalParameters ):
        assert isinstance( name, ( str, unicode ) ), name
        if events is not DefaultValueForOptionalParameters:
            assert all( isinstance( element, ( str, unicode ) ) for element in events ), events
        if active is not DefaultValueForOptionalParameters:
            assert isinstance( active, bool ), active
        post_parameters = {
            "name": name,
            "config": config,
        }
        if events is not DefaultValueForOptionalParameters:
            post_parameters[ "events" ] = events
        if active is not DefaultValueForOptionalParameters:
            post_parameters[ "active" ] = active
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/hooks",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return Hook.Hook( self._requester, data, completed = True )

    def create_issue( self, title, body = DefaultValueForOptionalParameters, assignee = DefaultValueForOptionalParameters, milestone = DefaultValueForOptionalParameters, labels = DefaultValueForOptionalParameters ):
        assert isinstance( title, ( str, unicode ) ), title
        if body is not DefaultValueForOptionalParameters:
            assert isinstance( body, ( str, unicode ) ), body
        if assignee is not DefaultValueForOptionalParameters:
            assert isinstance( assignee, ( str, unicode ) ), assignee
        if milestone is not DefaultValueForOptionalParameters:
            assert isinstance( milestone, int ), milestone
        if labels is not DefaultValueForOptionalParameters:
            assert all( isinstance( element, ( str, unicode ) ) for element in labels ), labels
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
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/issues",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return Issue.Issue( self._requester, data, completed = True )

    def create_key( self, title, key ):
        assert isinstance( title, ( str, unicode ) ), title
        assert isinstance( key, ( str, unicode ) ), key
        post_parameters = {
            "title": title,
            "key": key,
        }
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/keys",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return RepositoryKey.RepositoryKey( self._requester, data, completed = True, repoUrl = self._url )

    def create_label( self, name, color ):
        assert isinstance( name, ( str, unicode ) ), name
        assert isinstance( color, ( str, unicode ) ), color
        post_parameters = {
            "name": name,
            "color": color,
        }
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/labels",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return Label.Label( self._requester, data, completed = True )

    def create_milestone( self, title, state = DefaultValueForOptionalParameters, description = DefaultValueForOptionalParameters, due_on = DefaultValueForOptionalParameters ):
        assert isinstance( title, ( str, unicode ) ), title
        if state is not DefaultValueForOptionalParameters:
            assert isinstance( state, ( str, unicode ) ), state
        if description is not DefaultValueForOptionalParameters:
            assert isinstance( description, ( str, unicode ) ), description
        if due_on is not DefaultValueForOptionalParameters:
            assert isinstance( due_on, ( str, unicode ) ), due_on
        post_parameters = {
            "title": title,
        }
        if state is not DefaultValueForOptionalParameters:
            post_parameters[ "state" ] = state
        if description is not DefaultValueForOptionalParameters:
            post_parameters[ "description" ] = description
        if due_on is not DefaultValueForOptionalParameters:
            post_parameters[ "due_on" ] = due_on
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/milestones",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return Milestone.Milestone( self._requester, data, completed = True )

    def create_pull( self, *args, **kwds ):
        if len( args ) + len( kwds ) == 4:
            return self.__create_pull_1( *args, **kwds )
        else:
            return self.__create_pull_2( *args, **kwds )

    def __create_pull_1( self, title, body, base, head ):
        assert isinstance( title, ( str, unicode ) ), title
        assert isinstance( body, ( str, unicode ) ), body
        return self.__create_pull( title = title, body = body, base = base, head = head )

    def __create_pull_2( self, issue, base, head ):
        assert isinstance( issue, int ), issue
        return self.__create_pull( issue = issue, base = base, head = head )

    def __create_pull( self, **kwds ):
        post_parameters = kwds
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/pulls",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return PullRequest.PullRequest( self._requester, data, completed = True )

    def edit( self, name, description = DefaultValueForOptionalParameters, homepage = DefaultValueForOptionalParameters, public = DefaultValueForOptionalParameters, has_issues = DefaultValueForOptionalParameters, has_wiki = DefaultValueForOptionalParameters, has_downloads = DefaultValueForOptionalParameters ):
        assert isinstance( name, ( str, unicode ) ), name
        if description is not DefaultValueForOptionalParameters:
            assert isinstance( description, ( str, unicode ) ), description
        if homepage is not DefaultValueForOptionalParameters:
            assert isinstance( homepage, ( str, unicode ) ), homepage
        if public is not DefaultValueForOptionalParameters:
            assert isinstance( public, bool ), public
        if has_issues is not DefaultValueForOptionalParameters:
            assert isinstance( has_issues, bool ), has_issues
        if has_wiki is not DefaultValueForOptionalParameters:
            assert isinstance( has_wiki, bool ), has_wiki
        if has_downloads is not DefaultValueForOptionalParameters:
            assert isinstance( has_downloads, bool ), has_downloads
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
        status, headers, data = self._request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        self._useAttributes( data )

    def get_branches( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/branches",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Branch.Branch,
            self._requester,
            headers,
            data
        )

    def get_collaborators( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/collaborators",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self._requester,
            headers,
            data
        )

    def get_comment( self, id ):
        assert isinstance( id, int ), id
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/comments/" + str( id ),
            None,
            None
        )
        self._checkStatus( status, data )
        return CommitComment.CommitComment( self._requester, data, completed = True )

    def get_comments( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/comments",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            CommitComment.CommitComment,
            self._requester,
            headers,
            data
        )

    def get_commit( self, sha ):
        assert isinstance( sha, ( str, unicode ) ), sha
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/commits/" + str( sha ),
            None,
            None
        )
        self._checkStatus( status, data )
        return Commit.Commit( self._requester, data, completed = True )

    def get_commits( self, sha = DefaultValueForOptionalParameters, path = DefaultValueForOptionalParameters ):
        if sha is not DefaultValueForOptionalParameters:
            assert isinstance( sha, ( str, unicode ) ), sha
        if path is not DefaultValueForOptionalParameters:
            assert isinstance( path, ( str, unicode ) ), path
        url_parameters = dict()
        if sha is not DefaultValueForOptionalParameters:
            url_parameters[ "sha" ] = sha
        if path is not DefaultValueForOptionalParameters:
            url_parameters[ "path" ] = path
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/commits",
            url_parameters,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Commit.Commit,
            self._requester,
            headers,
            data
        )

    def get_contributors( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/contributors",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self._requester,
            headers,
            data
        )

    def get_download( self, id ):
        assert isinstance( id, int ), id
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/downloads/" + str( id ),
            None,
            None
        )
        self._checkStatus( status, data )
        return Download.Download( self._requester, data, completed = True )

    def get_downloads( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/downloads",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Download.Download,
            self._requester,
            headers,
            data
        )

    def get_events( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/events",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Event.Event,
            self._requester,
            headers,
            data
        )

    def get_forks( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/forks",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Repository,
            self._requester,
            headers,
            data
        )

    def get_git_blob( self, sha ):
        assert isinstance( sha, ( str, unicode ) ), sha
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/git/blobs/" + str( sha ),
            None,
            None
        )
        self._checkStatus( status, data )
        return GitBlob.GitBlob( self._requester, data, completed = True )

    def get_git_commit( self, sha ):
        assert isinstance( sha, ( str, unicode ) ), sha
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/git/commits/" + str( sha ),
            None,
            None
        )
        self._checkStatus( status, data )
        return GitCommit.GitCommit( self._requester, data, completed = True )

    def get_git_ref( self, ref ):
        assert isinstance( ref, ( str, unicode ) ), ref
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/git/" + str( ref ),
            None,
            None
        )
        self._checkStatus( status, data )
        return GitRef.GitRef( self._requester, data, completed = True )

    def get_git_refs( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/git/refs",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            GitRef.GitRef,
            self._requester,
            headers,
            data
        )

    def get_git_tag( self, sha ):
        assert isinstance( sha, ( str, unicode ) ), sha
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/git/tags/" + str( sha ),
            None,
            None
        )
        self._checkStatus( status, data )
        return GitTag.GitTag( self._requester, data, completed = True )

    def get_git_tree( self, sha, recursive = DefaultValueForOptionalParameters ):
        assert isinstance( sha, ( str, unicode ) ), sha
        if recursive is not DefaultValueForOptionalParameters:
            assert isinstance( recursive, bool ), recursive
        url_parameters = dict()
        if recursive is not DefaultValueForOptionalParameters:
            url_parameters[ "recursive" ] = recursive
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/git/trees/" + str( sha ),
            url_parameters,
            None
        )
        self._checkStatus( status, data )
        return GitTree.GitTree( self._requester, data, completed = True )

    def get_hook( self, id ):
        assert isinstance( id, int ), id
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/hooks/" + str( id ),
            None,
            None
        )
        self._checkStatus( status, data )
        return Hook.Hook( self._requester, data, completed = True )

    def get_hooks( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/hooks",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Hook.Hook,
            self._requester,
            headers,
            data
        )

    def get_issue( self, number ):
        assert isinstance( number, int ), number
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/issues/" + str( number ),
            None,
            None
        )
        self._checkStatus( status, data )
        return Issue.Issue( self._requester, data, completed = True )

    def get_issues( self, milestone = DefaultValueForOptionalParameters, state = DefaultValueForOptionalParameters, assignee = DefaultValueForOptionalParameters, mentioned = DefaultValueForOptionalParameters, labels = DefaultValueForOptionalParameters, sort = DefaultValueForOptionalParameters, direction = DefaultValueForOptionalParameters, since = DefaultValueForOptionalParameters ):
        if milestone is not DefaultValueForOptionalParameters:
            assert isinstance( milestone, int ), milestone
        if state is not DefaultValueForOptionalParameters:
            assert isinstance( state, ( str, unicode ) ), state
        if assignee is not DefaultValueForOptionalParameters:
            assert isinstance( assignee, ( str, unicode ) ), assignee
        if mentioned is not DefaultValueForOptionalParameters:
            assert isinstance( mentioned, ( str, unicode ) ), mentioned
        if labels is not DefaultValueForOptionalParameters:
            assert isinstance( labels, ( str, unicode ) ), labels
        if sort is not DefaultValueForOptionalParameters:
            assert isinstance( sort, ( str, unicode ) ), sort
        if direction is not DefaultValueForOptionalParameters:
            assert isinstance( direction, ( str, unicode ) ), direction
        if since is not DefaultValueForOptionalParameters:
            assert isinstance( since, ( str, unicode ) ), since
        url_parameters = dict()
        if milestone is not DefaultValueForOptionalParameters:
            url_parameters[ "milestone" ] = milestone
        if state is not DefaultValueForOptionalParameters:
            url_parameters[ "state" ] = state
        if assignee is not DefaultValueForOptionalParameters:
            url_parameters[ "assignee" ] = assignee
        if mentioned is not DefaultValueForOptionalParameters:
            url_parameters[ "mentioned" ] = mentioned
        if labels is not DefaultValueForOptionalParameters:
            url_parameters[ "labels" ] = labels
        if sort is not DefaultValueForOptionalParameters:
            url_parameters[ "sort" ] = sort
        if direction is not DefaultValueForOptionalParameters:
            url_parameters[ "direction" ] = direction
        if since is not DefaultValueForOptionalParameters:
            url_parameters[ "since" ] = since
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/issues",
            url_parameters,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Issue.Issue,
            self._requester,
            headers,
            data
        )

    def get_issues_event( self, id ):
        assert isinstance( id, int ), id
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/issues/events/" + str( id ),
            None,
            None
        )
        self._checkStatus( status, data )
        return IssueEvent.IssueEvent( self._requester, data, completed = True )

    def get_issues_events( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/issues/events",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            IssueEvent.IssueEvent,
            self._requester,
            headers,
            data
        )

    def get_key( self, id ):
        assert isinstance( id, int ), id
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/keys/" + str( id ),
            None,
            None
        )
        self._checkStatus( status, data )
        return RepositoryKey.RepositoryKey( self._requester, data, completed = True, repoUrl = self._url )

    def get_keys( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/keys",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            lambda requester, data, completed: RepositoryKey.RepositoryKey( requester, data, completed, repoUrl = self._url ),
            self._requester,
            headers,
            data
        )

    def get_label( self, name ):
        assert isinstance( name, ( str, unicode ) ), name
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/labels/" + urllib.quote( str( name ) ),
            None,
            None
        )
        self._checkStatus( status, data )
        return Label.Label( self._requester, data, completed = True )

    def get_labels( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/labels",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Label.Label,
            self._requester,
            headers,
            data
        )

    def get_languages( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/languages",
            None,
            None
        )
        self._checkStatus( status, data )
        return data

    def get_milestone( self, number ):
        assert isinstance( number, int ), number
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/milestones/" + str( number ),
            None,
            None
        )
        self._checkStatus( status, data )
        return Milestone.Milestone( self._requester, data, completed = True )

    def get_milestones( self, state = DefaultValueForOptionalParameters, sort = DefaultValueForOptionalParameters, direction = DefaultValueForOptionalParameters ):
        if state is not DefaultValueForOptionalParameters:
            assert isinstance( state, ( str, unicode ) ), state
        if sort is not DefaultValueForOptionalParameters:
            assert isinstance( sort, ( str, unicode ) ), sort
        if direction is not DefaultValueForOptionalParameters:
            assert isinstance( direction, ( str, unicode ) ), direction
        url_parameters = dict()
        if state is not DefaultValueForOptionalParameters:
            url_parameters[ "state" ] = state
        if sort is not DefaultValueForOptionalParameters:
            url_parameters[ "sort" ] = sort
        if direction is not DefaultValueForOptionalParameters:
            url_parameters[ "direction" ] = direction
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/milestones",
            url_parameters,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Milestone.Milestone,
            self._requester,
            headers,
            data
        )

    def get_network_events( self ):
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/networks/" + str( self.owner.login ) + "/" + str( self.name ) + "/events",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Event.Event,
            self._requester,
            headers,
            data
        )

    def get_pull( self, number ):
        assert isinstance( number, int ), number
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/pulls/" + str( number ),
            None,
            None
        )
        self._checkStatus( status, data )
        return PullRequest.PullRequest( self._requester, data, completed = True )

    def get_pulls( self, state = DefaultValueForOptionalParameters ):
        if state is not DefaultValueForOptionalParameters:
            assert isinstance( state, ( str, unicode ) ), state
        url_parameters = dict()
        if state is not DefaultValueForOptionalParameters:
            url_parameters[ "state" ] = state
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/pulls",
            url_parameters,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            PullRequest.PullRequest,
            self._requester,
            headers,
            data
        )

    def get_tags( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/tags",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Tag.Tag,
            self._requester,
            headers,
            data
        )

    def get_teams( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/teams",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Team.Team,
            self._requester,
            headers,
            data
        )

    def get_watchers( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/watchers",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self._requester,
            headers,
            data
        )

    def has_in_collaborators( self, collaborator ):
        assert isinstance( collaborator, NamedUser.NamedUser ), collaborator
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/collaborators/" + str( collaborator._identity ),
            None,
            None
        )
        return status == 204

    def remove_from_collaborators( self, collaborator ):
        assert isinstance( collaborator, NamedUser.NamedUser ), collaborator
        status, headers, data = self._request(
            "DELETE",
            str( self.url ) + "/collaborators/" + str( collaborator._identity ),
            None,
            None
        )
        self._checkStatus( status, data )

    @property
    def _identity( self ):
        return str( self.owner.login ) + "/" + str( self.name )

    def _initAttributes( self ):
        self._clone_url = None
        self._created_at = None
        self._description = None
        self._fork = None
        self._forks = None
        self._full_name = None
        self._git_url = None
        self._has_downloads = None
        self._has_issues = None
        self._has_wiki = None
        self._homepage = None
        self._html_url = None
        self._id = None
        self._language = None
        self._master_branch = None
        self._name = None
        self._open_issues = None
        self._organization = None
        self._owner = None
        self._parent = None
        self._permissions = None
        self._private = None
        self._pushed_at = None
        self._size = None
        self._source = None
        self._ssh_url = None
        self._svn_url = None
        self._updated_at = None
        self._url = None
        self._watchers = None

    def _useAttributes( self, attributes ):
        if "clone_url" in attributes and attributes[ "clone_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "clone_url" ], ( str, unicode ) ), attributes[ "clone_url" ]
            self._clone_url = attributes[ "clone_url" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self._created_at = attributes[ "created_at" ]
        if "description" in attributes and attributes[ "description" ] is not None: # pragma no branch
            assert isinstance( attributes[ "description" ], ( str, unicode ) ), attributes[ "description" ]
            self._description = attributes[ "description" ]
        if "fork" in attributes and attributes[ "fork" ] is not None: # pragma no branch
            assert isinstance( attributes[ "fork" ], bool ), attributes[ "fork" ]
            self._fork = attributes[ "fork" ]
        if "forks" in attributes and attributes[ "forks" ] is not None: # pragma no branch
            assert isinstance( attributes[ "forks" ], int ), attributes[ "forks" ]
            self._forks = attributes[ "forks" ]
        if "full_name" in attributes and attributes[ "full_name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "full_name" ], ( str, unicode ) ), attributes[ "full_name" ]
            self._full_name = attributes[ "full_name" ]
        if "git_url" in attributes and attributes[ "git_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "git_url" ], ( str, unicode ) ), attributes[ "git_url" ]
            self._git_url = attributes[ "git_url" ]
        if "has_downloads" in attributes and attributes[ "has_downloads" ] is not None: # pragma no branch
            assert isinstance( attributes[ "has_downloads" ], bool ), attributes[ "has_downloads" ]
            self._has_downloads = attributes[ "has_downloads" ]
        if "has_issues" in attributes and attributes[ "has_issues" ] is not None: # pragma no branch
            assert isinstance( attributes[ "has_issues" ], bool ), attributes[ "has_issues" ]
            self._has_issues = attributes[ "has_issues" ]
        if "has_wiki" in attributes and attributes[ "has_wiki" ] is not None: # pragma no branch
            assert isinstance( attributes[ "has_wiki" ], bool ), attributes[ "has_wiki" ]
            self._has_wiki = attributes[ "has_wiki" ]
        if "homepage" in attributes and attributes[ "homepage" ] is not None: # pragma no branch
            assert isinstance( attributes[ "homepage" ], ( str, unicode ) ), attributes[ "homepage" ]
            self._homepage = attributes[ "homepage" ]
        if "html_url" in attributes and attributes[ "html_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "html_url" ], ( str, unicode ) ), attributes[ "html_url" ]
            self._html_url = attributes[ "html_url" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "language" in attributes and attributes[ "language" ] is not None: # pragma no branch
            assert isinstance( attributes[ "language" ], ( str, unicode ) ), attributes[ "language" ]
            self._language = attributes[ "language" ]
        if "master_branch" in attributes and attributes[ "master_branch" ] is not None: # pragma no branch
            assert isinstance( attributes[ "master_branch" ], ( str, unicode ) ), attributes[ "master_branch" ]
            self._master_branch = attributes[ "master_branch" ]
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
        if "open_issues" in attributes and attributes[ "open_issues" ] is not None: # pragma no branch
            assert isinstance( attributes[ "open_issues" ], int ), attributes[ "open_issues" ]
            self._open_issues = attributes[ "open_issues" ]
        if "organization" in attributes and attributes[ "organization" ] is not None: # pragma no branch
            assert isinstance( attributes[ "organization" ], dict ), attributes[ "organization" ]
            self._organization = Organization.Organization( self._requester, attributes[ "organization" ], completed = False )
        if "owner" in attributes and attributes[ "owner" ] is not None: # pragma no branch
            assert isinstance( attributes[ "owner" ], dict ), attributes[ "owner" ]
            self._owner = NamedUser.NamedUser( self._requester, attributes[ "owner" ], completed = False )
        if "parent" in attributes and attributes[ "parent" ] is not None: # pragma no branch
            assert isinstance( attributes[ "parent" ], dict ), attributes[ "parent" ]
            self._parent = Repository( self._requester, attributes[ "parent" ], completed = False )
        if "permissions" in attributes and attributes[ "permissions" ] is not None: # pragma no branch
            assert isinstance( attributes[ "permissions" ], dict ), attributes[ "permissions" ]
            self._permissions = Permissions.Permissions( self._requester, attributes[ "permissions" ], completed = False )
        if "private" in attributes and attributes[ "private" ] is not None: # pragma no branch
            assert isinstance( attributes[ "private" ], bool ), attributes[ "private" ]
            self._private = attributes[ "private" ]
        if "pushed_at" in attributes and attributes[ "pushed_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "pushed_at" ], ( str, unicode ) ), attributes[ "pushed_at" ]
            self._pushed_at = attributes[ "pushed_at" ]
        if "size" in attributes and attributes[ "size" ] is not None: # pragma no branch
            assert isinstance( attributes[ "size" ], int ), attributes[ "size" ]
            self._size = attributes[ "size" ]
        if "source" in attributes and attributes[ "source" ] is not None: # pragma no branch
            assert isinstance( attributes[ "source" ], dict ), attributes[ "source" ]
            self._source = Repository( self._requester, attributes[ "source" ], completed = False )
        if "ssh_url" in attributes and attributes[ "ssh_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "ssh_url" ], ( str, unicode ) ), attributes[ "ssh_url" ]
            self._ssh_url = attributes[ "ssh_url" ]
        if "svn_url" in attributes and attributes[ "svn_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "svn_url" ], ( str, unicode ) ), attributes[ "svn_url" ]
            self._svn_url = attributes[ "svn_url" ]
        if "updated_at" in attributes and attributes[ "updated_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "updated_at" ], ( str, unicode ) ), attributes[ "updated_at" ]
            self._updated_at = attributes[ "updated_at" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
        if "watchers" in attributes and attributes[ "watchers" ] is not None: # pragma no branch
            assert isinstance( attributes[ "watchers" ], int ), attributes[ "watchers" ]
            self._watchers = attributes[ "watchers" ]
