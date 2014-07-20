# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import sys
assert sys.hexversion >= 0x03040000

import collections
import inspect
import itertools
import re

import CodeGeneration.ApiDefinition.Structured as Structured
from CodeGeneration.CaseUtils import toUpperCamel


class Type:
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


class AttributeType(Type):
    def __init__(self, type, attribute):
        Type.__init__(self, "Attribute " + attribute.name + " of " + type.name, "attribute")
        self.__type = type
        self.__attribute = attribute

    @property
    def type(self):
        return self.__type

    @property
    def attribute(self):
        return self.__attribute

    # @property
    # def underlyingTypes(self):
    #     return set([self.type, self.attribute.type])


class EndPoint:
    def __init__(self, verb, url, parameters, doc):
        self.__verb = verb
        self.__url = url
        self.__urlTemplate = re.sub(":([a-z]+)", "{\\1}", url)
        self.__parameters = parameters
        self.__doc = doc

        self.__methods = []

    def _applyRecursively(self, f):
        f(self)

    def _addMethod(self, method):
        self.__methods.append(method)

    def _sortMethods(self):
        self.__methods = sorted(self.__methods, key=lambda m: (m.containerClass.name, m.name))

    @property
    def verb(self):
        return self.__verb

    @property
    def url(self):
        return self.__url

    @property
    def parameters(self):
        return self.__parameters

    @property
    def doc(self):
        return self.__doc

    @property
    def methods(self):
        return self.__methods

    @property
    def urlTemplate(self):
        return self.__urlTemplate


class AttributedType(SimpleType):
    def __init__(self, name, category, updatable, attributes, deprecatedAttributes):
        super(AttributedType, self).__init__(name, category)
        self.__updatable = updatable
        self.__attributes = sorted((Attribute(self, *a) for a in attributes), key=lambda a: a.name)
        self.__deprecatedAttributes = sorted(deprecatedAttributes)
        self.__factories = []

    def _applyRecursively(self, f):
        f(self)
        for a in self.__attributes:
            a._applyRecursively(f)

    def _addFactory(self, f):
        self.__factories.append(f)

    def _sortFactories(self):
        self.__factories = sorted(self.__factories, key=lambda f: (f.object.containerClass.name, f.object.name))

    @property
    def factories(self):
        return self.__factories

    @property
    def deprecatedAttributes(self):
        return self.__deprecatedAttributes

    @property
    def attributes(self):
        return self.__attributes

    @property
    def isUpdatable(self):
        return self.__updatable


class Attribute:
    def __init__(self, containerClass, name, type):
        self.__containerClass = containerClass
        self.__name = name

        self.__tmp_typeDescription = type

    def _applyRecursively(self, f):
        f(self)

    def _referenceType(self, typesRepo):
        self.__type = typesRepo.get(self.__tmp_typeDescription)
        del self.__tmp_typeDescription

    def _propagateFactories(self):
        for t in self.__type.underlyingTypes:
            if isinstance(t, AttributedType):
                t._addFactory(Factory("attribute", self))

    @property
    def containerClass(self):
        return self.__containerClass

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type


Factory = collections.namedtuple("Factory", "category, object")


class Class(AttributedType):
    def __init__(self, module, name, updatable, completable, base, structures, attributes, methods, deprecatedAttributes):
        super(Class, self).__init__(name, "class", updatable, attributes, deprecatedAttributes)
        self.__module = module
        self.__completable = completable
        self.__structures = sorted((Structure(self, *s) for s in structures), key=lambda s: s.name)
        self.__methods = sorted((Method(self, *m) for m in methods), key=lambda m: m.name)
        self.__derived = []

        self.__tmp_baseTypeDescription = base

    def _applyRecursively(self, f):
        super(Class, self)._applyRecursively(f)
        for s in self.__structures:
            s._applyRecursively(f)
        for m in self.__methods:
            m._applyRecursively(f)

    def _referenceBase(self, typesRepo):
        if self.__tmp_baseTypeDescription is None:
            self.__base = None
        else:
            self.__base = typesRepo.get(self.__tmp_baseTypeDescription)
            self.__base.__derived.append(self)
        del self.__tmp_baseTypeDescription

    def _sortDerived(self):
        self.__derived = sorted(self.__derived, key=lambda d: d.name)

    @property
    def module(self):
        return self.__module

    @property
    def base(self):
        return self.__base

    @property
    def derived(self):
        return self.__derived

    @property
    def structures(self):
        return self.__structures

    @property
    def methods(self):
        return self.__methods

    @property
    def isCompletable(self):
        return self.__completable


