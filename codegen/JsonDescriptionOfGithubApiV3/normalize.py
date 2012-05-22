#!/bin/env python

import os.path
import json
import itertools

def checkKeys( d, mandatoryKeys, optionalKeys = [] ):
    assert set( d.keys() ) >= set( mandatoryKeys ), d.keys()
    assert set( d.keys() ) <= set( mandatoryKeys ) | set( optionalKeys ) | set( [ "@todo" ] ), d.keys()

class Type:
    def __init__( self, arg ):
        if isinstance( arg, ( str, unicode ) ):
            self.__fromString( arg )
        else:
            self.__fromDesc( arg )

    def ToJson( self ):
        return {
            "cardinality": self.cardinality,
            "name": self.name,
            "simple": self.name in [ "void", "string", "integer", "bool", "float", "@todo" ],
        }

    def __fromString( self, name ):
        listPrefix = "list:"
        if name.startswith( listPrefix ):
            self.cardinality = "list"
            self.name = name[ len( listPrefix ) : ]
        else:
            self.cardinality = "scalar"
            self.name = name

    def __fromDesc( self, desc ):
        checkKeys( desc, [ "cardinality", "name" ] )

        self.cardinality = desc[ "cardinality" ]
        self.name = desc[ "name" ]

class Variable:
    def __init__( self, desc ):
        checkKeys( desc, [ "name", "type" ] )

        self.name = desc[ "name" ]
        self.type = Type( desc[ "type" ] )

    def ToJson( self ):
        return {
            "name": self.name,
            "type": self.type,
        }

class Function:
    # method
        # input
            # self
            # arguments
        # output
            # type
                # bool
                # object
                # fundamental type
                # list of
                    # object
                    # fundamental type
        # body
            # status or data request
            # url from input
            # GET parameters from input
            # POST parameters from input

    def __init__( self, desc, *additionalDescs ):
        for additionalDesc in additionalDescs:
            desc.update( additionalDesc )
        checkKeys( desc, [ "name", "type", "group" ], [ "url", "isMutation", "mandatoryParameters", "optionalParameters", "variadicParameter", "parameter", "request" ] ) # @todo Move request to mandatoryKeys

        self.name = desc[ "name" ]
        self.type = Type( desc[ "type" ] )
        self.group = desc[ "group" ]
        self.isMutation = "isMutation" in desc and desc[ "isMutation" ]
        self.mandatoryParameters = list()
        if "mandatoryParameters" in desc:
            for parameter in desc[ "mandatoryParameters" ]:
                self.mandatoryParameters.append( Variable( parameter ) )
        self.optionalParameters = list()
        if "optionalParameters" in desc:
            for parameter in desc[ "optionalParameters" ]:
                self.optionalParameters.append( Variable( parameter ) )
        if "variadicParameter" in desc:
            self.variadicParameter = Variable( desc[ "variadicParameter" ] )
        else:
            self.variadicParameter = None
        if "request" in desc:
            self.request = desc[ "request" ]
        else:
            self.request = None

    def ToJson( self ):
        json = {
            "name": self.name,
            "type": self.type,
            "group": self.group,
            "isMutation": self.isMutation,
            "mandatoryParameters": self.mandatoryParameters,
            "optionalParameters": self.optionalParameters,
        }
        if self.variadicParameter is not None:
            json[ "variadicParameter" ] = self.variadicParameter
        if self.request is not None:
            json[ "request" ] = self.request
        return json

