# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import itertools
import collections

import CodeGeneration.ApiDefinition.Typing as Typing
import CodeGeneration.ApiDefinition.CrossReferenced as CrossReferenced


class YmlPrettyPrinter:
    def p(self, value):
        yield from self.rec(value)

    def rec(self, value):
        if isinstance(value, collections.OrderedDict):
            yield from self.recDict(value.items())
        elif isinstance(value, dict):
            yield from self.recDict(sorted(value.items()))
        elif isinstance(value, list):
            yield from self.recList(value)
        elif isinstance(value, tuple):
            assert all(isinstance(item, str) for item in value)
            yield "[" + ", ".join(value) + "]"
        elif isinstance(value, str):
            yield value
        else:
            assert False, value  # pragma no cover

    def recList(self, items):
        for v in items:
            lines = list(self.rec(v))
            yield from ["- " + lines[0]] + ["  " + l for l in lines[1:]]

    def recDict(self, items):
        for k, v in items:
            lines = list(self.rec(v))
            if len(lines) == 1 and not isinstance(v, (dict, list)):
                yield k + ": " + lines[0]
            else:
                yield from [k + ":"] + ["  " + l for l in lines]


class YmlGenerator:
    def generateEndpoints(self, endPoints):
        yield from YmlPrettyPrinter().p(self.createDataForEndPoints(endPoints))

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

    def generateClass(self, klass):
        yield from YmlPrettyPrinter().p(self.createDataForKlass(klass))

    def createDataForKlass(self, klass):
        data = collections.OrderedDict()

        if klass.base.name not in ["UpdatableGithubObject", "SessionedGithubObject"]:
            data["base"] = klass.base.name

        data["updatable"] = "true" if klass.isUpdatable else "false"

        if len(klass.structures) != 0:
            data["structures"] = [self.createDataForStrukture(structure) for structure in klass.structures]

        if len(klass.attributes) != 0:
            data["attributes"] = [self.createDataForAttribute(attribute) for attribute in klass.attributes]

        if len(klass.deprecatedAttributes) != 0:
            data["deprecated_attributes"] = list(klass.deprecatedAttributes)

        if len(klass.methods) != 0:
            data["methods"] = [self.createDataForMethod(method) for method in klass.methods]

        return data

    def createDataForStrukture(self, structure):
        data = collections.OrderedDict()
        data["name"] = structure.name
        data["updatable"] = ("true" if structure.isUpdatable else "false")
        data["attributes"] = [self.createDataForAttribute(attribute) for attribute in structure.attributes]
        if len(structure.deprecatedAttributes) != 0:
            data["deprecated_attributes"] = tuple(structure.deprecatedAttributes)
        return data

    def createDataForMethod(self, method):
        data = collections.OrderedDict()

        data["name"] = method.name

        if len(method.endPoints) == 1:
            data["end_point"] = method.endPoints[0].verb + " " + method.endPoints[0].url
        else:
            data["end_points"] = [ep.verb + " " + ep.url for ep in method.endPoints]

        if not all(p.optional for p in method.parameters):
            data["parameters"] = []
        if any(p.optional for p in method.parameters):
            data["optional_parameters"] = []
        for parameter in method.parameters:
            p = self.createDataForParameter(parameter)
            if parameter.optional:
                data["optional_parameters"].append(p)
            else:
                data["parameters"].append(p)

        data["url_template"] = self.createDataForValue(method.urlTemplate)

        if len(method.urlTemplateArguments) != 0:
            data["url_template_arguments"] = [self.createDataForArgument(argument) for argument in method.urlTemplateArguments]

        if len(method.urlArguments) != 0:
            data["url_arguments"] = [self.createDataForArgument(argument) for argument in method.urlArguments]

        if len(method.postArguments) != 0:
            data["post_arguments"] = [self.createDataForArgument(argument) for argument in method.postArguments]

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

    createDataForParameter = createDataForAttribute

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
        if (
            # @todoGeni Do something?
            len(type.types) == 2 and type.types[0].name != "TwoStrings" and type.types[1].name == "string"
            or len(type.types) == 3 and type.types[1].name == "string" and type.types[2].name == "TwoStrings"
        ):
            return self.createDataForType(type.types[0])
        else:
            types = [self.createDataForType(t) for t in type.types]
            if all(isinstance(t, str) for t in types):
                types = tuple(types)
            return {"union": types}

    def createDataForNoneType(self, type):
        return "none"

    def createDataForClass(self, type):
        return type.name

    def createDataForBuiltinType(self, type):
        return type.name

    def createDataForLinearCollection(self, type):
        data = collections.OrderedDict()
        data["container"] = self.createDataForType(type.container)
        data["content"] = self.createDataForType(type.content)
        return data

    def createDataForEnumeratedType(self, type):
        return {"enum": tuple(type.values)}

    def createDataForStructure(self, type):
        return type.name

    def getMethod(self, scheme, *names):
        name = scheme.format(*("".join(part[0].capitalize() + part[1:] for part in name.strip("_").split("_")) for name in names))
        return getattr(self, name)
