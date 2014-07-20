# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import sys
assert sys.hexversion >= 0x03040000

import os

import CodeGeneration.CodeGenerator
import CodeGeneration.RstGenerator


class Generator(object):
    def __init__(self, definition):
        self.__definition = definition
        self.codeGenerator = CodeGeneration.CodeGenerator.CodeGenerator()
        self.rstGenerator = CodeGeneration.RstGenerator.RstGenerator()

    def generate(self):
        self.__writeFile(self.rstGenerator.generateApis(self.__definition.endPoints), "doc/reference/apis.rst")

        for klass in self.__definition.classes:
            self.__writeFile(self.rstGenerator.generateClass(klass), os.path.join("doc", "reference", "classes", klass.name + ".rst"))
            self.__writeFile(self.codeGenerator.generateClass(klass), os.path.join("PyGithub", "Blocking", klass.name + ".py"))

    def __writeFile(self, content, output):
        content = list(content)  # To make sure all exceptions are raised before opening the file

        with open(output, "w") as f:
            if output.endswith(".py"):
                f.write("# -*- coding: utf-8 -*-\n")
                f.write("\n")
                f.write("# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>\n")
                f.write("\n")
                f.write("# ######################################################################\n")
                f.write("# #### This file is generated. Manual changes will likely be lost. #####\n")
                f.write("# ######################################################################\n")
                f.write("\n")
            elif output.endswith(".rst"):
                f.write(".. ########################################################################\n")
                f.write("   ###### This file is generated. Manual changes will likely be lost. #####\n")
                f.write("   ########################################################################\n")
                f.write("\n")
            else:
                raise Exception("Unable to write the 'generated' warning")  # pragma no cover

            f.write("\n".join(content))
            if content[-1] != "":
                f.write("\n")
