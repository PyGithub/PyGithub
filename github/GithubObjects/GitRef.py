# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class GitRef( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

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

    def delete( self ):
        pass

    def edit( self, sha, force = None ):
        post_parameters = {
            "sha": sha,
        }
        if force is not None:
            post_parameters[ "force" ] = force
        result = self.__github._dataRequest(
            "PATCH",
            "https://api.github.com/user",
            None,
            post_parameters
        )
        self.__useAttributes( result )

    def __initAttributes( self ):
        self.__object = None
        self.__ref = None
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
        if "object" in attributes:
            self.__object = attributes[ "object" ]
        if "ref" in attributes:
            self.__ref = attributes[ "ref" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
