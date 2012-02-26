import itertools

from Basic import *
from TypePolicies import *
from ArgumentsChecker import *

class ListCapacity:
    def setList( self, attributeName, singularName, typePolicy ):
        self.attributeName = attributeName
        self.singularName = singularName
        self.safeAttributeName = attributeName.replace( "/", "_" )
        self.safeSingularName = singularName.replace( "/", "_" )
        self.typePolicy = typePolicy

class ElementAddable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "add_to_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, toBeAdded ):
        obj._github._statusRequest( "PUT", obj._baseUrl + "/" + self.attributeName + "/" + self.typePolicy.getIdentity( toBeAdded ), None, None )

class ElementRemovable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "remove_from_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, toBeDeleted ):
        obj._github._statusRequest( "DELETE", obj._baseUrl + "/" + self.attributeName + "/" + self.typePolicy.getIdentity( toBeDeleted ), None, None )

class ElementHasable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "has_in_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, toBeQueried ):
        return obj._github._statusRequest( "GET", obj._baseUrl + "/" + self.attributeName + "/" + self.typePolicy.getIdentity( toBeQueried ), None, None ) == 204

class ElementCreatable( ListCapacity ):
    def __init__( self, mandatoryParameters, optionalParameters, modifyAttributes = lambda obj, attributes: attributes ):
        self.__argumentsChecker = ArgumentsChecker( mandatoryParameters, optionalParameters )
        self.__modifyAttributes = modifyAttributes

    def apply( self, cls ):
        cls._addMethod( "create_" + self.singularName, self.__execute )

    def __execute( self, obj, *args, **kwds ):
        data = self.__argumentsChecker.check( args, kwds )
        return self.typePolicy.createLazy( obj, self.__modifyAttributes( obj, obj._github._dataRequest( "POST", obj._baseUrl + "/" + self.attributeName, None, data ) ) )

class ElementGetable( ListCapacity ):
    def __init__( self, mandatoryParameters, optionalParameters, objReferenceName = None ):
        self.__argumentsChecker = ArgumentsChecker( mandatoryParameters, optionalParameters )
        self.__objReferenceName = objReferenceName

    def apply( self, cls ):
        cls._addMethod( "get_" + self.singularName, self.__execute )

    def __execute( self, obj, *args, **kwds ):
        attributes = self.__argumentsChecker.check( args, kwds )
        if self.__objReferenceName is not None:
            attributes[ self.__objReferenceName ] = obj
        return self.typePolicy.createNonLazy( obj, attributes )

class SeveralElementsAddable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "add_to_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, *toBeAddeds ):
        obj._github._statusRequest( "POST", obj._baseUrl + "/" + self.attributeName, None, [ self.typePolicy.getIdentity( toBeAdded ) for toBeAdded in toBeAddeds ] )

class SeveralElementsRemovable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "remove_from_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, *toBeDeleteds ):
        obj._github._statusRequest( "DELETE", obj._baseUrl + "/" + self.attributeName, None, [ self.typePolicy.getIdentity( toBeDeleted ) for toBeDeleted in toBeDeleteds ] )

class ListGetable( ListCapacity ):
    def __init__( self, mandatoryParameters, optionalParameters, modifyAttributes = lambda obj, attributes: attributes ):
        self.__argumentsChecker = ArgumentsChecker( mandatoryParameters, optionalParameters )
        self.__modifyAttributes = modifyAttributes

    def apply( self, cls ):
        cls._addMethod( "get_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, *args, **kwds ):
        params = self.__argumentsChecker.check( args, kwds )
        return [
            self.typePolicy.createLazy( obj, self.__modifyAttributes( obj, attributes ) )
            for attributes in obj._github._dataRequest( "GET", obj._baseUrl + "/" + self.attributeName, params, None )
        ]

class ListSetable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "set_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, *toBeSets ):
        obj._github._statusRequest( "PUT", obj._baseUrl + "/" + self.attributeName, None, [ self.typePolicy.getIdentity( toBeSet ) for toBeSet in toBeSets ] )

class ListDeletable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "delete_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj ):
        obj._github._statusRequest( "DELETE", obj._baseUrl + "/" + self.attributeName, None, None )

def ExternalListOfObjects( attributeName, singularName, type, *capacities ):
    for capacity in capacities:
        capacity.setList( attributeName, singularName, ObjectTypePolicy( type ) )
    return SeveralAttributePolicies( capacities )

def ExternalListOfSimpleTypes( attributeName, singularName, *capacities ):
    for capacity in capacities:
        capacity.setList( attributeName, singularName, SimpleTypePolicy() )
    return SeveralAttributePolicies( capacities )
