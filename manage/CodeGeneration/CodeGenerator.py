# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import CodeGeneration.PythonSnippets as PS


class CodeGenerator:
    def generateClass(self, klass):
        yield "import logging"
        yield "log = logging.getLogger(__name__)"
        yield ""
        yield "import uritemplate"
        yield ""
        yield "import PyGithub.Blocking._base_github_object as bgo"
        yield "import PyGithub.Blocking._send as snd"
        yield "import PyGithub.Blocking._receive as rcv"
        if klass.base.module != "PyGithub.Blocking.BaseGithubObject":
            yield ""
            yield "import " + klass.base.module
        yield ""
        yield ""

        yield from (
            PS.Class(klass.name)
            .base((klass.base.module if klass.base.module != "PyGithub.Blocking.BaseGithubObject" else "bgo") + "." + klass.base.name)
            .docstring(self.generateDocStringForClass(klass))
            .elements(self.createClassStructure(s) for s in klass.structures)
            .elements(p for p in self.createClassPrivateParts(klass))
            .elements(self.createClassProperty(a) for a in klass.attributes)
            .elements(self.createClassMethod(m) for m in klass.methods)
        )

    def generateDocStringForClass(self, klass):
        yield "Base class: :class:`.{}`".format(klass.base.name)
        yield ""
        if len(klass.derived) == 0:
            yield "Derived classes: none."
        else:
            yield "Derived classes:"
            for d in klass.derived:
                yield "  * :class:`.{}`".format(d.name)
        yield ""
        yield from self.generateDocForFactories(klass)

    def generateDocForFactories(self, klass):
        if len(klass.factories) == 0:
            yield "Methods and attributes returning instances of this class: none."
        else:
            yield "Methods and attributes returning instances of this class:"
            for factory in klass.factories:
                yield "  * " + self.generateDocForFactory(factory)

    def generateDocForFactory(self, factory):
        return self.getMethod("generateDocFor{}Factory", factory.category)(factory)

    def generateDocForMethodFactory(self, factory):
        return ":meth:`.{}.{}`".format(factory.object.containerClass.name, factory.object.name)

    def generateDocForAttributeFactory(self, factory):
        return ":attr:`.{}.{}`".format(factory.object.containerClass.name, factory.object.name)

    def createClassStructure(self, structure):
        pyClass = (
            PS.Class(structure.name)
            .base("bgo.SessionedGithubObject")
            .docstring(self.generateDocForFactories(structure))
            .element(
                PS.Method("_initAttributes")
                .parameters((a.name, "None") for a in structure.attributes)
                .parameters((a, "None") for a in structure.deprecatedAttributes)
                .parameter("**kwds")
                .body(self.generateImportsForAllUnderlyingTypes(structure.containerClass.name, [a.type for a in structure.attributes]))
                .body("super({}.{}, self)._initAttributes(**kwds)".format(structure.containerClass.name, structure.name))
                .body("self.__{} = {}".format(a.name, self.createCallForAttributeInitializer(a)) for a in structure.attributes)
            )
        )
        if structure.isUpdatable:
            pyClass.element(
                PS.Method("_updateAttributes")
                .parameters((a.name, "None") for a in structure.attributes)
                .parameters((a, "None") for a in structure.deprecatedAttributes)
                .parameter("**kwds")
                .body("super({}.{}, self)._updateAttributes(**kwds)".format(structure.containerClass.name, structure.name))
                .body("self.__{0}.update({0})".format(a.name) for a in structure.attributes)
            )
        pyClass.elements(
            PS.Property(a.name)
            .docstring(":type: {}".format(self.generateDocForType(a.type)))
            .body("return self.__{}.value".format(a.name))
            for a in structure.attributes
        )
        return pyClass

    def createClassPrivateParts(self, klass):
        if len(klass.attributes) != 0:
            init = (
                PS.Method("_initAttributes")
                .parameters((a.name, "rcv.Absent") for a in klass.attributes)
                .parameters((a, "None") for a in klass.deprecatedAttributes)
                .parameter("**kwds")
            )
            init.body(self.generateImportsForAllUnderlyingTypes(klass, [a.type for a in klass.attributes]))
            yield (  # pragma no branch
                init
                .body("super({}, self)._initAttributes(**kwds)".format(klass.name))
                .body("self.__{} = {}".format(a.name, self.createCallForAttributeInitializer(a)) for a in klass.attributes)
            )
            if klass.isUpdatable:
                yield (
                    PS.Method("_updateAttributes")
                    .parameter("eTag")
                    .parameters((a.name, "rcv.Absent") for a in klass.attributes)
                    .parameters((a, "None") for a in klass.deprecatedAttributes)
                    .parameter("**kwds")
                    .body("super({}, self)._updateAttributes(eTag, **kwds)".format(klass.name))
                    .body("self.__{0}.update({0})".format(a.name) for a in klass.attributes)
                )

    def generateImportsForAllUnderlyingTypes(self, klass, types):
        imports = set()
        for type in types:
            for t in type.underlyingTypes:
                if t.category == "class" and t is not klass and t.module != "PyGithub.Blocking.BaseGithubObject":
                    imports.add(t.module)
        for i in sorted(imports):
            yield "import " + i

    def createCallForAttributeInitializer(self, attribute):
        return (
            PS.Call("rcv.Attribute")
            .arg(self.generateFullyQualifiedAttributeName(attribute))
            .arg(self.generateCodeForConverter("rcv", attribute, attribute.type))
            .arg(attribute.name)
        )

    def generateCodeForConverter(self, module, attribute, type):
        return module + "." + self.getMethod("generateCodeFor{}Converter", type.category)(module, attribute, type)

    def generateCodeForLinearCollectionConverter(self, module, attribute, type):
        return self.getMethod("generateCodeFor{}Converter", type.container.name)(module, attribute, type)

    def generateCodeForListConverter(self, module, attribute, type):
        return "ListConverter({})".format(self.generateCodeForConverter(module, attribute, type.content))

    def generateCodeForPaginatedListConverter(self, module, attribute, type):
        return "PaginatedListConverter(self.Session, {})".format(self.generateCodeForConverter(module, attribute, type.content))

    def generateCodeForMappingCollectionConverter(self, module, attribute, type):
        return "DictConverter({}, {})".format(self.generateCodeForConverter(module, attribute, type.key), self.generateCodeForConverter(module, attribute, type.value))

    def generateCodeForBuiltinConverter(self, module, attribute, type):
        return "{}Converter".format(type.name.capitalize())

    def generateCodeForClassConverter(self, module, attribute, type):
        if type.name == attribute.containerClass.name:
            typeName = type.name
        else:
            typeName = "{}.{}".format(type.module, type.name)
        if type.isUpdatable:
            converterName = "ClassConverter"
        else:
            converterName = "StructureConverter"
        return "{}(self.Session, {})".format(converterName, typeName)

    def generateCodeForUnionConverter(self, module, attribute, type):
        if type.key is not None:
            converters = {k: self.generateCodeForConverter(module, attribute, t) for k, t in zip(type.keys, type.types)}
            return 'KeyedStructureUnionConverter("{}", dict({}))'.format(type.key, ", ".join("{}={}".format(k, v) for k, v in sorted(converters.items())))
        elif type.converter is not None:
            return '{}UnionConverter({})'.format(
                type.converter,
                ", ".join(self.generateCodeForConverter(module, attribute, t) for t in type.types)
            )
        else:
            return '{}UnionConverter({})'.format(
                "".join(t.name for t in type.types),
                ", ".join(self.generateCodeForConverter(module, attribute, t) for t in type.types)
            )

    def generateCodeForStructConverter(self, module, attribute, type):
        return "StructureConverter(self.Session, {}.{})".format(type.containerClass.name, type.name)

    def generateFullyQualifiedAttributeName(self, attribute):
        name = [attribute.name]
        current = attribute
        while hasattr(current, "containerClass"):
            current = current.containerClass
            name.append(current.name)
        name.reverse()
        return '"{}"'.format(".".join(name))

    def createClassProperty(self, attribute):
        p = PS.Property(attribute.name)
        p.docstring(":type: {}".format(self.generateDocForType(attribute.type)))
        if attribute.containerClass.isUpdatable:
            p.body("self._completeLazily(self.__{}.needsLazyCompletion)".format(attribute.name))
        p.body("return self.__{}.value".format(attribute.name))
        return p

    def createClassMethod(self, method):
        return (
            PS.Method(method.name)
            .parameters((p.name, "None") if p.optional else p.name for p in method.parameters)
            .docstring(self.generateDocStringForMethod(method))
            .body(self.generateMethodBody(method))
        )

    def generateDocStringForMethod(self, method):
        # @todoSomeday Document the "or" aspect of a method calling several end-points
        for endPoint in method.endPoints:
            yield "Calls the `{} {} <{}>`__ end point.".format(endPoint.verb, endPoint.url, endPoint.doc)
            yield ""
            if len(endPoint.methods) > 1:
                yield "The following methods also call this end point:"
                for otherMethod in endPoint.methods:
                    if otherMethod is not method:
                        yield "  * :meth:`.{}.{}`".format(otherMethod.containerClass.name, otherMethod.name)
            else:
                yield "This is the only method calling this end point."
            yield ""
        for parameter in method.parameters:
            yield ":param {}: {} {}".format(
                parameter.name,
                "optional" if parameter.optional else "mandatory",
                # @todoGeni Fix the "its User.id" case: User inherits id from Entity and the doc has no link
                self.generateDocForType(parameter.type) + ("" if parameter.orig is None else " (its :attr:`.{}.{}`)".format(parameter.type.types[0].name, parameter.orig))
            )
        yield ":rtype: " + self.generateDocForType(method.returnType)

    def generateMethodBody(self, method):
        yield from self.generateImportsForAllUnderlyingTypes(method.containerClass, [method.returnType])
        yield ""
        if len(method.parameters) != 0:
            for p in method.parameters:
                if p.name == "files":  # @todoAlpha Remove this special case for AuthenticatedUser.create_gist when input type has been decided
                    pass
                elif p.name == "per_page":
                    yield "if per_page is None:"
                    yield "    per_page = self.Session.PerPage"
                    yield "else:"
                    yield "    per_page = snd.normalizeInt(per_page)"
                elif p.optional:
                    yield "if {} is not None:".format(p.name)
                    if p.name == "since" and method.name in ["get_users", "get_repos"]:
                        yield from PS.indent(self.generateCodeToNormalizeParameterSince(p))
                    else:
                        yield from PS.indent(self.generateCodeToNormalizeParameter(p))
                else:
                    yield from self.generateCodeToNormalizeParameter(p)
            yield ""

        # @todoSomeday Open an issue to Github to make name optional in PATCH /repository
        if method.containerClass.name == "Repository" and method.name == "edit":
            yield "if name is None:"
            yield "    name = self.name"
            yield ""

        if len(method.urlTemplateArguments) == 0:
            yield "url = uritemplate.expand({})".format(self.generateCodeForValue(method, method.urlTemplate))
        else:
            yield "url = uritemplate.expand({}, {})".format(self.generateCodeForValue(method, method.urlTemplate), ", ".join("{}={}".format(a.name, self.generateCodeForStringValue(method, a.value)) for a in method.urlTemplateArguments))  # pragma no branch
        if len(method.urlArguments) != 0:
            yield "urlArguments = snd.dictionary({})".format(", ".join("{}={}".format(a.name, self.generateCodeForValue(method, a.value)) for a in method.urlArguments))  # pragma no branch
        if len(method.postArguments) != 0:
            yield "postArguments = snd.dictionary({})".format(", ".join("{}={}".format(a.name, self.generateCodeForValue(method, a.value)) for a in method.postArguments))  # pragma no branch

        yield "r = self.Session._request{}({})".format("Anonymous" if method.name == "create_anonymous_gist" else "", self.generateCallArguments(method))  # @todoSomeday Remove hard-coded method name
        yield from self.generateCodeForEffects(method)
        yield from self.generateCodeForReturnValue(method)

    def generateCodeToNormalizeParameter(self, parameter):
        yield from self.getMethod("generateCodeToNormalize{}Parameter", parameter.type.category)(parameter)

    def generateCodeToNormalizeEnumParameter(self, parameter):
        yield "{} = snd.normalizeEnum({}, {})".format(parameter.name, parameter.name, ", ".join('"' + v + '"' for v in parameter.type.values))  # pragma no branch

    def generateCodeToNormalizeUnionParameter(self, parameter):
        if parameter.orig is None:
            # if parameter.type.types[0].category == "class":
            #     t = parameter.type.types[0]
            #     yield "{} = snd.normalize{}({})".format(parameter.name, self.capfirst(t.name), parameter.name)
            # else:
                if parameter.name == "repo":
                    yield "repo = snd.normalizeTwoStringsString(repo)"
                else:
                    yield "{} = snd.normalize{}({})".format(parameter.name, "".join(self.capfirst(t.name) for t in parameter.type.types), parameter.name)  # pragma no branch
        else:
            t = parameter.type.types[0]
            yield "{} = snd.normalize{}{}({})".format(parameter.name, self.capfirst(t.name), "".join(p.capitalize() for p in parameter.orig.split("_")), parameter.name)

    def generateCodeToNormalizeBuiltinParameter(self, parameter):
        yield "{} = snd.normalize{}({})".format(parameter.name, self.capfirst(parameter.type.name), parameter.name)

    def generateCodeToNormalizeLinearCollectionParameter(self, parameter):
        yield from self.getMethod("generateCodeToNormalize{}Of{}Parameter", parameter.type.container.name, parameter.type.content.category)(parameter)

    def generateCodeToNormalizeListOfClassParameter(self, parameter):
        yield "{} = snd.normalizeList(snd.normalize{}FullName, {})".format(parameter.name, self.capfirst(parameter.type.content.name), parameter.name)

    def generateCodeToNormalizeListOfBuiltinParameter(self, parameter):
        yield "{} = snd.normalizeList(snd.normalize{}, {})".format(parameter.name, self.capfirst(parameter.type.content.name), parameter.name)

    def generateCodeToNormalizeParameterSince(self, parameter):
        t = parameter.type.types[0]
        yield "{} = snd.normalize{}Id({})".format(parameter.name, self.capfirst(t.name), parameter.name)

    def generateCodeForEffects(self, method):
        for effect in method.effects:
            yield from self.generateCodeForEffect(method, effect)

    def generateCodeForEffect(self, method, effect):
        if effect == "update":
            yield 'self._updateAttributes(r.headers.get("ETag"), **r.json())'
        elif effect == "update from json.content":
            yield 'self._updateAttributes(None, **(r.json()["content"]))'
        elif effect == "update_attr content from parameter content":
            yield "self.__content.update(content)"
        else:
            assert False  # pragma no cover

    def generateCodeForReturnValue(self, method):
        if method.returnType.category == "none":
            return []
        else:
            if method.returnFrom is None:
                if method.returnType.category == "class":
                    args = 'r.json(), r.headers.get("ETag")'
                elif method.returnType.category == "linear_collection" and method.returnType.container.name == "PaginatedList":
                    args = "r"
                else:
                    args = "r.json()"
            elif method.returnFrom == "json":
                args = "r.json()"
            elif method.returnFrom == "status":
                args = "r.status_code == 204"
            elif method.returnFrom == "json.commit":
                args = 'r.json()["commit"]'
            else:
                assert False  # pragma no cover
            yield "return {}(None, {})".format(self.generateCodeForConverter("rcv", method, method.returnType), args)

    def generateCallArguments(self, m):
        args = '"{}", url'.format(m.endPoints[0].verb)
        if m.returnType.name == "bool":
            args += ", accept404=True"
        if len(m.urlArguments) != 0:
            args += ", urlArguments=urlArguments"
        if len(m.postArguments) != 0:
            args += ", postArguments=postArguments"
        return args

    def capfirst(self, s):
        return s[0].capitalize() + s[1:]

    def generateDocForType(self, type):
        return self.getMethod("generateDocFor{}Type", type.category)(type)

    def generateDocForBuiltinType(self, type):
        return ":class:`{}`".format(type.name)

    def generateDocForClassType(self, type):
        return ":class:`.{}`".format(type.name)

    def generateDocForEnumType(self, type):
        return " or ".join('"' + v + '"' for v in type.values)

    def generateDocForLinearCollectionType(self, type):
        return self.generateDocForType(type.container) + " of " + self.generateDocForType(type.content)

    def generateDocForMappingCollectionType(self, type):
        return self.generateDocForType(type.container) + " of " + self.generateDocForType(type.key) + " to " + self.generateDocForType(type.value)

    def generateDocForNoneType(self, type):
        return "None"

    def generateDocForStructType(self, type):
        return ":class:`.{}`".format(type.name)

    def generateDocForUnionType(self, type):
        return " or ".join(self.generateDocForType(st) for st in type.types)

    def generateCodeForValue(self, method, value):
        return self.getMethod("generateCodeFor{}", value.__class__.__name__)(method, value)

    def generateCodeForEndPointValue(self, method, value):
        return '"https://api.github.com{}"'.format(method.endPoints[0].urlTemplate)

    def generateCodeForAttributeValue(self, method, value):
        return "self.{}".format(value.attribute)

    def generateCodeForRepositoryNameValue(self, method, value):
        return "{}[1]".format(value.repository)

    def generateCodeForRepositoryOwnerValue(self, method, value):
        return "{}[0]".format(value.repository)

    def generateCodeForParameterValue(self, method, value):
        return value.parameter

    def generateCodeForStringValue(self, method, value):
        format = "{}"
        if value.__class__.__name__[:-5] == "Parameter" and value.parameter in ["id", "number"]:  # @todoGeni Test against the type instead of the name
            format = "str({})"
        if value.__class__.__name__[:-5] == "Attribute" and value.attribute == "id":  # @todoGeni Test against the type instead of the name
            format = "str({})"
        return format.format(self.generateCodeForValue(method, value))

    def getMethod(self, scheme, *names):
        name = scheme.format(*("".join(part[0].capitalize() + part[1:] for part in name.split("_")) for name in names))
        return getattr(self, name)
