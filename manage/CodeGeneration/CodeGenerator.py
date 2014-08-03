# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import sys
assert sys.hexversion >= 0x03040000

import CodeGeneration.PythonSnippets as PS
from CodeGeneration.CaseUtils import toUpperCamel


# @todoAlpha Implement the following, rephrase it and put it in the "rationales" doc
# About Completability and Updatability
#  - this does not apply to the Github class
#  - all classes have a 'url' attribute (things that don't are structures)
#  - all classes are lazilly completable, even if there is no use case for this now (like AuthenticatedUser which is always returned fully) to be future-proof
#  - all classes are updatable (have a .update method), even if they represent immutable objects (like GitTag), and in that case, .update always returns False, but this keeps the interface consistent
#  - structures are updatable (have a ._updateAttributes method) iif they are (recursively) an attribute of a class. (This is currently not enforced, and instead specified manually in the .yml file)
# Examples of classes:
#   mutable     returned partially      examples
#   True        True                    User
#   True        False                   AuthenticatedUser
#   False       True                    GitCommit
#   False       False                   GitTag
# Examples of structures:
#   updatable   examples
#   True        AuthenticatedUser.Plan
#   False       Github.GitIgnoreTemplate

# CodeGeneration.ApiDefinition.Structured
# @todoAlpha go back to the PaginatedListWithoutPerPage model; remove the warning "returns paginated list but has no per_page"

# CodeGeneration.ApiDefinition.CrossReferenced
# @todoAlpha for methods returning a PaginatedList (with per_page), add parameter per_page. Or at least reimplement the warning

# CodeGeneration.CodeGenerator
# @todoAlpha remove special cases :-/

# CodeGeneration.RstGenerator
# @todoAlpha document the sha from developer.github.com
# @todoAlpha document how many end-points are implemented and unimplemented

# Global
# @todoAlpha hide UpdatableGithubObject.update and generate an update method for each class
# @todoAlpha assert url is not none in any updatable instance
# @todoAlpha test lazy completion and update of all classes in two topic test cases, not in each class test case? Maybe?
# @todoAlpha What happens when a suspended enterprise user tries to do anything?


