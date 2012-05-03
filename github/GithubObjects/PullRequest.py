# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import Commit
import NamedUser
import PullRequestComment
import PullRequestFile

class PullRequest( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def additions( self ):
        if self.__additions is None:
            self.__completeIfNeeded()
        return self.__additions

    @property
    def base( self ):
        if self.__base is None:
            self.__completeIfNeeded()
        return self.__base

    @property
    def body( self ):
        if self.__body is None:
            self.__completeIfNeeded()
        return self.__body

    @property
    def changed_files( self ):
        if self.__changed_files is None:
            self.__completeIfNeeded()
        return self.__changed_files

    @property
    def closed_at( self ):
        if self.__closed_at is None:
            self.__completeIfNeeded()
        return self.__closed_at

    @property
    def comments( self ):
        if self.__comments is None:
            self.__completeIfNeeded()
        return self.__comments

    @property
    def commits( self ):
        if self.__commits is None:
            self.__completeIfNeeded()
        return self.__commits

    @property
    def created_at( self ):
        if self.__created_at is None:
            self.__completeIfNeeded()
        return self.__created_at

    @property
    def deletions( self ):
        if self.__deletions is None:
            self.__completeIfNeeded()
        return self.__deletions

    @property
    def diff_url( self ):
        if self.__diff_url is None:
            self.__completeIfNeeded()
        return self.__diff_url

    @property
    def head( self ):
        if self.__head is None:
            self.__completeIfNeeded()
        return self.__head

    @property
    def html_url( self ):
        if self.__html_url is None:
            self.__completeIfNeeded()
        return self.__html_url

    @property
    def id( self ):
        if self.__id is None:
            self.__completeIfNeeded()
        return self.__id

    @property
    def issue_url( self ):
        if self.__issue_url is None:
            self.__completeIfNeeded()
        return self.__issue_url

    @property
    def mergeable( self ):
        if self.__mergeable is None:
            self.__completeIfNeeded()
        return self.__mergeable

    @property
    def merged( self ):
        if self.__merged is None:
            self.__completeIfNeeded()
        return self.__merged

    @property
    def merged_at( self ):
        if self.__merged_at is None:
            self.__completeIfNeeded()
        return self.__merged_at

    @property
    def merged_by( self ):
        if self.__merged_by is None:
            self.__completeIfNeeded()
        return self.__merged_by

    @property
    def number( self ):
        if self.__number is None:
            self.__completeIfNeeded()
        return self.__number

    @property
    def patch_url( self ):
        if self.__patch_url is None:
            self.__completeIfNeeded()
        return self.__patch_url

    @property
    def review_comments( self ):
        if self.__review_comments is None:
            self.__completeIfNeeded()
        return self.__review_comments

    @property
    def state( self ):
        if self.__state is None:
            self.__completeIfNeeded()
        return self.__state

    @property
    def title( self ):
        if self.__title is None:
            self.__completeIfNeeded()
        return self.__title

    @property
    def updated_at( self ):
        if self.__updated_at is None:
            self.__completeIfNeeded()
        return self.__updated_at

    @property
    def url( self ):
        if self.__url is None:
            self.__completeIfNeeded()
        return self.__url

    @property
    def user( self ):
        if self.__user is None:
            self.__completeIfNeeded()
        return self.__user

    def __initAttributes( self ):
        self.__additions = None
        self.__base = None
        self.__body = None
        self.__changed_files = None
        self.__closed_at = None
        self.__comments = None
        self.__commits = None
        self.__created_at = None
        self.__deletions = None
        self.__diff_url = None
        self.__head = None
        self.__html_url = None
        self.__id = None
        self.__issue_url = None
        self.__mergeable = None
        self.__merged = None
        self.__merged_at = None
        self.__merged_by = None
        self.__number = None
        self.__patch_url = None
        self.__review_comments = None
        self.__state = None
        self.__title = None
        self.__updated_at = None
        self.__url = None
        self.__user = None

    def __completeIfNeeded( self ):
        if not self.__completed:
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

    def edit( self, title = None, body = None, state = None ):
        pass

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
            PullRequestComment.PullRequestComment( self.__github, element, lazy = True )
            for element in result
        ]

    def get_commits( self ):
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

    def get_files( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/files",
            None,
            None
        )
        return [
            PullRequestFile.PullRequestFile( self.__github, element, lazy = True )
            for element in result
        ]

    def is_merged( self ):
        pass

    def merge( self, commit_message = None ):
        pass

    def __useAttributes( self, attributes ):
        if "additions" in attributes:
            self.__additions = attributes[ "additions" ]
        if "base" in attributes:
            self.__base = attributes[ "base" ]
        if "body" in attributes:
            self.__body = attributes[ "body" ]
        if "changed_files" in attributes:
            self.__changed_files = attributes[ "changed_files" ]
        if "closed_at" in attributes:
            self.__closed_at = attributes[ "closed_at" ]
        if "comments" in attributes:
            self.__comments = attributes[ "comments" ]
        if "commits" in attributes:
            self.__commits = attributes[ "commits" ]
        if "created_at" in attributes:
            self.__created_at = attributes[ "created_at" ]
        if "deletions" in attributes:
            self.__deletions = attributes[ "deletions" ]
        if "diff_url" in attributes:
            self.__diff_url = attributes[ "diff_url" ]
        if "head" in attributes:
            self.__head = attributes[ "head" ]
        if "html_url" in attributes:
            self.__html_url = attributes[ "html_url" ]
        if "id" in attributes:
            self.__id = attributes[ "id" ]
        if "issue_url" in attributes:
            self.__issue_url = attributes[ "issue_url" ]
        if "mergeable" in attributes:
            self.__mergeable = attributes[ "mergeable" ]
        if "merged" in attributes:
            self.__merged = attributes[ "merged" ]
        if "merged_at" in attributes:
            self.__merged_at = attributes[ "merged_at" ]
        if "merged_by" in attributes:
            self.__merged_by = attributes[ "merged_by" ]
        if "number" in attributes:
            self.__number = attributes[ "number" ]
        if "patch_url" in attributes:
            self.__patch_url = attributes[ "patch_url" ]
        if "review_comments" in attributes:
            self.__review_comments = attributes[ "review_comments" ]
        if "state" in attributes:
            self.__state = attributes[ "state" ]
        if "title" in attributes:
            self.__title = attributes[ "title" ]
        if "updated_at" in attributes:
            self.__updated_at = attributes[ "updated_at" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
        if "user" in attributes:
            self.__user = attributes[ "user" ]
