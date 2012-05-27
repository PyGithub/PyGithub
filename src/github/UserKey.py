# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *

class UserKey( object ):
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

    @property
    def verified( self ):
        self.__completeIfNeeded( self.__verified )
        return self.__verified

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
        self.__verified = None

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
            assert attribute in [ "id", "key", "title", "url", "verified", ], attribute
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            self.__id = attributes[ "id" ]
        if "key" in attributes and attributes[ "key" ] is not None: # pragma no branch
            self.__key = attributes[ "key" ]
        if "title" in attributes and attributes[ "title" ] is not None: # pragma no branch
            self.__title = attributes[ "title" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            self.__url = attributes[ "url" ]
        if "verified" in attributes and attributes[ "verified" ] is not None: # pragma no branch
            assert isinstance( attributes[ "verified" ], bool )
            self.__verified = attributes[ "verified" ]
