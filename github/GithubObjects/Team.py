# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import Repository
import NamedUser

class Team( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

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

    def add_to_members( self, member ):
        pass

    def add_to_repos( self, repo ):
        pass

    def delete( self ):
        pass

    def edit( self, name, permission = None ):
        pass

    def get_members( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/members",
            None,
            None
        )
        return [
            NamedUser.NamedUser( self.__github, element, lazy = True )
            for element in result
        ]

    def get_repos( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/repos",
            None,
            None
        )
        return [
            Repository.Repository( self.__github, element, lazy = True )
            for element in result
        ]

    def has_in_members( self, member ):
        pass

    def has_in_repos( self, repo ):
        pass

    def remove_from_members( self, member ):
        pass

    def remove_from_repos( self, repo ):
        pass

    def __useAttributes( self, attributes ):
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
