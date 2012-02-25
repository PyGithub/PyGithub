import itertools

from Basic import SeveralAttributePolicies
import ArgumentsChecker

class ListCapacity:
    def setList( self, attributeName, type ):
        self.attributeName = attributeName
        self.safeAttributeName = attributeName.replace( "/", "_" )
        self.type = type

class ElementAddable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "add_to_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, toBeAdded ):
        assert isinstance( toBeAdded, self.type )
        obj._github._statusRequest( "PUT", obj._baseUrl + "/" + self.attributeName + "/" + toBeAdded._identity, None, None )

class ElementRemovable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "remove_from_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, toBeDeleted ):
        assert isinstance( toBeDeleted, self.type )
        obj._github._statusRequest( "DELETE", obj._baseUrl + "/" + self.attributeName + "/" + toBeDeleted._identity, None, None )

class ElementHasable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "has_in_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, toBeQueried ):
        assert isinstance( toBeQueried, self.type )
        return obj._github._statusRequest( "GET", obj._baseUrl + "/" + self.attributeName + "/" + toBeQueried._identity, None, None ) == 204

class ElementCreatable( ListCapacity ):
    def __init__( self, singularName, mandatoryParameters, optionalParameters, modifyAttributes = lambda obj, attributes: attributes ):
        self.__argumentsChecker = ArgumentsChecker.ArgumentsChecker( mandatoryParameters, optionalParameters )
        self.__createName = "create_" + singularName
        self.__modifyAttributes = modifyAttributes

    def apply( self, cls ):
        cls._addMethod( self.__createName, self.__execute )

    def __execute( self, obj, *args, **kwds ):
        data = self.__argumentsChecker.check( args, kwds )
        return self.type( obj._github, self.__modifyAttributes( obj, obj._github._dataRequest( "POST", obj._baseUrl + "/" + self.attributeName, None, data ) ), lazy = True )

class ElementGetable( ListCapacity ):
    def __init__( self, singularName, attributes ):
        self.__getName = "get_" + singularName
        self.__attributes = attributes

    def apply( self, cls ):
        cls._addMethod( self.__getName, self.__execute )

    def __execute( self, obj, *args, **kwds ):
        return self.type( obj._github, self.__attributes( obj, *args, **kwds ), lazy = False )

class ListGetable( ListCapacity ):
    def __init__( self, mandatoryParameters, optionalParameters, modifyAttributes = lambda obj, attributes: attributes ):
        self.__argumentsChecker = ArgumentsChecker.ArgumentsChecker( mandatoryParameters, optionalParameters )
        self.__modifyAttributes = modifyAttributes

    def apply( self, cls ):
        cls._addMethod( "get_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, *args, **kwds ):
        params = self.__argumentsChecker.check( args, kwds )
        return [
            self.type( obj._github, self.__modifyAttributes( obj, attributes ), lazy = True )
            for attributes in obj._github._dataRequest( "GET", obj._baseUrl + "/" + self.attributeName, params, None )
        ]

class ListAddable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "add_to_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, *toBeAddeds ):
        for toBeAdded in toBeAddeds:
            assert isinstance( toBeAdded, self.type )
        obj._github._statusRequest( "POST", obj._baseUrl + "/" + self.attributeName, None, [ toBeAdded._identity for toBeAdded in toBeAddeds ] )

class ListSetable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "set_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, *toBeSets ):
        for toBeSet in toBeSets:
            assert isinstance( toBeSet, self.type )
        obj._github._statusRequest( "PUT", obj._baseUrl + "/" + self.attributeName, None, [ toBeSet._identity for toBeSet in toBeSets ] )

class ListDeletable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "delete_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj ):
        obj._github._statusRequest( "DELETE", obj._baseUrl + "/" + self.attributeName, None, None )

def ExternalListOfObjects( attributeName, type, *capacities ):
    for capacity in capacities:
        capacity.setList( attributeName, type )
    return SeveralAttributePolicies( capacities )
