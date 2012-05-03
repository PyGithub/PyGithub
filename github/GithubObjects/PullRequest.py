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
        if not lazy:
            self.__complete()

    @property
    def additions( self ):
        self.__completeIfNeeded( self.__additions )
        return self.__additions

    @property
    def base( self ):
        self.__completeIfNeeded( self.__base )
        return self.__base

    @property
    def body( self ):
        self.__completeIfNeeded( self.__body )
        return self.__body

    @property
    def changed_files( self ):
        self.__completeIfNeeded( self.__changed_files )
        return self.__changed_files

    @property
    def closed_at( self ):
        self.__completeIfNeeded( self.__closed_at )
        return self.__closed_at

    @property
    def comments( self ):
        self.__completeIfNeeded( self.__comments )
        return self.__comments

    @property
    def commits( self ):
        self.__completeIfNeeded( self.__commits )
        return self.__commits

    @property
    def created_at( self ):
        self.__completeIfNeeded( self.__created_at )
        return self.__created_at

    @property
    def deletions( self ):
        self.__completeIfNeeded( self.__deletions )
        return self.__deletions

    @property
    def diff_url( self ):
        self.__completeIfNeeded( self.__diff_url )
        return self.__diff_url

    @property
    def head( self ):
        self.__completeIfNeeded( self.__head )
        return self.__head

    @property
    def html_url( self ):
        self.__completeIfNeeded( self.__html_url )
        return self.__html_url

    @property
    def id( self ):
        self.__completeIfNeeded( self.__id )
        return self.__id

    @property
    def issue_url( self ):
        self.__completeIfNeeded( self.__issue_url )
        return self.__issue_url

    @property
    def mergeable( self ):
        self.__completeIfNeeded( self.__mergeable )
        return self.__mergeable

    @property
    def merged( self ):
        self.__completeIfNeeded( self.__merged )
        return self.__merged

    @property
    def merged_at( self ):
        self.__completeIfNeeded( self.__merged_at )
        return self.__merged_at

    @property
    def merged_by( self ):
        self.__completeIfNeeded( self.__merged_by )
        return self.__merged_by

    @property
    def number( self ):
        self.__completeIfNeeded( self.__number )
        return self.__number

    @property
    def patch_url( self ):
        self.__completeIfNeeded( self.__patch_url )
        return self.__patch_url

    @property
    def review_comments( self ):
        self.__completeIfNeeded( self.__review_comments )
        return self.__review_comments

    @property
    def state( self ):
        self.__completeIfNeeded( self.__state )
        return self.__state

    @property
    def title( self ):
        self.__completeIfNeeded( self.__title )
        return self.__title

    @property
    def updated_at( self ):
        self.__completeIfNeeded( self.__updated_at )
        return self.__updated_at

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    @property
    def user( self ):
        self.__completeIfNeeded( self.__user )
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

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete()

    # @todo Do not generate __complete if type has no url attribute
    def __complete( self ):
        result = self.__github._dataRequest(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( result )
        self.__completed = True

    def edit( self, title = None, body = None, state = None ):
        post_parameters = {
        }
        if title is not None:
            post_parameters[ "title" ] = title
        if body is not None:
            post_parameters[ "body" ] = body
        if state is not None:
            post_parameters[ "state" ] = state
        result = self.__github._dataRequest(
            "PATCH",
            "https://api.github.com/user",
            None,
            post_parameters
        )
        self.__useAttributes( result )

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
