# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *

class Plan( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__completed = completion != LazyCompletion
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def collaborators( self ):
        return self.__collaborators

    @property
    def name( self ):
        return self.__name

    @property
    def private_repos( self ):
        return self.__private_repos

    @property
    def space( self ):
        return self.__space

    def __initAttributes( self ):
        self.__collaborators = None
        self.__name = None
        self.__private_repos = None
        self.__space = None

    def __useAttributes( self, attributes ):
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "collaborators", "name", "private_repos", "space", ], attribute
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "collaborators" in attributes and attributes[ "collaborators" ] is not None:
            assert isinstance( attributes[ "collaborators" ], int )
            self.__collaborators = attributes[ "collaborators" ]
        if "name" in attributes and attributes[ "name" ] is not None:
            assert isinstance( attributes[ "name" ], ( str, unicode ) )
            self.__name = attributes[ "name" ]
        if "private_repos" in attributes and attributes[ "private_repos" ] is not None:
            assert isinstance( attributes[ "private_repos" ], int )
            self.__private_repos = attributes[ "private_repos" ]
        if "space" in attributes and attributes[ "space" ] is not None:
            assert isinstance( attributes[ "space" ], int )
            self.__space = attributes[ "space" ]