class CodeGenerator:
    def generateClass(self, klass):
        yield "import uritemplate"
        yield ""
        yield "import PyGithub.Blocking._base_github_object as _bgo"
        yield "import PyGithub.Blocking._send as _snd"
        yield "import PyGithub.Blocking._receive as _rcv"
        if klass.base is not None:
            yield ""
            yield "import {}".format(self.computeModuleNameFor(klass.base))
        yield ""
        yield ""

        if klass.base is None:
            if klass.qualifiedName == "Github":
                baseName = "_bgo.SessionedGithubObject"
            else:
                baseName = "_bgo.UpdatableGithubObject"
        else:
            baseName = self.computeFullyQualifiedName(klass.base)

        yield from (
            PS.Class(klass.simpleName)
            .base(baseName)
            .docstring(self.generateDocStringForClass(klass, baseName))
            .elements(self.createClassStructure(s) for s in klass.structures)
            .elements(self.createClassPrivateParts(klass))
            .elements(self.createClassProperty(a) for a in klass.attributes)
            .elements(self.createClassMethod(m) for m in klass.methods)
        )

    def generateDocStringForClass(self, klass, baseName):
        yield "Base class: :class:`.{}`".format(baseName.split(".")[-1])
        yield ""
        if len(klass.derived) == 0:
            yield "Derived classes: none."
        else:
            yield "Derived classes:"
            for d in klass.derived:
                yield "  * :class:`.{}`".format(d.qualifiedName)
        yield ""
        yield from self.generateDocForSourcesAndSinks(klass)

    def generateDocForSourcesAndSinks(self, klass):
        assert len(klass.sources) != 0
        yield "Methods and attributes returning instances of this class:"
        for source in klass.sources:
            yield "  * {}".format(self.generateDocForSource(source))
        yield ""
        if len(klass.sinks) == 0:
            yield "Methods accepting instances of this class as parameter: none."
        else:
            yield "Methods accepting instances of this class as parameter:"
            for sink in klass.sinks:
                yield "  * {}".format(self.generateDocForSink(sink))

    def generateDocForSource(self, source):
        return self.getMethod("generateDocFor{}", source.__class__.__name__)(source)

    def generateDocForMethodSource(self, source):
        return ":meth:`.{}`".format(source.object.qualifiedName)

    def generateDocForAttributeSource(self, source):
        return ":attr:`.{}`".format(source.object.qualifiedName)

    def generateDocForSink(self, sink):
        return ":meth:`.{}`".format(sink.object.qualifiedName)

    def createClassStructure(self, structure):
        return (
            PS.Class(structure.simpleName)
            .base("_bgo.SessionedGithubObject")
            .docstring(self.generateDocForSourcesAndSinks(structure))
            .elements(self.createStructPrivateParts(structure))
            .elements(self.createStructProperty(a) for a in structure.attributes)
        )

    def createStructPrivateParts(self, structure):
        yield (  # pragma no cover
            PS.Method("_initAttributes")
            .parameters((a.simpleName, "None") for a in structure.attributes)
            .parameters((a, "None") for a in structure.deprecatedAttributes)
            .parameter("**kwds")
            .body(self.generateImportsForAllUnderlyingTypes(structure, [a.type for a in structure.attributes]))
            .body("super({}, self)._initAttributes(**kwds)".format(structure.qualifiedName))
            .body("self.__{} = {}".format(a.simpleName, self.createCallForAttributeInitializer(a)) for a in structure.attributes)
        )
        if structure.isUpdatable:
            yield(
                PS.Method("_updateAttributes")
                .parameters((a.simpleName, "None") for a in structure.attributes)
                .parameters((a, "None") for a in structure.deprecatedAttributes)
                .parameter("**kwds")
                .body("super({}, self)._updateAttributes(**kwds)".format(structure.qualifiedName))
                .body("self.__{0}.update({0})".format(a.simpleName) for a in structure.attributes)
            )

    def createStructProperty(self, attribute):
        return (
            PS.Property(attribute.simpleName)
            .docstring(":type: {}".format(self.generateDocForType(attribute.type)))
            .body("return self.__{}.value".format(attribute.simpleName))
        )

    def createClassPrivateParts(self, klass):
        if len(klass.attributes) != 0:
            yield (  # pragma no cover
                PS.Method("_initAttributes")
                .parameters((a.simpleName, "_rcv.Absent") for a in klass.attributes)
                .parameters((a, "None") for a in klass.deprecatedAttributes)
                .parameter("**kwds")
                .body(self.generateImportsForAllUnderlyingTypes(klass, [a.type for a in klass.attributes]))
                .body("super({}, self)._initAttributes(**kwds)".format(klass.qualifiedName))
                .body("self.__{} = {}".format(a.simpleName, self.createCallForAttributeInitializer(a)) for a in klass.attributes)
            )
            yield (
                PS.Method("_updateAttributes")
                .parameter("eTag")
                .parameters((a.simpleName, "_rcv.Absent") for a in klass.attributes)
                .parameters((a, "None") for a in klass.deprecatedAttributes)
                .parameter("**kwds")
                .body("super({}, self)._updateAttributes(eTag, **kwds)".format(klass.qualifiedName))
                .body("self.__{0}.update({0})".format(a.simpleName) for a in klass.attributes)
            )

    def generateImportsForAllUnderlyingTypes(self, klass, types):
        imports = set()
        for type in types:
            for t in type.underlyingTypes:
                if t.__class__.__name__ == "Class" and t is not klass and t.qualifiedName != "PaginatedList":
                    imports.add(self.computeModuleNameFor(t))
                if t.__class__.__name__ == "Structure" and klass.__class__.__name__ == "Class" and t.containerClass is not klass:
                    imports.add(self.computeModuleNameFor(t))
        for i in sorted(imports):
            yield "import {}".format(i)

    def createCallForAttributeInitializer(self, attribute):
        return (
            PS.Call("_rcv.Attribute")
            .arg('"{}"'.format(attribute.qualifiedName))
            .arg(self.generateCodeForConverter(attribute, attribute.type))
            .arg(attribute.simpleName)
        )

    def generateCodeForConverter(self, attribute, type):
        return "_rcv.{}".format(self.getMethod("generateCodeFor{}Converter", type.__class__.__name__)(attribute, type))

    def generateCodeForLinearCollectionConverter(self, attribute, type):
        return self.getMethod("generateCodeFor{}Converter", type.container.simpleName)(attribute, type)

    def generateCodeForListConverter(self, attribute, type):
        return "ListConverter({})".format(self.generateCodeForConverter(attribute, type.content))

    def generateCodeForPaginatedListConverter(self, attribute, type):
        return "PaginatedListConverter(self.Session, {})".format(self.generateCodeForConverter(attribute, type.content))

    def generateCodeForMappingCollectionConverter(self, attribute, type):
        return "DictConverter({}, {})".format(self.generateCodeForConverter(attribute, type.key), self.generateCodeForConverter(attribute, type.value))

    def generateCodeForBuiltinTypeConverter(self, attribute, type):
        return "{}Converter".format(toUpperCamel(type.simpleName))

    def generateCodeForClassConverter(self, attribute, type):
        # @todoAlpha computeContextualName(attribute.qualifiedName, type.qualifiedName) ?
        if self.computeModuleNameFor(type) == self.computeModuleNameFor(attribute.containerClass):
            typeName = type.qualifiedName
        else:
            typeName = self.computeFullyQualifiedName(type)
        return "ClassConverter(self.Session, {})".format(typeName)

    def generateCodeForUnionTypeConverter(self, attribute, type):
        if type.key is not None:
            converters = {k: self.generateCodeForConverter(attribute, t) for k, t in zip(type.keys, type.types)}
            return 'KeyedStructureUnionConverter("{}", dict({}))'.format(type.key, ", ".join("{}={}".format(k, v) for k, v in sorted(converters.items())))
        elif type.converter is not None:
            return '{}UnionConverter({})'.format(
                type.converter,
                ", ".join(self.generateCodeForConverter(attribute, t) for t in type.types)
            )
        else:
            return '{}UnionConverter({})'.format(
                "".join(t.simpleName for t in type.types),
                ", ".join(self.generateCodeForConverter(attribute, t) for t in type.types)
            )

    def generateCodeForStructureConverter(self, attribute, type):
        # @todoAlpha computeContextualName(attribute.qualifiedName, type.qualifiedName) ?
        if self.computeModuleNameFor(type.containerClass) == self.computeModuleNameFor(attribute.containerClass):
            typeName = type.qualifiedName
        else:
            typeName = self.computeFullyQualifiedName(type)
        return "StructureConverter(self.Session, {})".format(typeName)

    def createClassProperty(self, attribute):
        return (
            PS.Property(attribute.simpleName)
            .docstring(":type: {}".format(self.generateDocForType(attribute.type)))
            .body("self._completeLazily(self.__{}.needsLazyCompletion)".format(attribute.simpleName))
            .body("return self.__{}.value".format(attribute.simpleName))
        )

    def createClassMethod(self, method):
        return (
            PS.Method(method.simpleName)
            .parameters((p.name, "None") if p.optional else "*{}".format(p.name) if p.variable else p.name for p in method.parameters)
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
                        yield "  * :meth:`.{}`".format(otherMethod.qualifiedName)
            else:
                yield "This is the only method calling this end point."
            yield ""
        for parameter in method.parameters:
            yield ":param {}: {} {}".format(
                parameter.name,
                "optional" if parameter.optional else "mandatory",
                self.generateDocForType(parameter.type)
            )
        yield ":rtype: {}".format(self.generateDocForType(method.returnType))

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
                    yield "    per_page = _snd.normalizeInt(per_page)"
                elif method.qualifiedName == "Github.get_repo" and p.name == "repo":
                    yield "repo = _snd.normalizeTwoStringsString(repo)"
                elif p.optional:
                    yield "if {} is not None:".format(p.name)
                    yield from PS.indent(self.generateCodeToNormalizeParameter(p))
                elif p.variable and p.name == "email":
                    yield "email = _snd.normalizeList(_snd.normalizeString, email)"
                elif p.variable and p.name == "label":
                    yield "label = _snd.normalizeList(_snd.normalizeLabelName, label)"
                else:
                    yield from self.generateCodeToNormalizeParameter(p)
            yield ""

        # @todoSomeday Open an issue to Github to make name optional in PATCH /repository
        if method.qualifiedName == "Repository.edit":
            yield "if name is None:"
            yield "    name = self.name"
            yield ""

        if method.qualifiedName == "Repository.get_git_ref":
            yield "assert ref.startswith(\"refs/\")"
            yield "url = uritemplate.expand(self.git_refs_url) + ref[4:]"
        elif method.qualifiedName == "GitTree.create_modified_copy":
            yield "url = self.url[:self.url.rfind(self.sha) - 1]"
        elif len(method.urlTemplateArguments) == 0:
            yield "url = uritemplate.expand({})".format(self.generateCodeForValue(method, method.urlTemplate))
        else:
            yield "url = uritemplate.expand({}, {})".format(self.generateCodeForValue(method, method.urlTemplate), ", ".join("{}={}".format(a.name, self.generateCodeForStringValue(method, a.value)) for a in method.urlTemplateArguments))  # pragma no branch
        if len(method.urlArguments) != 0:
            yield "urlArguments = _snd.dictionary({})".format(", ".join("{}={}".format(a.name, self.generateCodeForValue(method, a.value)) for a in method.urlArguments))  # pragma no branch
        if len(method.postArguments) != 0:
            if method.qualifiedName in ["AuthenticatedUser.add_to_emails", "AuthenticatedUser.remove_from_emails"]:
                # @todoAlpha solve this special case by changing Method.postArguments to Method.postPaylod, polymorphic, with DictionaryPayload and DirectPayload. Also change Session._request's parameter.
                yield "postArguments = email"
            elif method.qualifiedName in ["Issue.add_to_labels", "Issue.set_labels"]:
                # @todoAlpha solve this special case by changing Method.postArguments to Method.postPaylod, polymorphic, with DictionaryPayload and DirectPayload. Also change Session._request's parameter.
                yield "postArguments = label"
            else:
                yield "postArguments = _snd.dictionary({})".format(", ".join("{}={}".format(a.name, self.generateCodeForValue(method, a.value)) for a in method.postArguments))  # pragma no branch

        yield "r = self.Session._request{}({})".format("Anonymous" if method.qualifiedName == "Github.create_anonymous_gist" else "", self.generateCallArguments(method))  # @todoSomeday Remove hard-coded method name
        yield from self.generateCodeForEffects(method)
        yield from self.generateCodeForReturnValue(method)

    def generateCodeToNormalizeParameter(self, parameter):
        # @todoAlpha To solve the "variable parameter needs to be normalized as list" case, don't pass the parameter but its type, and return a format string where the caller will substitute the param name
        yield from self.getMethod("generateCodeToNormalize{}Parameter", parameter.type.__class__.__name__)(parameter)

    def generateCodeToNormalizeEnumeratedTypeParameter(self, parameter):
        yield "{} = _snd.normalizeEnum({}, {})".format(parameter.name, parameter.name, ", ".join('"' + v + '"' for v in parameter.type.values))  # pragma no branch

    def generateCodeToNormalizeAttributeTypeParameter(self, parameter):
        yield "{} = _snd.normalize{}{}({})".format(parameter.name, parameter.type.type.simpleName, toUpperCamel(parameter.type.attribute.simpleName), parameter.name)

    def generateCodeToNormalizeUnionTypeParameter(self, parameter):
        yield "{} = _snd.normalize{}({})".format(parameter.name, "".join(((toUpperCamel(t.type.simpleName) + toUpperCamel(t.attribute.simpleName)) if t.__class__.__name__ == "AttributeType" else toUpperCamel(t.simpleName)) for t in parameter.type.types), parameter.name)  # pragma no branch

    def generateCodeToNormalizeBuiltinTypeParameter(self, parameter):
        yield "{} = _snd.normalize{}({})".format(parameter.name, toUpperCamel(parameter.type.qualifiedName), parameter.name)

    def generateCodeToNormalizeLinearCollectionParameter(self, parameter):
        yield from self.getMethod("generateCodeToNormalize{}Of{}Parameter", parameter.type.container.simpleName, parameter.type.content.__class__.__name__)(parameter)

    def generateCodeToNormalizeListOfAttributeTypeParameter(self, parameter):
        yield "{} = _snd.normalizeList(_snd.normalize{}{}, {})".format(parameter.name, parameter.type.content.type.simpleName, toUpperCamel(parameter.type.content.attribute.simpleName), parameter.name)

    def generateCodeToNormalizeListOfBuiltinTypeParameter(self, parameter):
        yield "{} = _snd.normalizeList(_snd.normalize{}, {})".format(parameter.name, toUpperCamel(parameter.type.content.simpleName), parameter.name)

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
        if method.returnType.__class__.__name__ == "NoneType_":
            return []
        else:
            if method.returnFrom is None:
                if method.returnType.__class__.__name__ == "Class":
                    args = 'r.json(), r.headers.get("ETag")'
                elif method.returnType.__class__.__name__ == "LinearCollection" and method.returnType.container.qualifiedName == "PaginatedList":
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
            yield "return {}(None, {})".format(self.generateCodeForConverter(method, method.returnType), args)

    def generateCallArguments(self, m):
        args = '"{}", url'.format(m.endPoints[0].verb)
        if m.returnType.qualifiedName == "bool":
            args += ", accept404=True"
        if len(m.urlArguments) != 0:
            args += ", urlArguments=urlArguments"
        if len(m.postArguments) != 0:
            args += ", postArguments=postArguments"
        return args

    def generateDocForType(self, type):
        return self.getMethod("generateDocFor{}", type.__class__.__name__)(type)

    def generateDocForBuiltinType(self, type):
        return ":class:`{}`".format(type.qualifiedName)

    def generateDocForClass(self, type):
        return ":class:`.{}`".format(type.qualifiedName)

    def generateDocForAttributeType(self, type):
        if type.attribute.qualifiedName == "Repository.full_name":
            return ":class:`.Repository` or :class:`string` (its :attr:`.Repository.full_name`) or :class:`(string, string)` (its owner's :attr:`.Entity.login` and :attr:`.Repository.name`)"
        else:
            return ":class:`.{}` or :class:`{}` (its :attr:`.{}`)".format(type.type.qualifiedName, type.attribute.type.qualifiedName, type.attribute.qualifiedName)

    def generateDocForEnumeratedType(self, type):
        return " or ".join('"' + v + '"' for v in type.values)

    def generateDocForLinearCollection(self, type):
        return "{} of {}".format(self.generateDocForType(type.container), self.generateDocForType(type.content))

    def generateDocForMappingCollection(self, type):
        return "{} of {} to {}".format(self.generateDocForType(type.container), self.generateDocForType(type.key), self.generateDocForType(type.value))

    def generateDocForNoneType(self, type):
        return "None"

    def generateDocForStructure(self, type):
        return ":class:`.{}`".format(type.qualifiedName)

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
        if value.__class__.__name__[:-5] == "Parameter":
            p = [p for p in method.parameters if p.name == value.parameter][0]
            if p.type.qualifiedName in ["int"]:
                format = "str({})"
        if value.__class__.__name__[:-5] == "Attribute":
            a = self.findAttribute(method.containerClass, value.attribute)
            if a is not None and a.type.qualifiedName in ["int"]:
                format = "str({})"
        return format.format(self.generateCodeForValue(method, value))

    def getMethod(self, scheme, *names):
        name = scheme.format(*(toUpperCamel(name) for name in names))
        return getattr(self, name)

    def findAttribute(self, t, n):
        for a in t.attributes:
            if a.simpleName == n:
                return a
        if t.base is not None:
            return self.findAttribute(t.base, n)

    def computeModuleNameFor(self, t):
        return self.getMethod("computeModuleNameFor{}", t.__class__.__name__)(t)

    def computeModuleNameForClass(self, t):
        return "PyGithub.Blocking.{}".format(t.simpleName)

    def computeModuleNameForStructure(self, t):
        return self.computeModuleNameFor(t.containerClass)

    def computeFullyQualifiedName(self, t):
        return "{}.{}".format(self.computeModuleNameFor(t), t.qualifiedName)