class Collection:
    def __init__( self, desc, ownerUrl ):
        checkKeys( desc, [ "name", "singularName", "type" ], [ "addElement", "addSeveralElements", "createElement", "deleteList", "getElement", "getList", "hasElement", "removeElement", "removeSeveralElements", "setList", "url" ] )

        if "url" in desc:
            self.__url = desc[ "url" ]
        else:
            self.__url = ownerUrl + [
                { "type": "constant", "value": "/" + desc[ "name" ] },
            ]

        name = desc[ "name" ] if isinstance( desc[ "name" ], list ) else [ desc[ "name" ] ]
        self.methods = list()
        if "addElement" in desc:
            assert desc[ "addElement" ] is True
            self.methods.append( Function(
                { "name": [ "add", "to" ] + name, "type": "void", "group": desc[ "name" ], "mandatoryParameters": [ { "name": desc[ "singularName" ], "type": desc[ "type" ] } ] },
                {
                    "request": {
                        "verb": "PUT",
                        "url": self.__url + [
                            { "type": "constant", "value": "/" },
                            { "type": "argument", "value": [ desc[ "singularName" ], "_identity" ] },
                        ],
                        "information": "status",
                    }
                }
            ) )
        if "addSeveralElements" in desc:
            assert desc[ "addSeveralElements" ] is True
            self.methods.append( Function(
                { "name": [ "add", "to" ] + name, "type": "void", "group": desc[ "name" ], "variadicParameter": { "name": desc[ "singularName" ], "type": desc[ "type" ] } },
                {
                    "request": {
                        "verb": "POST",
                        "url": self.__url,
                        "information": "status",
                        "postParameters": True
                    }
                }
            ) )
        if "createElement" in desc:
            self.methods.append( Function(
                desc[ "createElement" ],
                { "name": [ "create", desc[ "singularName" ] ], "type": desc[ "type" ], "group": desc[ "name" ] },
                {
                    "request": {
                        "verb": "POST",
                        "url": self.__url,
                        "information": "status",
                        "postParameters": True,
                    }
                }
            ) )
        if "deleteList" in desc:
            assert desc[ "deleteList" ] is True
            self.methods.append( Function( { "name": [ "delete" ] + name, "type": "void", "group": desc[ "name" ] } ) )
        if "getElement" in desc:
            if "url" in desc[ "getElement" ]:
                urlForGetElement = desc[ "getElement" ][ "url" ]
            else:
                urlForGetElement = self.__url + [
                    { "type": "constant", "value": "/" },
                    { "type": "argument", "value": [ desc[ "getElement" ][ "parameter" ][ "name" ] ] },
                ]

            self.methods.append( Function(
                desc[ "getElement" ],
                { "name": [ "get", desc[ "singularName" ] ], "type": desc[ "type" ], "group": desc[ "name" ], "mandatoryParameters": [ desc[ "getElement" ][ "parameter" ] ] },
                {
                    "request": {
                        "verb": "GET",
                        "url": urlForGetElement,
                        "information": "data",
                    }
                }
            ) )
        if "getList" in desc:
            self.methods.append( Function(
                desc[ "getList" ] if desc[ "getList" ] is not True else dict(),
                { "name": [ "get" ] + name, "type": { "cardinality": "list", "name": desc[ "type" ] }, "group": desc[ "name" ] },
                {
                    "request": {
                        "verb": "GET",
                        "url": self.__url,
                        "information": "data",
                    }
                }
            ) )
        if "hasElement" in desc:
            assert desc[ "hasElement" ] is True
            self.methods.append( Function(
                { "name": [ "has", "in" ] + name, "type": "bool", "group": desc[ "name" ], "mandatoryParameters": [ { "name": desc[ "singularName" ], "type": desc[ "type" ] } ] },
                {
                    "request": {
                        "verb": "GET",
                        "url": self.__url + [
                            { "type": "constant", "value": "/" },
                            { "type": "argument", "value": [ desc[ "singularName" ], "_identity" ] },
                        ],
                        "information": "status",
                    }
                }
            ) )
        if "removeElement" in desc:
            assert desc[ "removeElement" ] is True
            self.methods.append( Function(
                { "name": [ "remove", "from" ] + name, "type": "void", "group": desc[ "name" ], "mandatoryParameters": [ { "name": desc[ "singularName" ], "type": desc[ "type" ] } ] },
                {
                    "request": {
                        "verb": "DELETE",
                        "url": self.__url + [
                            { "type": "constant", "value": "/" },
                            { "type": "argument", "value": [ desc[ "singularName" ], "_identity" ] },
                        ],
                        "information": "status",
                    }
                }
            ) )
        if "removeSeveralElements" in desc:
            assert desc[ "removeSeveralElements" ] is True
            self.methods.append( Function(
                { "name": [ "remove", "from" ] + name, "type": "void", "group": desc[ "name" ], "variadicParameter": { "name": desc[ "singularName" ], "type": desc[ "type" ] } },
                {
                    "request": {
                        "verb": "DELETE",
                        "url": self.__url,
                        "information": "status",
                        "postParameters": True
                    }
                }
            ) )
        if "setList" in desc:
            assert desc[ "setList" ] is True
            self.methods.append( Function( { "name": [ "set" ] + name, "type": "void", "group": desc[ "name" ], "variadicParameter": { "name": desc[ "singularName" ], "type": desc[ "type" ] } } ) )

