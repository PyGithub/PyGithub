# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import sys
assert sys.hexversion >= 0x03040000

import collections
import glob
import itertools
import os

import yaml


def load(*args, **kwds):
    return _DefinitionLoader(*args, **kwds).load()


def dump(*args, **kwds):
    _DefinitionDumper(*args, **kwds).dump()


# Monomorphic structures
Definition = collections.namedtuple("Definition", "endPoints, classes, unimplementedEndPoints")
Class = collections.namedtuple("Class", "name, base, structures, attributes, methods, deprecatedAttributes")
Structure = collections.namedtuple("Structure", "name, updatable, attributes, deprecatedAttributes")
Attribute = collections.namedtuple("Attribute", "name, type")
Method = collections.namedtuple("Method", "name, endPoints, parameters, unimplementedParameters, urlTemplate, urlTemplateArguments, urlArguments, postArguments, effects, returnFrom, returnType")
EndPoint = collections.namedtuple("EndPoint", "verb, url, parameters, doc")
Parameter = collections.namedtuple("Parameter", "name, type, optional, variable")
Argument = collections.namedtuple("Argument", "name, value")

# Polymorphic structures: types
NoneType_ = collections.namedtuple("NoneType_", "")
NoneType = NoneType_()
ScalarType = collections.namedtuple("ScalarType", "name")
LinearCollectionType = collections.namedtuple("LinearCollectionType", "container, content")
MappingCollectionType = collections.namedtuple("MappingCollectionType", "container, key, value")
UnionType = collections.namedtuple("UnionType", "types, key, keys, converter")
EnumType = collections.namedtuple("EnumType", "values")
AttributeType = collections.namedtuple("AttributeType", "type, attribute")

# Polymorphic structures: values
AttributeValue = collections.namedtuple("AttributeValue", "attribute")
EndPointValue = collections.namedtuple("EndPointValue", "")
ParameterValue = collections.namedtuple("ParameterValue", "parameter")
RepositoryOwnerValue = collections.namedtuple("RepositoryOwnerValue", "repository")
RepositoryNameValue = collections.namedtuple("RepositoryNameValue", "repository")


def _loadYml(fileName):
    with open(fileName) as f:
        return yaml.load(f.read())


def _dumpYml(fileName, data):
    def rec(value):
        if isinstance(value, collections.OrderedDict):
            yield from recDict(value.items())
        elif isinstance(value, dict):
            yield from recDict(sorted(value.items()))
        elif isinstance(value, list):
            yield from recList(value)
        elif isinstance(value, tuple):
            assert all(isinstance(item, str) for item in value), value
            yield "[" + ", ".join(list(rec(item))[0] for item in value) + "]"
        elif isinstance(value, str):
            if "(" in value:
                yield '"' + value + '"'
            else:
                yield value
        else:
            assert False, value  # pragma no cover

    def recList(items):
        for v in items:
            lines = list(rec(v))
            yield from ["- " + lines[0]] + ["  " + l for l in lines[1:]]  # pragma no branch

    def recDict(items):
        for k, v in items:
            lines = list(rec(v))
            if len(lines) == 1 and not isinstance(v, (dict, list)):
                yield k + ": " + lines[0]
            else:
                yield from [k + ":"] + ["  " + l for l in lines]  # pragma no branch

    with open(fileName, "w") as f:
        f.write("\n".join(rec(data)))
        f.write("\n")


