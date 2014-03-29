# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime
import logging
import sys
import unittest

import MockMockMock

import PyGithub.Blocking.Exceptions
import PyGithub.Blocking._receive as rcv


class AttributeTestCase(unittest.TestCase):
    def setUp(self):
        self.mocks = MockMockMock.Engine()
        self.conv = self.mocks.create("conv")
        self.conv.expect.desc.andReturn("desc")
        self.a = rcv.Attribute("name", self.conv.object, rcv.Absent)

        self.log = logging.getLogger("PyGithub")
        for handler in self.log.handlers:
            self.log.removeHandler(handler)
        self.logHandler = self.mocks.create("log")
        self.log.addHandler(self.logHandler.object)

    def expectLog(self, level, *messages):
        def checkLogRecord(args, kwds):
            (logRecord,) = args
            if logRecord.levelno == level and str(logRecord.msg) in messages:
                return True
            else:
                print()
                print("checkLogRecord received")
                print(logRecord.levelno)
                print(logRecord.msg)
                print("instead of")
                print(level)
                print("\n".join(messages))
                print()
        self.logHandler.expect.level.andReturn(logging.DEBUG)
        self.logHandler.expect.handle.withArguments(checkLogRecord)

    def tearDown(self):
        self.mocks.tearDown()

    def testCreateAttribute(self):
        self.assertEqual(self.a.name, "name")
        self.assertEqual(self.a.value, None)

    def testUpdateAttributeWithAbsent(self):
        self.a.update(rcv.Absent)

        self.assertEqual(self.a.value, None)

    def testUpdateAttributeWithNone(self):
        self.a.update(None)

        self.assertEqual(self.a.value, None)

    def testUpdateAttributeWithValidValue(self):
        self.conv.expect(42).andReturn(42)

        self.a.update(42)

        self.assertEqual(self.a.value, 42)
        self.assertFalse(self.a.needsLazyCompletion)

    def testUpdateAttributeWithValidValueThenAbsent(self):
        self.conv.expect(42).andReturn(42)

        self.a.update(42)
        self.a.update(rcv.Absent)

        self.assertEqual(self.a.value, 42)

    def testUpdateAttributeWithValidValueThenNone(self):
        self.conv.expect(42).andReturn(42)

        self.a.update(42)
        self.a.update(None)

        self.assertEqual(self.a.value, None)

    def testUpdateAttributeWithInvalidValue(self):
        e = rcv._ConversionException()
        self.conv.expect(42).andRaise(e)
        self.expectLog(logging.WARN, "Attribute name is expected to be a desc but GitHub API v3 returned 42")

        self.a.update(42)

        with self.assertRaises(PyGithub.Blocking.Exceptions.BadAttributeException) as cm:
            self.a.value
        self.assertEqual(cm.exception.args, ("name", "desc", 42, e))
        self.assertFalse(self.a.needsLazyCompletion)

    def testUpdateTwice(self):
        v = []
        self.conv.expect(42).andReturn(v)
        self.conv.expect(43, v).andReturn(v)

        self.a.update(42)
        self.a.update(43)

        self.assertIs(self.a.value, v)

    def testUpdateAfterException(self):
        v = []
        self.conv.expect(42).andReturn(v)
        self.conv.expect(43, v).andRaise(rcv._ConversionException())
        self.expectLog(logging.WARN, "Attribute name is expected to be a desc but GitHub API v3 returned 43")
        self.conv.expect(44, v).andReturn(v)

        self.a.update(42)
        self.a.update(43)
        self.a.update(44)

        self.assertIs(self.a.value, v)

    def testNeedsLazyCompletion(self):
        self.assertTrue(self.a.needsLazyCompletion)


