# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import urllib
import PaginatedList
import GithubException
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters

class Label( object ):
    def __init__( self, requester, attributes, completed ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def color( self ):
        return self.__color

    @property
    def name( self ):
        return self.__name

    @property
    def url( self ):
        return self.__url

    def delete( self ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ),
            None,
            None
        )
        if self.__requester.isFailureStatus( status ): # pragma no branch
            raise GithubException.GithubException( status, data ) # pragma no cover

    def edit( self, name, color ):
        assert isinstance( name, ( str, unicode ) ), name
        assert isinstance( color, ( str, unicode ) ), color
        post_parameters = {
            "name": name,
            "color": color,
        }
        status, headers, data = self.__requester.request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        if self.__requester.isFailureStatus( status ): # pragma no branch
            raise GithubException.GithubException( status, data ) # pragma no cover
        self.__useAttributes( data )

    @property
    def _identity( self ):
        return urllib.quote( str( self.name ) )

    def __initAttributes( self ):
        self.__color = None
        self.__name = None
        self.__url = None

    def __useAttributes( self, attributes ):
        if "color" in attributes and attributes[ "color" ] is not None: # pragma no branch
            assert isinstance( attributes[ "color" ], ( str, unicode ) ), attributes[ "color" ]
            self.__color = attributes[ "color" ]
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self.__name = attributes[ "name" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self.__url = attributes[ "url" ]
