import itertools

class BadGithubObjectException( Exception ):
    pass

class SimpleScalarAttributes:
    class AttributeDefinition:
        def __init__( self, attributeNames ):
            self.__attributeNames = attributeNames

        def getValueFromRawValue( self, obj, rawValue ):
            return rawValue

        def updateAttributes( self, obj ):
            attributes = obj._github.rawRequest( "GET", obj._baseUrl )
            for attributeName in self.__attributeNames:
                if attributeName not in attributes:
                    attributes[ attributeName ] = None
            obj._updateAttributes( attributes )

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
        def __init__( self, obj, mandatoryParameters, optionalParameters ):
            self.__obj = obj
            self.__mandatoryParameters = mandatoryParameters
            self.__optionalParameters = optionalParameters

        def __call__( self, *args, **kwds ):
            if len( args ) + len( kwds ) == 0:
                raise TypeError()
            for arg, argumentName in itertools.izip( args, itertools.chain( self.__mandatoryParameters, self.__optionalParameters ) ):
                kwds[ argumentName ] = arg
            for argumentName in kwds:
                if argumentName not in itertools.chain( self.__mandatoryParameters, self.__optionalParameters ):
                    raise TypeError()
            attributes = self.__obj._github.rawRequest( "PATCH", self.__obj._baseUrl, kwds )
            self.__obj._updateAttributes( attributes )

    class AttributeDefinition:
        def __init__( self, mandatoryParameters, optionalParameters ):
            self.__mandatoryParameters = mandatoryParameters
            self.__optionalParameters = optionalParameters

        def getValueFromRawValue( self, obj, rawValue ):
            return rawValue

        def updateAttributes( self, obj ):
            obj._updateAttributes( { "edit": Editable.Editor( obj, self.__mandatoryParameters, self.__optionalParameters ) } )

    def __init__( self, mandatoryParameters, optionalParameters ):
        self.__mandatoryParameters = mandatoryParameters
        self.__optionalParameters = optionalParameters

    def getAttributeDefinitions( self ):
        yield "edit", Editable.AttributeDefinition( self.__mandatoryParameters, self.__optionalParameters )

class Deletable:
    class Deletor:
        def __init__( self, obj ):
            self.__obj = obj

        def __call__( self ):
            self.__obj._github.rawRequest( "DELETE", self.__obj._baseUrl )

    class AttributeDefinition:
        def getValueFromRawValue( self, obj, rawValue ):
            return rawValue

        def updateAttributes( self, obj ):
            obj._updateAttributes( { "delete": Deletable.Deletor( obj ) } )

    def getAttributeDefinitions( self ):
        yield "delete", Deletable.AttributeDefinition()

class BaseUrl:
    class AttributeDefinition:
        def __init__( self, baseUrl ):
            self.__baseUrl = baseUrl

        def getValueFromRawValue( self, obj, rawValue ):
            return rawValue

        def updateAttributes( self, obj ):
            obj._updateAttributes( { "_baseUrl": self.__baseUrl( obj ) } )

    def __init__( self, baseUrl ):
        self.__baseUrl = baseUrl

    def getAttributeDefinitions( self ):
        yield "_baseUrl", BaseUrl.AttributeDefinition( self.__baseUrl )

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
            attributeDefinition.updateAttributes( self )

    return GithubObject
