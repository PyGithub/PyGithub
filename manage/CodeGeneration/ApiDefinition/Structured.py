# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import yaml
import collections
import os
import glob
import types


EndPoint = collections.namedtuple("EndPoint", "verb, url, parameters, doc")
Enum = collections.namedtuple("Enum", "name, values")
List = collections.namedtuple("List", "type")
Structure = collections.namedtuple("Structure", "name, attributes, deprecatedAttributes")
Class = collections.namedtuple("Class", "name, base, structures, attributes, methods, deprecatedAttributes")
Method = collections.namedtuple("Method", "name, endPoints, parameters, urlTemplate, urlTemplateArguments, urlArguments, postArguments, returnStrategy")
Parameter = collections.namedtuple("Parameter", "name, types, optional")
Argument = collections.namedtuple("Argument", "name, value")
Attribute = collections.namedtuple("Attribute", "name, types")


class Definition(object):
    """
    At this level of description of the API, all data is structured (no more parsing needed, not even a .split(" "))
    but not cross-referenced (references are named by strings).
    """

    def __init__(self, dirName):
        self.__loadEndPoints(dirName)
        self.__loadClasses(dirName)
        self.__validate(dirName)

    @property
    def endPoints(self):
        return self.__endPoints

    @property
    def classes(self):
        return self.__classes

    def __loadEndPoints(self, dirName):
        with open(os.path.join(dirName, "end_points.yml")) as f:
            data = yaml.load(f.read())
        self.__endPoints = [self.__buildEndPoint(url, **op) for url, ops in data.items() for op in ops]

    def __buildEndPoint(self, url, verb, doc, parameters=[]):
        assert isinstance(url, str), url
        assert isinstance(verb, str), verb
        assert isinstance(doc, str), doc
        assert all(isinstance(p, str) for p in parameters), parameters
        return EndPoint(
            verb=verb,
            url=url,
            parameters=parameters,
            doc=doc
        )

    def __loadClasses(self, dirName):
        self.__classes = [
            self.__loadClass(fileName)
            for fileName in glob.glob(os.path.join(dirName, "classes", "*.yml"))
        ]

    def __loadClass(self, fileName):
        name = os.path.basename(fileName)[:-4]
        with open(fileName) as f:
            data = yaml.load(f.read())
        return self.__buildClass(name, **data)

    def __buildClass(self, name, base=None, structures=[], attributes=[], methods=[], deprecated_attributes=[]):
        assert isinstance(name, str), name
        assert isinstance(base, (type(None), str)), base
        assert all(isinstance(a, str) for a in deprecated_attributes), deprecated_attributes
        return Class(
            name=name,
            base=base,
            structures=[self.__buildStructure(**s) for s in structures],
            attributes=[self.__buildAttribute(**a) for a in attributes],
            methods=[self.__buildMethod(**m) for m in methods],
            deprecatedAttributes=deprecated_attributes
        )

    def __buildStructure(self, name, attributes=[], deprecated_attributes=[]):
        assert isinstance(name, str), name
        assert all(isinstance(a, str) for a in deprecated_attributes), deprecated_attributes
        return Structure(
            name=name,
            attributes=[self.__buildAttribute(**a) for a in attributes],
            deprecatedAttributes=deprecated_attributes
        )

    def __buildAttribute(self, name, **typeArgs):
        assert isinstance(name, str), name
        return Attribute(
            name=name,
            types=self.__buildTypes(**typeArgs)
        )

    def __buildTypes(self, type=None, types=None):
        if types is None:
            types = []
        if type is not None:
            types.append(type)
        assert len(types) != 0
        return [self.__buildType(t) for t in types]

    def __buildType(self, type):
        if isinstance(type, str):
            if len(type.split(" ")) != 1:
                print("WARNING: type seems to be complex but not structured: ", type)  # pragma no cover
            return type
        else:
            return self.__buildAnonymousType(**type)

    def __buildAnonymousType(self, meta, **kwds):
        if meta == "enum":
            return self.__buildEnum(**kwds)
        elif meta == "list":
            return self.__buildList(**kwds)
        else:
            assert False, "Unknown meta" + meta  # pragma no cover

    def __buildEnum(self, values):
        assert all(isinstance(v, str) for v in values), values
        return Enum(None, values)

    def __buildList(self, type):
        return List(type)

    def __buildMethod(self, name, url_template, return_strategy, end_point=None, end_points=[], url_template_arguments=[], url_arguments=[], post_arguments=[], parameters=[], optional_parameters=[]):
        assert isinstance(name, str), name
        end_points = list(end_points)
        if end_point is not None:
            end_points.append(end_point)

        if return_strategy.startswith("paginatedList("):
            optional_parameters = list(optional_parameters)
            optional_parameters.append(dict(name="per_page", type="int"))
            url_arguments = list(url_arguments)
            url_arguments.append(dict(name="per_page", value="parameter per_page"))

        return Method(
            name=name,
            endPoints=end_points,
            parameters=[self.__buildParameter(optional=False, **p) for p in parameters]
            + [self.__buildParameter(optional=True, **p) for p in optional_parameters],
            urlTemplate=self.__buildValue(url_template),
            urlTemplateArguments=[self.__buildArgument(**a) for a in url_template_arguments],
            urlArguments=[self.__buildArgument(**a) for a in url_arguments],
            postArguments=[self.__buildArgument(**a) for a in post_arguments],
            returnStrategy=self.__buildReturnStrategy(return_strategy)
        )

    def __buildParameter(self, name, optional, **typeArgs):
        assert isinstance(name, str), name
        assert isinstance(optional, bool), optional
        return Parameter(
            name=name,
            types=self.__buildTypes(**typeArgs),
            optional=optional
        )

    def __buildArgument(self, name, value):
        assert isinstance(name, str), name
        return Argument(
            name=name,
            value=self.__buildValue(value)
        )

    def __buildValue(self, value):
        return value  # @todoGeni Structure

    def __buildReturnStrategy(self, strategy):
        return strategy  # @todoGeni Structure (strategy/purpose/whatever: this is the most complex topic)

    def __validate(self, dirName):
        with open(os.path.join(dirName, "unimplemented.yml")) as f:
            data = yaml.load(f.read())
        unimplemented = set(verb + " " + url for url, verbs in data.items() for verb in verbs)

        allEndPoints = set(ep.verb + " " + ep.url for ep in self.endPoints)
        implemented = set()
        for c in self.classes:
            for m in c.methods:
                implemented.update(m.endPoints)

        inter = implemented & unimplemented
        union = implemented | unimplemented
        assert len(inter) == 0, inter
        assert union == allEndPoints, allEndPoints - union
