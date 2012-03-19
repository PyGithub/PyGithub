import itertools

from Basic import *
from TypePolicies import *
from ArgumentsChecker import *

class ListCapacity:
    def setList( self, attributeName, singularName, typePolicy, url = None ):
        self.attributeName = attributeName
        self.singularName = singularName
        self.safeAttributeName = attributeName.replace( "/", "_" )
        self.safeSingularName = singularName.replace( "/", "_" )
        self.typePolicy = typePolicy
        self.__url = url

    def baseUrl( self, obj ):
        if self.__url is None:
            return obj._baseUrl() + "/" + self.attributeName
        else:
            return self.__url

class ElementAddable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "add_to_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, toBeAdded ):
        obj._github._statusRequest(
            "PUT",
            self.baseUrl( obj ) + "/" + self.typePolicy.getIdentity( toBeAdded ),
            None,
            None
        )

    def autoDocument( self ):
        return "* `add_to_" + self.safeAttributeName + "( " + self.singularName + " )`\n    * `" + self.singularName + "`: " + self.typePolicy.documentTypeName() + "\n"

class ElementRemovable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "remove_from_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, toBeDeleted ):
        obj._github._statusRequest(
            "DELETE",
            self.baseUrl( obj ) + "/" + self.typePolicy.getIdentity( toBeDeleted ),
            None,
            None
        )

    def autoDocument( self ):
        return "* `remove_from_" + self.safeAttributeName + "( " + self.singularName + " )`\n    * `" + self.singularName + "`: " + self.typePolicy.documentTypeName() + "\n"

class ElementHasable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "has_in_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, toBeQueried ):
        return obj._github._statusRequest(
            "GET",
            self.baseUrl( obj ) + "/" + self.typePolicy.getIdentity( toBeQueried ),
            None,
            None
        ) == 204

    def autoDocument( self ):
        return "* `has_in_" + self.safeAttributeName + "( " + self.singularName + " )`: bool\n    * `" + self.singularName + "`: " + self.typePolicy.documentTypeName() + "\n"

class ListCapacityWithModifier( ListCapacity ):
    def __init__( self, attributeModifiers ):
        self.__attributeModifiers = attributeModifiers

    def _modifyAttributes( self, obj, attributes ):
        for attributeName, attributeModifier in self.__attributeModifiers.iteritems():
            attributes[ attributeName ] = attributeModifier( obj )
        return attributes

class ElementCreatable( ListCapacityWithModifier ):
    def __init__( self, parameters = NoParameters(), attributeModifiers = {} ):
        ListCapacityWithModifier.__init__( self, attributeModifiers )
        self.__argumentsChecker = parameters

    def apply( self, cls ):
        cls._addMethod( "create_" + self.singularName, self.__execute )

    def __execute( self, obj, *args, **kwds ):
        return self.typePolicy.createLazy(
            obj,
            self._modifyAttributes(
                obj,
                obj._github._dataRequest(
                    "POST",
                    self.baseUrl( obj ),
                    None,
                    self.__argumentsChecker.check( args, kwds )
                )
            )
        )

    def autoDocument( self ):
        return "* `create_" + self.singularName + "(" + self.__argumentsChecker.documentParameters() + ")`: " + self.typePolicy.documentTypeName() + "\n"

class ElementGetable( ListCapacityWithModifier ):
    def __init__( self, parameters = NoParameters(), attributeModifiers = {} ):
        ListCapacityWithModifier.__init__( self, attributeModifiers )
        self.__argumentsChecker = parameters

    def apply( self, cls ):
        cls._addMethod( "get_" + self.singularName, self.__execute )

    def __execute( self, obj, *args, **kwds ):
        return self.typePolicy.createNonLazy(
            obj,
            self._modifyAttributes(
                obj,
                self.__argumentsChecker.check( args, kwds )
            )
        )

    def autoDocument( self ):
        return "* `get_" + self.singularName + "(" + self.__argumentsChecker.documentParameters() + ")`: " + self.typePolicy.documentTypeName() + "\n"

class SeveralElementsAddable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "add_to_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, *toBeAddeds ):
        obj._github._statusRequest(
            "POST",
            self.baseUrl( obj ),
            None,
            [
                self.typePolicy.getIdentity( toBeAdded )
                for toBeAdded in toBeAddeds
            ]
        )

    def autoDocument( self ):
        return "* `add_to_" + self.safeAttributeName + "( " + self.singularName + ", ... )`\n    * `" + self.singularName + "`: " + self.typePolicy.documentTypeName() + "\n"

class SeveralElementsRemovable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "remove_from_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, *toBeDeleteds ):
        obj._github._statusRequest(
            "DELETE",
            self.baseUrl( obj ),
            None,
            [
                self.typePolicy.getIdentity( toBeDeleted )
                for toBeDeleted in toBeDeleteds
            ]
        )

    def autoDocument( self ):
        return "* `remove_from_" + self.safeAttributeName + "( " + self.singularName + ", ... )`\n    * `" + self.singularName + "`: " + self.typePolicy.documentTypeName() + "\n"

class ListGetable( ListCapacityWithModifier ):
    def __init__( self, parameters = NoParameters(), attributeModifiers = {} ):
        ListCapacityWithModifier.__init__( self, attributeModifiers )
        self.__argumentsChecker = parameters

    def apply( self, cls ):
        cls._addMethod( "get_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, *args, **kwds ):
        params = self.__argumentsChecker.check( args, kwds )
        return [
            self.typePolicy.createLazy(
                obj,
                self._modifyAttributes( obj, attributes )
            )
            for attributes in obj._github._dataRequest(
                "GET",
                self.baseUrl( obj ),
                params,
                None
            )
        ]

    def autoDocument( self ):
        return "* `get_" + self.safeAttributeName + "(" + self.__argumentsChecker.documentParameters() + ")`: list of " + self.typePolicy.documentTypeName() + "\n"

class ListSetable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "set_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj, *toBeSets ):
        obj._github._statusRequest(
            "PUT",
            self.baseUrl( obj ),
            None,
            [
                self.typePolicy.getIdentity( toBeSet )
                for toBeSet in toBeSets
            ]
        )

    def autoDocument( self ):
        return "* `set_" + self.safeAttributeName + "( " + self.singularName + ", ... )`\n    * `" + self.singularName + "`: " + self.typePolicy.documentTypeName() + "\n"

class ListDeletable( ListCapacity ):
    def apply( self, cls ):
        cls._addMethod( "delete_" + self.safeAttributeName, self.__execute )

    def __execute( self, obj ):
        obj._github._statusRequest(
            "DELETE",
            self.baseUrl( obj ),
            None,
            None
        )

    def autoDocument( self ):
        return "* `delete_" + self.safeAttributeName + "()`\n"

def ExternalListOfObjects( attributeName, singularName, type, *capacities, **kwds ):
    for capacity in capacities:
        capacity.setList( attributeName, singularName, ObjectTypePolicy( type ), **kwds )
    return SeveralAttributePolicies( capacities, attributeName.capitalize().replace( "_", " " ).replace( "/", " " ) )

def ExternalListOfSimpleTypes( attributeName, singularName, type, *capacities ):
    for capacity in capacities:
        capacity.setList( attributeName, singularName, SimpleTypePolicy( type ) )
    return SeveralAttributePolicies( capacities, attributeName.capitalize().replace( "_", " " ).replace( "/", " " ) )
