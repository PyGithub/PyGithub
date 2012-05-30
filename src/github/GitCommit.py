# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import GitAuthor
import GitCommit
import GitTree

class GitCommit( object ):
    def __init__( self, requester, attributes, completed ):
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
        if "author" in attributes and attributes[ "author" ] is not None: # pragma no branch
            assert isinstance( attributes[ "author" ], dict ), attributes[ "author" ]
            self.__author = GitAuthor.GitAuthor( self.__requester, attributes[ "author" ], completed = False )
        if "committer" in attributes and attributes[ "committer" ] is not None: # pragma no branch
            assert isinstance( attributes[ "committer" ], dict ), attributes[ "committer" ]
            self.__committer = GitAuthor.GitAuthor( self.__requester, attributes[ "committer" ], completed = False )
        if "message" in attributes and attributes[ "message" ] is not None: # pragma no branch
            assert isinstance( attributes[ "message" ], ( str, unicode ) ), attributes[ "message" ]
            self.__message = attributes[ "message" ]
        if "parents" in attributes and attributes[ "parents" ] is not None: # pragma no branch
            assert all( isinstance( element, dict ) for element in attributes[ "parents" ] ), attributes[ "parents" ]
            self.__parents = [
                GitCommit( self.__requester, element, completed = False )
                for element in attributes[ "parents" ]
            ]
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self.__sha = attributes[ "sha" ]
        if "tree" in attributes and attributes[ "tree" ] is not None: # pragma no branch
            assert isinstance( attributes[ "tree" ], dict ), attributes[ "tree" ]
            self.__tree = GitTree.GitTree( self.__requester, attributes[ "tree" ], completed = False )
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self.__url = attributes[ "url" ]
