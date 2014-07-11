# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import os

import CodeGeneration.ApiDefinition.Typing as Typing
import CodeGeneration.CodeGenerator
import CodeGeneration.RstGenerator
import CodeGeneration.YmlGenerator


class Generator(object):
    def __init__(self, definition):
        self.__definition = definition
        self.codeGenerator = CodeGeneration.CodeGenerator.CodeGenerator()
        self.rstGenerator = CodeGeneration.RstGenerator.RstGenerator()
        self.ymlGenerator = CodeGeneration.YmlGenerator.YmlGenerator()

    def generate(self):
        self.__writeFile(self.rstGenerator.generateApis(self.__definition.endPoints), "doc/reference/apis.rst")
        self.__writeFile(self.ymlGenerator.generateEndpoints(self.__definition.endPoints), "ApiDefinition/end_points.yml")

        for klass in self.__definition.classes:
            self.__writeFile(self.rstGenerator.generateClass(klass), os.path.join("doc", "reference", "classes", klass.name + ".rst"))
            self.__writeFile(self.codeGenerator.generateClass(klass), os.path.join("PyGithub", "Blocking", klass.name + ".py"))
            self.__writeFile(self.ymlGenerator.generateClass(klass), os.path.join("ApiDefinition", "classes", klass.name + ".yml"))

    def __writeFile(self, content, output):
        content = list(content)

        outputDir = os.path.dirname(output)
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
            elif output.endswith(".yml"):
                pass  # Not really generated, just re-generated
            else:
                raise Exception("Unable to write the 'generated' warning")  # pragma no cover

            f.write("\n".join(content))
            if content[-1] != "":
                f.write("\n")
