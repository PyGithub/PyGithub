# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
# This allows None as a valid value for an optional parameter

class DefaultValueForOptionalParametersType:
    pass
DefaultValueForOptionalParameters = DefaultValueForOptionalParametersType()

class UserKey( object ):
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
    def key( self ):
        self.__completeIfNeeded( self.__key )
        return self.__key

    @property
    def title( self ):
        self.__completeIfNeeded( self.__title )
        return self.__title

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

    def edit( self, title = DefaultValueForOptionalParameters, key = DefaultValueForOptionalParameters ):
        post_parameters = {
        }
        if title is not DefaultValueForOptionalParameters:
            post_parameters[ "title" ] = title
        if key is not DefaultValueForOptionalParameters:
            post_parameters[ "key" ] = key
        status, headers, data = self.__requester.request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self.__useAttributes( data )

    def __initAttributes( self ):
        self.__id = None
        self.__key = None
        self.__title = None
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
        if "id" in attributes and attributes[ "id" ] is not None:
            self.__id = attributes[ "id" ]
        if "key" in attributes and attributes[ "key" ] is not None:
            self.__key = attributes[ "key" ]
        if "title" in attributes and attributes[ "title" ] is not None:
            self.__title = attributes[ "title" ]
        if "url" in attributes and attributes[ "url" ] is not None:
            self.__url = attributes[ "url" ]
