import itertools

class BadGithubObjectException( Exception ):
    pass

class BasicAttributes:
    class AttributeDefinition:
        def __init__( self, attributeNames ):
            self.__attributeNames = attributeNames

        def getValueFromRawValue( self, obj, rawValue ):
            return rawValue

        def updateAttributes( self, obj ):
            attributes = obj._github._dataRequest( "GET", obj._baseUrl )
            for attributeName in self.__attributeNames:
                if attributeName not in attributes:
                    attributes[ attributeName ] = None
            obj._updateAttributes( attributes )

    def __init__( self, *attributeNames ):
        self.__attributeNames = attributeNames

    def apply( self, cls ):
        commonDefinition = BasicAttributes.AttributeDefinition( self.__attributeNames )
        for attributeName in self.__attributeNames:
            cls._addAttribute( attributeName, commonDefinition )

class ComplexAttribute:
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

    def apply( self, cls ):
        cls._addAttribute( self.__attributeName, ComplexAttribute.AttributeDefinition( self.__attributeName, self.__type ) )

class AttributeFromCallable:
    class AttributeDefinition:
        def __init__( self, name, callable ):
            self.__name = name
            self.__callable = callable

        def getValueFromRawValue( self, obj, rawValue ):
            return rawValue

        def updateAttributes( self, obj ):
            obj._updateAttributes( { self.__name: self.__callable( obj ) } )

    def __init__( self, name, callable ):
        self.__name = name
        self.__callable = callable

    def apply( self, cls ):
        cls._addAttribute( self.__name, AttributeFromCallable.AttributeDefinition( self.__name, self.__callable ) )

class BaseUrl( AttributeFromCallable ):
    def __init__( self, baseUrl ):
        AttributeFromCallable.__init__( self, "_baseUrl", baseUrl )

class Identity( AttributeFromCallable ):
    def __init__( self, identity ):
        AttributeFromCallable.__init__( self, "_identity", identity )

class ListOfReferences:
    def __init__( self, attributeName, type, addable = False, removable = False, hasable = False ):
        self.__attributeName = attributeName
        self.__type = type
        self.__getName = "get_" + attributeName
        if addable:
            self.__addName = "add_to_" + attributeName
        else:
            self.__addName = None
        if removable:
            self.__removeName = "remove_from_" + attributeName
        else:
            self.__removeName = None
        if hasable:
            self.__hasName = "has_in_" + attributeName
        else:
            self.__hasName = None

    def apply( self, cls ):
        cls._addMethod( self.__getName, self.__executeGet )
        if self.__addName is not None:
            cls._addMethod( self.__addName, self.__executeAdd )
        if self.__removeName is not None:
            cls._addMethod( self.__removeName, self.__executeRemove )
        if self.__hasName is not None:
            cls._addMethod( self.__hasName, self.__executeHas )

    def __executeGet( self, obj ):
        return [
            self.__type( obj._github, attributes, lazy = True )
            for attributes in obj._github._dataRequest( "GET", obj._baseUrl + "/" + self.__attributeName )
        ]

    def __executeAdd( self, obj, toBeAdded ):
        assert( isinstance( toBeAdded, self.__type ) )
        obj._github._statusRequest( "PUT", obj._baseUrl + "/" + self.__attributeName + "/" + toBeAdded._identity )

    def __executeRemove( self, obj, toBeDeleted ):
        assert( isinstance( toBeDeleted, self.__type ) )
        obj._github._statusRequest( "DELETE", obj._baseUrl + "/" + self.__attributeName + "/" + toBeDeleted._identity )

    def __executeHas( self, obj, toBeQueried ):
        assert( isinstance( toBeQueried, self.__type ) )
        return obj._github._statusRequest( "GET", obj._baseUrl + "/" + self.__attributeName + "/" + toBeQueried._identity ) == 204

