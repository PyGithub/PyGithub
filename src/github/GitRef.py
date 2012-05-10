# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
# This allows None as a valid value for an optional parameter

class DefaultValueForOptionalParametersType:
    pass
DefaultValueForOptionalParameters = DefaultValueForOptionalParametersType()

class GitRef( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def object( self ):
        self.__completeIfNeeded( self.__object )
        return self.__object

    @property
    def ref( self ):
        self.__completeIfNeeded( self.__ref )
        return self.__ref

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def delete( self ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ),
            None,
            None
        )

    def edit( self, sha, force = DefaultValueForOptionalParameters ):
        post_parameters = {
            "sha": sha,
        }
        if force is not DefaultValueForOptionalParameters:
            post_parameters[ "force" ] = force
        status, headers, data = self.__requester.request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self.__useAttributes( data )

    def __initAttributes( self ):
        self.__object = None
        self.__ref = None
        self.__url = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete()

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
        if "object" in attributes and attributes[ "object" ] is not None:
            self.__object = attributes[ "object" ]
        if "ref" in attributes and attributes[ "ref" ] is not None:
            assert isinstance( attributes[ "ref" ], ( str, unicode ) )
            self.__ref = attributes[ "ref" ]
        if "url" in attributes and attributes[ "url" ] is not None:
            self.__url = attributes[ "url" ]
