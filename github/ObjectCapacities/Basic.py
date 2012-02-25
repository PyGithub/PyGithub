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

### @todo include the ArgumentsChecker
class MethodFromCallable:
    def __init__( self, name, callable ):
        self.__name = name
        self.__callable = callable

    def apply( self, cls ):
        cls._addMethod( self.__name, self.__callable )

class InternalAttribute:
    class AttributeDefinition:
        def __init__( self, typePolicy ):
            self.__typePolicy = typePolicy

        def getValueFromRawValue( self, obj, rawValue ):
			if rawValue is None:
				return None
			else:
				return self.__typePolicy.createLazy( obj, rawValue )

        def updateAttributes( self, obj ):
            attributes = obj._github._dataRequest( "GET", obj._baseUrl, None, None )
            obj._updateAttributes( attributes )
            obj._markAsCompleted()

        def isLazy( self ):
            return True

    def __init__( self, attributeName, typePolicy ):
        self.__attributeName = attributeName
        self.__typePolicy = typePolicy

    def apply( self, cls ):
        cls._addAttribute( self.__attributeName, InternalAttribute.AttributeDefinition( self.__typePolicy ) )

class ExternalAttribute:
    def __init__( self, attributeName, typePolicy ):
        self.__attributeName = attributeName
        self.__typePolicy = typePolicy

    def apply( self, cls ):
        cls._addMethod( "get_" + self.__attributeName, self.__execute )

    def __execute( self, obj ):
        return self.__typePolicy.createLazy(
            obj,
            obj._github._dataRequest( "GET", obj._baseUrl + "/" + self.__attributeName, None, None )
        )

class SeveralAttributePolicies:
    def __init__( self, attributePolicies ):
        self.__attributePolicies = attributePolicies

    def apply( self, cls ):
        for attributePolicy in self.__attributePolicies:
            attributePolicy.apply( cls )
