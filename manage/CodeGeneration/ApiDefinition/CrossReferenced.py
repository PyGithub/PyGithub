# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import re

import CodeGeneration.ApiDefinition.Structured as Structured
import CodeGeneration.ApiDefinition.Typing as Typing
import CodeGeneration.ApiDefinition.ReturnStrategies as ReturnStrategies


class EndPoint(object):
    def __init__(self, verb, url, parameters, doc):
        self.__verb = verb
        self.__url = url
        self.__urlTemplate = re.sub(":([a-z]+)", "{\\1}", url)
        self.__parameters = parameters
        self.__doc = doc

        self.__tmp_methods = []

    def _addMethod(self, method):
        self.__tmp_methods.append(method)

    def _finalize(self):
        self.__methods = sorted(self.__tmp_methods, key=lambda m: (m.containerClass.name, m.name))
        del self.__tmp_methods

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


class AttributedType(Typing.SimpleType):
    def __init__(self, name, category, attributes, deprecatedAttributes):
        Typing.Type.__init__(self, name, category)
        self.__deprecatedAttributes = sorted(deprecatedAttributes)

        self.__tmp_attributes = [Attribute(self, *a) for a in attributes]
        self.__tmp_factories = []

    def _crossReference(self, types, endPoints):
        for a in self.__tmp_attributes:
            a._crossReference(types, endPoints)

    def _addFactory(self, f):
        self.__tmp_factories.append(f)

    def _finalize(self):
        self.__attributes = sorted(self.__tmp_attributes, key=lambda a: a.name)
        del self.__tmp_attributes
        self.__factories = sorted(self.__tmp_factories, key=lambda f: (f.object.containerClass.name, f.object.name))
        del self.__tmp_factories

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
        return (
            self.name == "RateLimits"
            or any(f.category == "attribute" and f.object.containerClass.isUpdatable for f in self.__factories)
        )


class Member(object):
    def __init__(self, containerClass):
        self.__containerClass = containerClass

    @property
    def containerClass(self):
        return self.__containerClass


class Attribute(Member):
    def __init__(self, containerClass, name, types):
        Member.__init__(self, containerClass)
        self.__name = name

        self.__tmp_types = types

    def _crossReference(self, types, endPoints):
        ts = []
        for typeName in self.__tmp_types:
            t = types[typeName]
            ts.append(t)
            if isinstance(t, AttributedType):
                t._addFactory(Factory("attribute", self))
        del self.__tmp_types

        assert len(ts) != 0
        if len(ts) > 1:
            self.__type = Typing.UnionType(*ts)
        else:
            self.__type = ts[0]

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type


class Argument(object):
    def __init__(self, name, value):
        self.__name = name
        self.__value = Value(value)

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value


class Value(object):
    def __init__(self, value):
        if value == "end_point":
            self.__origin = "end_point"
        else:
            self.__origin, self.__value = value.split(" ")
            assert self.__origin in ["attribute", "parameter", "ownerFromRepo", "nameFromRepo"]

    @property
    def origin(self):
        return self.__origin

    @property
    def value(self):
        return self.__value


class Factory:
    def __init__(self, category, object):
        self.category = category
        self.object = object


