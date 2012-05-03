# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import Commit

class Branch( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def commit( self ):
        self.__completeIfNeeded( self.__commit )
        return self.__commit

    @property
    def name( self ):
        self.__completeIfNeeded( self.__name )
        return self.__name

    def __initAttributes( self ):
        self.__commit = None
        self.__name = None

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
        if "commit" in attributes:
            self.__commit = Commit.Commit( self.__github, attributes[ "commit" ], lazy = True )
        if "name" in attributes:
            self.__name = attributes[ "name" ]
