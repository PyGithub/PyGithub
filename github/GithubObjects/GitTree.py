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
        if self.__recursive is None:
            self.__completeIfNeeded()
        return self.__recursive

    @property
    def sha( self ):
        if self.__sha is None:
            self.__completeIfNeeded()
        return self.__sha

    @property
    def tree( self ):
        if self.__tree is None:
            self.__completeIfNeeded()
        return self.__tree

    @property
    def url( self ):
        if self.__url is None:
            self.__completeIfNeeded()
        return self.__url

    def __initAttributes( self ):
        self.__recursive = None
        self.__sha = None
        self.__tree = None
        self.__url = None

    def __completeIfNeeded( self ):
        if not self.__completed:
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
