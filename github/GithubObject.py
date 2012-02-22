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
            attributes = obj._github._dataRequest( "GET", obj._baseUrl, None, None )
            obj._updateAttributes( attributes )
            obj._markAsCompleted()

        def isLazy( self ):
            return True

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
            attributes = obj._github._dataRequest( "GET", obj._baseUrl, None, None )
            obj._updateAttributes( attributes )
            obj._markAsCompleted()

        def isLazy( self ):
            return True

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

        def isLazy( self ):
            return False

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
    def __init__( self, attributeName, type, addable = False, removable = False, hasable = False, getParameters = [] ):
        self.__attributeName = attributeName
        self.__type = type
        self.__getName = "get_" + attributeName
        self.__getParameters = getParameters
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

    def __executeGet( self, obj, *args, **kwds ):
        for arg, argumentName in itertools.izip( args, self.__getParameters ):
            kwds[ argumentName ] = arg
        return [
            self.__type( obj._github, attributes, lazy = True )
            for attributes in obj._github._dataRequest( "GET", obj._baseUrl + "/" + self.__attributeName, kwds, None )
        ]

    def __executeAdd( self, obj, toBeAdded ):
        assert isinstance( toBeAdded, self.__type )
        obj._github._statusRequest( "PUT", obj._baseUrl + "/" + self.__attributeName + "/" + toBeAdded._identity, None, None )

    def __executeRemove( self, obj, toBeDeleted ):
        assert isinstance( toBeDeleted, self.__type )
        obj._github._statusRequest( "DELETE", obj._baseUrl + "/" + self.__attributeName + "/" + toBeDeleted._identity, None, None )

    def __executeHas( self, obj, toBeQueried ):
        assert isinstance( toBeQueried, self.__type )
        return obj._github._statusRequest( "GET", obj._baseUrl + "/" + self.__attributeName + "/" + toBeQueried._identity, None, None ) == 204

class Creatable:
    def __init__( self, singularName, mandatoryParameters, optionalParameters ):
        self.__createArgumentsChecker = _ArgumentsChecker( mandatoryParameters, optionalParameters )
        self.__createName = "create_" + singularName

    def apply( self, list, cls ):
        self.__type = list.type
        self.__attributeName = list.attributeName
        cls._addMethod( self.__createName, self.__execute )

    def __execute( self, obj, *args, **kwds ):
        data = self.__createArgumentsChecker.check( args, kwds )
        return self.__type( obj._github, obj._github._dataRequest( "POST", obj._baseUrl + "/" + self.__attributeName, None, data ), lazy = True )

class ListGetable:
    def apply( self, list, cls ):
        self.__type = list.type
        self.__attributeName = list.attributeName
        cls._addMethod( "get_" + list.attributeName, self.__execute )

    def __execute( self, obj ):
        return [
            self.__type( obj._github, attributes, lazy = True )
            for attributes in obj._github._dataRequest( "GET", obj._baseUrl + "/" + self.__attributeName, None, None )
        ]

### @todo Merge ObjectGetter in ListOfObjects, with a SingleGettable similar to Creatable
### @todo Add a ListGetable that couls be False for non-getable lists (repo/git/commits for example)
class ListOfObjects:
    def __init__( self, attributeName, type, *capacities ):
        self.attributeName = attributeName
        self.type = type
        self.__getName = "get_" + attributeName
        self.__capacities = list( capacities )
        self.__capacities.append( ListGetable() )

    def apply( self, cls ):
        for capacity in self.__capacities:
            capacity.apply( self, cls )

class MethodFromCallable:
    def __init__( self, name, callable ):
        self.__name = name
        self.__callable = callable

    def apply( self, cls ):
        cls._addMethod( self.__name, self.__callable )

class _ArgumentsChecker:
    def __init__( self, mandatoryParameters, optionalParameters ):
        self.__mandatoryParameters = mandatoryParameters
        self.__optionalParameters = optionalParameters

    def check( self, args, kwds ):
        data = dict( kwds )
        if len( args ) + len( kwds ) == 0:
            raise TypeError()
        for arg, argumentName in itertools.izip( args, itertools.chain( self.__mandatoryParameters, self.__optionalParameters ) ):
            if argumentName in kwds:
                raise TypeError()
            else:
                data[ argumentName ] = arg
        for argumentName in data:
            if argumentName not in itertools.chain( self.__mandatoryParameters, self.__optionalParameters ):
                raise TypeError()
        for argumentName in self.__mandatoryParameters:
            if argumentName not in data:
                raise TypeError()
        return data

class Editable( MethodFromCallable ):
    def __init__( self, mandatoryParameters, optionalParameters ):
        MethodFromCallable.__init__( self, "edit", self.__execute )
        self.__argumentsChecker = _ArgumentsChecker( mandatoryParameters, optionalParameters )

    def __execute( self, obj, *args, **kwds ):
        data = self.__argumentsChecker.check( args, kwds )
        attributes = obj._github._dataRequest( "PATCH", obj._baseUrl, None, data )
        obj._updateAttributes( attributes )

class Deletable( MethodFromCallable ):
    def __init__( self ):
        MethodFromCallable.__init__( self, "delete", self.__execute )

    def __execute( self, obj, *args, **kwds ):
        obj._github._statusRequest( "DELETE", obj._baseUrl, None, None )

class ObjectGetter( MethodFromCallable ):
    def __init__( self, singularName, type, attributes ):
        MethodFromCallable.__init__( self, "get_" + singularName, self.__execute )
        self.__attributes = attributes
        self.__type = type

    def __execute( self, obj, *args, **kwds ):
        return self.__type( obj._github, self.__attributes( obj, *args, **kwds ), lazy = False )

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
            GithubObject.__checkAttributeName( attributeName )
            GithubObject.__attributeDefinitions[ attributeName ] = attributeDefinition

        @staticmethod
        def _addMethod( methodName, methodDefinition ):
            GithubObject.__checkAttributeName( methodName )
            GithubObject.__methodDefinitions[ methodName ] = methodDefinition

        @staticmethod
        def __checkAttributeName( attributeName ):
            if attributeName in GithubObject.__attributeDefinitions or attributeName in GithubObject.__methodDefinitions:
                raise BadGithubObjectException( "Same attribute defined by two policies" )

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
                self.__attributes[ attributeName ] = attributeDefinition.getValueFromRawValue( self, attributeValue )

        def _markAsCompleted( self ):
            for attributeName, attributeDefinition in GithubObject.__attributeDefinitions.iteritems():
                if attributeDefinition.isLazy() and attributeName not in self.__attributes:
                    self.__attributes[ attributeName ] = None

        def __dir__( self ):
            return GithubObject.__attributeDefinitions.keys()

        def __fetchAttribute( self, attributeName ):
            attributeDefinition = GithubObject.__attributeDefinitions[ attributeName ]
            attributeDefinition.updateAttributes( self )

    GithubObject.__name__ = className
    GithubObject._addAttributePolicies( attributePolicies )

    return GithubObject
