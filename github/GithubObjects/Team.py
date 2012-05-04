# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import Repository
import NamedUser
# This allows None as a valid value for an optional parameter

class DefaultValueForOptionalParametersType:
    pass
DefaultValueForOptionalParameters = DefaultValueForOptionalParametersType()

class Team( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

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
            str( self.url ) + "/members/" + str( member.login ),
            None,
            None
        )

    def add_to_repos( self, repo ):
        status, headers, data = self.__requester.request(
            "PUT",
            str( self.url ) + "/repos/" + str( repo.login ),
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
        return [
            NamedUser.NamedUser( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_repos( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/repos",
            None,
            None
        )
        return [
            Repository.Repository( self.__requester, element, lazy = True )
            for element in data
        ]

    def has_in_members( self, member ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/members/" + str( member.login ),
            None,
            None
        )
        return status == 204

    def has_in_repos( self, repo ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/repos/" + str( repo.login ),
            None,
            None
        )
        return status == 204

    def remove_from_members( self, member ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ) + "/members/" + str( member.login ),
            None,
            None
        )

    def remove_from_repos( self, repo ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ) + "/repos/" + str( repo.login ),
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
            self.__complete()

    # @todo Do not generate __complete if type has no url attribute
    def __complete( self ):
        status, headers, data = self.__requester.request(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( data )
        self.__completed = True

    def __useAttributes( self, attributes ):
         #@todo No need to check if attribute is in attributes when attribute is mandatory
        if "id" in attributes:
            self.__id = attributes[ "id" ]
        if "members_count" in attributes:
            self.__members_count = attributes[ "members_count" ]
        if "name" in attributes:
            self.__name = attributes[ "name" ]
        if "permission" in attributes:
            self.__permission = attributes[ "permission" ]
        if "repos_count" in attributes:
            self.__repos_count = attributes[ "repos_count" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
