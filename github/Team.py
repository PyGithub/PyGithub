# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
import PaginatedList
##########
import Repository
import NamedUser

class Team( GithubObject.GithubObject ):
    @property
    def id( self ):
        self._completeIfNotSet( self._id )
        return self._NoneIfNotSet( self._id )

    @property
    def members_count( self ):
        self._completeIfNotSet( self._members_count )
        return self._NoneIfNotSet( self._members_count )

    @property
    def name( self ):
        self._completeIfNotSet( self._name )
        return self._NoneIfNotSet( self._name )

    @property
    def permission( self ):
        self._completeIfNotSet( self._permission )
        return self._NoneIfNotSet( self._permission )

    @property
    def repos_count( self ):
        self._completeIfNotSet( self._repos_count )
        return self._NoneIfNotSet( self._repos_count )

    @property
    def url( self ):
        self._completeIfNotSet( self._url )
        return self._NoneIfNotSet( self._url )

    def add_to_members( self, member ):
        assert isinstance( member, NamedUser.NamedUser ), member
        headers, data = self._requester.requestAndCheck(
            "PUT",
            self.url + "/members/" + member._identity,
            None,
            None
        )

    def add_to_repos( self, repo ):
        assert isinstance( repo, Repository.Repository ), repo
        headers, data = self._requester.requestAndCheck(
            "PUT",
            self.url + "/repos/" + repo._identity,
            None,
            None
        )

    def delete( self ):
        headers, data = self._requester.requestAndCheck(
            "DELETE",
            self.url,
            None,
            None
        )

    def edit( self, name, permission = GithubObject.NotSet ):
        assert isinstance( name, ( str, unicode ) ), name
        assert permission is GithubObject.NotSet or isinstance( permission, ( str, unicode ) ), permission
        post_parameters = {
            "name": name,
        }
        if permission is not GithubObject.NotSet:
            post_parameters[ "permission" ] = permission
        headers, data = self._requester.requestAndCheck(
            "PATCH",
            self.url,
            None,
            post_parameters
        )
        self._useAttributes( data )

    def get_members( self ):
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/members",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self._requester,
            headers,
            data
        )

    def get_repos( self ):
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/repos",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Repository.Repository,
            self._requester,
            headers,
            data
        )

    def has_in_members( self, member ):
        assert isinstance( member, NamedUser.NamedUser ), member
        status, headers, data = self._requester.requestRaw(
            "GET",
            self.url + "/members/" + member._identity,
            None,
            None
        )
        return status == 204

    def has_in_repos( self, repo ):
        assert isinstance( repo, Repository.Repository ), repo
        status, headers, data = self._requester.requestRaw(
            "GET",
            self.url + "/repos/" + repo._identity,
            None,
            None
        )
        return status == 204

    def remove_from_members( self, member ):
        assert isinstance( member, NamedUser.NamedUser ), member
        headers, data = self._requester.requestAndCheck(
            "DELETE",
            self.url + "/members/" + member._identity,
            None,
            None
        )

    def remove_from_repos( self, repo ):
        assert isinstance( repo, Repository.Repository ), repo
        headers, data = self._requester.requestAndCheck(
            "DELETE",
            self.url + "/repos/" + repo._identity,
            None,
            None
        )

    @property
    def _identity( self ):
        return self.id

    def _initAttributes( self ):
        self._id = GithubObject.NotSet
        self._members_count = GithubObject.NotSet
        self._name = GithubObject.NotSet
        self._permission = GithubObject.NotSet
        self._repos_count = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "id" in attributes: # pragma no branch
            assert attributes[ "id" ] is None or isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "members_count" in attributes: # pragma no branch
            assert attributes[ "members_count" ] is None or isinstance( attributes[ "members_count" ], int ), attributes[ "members_count" ]
            self._members_count = attributes[ "members_count" ]
        if "name" in attributes: # pragma no branch
            assert attributes[ "name" ] is None or isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
        if "permission" in attributes: # pragma no branch
            assert attributes[ "permission" ] is None or isinstance( attributes[ "permission" ], ( str, unicode ) ), attributes[ "permission" ]
            self._permission = attributes[ "permission" ]
        if "repos_count" in attributes: # pragma no branch
            assert attributes[ "repos_count" ] is None or isinstance( attributes[ "repos_count" ], int ), attributes[ "repos_count" ]
            self._repos_count = attributes[ "repos_count" ]
        if "url" in attributes: # pragma no branch
            assert attributes[ "url" ] is None or isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
