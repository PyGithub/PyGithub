class SimpleTypePolicy:
    def __init__( self, type ):
        self.__type = type

    def createLazy( self, obj, value ):
        return value

    def getIdentity( self, value ):
        return value

    def hasMeaningfulDocumentation( self ):
        return self.__type is not None

    def documentTypeName( self ):
        return self.__type

class ObjectTypePolicy:
    def __init__( self, type ):
        self.__type = type

    def createLazy( self, obj, attributes ):
        if isinstance( attributes, self.__type ):
            return attributes
        else:
            return self.__type( obj._github, attributes, lazy = True )

    def createNonLazy( self, obj, attributes ):
        return self.__type( obj._github, attributes, lazy = False )

    def getIdentity( self, obj ):
        assert isinstance( obj, self.__type )
        return obj._identity

    def hasMeaningfulDocumentation( self ):
        return True

    def documentTypeName( self ):
        return "`" + self.__type.__name__ + "`"
