# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import yaml
import collections
import os
import glob


# Monomorphic structures
# @todoAlpha separate updatable (for objects with an update method) from completable (for objects with lazy completion)
# @todoAlpha Test lazy completion and update of all classes in two topic test cases, not in each class test case
Class = collections.namedtuple("Class", "name, updatable, base, structures, attributes, methods, deprecatedAttributes")
Structure = collections.namedtuple("Structure", "name, updatable, attributes, deprecatedAttributes")
Attribute = collections.namedtuple("Attribute", "name, type")
Method = collections.namedtuple("Method", "name, endPoints, parameters, urlTemplate, urlTemplateArguments, urlArguments, postArguments, effects, returnFrom, returnType")
EndPoint = collections.namedtuple("EndPoint", "verb, url, parameters, doc")
Parameter = collections.namedtuple("Parameter", "name, type, orig, optional")
ParameterOrigin = collections.namedtuple("ParameterOrigin", "type, attribute")
Argument = collections.namedtuple("Argument", "name, value")

# Polymorphic structures: types
NoneType_ = collections.namedtuple("NoneType_", "")
NoneType = NoneType_()
ScalarType = collections.namedtuple("ScalarType", "name")
LinearCollectionType = collections.namedtuple("LinearCollectionType", "container, content")
MappingCollectionType = collections.namedtuple("MappingCollectionType", "container, key, value")
UnionType = collections.namedtuple("UnionType", "types, key, keys, converter")
EnumType = collections.namedtuple("EnumType", "values")

# Polymorphic structures: values
AttributeValue = collections.namedtuple("AttributeValue", "attribute")
EndPointValue = collections.namedtuple("EndPointValue", "")
ParameterValue = collections.namedtuple("ParameterValue", "parameter")
RepositoryOwnerValue = collections.namedtuple("RepositoryOwnerValue", "repository")
RepositoryNameValue = collections.namedtuple("RepositoryNameValue", "repository")


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

    def __buildClass(self, name, updatable, base=None, structures=[], attributes=[], methods=[], deprecated_attributes=[]):
        assert isinstance(name, str), name
        assert isinstance(base, (type(None), str)), base
        assert all(isinstance(a, str) for a in deprecated_attributes), deprecated_attributes
        # @todoAlpha Warn if base is updatable but class is not
        if not updatable and any(a["name"] == "url" for a in attributes):
            print("WARNING:", name, "has a url attribute but is not updatable")
        return Class(
            name=name,
            updatable=updatable,
            base=self.__buildType(base),
            structures=[self.__buildStructure(name, **s) for s in structures],
            attributes=[self.__buildAttribute(**a) for a in attributes],
            methods=[self.__buildMethod(name, **m) for m in methods],
            deprecatedAttributes=deprecated_attributes
        )

    def __buildStructure(self, className, name, updatable, attributes=[], deprecated_attributes=[]):
        assert isinstance(name, str), name
        assert all(isinstance(a, str) for a in deprecated_attributes), deprecated_attributes
        if not updatable and any(a["name"] == "url" for a in attributes):
            print("WARNING:", className + "." + name, "has a url attribute but is not updatable")
        return Structure(
            name=name,
            updatable=updatable,
            attributes=[self.__buildAttribute(**a) for a in attributes],
            deprecatedAttributes=deprecated_attributes
        )

    def __buildAttribute(self, name, type):
        assert isinstance(name, str), name
        return Attribute(
            name=name,
            type=self.__buildType(type)
        )

    def __buildMethod(self, className, name, url_template, effect=None, effects=None, return_from=None, return_type=None, end_point=None, end_points=None, url_template_arguments=[], url_arguments=[], post_arguments=[], parameters=[], optional_parameters=[]):
        assert isinstance(name, str), name
        if (
            isinstance(return_type, dict)
            and "container" in return_type
            and return_type["container"] == "PaginatedList"
            and all(p["name"] != "per_page" for p in optional_parameters)
            and className != "Github"
            and name not in ["get_repos", "get_users"]
        ):
            print("WARNING:", className + "." + name, "returns a paginated list but does not have a per_page parameter")  # pragma no cover
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
            returnFrom=return_from,
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

    def __buildParameter(self, name, optional, type=None, orig=None):
        assert isinstance(name, str), name
        assert isinstance(optional, bool), optional
        return Parameter(
            name=name,
            type=self.__buildType(type),
            orig=self.__buildParameterOrigin(orig),
            optional=optional
        )

    def __buildParameterOrigin(self, orig):
        if orig is None:
            return None
        else:
            assert isinstance(orig, str), orig
            type, attribute = orig.split(".")
            return ParameterOrigin(self.__buildType(type), attribute)

    def __buildArgument(self, name, value):
        assert isinstance(name, str), name
        return Argument(
            name=name,
            value=self.__buildValue(value)
        )

    def __buildValue(self, value):
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

    def __buildType(self, description):
        if description is None:
            return None
        elif description == "none":
            return NoneType
        elif isinstance(description, str):
            return ScalarType(description)
        elif "container" in description:
            if "content" in description:
                return LinearCollectionType(self.__buildType(description["container"]), self.__buildType(description["content"]))
            elif "key" in description and "value" in description:
                return MappingCollectionType(self.__buildType(description["container"]), self.__buildType(description["key"]), self.__buildType(description["value"]))
            else:
                assert False, description  # pragma no cover
        elif "union" in description:
            return UnionType([self.__buildType(t) for t in description["union"]], description.get("key"), description.get("keys"), description.get("converter"))
        elif "enum" in description:
            return EnumType(description["enum"])
        else:
            assert False, description  # pragma no cover

    def __buildEffect(self, effect):
        return effect  # @todoGeni Structure

    def __validate(self, dirName):
        unimplemented = set()
        for fileName in glob.glob(os.path.join(dirName, "unimplemented.*.yml")):
            with open(fileName) as f:
                data = yaml.load(f.read())
                unimplemented.update(verb + " " + url for url, verbs in data.items() for verb in verbs)

        allEndPoints = set(ep.verb + " " + ep.url for ep in self.endPoints)
        implemented = set()
        for c in self.classes:
            for m in c.methods:
                implemented.update(m.endPoints)

        print("INFO: Implemented end-points:", len(implemented), " - unimplemented end-points: ", len(unimplemented))

        inter = implemented & unimplemented
        assert len(inter) == 0, inter
        diff = unimplemented - allEndPoints
        assert len(diff) == 0, diff
        union = implemented | unimplemented
        assert union == allEndPoints, allEndPoints - union
