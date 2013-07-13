#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright  

# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import fnmatch
import os
import subprocess
import itertools


license = [
    "# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/",
    "",
    "# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License",
    "# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.",
    "",
    "# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of",
    "# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.",
    "",
    "# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.",
]


class PythonHeader:
    def fix(self, filename, lines):
        isExecutable = lines[0].startswith("#!")
        newLines = []

        if isExecutable:
            newLines.append("#!/usr/bin/env python")
        newLines.append("# -*- coding: utf-8 -*-")
        newLines.append("")

        # @todo add <> around mails
        # @todo add ############## Copyrights and license (add sections to the header)

        for year, name in sorted(listContributors(filename)):
            newLines.append("# Copyright " + year + " " + name)
        newLines.append("")

        for line in license:
            newLines.append(line)

        bodyLines = list(itertools.dropwhile(self.lineCanBeHeader, lines))

        if len(bodyLines) > 0:
            newLines.append("")
            if "import " not in bodyLines[0] and bodyLines[0] != '"""' and not bodyLines[0].startswith("##########"):
                newLines.append("")

            newLines += bodyLines

        return newLines

    def lineCanBeHeader(self, line):
        return (len(line) == 0 or line[0] == "#") and not line.startswith("##########")


class StandardHeader:
    def fix(self, filename, lines):
        newLines = []

        for year, name in sorted(listContributors(filename)):
            newLines.append("# Copyright " + year + " " + name)
        newLines.append("")

        for line in license:
            newLines.append(line)

        bodyLines = list(itertools.dropwhile(self.lineCanBeHeader, lines))

        if len(bodyLines) > 0:
            newLines.append("")
            newLines += bodyLines

        return newLines

    def lineCanBeHeader(self, line):
        return (len(line) == 0 or line[0] == "#") and not line.startswith("##########")


def listContributors(filename):
    contributors = set()
    for line in subprocess.check_output(["git", "log", "--format=format:%ad %an %ae", "--date=short", "--", filename]).split("\n"):
        year = line[0:4]
        name = line[11:]
        contributors.add((year, name))
    return contributors


def findHeadersAndFiles():
    for root, dirs, files in os.walk('.', topdown=True):
        if ".git" in dirs:
            dirs.remove(".git")

        for filename in files:
            fullname = os.path.join(root, filename)
            if filename.endswith(".py"):
                yield (PythonHeader(), fullname)
            elif filename in ["COPYING", "COPYING.LESSER"]:
                pass
            elif filename.endswith(".rst") or filename.endswith(".md"):
                pass
            elif filename == ".gitignore":
                yield (StandardHeader(), fullname)
            elif "ReplayData" in fullname:
                pass
            else:
                print "Don't know what to do with", filename


def main():
    for header, filename in findHeadersAndFiles():
        print "Analyzing", filename
        with open(filename) as f:
            lines = list(line.rstrip() for line in f)
        newLines = header.fix(filename, lines)
        if newLines != lines:
            print " => actually modifying", filename
            with open(filename, "w") as f:
                for line in newLines:
                    f.write(line + "\n")


if __name__ == "__main__":
    main()
