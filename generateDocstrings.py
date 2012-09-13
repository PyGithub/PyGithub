#!/usr/bin/env python

import subprocess
import glob
import re
import collections

class ClassDescription:
    def __init__( self ):
        self.properties = dict()
        self.methods = collections.OrderedDict()

class MethodDescription:
    def __init__( self, returnType ):
        self.verb = None
        self.url = None
        self.returnType = returnType
        self.parameters = collections.OrderedDict()

class Generator():
    privateClasses = [
        "PaginatedList",
        "PaginatedListBase",
        "GithubObject",
        "BasicGithubObject",
        "_NotSetType",
        "Requester",
    ]

    def getClassDocstring( self, className ):
        if className in self.privateClasses:
            return []
        else:
            return [
                "Please edit this generated docstring for class " + className + ".",
            ]

    def getMemberDocstring( self, className, memberName ):
        if className in self.privateClasses:
            return []
        elif className in self.classDescriptions:
            classDescription = self.classDescriptions[ className ]
            if memberName in classDescription.properties:
                return [
                    "Please edit this generated docstring for property " + className + "." + memberName + ".",
                    classDescription.properties[ memberName ]
                ]
            elif memberName in classDescription.methods:
                return [
                    "Please edit this generated docstring for method " + className + "." + memberName + ".",
                    "Calls " + ( classDescription.methods[ memberName ].verb or "WTF" ) + " " + ( classDescription.methods[ memberName ].url or "WTF" )
                ] + [
                    ":param " + parameterName + ": " + parameterType for parameterName, parameterType in classDescription.methods[ memberName ].parameters.items()
                ] + [
                    ":return: " + str( classDescription.methods[ memberName ].returnType )
                ]
            elif memberName.startswith( "_" ): # private member
                return []
            else:
                print "Unknown member", className, memberName
                return []
        else:
            print "Unknown class", className
            return []

    def __init__( self ):
        pass

    def run( self ):
        self.restoreSources()
        self.readReferenceOfClasses()
        self.readReferenceOfApis()
        self.generate()

    def restoreSources( self ):
        subprocess.check_call( [ "git", "checkout", "--", "github" ] )

    def readReferenceOfClasses( self ):
        self.classDescriptions = dict()
        with open( "doc/ReferenceOfClasses.md" ) as f:
            for line in f:
                line = line.rstrip()
                if line.startswith( "Class `" ):
                    className = line[ 7 : -1 ]
                    self.classDescriptions[ className ] = ClassDescription()
                if line.startswith( "*" ):
                    if "rate_limiting" in line:
                        self.classDescriptions[ className ].properties[ "rate_limiting" ] = "( int, int )"
                    elif "(" in line:
                        methodName, returnType = re.match( "^\* `(.*)\(.*\)`(?:: (.*))?$", line ).groups()
                        self.classDescriptions[ className ].methods[ methodName ] = MethodDescription( returnType )
                    else:
                        attributeName, attributeType = re.match( "^\* `(.*)`: (.*)$", line ).groups()
                        self.classDescriptions[ className ].properties[ attributeName ] = attributeType
                if line.startswith( "    *" ):
                    parameterName, parameterType = re.match( "^    \* `(.*)`: (.*)$", line ).groups()
                    self.classDescriptions[ className ].methods[ methodName ].parameters[ parameterName ] = parameterType

    def readReferenceOfApis( self ):
        with open( "doc/ReferenceOfApis.md" ) as f:
            for line in f:
                line = line.rstrip()
                if line.startswith( "API" ):
                    url = line[ 5 : -1 ]
                if line.startswith( "*" ) and line not in [ "* POST: see API `/markdown`", "* GET: Not implemented, see `Github.rate_limiting`" ]:
                    verb, methods = re.match( "^\* (.*): (.*)$", line ).groups()
                    for method in methods.split( " or " ):
                        className, methodName = re.match( "^`(.*)\.(.*)`", method ).groups()
                        self.classDescriptions[ className ].methods[ methodName ].verb = verb
                        self.classDescriptions[ className ].methods[ methodName ].url = url

    def generate( self ):
        for f in glob.glob( "github/*.py" ):
            self.generateForFile( f )

    def generateForFile( self, fileName ):
        self.writeLines( fileName, self.processLines( self.readLines( fileName ) ) )

    def processLines( self, lines ):
        nextDefIsStaticMethod = False
        nextDefIsClassMethod = False

        for line in lines:
            yield line
            if line.startswith( "class" ):
                className = re.match( "^class (.*?)(?:\(.*\))?:$", line ).group( 1 )
                for docStringLine in self.formatDocstring( "    ", self.getClassDocstring( className ) ):
                    yield docStringLine
            if line.startswith( "    def" ):
                if nextDefIsStaticMethod or nextDefIsClassMethod:
                    pass
                else:
                    memberName = re.match( "^    def (.*?)\( self.* \):$", line ).group( 1 )
                    for docStringLine in self.formatDocstring( "        ", self.getMemberDocstring( className, memberName ) ):
                        yield docStringLine

            nextDefIsStaticMethod = line == "    @staticmethod"
            nextDefIsClassMethod = line == "    @classmethod"

    def formatDocstring( self, indent, lines ):
        if len( lines ) != 0:
            yield indent + '"""'
            for docStringLine in lines:
                yield indent + docStringLine
            yield indent + '"""'
            yield ""

    def readLines( self, fileName ):
        with open( fileName ) as f:
            return list( line.rstrip() for line in f )

    def writeLines( self, fileName, lines ):
        with open( fileName, "wb" ) as f:
            for line in lines:
                f.write( line + "\n" )

if __name__ == "__main__":
    Generator().run()
