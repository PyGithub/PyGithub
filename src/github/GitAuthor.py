# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *

class GitAuthor( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def date( self ):
        return self.__date

    @property
    def email( self ):
        return self.__email

    @property
    def name( self ):
        return self.__name

    def __initAttributes( self ):
        self.__date = None
        self.__email = None
        self.__name = None

    def __useAttributes( self, attributes ):
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "date" in attributes and attributes[ "date" ] is not None: # pragma no branch
            assert isinstance( attributes[ "date" ], ( str, unicode ) )
            self.__date = attributes[ "date" ]
        if "email" in attributes and attributes[ "email" ] is not None: # pragma no branch
            assert isinstance( attributes[ "email" ], ( str, unicode ) )
            self.__email = attributes[ "email" ]
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "name" ], ( str, unicode ) )
            self.__name = attributes[ "name" ]
