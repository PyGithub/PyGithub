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
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

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
        self.__completed = True

    # @todo Do not generate __complete if type has no url attribute
    def __complete( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url,
            None,
            None
        )
        self.__useAttributes( result )

    def add_to_collaborators( self, collaborator ):
        pass

    def compare( self, base, head ):
        pass

    def create_download( self, name, size, description = None, content_type = None ):
        pass

    def create_git_blob( self, content, encoding ):
        pass

    def create_git_commit( self, message, tree, parents, author = None, committer = None ):
        pass

    def create_git_ref( self, ref, sha ):
        pass

    def create_git_tag( self, tag, message, object, type, tagger = None ):
        pass

    def create_git_tree( self, tree, base_tree = None ):
        pass

    def create_hook( self, name, config, events = None, active = None ):
        pass

    def create_issue( self, title, body = None, assignee = None, milestone = None, labels = None ):
        pass

    def create_key( self, title, key ):
        pass

    def create_label( self, name, color ):
        pass

    def create_milestone( self, title, state = None, description = None, due_on = None ):
        pass

    def edit( self, name, description = None, homepage = None, public = None, has_issues = None, has_wiki = None, has_downloads = None ):
        pass

    def get_branches( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/branches",
            None,
            None
        )
        return [
            Branch.Branch( self.__github, element, lazy = True )
            for element in result
        ]

    def get_collaborators( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/collaborators",
            None,
            None
        )
        return [
            NamedUser.NamedUser( self.__github, element, lazy = True )
            for element in result
        ]

    def get_comment( self, id ):
        pass

    def get_comments( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/comments",
            None,
            None
        )
        return [
            CommitComment.CommitComment( self.__github, element, lazy = True )
            for element in result
        ]

    def get_commit( self, sha ):
        pass

    def get_commits( self, sha = None, path = None ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/commits",
            None,
            None
        )
        return [
            Commit.Commit( self.__github, element, lazy = True )
            for element in result
        ]

    def get_contributors( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/contributors",
            None,
            None
        )
        return [
            NamedUser.NamedUser( self.__github, element, lazy = True )
            for element in result
        ]

    def get_download( self, id ):
        pass

    def get_downloads( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/downloads",
            None,
            None
        )
        return [
            Download.Download( self.__github, element, lazy = True )
            for element in result
        ]

    def get_events( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/events",
            None,
            None
        )
        return [
            Event.Event( self.__github, element, lazy = True )
            for element in result
        ]

    def get_forks( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/forks",
            None,
            None
        )
        return [
            Repository.Repository( self.__github, element, lazy = True )
            for element in result
        ]

    def get_git_blob( self, sha ):
        pass

    def get_git_commit( self, sha ):
        pass

    def get_git_ref( self, ref ):
        pass

    def get_git_refs( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/git_refs",
            None,
            None
        )
        return [
            GitRef.GitRef( self.__github, element, lazy = True )
            for element in result
        ]

    def get_git_tag( self, sha ):
        pass

    def get_git_tree( self, sha, recursive = None ):
        pass

    def get_hook( self, id ):
        pass

    def get_hooks( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/hooks",
            None,
            None
        )
        return [
            Hook.Hook( self.__github, element, lazy = True )
            for element in result
        ]

    def get_issue( self, number ):
        pass

    def get_issues( self, milestone = None, state = None, assignee = None, mentioned = None, labels = None, sort = None, direction = None, since = None ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/issues",
            None,
            None
        )
        return [
            Issue.Issue( self.__github, element, lazy = True )
            for element in result
        ]

    def get_issues_event( self, id ):
        pass

    def get_issues_events( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/issues_events",
            None,
            None
        )
        return [
            IssueEvent.IssueEvent( self.__github, element, lazy = True )
            for element in result
        ]

    def get_key( self, id ):
        pass

    def get_keys( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/keys",
            None,
            None
        )
        return [
            RepositoryKey.RepositoryKey( self.__github, element, lazy = True )
            for element in result
        ]

    def get_label( self, name ):
        pass

    def get_labels( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/labels",
            None,
            None
        )
        return [
            Label.Label( self.__github, element, lazy = True )
            for element in result
        ]

    def get_languages( self ):
        pass

    def get_milestone( self, number ):
        pass

    def get_milestones( self, state = None, sort = None, direction = None ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/milestones",
            None,
            None
        )
        return [
            Milestone.Milestone( self.__github, element, lazy = True )
            for element in result
        ]

    def get_network_events( self ):
        pass

    def get_pull( self, number ):
        pass

    def get_pulls( self, state = None ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/pulls",
            None,
            None
        )
        return [
            PullRequest.PullRequest( self.__github, element, lazy = True )
            for element in result
        ]

    def get_tags( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/tags",
            None,
            None
        )
        return [
            Tag.Tag( self.__github, element, lazy = True )
            for element in result
        ]

    def get_teams( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/teams",
            None,
            None
        )
        return [
            Team.Team( self.__github, element, lazy = True )
            for element in result
        ]

    def get_watchers( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/watchers",
            None,
            None
        )
        return [
            NamedUser.NamedUser( self.__github, element, lazy = True )
            for element in result
        ]

    def has_in_collaborators( self, collaborator ):
        pass

    def remove_from_collaborators( self, collaborator ):
        pass

    def __useAttributes( self, attributes ):
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
            self.__owner = attributes[ "owner" ]
        if "parent" in attributes:
            self.__parent = attributes[ "parent" ]
        if "permissions" in attributes:
            self.__permissions = attributes[ "permissions" ]
        if "private" in attributes:
            self.__private = attributes[ "private" ]
        if "pushed_at" in attributes:
            self.__pushed_at = attributes[ "pushed_at" ]
        if "size" in attributes:
            self.__size = attributes[ "size" ]
        if "source" in attributes:
            self.__source = attributes[ "source" ]
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
