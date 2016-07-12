#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.github.io/PyGithub/v1/index.html                             #
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
# ##############################################################################

import sys
import os.path

# This script is unable to add an attribute after all the existing ones
# but, well, I'll do it manually in that case.

className, attributeName, attributeType = sys.argv[1:]


types = {
    "string": ("string", "(str, unicode)", "attributes[\"" + attributeName + "\"]"),
    "int": ("integer", "(int, long)", "attributes[\"" + attributeName + "\"]"),
    "bool": ("bool", "bool", "attributes[\"" + attributeName + "\"]"),
    "float": ("float", "float", "attributes[\"" + attributeName + "\"]"),
    "datetime": ("datetime.datetime", "(str, unicode)", "self._parseDatetime(attributes[\"" + attributeName + "\"])"),
}

attributeDocType, attributeAssertType, attributeValue = types[attributeType]


fileName = os.path.join("github", className + ".py")

with open(fileName) as f:
    lines = list(f)

newLines = []

i = 0

added = False

isProperty = False
while not added:
    line = lines[i].rstrip()
    i += 1
    if line == "    @property":
        isProperty = True
    if line.startswith("    def "):
        if isProperty:
            attrName = line[8:-7]
            if attrName == "_identity" or attrName > attributeName:
                newLines.append("    def " + attributeName + "(self):")
                newLines.append("        \"\"\"")
                newLines.append("        :type: " + attributeDocType)
                newLines.append("        \"\"\"")
                newLines.append("        self._completeIfNotSet(self._" + attributeName + ")")
                newLines.append("        return self._NoneIfNotSet(self._" + attributeName + ")")
                newLines.append("")
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
    line = lines[i].rstrip()
    i += 1
    if line == "    def _useAttributes(self, attributes):":
        inUse = True
    if inUse:
        if not line or line.endswith(" in attributes:  # pragma no branch"):
            if line:
                attrName = line[12:-36]
            if not line or attrName > attributeName:
                newLines.append("        if \"" + attributeName + "\" in attributes:  # pragma no branch")
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