class _DefinitionLoader:
    """
    At this level of description of the API, all data is structured (no more parsing needed, not even a .split(" "))
    but not cross-referenced (references are named by strings).
    """

    def __init__(self, dirName):
        self.dirName = dirName

    def load(self):
        endPoints = self.loadEndPoints()
        classes = self.loadClasses()
        unimplementedEndPoints = self.loadUnimplementedEndPoints()
        return Definition(endPoints, classes, unimplementedEndPoints)

    def loadEndPoints(self):
        data = _loadYml(os.path.join(self.dirName, "end_points.yml"))
        return tuple(sorted((self.buildEndPoint(url, **op) for url, ops in data.items() for op in ops), key=lambda ep: (ep.url, ep.verb)))

    def buildEndPoint(self, url, verb, doc, parameters=[]):
        assert isinstance(url, str), url
        assert verb in ("GET", "PUT", "HEAD", "POST", "PATCH", "DELETE"), verb
        assert isinstance(doc, str), doc
        assert all(isinstance(p, str) for p in parameters), parameters
        return EndPoint(
            verb=verb,
            url=url,
            parameters=tuple(parameters),  # Do not sort
            doc=doc,
        )

    def loadClasses(self):
        return tuple(sorted(
            (
                self.loadClass(fileName)
                for fileName in glob.glob(os.path.join(self.dirName, "classes", "*.yml"))
            ),
            key=lambda c: c.name,
        ))

    def loadClass(self, fileName):
        name = os.path.basename(fileName)[:-4]
        data = _loadYml(fileName)
        return self.buildClass(name, **data)

    def buildClass(self, name, base=None, structures=[], attributes=[], methods=[], deprecated_attributes=[]):
        assert isinstance(name, str), name
        assert isinstance(base, (type(None), str)), base
        assert all(isinstance(s, dict) for s in structures), structures
        assert all(isinstance(a, dict) for a in attributes), attributes
        assert all(isinstance(m, dict) for m in methods), methods
        assert all(isinstance(a, str) for a in deprecated_attributes), deprecated_attributes
        return Class(
            name=name,
            base=self.buildType(base),
            structures=tuple(sorted((self.buildStructure(**s) for s in structures), key=lambda s: s.name)),
            attributes=tuple(sorted((self.buildAttribute(**a) for a in attributes), key=lambda a: a.name)),
            methods=tuple(sorted((self.buildMethod(**m) for m in methods), key=lambda m: m.name)),
            deprecatedAttributes=tuple(sorted(deprecated_attributes)),
        )

    def buildStructure(self, name, updatable=True, attributes=[], deprecated_attributes=[]):
        assert isinstance(name, str), name
        assert isinstance(updatable, bool), updatable
        assert all(isinstance(a, dict) for a in attributes), attributes
        assert all(isinstance(a, str) for a in deprecated_attributes), deprecated_attributes
        return Structure(
            name=name,
            updatable=updatable,
            attributes=tuple(sorted((self.buildAttribute(**a) for a in attributes), key=lambda a: a.name)),
            deprecatedAttributes=tuple(sorted(deprecated_attributes)),
        )

    def buildAttribute(self, name, type):
        assert isinstance(name, str), name
        # no assert on type
        return Attribute(
            name=name,
            type=self.buildType(type),
        )

    def buildMethod(self, name, url_template, effect=None, effects=None, return_from=None, return_type=None, end_point=None, end_points=None, url_template_arguments=[], url_arguments=[], post_arguments=[], parameters=[], optional_parameters=[], variable_parameter=None, unimplemented_parameters=[]):
        assert isinstance(name, str), name
        # no assert on url_template
        effects = self.makeList(effect, effects)
        assert all(isinstance(e, str) for e in effects)
        assert isinstance(return_from, (type(None), str)), return_from
        # no assert on return_type
        end_points = self.makeList(end_point, end_points)
        assert all(isinstance(ep, str) for ep in end_points)
        assert all(isinstance(a, dict) for a in url_template_arguments), url_template_arguments
        assert all(isinstance(a, dict) for a in url_arguments), url_arguments
        assert all(isinstance(a, dict) for a in post_arguments), post_arguments
        assert all(isinstance(p, dict) for p in parameters), parameters
        assert all(isinstance(p, dict) for p in optional_parameters), optional_parameters
        assert isinstance(variable_parameter, (type(None), dict)), variable_parameter
        assert all(isinstance(p, str) for p in unimplemented_parameters)
        return Method(
            name=name,
            endPoints=tuple(sorted(end_points)),
            parameters=tuple(itertools.chain(
                (self.buildParameter(optional=False, variable=False, **p) for p in parameters),  # Do not sort
                (self.buildParameter(optional=True, variable=False, **p) for p in optional_parameters),  # Do not sort
                () if variable_parameter is None else (self.buildParameter(optional=False, variable=True, **variable_parameter),)
            )),
            unimplementedParameters=tuple(sorted(unimplemented_parameters)),
            urlTemplate=self.buildValue(url_template),
            urlTemplateArguments=self.buildArguments(url_template_arguments),
            urlArguments=self.buildArguments(url_arguments),
            postArguments=self.buildArguments(post_arguments),
            effects=tuple(self.buildEffect(e) for e in effects),
            returnFrom=return_from,
            returnType=self.buildType(return_type),
        )

    def makeList(self, element, elements):
        if elements is None:
            if element is None:
                return []
            else:
                return [element]
        else:
            assert element is None
            return elements

    def buildParameter(self, name, optional, variable, type=None):
        assert isinstance(name, str), name
        assert isinstance(optional, bool), optional
        assert isinstance(variable, bool), variable
        # no assert on type
        return Parameter(
            name=name,
            type=self.buildType(type),
            optional=optional,
            variable=variable,
        )

    def buildArguments(self, arguments):
        return tuple(sorted((self.buildArgument(**a) for a in arguments), key=lambda a: a.name))

    def buildArgument(self, name, value):
        assert isinstance(name, str), name
        # no assert on value
        return Argument(
            name=name,
            value=self.buildValue(value)
        )

    def buildValue(self, value):
        if value == "end_point":
            return EndPointValue()
        else:
            origin, value = value.split()
            if origin == "attribute":
                return AttributeValue(value)
            elif origin == "parameter":
                return ParameterValue(value)
            elif origin == "ownerFromRepo":
                return RepositoryOwnerValue(value)
            elif origin == "nameFromRepo":
                return RepositoryNameValue(value)
            else:
                assert False, origin  # pragma no cover

    def buildType(self, description):
        if description is None:
            return None
        elif description == "none":
            return NoneType
        elif isinstance(description, str):
            return ScalarType(description)
        elif "class" in description:
            return AttributeType(self.buildType(description["class"]), description["attribute"])
        elif "container" in description:
            if "content" in description:
                return LinearCollectionType(self.buildType(description["container"]), self.buildType(description["content"]))
            elif "key" in description and "value" in description:
                return MappingCollectionType(self.buildType(description["container"]), self.buildType(description["key"]), self.buildType(description["value"]))
            else:
                assert False, description  # pragma no cover
        elif "union" in description:
            return UnionType(tuple(self.buildType(t) for t in description["union"]), description.get("key"), None if description.get("keys") is None else tuple(description.get("keys")), description.get("converter"))
        elif "enum" in description:
            return EnumType(tuple(sorted(description["enum"])))
        else:
            assert False, description  # pragma no cover

    def buildEffect(self, effect):
        return effect  # @todoGeni Structure

    def loadUnimplementedEndPoints(self):
        unimplemented = dict()
        for fileName in glob.glob(os.path.join(self.dirName, "unimplemented.*.yml")):
            family = os.path.basename(fileName)[14:-4]
            unimplemented[family] = tuple((k, tuple(sorted(v))) for k, v in sorted(_loadYml(fileName).items()))
        return tuple(sorted(unimplemented.items()))


