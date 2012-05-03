#!/bin/env python

import json

import django.conf
import django.template
import django.template.loader

django.conf.settings.configure(
    TEMPLATE_DIRS = (
        "CodeGenerator/templates",
    )
)

description = json.load( open( "JsonDescriptionOfGithubApiV3/description.001.normalized.json" ) )

githubObjectTemplate = django.template.loader.get_template( "GithubObject.py" )
for class_ in description[ "classes" ]:
    with open( "github/GithubObjects/" + class_[ "name" ] + ".py", "w" ) as f:
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
            code.append( line )
        f.write( "\n".join( code ) + "\n" )

referenceOfClassesTemplate = django.template.loader.get_template( "ReferenceOfClasses.md" )
with open( "ReferenceOfClasses.md", "w" ) as f:
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
