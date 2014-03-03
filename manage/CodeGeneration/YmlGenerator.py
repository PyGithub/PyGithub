# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import itertools


class YmlGenerator:
    def generateEndpoints(self, endPoints):
        for url, endPoints in itertools.groupby(endPoints, lambda ep: ep.url):
            yield "{}:".format(url)
            for endPoint in endPoints:
                yield "  - verb: {}".format(endPoint.verb)
                if len(endPoint.parameters) != 0:
                    yield "    parameters: [{}]".format(", ".join(endPoint.parameters))
                yield "    doc: {}".format(endPoint.doc)

    # def generateClass(self, klass):
    #     if klass.base.name not in ["UpdatableGithubObject", "SessionedGithubObject"]:
    #         yield "base: " + klass.base.name
    #     if len(klass.structures) != 0:
    #         yield "structures:"
    #         for structure in klass.structures:
    #             yield "  - name: " + structure.name
    #             yield "    attributes:"
    #             for attribute in structure.attributes:
    #                 yield "      - name: " + attribute.name
    #                 yield "        type: " + attribute.type.name
    #             if len(structure.deprecatedAttributes) != 0:
    #                 yield "    deprecated_attributes:"
    #                 for attribute in structure.deprecatedAttributes:
    #                     yield "      - " + attribute
    #     if len(klass.attributes) != 0:
    #         yield "attributes:"
    #         for attribute in klass.attributes:
    #             yield "  - name: " + attribute.name
    #             if attribute.type.category in ["builtin", "struct", "class"]:
    #                 yield "    type: " + attribute.type.name
    #             elif attribute.type.category == "union":
    #                 yield "    types: [" + ", ".join(t.name for t in attribute.type.types) + "]"
    #     if len(klass.deprecatedAttributes) != 0:
    #         yield "deprecated_attributes:"
    #         for attribute in klass.deprecatedAttributes:
    #             yield "  - " + attribute
    #     if len(klass.methods) != 0:
    #         yield "methods:"
    #         for method in klass.methods:
    #             yield "  - name: " + method.name
    #             yield "    end_point: " + method.endPoint.verb + " " + method.endPoint.url

    #             if not all(p.optional for p in method.parameters):
    #                 yield "    parameters:"
    #                 for parameter in method.parameters:
    #                     if not parameter.optional:
    #                         yield "      - name: " + parameter.name
    #                         if parameter.type.category == "union":
    #                             if parameter.type.types[0].name == "TwoStrings":
    #                                 yield "        types:"
    #                                 yield "          - TwoStrings"
    #                                 yield "          - string"
    #                             else:
    #                                 yield "        type: " + parameter.type.types[0].name
    #                         elif parameter.type.category in ["builtin"]:
    #                             yield "        type: " + parameter.type.name

    #             if any(p.optional and p.name != "per_page" for p in method.parameters):
    #                 yield "    optional_parameters:"
    #                 for parameter in method.parameters:
    #                     if parameter.optional and parameter.name != "per_page":
    #                         yield "      - name: " + parameter.name
    #                         if parameter.type.category == "enum":
    #                             yield "        type:"
    #                             yield "          meta: enum"
    #                             yield "          values: [" + ", ".join(parameter.type.values) + "]"
    #                         elif parameter.type.category == "union":
    #                             if parameter.type.types[1].name == "Reset":
    #                                 yield "        types: [" + parameter.type.types[0].name + ", Reset]"
    #                             else:
    #                                 yield "        type: " + parameter.type.types[0].name
    #                         elif parameter.type.category == "linear_collection":
    #                             yield "        type:"
    #                             yield "          meta: list"
    #                             yield "          type: " + parameter.type.content.name
    #                         elif parameter.type.category in ["builtin"]:
    #                             yield "        type: " + parameter.type.name

    #             if method.urlTemplate.origin in ["attribute", "parameter", "ownerFromRepo", "nameFromRepo"]:
    #                 yield "    url_template: " + method.urlTemplate.origin + " " + method.urlTemplate.value
    #             else:
    #                 yield "    url_template: " + method.urlTemplate.origin

    #             if len(method.urlTemplateArguments) != 0:
    #                 yield "    url_template_arguments:"
    #                 for urlTemplateArgument in method.urlTemplateArguments:
    #                     yield "      - name: " + urlTemplateArgument.name
    #                     yield "        value: " + urlTemplateArgument.value.origin + " " + urlTemplateArgument.value.value

    #             if any(a.name != "per_page" for a in method.urlArguments):
    #                 yield "    url_arguments:"
    #                 for urlArgument in method.urlArguments:
    #                     if urlArgument.name != "per_page":
    #                         yield "      - name: " + urlArgument.name
    #                         yield "        value: " + urlArgument.value.origin + " " + urlArgument.value.value

    #             if len(method.postArguments) != 0:
    #                 yield "    post_arguments:"
    #                 for postArgument in method.postArguments:
    #                     yield "      - name: " + postArgument.name
    #                     yield "        value: " + postArgument.value.origin + " " + postArgument.value.value

    #             if method.returnStrategy.name == "None":
    #                 yield "    return_strategy: none"
    #             elif method.returnStrategy.name == "Bool":
    #                 yield "    return_strategy: boolFromStatus"
    #             elif method.returnStrategy.name == "Instance":
    #                 yield "    return_strategy: instanceFromAttributes(" + method.returnStrategy.returnType.name + ")"
    #             elif method.returnStrategy.name == "Structure":
    #                 yield "    return_strategy: structFromAttributes(" + method.returnStrategy.returnType.name + ")"
    #             elif method.returnStrategy.name == "PaginatedList":
    #                 if method.returnStrategy.returnType.content.category == "union":
    #                     yield "    return_strategy: paginatedList(union(" + ", ".join(t.name for t in method.returnStrategy.returnType.content.types) + "))"
    #                 else:
    #                     yield "    return_strategy: paginatedList(" + method.returnStrategy.returnType.content.name + ")"
    #             elif method.returnStrategy.name == "PaginatedListWithoutPerPage":
    #                 yield "    return_strategy: paginatedListWithoutPerPage(" + method.returnStrategy.returnType.content.name + ")"
    #             elif method.returnStrategy.name == "UpdateSelf":
    #                 yield "    return_strategy: updateSelfThen(none)"