class _DefinitionDumper:
    def __init__(self, dirName, definition):
        self.dirName = dirName
        self.definition = definition

    def dump(self):
        _dumpYml(os.path.join(self.dirName, "end_points.yml"), self.createDataForEndPoints(self.definition.endPoints))
        for klass in self.definition.classes:
            _dumpYml(os.path.join(self.dirName, "classes", klass.name + ".yml"), self.createDataForClass(klass))
        for family, unimplementedEndPoints in self.definition.unimplementedEndPoints:
            _dumpYml(os.path.join(self.dirName, "unimplemented." + family + ".yml"), self.createDataForUnimplementedEndPoints(unimplementedEndPoints))

    def createDataForEndPoints(self, endPoints):
        return {
            url: [self.createDataForEndPoint(endPoint) for endPoint in endPoints]
            for url, endPoints in itertools.groupby(endPoints, lambda ep: ep.url)
        }

    def createDataForEndPoint(self, endPoint):
        data = collections.OrderedDict()
        data["verb"] = endPoint.verb
        if len(endPoint.parameters) != 0:
            data["parameters"] = tuple(endPoint.parameters)
        data["doc"] = endPoint.doc
        return data

    def createDataForClass(self, klass):
        data = collections.OrderedDict()
        if klass.base is not None:
            data["base"] = klass.base.name
        if len(klass.structures) != 0:
            data["structures"] = [self.createDataForStructure(structure) for structure in klass.structures]
        if len(klass.attributes) != 0:
            data["attributes"] = [self.createDataForAttribute(attribute) for attribute in klass.attributes]
        if len(klass.deprecatedAttributes) != 0:
            data["deprecated_attributes"] = list(klass.deprecatedAttributes)
        if len(klass.methods) != 0:
            data["methods"] = [self.createDataForMethod(method) for method in klass.methods]
        return data

    def createDataForStructure(self, structure):
        data = collections.OrderedDict()
        data["name"] = structure.name
        if not structure.updatable:
            data["updatable"] = "false"
        data["attributes"] = [self.createDataForAttribute(attribute) for attribute in structure.attributes]
        if len(structure.deprecatedAttributes) != 0:
            data["deprecated_attributes"] = tuple(structure.deprecatedAttributes)
        return data

    def createDataForMethod(self, method):
        data = collections.OrderedDict()
        data["name"] = method.name
        if len(method.endPoints) == 1:
            data["end_point"] = method.endPoints[0]
        else:
            data["end_points"] = list(method.endPoints)
        if not all(p.optional or p.variable for p in method.parameters):
            data["parameters"] = []
        if any(p.optional for p in method.parameters):
            data["optional_parameters"] = []
        if len(method.unimplementedParameters) != 0:
            data["unimplemented_parameters"] = list(method.unimplementedParameters)
        for parameter in method.parameters:
            p = self.createDataForParameter(parameter)
            if parameter.optional:
                data["optional_parameters"].append(p)
            elif parameter.variable:
                data["variable_parameter"] = p
            else:
                data["parameters"].append(p)
        data["url_template"] = self.createDataForValue(method.urlTemplate)
        if len(method.urlTemplateArguments) != 0:
            data["url_template_arguments"] = self.createDataForArguments(method.urlTemplateArguments)
        if len(method.urlArguments) != 0:
            data["url_arguments"] = self.createDataForArguments(method.urlArguments)
        if len(method.postArguments) != 0:
            data["post_arguments"] = self.createDataForArguments(method.postArguments)
        if len(method.effects) == 1:
            data["effect"] = method.effects[0]
        elif len(method.effects) > 1:
            data["effects"] = list(method.effects)
        if method.returnFrom is not None:
            data["return_from"] = method.returnFrom
        data["return_type"] = self.createDataForType(method.returnType)
        return data

    def createDataForAttribute(self, attribute):
        data = collections.OrderedDict()
        data["name"] = attribute.name
        data["type"] = self.createDataForType(attribute.type)
        return data

    def createDataForParameter(self, parameter):
        data = collections.OrderedDict()
        data["name"] = parameter.name
        data["type"] = self.createDataForType(parameter.type)
        return data

    def createDataForArguments(self, arguments):
        return [self.createDataForArgument(argument) for argument in arguments]

    def createDataForArgument(self, argument):
        data = collections.OrderedDict()
        data["name"] = argument.name
        data["value"] = self.createDataForValue(argument.value)
        return data

    def createDataForValue(self, value):
        return self.getMethod("createDataFor{}", value.__class__.__name__)(value)

    def createDataForEndPointValue(self, value):
        return "end_point"

    def createDataForParameterValue(self, value):
        return "parameter " + value.parameter

    def createDataForAttributeValue(self, value):
        return "attribute " + value.attribute

    def createDataForRepositoryNameValue(self, value):
        return "nameFromRepo " + value.repository

    def createDataForRepositoryOwnerValue(self, value):
        return "ownerFromRepo " + value.repository

    def createDataForType(self, type):
        return self.getMethod("createDataFor{}", type.__class__.__name__)(type)

    def createDataForUnionType(self, type):
        types = [self.createDataForType(t) for t in type.types]
        if all(isinstance(t, str) for t in types):
            types = tuple(types)
        data = collections.OrderedDict(union=types)
        if type.key is not None:
            data["key"] = type.key
        if type.keys is not None:
            data["keys"] = tuple(type.keys)
        if type.converter is not None:
            data["converter"] = type.converter
        return data

    def createDataForAttributeType(self, type):
        data = collections.OrderedDict()
        data["class"] = type.type.name
        data["attribute"] = type.attribute
        return data

    def createDataForNoneType(self, type):
        return "none"

    def createDataForScalarType(self, type):
        return type.name

    def createDataForLinearCollectionType(self, type):
        data = collections.OrderedDict()
        data["container"] = self.createDataForType(type.container)
        data["content"] = self.createDataForType(type.content)
        return data

    def createDataForMappingCollectionType(self, type):
        data = collections.OrderedDict()
        data["container"] = self.createDataForType(type.container)
        data["key"] = self.createDataForType(type.key)
        data["value"] = self.createDataForType(type.value)
        return data

    def createDataForEnumType(self, type):
        return {"enum": tuple(type.values)}

    def createDataForUnimplementedEndPoints(self, endPoints):
        return {k: list(v) for (k, v) in endPoints}

    def getMethod(self, scheme, *names):
        name = scheme.format(*("".join(part[0].capitalize() + part[1:] for part in name.strip("_").split("_")) for name in names))
        return getattr(self, name)
