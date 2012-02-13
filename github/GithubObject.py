import itertools

class BadGithubObjectException( Exception ):
    pass

class SimpleScalarAttributes:
    class AttributeDefinition:
        def __init__( self, attributeNames ):
            self.__attributeNames = attributeNames

        def getValueFromRawValue( self, obj, rawValue ):
            # if isinstance( rawValue, dict ):
                # print rawValue, "is a dict, you may want to use an extended attribute for it"
            return rawValue

        def updateAttributes( self, obj ):
            attributes = obj._github._dataRequest( "GET", obj._baseUrl )
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

class ExtendedListAttribute:
    class Getter:
        def __init__( self, obj, attributeName, type ):
            self.__obj = obj
            self.__attributeName = attributeName
            self.__type = type

        def __call__( self ):
            return [
                self.__type( self.__obj._github, attributes, lazy = True )
                for attributes in self.__obj._github._dataRequest( "GET", self.__obj._baseUrl + "/" + self.__attributeName )
            ]

    class GetDefinition:
        def __init__( self, attributeName, getName, type ):
            self.__getName = getName
            self.__attributeName = attributeName
            self.__type = type

        def getValueFromRawValue( self, obj, rawValue ):
            return rawValue

        def updateAttributes( self, obj ):
            obj._updateAttributes( { self.__getName: ExtendedListAttribute.Getter( obj, self.__attributeName, self.__type ) } )

    class Remover:
        def __init__( self, obj, attributeName, type ):
            self.__obj = obj
            self.__attributeName = attributeName
            self.__type = type

        def __call__( self, toBeDeleted ):
            assert( isinstance( toBeDeleted, self.__type ) )
            self.__obj._github._dataRequest( "DELETE", self.__obj._baseUrl + "/" + self.__attributeName + "/" + toBeDeleted._identity )

    class RemoveDefinition:
        def __init__( self, attributeName, removeName, type ):
            self.__removeName = removeName
            self.__attributeName = attributeName
            self.__type = type

        def getValueFromRawValue( self, obj, rawValue ):
            return rawValue

        def updateAttributes( self, obj ):
            obj._updateAttributes( { self.__removeName: ExtendedListAttribute.Remover( obj, self.__attributeName, self.__type ) } )

    class Adder:
        def __init__( self, obj, attributeName, type ):
            self.__obj = obj
            self.__attributeName = attributeName
            self.__type = type

        def __call__( self, toBeAdded ):
            assert( isinstance( toBeAdded, self.__type ) )
            self.__obj._github._dataRequest( "PUT", self.__obj._baseUrl + "/" + self.__attributeName + "/" + toBeAdded._identity )

    class AddDefinition:
        def __init__( self, attributeName, addName, type ):
            self.__addName = addName
            self.__attributeName = attributeName
            self.__type = type

        def getValueFromRawValue( self, obj, rawValue ):
            return rawValue

        def updateAttributes( self, obj ):
            obj._updateAttributes( { self.__addName: ExtendedListAttribute.Adder( obj, self.__attributeName, self.__type ) } )

    def __init__( self, attributeName, type, addable = False, removable = False ):
        self.__attributeName = attributeName
        self.__type = type
        self.__getName = "get_" + attributeName
        if addable:
            self.__addName = "add_" + attributeName
        else:
            self.__addName = None
        if removable:
            self.__removeName = "remove_" + attributeName
        else:
            self.__removeName = None

    def getAttributeDefinitions( self ):
        yield self.__getName, ExtendedListAttribute.GetDefinition( self.__attributeName, self.__getName, self.__type )
        if self.__addName is not None:
            yield self.__addName, ExtendedListAttribute.AddDefinition( self.__attributeName, self.__addName, self.__type )
        if self.__removeName is not None:
            yield self.__removeName, ExtendedListAttribute.RemoveDefinition( self.__attributeName, self.__removeName, self.__type )

class ExtendedScalarAttribute:
    class AttributeDefinition:
        def __init__( self, attributeName, type ):
            self.__attributeName = attributeName
            self.__type = type

        def getValueFromRawValue( self, obj, rawValue ):
            return self.__type( obj._github, rawValue, lazy = True )

        def updateAttributes( self, obj ):
            attributes = obj._github._dataRequest( "GET", obj._baseUrl )
            # for attributeName in self.__attributeNames:
                # if attributeName not in attributes:
                    # attributes[ attributeName ] = None
            obj._updateAttributes( attributes )

    def __init__( self, attributeName, type ):
        self.__attributeName = attributeName
        self.__type = type

    def getAttributeDefinitions( self ):
        yield self.__attributeName, ExtendedScalarAttribute.AttributeDefinition( self.__attributeName, self.__type )

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
            attributes = self.__obj._github._dataRequest( "PATCH", self.__obj._baseUrl, kwds )
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
    class Deleter:
        def __init__( self, obj ):
            self.__obj = obj

        def __call__( self ):
            self.__obj._github._dataRequest( "DELETE", self.__obj._baseUrl )

    class AttributeDefinition:
        def getValueFromRawValue( self, obj, rawValue ):
            return rawValue

        def updateAttributes( self, obj ):
            obj._updateAttributes( { "delete": Deletable.Deleter( obj ) } )

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

class Identity:
    class AttributeDefinition:
        def __init__( self, identity ):
            self.__identity = identity

        def getValueFromRawValue( self, obj, rawValue ):
            return rawValue

        def updateAttributes( self, obj ):
            obj._updateAttributes( { "_identity": self.__identity( obj ) } )

    def __init__( self, identity ):
        self.__identity = identity

    def getAttributeDefinitions( self ):
        yield "_identity", Identity.AttributeDefinition( self.__identity )

def GithubObject( className, *attributePolicies ):
    class GithubObject:
        __attributeDefinitions = dict()

        @staticmethod
        def _addAttributePolicy( attributePolicy ):
            for attributeName, attributeDefinition in attributePolicy.getAttributeDefinitions():
                if attributeName in GithubObject.__attributeDefinitions:
                    raise BadGithubObjectException( "Same attribute defined by two policies" )
                else:
                    GithubObject.__attributeDefinitions[ attributeName ] = attributeDefinition

        def __init__( self, github, attributes, lazy ):
            self._github = github
            self.__attributes = dict()
            self._updateAttributes( attributes )
            if not lazy:
                for attributeName in GithubObject.__attributeDefinitions:
                    if attributeName not in self.__attributes:
                        self.__fetchAttribute( attributeName )

        def __getattr__( self, attributeName ):
            if attributeName in GithubObject.__attributeDefinitions:
                if attributeName not in self.__attributes:
                    self.__fetchAttribute( attributeName )
                return self.__attributes[ attributeName ]
            else:
                raise AttributeError()

        def _updateAttributes( self, attributes ):
            for attributeName, attributeValue in attributes.iteritems():
                attributeDefinition = GithubObject.__attributeDefinitions[ attributeName ]
                if attributeValue is None:
                    if attributeName not in self.__attributes:
                        self.__attributes[ attributeName ] = None
                else:
                    self.__attributes[ attributeName ] = attributeDefinition.getValueFromRawValue( self, attributeValue )

        def __dir__( self ):
            return GithubObject.__attributeDefinitions.keys()

        def __fetchAttribute( self, attributeName ):
            attributeDefinition = GithubObject.__attributeDefinitions[ attributeName ]
            attributeDefinition.updateAttributes( self )

    GithubObject.__name__ = className

    for attributePolicy in attributePolicies:
        GithubObject._addAttributePolicy( attributePolicy )

    return GithubObject
