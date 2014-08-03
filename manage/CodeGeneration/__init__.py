# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import sys
assert sys.hexversion >= 0x03040000

import CodeGeneration.ApiDefinition.Structured as Structured
import CodeGeneration.ApiDefinition.CrossReferenced as CrossReferenced
from CodeGeneration.ApiDefinition.Checker import Checker
from CodeGeneration.Generator import Generator


def main():
    structured = Structured.load("ApiDefinition")
    Structured.dump("ApiDefinition", structured)

    typesRepo = CrossReferenced.TypesRepository()
    for t in ["int", "bool", "string", "datetime", "list", "dict"]:
        typesRepo.register(CrossReferenced.BuiltinType(t))
    for t in ["Reset", "(string, string)", "GitAuthor"]:  # @todoAlpha Fix this: those are not builtins
        typesRepo.register(CrossReferenced.BuiltinType(t))
    for t in ["SessionedGithubObject", "UpdatableGithubObject", "PaginatedList"]:
        typesRepo.register(CrossReferenced.Class(t, None, (), (), (), ()))

    crossReferenced = CrossReferenced.Definition(structured, typesRepo)

    builder = CrossReferenced.Class("Builder", None, (), (), (Structured.Method("Build", (), (), (), Structured.EndPointValue(), (), (), (), (), None, Structured.ScalarType("Github")),), ())
    github = [c for c in crossReferenced.classes if c.simpleName == "Github"][0]
    github._addSource(CrossReferenced.MethodSource(builder.methods[0]))
    github._sortSources()

    session = CrossReferenced.Class("Session", None, (), (Structured.Attribute("RateLimit", Structured.ScalarType("RateLimits")),), (), ())
    rateLimits = [s for s in github.structures if s.qualifiedName == "Github.RateLimits"][0]
    rateLimits._addSource(CrossReferenced.AttributeSource(session.attributes[0]))
    rateLimits._sortSources()

    Checker(crossReferenced).check()
    Generator(crossReferenced).generate()
