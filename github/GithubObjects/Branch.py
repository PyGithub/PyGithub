# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import Commit

class Branch( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

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
        if "commit" in attributes:
            self.__commit = attributes[ "commit" ]
        if "name" in attributes:
            self.__name = attributes[ "name" ]
