import itertools

import ArgumentsChecker

class ElementAddable:
    def setList( self, list ):
        self.__type = list.type
        self.__attributeName = list.attributeName

    def apply( self, cls ):
        cls._addMethod( "add_to_" + self.__attributeName.replace( "/", "_" ), self.__execute )

    def __execute( self, obj, toBeAdded ):
        assert isinstance( toBeAdded, self.__type )
        obj._github._statusRequest( "PUT", obj._baseUrl + "/" + self.__attributeName + "/" + toBeAdded._identity, None, None )

class ElementRemovable:
    def setList( self, list ):
        self.__type = list.type
        self.__attributeName = list.attributeName

    def apply( self, cls ):
        cls._addMethod( "remove_from_" + self.__attributeName.replace( "/", "_" ), self.__execute )

    def __execute( self, obj, toBeDeleted ):
        assert isinstance( toBeDeleted, self.__type )
        obj._github._statusRequest( "DELETE", obj._baseUrl + "/" + self.__attributeName + "/" + toBeDeleted._identity, None, None )

class ElementHasable:
    def setList( self, list ):
        self.__type = list.type
        self.__attributeName = list.attributeName

    def apply( self, cls ):
        cls._addMethod( "has_in_" + self.__attributeName.replace( "/", "_" ), self.__execute )

    def __execute( self, obj, toBeQueried ):
        assert isinstance( toBeQueried, self.__type )
        return obj._github._statusRequest( "GET", obj._baseUrl + "/" + self.__attributeName + "/" + toBeQueried._identity, None, None ) == 204

class ElementCreatable:
    def __init__( self, singularName, mandatoryParameters, optionalParameters, modifyAttributes = lambda obj, attributes: attributes ):
        self.__argumentsChecker = ArgumentsChecker.ArgumentsChecker( mandatoryParameters, optionalParameters )
        self.__createName = "create_" + singularName
        self.__modifyAttributes = modifyAttributes

    def setList( self, list ):
        self.__type = list.type
        self.__attributeName = list.attributeName

    def apply( self, cls ):
        cls._addMethod( self.__createName, self.__execute )

    def __execute( self, obj, *args, **kwds ):
        data = self.__argumentsChecker.check( args, kwds )
        return self.__type( obj._github, self.__modifyAttributes( obj, obj._github._dataRequest( "POST", obj._baseUrl + "/" + self.__attributeName, None, data ) ), lazy = True )

class ElementGetable:
    def __init__( self, singularName, attributes ):
        self.__getName = "get_" + singularName
        self.__attributes = attributes

    def setList( self, list ):
        self.__type = list.type
        self.__attributeName = list.attributeName

    def apply( self, cls ):
        cls._addMethod( self.__getName, self.__execute )

    def __execute( self, obj, *args, **kwds ):
        return self.__type( obj._github, self.__attributes( obj, *args, **kwds ), lazy = False )

class ListGetable:
    def __init__( self, mandatoryParameters, optionalParameters, modifyAttributes = lambda obj, attributes: attributes ):
        self.__argumentsChecker = ArgumentsChecker.ArgumentsChecker( mandatoryParameters, optionalParameters )
        self.__modifyAttributes = modifyAttributes

    def setList( self, list ):
        self.__type = list.type
        self.__attributeName = list.attributeName

    def apply( self, cls ):
        cls._addMethod( "get_" + self.__attributeName.replace( "/", "_" ), self.__execute )

    def __execute( self, obj, *args, **kwds ):
        params = self.__argumentsChecker.check( args, kwds )
        return [
            self.__type( obj._github, self.__modifyAttributes( obj, attributes ), lazy = True )
            for attributes in obj._github._dataRequest( "GET", obj._baseUrl + "/" + self.__attributeName, params, None )
        ]

class ListAddable:
    def setList( self, list ):
        self.__type = list.type
        self.__attributeName = list.attributeName

    def apply( self, cls ):
        cls._addMethod( "add_to_" + self.__attributeName.replace( "/", "_" ), self.__execute )

    def __execute( self, obj, *toBeAddeds ):
        for toBeAdded in toBeAddeds:
            assert isinstance( toBeAdded, self.__type )
        obj._github._statusRequest( "POST", obj._baseUrl + "/" + self.__attributeName, None, [ toBeAdded._identity for toBeAdded in toBeAddeds ] )

class ListSetable:
    def setList( self, list ):
        self.__type = list.type
        self.__attributeName = list.attributeName

    def apply( self, cls ):
        cls._addMethod( "set_" + self.__attributeName.replace( "/", "_" ), self.__execute )

    def __execute( self, obj, *toBeSets ):
        for toBeSet in toBeSets:
            assert isinstance( toBeSet, self.__type )
        obj._github._statusRequest( "PUT", obj._baseUrl + "/" + self.__attributeName, None, [ toBeSet._identity for toBeSet in toBeSets ] )

class ListDeletable:
    def setList( self, list ):
        self.__type = list.type
        self.__attributeName = list.attributeName

    def apply( self, cls ):
        cls._addMethod( "delete_" + self.__attributeName.replace( "/", "_" ), self.__execute )

    def __execute( self, obj ):
        obj._github._statusRequest( "DELETE", obj._baseUrl + "/" + self.__attributeName, None, None )

### @todo use SeveralAttributes
class ExternalListOfObjects:
    def __init__( self, attributeName, type, *capacities ):
        self.attributeName = attributeName
        self.type = type
        self.__getName = "get_" + attributeName
        self.__capacities = capacities

    def apply( self, cls ):
        for capacity in self.__capacities:
            capacity.setList( self )
            capacity.apply( cls )
