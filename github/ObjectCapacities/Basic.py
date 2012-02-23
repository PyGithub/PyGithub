class AttributeFromCallable:
    class AttributeDefinition:
        def __init__( self, name, callable ):
            self.__name = name
            self.__callable = callable

        def getValueFromRawValue( self, obj, rawValue ):
            return rawValue

        def updateAttributes( self, obj ):
            obj._updateAttributes( { self.__name: self.__callable( obj ) } )

        def isLazy( self ):
            return False

    def __init__( self, name, callable ):
        self.__name = name
        self.__callable = callable

    def apply( self, cls ):
        cls._addAttribute( self.__name, AttributeFromCallable.AttributeDefinition( self.__name, self.__callable ) )

class MethodFromCallable:
    def __init__( self, name, callable ):
        self.__name = name
        self.__callable = callable

    def apply( self, cls ):
        cls._addMethod( self.__name, self.__callable )
