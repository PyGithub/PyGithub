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
        if self.__object is None:
            self.__completeIfNeeded()
        return self.__object

    @property
    def ref( self ):
        if self.__ref is None:
            self.__completeIfNeeded()
        return self.__ref

    @property
    def url( self ):
        if self.__url is None:
            self.__completeIfNeeded()
        return self.__url

    def __initAttributes( self ):
        self.__object = None
        self.__ref = None
        self.__url = None

    def __completeIfNeeded( self ):
        if not self.__completed:
            self.__complete()
        self.__completed = True

    def __complete( self ):
        pass

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
