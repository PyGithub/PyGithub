# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GitTree

class GitCommit( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def author( self ):
        self.__completeIfNeeded( self.__author )
        return self.__author

    @property
    def committer( self ):
        self.__completeIfNeeded( self.__committer )
        return self.__committer

    @property
    def message( self ):
        self.__completeIfNeeded( self.__message )
        return self.__message

    @property
    def parents( self ):
        self.__completeIfNeeded( self.__parents )
        return self.__parents

    @property
    def sha( self ):
        self.__completeIfNeeded( self.__sha )
        return self.__sha

    @property
    def tree( self ):
        self.__completeIfNeeded( self.__tree )
        return self.__tree

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def __initAttributes( self ):
        self.__author = None
        self.__committer = None
        self.__message = None
        self.__parents = None
        self.__sha = None
        self.__tree = None
        self.__url = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete()

    # @todo Do not generate __complete if type has no url attribute
    def __complete( self ):
        result = self.__github._dataRequest(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( result )
        self.__completed = True

    def __useAttributes( self, attributes ):
         #@todo No need to check if attribute is in attributes when attribute is mandatory
        if "author" in attributes:
            self.__author = attributes[ "author" ]
        if "committer" in attributes:
            self.__committer = attributes[ "committer" ]
        if "message" in attributes:
            self.__message = attributes[ "message" ]
        if "parents" in attributes:
            self.__parents = attributes[ "parents" ]
        if "sha" in attributes:
            self.__sha = attributes[ "sha" ]
        if "tree" in attributes:
            self.__tree = GitTree.GitTree( self.__github, attributes[ "tree" ], lazy = True )
        if "url" in attributes:
            self.__url = attributes[ "url" ]
