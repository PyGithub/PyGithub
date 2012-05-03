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
        self.__completeIfNeeded( self.__color )
        return self.__color

    @property
    def name( self ):
        self.__completeIfNeeded( self.__name )
        return self.__name

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def __initAttributes( self ):
        self.__color = None
        self.__name = None
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

    def edit( self, name, color ):
        post_parameters = {
            "name": name,
            "color": color,
        }
        result = self.__github._dataRequest(
            "PATCH",
            "https://api.github.com/user",
            None,
            post_parameters
        )
        self.__useAttributes( result )

    def __useAttributes( self, attributes ):
        if "color" in attributes:
            self.__color = attributes[ "color" ]
        if "name" in attributes:
            self.__name = attributes[ "name" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
