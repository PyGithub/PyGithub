import itertools

import ArgumentsChecker

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
        ### @todo ArgumentsChecker?
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

class ElementCreatable:
    def __init__( self, singularName, mandatoryParameters, optionalParameters ):
        self.__argumentsChecker = ArgumentsChecker.ArgumentsChecker( mandatoryParameters, optionalParameters )
        self.__createName = "create_" + singularName

    def apply( self, list, cls ):
        self.__type = list.type
        self.__attributeName = list.attributeName
        cls._addMethod( self.__createName, self.__execute )

    def __execute( self, obj, *args, **kwds ):
        data = self.__argumentsChecker.check( args, kwds )
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

class ElementGetable:
    def __init__( self, singularName ):
        self.__getName = "get_" + singularName

    def apply( self, list, cls ):
        self.__type = list.type
        self.__attributeName = list.attributeName
        cls._addMethod( self.__getName, self.__execute )

    def __execute( self, obj, identity ):
        return self.__type( obj._github, obj._github._dataRequest( "GET", obj._baseUrl + "/" + self.__attributeName + "/" + identity, None, None ), lazy = True )

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
