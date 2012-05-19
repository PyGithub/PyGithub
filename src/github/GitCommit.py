# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import GitAuthor
import GitCommit
import GitTree

class GitCommit( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def author( self ):
        return self.__author

    @property
    def committer( self ):
        return self.__committer

    @property
    def message( self ):
        return self.__message

    @property
    def parents( self ):
        return self.__parents

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
        self.__author = None
        self.__committer = None
        self.__message = None
        self.__parents = None
        self.__sha = None
        self.__tree = None
        self.__url = None

    def __useAttributes( self, attributes ):
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "author", "committer", "message", "parents", "sha", "tree", "url", ], attribute
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "author" in attributes and attributes[ "author" ] is not None:
            assert isinstance( attributes[ "author" ], dict )
            self.__author = GitAuthor.GitAuthor( self.__requester, attributes[ "author" ], completion = LazyCompletion )
        if "committer" in attributes and attributes[ "committer" ] is not None:
            assert isinstance( attributes[ "committer" ], dict )
            self.__committer = GitAuthor.GitAuthor( self.__requester, attributes[ "committer" ], completion = LazyCompletion )
        if "message" in attributes and attributes[ "message" ] is not None:
            assert isinstance( attributes[ "message" ], ( str, unicode ) )
            self.__message = attributes[ "message" ]
        if "parents" in attributes and attributes[ "parents" ] is not None:
            assert isinstance( attributes[ "parents" ], list ) and ( len( attributes[ "parents" ] ) == 0 or isinstance( attributes[ "parents" ][ 0 ], dict ) )
            self.__parents = [
                GitCommit( self.__requester, element, completion = LazyCompletion )
                for element in attributes[ "parents" ]
            ]
        if "sha" in attributes and attributes[ "sha" ] is not None:
            assert isinstance( attributes[ "sha" ], ( str, unicode ) )
            self.__sha = attributes[ "sha" ]
        if "tree" in attributes and attributes[ "tree" ] is not None:
            assert isinstance( attributes[ "tree" ], dict )
            self.__tree = GitTree.GitTree( self.__requester, attributes[ "tree" ], completion = LazyCompletion )
        if "url" in attributes and attributes[ "url" ] is not None:
            assert isinstance( attributes[ "url" ], ( str, unicode ) )
            self.__url = attributes[ "url" ]
