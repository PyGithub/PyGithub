# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class GitTag( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def message( self ):
        if self.__message is None:
            self.__completeIfNeeded()
        return self.__message

    @property
    def object( self ):
        if self.__object is None:
            self.__completeIfNeeded()
        return self.__object

    @property
    def sha( self ):
        if self.__sha is None:
            self.__completeIfNeeded()
        return self.__sha

    @property
    def tag( self ):
        if self.__tag is None:
            self.__completeIfNeeded()
        return self.__tag

    @property
    def tagger( self ):
        if self.__tagger is None:
            self.__completeIfNeeded()
        return self.__tagger

    @property
    def url( self ):
        if self.__url is None:
            self.__completeIfNeeded()
        return self.__url

    def __initAttributes( self ):
        self.__message = None
        self.__object = None
        self.__sha = None
        self.__tag = None
        self.__tagger = None
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
        if "message" in attributes:
            self.__message = attributes[ "message" ]
        if "object" in attributes:
            self.__object = attributes[ "object" ]
        if "sha" in attributes:
            self.__sha = attributes[ "sha" ]
        if "tag" in attributes:
            self.__tag = attributes[ "tag" ]
        if "tagger" in attributes:
            self.__tagger = attributes[ "tagger" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
