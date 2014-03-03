# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import CodeGeneration.ApiDefinition.Typing as Typing


class ReturnStrategy(object):
    @property
    def name(self):
        name = self.__class__.__name__
        assert name.endswith("ReturnStrategy")
        return name[:-len("ReturnStrategy")]


class NoneReturnStrategy(ReturnStrategy):
    @property
    def returnType(self):
        return Typing.NoneType


class UpdateSelfReturnStrategy(ReturnStrategy):
    def __init__(self, then):
        self.__then = then

    @property
    def returnType(self):
        return self.__then.returnType


class BoolReturnStrategy(ReturnStrategy):
    @property
    def returnType(self):
        return Typing.BuiltinType("bool")


class InstanceReturnStrategy(ReturnStrategy):
    def __init__(self, type):
        self.__type = type

    @property
    def returnType(self):
        return self.__type


class StructureReturnStrategy(ReturnStrategy):
    def __init__(self, type):
        self.__type = type

    @property
    def returnType(self):
        return self.__type


# class ListFromDictItemsReturnStrategy(ReturnStrategy):
#     def __init__(self, type):
#         self.__type = type

#     @property
#     def returnType(self):
#         return Typing.LinearCollection(Typing.BuiltinType("list"), self.__type)


class ListOfReturnStrategy(ReturnStrategy):
    def __init__(self, type):
        self.__type = type

    @property
    def returnType(self):
        return Typing.LinearCollection(Typing.BuiltinType("list"), self.__type)


class PaginatedListReturnStrategy(ReturnStrategy):
    def __init__(self, type):
        self.__type = type

    @property
    def returnType(self):
        return Typing.LinearCollection(Typing.SimpleType("PaginatedList", "class"), self.__type)


class PaginatedListWithoutPerPageReturnStrategy(ReturnStrategy):
    def __init__(self, type):
        self.__type = type

    @property
    def returnType(self):
        return Typing.LinearCollection(Typing.SimpleType("PaginatedList", "class"), self.__type)


def parse(types, text):
    evalLocals = {
        "none": NoneReturnStrategy(),
        "boolFromStatus": BoolReturnStrategy(),
        "instanceFromAttributes": InstanceReturnStrategy,
        "structFromAttributes": StructureReturnStrategy,
        # "listFromDictItems": ListFromDictItemsReturnStrategy,
        "paginatedList": PaginatedListReturnStrategy,
        "paginatedListWithoutPerPage": PaginatedListWithoutPerPageReturnStrategy,
        "updateSelfThen": UpdateSelfReturnStrategy,
        "union": Typing.UnionType,
        "listOf": ListOfReturnStrategy,
    }
    for t in types:
        assert t.name not in evalLocals
        evalLocals[t.name] = t
    return eval(text, {"__builtins__": None}, evalLocals)
