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
        if self.__id is None:
            self.__completeIfNeeded()
        return self.__id

    @property
    def key( self ):
        if self.__key is None:
            self.__completeIfNeeded()
        return self.__key

    @property
    def title( self ):
        if self.__title is None:
            self.__completeIfNeeded()
        return self.__title

    @property
    def url( self ):
        if self.__url is None:
            self.__completeIfNeeded()
        return self.__url

    def __initAttributes( self ):
        self.__id = None
        self.__key = None
        self.__title = None
        self.__url = None

    def __completeIfNeeded( self ):
        if not self.__completed:
            self.__complete()
        self.__completed = True

    def __complete( self ):
        pass

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