class Structure(AttributedType):
    def __init__(self, containerClass, name, updatable, attributes, deprecatedAttributes):
        super(Structure, self).__init__(name, "struct", updatable, attributes, deprecatedAttributes)
        self.__containerClass = containerClass

    @property
    def containerClass(self):
        return self.__containerClass


class Method:
    def __init__(self, containerClass, name, endPoints, parameters, unimplementedParameters, urlTemplate, urlTemplateArguments, urlArguments, postArguments, effects, returnFrom, returnType):
        self.__containerClass = containerClass
        self.__name = name
        self.__parameters = [Parameter(*p) for p in parameters]
        self.__unimplementedParameters = unimplementedParameters
        self.__urlTemplate = Value(urlTemplate)
        self.__urlTemplateArguments = [Argument(*a) for a in urlTemplateArguments]
        self.__urlArguments = [Argument(*a) for a in urlArguments]
        self.__postArguments = [Argument(*a) for a in postArguments]
        self.__effects = effects
        self.__returnFrom = returnFrom

        self.__tmp_endPointDescriptions = endPoints
        self.__tmp_returnTypeDescription = returnType

    def _applyRecursively(self, f):
        f(self)
        for p in self.__parameters:
            p._applyRecursively(f)

    def _referenceEndPoints(self, endPointsRepo):
        self.__endPoints = sorted((endPointsRepo[ep] for ep in self.__tmp_endPointDescriptions), key=lambda ep: (ep.url, ep.verb))
        del self.__tmp_endPointDescriptions

    def _referenceReturnType(self, typesRepo):
        self.__returnType = typesRepo.get(self.__tmp_returnTypeDescription)
        del self.__tmp_returnTypeDescription

    def _propagateEndPoints(self):
        for ep in self.__endPoints:
            ep._addMethod(self)

    def _propagateFactories(self):
        for t in self.__returnType.underlyingTypes:
            if isinstance(t, AttributedType):
                t._addFactory(Factory("method", self))

    @property
    def containerClass(self):
        return self.__containerClass

    @property
    def name(self):
        return self.__name

    @property
    def endPoints(self):
        return self.__endPoints

    @property
    def parameters(self):
        return self.__parameters

    @property
    def unimplementedParameters(self):
        return self.__unimplementedParameters

    @property
    def urlTemplate(self):
        return self.__urlTemplate

    @property
    def urlTemplateArguments(self):
        return self.__urlTemplateArguments

    @property
    def postArguments(self):
        return self.__postArguments

    @property
    def urlArguments(self):
        return self.__urlArguments

    @property
    def returnFrom(self):
        return self.__returnFrom

    @property
    def returnType(self):
        return self.__returnType

    @property
    def effects(self):
        return self.__effects


class Parameter:
    def __init__(self, name, type, optional):
        self.__name = name
        self.__optional = optional
        # @todoGeni Couldn't we do something to factorize all this "descrition -> type" logic? Maybe with a metaclass?
        self.__tmp_typeDescription = type

    def _applyRecursively(self, f):
        f(self)

    def _propagateType(self, typesRepo):
        self.__type = typesRepo.get(self.__tmp_typeDescription)
        del self.__tmp_typeDescription

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def optional(self):
        return self.__optional


