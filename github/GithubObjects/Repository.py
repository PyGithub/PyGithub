# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

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
            str( self.url ) + "/collaborators/" + str( collaborator.login ),
            None,
            None
        )

    def compare( self, base, head ):
        pass

    def create_download( self, name, size, description = None, content_type = None ):
        post_parameters = {
            "name": name,
            "size": size,
        }
        if description is not None:
            post_parameters[ "description" ] = description
        if content_type is not None:
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

    def create_git_commit( self, message, tree, parents, author = None, committer = None ):
        post_parameters = {
            "message": message,
            "tree": tree,
            "parents": parents,
        }
        if author is not None:
            post_parameters[ "author" ] = author
        if committer is not None:
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

    def create_git_tag( self, tag, message, object, type, tagger = None ):
        post_parameters = {
            "tag": tag,
            "message": message,
            "object": object,
            "type": type,
        }
        if tagger is not None:
            post_parameters[ "tagger" ] = tagger
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/git_tags",
            None,
            post_parameters
        )
        return GitTag.GitTag( self.__requester, data, lazy = True )

    def create_git_tree( self, tree, base_tree = None ):
        post_parameters = {
            "tree": tree,
        }
        if base_tree is not None:
            post_parameters[ "base_tree" ] = base_tree
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/git_trees",
            None,
            post_parameters
        )
        return GitTree.GitTree( self.__requester, data, lazy = True )

    def create_hook( self, name, config, events = None, active = None ):
        post_parameters = {
            "name": name,
            "config": config,
        }
        if events is not None:
            post_parameters[ "events" ] = events
        if active is not None:
            post_parameters[ "active" ] = active
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/hooks",
            None,
            post_parameters
        )
        return Hook.Hook( self.__requester, data, lazy = True )

    def create_issue( self, title, body = None, assignee = None, milestone = None, labels = None ):
        post_parameters = {
            "title": title,
        }
        if body is not None:
            post_parameters[ "body" ] = body
        if assignee is not None:
            post_parameters[ "assignee" ] = assignee
        if milestone is not None:
            post_parameters[ "milestone" ] = milestone
        if labels is not None:
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

    def create_milestone( self, title, state = None, description = None, due_on = None ):
        post_parameters = {
            "title": title,
        }
        if state is not None:
            post_parameters[ "state" ] = state
        if description is not None:
            post_parameters[ "description" ] = description
        if due_on is not None:
            post_parameters[ "due_on" ] = due_on
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/milestones",
            None,
            post_parameters
        )
        return Milestone.Milestone( self.__requester, data, lazy = True )

    def edit( self, name, description = None, homepage = None, public = None, has_issues = None, has_wiki = None, has_downloads = None ):
        post_parameters = {
            "name": name,
        }
        if description is not None:
            post_parameters[ "description" ] = description
        if homepage is not None:
            post_parameters[ "homepage" ] = homepage
        if public is not None:
            post_parameters[ "public" ] = public
        if has_issues is not None:
            post_parameters[ "has_issues" ] = has_issues
        if has_wiki is not None:
            post_parameters[ "has_wiki" ] = has_wiki
        if has_downloads is not None:
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
        return [
            Branch.Branch( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_collaborators( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/collaborators",
            None,
            None
        )
        return [
            NamedUser.NamedUser( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_comment( self, id ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/comments/" + str( id ),
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
        return [
            CommitComment.CommitComment( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_commit( self, sha ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/commits/" + str( sha ),
            None,
            None
        )
        return Commit.Commit( self.__requester, data, lazy = True )

    def get_commits( self, sha = None, path = None ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/commits",
            None,
            None
        )
        return [
            Commit.Commit( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_contributors( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/contributors",
            None,
            None
        )
        return [
            NamedUser.NamedUser( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_download( self, id ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/downloads/" + str( id ),
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
        return [
            Download.Download( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_events( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/events",
            None,
            None
        )
        return [
            Event.Event( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_forks( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/forks",
            None,
            None
        )
        return [
            Repository( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_git_blob( self, sha ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/git_blobs/" + str( sha ),
            None,
            None
        )
        return GitBlob.GitBlob( self.__requester, data, lazy = True )

    def get_git_commit( self, sha ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/git_commits/" + str( sha ),
            None,
            None
        )
        return GitCommit.GitCommit( self.__requester, data, lazy = True )

    def get_git_ref( self, ref ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/git_refs/" + str( ref ),
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
        return [
            GitRef.GitRef( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_git_tag( self, sha ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/git_tags/" + str( sha ),
            None,
            None
        )
        return GitTag.GitTag( self.__requester, data, lazy = True )

    def get_git_tree( self, sha, recursive = None ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/git_trees/" + str( sha ),
            None,
            None
        )
        return GitTree.GitTree( self.__requester, data, lazy = True )

    def get_hook( self, id ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/hooks/" + str( id ),
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
        return [
            Hook.Hook( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_issue( self, number ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/issues/" + str( number ),
            None,
            None
        )
        return Issue.Issue( self.__requester, data, lazy = True )

    def get_issues( self, milestone = None, state = None, assignee = None, mentioned = None, labels = None, sort = None, direction = None, since = None ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/issues",
            None,
            None
        )
        return [
            Issue.Issue( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_issues_event( self, id ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/issues_events/" + str( id ),
            None,
            None
        )
        return IssueEvent.IssueEvent( self.__requester, data, lazy = True )

    def get_issues_events( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/issues_events",
            None,
            None
        )
        return [
            IssueEvent.IssueEvent( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_key( self, id ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/keys/" + str( id ),
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
        return [
            RepositoryKey.RepositoryKey( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_label( self, name ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/labels/" + str( name ),
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
        return [
            Label.Label( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_languages( self ):
        pass

    def get_milestone( self, number ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/milestones/" + str( number ),
            None,
            None
        )
        return Milestone.Milestone( self.__requester, data, lazy = True )

    def get_milestones( self, state = None, sort = None, direction = None ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/milestones",
            None,
            None
        )
        return [
            Milestone.Milestone( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_network_events( self ):
        pass

    def get_pull( self, number ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/pulls/" + str( number ),
            None,
            None
        )
        return PullRequest.PullRequest( self.__requester, data, lazy = True )

    def get_pulls( self, state = None ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/pulls",
            None,
            None
        )
        return [
            PullRequest.PullRequest( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_tags( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/tags",
            None,
            None
        )
        return [
            Tag.Tag( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_teams( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/teams",
            None,
            None
        )
        return [
            Team.Team( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_watchers( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/watchers",
            None,
            None
        )
        return [
            NamedUser.NamedUser( self.__requester, element, lazy = True )
            for element in data
        ]

    def has_in_collaborators( self, collaborator ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/collaborators/" + str( collaborator.login ),
            None,
            None
        )
        return status == 204

    def remove_from_collaborators( self, collaborator ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ) + "/collaborators/" + str( collaborator.login ),
            None,
            None
        )

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
        if "clone_url" in attributes:
            self.__clone_url = attributes[ "clone_url" ]
        if "created_at" in attributes:
            self.__created_at = attributes[ "created_at" ]
        if "description" in attributes:
            self.__description = attributes[ "description" ]
        if "fork" in attributes:
            self.__fork = attributes[ "fork" ]
        if "forks" in attributes:
            self.__forks = attributes[ "forks" ]
        if "git_url" in attributes:
            self.__git_url = attributes[ "git_url" ]
        if "has_downloads" in attributes:
            self.__has_downloads = attributes[ "has_downloads" ]
        if "has_issues" in attributes:
            self.__has_issues = attributes[ "has_issues" ]
        if "has_wiki" in attributes:
            self.__has_wiki = attributes[ "has_wiki" ]
        if "homepage" in attributes:
            self.__homepage = attributes[ "homepage" ]
        if "html_url" in attributes:
            self.__html_url = attributes[ "html_url" ]
        if "id" in attributes:
            self.__id = attributes[ "id" ]
        if "language" in attributes:
            self.__language = attributes[ "language" ]
        if "master_branch" in attributes:
            self.__master_branch = attributes[ "master_branch" ]
        if "mirror_url" in attributes:
            self.__mirror_url = attributes[ "mirror_url" ]
        if "name" in attributes:
            self.__name = attributes[ "name" ]
        if "open_issues" in attributes:
            self.__open_issues = attributes[ "open_issues" ]
        if "organization" in attributes:
            self.__organization = attributes[ "organization" ]
        if "owner" in attributes:
            self.__owner = NamedUser.NamedUser( self.__requester, attributes[ "owner" ], lazy = True )
        if "parent" in attributes:
            self.__parent = Repository( self.__requester, attributes[ "parent" ], lazy = True )
        if "permissions" in attributes:
            self.__permissions = attributes[ "permissions" ]
        if "private" in attributes:
            self.__private = attributes[ "private" ]
        if "pushed_at" in attributes:
            self.__pushed_at = attributes[ "pushed_at" ]
        if "size" in attributes:
            self.__size = attributes[ "size" ]
        if "source" in attributes:
            self.__source = Repository( self.__requester, attributes[ "source" ], lazy = True )
        if "ssh_url" in attributes:
            self.__ssh_url = attributes[ "ssh_url" ]
        if "svn_url" in attributes:
            self.__svn_url = attributes[ "svn_url" ]
        if "updated_at" in attributes:
            self.__updated_at = attributes[ "updated_at" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
        if "watchers" in attributes:
            self.__watchers = attributes[ "watchers" ]
