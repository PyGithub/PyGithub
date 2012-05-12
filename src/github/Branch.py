# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import Commit

class Branch( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def commit( self ):
        return self.__commit

    @property
    def name( self ):
        return self.__name

    def __initAttributes( self ):
        self.__commit = None
        self.__name = None

    def __useAttributes( self, attributes ):
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "commit", "name", ]
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "commit" in attributes and attributes[ "commit" ] is not None:
            assert isinstance( attributes[ "commit" ], dict )
            self.__commit = Commit.Commit( self.__requester, attributes[ "commit" ], lazy = True )
        if "name" in attributes and attributes[ "name" ] is not None:
            assert isinstance( attributes[ "name" ], ( str, unicode ) )
            self.__name = attributes[ "name" ]
