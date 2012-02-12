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
            self.__updateAttributes( attributes )
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

        def __updateAttributes( self, attributes ):
            for attributeName, attributeValue in attributes.iteritems():
                attributeDefinition = attributeDefinitions[ attributeName ]
                if attributeValue is None:
                    if attributeName not in self.__attributes:
                        self.__attributes[ attributeName ] = None
                else:
                    self.__attributes[ attributeName ] = attributeDefinition.getValueFromRawValue( self, attributeValue )

        def __fetchAttribute( self, attributeName ):
            attributeDefinition = attributeDefinitions[ attributeName ]
            self.__updateAttributes( attributeDefinition.fetchRawValues( self ) )

    return GithubObject
