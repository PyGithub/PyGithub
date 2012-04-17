import itertools

from ArgumentsChecker import *
from Basic import *
from List import *
from TypePolicies import *

class BadGithubObjectException( Exception ):
    pass

def InternalSimpleAttribute( attributeName ):
    return InternalAttribute( attributeName, SimpleTypePolicy( None ) )

def InternalSimpleAttributes( *attributeNames ):
    return SeveralAttributePolicies( [ InternalSimpleAttribute( attributeName ) for attributeName in attributeNames ], "Attributes" )

def InternalObjectAttribute( attributeName, type ):
    return InternalAttribute( attributeName, ObjectTypePolicy( type ) )

def ExternalSimpleAttribute( attributeName, type ):
    return ExternalAttribute( attributeName, SimpleTypePolicy( type ) )

def BaseUrl( baseUrl ):
    return MethodFromCallable( "_baseUrl", NoParameters(), baseUrl, SimpleTypePolicy( None ) )

def Identity( identity ):
    return AttributeFromCallable( "_identity", identity )

def Editable( parameters ):
    def __execute( obj, **data ):
        attributes = obj._github._dataRequest( "PATCH", obj._baseUrl(), None, data )
        obj._updateAttributes( attributes )
    return SeveralAttributePolicies( [ MethodFromCallable( "edit", parameters, __execute, SimpleTypePolicy( None ) ) ], "Modification" )

def Deletable():
    def __execute( obj ):
        obj._github._statusRequest( "DELETE", obj._baseUrl(), None, None )
    return SeveralAttributePolicies( [ MethodFromCallable( "delete", NoParameters(), __execute, SimpleTypePolicy( None ) ) ], "Deletion" )

def GithubObject( className, *attributePolicies ):
    class GithubObject:
        __attributeDefinitions = dict()
        __methodDefinitions = dict()
        __attributePolicies = list()

        @staticmethod
        def _addAttributePolicy( attributePolicy ):
            GithubObject.__attributePolicies.append( attributePolicy )
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
                try:
                    attributeDefinition = GithubObject.__attributeDefinitions[ attributeName ]
                    self.__attributes[ attributeName ] = attributeDefinition.getValueFromRawValue( self, attributeValue )
                except KeyError:
                    self._github._printDebug( "Missing definition of attribute", attributeName, "in class", className )

        def _markAsCompleted( self ):
            for attributeName, attributeDefinition in GithubObject.__attributeDefinitions.iteritems():
                if attributeDefinition.isLazy() and attributeName not in self.__attributes:
                    self.__attributes[ attributeName ] = None

        def __dir__( self ):
            return GithubObject.__attributeDefinitions.keys()

        def __fetchAttribute( self, attributeName ):
            attributeDefinition = GithubObject.__attributeDefinitions[ attributeName ]
            attributeDefinition.updateAttributes( self )

        @classmethod
        def _autoDocument( cls ):
            doc = "Class `" + cls.__name__ + "`\n"
            doc += "=" * ( len( cls.__name__ ) + 8 ) + "\n"
            for attributePolicy in cls.__attributePolicies:
                doc += attributePolicy.autoDocument()
            doc += "\n"
            return doc

    GithubObject.__name__ = className
    GithubObject._addAttributePolicy( SeveralAttributePolicies( attributePolicies ) )

    return GithubObject
