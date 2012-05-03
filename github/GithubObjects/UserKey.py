# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class UserKey( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def id( self ):
        self.__completeIfNeeded( self.__id )
        return self.__id

    @property
    def key( self ):
        self.__completeIfNeeded( self.__key )
        return self.__key

    @property
    def title( self ):
        self.__completeIfNeeded( self.__title )
        return self.__title

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def __initAttributes( self ):
        self.__id = None
        self.__key = None
        self.__title = None
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

    def edit( self, title = None, key = None ):
        pass

    def __useAttributes( self, attributes ):
        if "id" in attributes:
            self.__id = attributes[ "id" ]
        if "key" in attributes:
            self.__key = attributes[ "key" ]
        if "title" in attributes:
            self.__title = attributes[ "title" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
