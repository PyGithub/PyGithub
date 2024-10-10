#!/usr/bin/env python
############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Thialfihar <thi@thialfihar.org>                               #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Yossarian King <yggy@blackbirdinteractive.com>                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Isac Souza <isouza@daitan.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2020 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2021 karsten-wagner <39054096+karsten-wagner@users.noreply.github.com>#
# Copyright 2022 Gabriele Oliaro <ict@gabrieleoliaro.it>                       #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Jonathan Leitschuh <jonathan.leitschuh@gmail.com>             #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Jacky Lam <jacky.lam@r2studiohk.com>                          #
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

from __future__ import annotations

import os.path
import sys

className, attributeName, attributeType = sys.argv[1:4]
if len(sys.argv) > 4:
    attributeClassType = sys.argv[4]
else:
    attributeClassType = ""

types = {
    "string": (
        "str",
        None,
        'self._makeStringAttribute(attributes["' + attributeName + '"])',
        "str",
    ),
    "int": (
        "int",
        None,
        'self._makeIntAttribute(attributes["' + attributeName + '"])',
        "int",
    ),
    "bool": (
        "bool",
        None,
        'self._makeBoolAttribute(attributes["' + attributeName + '"])',
        "bool",
    ),
    "datetime": (
        "datetime",
        "str",
        'self._makeDatetimeAttribute(attributes["' + attributeName + '"])',
        "datetime",
    ),
    "dict": (
        "dict[" + attributeClassType + "]",
        None,
        'self._makeDictAttribute(attributes["' + attributeName + '"])',
        "dict[" + attributeClassType + "]",
    ),
    "class": (
        ":class:`" + attributeClassType + "`",
        None,
        "self._makeClassAttribute(" + attributeClassType + ', attributes["' + attributeName + '"])',
        attributeClassType,
    ),
}

attributeDocType, attributeAssertType, attributeValue, attributeClassType = types[attributeType]
if attributeType == "class":
    # Wrap in quotes to avoid an explicit import requirement which can cause circular import errors
    attributeClassType = f"'{attributeClassType}'"

fileName = os.path.join("github", className + ".py")


def add_as_class_property(lines: list[str]) -> list[str]:
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
            if (not attrName.startswith("__repr__") and not attrName.startswith("_initAttributes")) and (
                attrName == "_identity" or attrName > attributeName or not isProperty
            ):
                if not isProperty:
                    newLines.append("    @property")
                newLines.append("    def " + attributeName + "(self) -> " + attributeClassType + ":")
                if isCompletable:
                    newLines.append("        self._completeIfNotSet(self._" + attributeName + ")")
                newLines.append("        return self._" + attributeName + ".value")
                newLines.append("")
                if isProperty:
                    newLines.append("    @property")
                added = True
            isProperty = False
        newLines.append(line)

    while i < len(lines):
        line = lines[i].rstrip()
        i += 1
        newLines.append(line)

    return newLines


def add_to_initAttributes(lines: list[str]) -> list[str]:
    newLines = []
    added = False

    i = 0
    inInit = False

    while not added:
        line = lines[i].rstrip()
        i += 1
        if line.strip().startswith("def _initAttributes(self)"):
            inInit = True
        if inInit:
            if not line or line.endswith(" = github.GithubObject.NotSet") or line.endswith(" = NotSet"):
                if line:
                    attrName = line[14:-29]
                if not line or attrName > attributeName:
                    newLines.append(f"        self._{attributeName}: Attribute[{attributeClassType}] = NotSet")
                    added = True
        newLines.append(line)

    while i < len(lines):
        line = lines[i].rstrip()
        i += 1
        newLines.append(line)

    return newLines


def add_to_useAttributes(lines: list[str]) -> list[str]:
    i = 0
    newLines = []
    added = False
    inUse = False
    while not added:
        try:
            line = lines[i].rstrip()
        except IndexError:
            line = ""
        i += 1
        if line.strip().startswith("def _useAttributes(self, attributes:"):
            inUse = True
        if inUse:
            if not line or line.endswith(" in attributes:  # pragma no branch"):
                if line:
                    attrName = line[12:-36]
                if not line or attrName > attributeName:
                    newLines.append('        if "' + attributeName + '" in attributes:  # pragma no branch')
                    if attributeAssertType:
                        newLines.append(
                            '            assert attributes["'
                            + attributeName
                            + '"] is None or isinstance(attributes["'
                            + attributeName
                            + '"], '
                            + attributeAssertType
                            + '), attributes["'
                            + attributeName
                            + '"]'
                        )
                    newLines.append(f"            self._{attributeName} = {attributeValue}")
                    added = True
        newLines.append(line)

    while i < len(lines):
        line = lines[i].rstrip()
        i += 1
        newLines.append(line)

    return newLines


with open(fileName) as f:
    source = f.readlines()

source = add_as_class_property(source)
source = add_to_initAttributes(source)
source = add_to_useAttributes(source)

with open(fileName, "w", newline="\n") as f:
    f.write("\n".join(source) + "\n")
