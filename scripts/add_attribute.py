#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Thialfihar <thi@thialfihar.org>                               #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2018 bbi-yggy <yossarian@blackbirdinteractive.com>                 #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

import sys
import os.path

className, attributeName, attributeType = sys.argv[1:4]
if len(sys.argv) > 4:
    attributeClassType = sys.argv[4]
else:
    attributeClassType = ""


types = {
    "string": ("string", None, "self._makeStringAttribute(attributes[\"" + attributeName + "\"])"),
    "int": ("integer", None, "self._makeIntAttribute(attributes[\"" + attributeName + "\"])"),
    "bool": ("bool", None, "self._makeBoolAttribute(attributes[\"" + attributeName + "\"])"),
    "datetime": ("datetime.datetime", "(str, unicode)", "self._makeDatetimeAttribute(attributes[\"" + attributeName + "\"])"),
    "class": (":class:`" + attributeClassType + "`", None, "self._makeClassAttribute(" + attributeClassType + ", attributes[\"" + attributeName + "\"])"),
}

attributeDocType, attributeAssertType, attributeValue = types[attributeType]


fileName = os.path.join("github", className + ".py")

with open(fileName) as f:
    lines = list(f)

newLines = []

i = 0

added = False

isCompletable = True
isProperty = False
while not added:
    line = lines[i].rstrip()
    i += 1
    if line.startswith("class "):
        if "NonCompletableGithubObject" in line:
            isCompletable = False
    elif line == "    @property":
        isProperty = True
    elif line.startswith("    def "):
        attrName = line[8:-7]
        # Properties will be inserted after __repr__, but before any other function.
        if attrName != "__repr__" and (attrName == "_identity" or attrName > attributeName or not isProperty):
            if not isProperty:
                newLines.append("    @property")
            newLines.append("    def " + attributeName + "(self):")
            newLines.append("        \"\"\"")
            newLines.append("        :type: " + attributeDocType)
            newLines.append("        \"\"\"")
            if isCompletable:
                newLines.append("        self._completeIfNotSet(self._" + attributeName + ")")
            newLines.append("        return self._" + attributeName + ".value")
            newLines.append("")
            if isProperty:
                newLines.append("    @property")
            added = True
        isProperty = False
    newLines.append(line)

added = False

inInit = False
while not added:
    line = lines[i].rstrip()
    i += 1
    if line == "    def _initAttributes(self):":
        inInit = True
    if inInit:
        if not line or line.endswith(" = github.GithubObject.NotSet"):
            if line:
                attrName = line[14:-29]
            if not line or attrName > attributeName:
                newLines.append("        self._" + attributeName + " = github.GithubObject.NotSet")
                added = True
    newLines.append(line)

added = False

inUse = False
while not added:
    try:
        line = lines[i].rstrip()
    except IndexError:
        line = ""
    i += 1
    if line == "    def _useAttributes(self, attributes):":
        inUse = True
    if inUse:
        if not line or line.endswith(" in attributes:  # pragma no branch"):
            if line:
                attrName = line[12:-36]
            if not line or attrName > attributeName:
                newLines.append("        if \"" + attributeName + "\" in attributes:  # pragma no branch")
                if attributeAssertType:
                    newLines.append("            assert attributes[\"" + attributeName + "\"] is None or isinstance(attributes[\"" + attributeName + "\"], " + attributeAssertType + "), attributes[\"" + attributeName + "\"]")
                newLines.append("            self._" + attributeName + " = " + attributeValue)
                added = True
    newLines.append(line)


while i < len(lines):
    line = lines[i].rstrip()
    i += 1
    newLines.append(line)

with open(fileName, "wb") as f:
    for line in newLines:
        f.write(line + "\n")
