#!/usr/bin/env python

import subprocess
import glob
import re
import collections


class ClassDescription:
    def __init__(self):
        self.properties = dict()
        self.methods = collections.OrderedDict()


class MethodDescription:
    def __init__(self, returnType):
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

    def getClassDocstring(self, className):
        if className in self.privateClasses:
            return None
        else:
            return [
                "This class represents " + className + "s as returned for example by http://developer.github.com/v3/todo"
            ]

    def getMemberDocstring(self, className, memberName):
        if className in self.privateClasses:
            return None
        elif className in self.classDescriptions:
            classDescription = self.classDescriptions[className]
            if memberName in classDescription.properties:
                return [
                    ":type: " + self.__formatType(classDescription.properties[memberName])
                ]
            elif memberName in classDescription.methods:
                return [
                    ":calls: `" + classDescription.methods[memberName].verb + " " + classDescription.methods[memberName].url + " <http://developer.github.com/v3/todo>`_",
                    # ":auth. level: ?",
                ] + [
                    ":param " + parameterName + ": " + self.__formatType(parameterType) for parameterName, parameterType in classDescription.methods[memberName].parameters.items()
                ] + [
                    ":rtype: " + self.__formatType(str(classDescription.methods[memberName].returnType))
                ]
            elif memberName.startswith("_"):  # private member
                return None
            else:
                print "Unknown member", className, memberName
                return None
        else:
            print "Unknown class", className
            return None

    def __formatType(self, type):
        if type.startswith("`PaginatedList` of "):
            return ":class:`github.PaginatedList.PaginatedList` of " + self.__formatType(type[19:])
        elif type.startswith("list of "):
            return "list of " + self.__formatType(type[8:])
        elif type.startswith("dict of string to "):
            return "dict of string to " + self.__formatType(type[18:])
        elif type.startswith("`") and type.endswith("`"):
            type = type[1:-1]
            return ":class:`github." + type + "." + type + "`"
        elif type == "`Milestone` or \"none\" or \"*\"":
            return ":class:`github.Milestone.Milestone` or \"none\" or \"*\""
        elif type == "`NamedUser` or \"none\" or \"*\"":
            return ":class:`github.NamedUser.NamedUser` or \"none\" or \"*\""
        elif type == "`Milestone` or None":
            return ":class:`github.Milestone.Milestone` or None"
        elif type == "`NamedUser` or None":
            return ":class:`github.NamedUser.NamedUser` or None"
        elif type in [
            "bool", "string", "None", "integer",
            "datetime.datetime", "date",
            "\"open\" or \"closed\"",
            "dict", "(int, int)"
        ]:
            return type
        else:
            raise Exception("Unknown type " + type)

    def __init__(self):
        pass

    def run(self):
        self.restoreSources()
        self.readReferenceOfClasses()
        self.readReferenceOfApis()
        self.generate()

    def restoreSources(self):
        subprocess.check_call(["git", "checkout", "--", "github"])

    def readReferenceOfClasses(self):
        self.classDescriptions = dict()
        with open("doc/ReferenceOfClasses.md") as f:
            for line in f:
                line = line.rstrip()
                if line.startswith("Class `"):
                    className = line[7:-1]
                    self.classDescriptions[className] = ClassDescription()
                if line.startswith("*"):
                    if "rate_limiting" in line:
                        self.classDescriptions[className].properties["rate_limiting"] = "(int, int)"
                    elif "(" in line:
                        methodName, returnType = re.match("^\* `(.*)\(.*\)`(?:: (.*))?$", line).groups()
                        self.classDescriptions[className].methods[methodName] = MethodDescription(returnType)
                    else:
                        attributeName, attributeType = re.match("^\* `(.*)`: (.*)$", line).groups()
                        self.classDescriptions[className].properties[attributeName] = attributeType
                if line.startswith("    *"):
                    parameterName, parameterType = re.match("^    \* `(.*)`: (.*)$", line).groups()
                    self.classDescriptions[className].methods[methodName].parameters[parameterName] = parameterType

    def readReferenceOfApis(self):
        with open("doc/ReferenceOfApis.md") as f:
            for line in f:
                line = line.rstrip()
                if line.startswith("API"):
                    url = line[5:-1]
                if line.startswith("*") and line not in ["* POST: see API `/markdown`", "* GET: Not implemented, see `Github.rate_limiting`"]:
                    verb, methods = re.match("^\* (.*): (.*)$", line).groups()
                    for method in methods.split(" or "):
                        className, methodName = re.match("^`(.*)\.(.*)`", method).groups()
                        self.classDescriptions[className].methods[methodName].verb = verb
                        self.classDescriptions[className].methods[methodName].url = url

    def generate(self):
        for f in glob.glob("github/*.py"):
            self.generateForFile(f)

    def generateForFile(self, fileName):
        self.writeLines(fileName, self.processLines(self.readLines(fileName)))

    def processLines(self, lines):
        nextDefIsStaticMethod = False
        nextDefIsClassMethod = False

        for line in lines:
            yield line
            if line.startswith("class"):
                className = re.match("^class (.*?)(?:\(.*\))?:$", line).group(1)
                for docStringLine in self.formatDocstring("    ", self.getClassDocstring(className), True):
                    yield docStringLine
            if line.startswith("    def"):
                if nextDefIsStaticMethod or nextDefIsClassMethod:
                    pass
                else:
                    assert re.match("^    def (.*?)\(self.*\):$", line), line
                    memberName = re.match("^    def (.*?)\(self.*\):$", line).group(1)
                    for docStringLine in self.formatDocstring("        ", self.getMemberDocstring(className, memberName)):
                        yield docStringLine

            nextDefIsStaticMethod = line == "    @staticmethod"
            nextDefIsClassMethod = line == "    @classmethod"

    def formatDocstring(self, indent, lines, addBlankLine=False):
        if lines is not None:
            yield indent + '"""'
            for docStringLine in lines:
                yield indent + docStringLine
            yield indent + '"""'
            if addBlankLine:
                yield ""

    def readLines(self, fileName):
        with open(fileName) as f:
            return list(line.rstrip() for line in f)

    def writeLines(self, fileName, lines):
        with open(fileName, "wb") as f:
            for line in lines:
                f.write(line + "\n")

if __name__ == "__main__":
    Generator().run()
