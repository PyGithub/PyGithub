#!/bin/env python

import os.path
import json
import itertools

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
        self.cardinality = desc[ "cardinality" ]
        self.name = desc[ "name" ]

class Variable:
    def __init__( self, desc ):
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
            self.methods.append( Function( desc[ "get_element" ], { "name": [ "get", desc[ "singular_name" ] ], "type": desc[ "type" ], "group": desc[ "name" ] } ) )
        if "get_list" in desc:
            self.methods.append( Function(
                desc[ "get_list" ] if desc[ "get_list" ] is not True else dict(),
                { "name": [ "get" ] + name, "type": { "cardinality": "list", "name": desc[ "type" ] }, "group": desc[ "name" ] },
                { "request": {
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
            self.methods.append( Function( desc[ "edit" ], { "name": [ "edit" ], "type": "void", "group": "modification" } ) )
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

# def normalizeTypes( description ):
    # for class_ in description[ "classes" ]:
        # for subObject in itertools.chain( class_[ "collections" ], class_[ "attributes" ] ):
            # subObject[ "type" ] = normalizeType( subObject[ "type" ] )
        # if "additional_methods" in class_:
            # for subObject in class_[ "additional_methods" ]:
                # subObject[ "type" ] = normalizeType( subObject[ "type" ] )

# def normalizeType( type ):
    # def isSimple( typeName ):
        # return typeName in [ "string", "integer", "bool", "float", "@todo" ]
    # if isinstance( type, ( str, unicode ) ):
        # return {
            # "cardinality": "scalar",
            # "simple": isSimple( type ),
            # "name": type,
        # }
    # else:
        # type[ "simple" ] = isSimple( type[ "name" ] )
        # return type

# def normalizeFunction( function ):
    # if "mandatory_parameters" not in function:
        # function[ "mandatory_parameters" ] = []
    # if "optional_parameters" not in function:
        # function[ "optional_parameters" ] = []
    # if "automatic_parameters" not in function:
        # function[ "automatic_parameters" ] = []

# def normalizeFunctions( description ):
    # for class_ in description[ "classes" ]:
        # if "edit" in class_:
            # normalizeFunction( class_[ "edit" ] )
        # if "delete" in class_:
            # if class_[ "delete" ] is True:
                # class_[ "delete" ] = {}
            # normalizeFunction( class_[ "delete" ] )
        # for collection in class_[ "collections" ]:
            # def completeImplicitFunction( name, explicitDefinition ):
                # if name in collection and collection[ name ] is True:
                    # collection[ name ] = explicitDefinition

            # completeImplicitFunction( "get_list",
                # {}
            # )
            # completeImplicitFunction( "delete_list",
                # {}
            # )
            # completeImplicitFunction( "add_element",
                # { "mandatory_parameters": [ { "name": collection[ "singular_name" ], "type": collection[ "type" ][ "name" ] } ] }
            # )
            # completeImplicitFunction( "remove_element",
                # { "mandatory_parameters": [ { "name": collection[ "singular_name" ], "type": collection[ "type" ][ "name" ] } ] }
            # )
            # completeImplicitFunction( "has_element",
                # { "mandatory_parameters": [ { "name": collection[ "singular_name" ], "type": collection[ "type" ][ "name" ] } ] }
            # )

            # for function in [ "get_list", "delete_list", "has_element", "get_element", "add_element", "remove_element", "create_element" ]:
                # if function in collection:
                    # normalizeFunction( collection[ function ] )

# def normalizeAttributes( description ):
    # for class_ in description[ "classes" ]:
        # for attribute in class_[ "attributes" ]:
            # if "mandatory" not in attribute:
                # attribute[ "mandatory" ] = False
            # if "identifying" not in attribute:
                # attribute[ "identifying" ] = False

# def gatherDependencies( description ):
    # for class_ in description[ "classes" ]:
        # dependencies = set()
        # for subObject in itertools.chain( class_[ "collections" ], class_[ "attributes" ] ):
            # if not subObject[ "type" ][ "simple" ]:
                # if subObject[ "type" ][ "name" ] != class_[ "name" ]:
                    # dependencies.add( subObject[ "type" ][ "name" ] )
        # class_[ "dependencies" ] = list( dependencies )

# def generateMethodDescriptions( description ):
    # for class_ in description[ "classes" ]:
        # methods = list()
        # if "additional_methods" in class_:
            # for method in class_[ "additional_methods" ]:
                # methods.append( method )
        # for collection in class_[ "collections" ]:
            # if "get_list" in collection:
                # method = {
                    # "name": [ "get", collection[ "name" ] ],
                    # "group": collection[ "name" ],
                    # "type": { "cardinality": "list", "base": collection[ "type" ] },
                    # "request": {
                        # "verb": "GET",
                        # "url": [
                            # { "type": "attribute", "value": [ "url" ] },
                            # { "type": "constant", "value": "/" + collection[ "name" ] },
                        # ],
                    # },
                # }
            # methods.append( method )
        # class_[ "methods" ] = methods

# def checkDescription( description ):
    # def checkKeys( d, mandatory_keys, optional_keys = [] ):
        # assert set( d.keys() ) >= set( mandatory_keys ), d
        # assert set( d.keys() ) <= set( mandatory_keys ) | set( optional_keys ) | set( [ "@todo" ] ), d

    # def checkString( s ):
        # assert isinstance( s, ( str, unicode ) )

    # def checkBool( s ):
        # assert isinstance( s, bool )

    # def checkConcatenation( concatenation ):
        # for part in concatenation:
            # checkKeys( part, [ "type", "value" ] )
            # assert part[ "type" ] in [ "constant", "attribute" ]
            # if part[ "type" ] == "constant":
                # checkString( part[ "value" ] )
            # if part[ "type" ] == "attribute":
                # for level in part[ "value" ]:
                    # checkString( level )

    # def checkType( type ):
        # checkKeys( type, [ "simple", "name" ] )
        # checkBool( type[ "simple" ] )
        # checkString( type[ "name" ] )

    # def checkParameter( parameter ):
        # checkKeys( parameter, [ "name", "type" ], [ "values" ] )
        # checkString( parameter[ "name" ] )
        # checkString( parameter[ "type" ] )

    # def checkFunction( function ):
        # checkKeys( function, [ "mandatory_parameters", "optional_parameters" ], [ "automatic_parameters" ] )
        # for parameter in itertools.chain( function[ "mandatory_parameters" ], function[ "optional_parameters" ] ):
            # checkParameter( parameter )
        # if "automatic_parameters" in function:
            # for parameter in function[ "automatic_parameters" ]:
                # checkKeys( parameter, [ "name", "source" ] )
                # checkString( parameter[ "name" ] )
                # checkConcatenation( parameter[ "source" ] )

    # checkKeys( description, [ "classes" ] )
    # for class_ in description[ "classes" ]:
        # checkKeys( class_, [ "name", "dependencies", "collections", "attributes" ], [ "base_url", "identity", "edit", "delete" ] )
        # checkString( class_[ "name" ] )
        # for dependency in class_[ "dependencies" ]:
            # checkString( dependency )
        # for collection in class_[ "collections" ]:
            # functions = [ "get_list", "delete_list", "has_element", "get_element", "add_element", "remove_element", "create_element" ]
            # checkKeys( collection, [ "name", "singular_name", "type" ], [ "special_url", "add_several_elements", "remove_several_elements", "set_list" ] + functions )
            # checkString( collection[ "name" ] )
            # checkString( collection[ "singular_name" ] )
            # checkType( collection[ "type" ] )
            # if "special_url" in collection:
                # checkString( collection[ "special_url" ] )
            # for function in functions:
                # if function in collection:
                    # checkFunction( collection[ function ] )
            # if "add_several_elements" in collection:
                # checkBool( collection[ "add_several_elements" ] )
            # if "remove_several_elements" in collection:
                # checkBool( collection[ "remove_several_elements" ] )
            # if "set_list" in collection:
                # checkBool( collection[ "set_list" ] )
        # for attribute in class_[ "attributes" ]:
            # checkKeys( attribute, [ "name", "type", "mandatory", "identifying" ] )
            # checkString( attribute[ "name" ] )
            # checkType( attribute[ "type" ] )
            # checkBool( attribute[ "mandatory" ] )
            # checkBool( attribute[ "identifying" ] )
        # if "base_url" in class_:
            # checkConcatenation( class_[ "base_url" ] )
        # if "identity" in class_:
            # checkConcatenation( class_[ "identity" ] )
        # if "edit" in class_:
            # checkFunction( class_[ "edit" ] )
        # if "delete" in class_:
            # checkFunction( class_[ "delete" ] )
