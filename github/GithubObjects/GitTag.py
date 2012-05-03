# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class GitTag( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def message( self ):
        self.__completeIfNeeded( self.__message )
        return self.__message

    @property
    def object( self ):
        self.__completeIfNeeded( self.__object )
        return self.__object

    @property
    def sha( self ):
        self.__completeIfNeeded( self.__sha )
        return self.__sha

    @property
    def tag( self ):
        self.__completeIfNeeded( self.__tag )
        return self.__tag

    @property
    def tagger( self ):
        self.__completeIfNeeded( self.__tagger )
        return self.__tagger

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def __initAttributes( self ):
        self.__message = None
        self.__object = None
        self.__sha = None
        self.__tag = None
        self.__tagger = None
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