class Class(AttributedType):
    def __init__(self, module, name, base, structures, attributes, methods, deprecatedAttributes):
        AttributedType.__init__(self, name, "class", attributes, deprecatedAttributes)
        self.__module = module
        self.__tmp_base = base
        self.__tmp_structures = {s.name: Structure(self, *s) for s in structures}
        self.__tmp_methods = {m.name: Method(self, *m) for m in methods}
        self.__tmp_derived = []
        self.__tmp_dependencies = set()

    def _crossReference(self, types, endPoints):
        types = dict(types)
        types.update(self.__tmp_structures)

        AttributedType._crossReference(self, types, endPoints)

        if self.__tmp_base is None:
            if self.name == "Github":
                self.__base = types["SessionedGithubObject"]
            else:
                self.__base = types["UpdatableGithubObject"]
        else:
            self.__base = types[self.__tmp_base]
            self.__base.__tmp_derived.append(self)
            self.__tmp_dependencies.add(self.__base)
        del self.__tmp_base

        for s in self.__tmp_structures.values():
            s._crossReference(types, endPoints)
            for a in s._AttributedType__tmp_attributes:
                self.__tmp_dependencies.add(a.type)

        for m in self.__tmp_methods.values():
            m._crossReference(types, endPoints)
            self.__tmp_dependencies.update(m.returnStrategy.returnType.underlyingTypes)

    def _finalize(self):
        AttributedType._finalize(self)

        for s in self.__tmp_structures.values():
            s._finalize()
        self.__structures = sorted(self.__tmp_structures.values(), key=lambda s: s.name)
        del self.__tmp_structures

        for m in self.__tmp_methods.values():
            m._finalize()
        self.__methods = sorted(self.__tmp_methods.values(), key=lambda m: m.name)
        del self.__tmp_methods

        self.__derived = sorted(self.__tmp_derived, key=lambda d: d.name)
        del self.__tmp_derived

        for a in self.attributes:
            self.__tmp_dependencies.update(a.type.underlyingTypes)

        self.__dependencies = sorted((d for d in self.__tmp_dependencies if d.category == "class" and d.name != "PaginatedList" and d.name != self.name), key=lambda c: c.name)
        del self.__tmp_dependencies

    def _getStruct(self, name):
        return self.__tmp_structures[name]

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
    def dependencies(self):
        return self.__dependencies

    @property
    def isUpdatable(self):
        return True


class Structure(AttributedType, Member):
    def __init__(self, containerClass, name, attributes, deprecatedAttributes):
        AttributedType.__init__(self, name, "struct", attributes, deprecatedAttributes)
        Member.__init__(self, containerClass)


class Method(Member):
    def __init__(self, containerClass, name, endPoints, parameters, urlTemplate, urlTemplateArguments, urlArguments, postArguments, returnStrategy):
        Member.__init__(self, containerClass)
        self.__name = name
        self.__parameters = [Parameter(*p) for p in parameters]
        self.__urlTemplate = Value(urlTemplate)
        self.__urlTemplateArguments = [Argument(*a) for a in urlTemplateArguments]
        self.__urlArguments = [Argument(*a) for a in urlArguments]
        self.__postArguments = [Argument(*a) for a in postArguments]

        self.__tmp_endPoints = endPoints
        self.__tmp_returnStrategy = returnStrategy

    def _crossReference(self, types, endPoints):
        eps = []
        for ep in self.__tmp_endPoints:
            ep = endPoints[ep]
            ep._addMethod(self)
            eps.append(ep)
        self.__endPoints = sorted(eps, key=lambda ep: (ep.url, ep.verb))

        for p in self.__parameters:
            p._crossReference(types, endPoints)

        self.__returnStrategy = ReturnStrategies.parse(types.values(), self.__tmp_returnStrategy)
        for t in self.returnType.underlyingTypes:
            if isinstance(t, AttributedType):
                t._addFactory(Factory("method", self))

    def _finalize(self):
        self.__displayWarnings()
        del self.__tmp_endPoints

    def __displayWarnings(self):  # pragma no cover
        for ep in self.__endPoints:
            unimplementedParameters = set(ep.parameters) - set(p.name for p in self.__parameters)
            # @todoGeni Put those special cases in .yml definition files
            if self.containerClass.name == "AuthenticatedUser" and self.__name == "create_repo":
                unimplementedParameters.remove("team_id")
            if self.__name == "create_fork":
                unimplementedParameters.remove("organization")
            if self.containerClass.name == "AuthenticatedUser" and self.__name == "edit":
                unimplementedParameters.remove("bio")
            if self.containerClass.name == "Repository" and self.__name == "edit":
                unimplementedParameters.remove("has_downloads")
            if self.containerClass.name == "Repository" and self.__name == "create_file":
                unimplementedParameters.remove("sha")
                unimplementedParameters.remove("name")
                unimplementedParameters.remove("email")
            if self.containerClass.name == "File" and self.__name in ["edit", "delete"]:
                unimplementedParameters.remove("sha")
                unimplementedParameters.remove("name")
                unimplementedParameters.remove("email")
                unimplementedParameters.remove("path")
                unimplementedParameters.remove("branch")
            if len(unimplementedParameters) > 0:
                print(self.containerClass.name + "." + self.__name, "does not implement following parameters:", ", ".join(unimplementedParameters))

        unusedParameters = set(p.name for p in self.__parameters) - set(a.value.value for a in self.__urlTemplateArguments) - set((a.value.value for a in self.__urlArguments)) - set((a.value.value for a in self.__postArguments))
        if len(unusedParameters) > 0:
            print(self.containerClass.name + "." + self.__name, "does not use following parameters:", ", ".join(unusedParameters))

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
    def returnStrategy(self):
        return self.__returnStrategy

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
    def returnType(self):
        return self.__returnStrategy.returnType


