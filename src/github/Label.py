# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import urllib

import PaginatedList
from GithubObject import *

class Label( object ):
    def __init__( self, requester, attributes, completion ):
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

    def edit( self, name, color ):
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
        self.__useAttributes( data )

    # @todo Remove '_identity' from the normalized json description
    @property
    def _identity( self ):
        return urllib.quote( self.name )

    def __initAttributes( self ):
        self.__color = None
        self.__name = None
        self.__url = None

    def __useAttributes( self, attributes ):
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "color" in attributes and attributes[ "color" ] is not None: # pragma no branch
            self.__color = attributes[ "color" ]
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            self.__name = attributes[ "name" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            self.__url = attributes[ "url" ]
