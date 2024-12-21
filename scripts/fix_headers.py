#!/usr/bin/env python
############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2020 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Jonathan Leitschuh <jonathan.leitschuh@gmail.com>             #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
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

import os
import subprocess

eightySharps = "#" * 80


def generateLicenseSection(filename):
    yield "############################ Copyrights and license ############################"
    yield "#                                                                              #"
    for year, name in sorted(listContributors(filename)):
        line = "# Copyright " + year + " " + name
        line += (79 - len(line)) * " " + "#"
        yield line
    yield "#                                                                              #"
    yield "# This file is part of PyGithub.                                               #"
    yield "# http://pygithub.readthedocs.io/                                              #"
    yield "#                                                                              #"
    yield "# PyGithub is free software: you can redistribute it and/or modify it under    #"
    yield "# the terms of the GNU Lesser General Public License as published by the Free  #"
    yield "# Software Foundation, either version 3 of the License, or (at your option)    #"
    yield "# any later version.                                                           #"
    yield "#                                                                              #"
    yield "# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #"
    yield "# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #"
    yield "# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #"
    yield "# details.                                                                     #"
    yield "#                                                                              #"
    yield "# You should have received a copy of the GNU Lesser General Public License     #"
    yield "# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #"
    yield "#                                                                              #"
    yield "################################################################################"


def listContributors(filename):
    contributors = set()
    result = subprocess.check_output(
        ["git", "log", "--follow", "--format=format:%ad %an <%ae>", "--date=short", "--", filename],
        text=True,
    )
    for line in result.split("\n"):
        year = line[0:4]
        name = line[11:]
        contributors.add((year, name))
    return contributors


def extractBodyLines(lines):
    bodyLines = []

    seenEndOfHeader = False

    for line in lines:
        if len(line) > 0 and line[0] != "#":
            seenEndOfHeader = True
        if seenEndOfHeader:
            bodyLines.append(line)
        # else:
        #     print "HEAD:", line
        if line == eightySharps:
            seenEndOfHeader = True

    # print "BODY:", "\nBODY: ".join(bodyLines)

    return bodyLines


class PythonHeader:
    def fix(self, filename, lines):
        isExecutable = len(lines) > 0 and lines[0].startswith("#!")
        newLines = []

        if isExecutable:
            newLines.append("#!/usr/bin/env python")

        for line in generateLicenseSection(filename):
            newLines.append(line)

        bodyLines = extractBodyLines(lines)

        if len(bodyLines) > 0 and bodyLines[0] != "":
            newLines.append("")
            if "import " not in bodyLines[0] and bodyLines[0] != '"""' and not bodyLines[0].startswith("##########"):
                newLines.append("")
        newLines += bodyLines

        return newLines


class StandardHeader:
    def fix(self, filename, lines):
        newLines = []

        for line in generateLicenseSection(filename):
            newLines.append(line)

        bodyLines = extractBodyLines(lines)

        if len(bodyLines) > 0 and bodyLines[0] != "":
            newLines.append("")
        newLines += bodyLines

        return newLines


def findHeadersAndFiles():
    for root, dirs, files in os.walk(".", topdown=True):
        for dir in list(dirs):
            if dir.startswith("."):
                dirs.remove(dir)
        for excluded in ["developer.github.com", "build", "venv", "PyGithub.egg-info", "requirements", "pre-commit"]:
            if excluded in dirs:
                dirs.remove(excluded)

        for filename in files:
            fullname = os.path.join(root, filename)
            if filename == "GithubCredentials.py":
                pass
            elif filename.endswith(".py"):
                yield (PythonHeader(), fullname)
            elif filename in ["COPYING", "COPYING.LESSER", "MAINTAINERS"]:
                pass
            elif filename.endswith(".rst") or filename.endswith(".md"):
                pass
            elif filename == ".gitignore":
                yield (StandardHeader(), fullname)
            elif "ReplayData" in fullname:
                pass
            elif fullname.endswith(".pyi"):
                pass
            elif fullname.endswith(".pyc"):
                pass
            else:
                print(f"Don't know what to do with {filename} in {root}")


def main():
    for header, filename in findHeadersAndFiles():
        print("Analyzing", filename)
        with open(filename, encoding="utf-8") as f:
            lines = list(line.rstrip() for line in f)
        newLines = header.fix(filename, lines)
        if newLines != lines:
            print(" => actually modifying", filename)
            with open(filename, "w", encoding="utf-8") as f:
                for line in newLines:
                    f.write(line + "\n")


if __name__ == "__main__":
    main()
