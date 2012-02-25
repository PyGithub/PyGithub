import itertools

import ObjectCapacities.ArgumentsChecker as ArgumentsChecker
from ObjectCapacities.Basic import AttributeFromCallable, MethodFromCallable
from ObjectCapacities.List import ListAttribute, ListGetable, ElementCreatable, ElementGetable, ElementAddable, ElementRemovable, ElementHasable, ListAddable, ListSetable, ListDeletable
from TypePolicies import SimpleTypePolicy, ObjectTypePolicy

class BadGithubObjectException( Exception ):
    pass

class InternalAttribute:
    class AttributeDefinition:
        def __init__( self, typePolicy ):
            self.__typePolicy = typePolicy

        def getValueFromRawValue( self, obj, rawValue ):
			if rawValue is None:
				return None
			else:
				return self.__typePolicy.create( obj, rawValue )

        def updateAttributes( self, obj ):
            attributes = obj._github._dataRequest( "GET", obj._baseUrl, None, None )
            obj._updateAttributes( attributes )
            obj._markAsCompleted()

        def isLazy( self ):
            return True

    def __init__( self, attributeName, typePolicy ):
        self.__attributeName = attributeName
        self.__typePolicy = typePolicy

    def apply( self, cls ):
        cls._addAttribute( self.__attributeName, InternalAttribute.AttributeDefinition( self.__typePolicy ) )

class SeveralAttributes:
    def __init__( self, attributePolicies ):
        self.__attributePolicies = attributePolicies

    def apply( self, cls ):
        for attributePolicy in self.__attributePolicies:
            attributePolicy.apply( cls )

def InternalSimpleAttribute( attributeName ):
    return InternalAttribute( attributeName, SimpleTypePolicy() )

def InternalSimpleAttributes( *attributeNames ):
    return SeveralAttributes( [ InternalSimpleAttribute( attributeName ) for attributeName in attributeNames ] )

def InternalObjectAttribute( attributeName, type ):
    return InternalAttribute( attributeName, ObjectTypePolicy( type ) )

class BaseUrl( AttributeFromCallable ):
    def __init__( self, baseUrl ):
        AttributeFromCallable.__init__( self, "_baseUrl", baseUrl )

class Identity( AttributeFromCallable ):
    def __init__( self, identity ):
        AttributeFromCallable.__init__( self, "_identity", identity )

class Editable( MethodFromCallable ):
    def __init__( self, mandatoryParameters, optionalParameters ):
        MethodFromCallable.__init__( self, "edit", self.__execute )
        self.__argumentsChecker = ArgumentsChecker.ArgumentsChecker( mandatoryParameters, optionalParameters )

    def __execute( self, obj, *args, **kwds ):
        data = self.__argumentsChecker.check( args, kwds )
        attributes = obj._github._dataRequest( "PATCH", obj._baseUrl, None, data )
        obj._updateAttributes( attributes )

class Deletable( MethodFromCallable ):
    def __init__( self ):
        MethodFromCallable.__init__( self, "delete", self.__execute )

    def __execute( self, obj, *args, **kwds ):
        obj._github._statusRequest( "DELETE", obj._baseUrl, None, None )

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
