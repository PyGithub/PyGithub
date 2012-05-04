#!/bin/env python

import os.path
import json
import itertools

def checkKeys( d, mandatory_keys, optional_keys = [] ):
    assert set( d.keys() ) >= set( mandatory_keys ), d.keys()
    assert set( d.keys() ) <= set( mandatory_keys ) | set( optional_keys ) | set( [ "@todo" ] ), d.keys()

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

    def __init__( self, desc, *additional_descs ):
        for additional_desc in additional_descs:
            desc.update( additional_desc )
        checkKeys( desc, [ "name", "type", "group" ], [ "mandatory_parameters", "optional_parameters", "variadic_parameter", "parameter", "request" ] ) # @todo Move request to mandatory_keys

        self.name = desc[ "name" ]
        self.type = Type( desc[ "type" ] )
        self.group = desc[ "group" ]
        self.mandatory_parameters = list()
        if "mandatory_parameters" in desc:
            for parameter in desc[ "mandatory_parameters" ]:
                self.mandatory_parameters.append( Variable( parameter ) )
        self.optional_parameters = list()
        if "optional_parameters" in desc:
            for parameter in desc[ "optional_parameters" ]:
                self.optional_parameters.append( Variable( parameter ) )
        if "variadic_parameter" in desc:
            self.variadic_parameter = Variable( desc[ "variadic_parameter" ] )
        else:
            self.variadic_parameter = None
        if "request" in desc:
            self.request = desc[ "request" ]
        else:
            self.request = None

    def ToJson( self ):
        json = {
            "name": self.name,
            "type": self.type,
            "group": self.group,
            "mandatory_parameters": self.mandatory_parameters,
            "optional_parameters": self.optional_parameters,
        }
        if self.variadic_parameter is not None:
            json[ "variadic_parameter" ] = self.variadic_parameter
        if self.request is not None:
            json[ "request" ] = self.request
        return json

class Collection:
    def __init__( self, desc ):
        checkKeys( desc, [ "name", "singular_name", "type" ], [ "add_element", "add_several_elements", "create_element", "delete_list", "get_element", "get_list", "has_element", "remove_element", "remove_several_elements", "set_list" ] )

        name = desc[ "name" ] if isinstance( desc[ "name" ], list ) else [ desc[ "name" ] ]
        self.methods = list()
        if "add_element" in desc:
            assert desc[ "add_element" ] is True
            self.methods.append( Function( { "name": [ "add", "to" ] + name, "type": "void", "group": desc[ "name" ], "mandatory_parameters": [ { "name": desc[ "singular_name" ], "type": desc[ "type" ] } ] } ) )
        if "add_several_elements" in desc:
            assert desc[ "add_several_elements" ] is True
            self.methods.append( Function( { "name": [ "add", "to" ] + name, "type": "void", "group": desc[ "name" ], "variadic_parameter": { "name": desc[ "singular_name" ], "type": desc[ "type" ] } } ) )
        if "create_element" in desc:
            self.methods.append( Function( desc[ "create_element" ], { "name": [ "create", desc[ "singular_name" ] ], "type": desc[ "type" ], "group": desc[ "name" ] } ) )
        if "delete_list" in desc:
            assert desc[ "delete_list" ] is True
            self.methods.append( Function( { "name": [ "delete" ] + name, "type": "void", "group": desc[ "name" ] } ) )
        if "get_element" in desc:

            # @todo Generalize
            if desc[ "name" ] == "repos":
                hack = {
                    "request": {
                        "verb": "GET",
                        "url": [
                            { "type": "constant", "value": "https://api.github.com/repos/" },
                            { "type": "attribute", "value": [ "login" ] },
                            { "type": "constant", "value": "/" },
                            { "type": "argument", "value": [ "name" ] },
                        ],
                    }
                }
            else:
                hack = dict()

            self.methods.append( Function(
                desc[ "get_element" ],
                { "name": [ "get", desc[ "singular_name" ] ], "type": desc[ "type" ], "group": desc[ "name" ], "mandatory_parameters": [ desc[ "get_element" ][ "parameter" ] ] },
                hack
            ) )
        if "get_list" in desc:
            self.methods.append( Function(
                desc[ "get_list" ] if desc[ "get_list" ] is not True else dict(),
                { "name": [ "get" ] + name, "type": { "cardinality": "list", "name": desc[ "type" ] }, "group": desc[ "name" ] },
                {
                    "request": {
                        "verb": "GET",
                        "url": [ { "type": "attribute", "value": [ "url" ] }, { "type": "constant", "value": "/" + desc[ "name" ] } ],
                    }
                }
            ) )
        if "has_element" in desc:
            assert desc[ "has_element" ] is True
            self.methods.append( Function( { "name": [ "has", "in" ] + name, "type": "bool", "group": desc[ "name" ], "mandatory_parameters": [ { "name": desc[ "singular_name" ], "type": desc[ "type" ] } ] } ) )
        if "remove_element" in desc:
            assert desc[ "remove_element" ] is True
            self.methods.append( Function( { "name": [ "remove", "from" ] + name, "type": "void", "group": desc[ "name" ], "mandatory_parameters": [ { "name": desc[ "singular_name" ], "type": desc[ "type" ] } ] } ) )
        if "remove_several_elements" in desc:
            assert desc[ "remove_several_elements" ] is True
            self.methods.append( Function( { "name": [ "remove", "from" ] + name, "type": "void", "group": desc[ "name" ], "variadic_parameter": { "name": desc[ "singular_name" ], "type": desc[ "type" ] } } ) )
        if "set_list" in desc:
            assert desc[ "set_list" ] is True
            self.methods.append( Function( { "name": [ "set" ] + name, "type": "void", "group": desc[ "name" ], "variadic_parameter": { "name": desc[ "singular_name" ], "type": desc[ "type" ] } } ) )

class Class:
    def __init__( self, desc ):
        checkKeys( desc, [ "name", "attributes", "collections" ], [ "edit", "delete", "additional_methods" ] )

        self.name = desc[ "name" ]
        self.attributes = sorted(
            [
                Variable( attr )
                for attr in desc[ "attributes" ]
            ],
            key = lambda class_: class_.name
        )
        self.methods = []
        if "edit" in desc:
            self.methods.append( Function(
                desc[ "edit" ],
                { "name": [ "edit" ], "type": "void", "group": "modification" },
                {
                    "request": {
                        "verb": "PATCH",
                        "url": [ { "type": "constant", "value": "https://api.github.com/user" } ], # @todo
                        "post_parameters": True, # @todo
                    },
                }
            ) )
        if "delete" in desc:
            self.methods.append( Function( { "name": [ "delete" ], "type": "void", "group": "deletion" } ) )
        for collection in [ Collection( collection ) for collection in desc[ "collections" ] ]:
            self.methods += collection.methods
        if "additional_methods" in desc:
            self.methods += [ Function( method ) for method in desc[ "additional_methods" ] ]

    def ToJson( self ):
        return {
            "name": self.name,
            "attributes": self.attributes,
            "methods": self.methods,
        }

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
