# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
import PaginatedList
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters
##########
import Commit
import NamedUser
import PullRequestMergeStatus
import PullRequestComment
import PullRequestFile

class PullRequest( GithubObject.GithubObject ):
    @property
    def additions( self ):
        self._completeIfNeeded( self._additions )
        return self._additions

    @property
    def base( self ):
        self._completeIfNeeded( self._base )
        return self._base

    @property
    def body( self ):
        self._completeIfNeeded( self._body )
        return self._body

    @property
    def changed_files( self ):
        self._completeIfNeeded( self._changed_files )
        return self._changed_files

    @property
    def closed_at( self ):
        self._completeIfNeeded( self._closed_at )
        return self._closed_at

    @property
    def comments( self ):
        self._completeIfNeeded( self._comments )
        return self._comments

    @property
    def commits( self ):
        self._completeIfNeeded( self._commits )
        return self._commits

    @property
    def created_at( self ):
        self._completeIfNeeded( self._created_at )
        return self._created_at

    @property
    def deletions( self ):
        self._completeIfNeeded( self._deletions )
        return self._deletions

    @property
    def diff_url( self ):
        self._completeIfNeeded( self._diff_url )
        return self._diff_url

    @property
    def head( self ):
        self._completeIfNeeded( self._head )
        return self._head

    @property
    def html_url( self ):
        self._completeIfNeeded( self._html_url )
        return self._html_url

    @property
    def id( self ):
        self._completeIfNeeded( self._id )
        return self._id

    @property
    def issue_url( self ):
        self._completeIfNeeded( self._issue_url )
        return self._issue_url

    @property
    def mergeable( self ):
        self._completeIfNeeded( self._mergeable )
        return self._mergeable

    @property
    def merged( self ):
        self._completeIfNeeded( self._merged )
        return self._merged

    @property
    def merged_at( self ):
        self._completeIfNeeded( self._merged_at )
        return self._merged_at

    @property
    def merged_by( self ):
        self._completeIfNeeded( self._merged_by )
        return self._merged_by

    @property
    def number( self ):
        self._completeIfNeeded( self._number )
        return self._number

    @property
    def patch_url( self ):
        self._completeIfNeeded( self._patch_url )
        return self._patch_url

    @property
    def review_comments( self ):
        self._completeIfNeeded( self._review_comments )
        return self._review_comments

    @property
    def state( self ):
        self._completeIfNeeded( self._state )
        return self._state

    @property
    def title( self ):
        self._completeIfNeeded( self._title )
        return self._title

    @property
    def updated_at( self ):
        self._completeIfNeeded( self._updated_at )
        return self._updated_at

    @property
    def url( self ):
        self._completeIfNeeded( self._url )
        return self._url

    @property
    def user( self ):
        self._completeIfNeeded( self._user )
        return self._user

    def create_comment( self, body, commit_id, path, position ):
        assert isinstance( body, ( str, unicode ) ), body
        assert isinstance( commit_id, ( str, unicode ) ), commit_id
        assert isinstance( path, ( str, unicode ) ), path
        assert isinstance( position, int ), position
        post_parameters = {
            "body": body,
            "commit_id": commit_id,
            "path": path,
            "position": position,
        }
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/comments",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return PullRequestComment.PullRequestComment( self._requester, data, completed = True )

    def edit( self, title = DefaultValueForOptionalParameters, body = DefaultValueForOptionalParameters, state = DefaultValueForOptionalParameters ):
        if title is not DefaultValueForOptionalParameters:
            assert isinstance( title, ( str, unicode ) ), title
        if body is not DefaultValueForOptionalParameters:
            assert isinstance( body, ( str, unicode ) ), body
        if state is not DefaultValueForOptionalParameters:
            assert isinstance( state, ( str, unicode ) ), state
        post_parameters = dict()
        if title is not DefaultValueForOptionalParameters:
            post_parameters[ "title" ] = title
        if body is not DefaultValueForOptionalParameters:
            post_parameters[ "body" ] = body
        if state is not DefaultValueForOptionalParameters:
            post_parameters[ "state" ] = state
        status, headers, data = self._request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        self._useAttributes( data )

    def get_comment( self, id ):
        assert isinstance( id, int ), id
        status, headers, data = self._request(
            "GET",
            self._parentUrl( str( self.url ) ) + "/comments/" + str( id ),
            None,
            None
        )
        self._checkStatus( status, data )
        return PullRequestComment.PullRequestComment( self._requester, data, completed = True )

    def get_comments( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/comments",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            PullRequestComment.PullRequestComment,
            self._requester,
            headers,
            data
        )

    def get_commits( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/commits",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Commit.Commit,
            self._requester,
            headers,
            data
        )

    def get_files( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/files",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            PullRequestFile.PullRequestFile,
            self._requester,
            headers,
            data
        )

    def is_merged( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/merge",
            None,
            None
        )
        return status == 204

    def merge( self, commit_message = DefaultValueForOptionalParameters ):
        if commit_message is not DefaultValueForOptionalParameters:
            assert isinstance( commit_message, ( str, unicode ) ), commit_message
        post_parameters = dict()
        if commit_message is not DefaultValueForOptionalParameters:
            post_parameters[ "commit_message" ] = commit_message
        status, headers, data = self._request(
            "PUT",
            str( self.url ) + "/merge",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return PullRequestMergeStatus.PullRequestMergeStatus( self._requester, data, completed = True )

    def _initAttributes( self ):
        self._additions = None
        self._base = None
        self._body = None
        self._changed_files = None
        self._closed_at = None
        self._comments = None
        self._commits = None
        self._created_at = None
        self._deletions = None
        self._diff_url = None
        self._head = None
        self._html_url = None
        self._id = None
        self._issue_url = None
        self._mergeable = None
        self._merged = None
        self._merged_at = None
        self._merged_by = None
        self._number = None
        self._patch_url = None
        self._review_comments = None
        self._state = None
        self._title = None
        self._updated_at = None
        self._url = None
        self._user = None

    def _useAttributes( self, attributes ):
        if "additions" in attributes and attributes[ "additions" ] is not None: # pragma no branch
            assert isinstance( attributes[ "additions" ], int ), attributes[ "additions" ]
            self._additions = attributes[ "additions" ]
        if "base" in attributes and attributes[ "base" ] is not None: # pragma no branch
            self._base = attributes[ "base" ]
        if "body" in attributes and attributes[ "body" ] is not None: # pragma no branch
            assert isinstance( attributes[ "body" ], ( str, unicode ) ), attributes[ "body" ]
            self._body = attributes[ "body" ]
        if "changed_files" in attributes and attributes[ "changed_files" ] is not None: # pragma no branch
            assert isinstance( attributes[ "changed_files" ], int ), attributes[ "changed_files" ]
            self._changed_files = attributes[ "changed_files" ]
        if "closed_at" in attributes and attributes[ "closed_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "closed_at" ], ( str, unicode ) ), attributes[ "closed_at" ]
            self._closed_at = attributes[ "closed_at" ]
        if "comments" in attributes and attributes[ "comments" ] is not None: # pragma no branch
            assert isinstance( attributes[ "comments" ], int ), attributes[ "comments" ]
            self._comments = attributes[ "comments" ]
        if "commits" in attributes and attributes[ "commits" ] is not None: # pragma no branch
            assert isinstance( attributes[ "commits" ], int ), attributes[ "commits" ]
            self._commits = attributes[ "commits" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self._created_at = attributes[ "created_at" ]
        if "deletions" in attributes and attributes[ "deletions" ] is not None: # pragma no branch
            assert isinstance( attributes[ "deletions" ], int ), attributes[ "deletions" ]
            self._deletions = attributes[ "deletions" ]
        if "diff_url" in attributes and attributes[ "diff_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "diff_url" ], ( str, unicode ) ), attributes[ "diff_url" ]
            self._diff_url = attributes[ "diff_url" ]
        if "head" in attributes and attributes[ "head" ] is not None: # pragma no branch
            self._head = attributes[ "head" ]
        if "html_url" in attributes and attributes[ "html_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "html_url" ], ( str, unicode ) ), attributes[ "html_url" ]
            self._html_url = attributes[ "html_url" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "issue_url" in attributes and attributes[ "issue_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "issue_url" ], ( str, unicode ) ), attributes[ "issue_url" ]
            self._issue_url = attributes[ "issue_url" ]
        if "mergeable" in attributes and attributes[ "mergeable" ] is not None: # pragma no branch
            assert isinstance( attributes[ "mergeable" ], bool ), attributes[ "mergeable" ]
            self._mergeable = attributes[ "mergeable" ]
        if "merged" in attributes and attributes[ "merged" ] is not None: # pragma no branch
            assert isinstance( attributes[ "merged" ], bool ), attributes[ "merged" ]
            self._merged = attributes[ "merged" ]
        if "merged_at" in attributes and attributes[ "merged_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "merged_at" ], ( str, unicode ) ), attributes[ "merged_at" ]
            self._merged_at = attributes[ "merged_at" ]
        if "merged_by" in attributes and attributes[ "merged_by" ] is not None: # pragma no branch
            assert isinstance( attributes[ "merged_by" ], dict ), attributes[ "merged_by" ]
            self._merged_by = NamedUser.NamedUser( self._requester, attributes[ "merged_by" ], completed = False )
        if "number" in attributes and attributes[ "number" ] is not None: # pragma no branch
            assert isinstance( attributes[ "number" ], int ), attributes[ "number" ]
            self._number = attributes[ "number" ]
        if "patch_url" in attributes and attributes[ "patch_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "patch_url" ], ( str, unicode ) ), attributes[ "patch_url" ]
            self._patch_url = attributes[ "patch_url" ]
        if "review_comments" in attributes and attributes[ "review_comments" ] is not None: # pragma no branch
            assert isinstance( attributes[ "review_comments" ], int ), attributes[ "review_comments" ]
            self._review_comments = attributes[ "review_comments" ]
        if "state" in attributes and attributes[ "state" ] is not None: # pragma no branch
            assert isinstance( attributes[ "state" ], ( str, unicode ) ), attributes[ "state" ]
            self._state = attributes[ "state" ]
        if "title" in attributes and attributes[ "title" ] is not None: # pragma no branch
            assert isinstance( attributes[ "title" ], ( str, unicode ) ), attributes[ "title" ]
            self._title = attributes[ "title" ]
        if "updated_at" in attributes and attributes[ "updated_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "updated_at" ], ( str, unicode ) ), attributes[ "updated_at" ]
            self._updated_at = attributes[ "updated_at" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
        if "user" in attributes and attributes[ "user" ] is not None: # pragma no branch
            assert isinstance( attributes[ "user" ], dict ), attributes[ "user" ]
            self._user = NamedUser.NamedUser( self._requester, attributes[ "user" ], completed = False )