class Class:
    def __init__( self, desc ):
        checkKeys( desc, [ "name", "attributes" ], [ "isCompletable", "url", "identity", "edit", "delete", "additionalMethods", "collections" ] )

        self.name = desc[ "name" ]
        self.attributes = sorted(
            [
                Variable( attr )
                for attr in desc[ "attributes" ]
            ],
            key = lambda class_: class_.name
        )
        self.isCompletable = "isCompletable" in desc and desc[ "isCompletable" ]
        self.methods = []
        if "identity" in desc:
            self.identity = desc[ "identity" ]
        else:
            self.identity = None
        if "edit" in desc:
            self.methods.append( Function(
                desc[ "edit" ],
                { "name": [ "edit" ], "type": "void", "group": "modification", "isMutation": True },
                {
                    "request": {
                        "verb": "PATCH",
                        "url": [ { "type": "constant", "value": "https://api.github.com/user" } if desc[ "name" ] == "AuthenticatedUser" else { "type": "attribute", "value": [ "url" ] } ], # @todo
                        "postParameters": True, # @todo
                        "information": "data",
                    },
                }
            ) )
        if "delete" in desc:
            self.methods.append( Function(
                { "name": [ "delete" ], "type": "void", "group": "deletion" },
                {
                    "request": {
                        "verb": "DELETE",
                        "url": [ { "type": "attribute", "value": [ "url" ] } ],
                        "information": "data",
                    },
                }
            ) )
        if "url" in desc:
            url = desc[ "url" ]
        else:
            url = [ { "type": "attribute", "value": [ "url" ] } ]
        if "collections" in desc:
            for collection in [ Collection( collection, url ) for collection in desc[ "collections" ] ]:
                self.methods += collection.methods
        if "additionalMethods" in desc:
            self.methods += [ Function( method ) for method in desc[ "additionalMethods" ] ]

    def ToJson( self ):
        d = {
            "name": self.name,
            "attributes": self.attributes,
            "methods": self.methods,
            "isCompletable": self.isCompletable,
        }
        if self.identity is not None:
            d[ "identity" ] = self.identity
        return d

class Description:
    def __init__( self, desc ):
        checkKeys( desc, [ "classes" ] )

        self.classes = sorted(
            [
                Class( class_ )
                for class_ in desc[ "classes" ]
            ],
            key = lambda class_: class_.name
        )

    def ToJson( self ):
        return {
            "classes": self.classes,
        }

    def save( self, fileName ):
        class Encoder( json.JSONEncoder ):
            def default( self, obj ):
                if hasattr( obj, "ToJson" ):
                    return obj.ToJson()
                return json.JSONEncoder.default( self, obj )

        with open( os.path.join( os.path.dirname( __file__ ), fileName ), "w" ) as f:
            json.dump( self, f, indent = 4, cls = Encoder )

with open( os.path.join( os.path.dirname( __file__ ), "description.000.human_readable.json" ) ) as f:
    description = Description( json.load( f ) )

description.save( "description.001.normalized.json" )
