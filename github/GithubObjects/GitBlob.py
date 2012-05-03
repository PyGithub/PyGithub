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
        if self.__content is None:
            self.__completeIfNeeded()
        return self.__content

    @property
    def encoding( self ):
        if self.__encoding is None:
            self.__completeIfNeeded()
        return self.__encoding

    @property
    def sha( self ):
        if self.__sha is None:
            self.__completeIfNeeded()
        return self.__sha

    @property
    def size( self ):
        if self.__size is None:
            self.__completeIfNeeded()
        return self.__size

    @property
    def url( self ):
        if self.__url is None:
            self.__completeIfNeeded()
        return self.__url

    def __initAttributes( self ):
        self.__content = None
        self.__encoding = None
        self.__sha = None
        self.__size = None
        self.__url = None

    def __completeIfNeeded( self ):
        if not self.__completed:
            self.__complete()
        self.__completed = True

    def __complete( self ):
        pass

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
