import itertools

class BadGithubObjectException( Exception ):
    pass

class SimpleScalarAttributes:
    class AttributeDefinition:
        def __init__( self, attributeNames ):
            self.__attributeNames = attributeNames

        def getValueFromRawValue( self, obj, rawValue ):
            return rawValue

        def fetchRawValues( self, obj ):
            attributes = obj._github.rawRequest( "GET", "/test" )
            for attributeName in self.__attributeNames:
                if attributeName not in attributes:
                    attributes[ attributeName ] = None
            return attributes

    def __init__( self, *attributeNames ):
        self.__attributeNames = attributeNames

    def getAttributeDefinitions( self ):
        commonDefinition = SimpleScalarAttributes.AttributeDefinition( self.__attributeNames )
        return [
            ( attributeName, commonDefinition )
            for attributeName in self.__attributeNames
        ]

class Editable:
    class Editor:
        def __init__( self, obj, mandatoryParamters, optionalParameters ):
            self.__obj = obj
            self.__mandatoryParamters = mandatoryParamters
            self.__optionalParameters = optionalParameters

        def __call__( self, *args, **kwds ):
            if len( args ) + len( kwds ) == 0:
                raise TypeError()
            for arg, argumentName in itertools.izip( args, itertools.chain( self.__mandatoryParamters, self.__optionalParameters ) ):
                kwds[ argumentName ] = arg
            for argumentName in kwds:
                if argumentName not in itertools.chain( self.__mandatoryParamters, self.__optionalParameters ):
                    raise TypeError()
            attributes = self.__obj._github.rawRequest( "PATCH", "/test", kwds )
            self.__obj._updateAttributes( attributes )

    class AttributeDefinition:
        def __init__( self, mandatoryParamters, optionalParameters ):
            self.__mandatoryParamters = mandatoryParamters
            self.__optionalParameters = optionalParameters

        def getValueFromRawValue( self, obj, rawValue ):
            return rawValue

        def fetchRawValues( self, obj ):
            return { "edit": Editable.Editor( obj, self.__mandatoryParamters, self.__optionalParameters ) }

    def __init__( self, mandatoryParamters, optionalParameters ):
        self.__mandatoryParamters = mandatoryParamters
        self.__optionalParameters = optionalParameters

    def getAttributeDefinitions( self ):
        yield "edit", Editable.AttributeDefinition( self.__mandatoryParamters, self.__optionalParameters )

def GithubObject( className, *attributePolicies ):
    attributeDefinitions = dict()
    for attributePolicy in attributePolicies:
        for attributeName, attributeDefinition in attributePolicy.getAttributeDefinitions():
            if attributeName in attributeDefinitions:
                raise BadGithubObjectException( "Same attribute defined by two policies" )
            else:
                attributeDefinitions[ attributeName ] = attributeDefinition

    class GithubObject:
        def __init__( self, github, attributes, lazy ):
            self._github = github
            self.__attributes = dict()
            self._updateAttributes( attributes )
            if not lazy:
                for attributeName in attributeDefinitions:
                    if attributeName not in self.__attributes:
                        self.__fetchAttribute( attributeName )

        def __getattr__( self, attributeName ):
            if attributeName in attributeDefinitions:
                if attributeName not in self.__attributes:
                    self.__fetchAttribute( attributeName )
                return self.__attributes[ attributeName ]
            else:
                raise AttributeError()

        def _updateAttributes( self, attributes ):
            for attributeName, attributeValue in attributes.iteritems():
                attributeDefinition = attributeDefinitions[ attributeName ]
                if attributeValue is None:
                    if attributeName not in self.__attributes:
                        self.__attributes[ attributeName ] = None
                else:
                    self.__attributes[ attributeName ] = attributeDefinition.getValueFromRawValue( self, attributeValue )

        def __fetchAttribute( self, attributeName ):
            attributeDefinition = attributeDefinitions[ attributeName ]
            self._updateAttributes( attributeDefinition.fetchRawValues( self ) )

    return GithubObject
