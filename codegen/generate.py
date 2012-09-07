#!/usr/bin/env python

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import os
import json
import itertools

import django.conf
import django.template
import django.template.loader

django.conf.settings.configure(
    TEMPLATE_DIRS = (
        os.path.join( os.path.dirname( __file__ ), "templates" ),
    ),
    TEMPLATE_STRING_IF_INVALID = "We have a logic error in our template or API description",
)

description = json.load( open( os.path.join( os.path.dirname( __file__ ), "JsonDescriptionOfGithubApiV3", "description.normalized.json" ) ) )

for class_ in description[ "classes" ]:
    dependencies = set()
    class_[ "needsPaginatedList" ] = False
    class_[ "needsDefaultValue" ] = False

    for method in class_[ "methods" ]:
        if method[ "type" ][ "cardinality" ] == "list":
            if not method[ "type" ][ "simple" ]:
                method[ "type" ][ "cardinality" ] = "iterator"
            class_[ "needsPaginatedList" ] = True
        if len( method[ "optionalParameters" ] ) != 0:
            class_[ "needsDefaultValue" ] = True
        if not method[ "type" ][ "simple" ]:
            dependencies.add( method[ "type" ][ "name" ] )
        for parameter in itertools.chain( method[ "mandatoryParameters" ], method[ "optionalParameters" ] ):
            if not parameter[ "type" ][ "simple" ]:
                dependencies.add( parameter[ "type" ][ "name" ] )

    for attribute in class_[ "attributes" ]:
        if not attribute[ "type" ][ "simple" ]:
            dependencies.add( attribute[ "type" ][ "name" ] )

    class_[ "dependencies" ] = list( dependencies )
    class_[ "needsUrllib" ] = class_[ "name" ] in [ "Label", "Repository" ]

githubObjectTemplate = django.template.loader.get_template( "GithubObject.py" )
for class_ in description[ "classes" ]:
    with open( os.path.join( os.path.dirname( __file__ ), "..", "github", class_[ "name" ] + ".py" ), "wb" ) as f:
        f.write( "# WARNING: this file is generated automaticaly.\n" )
        f.write( "# Do not modify it manually, your work would be lost.\n" )
        f.write( "\n" )
        rawCode = githubObjectTemplate.render( django.template.Context( { "class": class_ } ) ).split( "\n" )
        code = list()
        for line in rawCode:
            line = line.rstrip()
            if line == "":
                continue
            if len( code ) > 0 and code[ -1 ].startswith( "     " ) and line.startswith( "    " ) and not line.startswith( "     " ):
                code.append( "" )
            if line.startswith( "class" ):
                code.append( "" )
            if line == "##########":
                code.append( "" )
                continue
            code.append( line )
        f.write( "\n".join( code ) + "\n" )

referenceOfClassesTemplate = django.template.loader.get_template( "ReferenceOfClasses.md" )
with open( os.path.join( os.path.dirname( __file__ ), "..", "doc", "ReferenceOfClasses.md" ), "wb" ) as f:
    rawCode = referenceOfClassesTemplate.render( django.template.Context( description ) ).split( "\n" )
    code = list()
    for line in rawCode:
        line = line.rstrip()
        if line == "":
            continue
        if not line.lstrip().startswith( "*" ) and len( code ) > 0:
            prevLine = code[ -1 ].lstrip()
            if prevLine.startswith( "*" ) or prevLine.startswith( "=" ):
                code.append( "" )
        code.append( line )
    f.write( "\n".join( code ) + "\n" )