class BuiltinConverterTestCase(unittest.TestCase):
    def testIntegerConverterDescription(self):
        self.assertEqual(rcv.IntConverter.desc, "int")

    def testIntegerConversion(self):
        self.assertEqual(rcv.IntConverter(42), 42)

    def testBadIntegerConversion(self):
        with self.assertRaises(rcv._ConversionException):
            rcv.IntConverter("42")

    def testStringConverterDescription(self):
        self.assertEqual(rcv.StringConverter.desc, "str" if sys.hexversion >= 0x03000000 else "basestring")

    def testStringConversion(self):
        self.assertEqual(rcv.StringConverter("42"), "42")

    def testBadStringConversion(self):
        with self.assertRaises(rcv._ConversionException):
            rcv.StringConverter(42)

    def testDatetimeConverterDescription(self):
        self.assertEqual(rcv.DatetimeConverter.desc, "datetime")

    def testDatetimeConversionFromInt(self):
        self.assertEqual(rcv.DatetimeConverter(1395971262), datetime.datetime(2014, 3, 28, 1, 47, 42))

    def testDatetimeConversionFromString(self):
        self.assertEqual(rcv.DatetimeConverter("2010-07-09T06:10:06Z"), datetime.datetime(2010, 7, 9, 6, 10, 6))

    def testBadDatetimeConversion(self):
        with self.assertRaises(rcv._ConversionException):
            rcv.DatetimeConverter(4.5)

    def testBadDatetimeConversionFromString(self):
        with self.assertRaises(rcv._ConversionException):
            rcv.DatetimeConverter("foobar")


class ListConverterTestCase(unittest.TestCase):
    def setUp(self):
        self.mocks = MockMockMock.Engine()
        self.content = self.mocks.create("content")
        self.conv = rcv.ListConverter(self.content.object)

    def tearDown(self):
        self.mocks.tearDown()

    def testDescription(self):
        self.content.expect.desc.andReturn("desc")
        self.assertEqual(self.conv.desc, "list of desc")

    def testGoodConversion(self):
        self.content.expect(42).andReturn("42")
        self.content.expect(43).andReturn("43")

        self.assertEqual(self.conv([42, 43]), ["42", "43"])

    def testNotAList(self):
        with self.assertRaises(rcv._ConversionException):
            self.conv(42)

    def testBadElement(self):
        self.content.expect(42).andReturn("42")
        self.content.expect(43).andRaise(rcv._ConversionException())

        with self.assertRaises(rcv._ConversionException):
            self.conv([42, 43, 44])

    def testSecondConversionKeepsInstance(self):
        self.content.expect(42).andReturn("42")
        self.content.expect(43).andReturn("43")
        self.content.expect(44).andReturn("44")
        self.content.expect(45).andReturn("45")

        list1 = self.conv([42, 43])
        list2 = self.conv([44, 45], list1)

        self.assertEqual(list2, ["44", "45"])
        self.assertIs(list2, list1)


class StructureConverterTestCase(unittest.TestCase):
    class TheStruct(object):
        def __init__(self, session, attributes):
            self.Session = session
            self.__foo = rcv.Attribute("TheStruct.foo", rcv.StringConverter, rcv.Absent)
            self._updateAttributes(**attributes)

        @property
        def foo(self):
            return self.__foo.value

        def _updateAttributes(self, foo=rcv.Absent, **kwds):
            self.__foo.update(foo)

    def setUp(self):
        self.session = (42,)
        self.conv = rcv.StructureConverter(self.session, self.TheStruct)

    def testDescription(self):
        self.assertEqual(self.conv.desc, "TheStruct")

    def testConversion(self):
        instance = self.conv({"foo": "bar"})
        self.assertEqual(instance.foo, "bar")
        self.assertIs(instance.Session, self.session)

    def testConversionFromEmptyDict(self):
        instance = self.conv({})
        self.assertEqual(instance.foo, None)

    def testConversionWithUnexpectedKeys(self):
        instance = self.conv({"toto": "tutu"})
        self.assertEqual(instance.foo, None)

    def testTwoConversions(self):
        instance1 = self.conv({"foo": "bar"})
        self.assertEqual(instance1.foo, "bar")
        instance2 = self.conv({"foo": "baz"}, instance1)
        self.assertIs(instance2, instance1)
        self.assertEqual(instance2.foo, "baz")

    def testFailedConversion(self):
        with self.assertRaises(rcv._ConversionException):
            self.conv([])


