class SimpleTypePolicy:
    def create( self, obj, rawValue ):
        return rawValue

class ObjectTypePolicy:
    def __init__( self, type ):
        self.__type = type

    def create( self, obj, rawValue ):
        return self.__type( obj._github, rawValue, lazy = True )
