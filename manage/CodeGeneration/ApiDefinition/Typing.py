# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>


class Type(object):
    def __init__(self, name, category):
        self.__name = name
        self.__category = category

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category


class SimpleType(Type):
    @property
    def underlyingTypes(self):
        return set([self])


class BuiltinType(SimpleType):
    def __init__(self, name):
        Type.__init__(self, name, "builtin")


class NoneType_(SimpleType):
    def __init__(self):
        Type.__init__(self, "NoneType", "none")
NoneType = NoneType_()


class LinearCollection(Type):
    def __init__(self, container, content):
        Type.__init__(self, container.name + " of " + content.name, "linear_collection")
        self.__container = container
        self.__content = content

    @property
    def container(self):
        return self.__container

    @property
    def content(self):
        return self.__content

    @property
    def underlyingTypes(self):
        return self.__container.underlyingTypes | self.__content.underlyingTypes


class UnionType(Type):
    def __init__(self, *types):
        Type.__init__(self, " or ".join(t.name for t in types), "union")
        self.__types = types

    @property
    def types(self):
        return self.__types

    @property
    def underlyingTypes(self):
        types = set()
        for type in self.__types:
            types.update(type.underlyingTypes)
        return types


class EnumeratedType(SimpleType):
    def __init__(self, *values):
        Type.__init__(self, " or ".join('"' + v + '"' for v in values), "enum")
        self.__values = values

    @property
    def values(self):
        return self.__values
