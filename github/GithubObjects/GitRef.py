# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class GitRef( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def object( self ):
        self.__completeIfNeeded( self.__object )
        return self.__object

    @property
    def ref( self ):
        self.__completeIfNeeded( self.__ref )
        return self.__ref

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def __initAttributes( self ):
        self.__object = None
        self.__ref = None
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

    def delete( self ):
        pass

    def edit( self, sha, force = None ):
        pass

    def __useAttributes( self, attributes ):
        if "object" in attributes:
            self.__object = attributes[ "object" ]
        if "ref" in attributes:
            self.__ref = attributes[ "ref" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
