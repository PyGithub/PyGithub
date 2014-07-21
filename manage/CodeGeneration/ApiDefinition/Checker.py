# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import sys
assert sys.hexversion >= 0x03040000

import itertools
import unittest

import CodeGeneration.ApiDefinition.CrossReferenced as CrossReferenced
import CodeGeneration.ApiDefinition.Structured as Structured

# @todoAlpha Detect classes/structures with the same attributes (GitCommit.Author and GitTag.Tagger)


class Checker(object):
    def __init__(self, definition):
        self.definition = definition

    def check(self, *acknowledgedWarnings):  # pragma no cover
        acknowledgedWarnings = set(acknowledgedWarnings)
        for w in self.warnings():
            if w in acknowledgedWarnings:
                acknowledgedWarnings.remove(w)
            else:
                print("WARNING:", w)
        for w in acknowledgedWarnings:
            print("WARNING: \"", w, "\" was acknowledged but doesn't exist anymore")

    def warnings(self):
        yield from ("Class '{}' has no 'url' attribute".format(c.name) for c in self.classesWithoutUrl())
        yield from ("Struct '{}' is not updatable but is the type of attribute '{}' of class '{}'".format(s.name, a.name, c.name) for (c, s, a) in self.notUpdatableStructuresAttributeOfClass())
        yield from ("End-point '{} {}' is not implemented and not declared so".format(ep.verb, ep.url) for ep in self.unimplementedEndPointsNotDeclared())
        yield from ("End-point '{} {}' is declared as not implemented but is implemented by '{}.{}'".format(ep.verb, ep.url, m.containerClass.name, m.name) for (ep, m) in self.implementedEndPointsDeclaredUnimplemented())
        yield from ("Method '{}.{}' doesn't use its '{}' parameter".format(m.containerClass.name, m.name, p.name) for (m, p) in self.unusedParameters())
        yield from ("Method '{}.{}' doesn't implement the '{}' parameter of the '{} {}' end-point".format(m.containerClass.name, m.name, p, ep.verb, ep.url) for (m, ep, p) in self.unimplementedEndPointParametersNotDeclared())
        yield from ("In method '{}.{}', the '{}' parameter of the '{} {}' end-point is declared as not implemented but is implemented".format(m.containerClass.name, m.name, p, ep.verb, ep.url) for (m, ep, p) in self.implementedEndPointParametersDeclaredUnimplemented())
        yield from ("Method '{}.{}' tries to use unexisting parameter '{}'".format(m.containerClass.name, m.name, p) for (m, p) in self.unexistingParameters())
        yield from ("Method '{}.{}' re-orders the '{} {}' parameters ('{}') to ('{}')".format(m.containerClass.name, m.name, ep.verb, ep.url, "', '".join(ep.parameters), "', '".join(p.name for p in m.parameters)) for (m, ep) in self.reorderedParameters())

    def classesWithoutUrl(self):
        for c in self.definition.classes:
            if not self.classHasAttribute(c, "url"):
                yield c

    def notUpdatableStructuresAttributeOfClass(self):
        for c1 in self.definition.classes:
            for s in c1.structures:
                if not s.isUpdatable:
                    for c2 in self.definition.classes:
                        for a in c2.attributes:
                            if a.type.name == s.name:
                                yield c2, s, a

    def classHasAttribute(self, c, name):
        if hasattr(c.base, "attributes") and self.classHasAttribute(c.base, name):
            return True
        else:
            return any(a.name == name for a in c.attributes)

    def unimplementedEndPointsNotDeclared(self):
        unimplemented = set(self.definition.endPoints) - set(self.definition.unimplementedEndPoints)
        for c in self.definition.classes:
            for m in c.methods:
                for ep in m.endPoints:
                    unimplemented.discard(ep)
        return unimplemented

    def implementedEndPointsDeclaredUnimplemented(self):
        unimplemented = set(self.definition.unimplementedEndPoints)
        for c in self.definition.classes:
            for m in c.methods:
                for ep in m.endPoints:
                    if ep in unimplemented:
                        yield ep, m

    def unusedParameters(self):
        for c in self.definition.classes:
            for m in c.methods:
                for p in m.parameters:
                    for a in itertools.chain(m.urlTemplateArguments, m.urlArguments, m.postArguments):
                        if isinstance(a.value, CrossReferenced.ParameterValue) and a.value.parameter == p.name:
                            break
                        if isinstance(a.value, CrossReferenced.RepositoryOwnerValue) and a.value.repository == p.name:
                            break
                        if isinstance(a.value, CrossReferenced.RepositoryNameValue) and a.value.repository == p.name:
                            break
                    else:
                        yield m, p

    def unimplementedEndPointParametersNotDeclared(self):
        for c in self.definition.classes:
            for m in c.methods:
                for ep in m.endPoints:
                    unimplemented = set(ep.parameters) - set(m.unimplementedParameters)
                    for p in m.parameters:
                        unimplemented.discard(p.name)
                    for p in unimplemented:
                        yield m, ep, p

    def implementedEndPointParametersDeclaredUnimplemented(self):
        for c in self.definition.classes:
            for m in c.methods:
                for ep in m.endPoints:
                    unimplemented = set(m.unimplementedParameters)
                    for p in m.parameters:
                        if p.name in unimplemented:
                            yield m, ep, p.name

    def unexistingParameters(self):
        for c in self.definition.classes:
            for m in c.methods:
                for a in itertools.chain(m.urlTemplateArguments, m.urlArguments, m.postArguments):
                    if isinstance(a.value, CrossReferenced.ParameterValue):
                        for p in m.parameters:
                            if p.name == a.value.parameter:
                                break
                        else:
                            yield m, a.value.parameter

    def reorderedParameters(self):
        for c in self.definition.classes:
            for m in c.methods:
                for ep in m.endPoints:
                    methodParams = [p.name for p in m.parameters if p.name in ep.parameters]
                    epParams = [p for p in ep.parameters if p in methodParams]
                    if methodParams != epParams:
                        yield m, ep


