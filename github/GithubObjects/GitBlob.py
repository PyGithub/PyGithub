# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class GitBlob( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def content( self ):
        self.__completeIfNeeded( self.__content )
        return self.__content

    @property
    def encoding( self ):
        self.__completeIfNeeded( self.__encoding )
        return self.__encoding

    @property
    def sha( self ):
        self.__completeIfNeeded( self.__sha )
        return self.__sha

    @property
    def size( self ):
        self.__completeIfNeeded( self.__size )
        return self.__size

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def __initAttributes( self ):
        self.__content = None
        self.__encoding = None
        self.__sha = None
        self.__size = None
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
        if "content" in attributes:
            self.__content = attributes[ "content" ]
        if "encoding" in attributes:
            self.__encoding = attributes[ "encoding" ]
        if "sha" in attributes:
            self.__sha = attributes[ "sha" ]
        if "size" in attributes:
            self.__size = attributes[ "size" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
