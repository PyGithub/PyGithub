# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import CodeGeneration.ApiDefinition.Structured as Structured


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


class MappingCollection(Type):
    def __init__(self, container, key, value):
        Type.__init__(self, container.name + " of " + key.name + " to " + value.name, "mapping_collection")
        self.__container = container
        self.__key = key
        self.__value = value

    @property
    def container(self):
        return self.__container

    @property
    def key(self):
        return self.__key

    @property
    def value(self):
        return self.__value

    @property
    def underlyingTypes(self):
        return self.__container.underlyingTypes | self.__key.underlyingTypes | self.__value.underlyingTypes


class UnionType(Type):
    def __init__(self, types, key, keys, converter):
        Type.__init__(self, " or ".join(t.name for t in types), "union")
        self.__types = types
        self.key = key
        self.keys = keys
        self.converter = converter

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


class Repository(object):
    def __init__(self):
        self.__simpleTypes = {}

    def register(self, t):
        if isinstance(t, SimpleType):
            assert t.name not in self.__simpleTypes
            self.__simpleTypes[t.name] = t
        else:
            assert False, t  # pragma no cover

    def get(self, description):
        # @todoGeni Create a single instance of all types
        if description is Structured.NoneType:
            return NoneType
        elif isinstance(description, Structured.ScalarType):
            return self.__simpleTypes[description.name]
        elif isinstance(description, Structured.UnionType):
            return UnionType([self.get(t) for t in description.types], description.key, description.keys, description.converter)
        elif isinstance(description, Structured.EnumType):
            return EnumeratedType(*description.values)
        elif isinstance(description, Structured.LinearCollectionType):
            container = self.get(description.container)
            content = self.get(description.content)
            return LinearCollection(container, content)
        elif isinstance(description, Structured.MappingCollectionType):
            container = self.get(description.container)
            key = self.get(description.key)
            value = self.get(description.value)
            return MappingCollection(container, key, value)
        else:
            assert False, description  # pragma no cover
