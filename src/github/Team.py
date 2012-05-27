# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import Repository
import NamedUser

class Team( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )
        self.__completed = completion != LazyCompletion
        if completion == ImmediateCompletion:
            self.__complete() # pragma: no cover

    @property
    def id( self ):
        self.__completeIfNeeded( self.__id )
        return self.__id

    @property
    def members_count( self ):
        self.__completeIfNeeded( self.__members_count )
        return self.__members_count

    @property
    def name( self ):
        self.__completeIfNeeded( self.__name )
        return self.__name

    @property
    def permission( self ):
        self.__completeIfNeeded( self.__permission )
        return self.__permission

    @property
    def repos_count( self ):
        self.__completeIfNeeded( self.__repos_count )
        return self.__repos_count

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def add_to_members( self, member ):
        status, headers, data = self.__requester.request(
            "PUT",
            str( self.url ) + "/members" + "/" + str( member._identity ),
            None,
            None
        )

    def add_to_repos( self, repo ):
        status, headers, data = self.__requester.request(
            "PUT",
            str( self.url ) + "/repos" + "/" + str( repo._identity ),
            None,
            None
        )

    def delete( self ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ),
            None,
            None
        )

    def edit( self, name, permission = DefaultValueForOptionalParameters ):
        post_parameters = {
            "name": name,
        }
        if permission is not DefaultValueForOptionalParameters:
            post_parameters[ "permission" ] = permission
        status, headers, data = self.__requester.request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self.__useAttributes( data )

    def get_members( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/members",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self.__requester,
            headers,
            data
        )

    def get_repos( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/repos",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Repository.Repository,
            self.__requester,
            headers,
            data
        )

    def has_in_members( self, member ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/members" + "/" + str( member._identity ),
            None,
            None
        )
        return status == 204

    def has_in_repos( self, repo ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/repos" + "/" + str( repo._identity ),
            None,
            None
        )
        return status == 204

    def remove_from_members( self, member ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ) + "/members" + "/" + str( member._identity ),
            None,
            None
        )

    def remove_from_repos( self, repo ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ) + "/repos" + "/" + str( repo._identity ),
            None,
            None
        )

    def __initAttributes( self ):
        self.__id = None
        self.__members_count = None
        self.__name = None
        self.__permission = None
        self.__repos_count = None
        self.__url = None

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
            assert attribute in [ "id", "members_count", "name", "permission", "repos_count", "url", ], attribute
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            self.__id = attributes[ "id" ]
        if "members_count" in attributes and attributes[ "members_count" ] is not None: # pragma no branch
            self.__members_count = attributes[ "members_count" ]
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            self.__name = attributes[ "name" ]
        if "permission" in attributes and attributes[ "permission" ] is not None: # pragma no branch
            self.__permission = attributes[ "permission" ]
        if "repos_count" in attributes and attributes[ "repos_count" ] is not None: # pragma no branch
            self.__repos_count = attributes[ "repos_count" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            self.__url = attributes[ "url" ]