class ClassConverterTestCase(unittest.TestCase):
    class TheClass(object):
        def __init__(self, session, attributes, eTag):
            self.Session = session
            self.__foo = rcv.Attribute("TheClass.foo", rcv.StringConverter, rcv.Absent)
            self._updateAttributes(eTag, **attributes)

        @property
        def foo(self):
            return self.__foo.value

        def _updateAttributes(self, eTag, foo=rcv.Absent, **kwds):
            self.eTag = eTag
            self.__foo.update(foo)

    def setUp(self):
        self.session = (42,)
        self.conv = rcv.ClassConverter(self.session, self.TheClass)

    def testDescription(self):
        self.assertEqual(self.conv.desc, "TheClass")

    def testConversion(self):
        instance = self.conv({"foo": "bar"})
        self.assertEqual(instance.foo, "bar")
        self.assertIs(instance.Session, self.session)
        self.assertIsNone(instance.eTag)

    def testTwoConversions(self):
        instance1 = self.conv({"foo": "bar"})
        self.assertEqual(instance1.foo, "bar")
        instance2 = self.conv({"foo": "baz"}, instance1)
        self.assertIs(instance2, instance1)
        self.assertEqual(instance2.foo, "baz")


class KeyedStructureUnionConverterTestCase(unittest.TestCase):
    def setUp(self):
        self.mocks = MockMockMock.Engine()
        self.conv1 = self.mocks.create("conv1")
        self.conv2 = self.mocks.create("conv2")
        self.instance1 = self.mocks.create("instance1")
        self.instance2 = self.mocks.create("instance2")
        self.conv = rcv.KeyedStructureUnionConverter(
            "key",
            {
                "val1": self.conv1.object,
                "val2": self.conv2.object,
            }
        )

    def tearDown(self):
        self.mocks.tearDown()

    def testDesc(self):
        with self.mocks.unordered:
            self.conv1.expect.desc.andReturn("desc1")
            self.conv2.expect.desc.andReturn("desc2")
        self.assertEqual(self.conv.desc, "desc1 or desc2")

    def testOneConversion(self):
        instance = self.instance1.object

        self.conv1.expect({"key": "val1"}).andReturn(instance)

        actual = self.conv({"key": "val1"})
        self.assertIs(actual, instance)

    def testBadKey(self):
        with self.assertRaises(rcv._ConversionException):
            self.conv({"key": "not_a_val"})

    def testNoKey(self):
        with self.assertRaises(rcv._ConversionException):
            self.conv({})

    def testNotADict(self):
        with self.assertRaises(rcv._ConversionException):
            self.conv(42)

    def testTwoConversionsOfSameKey(self):
        instance = self.instance1.object

        self.conv1.expect({"key": "val1", "foo": "bar"}).andReturn(instance)
        self.instance1.expect.key.andReturn("val1")
        self.conv1.expect({"key": "val1", "foo": "baz"}, instance).andReturn(instance)

        instance1 = self.conv({"key": "val1", "foo": "bar"})
        instance2 = self.conv({"key": "val1", "foo": "baz"}, instance1)
        self.assertIs(instance1, instance)
        self.assertIs(instance2, instance1)

    def testTwoConversionsOfDifferentKeys(self):
        self.conv1.expect({"key": "val1"}).andReturn(self.instance1.object)
        self.instance1.expect.key.andReturn("val1")
        self.conv2.expect({"key": "val2"}).andReturn(self.instance2.object)

        instance1 = self.conv({"key": "val1"})
        instance2 = self.conv({"key": "val2"}, instance1)
        self.assertIsNot(instance2, instance1)
