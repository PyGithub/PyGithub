# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import sys
assert sys.hexversion >= 0x03040000

import CodeGeneration.ApiDefinition.Structured as Structured
import CodeGeneration.ApiDefinition.CrossReferenced as CrossReferenced
import CodeGeneration.ApiDefinition.Typing as Typing
from CodeGeneration.ApiDefinition.Checker import Checker
from CodeGeneration.Generator import Generator


def main():
    structured = Structured.load("ApiDefinition")
    Structured.dump("ApiDefinition", structured)

    typesRepo = Typing.Repository()
    for t in ["int", "bool", "string", "datetime", "list", "dict"]:
        typesRepo.register(Typing.BuiltinType(t))
    for t in ["Reset", "(string, string)", "GitAuthor"]:  # @todoAlpha Fix this: those are not builtins
        typesRepo.register(Typing.BuiltinType(t))
    for t in ["SessionedGithubObject", "UpdatableGithubObject", "PaginatedList"]:
        typesRepo.register(CrossReferenced.Class(None, t, False, False, None, [], [], [], []))

    crossReferenced = CrossReferenced.Definition(structured, typesRepo)

    Checker(crossReferenced).check()
    Generator(crossReferenced).generate()
