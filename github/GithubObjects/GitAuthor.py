# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
# This allows None as a valid value for an optional parameter

class DefaultValueForOptionalParametersType:
    pass
DefaultValueForOptionalParameters = DefaultValueForOptionalParametersType()

class GitAuthor( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def date( self ):
        self.__completeIfNeeded( self.__date )
        return self.__date

    @property
    def email( self ):
        self.__completeIfNeeded( self.__email )
        return self.__email

    @property
    def name( self ):
        self.__completeIfNeeded( self.__name )
        return self.__name

    def __initAttributes( self ):
        self.__date = None
        self.__email = None
        self.__name = None

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
        if "date" in attributes and attributes[ "date" ] is not None:
            assert isinstance( attributes[ "date" ], ( str, unicode ) )
            self.__date = attributes[ "date" ]
        if "email" in attributes and attributes[ "email" ] is not None:
            assert isinstance( attributes[ "email" ], ( str, unicode ) )
            self.__email = attributes[ "email" ]
        if "name" in attributes and attributes[ "name" ] is not None:
            assert isinstance( attributes[ "name" ], ( str, unicode ) )
            self.__name = attributes[ "name" ]
