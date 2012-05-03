# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class GitTree( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def recursive( self ):
        self.__completeIfNeeded( self.__recursive )
        return self.__recursive

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
        self.__recursive = None
        self.__sha = None
        self.__tree = None
        self.__url = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete()
        self.__completed = True

    # @todo Do not generate __complete if type has no url attribute
    def __complete( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url,
            None,
            None
        )
        self.__useAttributes( result )

    def __useAttributes( self, attributes ):
        if "recursive" in attributes:
            self.__recursive = attributes[ "recursive" ]
        if "sha" in attributes:
            self.__sha = attributes[ "sha" ]
        if "tree" in attributes:
            self.__tree = attributes[ "tree" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
