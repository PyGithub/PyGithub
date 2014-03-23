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
        yield "import PyGithub.Blocking.BaseGithubObject"
        yield "import PyGithub.Blocking.Parameters"
        yield "import PyGithub.Blocking.Attributes"
        if len(klass.dependencies) != 0:
            yield ""
            for d in klass.dependencies:
                yield "import {}".format(d.module)
        yield ""
        yield ""

        yield from (
            PS.Class(klass.name)
            .base(klass.base.module + "." + klass.base.name)
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
            .base("PyGithub.Blocking.BaseGithubObject.SessionedGithubObject")
            .docstring(self.generateDocForFactories(structure))
            .element(
                PS.Method("_initAttributes")
                .parameters((a.name, "None") for a in structure.attributes)
                .parameters((a, "None") for a in structure.deprecatedAttributes)
                .parameter("**kwds")
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
            yield (  # pragma no branch
                PS.Method("_initAttributes")
                .parameters((a.name, "PyGithub.Blocking.Attributes.Absent") for a in klass.attributes)
                .parameters((a, "None") for a in klass.deprecatedAttributes)
                .parameter("**kwds")
                .body("super({}, self)._initAttributes(**kwds)".format(klass.name))
                .body("self.__{} = {}".format(a.name, self.createCallForAttributeInitializer(a)) for a in klass.attributes)
            )
            yield (
                PS.Method("_updateAttributes")
                .parameter("eTag")
                .parameters((a.name, "PyGithub.Blocking.Attributes.Absent") for a in klass.attributes)
                .parameters((a, "None") for a in klass.deprecatedAttributes)
                .parameter("**kwds")
                .body("super({}, self)._updateAttributes(eTag, **kwds)".format(klass.name))
                .body("self.__{0}.update({0})".format(a.name) for a in klass.attributes)
            )

    def createCallForAttributeInitializer(self, attribute):
        return self.getMethod("createCallFor{}AttributeInitializer", attribute.type.category)(attribute)

    def createCallForBuiltinAttributeInitializer(self, attribute):
        return (
            PS.Call("PyGithub.Blocking.Attributes.{}Attribute".format(attribute.type.name.capitalize()))
            .arg(self.generateFullyQualifiedAttributeName(attribute))
            .arg(attribute.name)
        )

    def createCallForClassAttributeInitializer(self, attribute):
        if attribute.type.name == attribute.containerClass.name:
            type = attribute.type.name
        else:
            type = "{}.{}".format(attribute.type.module, attribute.type.name)
        return (
            PS.Call("PyGithub.Blocking.Attributes.ClassAttribute")
            .arg(self.generateFullyQualifiedAttributeName(attribute))
            .arg("self.Session")
            .arg(type)
            .arg(attribute.name)
        )

    def createCallForUnionAttributeInitializer(self, attribute):
        return (
            PS.Call("PyGithub.Blocking.Attributes.UnionAttribute")
            .arg(self.generateFullyQualifiedAttributeName(attribute))
            .arg("self.Session")
            .arg('"type"')
            .arg("dict({})".format(", ".join("{}={}.{}".format(t.name, t.module, t.name) for t in attribute.type.types)))
            .arg(attribute.name)
        )

    def createCallForStructAttributeInitializer(self, attribute):
        return (
            PS.Call("PyGithub.Blocking.Attributes.StructAttribute")
            .arg(self.generateFullyQualifiedAttributeName(attribute))
            .arg("self.Session")
            .arg("{}.{}".format(attribute.type.containerClass.name, attribute.type.name))
            .arg(attribute.name)
        )

    def generateFullyQualifiedAttributeName(self, attribute):
        name = [attribute.name]
        current = attribute
        while hasattr(current, "containerClass"):
            current = current.containerClass
            name.append(current.name)
        name.reverse()
        return '"{}"'.format(".".join(name))

    def createClassProperty(self, attribute):
        return (
            PS.Property(attribute.name)
            .docstring(":type: {}".format(self.generateDocForType(attribute.type)))
            .body("self._completeLazily(self.__{}.needsLazyCompletion)".format(attribute.name))
            .body("return self.__{}.value".format(attribute.name))
        )

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
                self.generateDocForType(parameter.type)
            )
        yield ":rtype: " + self.generateDocForType(method.returnType)

    def generateMethodBody(self, method):
        yield ""
        if len(method.parameters) != 0:
            for p in method.parameters:
                if p.optional:
                    yield "if {} is not None:".format(p.name)
                    if p.name == "since":
                        yield "    " + self.generateCodeToNormalizeParameterSince(p)
                    else:
                        yield "    " + self.generateCodeToNormalizeParameter(p)
                else:
                    yield self.generateCodeToNormalizeParameter(p)
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
            yield "urlArguments = PyGithub.Blocking.Parameters.dictionary({})".format(", ".join("{}={}".format(a.name, self.generateCodeForValue(method, a.value)) for a in method.urlArguments))  # pragma no branch
        if len(method.postArguments) != 0:
            yield "postArguments = PyGithub.Blocking.Parameters.dictionary({})".format(", ".join("{}={}".format(a.name, self.generateCodeForValue(method, a.value)) for a in method.postArguments))  # pragma no branch

        if not method.returnType.name.startswith("PaginatedList of"):
            yield "r = self.Session._request({})".format(self.generateCallArguments(method))
        yield from self.generateCodeForEffects(method)
        yield from self.generateCodeForReturnValue(method)

    def generateCodeToNormalizeParameter(self, parameter):
        return self.getMethod("generateCodeToNormalize{}Parameter", parameter.type.category)(parameter)

    def generateCodeToNormalizeEnumParameter(self, parameter):
        return "{} = PyGithub.Blocking.Parameters.normalizeEnum({}, {})".format(parameter.name, parameter.name, ", ".join('"' + v + '"' for v in parameter.type.values))  # pragma no branch

    def generateCodeToNormalizeUnionParameter(self, parameter):
        if parameter.type.types[0].category == "class":
            t = parameter.type.types[0]
            return "{} = PyGithub.Blocking.Parameters.normalize{}({})".format(parameter.name, self.capfirst(t.name), parameter.name)
        else:
            return "{} = PyGithub.Blocking.Parameters.normalize{}({})".format(parameter.name, "".join(self.capfirst(t.name) for t in parameter.type.types), parameter.name)  # pragma no branch

    def generateCodeToNormalizeBuiltinParameter(self, parameter):
        return "{} = PyGithub.Blocking.Parameters.normalize{}({})".format(parameter.name, self.capfirst(parameter.type.name), parameter.name)

    def generateCodeToNormalizeLinearCollectionParameter(self, parameter):
        return self.getMethod("generateCodeToNormalize{}Of{}Parameter", parameter.type.container.name, parameter.type.content.category)(parameter)

    def generateCodeToNormalizeListOfClassParameter(self, parameter):
        return "{} = PyGithub.Blocking.Parameters.normalizeList(PyGithub.Blocking.Parameters.normalize{}, {})".format(parameter.name, self.capfirst(parameter.type.content.name), parameter.name)

    def generateCodeToNormalizeParameterSince(self, parameter):
        t = parameter.type.types[0]
        return "{} = PyGithub.Blocking.Parameters.normalize{}Id({})".format(parameter.name, self.capfirst(t.name), parameter.name)

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
        yield from self.getMethod("generateCodeFor{}ReturnValue", method.returnType.category)(method)

    def generateCodeForNoneReturnValue(self, method):
        return []

    def generateCodeForClassReturnValue(self, method):
        if method.returnFrom is None:
            yield 'return {}(self.Session, r.json(), r.headers.get("ETag"))'.format(("" if method.returnType is method.containerClass else method.returnType.module + ".") + method.returnType.name)
        elif method.returnFrom == "json.commit":
            yield 'return {}(self.Session, r.json()["commit"], None)'.format(("" if method.returnType is method.containerClass else method.returnType.module + ".") + method.returnType.name)
        else:
            assert False  # pragma no cover

    def generateCodeForLinearCollectionReturnValue(self, method):
        yield from self.getMethod("generateCodeFor{}ReturnValue", method.returnType.container.name)(method)

    def generateCodeForPaginatedListReturnValue(self, method):
        yield from self.getMethod("generateCodeForPaginatedListOf{}ReturnValue", method.returnType.content.category)(method)

    def generateCodeForPaginatedListOfClassReturnValue(self, method):
        yield "return PyGithub.Blocking.PaginatedList.PaginatedList({}, self.Session, {})".format(("" if method.returnType.content is method.containerClass else method.returnType.content.module + ".") + method.returnType.content.name, self.generateCallArguments(method))

    def generateCodeForPaginatedListOfUnionReturnValue(self, method):
        yield 'return PyGithub.Blocking.PaginatedList.PaginatedList(PyGithub.Blocking.Attributes.Switch("type", dict(Anonymous=lambda session, attributes, eTag: PyGithub.Blocking.Repository.Repository.AnonymousContributor(session, attributes), User=PyGithub.Blocking.Contributor.Contributor)), self.Session, {})'.format(self.generateCallArguments(method))

    def generateCodeForListReturnValue(self, method):
        yield from self.getMethod("generateCodeForListOf{}ReturnValue", method.returnType.content.category)(method)

    def generateCodeForListOfBuiltinReturnValue(self, method):
        yield "return r.json()"

    def generateCodeForListOfClassReturnValue(self, method):
        yield "return [{}(self.Session, a, None) for a in r.json()]".format(("" if method.returnType.content is method.containerClass else method.returnType.content.module + ".") + method.returnType.content.name)

    def generateCodeForListOfUnionReturnValue(self, method):
        yield 'return [PyGithub.Blocking.Attributes.Switch("type", dict(dir=PyGithub.Blocking.Dir.Dir, file=PyGithub.Blocking.File.File))(self.Session, a, None) for a in r.json()]'

    def generateCodeForBuiltinReturnValue(self, method):
        yield from self.getMethod("generateCodeFor{}ReturnValue", method.returnType.name)(method)

    def generateCodeForStructReturnValue(self, method):
        yield "return {}(self.Session, r.json())".format(method.containerClass.name + "." + method.returnType.name)

    def generateCodeForBoolReturnValue(self, method):
        yield "if r.status_code == 204:"  # To force coverage of both cases in all classes
        yield "    return True"
        yield "else:"
        yield "    return False"

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

    def generateDocForNoneType(self, type):
        return "None"

    def generateDocForStructType(self, type):
        return ":class:`.{}`".format(type.name)

    def generateDocForUnionType(self, type):
        return " or ".join(self.generateDocForType(st) for st in type.types)

    def generateCodeForValue(self, method, value):
        return self.getMethod("generateCodeForValueFrom{}", value.origin)(method, value)

    def generateCodeForValueFromEndPoint(self, method, value):
        return '"https://api.github.com{}"'.format(method.endPoints[0].urlTemplate)

    def generateCodeForValueFromAttribute(self, method, value):
        return "self.{}".format(value.value)

    def generateCodeForValueFromNameFromRepo(self, method, value):
        return "repo[1]"

    def generateCodeForValueFromOwnerFromRepo(self, method, value):
        return "repo[0]"

    def generateCodeForValueFromParameter(self, method, value):
        return value.value

    def generateCodeForStringValue(self, method, value):
        format = "{}"
        if value.value == "id":  # @todoGeni Test against the type instead of the name
            format = "str({})"
        return format.format(self.generateCodeForValue(method, value))

    def getMethod(self, scheme, *names):
        name = scheme.format(*("".join(part[0].capitalize() + part[1:] for part in name.split("_")) for name in names))
        return getattr(self, name)
