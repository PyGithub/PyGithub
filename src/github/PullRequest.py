# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import Commit
import NamedUser
import PullRequestComment
import PullRequestFile

class PullRequest( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )
        self.__completed = completion != LazyCompletion
        if completion == ImmediateCompletion:
            self.__complete() # pragma: no cover

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

    def edit( self, title = DefaultValueForOptionalParameters, body = DefaultValueForOptionalParameters, state = DefaultValueForOptionalParameters ):
        post_parameters = {
        }
        if title is not DefaultValueForOptionalParameters:
            post_parameters[ "title" ] = title
        if body is not DefaultValueForOptionalParameters:
            post_parameters[ "body" ] = body
        if state is not DefaultValueForOptionalParameters:
            post_parameters[ "state" ] = state
        status, headers, data = self.__requester.request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self.__useAttributes( data )

    def get_comment( self, id ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/comments" + "/" + str( id ),
            None,
            None
        )
        return PullRequestComment.PullRequestComment( self.__requester, data, completion = NoCompletion )

    def get_comments( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/comments",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            PullRequestComment.PullRequestComment,
            self.__requester,
            headers,
            data
        )

    def get_commits( self ):
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

    def get_files( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/files",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            PullRequestFile.PullRequestFile,
            self.__requester,
            headers,
            data
        )

    def is_merged( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/merge",
            None,
            None
        )
        return status == 204

    def merge( self, commit_message = DefaultValueForOptionalParameters ):
        status, headers, data = self.__requester.request(
            "PUT",
            str( self.url ) + "/merge",
            None,
            None
        )

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
            self.__complete() # pragma: no cover

    def __complete( self ): # pragma: no cover
        status, headers, data = self.__requester.request(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( data )
        self.__completed = True

    def __useAttributes( self, attributes ):
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "additions", "base", "body", "changed_files", "closed_at", "comments", "commits", "created_at", "deletions", "diff_url", "head", "html_url", "id", "issue_url", "mergeable", "merged", "merged_at", "merged_by", "number", "patch_url", "review_comments", "state", "title", "updated_at", "url", "user", ], attribute
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "additions" in attributes and attributes[ "additions" ] is not None:
            self.__additions = attributes[ "additions" ]
        if "base" in attributes and attributes[ "base" ] is not None:
            self.__base = attributes[ "base" ]
        if "body" in attributes and attributes[ "body" ] is not None:
            self.__body = attributes[ "body" ]
        if "changed_files" in attributes and attributes[ "changed_files" ] is not None:
            self.__changed_files = attributes[ "changed_files" ]
        if "closed_at" in attributes and attributes[ "closed_at" ] is not None:
            self.__closed_at = attributes[ "closed_at" ]
        if "comments" in attributes and attributes[ "comments" ] is not None:
            self.__comments = attributes[ "comments" ]
        if "commits" in attributes and attributes[ "commits" ] is not None:
            self.__commits = attributes[ "commits" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None:
            self.__created_at = attributes[ "created_at" ]
        if "deletions" in attributes and attributes[ "deletions" ] is not None:
            self.__deletions = attributes[ "deletions" ]
        if "diff_url" in attributes and attributes[ "diff_url" ] is not None:
            self.__diff_url = attributes[ "diff_url" ]
        if "head" in attributes and attributes[ "head" ] is not None:
            self.__head = attributes[ "head" ]
        if "html_url" in attributes and attributes[ "html_url" ] is not None:
            self.__html_url = attributes[ "html_url" ]
        if "id" in attributes and attributes[ "id" ] is not None:
            self.__id = attributes[ "id" ]
        if "issue_url" in attributes and attributes[ "issue_url" ] is not None:
            self.__issue_url = attributes[ "issue_url" ]
        if "mergeable" in attributes and attributes[ "mergeable" ] is not None:
            self.__mergeable = attributes[ "mergeable" ]
        if "merged" in attributes and attributes[ "merged" ] is not None:
            self.__merged = attributes[ "merged" ]
        if "merged_at" in attributes and attributes[ "merged_at" ] is not None:
            self.__merged_at = attributes[ "merged_at" ]
        if "merged_by" in attributes and attributes[ "merged_by" ] is not None:
            self.__merged_by = attributes[ "merged_by" ]
        if "number" in attributes and attributes[ "number" ] is not None:
            self.__number = attributes[ "number" ]
        if "patch_url" in attributes and attributes[ "patch_url" ] is not None:
            self.__patch_url = attributes[ "patch_url" ]
        if "review_comments" in attributes and attributes[ "review_comments" ] is not None:
            self.__review_comments = attributes[ "review_comments" ]
        if "state" in attributes and attributes[ "state" ] is not None:
            self.__state = attributes[ "state" ]
        if "title" in attributes and attributes[ "title" ] is not None:
            self.__title = attributes[ "title" ]
        if "updated_at" in attributes and attributes[ "updated_at" ] is not None:
            self.__updated_at = attributes[ "updated_at" ]
        if "url" in attributes and attributes[ "url" ] is not None:
            self.__url = attributes[ "url" ]
        if "user" in attributes and attributes[ "user" ] is not None:
            assert isinstance( attributes[ "user" ], dict )
            self.__user = NamedUser.NamedUser( self.__requester, attributes[ "user" ], completion = LazyCompletion )
