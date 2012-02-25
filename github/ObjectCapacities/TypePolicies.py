class SimpleTypePolicy:
    def createLazy( self, obj, value ):
        return value

    def createNonLazy( self, obj, value ):
        return value

class ObjectTypePolicy:
    def __init__( self, type ):
        self.__type = type

    def createLazy( self, obj, attributes ):
        return self.__type( obj._github, attributes, lazy = True )

    def createNonLazy( self, obj, attributes ):
        return self.__type( obj._github, attributes, lazy = False )

    def getIdentity( self, obj ):
        assert isinstance( obj, self.__type )
        return obj._identity
