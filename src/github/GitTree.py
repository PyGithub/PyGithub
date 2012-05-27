# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import GitTreeElement

class GitTree( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def sha( self ):
        return self.__sha

    @property
    def tree( self ):
        return self.__tree

    @property
    def url( self ):
        return self.__url

    def __initAttributes( self ):
        self.__sha = None
        self.__tree = None
        self.__url = None

    def __useAttributes( self, attributes ):
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) )
            self.__sha = attributes[ "sha" ]
        if "tree" in attributes and attributes[ "tree" ] is not None: # pragma no branch
            assert isinstance( attributes[ "tree" ], list ) and ( len( attributes[ "tree" ] ) == 0 or isinstance( attributes[ "tree" ][ 0 ], dict ) )
            self.__tree = [
                GitTreeElement.GitTreeElement( self.__requester, element, completion = LazyCompletion )
                for element in attributes[ "tree" ]
            ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) )
            self.__url = attributes[ "url" ]