class Argument:
    def __init__(self, name, value):
        self.__name = name
        self.__value = Value(value)

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value


def Value(value):
    return globals()[value.__class__.__name__](*value)  # Why not...


AttributeValue = collections.namedtuple("AttributeValue", "attribute")
EndPointValue = collections.namedtuple("EndPointValue", "")
ParameterValue = collections.namedtuple("ParameterValue", "parameter")
RepositoryOwnerValue = collections.namedtuple("RepositoryOwnerValue", "repository")
RepositoryNameValue = collections.namedtuple("RepositoryNameValue", "repository")


class TypesRepository:
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
        elif isinstance(description, Structured.AttributeType):
            def findAttr(t, a):
                for attribute in t.attributes:
                    if attribute.name == a:
                        return attribute
                return findAttr(t.base, a)
            type = self.get(description.type)
            return AttributeType(type, findAttr(type, description.attribute))
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
            assert False, (description, self.__simpleTypes)  # pragma no cover


class Definition:
    """
    At this level, all is cross-referenced. Strings are only used for string-ish data.
    Only one object represents each conceptual object.
    """
    def __init__(self, definition, typesRepo, test=False):
        self.__endPoints = sorted((EndPoint(*ep) for ep in definition.endPoints), key=lambda ep: (ep.url, ep.verb))
        endPointsRepo = {ep.verb + " " + ep.url: ep for ep in self.__endPoints}

        unimplementedEndPoints = []
        for endPoints in definition.unimplementedEndPoints.values():
            for url, verbs in endPoints.items():
                for verb in verbs:
                    unimplementedEndPoints.append(endPointsRepo[verb + " " + url])
        self.__unimplementedEndPoints = sorted(unimplementedEndPoints, key=lambda ep: (ep.url, ep.verb))

        self.__classes = sorted((Class("PyGithub.Blocking." + c.name, *c) for c in definition.classes), key=lambda c: c.name)
        self.__test = test

        for c in self.__classes:
            typesRepo.register(c)
            for s in c.structures:
                typesRepo.register(s)

        build = Structured.Method("Build", [], [], [], Structured.EndPointValue(), [], [], [], [], None, Structured.ScalarType("Github"))
        self.__builder = Class("Builder", "Builder", False, False, None, [], [], [build], [])

        self._applyRecursively(Class, Class._referenceBase, typesRepo)
        self._applyRecursively(Method, Method._referenceEndPoints, endPointsRepo)
        self._applyRecursively(Method, Method._referenceReturnType, typesRepo)
        self._applyRecursively(Attribute, Attribute._referenceType, typesRepo)
        self._applyRecursively(Method, Method._propagateFactories)
        self._applyRecursively(Method, Method._propagateEndPoints)
        self._applyRecursively(Attribute, Attribute._propagateFactories)
        self._applyRecursively(Parameter, Parameter._propagateType, typesRepo)
        self._applyRecursively(Class, Class._sortDerived)
        self._applyRecursively(AttributedType, AttributedType._sortFactories)
        self._applyRecursively(EndPoint, EndPoint._sortMethods)

    def _applyRecursively(self, typeFilter, f, *args, **kwds):
        class FilteringFunction:
            def __init__(self, typeFilter, f, *args, **kwds):
                self.__typeFilter = typeFilter
                self.__f = f
                self.__args = args
                self.__kwds = kwds

            def __call__(self, o):
                if isinstance(o, self.__typeFilter):
                    self.__f(o, *self.__args, **self.__kwds)

        f = FilteringFunction(typeFilter, f, *args, **kwds)

        for c in self.__classes:
            c._applyRecursively(f)

        if not self.__test:
            self.__builder._applyRecursively(f)

        for ep in self.__endPoints:
            ep._applyRecursively(f)

    @property
    def classes(self):
        return self.__classes

    @property
    def endPoints(self):
        return self.__endPoints

    @property
    def unimplementedEndPoints(self):
        return self.__unimplementedEndPoints
