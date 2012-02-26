from ArgumentsChecker import *

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

    def autoDocument( self ):
        return ""
        return "* `" + self.__name + "`\n"

### @todo include the ArgumentsChecker
class MethodFromCallable:
    def __init__( self, name, mandatoryParameters, optionalParameters, callable, returnTypePolicy ):
        self.__argumentsChecker = ArgumentsChecker( mandatoryParameters, optionalParameters )
        self.__name = name
        self.__callable = callable
        self.__returnTypePolicy = returnTypePolicy

    def apply( self, cls ):
        cls._addMethod( self.__name, self.__execute )

    def __execute( self, obj, *args, **kwds ):
        data = self.__argumentsChecker.check( args, kwds )
        return self.__callable( obj, **data )

    def autoDocument( self ):
        doc = "* `" + self.__name + "(" + self.__argumentsChecker.documentParameters() + ")`"
        if self.__returnTypePolicy.hasMeaningfulDocumentation():
            doc += ": " + self.__returnTypePolicy.documentTypeName()
        doc += "\n"
        return doc

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

    def autoDocument( self ):
        if self.__attributeName.startswith( "_" ):
            return ""
        doc = "* `" + self.__attributeName + "`"
        if self.__typePolicy.hasMeaningfulDocumentation():
            doc += ": " + self.__typePolicy.documentTypeName()
        doc += "\n"
        return doc

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

    def autoDocument( self ):
        return "* `get_" + self.__attributeName + "()`: " + self.__typePolicy.documentTypeName() + "\n"

class SeveralAttributePolicies:
    def __init__( self, attributePolicies, documentationSection = None ):
        self.__attributePolicies = attributePolicies
        self.__documentationSection = documentationSection

    def apply( self, cls ):
        for attributePolicy in self.__attributePolicies:
            attributePolicy.apply( cls )

    def autoDocument( self ):
        doc = ""
        if self.__documentationSection is not None:
            doc += "\n"
            doc += self.__documentationSection + "\n"
            doc += "-" * len( self.__documentationSection ) + "\n"
        doc += "".join( attributePolicy.autoDocument() for attributePolicy in self.__attributePolicies )
        return doc
