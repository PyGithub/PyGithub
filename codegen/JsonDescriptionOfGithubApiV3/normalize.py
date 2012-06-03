#!/usr/bin/env python

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import os.path
import json
import itertools

def mergeDict( base, *additions ):
    r = dict( base )
    for addition in additions:
        for k in addition:
            if k in r:
                if isinstance( r[ k ], dict ):
                    r[ k ] = mergeDict( r[ k ], addition[ k ] )
                # else:
                    # we ignore the addition: the first dict which specifies a value wins
            else:
                r[ k ] = addition[ k ]
    return r

def checkKeys( d, mandatoryKeys, optionalKeys = [] ):
    assert set( d.keys() ) >= set( mandatoryKeys ), d.keys()
    assert set( d.keys() ) <= set( mandatoryKeys ) | set( optionalKeys ), d.keys()

class Type:
    def __init__( self, arg ):
        if isinstance( arg, ( str, unicode ) ):
            self.__fromString( arg )
        else:
            self.__fromDesc( arg )

    def ToJson( self ):
        json = {
            "cardinality": self.cardinality,
            "name": self.name,
            "simple": self.name in [ "void", "string", "integer", "bool", "float", "dict", "datetime", "date" ],
        }
        if self.keyName is not None:
            json[ "key_name" ] = self.keyName
        return json

    def __fromString( self, name ):
        listPrefix = "list:"
        dictPrefix = "dict:"
        self.keyName = None
        if name.startswith( listPrefix ):
            self.cardinality = "list"
            self.name = name[ len( listPrefix ) : ]
        elif name.startswith( dictPrefix ):
            self.cardinality = "dict"
            key, value = name[ len( dictPrefix ) : ].split( "-" )
            self.name = value
            self.keyName = key
        else:
            self.cardinality = "scalar"
            self.name = name

    def __fromDesc( self, desc ):
        checkKeys( desc, [ "cardinality", "name" ] )

        self.cardinality = desc[ "cardinality" ]
        self.name = desc[ "name" ]
        self.keyName = desc[ "key_name" ] if "key_name" in desc else None

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

    def __init__( self, *descs ):
        desc = mergeDict( *descs )
        checkKeys( desc, [ "name", "type", "group", "request" ], [ "url", "isMutation", "mandatoryParameters", "optionalParameters", "variadicParameter", "parameter", "request" ] )

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
        self.request = desc[ "request" ]
        self.__agregateRequestUrl()

    def __agregateRequestUrl( self ):
        url = list()
        for part in self.request[ "url" ]:
            if len( url ) != 0 and url[ -1 ][ "type" ] == "constant" and part[ "type" ] == "constant":
                url[ -1 ][ "value" ] += part[ "value" ]
            else:
                url.append( dict( part ) )
        self.request[ "url" ] = url

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
                            { "type": "identity", "value": [ desc[ "singularName" ] ] },
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
            self.methods.append( Function(
                { "name": [ "delete" ] + name, "type": "void", "group": desc[ "name" ] },
                {
                    "request": {
                        "verb": "DELETE",
                        "url": self.__url,
                        "information": "status",
                    }
                }
            ) )
        if "getElement" in desc:
            if "url" in desc[ "getElement" ]:
                urlForGetElement = desc[ "getElement" ][ "url" ]
            else:
                if desc[ "getElement" ][ "parameter" ][ "type" ] == "string":
                    partForArgument = { "type": "argument", "value": [ desc[ "getElement" ][ "parameter" ][ "name" ] ] }
                else:
                    partForArgument = { "type": "stringOf", "value": [ { "type": "argument", "value": [ desc[ "getElement" ][ "parameter" ][ "name" ] ] } ] }
                urlForGetElement = self.__url + [
                    { "type": "constant", "value": "/" },
                    partForArgument,
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
                            { "type": "identity", "value": [ desc[ "singularName" ] ] },
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
                            { "type": "identity", "value": [ desc[ "singularName" ] ] },
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
            self.methods.append( Function(
                { "name": [ "set" ] + name, "type": "void", "group": desc[ "name" ], "variadicParameter": { "name": desc[ "singularName" ], "type": desc[ "type" ] } },
                {
                    "request": {
                        "verb": "PUT",
                        "url": self.__url,
                        "information": "status",
                        "postParameters": True,
                    }
                }
            ) )

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
        self.isCompletable = ( "isCompletable" not in desc or desc[ "isCompletable" ] ) and any( attribute.name == "url" for attribute in self.attributes )
        self.methods = []
        if "identity" in desc:
            self.identity = desc[ "identity" ]
        else:
            self.identity = None
        if "url" in desc:
            url = desc[ "url" ]
        else:
            url = [ { "type": "attribute", "value": [ "url" ] } ]
        if "edit" in desc:
            self.methods.append( Function(
                desc[ "edit" ],
                { "name": [ "edit" ], "type": "void", "group": "modification", "isMutation": True },
                {
                    "request": {
                        "verb": "PATCH",
                        "url": url,
                        "postParameters": True,
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
                        "url": url,
                        "information": "data",
                    },
                }
            ) )
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

        with open( os.path.join( os.path.dirname( __file__ ), fileName ), "wb" ) as f:
            json.dump( self, f, indent = 4, cls = Encoder )

with open( os.path.join( os.path.dirname( __file__ ), "description.human_readable.json" ) ) as f:
    description = Description( json.load( f ) )

description.save( "description.normalized.json" )
