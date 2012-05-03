# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class Label( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def color( self ):
        if self.__color is None:
            self.__completeIfNeeded()
        return self.__color

    @property
    def name( self ):
        if self.__name is None:
            self.__completeIfNeeded()
        return self.__name

    @property
    def url( self ):
        if self.__url is None:
            self.__completeIfNeeded()
        return self.__url

    def __initAttributes( self ):
        self.__color = None
        self.__name = None
        self.__url = None

    def __completeIfNeeded( self ):
        if not self.__completed:
            self.__complete()
        self.__completed = True

    def __complete( self ):
        pass

    def delete( self ):
        pass

    def edit( self, name, color ):
        pass

    def __useAttributes( self, attributes ):
        if "color" in attributes:
            self.__color = attributes[ "color" ]
        if "name" in attributes:
            self.__name = attributes[ "name" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
