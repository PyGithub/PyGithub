# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import itertools

import CodeGeneration.ApiDefinition.Typing as Typing
import CodeGeneration.ApiDefinition.CrossReferenced as CrossReferenced


class YmlGenerator:
    def generateEndpoints(self, endPoints):
        for url, endPoints in itertools.groupby(endPoints, lambda ep: ep.url):
            yield "{}:".format(url)
            for endPoint in endPoints:
                yield "  - verb: {}".format(endPoint.verb)
                if len(endPoint.parameters) != 0:
                    yield "    parameters: [{}]".format(", ".join(endPoint.parameters))
                yield "    doc: {}".format(endPoint.doc)

    def generateClass(self, klass):
        if klass.base.name not in ["UpdatableGithubObject", "SessionedGithubObject"]:
            yield "base: " + klass.base.name
        if len(klass.structures) != 0:
            yield "structures:"
            for structure in klass.structures:
                yield "  - name: " + structure.name
                yield "    attributes:"
                for attribute in structure.attributes:
                    yield "      - name: " + attribute.name
                    yield "        type: " + attribute.type.name
                if len(structure.deprecatedAttributes) != 0:
                    yield "    deprecated_attributes:"
                    for attribute in structure.deprecatedAttributes:
                        yield "      - " + attribute
        if len(klass.attributes) != 0:
            yield "attributes:"
            for attribute in klass.attributes:
                yield "  - name: " + attribute.name
                if attribute.type.category in ["builtin", "struct", "class"]:
                    yield "    type: " + attribute.type.name
                elif attribute.type.category == "union":
                    yield "    type:"
                    yield "      union: [" + ", ".join(t.name for t in attribute.type.types) + "]"
                else:
                    assert False  # pragma no cover
        if len(klass.deprecatedAttributes) != 0:
            yield "deprecated_attributes:"
            for attribute in klass.deprecatedAttributes:
                yield "  - " + attribute
        if len(klass.methods) != 0:
            yield "methods:"
            for method in klass.methods:
                yield "  - name: " + method.name
                if len(method.endPoints) == 1:
                    yield "    end_point: " + method.endPoints[0].verb + " " + method.endPoints[0].url
                else:
                    yield "    end_points:"
                    for ep in method.endPoints:
                        yield "      - " + ep.verb + " " + ep.url
                if not all(p.optional for p in method.parameters):
                    yield "    parameters:"
                    for parameter in method.parameters:
                        if not parameter.optional:
                            yield "      - name: " + parameter.name
                            if parameter.type.category == "union":
                                if parameter.type.types[0].name == "TwoStrings":
                                    yield "        type:"
                                    yield "          union: [TwoStrings, string]"
                                else:
                                    yield "        type: " + parameter.type.types[0].name
                            elif parameter.type.category in ["builtin"]:
                                yield "        type: " + parameter.type.name
                            else:
                                assert False  # pragma no cover

                if any(p.optional for p in method.parameters):
                    yield "    optional_parameters:"
                    for parameter in method.parameters:
                        if parameter.optional:
                            yield "      - name: " + parameter.name
                            if parameter.type.category == "enum":
                                yield "        type:"
                                yield "          enum: [" + ", ".join(parameter.type.values) + "]"
                            elif parameter.type.category == "union":
                                if parameter.type.types[1].name == "Reset":
                                    yield "        type:"
                                    yield "          union: [" + parameter.type.types[0].name + ", Reset]"
                                elif parameter.type.types[1].name == "string":
                                    yield "        type: " + parameter.type.types[0].name
                                else:
                                    yield "        type:"
                                    yield "          union: [" + ", ".join(t.name for t in parameter.type.types) + "]"
                            elif parameter.type.category == "linear_collection":
                                yield "        type:"
                                yield "          container: list"
                                yield "          content: " + parameter.type.content.name
                            elif parameter.type.category in ["builtin"]:
                                yield "        type: " + parameter.type.name
                            else:
                                assert False  # pragma no cover

                if method.urlTemplate.origin in ["attribute", "parameter", "ownerFromRepo", "nameFromRepo"]:
                    yield "    url_template: " + method.urlTemplate.origin + " " + method.urlTemplate.value
                else:
                    yield "    url_template: " + method.urlTemplate.origin

                if len(method.urlTemplateArguments) != 0:
                    yield "    url_template_arguments:"
                    for urlTemplateArgument in method.urlTemplateArguments:
                        yield "      - name: " + urlTemplateArgument.name
                        yield "        value: " + urlTemplateArgument.value.origin + " " + urlTemplateArgument.value.value

                if len(method.urlArguments) != 0:
                    yield "    url_arguments:"
                    for urlArgument in method.urlArguments:
                        yield "      - name: " + urlArgument.name
                        yield "        value: " + urlArgument.value.origin + " " + urlArgument.value.value

                if len(method.postArguments) != 0:
                    yield "    post_arguments:"
                    for postArgument in method.postArguments:
                        yield "      - name: " + postArgument.name
                        yield "        value: " + postArgument.value.origin + " " + postArgument.value.value

                if len(method.effects) == 1:
                    yield "    effect: " + method.effects[0]
                elif len(method.effects) > 1:
                    yield "    effects:"
                    for effect in method.effects:
                        yield "      - " + effect

                if method.returnFrom is not None:
                    yield "    return_from: " + method.returnFrom

                returnType = method.returnType
                if returnType is Typing.NoneType:
                    yield "    return_type: none"
                elif isinstance(returnType, (CrossReferenced.Class, CrossReferenced.Structure, Typing.BuiltinType)):
                    yield "    return_type: " + returnType.name
                elif isinstance(returnType, Typing.UnionType):
                    # @todoGeni Generalize
                    yield "    return_type:"
                    yield "      union:"
                    yield "        - File"
                    yield "        - SymLink"
                    yield "        - Submodule"
                    yield "        - container: list"
                    yield "          content:"
                    yield "            union: [File, Dir, SymLink, Submodule]"
                elif isinstance(returnType, Typing.LinearCollection):
                    yield "    return_type:"
                    yield "      container: " + returnType.container.name
                    if isinstance(returnType.content, (CrossReferenced.Class, CrossReferenced.Structure, Typing.BuiltinType)):
                        yield "      content: " + returnType.content.name
                    elif isinstance(returnType.content, (Typing.UnionType)):
                        yield "      content:"
                        yield "        union: [" + ", ".join(t.name for t in returnType.content.types) + "]"
                    else:
                        assert False  # pragma no cover
                else:
                    assert False  # pragma no cover
