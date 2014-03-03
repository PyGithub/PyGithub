# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import CodeGeneration.ApiDefinition.Structured
import CodeGeneration.ApiDefinition.CrossReferenced
import CodeGeneration.Generator


def main():
    d = CodeGeneration.ApiDefinition.CrossReferenced.Definition(
        CodeGeneration.ApiDefinition.Structured.Definition("ApiDefinition")
    )

    CodeGeneration.Generator.Generator(d).generate()
