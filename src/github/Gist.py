# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
import PaginatedList
##########
import NamedUser
import GistHistoryState
import GistFile
import Gist
import GistComment

class Gist( GithubObject.GithubObject ):
    @property
    def comments( self ):
        self._completeIfNotSet( self._comments )
        return self._NoneIfNotSet( self._comments )

    @property
    def created_at( self ):
        self._completeIfNotSet( self._created_at )
        return self._NoneIfNotSet( self._created_at )

    @property
    def description( self ):
        self._completeIfNotSet( self._description )
        return self._NoneIfNotSet( self._description )

    @property
    def files( self ):
        self._completeIfNotSet( self._files )
        return self._NoneIfNotSet( self._files )

    @property
    def fork_of( self ):
        self._completeIfNotSet( self._fork_of )
        return self._NoneIfNotSet( self._fork_of )

    @property
    def forks( self ):
        self._completeIfNotSet( self._forks )
        return self._NoneIfNotSet( self._forks )

    @property
    def git_pull_url( self ):
        self._completeIfNotSet( self._git_pull_url )
        return self._NoneIfNotSet( self._git_pull_url )

    @property
    def git_push_url( self ):
        self._completeIfNotSet( self._git_push_url )
        return self._NoneIfNotSet( self._git_push_url )

    @property
    def history( self ):
        self._completeIfNotSet( self._history )
        return self._NoneIfNotSet( self._history )

    @property
    def html_url( self ):
        self._completeIfNotSet( self._html_url )
        return self._NoneIfNotSet( self._html_url )

    @property
    def id( self ):
        self._completeIfNotSet( self._id )
        return self._NoneIfNotSet( self._id )

    @property
    def public( self ):
        self._completeIfNotSet( self._public )
        return self._NoneIfNotSet( self._public )

    @property
    def updated_at( self ):
        self._completeIfNotSet( self._updated_at )
        return self._NoneIfNotSet( self._updated_at )

    @property
    def url( self ):
        self._completeIfNotSet( self._url )
        return self._NoneIfNotSet( self._url )

    @property
    def user( self ):
        self._completeIfNotSet( self._user )
        return self._NoneIfNotSet( self._user )

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

    def edit( self, description = GithubObject.NotSet, files = GithubObject.NotSet ):
        assert description is GithubObject.NotSet or isinstance( description, ( str, unicode ) ), description
        post_parameters = dict()
        if description is not GithubObject.NotSet:
            post_parameters[ "description" ] = description
        if files is not GithubObject.NotSet:
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
        self._comments = GithubObject.NotSet
        self._created_at = GithubObject.NotSet
        self._description = GithubObject.NotSet
        self._files = GithubObject.NotSet
        self._fork_of = GithubObject.NotSet
        self._forks = GithubObject.NotSet
        self._git_pull_url = GithubObject.NotSet
        self._git_push_url = GithubObject.NotSet
        self._history = GithubObject.NotSet
        self._html_url = GithubObject.NotSet
        self._id = GithubObject.NotSet
        self._public = GithubObject.NotSet
        self._updated_at = GithubObject.NotSet
        self._url = GithubObject.NotSet
        self._user = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "comments" in attributes: # pragma no branch
            assert attributes[ "comments" ] is None or isinstance( attributes[ "comments" ], int ), attributes[ "comments" ]
            self._comments = attributes[ "comments" ]
        if "created_at" in attributes: # pragma no branch
            assert attributes[ "created_at" ] is None or isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self._created_at = attributes[ "created_at" ]
        if "description" in attributes: # pragma no branch
            assert attributes[ "description" ] is None or isinstance( attributes[ "description" ], ( str, unicode ) ), attributes[ "description" ]
            self._description = attributes[ "description" ]
        if "files" in attributes: # pragma no branch
            assert attributes[ "files" ] is None or all( isinstance( element, dict ) for element in attributes[ "files" ].itervalues() ), attributes[ "files" ]
            self._files = None if attributes[ "files" ] is None else {
                key : GistFile.GistFile( self._requester, element, completed = False )
                for key, element in attributes[ "files" ].iteritems()
            }
        if "fork_of" in attributes: # pragma no branch
            assert attributes[ "fork_of" ] is None or isinstance( attributes[ "fork_of" ], dict ), attributes[ "fork_of" ]
            self._fork_of = None if attributes[ "fork_of" ] is None else Gist( self._requester, attributes[ "fork_of" ], completed = False )
        if "forks" in attributes: # pragma no branch
            assert attributes[ "forks" ] is None or all( isinstance( element, dict ) for element in attributes[ "forks" ] ), attributes[ "forks" ]
            self._forks = None if attributes[ "forks" ] is None else [
                Gist( self._requester, element, completed = False )
                for element in attributes[ "forks" ]
            ]
        if "git_pull_url" in attributes: # pragma no branch
            assert attributes[ "git_pull_url" ] is None or isinstance( attributes[ "git_pull_url" ], ( str, unicode ) ), attributes[ "git_pull_url" ]
            self._git_pull_url = attributes[ "git_pull_url" ]
        if "git_push_url" in attributes: # pragma no branch
            assert attributes[ "git_push_url" ] is None or isinstance( attributes[ "git_push_url" ], ( str, unicode ) ), attributes[ "git_push_url" ]
            self._git_push_url = attributes[ "git_push_url" ]
        if "history" in attributes: # pragma no branch
            assert attributes[ "history" ] is None or all( isinstance( element, dict ) for element in attributes[ "history" ] ), attributes[ "history" ]
            self._history = None if attributes[ "history" ] is None else [
                GistHistoryState.GistHistoryState( self._requester, element, completed = False )
                for element in attributes[ "history" ]
            ]
        if "html_url" in attributes: # pragma no branch
            assert attributes[ "html_url" ] is None or isinstance( attributes[ "html_url" ], ( str, unicode ) ), attributes[ "html_url" ]
            self._html_url = attributes[ "html_url" ]
        if "id" in attributes: # pragma no branch
            assert attributes[ "id" ] is None or isinstance( attributes[ "id" ], ( str, unicode ) ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "public" in attributes: # pragma no branch
            assert attributes[ "public" ] is None or isinstance( attributes[ "public" ], bool ), attributes[ "public" ]
            self._public = attributes[ "public" ]
        if "updated_at" in attributes: # pragma no branch
            assert attributes[ "updated_at" ] is None or isinstance( attributes[ "updated_at" ], ( str, unicode ) ), attributes[ "updated_at" ]
            self._updated_at = attributes[ "updated_at" ]
        if "url" in attributes: # pragma no branch
            assert attributes[ "url" ] is None or isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
        if "user" in attributes: # pragma no branch
            assert attributes[ "user" ] is None or isinstance( attributes[ "user" ], dict ), attributes[ "user" ]
            self._user = None if attributes[ "user" ] is None else NamedUser.NamedUser( self._requester, attributes[ "user" ], completed = False )
