# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import yaml
import collections
import os
import glob


Class = collections.namedtuple("Class", "name, base, structures, attributes, methods, deprecatedAttributes")
Structure = collections.namedtuple("Structure", "name, attributes, deprecatedAttributes")
Attribute = collections.namedtuple("Attribute", "name, type")
Method = collections.namedtuple("Method", "name, endPoints, parameters, urlTemplate, urlTemplateArguments, urlArguments, postArguments, effects, returnType")
EndPoint = collections.namedtuple("EndPoint", "verb, url, parameters, doc")
Parameter = collections.namedtuple("Parameter", "name, type, optional")
Argument = collections.namedtuple("Argument", "name, value")

NoneType_ = collections.namedtuple("NoneType_", "")
NoneType = NoneType_()
ScalarType = collections.namedtuple("ScalarType", "name")
LinearCollectionType = collections.namedtuple("LinearCollectionType", "container, content")
UnionType = collections.namedtuple("UnionType", "types")
EnumType = collections.namedtuple("EnumType", "values")

UpdateSelfEffect = collections.namedtuple("UpdateSelfEffect", "")


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
            base=self.__buildType(base),
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

    def __buildAttribute(self, name, type):
        assert isinstance(name, str), name
        return Attribute(
            name=name,
            type=self.__buildType(type)
        )

    def __buildMethod(self, name, url_template, effect=None, effects=None, return_type=None, end_point=None, end_points=None, url_template_arguments=[], url_arguments=[], post_arguments=[], parameters=[], optional_parameters=[]):
        assert isinstance(name, str), name
        return Method(
            name=name,
            endPoints=self.__makeList(end_point, end_points),
            parameters=[self.__buildParameter(optional=False, **p) for p in parameters]
            + [self.__buildParameter(optional=True, **p) for p in optional_parameters],
            urlTemplate=self.__buildValue(url_template),
            urlTemplateArguments=[self.__buildArgument(**a) for a in url_template_arguments],
            urlArguments=[self.__buildArgument(**a) for a in url_arguments],
            postArguments=[self.__buildArgument(**a) for a in post_arguments],
            effects=[self.__buildEffect(e) for e in self.__makeList(effect, effects)],
            returnType=self.__buildType(return_type)
        )

    def __makeList(self, element, elements):
        if elements is None:
            if element is None:
                return []
            else:
                return [element]
        else:
            assert element is None
            return elements

    def __buildParameter(self, name, optional, type):
        assert isinstance(name, str), name
        assert isinstance(optional, bool), optional
        return Parameter(
            name=name,
            type=self.__buildType(type),
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

    def __buildType(self, description):
        if description is None:
            return None
        elif description == "none":
            return NoneType
        elif isinstance(description, str):
            return ScalarType(description)
        elif "container" in description:
            return LinearCollectionType(self.__buildType(description["container"]), self.__buildType(description["content"]))
        elif "union" in description:
            return UnionType([self.__buildType(t) for t in description["union"]])
        elif "enum" in description:
            return EnumType(description["enum"])
        else:
            assert False, description  # pragma no cover

    def __buildEffect(self, effect):
        return UpdateSelfEffect()

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