class ListOfObjects:
    def __init__( self, attributeName, type, creatable = False, singularName = None ):
        self.__attributeName = attributeName
        self.__type = type
        self.__getName = "get_" + attributeName
        if creatable:
            self.__createName = "create_" + ( singularName or attributeName )
        else:
            self.__createName = None

    def apply( self, cls ):
        cls._addMethod( self.__getName, self.__executeGet )
        if self.__createName is not None:
            cls._addMethod( self.__createName, self.__executeCreate )

    def __executeGet( self, obj ):
        return [
            self.__type( obj._github, attributes, lazy = True )
            for attributes in obj._github._dataRequest( "GET", obj._baseUrl + "/" + self.__attributeName )
        ]

    def __executeCreate( self, obj, **data ):
        return self.__type( obj._github, obj._github._dataRequest( "POST", obj._baseUrl + "/" + self.__attributeName, data ), lazy = True )

class Editable:
    def __init__( self, mandatoryParameters, optionalParameters ):
        self.__mandatoryParameters = mandatoryParameters
        self.__optionalParameters = optionalParameters

    def apply( self, cls ):
        cls._addMethod( "edit", self.__execute )

    def __execute( self, obj, *args, **kwds ):
        if len( args ) + len( kwds ) == 0:
            raise TypeError()
        for arg, argumentName in itertools.izip( args, itertools.chain( self.__mandatoryParameters, self.__optionalParameters ) ):
            kwds[ argumentName ] = arg
        for argumentName in kwds:
            if argumentName not in itertools.chain( self.__mandatoryParameters, self.__optionalParameters ):
                raise TypeError()
        attributes = obj._github._dataRequest( "PATCH", obj._baseUrl, kwds )
        obj._updateAttributes( attributes )

class Deletable:
    def apply( self, cls ):
        cls._addMethod( "delete", self.__execute )

    def __execute( self, obj, *args, **kwds ):
        obj._github._statusRequest( "DELETE", obj._baseUrl )

class MethodFromCallable:
    def __init__( self, name, callable ):
        self.__name = name
        self.__callable = callable

    def apply( self, cls ):
        cls._addMethod( self.__name, self.__callable )

def GithubObject( className, *attributePolicies ):
    class GithubObject:
        __attributeDefinitions = dict()
        __methodDefinitions = dict()

        @staticmethod
        def _addAttributePolicies( attributePolicies ):
            for attributePolicy in attributePolicies:
                GithubObject._addAttributePolicy( attributePolicy )

        @staticmethod
        def _addAttributePolicy( attributePolicy ):
            attributePolicy.apply( GithubObject )

        @staticmethod
        def _addAttribute( attributeName, attributeDefinition ):
            if attributeName in GithubObject.__attributeDefinitions:
                raise BadGithubObjectException( "Same attribute defined by two policies" )
            else:
                GithubObject.__attributeDefinitions[ attributeName ] = attributeDefinition

        @staticmethod
        def _addMethod( methodName, methodDefinition ):
            if methodName in GithubObject.__methodDefinitions:
                raise BadGithubObjectException( "Same method defined by two policies" )
            else:
                GithubObject.__methodDefinitions[ methodName ] = methodDefinition

        def __init__( self, github, attributes, lazy ):
            self._github = github
            self.__attributes = dict()
            self._updateAttributes( attributes )
            if not lazy:
                for attributeName in GithubObject.__attributeDefinitions:
                    if attributeName not in self.__attributes:
                        self.__fetchAttribute( attributeName )

        def __getattr__( self, attributeName ):
            if attributeName in GithubObject.__methodDefinitions:
                return lambda *args, **kwds: GithubObject.__methodDefinitions[ attributeName ]( self, *args, **kwds )
            elif attributeName in GithubObject.__attributeDefinitions:
                if attributeName not in self.__attributes:
                    self.__fetchAttribute( attributeName )
                return self.__attributes[ attributeName ]
            else:
                raise AttributeError( attributeName )

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
    GithubObject._addAttributePolicies( attributePolicies )

    return GithubObject
