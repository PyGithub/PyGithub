# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
import PaginatedList
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters
##########
import Repository
import NamedUser

class Team( GithubObject.GithubObject ):
    @property
    def id( self ):
        self._completeIfNeeded( self._id )
        return self._id

    @property
    def members_count( self ):
        self._completeIfNeeded( self._members_count )
        return self._members_count

    @property
    def name( self ):
        self._completeIfNeeded( self._name )
        return self._name

    @property
    def permission( self ):
        self._completeIfNeeded( self._permission )
        return self._permission

    @property
    def repos_count( self ):
        self._completeIfNeeded( self._repos_count )
        return self._repos_count

    @property
    def url( self ):
        self._completeIfNeeded( self._url )
        return self._url

    def add_to_members( self, member ):
        assert isinstance( member, NamedUser.NamedUser ), member
        status, headers, data = self._request(
            "PUT",
            str( self.url ) + "/members/" + str( member._identity ),
            None,
            None
        )
        self._checkStatus( status, data )

    def add_to_repos( self, repo ):
        assert isinstance( repo, Repository.Repository ), repo
        status, headers, data = self._request(
            "PUT",
            str( self.url ) + "/repos/" + str( repo._identity ),
            None,
            None
        )
        self._checkStatus( status, data )

    def delete( self ):
        status, headers, data = self._request(
            "DELETE",
            str( self.url ),
            None,
            None
        )
        self._checkStatus( status, data )

    def edit( self, name, permission = DefaultValueForOptionalParameters ):
        assert isinstance( name, ( str, unicode ) ), name
        if permission is not DefaultValueForOptionalParameters:
            assert isinstance( permission, ( str, unicode ) ), permission
        post_parameters = {
            "name": name,
        }
        if permission is not DefaultValueForOptionalParameters:
            post_parameters[ "permission" ] = permission
        status, headers, data = self._request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        self._useAttributes( data )

    def get_members( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/members",
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

    def get_repos( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/repos",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Repository.Repository,
            self._requester,
            headers,
            data
        )

    def has_in_members( self, member ):
        assert isinstance( member, NamedUser.NamedUser ), member
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/members/" + str( member._identity ),
            None,
            None
        )
        return status == 204

    def has_in_repos( self, repo ):
        assert isinstance( repo, Repository.Repository ), repo
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/repos/" + str( repo._identity ),
            None,
            None
        )
        return status == 204

    def remove_from_members( self, member ):
        assert isinstance( member, NamedUser.NamedUser ), member
        status, headers, data = self._request(
            "DELETE",
            str( self.url ) + "/members/" + str( member._identity ),
            None,
            None
        )
        self._checkStatus( status, data )

    def remove_from_repos( self, repo ):
        assert isinstance( repo, Repository.Repository ), repo
        status, headers, data = self._request(
            "DELETE",
            str( self.url ) + "/repos/" + str( repo._identity ),
            None,
            None
        )
        self._checkStatus( status, data )

    def _initAttributes( self ):
        self._id = None
        self._members_count = None
        self._name = None
        self._permission = None
        self._repos_count = None
        self._url = None

    def _useAttributes( self, attributes ):
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "members_count" in attributes and attributes[ "members_count" ] is not None: # pragma no branch
            assert isinstance( attributes[ "members_count" ], int ), attributes[ "members_count" ]
            self._members_count = attributes[ "members_count" ]
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
        if "permission" in attributes and attributes[ "permission" ] is not None: # pragma no branch
            assert isinstance( attributes[ "permission" ], ( str, unicode ) ), attributes[ "permission" ]
            self._permission = attributes[ "permission" ]
        if "repos_count" in attributes and attributes[ "repos_count" ] is not None: # pragma no branch
            assert isinstance( attributes[ "repos_count" ], int ), attributes[ "repos_count" ]
            self._repos_count = attributes[ "repos_count" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
