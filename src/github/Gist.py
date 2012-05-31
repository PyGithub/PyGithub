# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
import PaginatedList
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters
##########
import GistHistoryState
import NamedUser
import Gist
import GistComment

class Gist( GithubObject.GithubObject ):
    @property
    def comments( self ):
        self._completeIfNeeded( self._comments )
        return self._comments

    @property
    def created_at( self ):
        self._completeIfNeeded( self._created_at )
        return self._created_at

    @property
    def description( self ):
        self._completeIfNeeded( self._description )
        return self._description

    @property
    def files( self ):
        self._completeIfNeeded( self._files )
        return self._files

    @property
    def fork_of( self ):
        self._completeIfNeeded( self._fork_of )
        return self._fork_of

    @property
    def forks( self ):
        self._completeIfNeeded( self._forks )
        return self._forks

    @property
    def git_pull_url( self ):
        self._completeIfNeeded( self._git_pull_url )
        return self._git_pull_url

    @property
    def git_push_url( self ):
        self._completeIfNeeded( self._git_push_url )
        return self._git_push_url

    @property
    def history( self ):
        self._completeIfNeeded( self._history )
        return self._history

    @property
    def html_url( self ):
        self._completeIfNeeded( self._html_url )
        return self._html_url

    @property
    def id( self ):
        self._completeIfNeeded( self._id )
        return self._id

    @property
    def public( self ):
        self._completeIfNeeded( self._public )
        return self._public

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

    def create_comment( self, body ):
        assert isinstance( body, ( str, unicode ) ), body
        post_parameters = {
            "body": body,
        }
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/comments",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return GistComment.GistComment( self._requester, data, completed = True )

    def create_fork( self ):
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/fork",
            None,
            None
        )
        self._checkStatus( status, data )
        return Gist( self._requester, data, completed = True )

    def delete( self ):
        status, headers, data = self._request(
            "DELETE",
            str( self.url ),
            None,
            None
        )
        self._checkStatus( status, data )

    def edit( self, description = DefaultValueForOptionalParameters, files = DefaultValueForOptionalParameters ):
        if description is not DefaultValueForOptionalParameters:
            assert isinstance( description, ( str, unicode ) ), description
        post_parameters = dict()
        if description is not DefaultValueForOptionalParameters:
            post_parameters[ "description" ] = description
        if files is not DefaultValueForOptionalParameters:
            post_parameters[ "files" ] = files
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
            "https://api.github.com/gists/comments/" + str( id ),
            None,
            None
        )
        self._checkStatus( status, data )
        return GistComment.GistComment( self._requester, data, completed = True )

    def get_comments( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/comments",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            GistComment.GistComment,
            self._requester,
            headers,
            data
        )

    def is_starred( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/star",
            None,
            None
        )
        return status == 204

    def reset_starred( self ):
        status, headers, data = self._request(
            "DELETE",
            str( self.url ) + "/star",
            None,
            None
        )
        self._checkStatus( status, data )

    def set_starred( self ):
        status, headers, data = self._request(
            "PUT",
            str( self.url ) + "/star",
            None,
            None
        )
        self._checkStatus( status, data )

    def _initAttributes( self ):
        self._comments = None
        self._created_at = None
        self._description = None
        self._files = None
        self._fork_of = None
        self._forks = None
        self._git_pull_url = None
        self._git_push_url = None
        self._history = None
        self._html_url = None
        self._id = None
        self._public = None
        self._updated_at = None
        self._url = None
        self._user = None

    def _useAttributes( self, attributes ):
        if "comments" in attributes and attributes[ "comments" ] is not None: # pragma no branch
            assert isinstance( attributes[ "comments" ], int ), attributes[ "comments" ]
            self._comments = attributes[ "comments" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self._created_at = attributes[ "created_at" ]
        if "description" in attributes and attributes[ "description" ] is not None: # pragma no branch
            assert isinstance( attributes[ "description" ], ( str, unicode ) ), attributes[ "description" ]
            self._description = attributes[ "description" ]
        if "files" in attributes and attributes[ "files" ] is not None: # pragma no branch
            self._files = attributes[ "files" ]
        if "fork_of" in attributes and attributes[ "fork_of" ] is not None: # pragma no branch
            assert isinstance( attributes[ "fork_of" ], dict ), attributes[ "fork_of" ]
            self._fork_of = Gist( self._requester, attributes[ "fork_of" ], completed = False )
        if "forks" in attributes and attributes[ "forks" ] is not None: # pragma no branch
            assert all( isinstance( element, dict ) for element in attributes[ "forks" ] ), attributes[ "forks" ]
            self._forks = [
                Gist( self._requester, element, completed = False )
                for element in attributes[ "forks" ]
            ]
        if "git_pull_url" in attributes and attributes[ "git_pull_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "git_pull_url" ], ( str, unicode ) ), attributes[ "git_pull_url" ]
            self._git_pull_url = attributes[ "git_pull_url" ]
        if "git_push_url" in attributes and attributes[ "git_push_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "git_push_url" ], ( str, unicode ) ), attributes[ "git_push_url" ]
            self._git_push_url = attributes[ "git_push_url" ]
        if "history" in attributes and attributes[ "history" ] is not None: # pragma no branch
            assert all( isinstance( element, dict ) for element in attributes[ "history" ] ), attributes[ "history" ]
            self._history = [
                GistHistoryState.GistHistoryState( self._requester, element, completed = False )
                for element in attributes[ "history" ]
            ]
        if "html_url" in attributes and attributes[ "html_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "html_url" ], ( str, unicode ) ), attributes[ "html_url" ]
            self._html_url = attributes[ "html_url" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], ( str, unicode ) ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "public" in attributes and attributes[ "public" ] is not None: # pragma no branch
            assert isinstance( attributes[ "public" ], bool ), attributes[ "public" ]
            self._public = attributes[ "public" ]
        if "updated_at" in attributes and attributes[ "updated_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "updated_at" ], ( str, unicode ) ), attributes[ "updated_at" ]
            self._updated_at = attributes[ "updated_at" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
        if "user" in attributes and attributes[ "user" ] is not None: # pragma no branch
            assert isinstance( attributes[ "user" ], dict ), attributes[ "user" ]
            self._user = NamedUser.NamedUser( self._requester, attributes[ "user" ], completed = False )