class Parameter(object):
    def __init__(self, name, types, optional):
        self.__name = name
        self.__optional = optional
        self.__tmp_types = types

    def _crossReference(self, types, endPoints):
        ts = []
        for typeName in self.__tmp_types:
            if isinstance(typeName, str):
                if "." in typeName:
                    className, structName = typeName.split(".")
                    ts.append(types[className]._getStruct(structName))
                else:
                    ts.append(types[typeName])
            elif isinstance(typeName, Structured.Enum):
                ts.append(Typing.EnumeratedType(*typeName.values))
            elif isinstance(typeName, Structured.List):
                ts.append(Typing.LinearCollection(Typing.BuiltinType("list"), types[typeName.type]))
            else:
                assert False, typeName  # pragma no cover

        for typeName in self.__tmp_types:
            if isinstance(typeName, str):
                if "." in typeName:
                    ts.append(Typing.BuiltinType("string"))
                else:
                    c = types[typeName]
                    if c.category == "class" and len(self.__tmp_types) == 1:
                        ts.append(Typing.BuiltinType("string"))  # @todoGeni The fact that c can be replaced by a string should be in ApiDefinition/c.yml
                        if c.name == "Repository":
                            ts.append(Typing.BuiltinType("TwoStrings"))  # @todoGeni The fact that c can be replaced by a 2-tuple of strings should be in ApiDefinition/c.yml

        del self.__tmp_types

        assert len(ts) != 0
        if len(ts) > 1:
            self.__type = Typing.UnionType(*ts)
        else:
            self.__type = ts[0]

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def optional(self):
        return self.__optional


class Definition(object):
    """
    At this level, all is cross-referenced. Strings are only used for string-ish data.
    Only one object represents each conceptual object.
    """
    def __init__(self, definition):
        endPoints = {ep.verb + " " + ep.url: EndPoint(*ep) for ep in definition.endPoints}
        classes = {c.name: Class("PyGithub.Blocking." + c.name, *c) for c in definition.classes}

        build = Structured.Method("build", [], [], "end_point", [], [], [], "instanceFromAttributes(Github)")
        builder = Class("Builder", "Builder", None, [], [], [build], [])

        types = {t: Typing.BuiltinType(t) for t in ["int", "bool", "string", "datetime"]}
        types.update({t: Typing.BuiltinType(t) for t in ["Reset", "TwoStrings", "GitAuthor"]})  # @todoAlpha Fix this: those are not builtins
        types.update({t: Class("PyGithub.Blocking.BaseGithubObject", t, None, [], [], [], []) for t in ["SessionedGithubObject", "UpdatableGithubObject"]})
        types.update(classes)

        for c in classes.values():
            c._crossReference(types, endPoints)
        builder._crossReference(types, endPoints)

        for ep in endPoints.values():
            ep._finalize()
        for c in classes.values():
            c._finalize()
        builder._finalize()

        self.__endPoints = sorted(endPoints.values(), key=lambda ep: (ep.url, ep.verb))
        self.__classes = sorted(classes.values(), key=lambda c: c.name)

    @property
    def classes(self):
        return self.__classes

    @property
    def endPoints(self):
        return self.__endPoints
