import itertools

import ArgumentsChecker

class ElementAddable:
    def apply( self, list, cls ):
        self.__type = list.type
        self.__attributeName = list.attributeName
        cls._addMethod( "add_to_" + list.attributeName, self.__execute )

    def __execute( self, obj, toBeAdded ):
        assert isinstance( toBeAdded, self.__type )
        obj._github._statusRequest( "PUT", obj._baseUrl + "/" + self.__attributeName + "/" + toBeAdded._identity, None, None )

class ElementRemovable:
    def apply( self, list, cls ):
        self.__type = list.type
        self.__attributeName = list.attributeName
        cls._addMethod( "remove_from_" + list.attributeName, self.__execute )

    def __execute( self, obj, toBeDeleted ):
        assert isinstance( toBeDeleted, self.__type )
        obj._github._statusRequest( "DELETE", obj._baseUrl + "/" + self.__attributeName + "/" + toBeDeleted._identity, None, None )

class ElementHasable:
    def apply( self, list, cls ):
        self.__type = list.type
        self.__attributeName = list.attributeName
        cls._addMethod( "has_in_" + list.attributeName, self.__execute )

    def __execute( self, obj, toBeQueried ):
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
    def __init__( self, mandatoryParameters, optionalParameters ):
        self.__argumentsChecker = ArgumentsChecker.ArgumentsChecker( mandatoryParameters, optionalParameters )

    def apply( self, list, cls ):
        self.__type = list.type
        self.__attributeName = list.attributeName
        cls._addMethod( "get_" + list.attributeName, self.__execute )

    def __execute( self, obj, *args, **kwds ):
        params = self.__argumentsChecker.check( args, kwds )
        return [
            self.__type( obj._github, attributes, lazy = True )
            for attributes in obj._github._dataRequest( "GET", obj._baseUrl + "/" + self.__attributeName, params, None )
        ]

class ElementGetable:
    def __init__( self, singularName, attributes ):
        self.__getName = "get_" + singularName
        self.__attributes = attributes

    def apply( self, list, cls ):
        self.__type = list.type
        self.__attributeName = list.attributeName
        cls._addMethod( self.__getName, self.__execute )

    def __execute( self, obj, *args, **kwds ):
        return self.__type( obj._github, self.__attributes( obj, *args, **kwds ), lazy = False )

class ListOfObjects:
    def __init__( self, attributeName, type, *capacities ):
        self.attributeName = attributeName
        self.type = type
        self.__getName = "get_" + attributeName
        self.__capacities = capacities

    def apply( self, cls ):
        for capacity in self.__capacities:
            capacity.apply( self, cls )
