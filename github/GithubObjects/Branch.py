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
        if self.__commit is None:
            self.__completeIfNeeded()
        return self.__commit

    @property
    def name( self ):
        if self.__name is None:
            self.__completeIfNeeded()
        return self.__name

    def __initAttributes( self ):
        self.__commit = None
        self.__name = None

    def __completeIfNeeded( self ):
        if not self.__completed:
            self.__complete()
        self.__completed = True

    def __complete( self ):
        pass

    def __useAttributes( self, attributes ):
        if "commit" in attributes:
            self.__commit = attributes[ "commit" ]
        if "name" in attributes:
            self.__name = attributes[ "name" ]