class CheckerTestCase(unittest.TestCase):
    def expect(self, d, *warnings):
        typesRepo = CrossReferenced.TypesRepository()
        typesRepo.register(CrossReferenced.BuiltinType("string"))
        self.assertEqual(set(Checker(CrossReferenced.Definition(d, typesRepo)).warnings()), set(warnings))

    def testNoUrlInClass(self):
        d = Structured.Definition(
            (),
            (
                Structured.Class("Foo", None, (), (), (), ()),
            ),
            ()
        )
        self.expect(d, "Class 'Foo' has no 'url' attribute")

    def testNoUrlInClassWithBase(self):
        d = Structured.Definition(
            (),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (), ()),
                Structured.Class("Foo", Structured.ScalarType("Bar",), (), (), (), ()),
            ),
            ()
        )
        self.expect(d)

    def testNotUpdatableStructureIsAttributeOfClass(self):
        d = Structured.Definition(
            (),
            (
                Structured.Class("Foo", None, (Structured.Structure("Stru", False, (), ()),), (Structured.Attribute("url", Structured.ScalarType("string")), Structured.Attribute("attr", Structured.ScalarType("Stru"))), (), ()),
            ),
            ()
        )
        self.expect(d, "Struct 'Stru' is not updatable but is the type of attribute 'attr' of class 'Foo'")

    def testUnimplementedEndPointNotDeclared(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", (), ""),
            ),
            (),
            ()
        )
        self.expect(d, "End-point 'GET /foo' is not implemented and not declared so")

    def testUnimplementedEndPointDeclared(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/bar", (), ""),
            ),
            (),
            (("family", (("/bar", ("GET",)),)),)
        )
        self.expect(d)

    def testImplementedEndPoint(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", (), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (), (), Structured.EndPointValue(), (), (), (), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d)

    def testImplementedEndPointDeclaredAsUnimplemented(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", (), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (), (), Structured.EndPointValue(), (), (), (), (), None, Structured.NoneType),), ()),
            ),
            (("family", (("/foo", ("GET",)),)),)
        )
        self.expect(d, "End-point 'GET /foo' is declared as not implemented but is implemented by 'Bar.get_foo'")

    def testUnusedParameter(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", (), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (Structured.Parameter("bar", Structured.ScalarType("string"), False),), (), Structured.EndPointValue(), (), (), (), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d, "Method 'Bar.get_foo' doesn't use its 'bar' parameter")

    def testParameterUsedAsUrlTemplateArgument(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", (), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (Structured.Parameter("bar", Structured.ScalarType("string"), False),), (), Structured.EndPointValue(), (Structured.Argument("baz", Structured.ParameterValue("bar",)),), (), (), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d)

    def testParameterUsedAsUrlArgument(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", (), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (Structured.Parameter("bar", Structured.ScalarType("string"), False),), (), Structured.EndPointValue(), (), (Structured.Argument("baz", Structured.ParameterValue("bar",)),), (), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d)

    def testParameterUsedAsPostArgument(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", (), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (Structured.Parameter("bar", Structured.ScalarType("string"), False),), (), Structured.EndPointValue(), (), (), (Structured.Argument("baz", Structured.ParameterValue("bar",)),), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d)

    def testParameterUsedAsRepoOwnerInUrlTemplateArgument(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", (), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (Structured.Parameter("bar", Structured.ScalarType("string"), False),), (), Structured.EndPointValue(), (Structured.Argument("baz", Structured.RepositoryOwnerValue("bar",)),), (), (), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d)

    def testParameterUsedAsRepoOwnerInUrlArgument(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", (), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (Structured.Parameter("bar", Structured.ScalarType("string"), False),), (), Structured.EndPointValue(), (), (Structured.Argument("baz", Structured.RepositoryOwnerValue("bar",)),), (), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d)

    def testParameterUsedAsRepoOwnerInPostArgument(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", (), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (Structured.Parameter("bar", Structured.ScalarType("string"), False),), (), Structured.EndPointValue(), (), (), (Structured.Argument("baz", Structured.RepositoryOwnerValue("bar",)),), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d)

    def testParameterUsedAsRepoNameInUrlTemplateArgument(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", (), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (Structured.Parameter("bar", Structured.ScalarType("string"), False),), (), Structured.EndPointValue(), (Structured.Argument("baz", Structured.RepositoryNameValue("bar",)),), (), (), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d)

    def testParameterUsedAsRepoNameInUrlArgument(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", (), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (Structured.Parameter("bar", Structured.ScalarType("string"), False),), (), Structured.EndPointValue(), (), (Structured.Argument("baz", Structured.RepositoryNameValue("bar",)),), (), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d)

    def testParameterUsedAsRepoNameInPostArgument(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", (), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (Structured.Parameter("bar", Structured.ScalarType("string"), False),), (), Structured.EndPointValue(), (), (), (Structured.Argument("baz", Structured.RepositoryNameValue("bar",)),), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d)

    def testUnimplementedEndPointParameterNotDeclared(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", ("bar",), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (), (), Structured.EndPointValue(), (), (), (), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d, "Method 'Bar.get_foo' doesn't implement the 'bar' parameter of the 'GET /foo' end-point")

    def testUnimplementedEndPointParameterDeclared(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", ("bar",), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (), ("bar",), Structured.EndPointValue(), (), (), (), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d)

    def testImplementedEndPointParameterDeclaredAsUnimplemented(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", ("bar",), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (Structured.Parameter("bar", Structured.ScalarType("string"), False),), ("bar",), Structured.EndPointValue(), (), (Structured.Argument("baz", Structured.ParameterValue("bar",)),), (), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d, "In method 'Bar.get_foo', the 'bar' parameter of the 'GET /foo' end-point is declared as not implemented but is implemented")

    def testImplementedEndPointParameter(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", ("bar",), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (Structured.Parameter("bar", Structured.ScalarType("string"), False),), (), Structured.EndPointValue(), (), (Structured.Argument("baz", Structured.ParameterValue("bar",)),), (), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d)

    def testOderedEndPointParameter(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", ("c", "a", "b"), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (Structured.Parameter("c", Structured.ScalarType("string"), False), Structured.Parameter("b", Structured.ScalarType("string"), False)), ("a"), Structured.EndPointValue(), (), (Structured.Argument("baz", Structured.ParameterValue("b")), Structured.Argument("foo", Structured.ParameterValue("c"))), (), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d)

    def testUnoderedEndPointParameter(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", ("c", "a", "b"), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (Structured.Parameter("b", Structured.ScalarType("string"), False), Structured.Parameter("c", Structured.ScalarType("string"), False)), ("a"), Structured.EndPointValue(), (), (Structured.Argument("baz", Structured.ParameterValue("b")), Structured.Argument("foo", Structured.ParameterValue("c"))), (), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d, "Method 'Bar.get_foo' re-orders the 'GET /foo' parameters ('c', 'a', 'b') to ('b', 'c')")

    def testUnexistingParameterUsedAsUrlTemplateArgument(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", (), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (), (), Structured.EndPointValue(), (Structured.Argument("baz", Structured.ParameterValue("bar",)),), (), (), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d, "Method 'Bar.get_foo' tries to use unexisting parameter 'bar'")

    def testUnexistingParameterUsedAsUrlArgument(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", (), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (), (), Structured.EndPointValue(), (), (Structured.Argument("baz", Structured.ParameterValue("bar",)),), (), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d, "Method 'Bar.get_foo' tries to use unexisting parameter 'bar'")

    def testUnexistingParameterUsedAsPostArgument(self):
        d = Structured.Definition(
            (
                Structured.EndPoint("GET", "/foo", (), ""),
            ),
            (
                Structured.Class("Bar", None, (), (Structured.Attribute("url", Structured.ScalarType("string")),), (Structured.Method("get_foo", ("GET /foo",), (), (), Structured.EndPointValue(), (), (), (Structured.Argument("baz", Structured.ParameterValue("bar",)),), (), None, Structured.NoneType),), ()),
            ),
            ()
        )
        self.expect(d, "Method 'Bar.get_foo' tries to use unexisting parameter 'bar'")
