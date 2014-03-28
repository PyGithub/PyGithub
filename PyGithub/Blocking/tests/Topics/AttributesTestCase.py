# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime
import logging
import unittest

import MockMockMock

import PyGithub.Blocking.Attributes


class AttributeTestCase(unittest.TestCase):
    def setUp(self):
        self.mocks = MockMockMock.Engine()
        self.conv = self.mocks.create("conv")
        self.conv.expect.desc.andReturn("desc")
        self.a = PyGithub.Blocking.Attributes.Attribute("name", self.conv.object, PyGithub.Blocking.Attributes.Absent)

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
        self.a.update(PyGithub.Blocking.Attributes.Absent)

        self.assertEqual(self.a.value, None)

    def testUpdateAttributeWithValidValue(self):
        self.conv.expect(None, 42).andReturn(42)

        self.a.update(42)

        self.assertEqual(self.a.value, 42)

    def testUpdateAttributeWithValidValueThenAbsent(self):
        self.conv.expect(None, 42).andReturn(42)

        self.a.update(42)
        self.a.update(PyGithub.Blocking.Attributes.Absent)

        self.assertEqual(self.a.value, 42)

    def testUpdateAttributeWithInvalidValue(self):
        e = PyGithub.Blocking.Attributes._ConversionException()
        self.conv.expect(None, 42).andRaise(e)
        self.expectLog(logging.WARN, "Attribute name is expected to be a desc but GitHub API v3 returned 42")

        self.a.update(42)

        with self.assertRaises(PyGithub.Blocking.Exceptions.BadAttributeException) as cm:
            self.a.value
        self.assertEqual(cm.exception.args, ("name", "desc", 42, e))

    def testUpdateTwice(self):
        v = []
        self.conv.expect(None, 42).andReturn(v)
        self.conv.expect(v, 43).andReturn(v)

        self.a.update(42)
        self.a.update(43)

        self.assertIs(self.a.value, v)

    def testUpdateAfterException(self):
        v = []
        self.conv.expect(None, 42).andReturn(v)
        self.conv.expect(v, 43).andRaise(PyGithub.Blocking.Attributes._ConversionException())
        self.expectLog(logging.WARN, "Attribute name is expected to be a desc but GitHub API v3 returned 43")
        self.conv.expect(v, 44).andReturn(v)

        self.a.update(42)
        self.a.update(43)
        self.a.update(44)

        self.assertIs(self.a.value, v)


class BuiltinConverterTestCase(unittest.TestCase):
    def testIntegerConverterDescription(self):
        self.assertEqual(PyGithub.Blocking.Attributes.IntConverter.desc, "int")

    def testIntegerConversion(self):
        self.assertEqual(PyGithub.Blocking.Attributes.IntConverter(None, 42), 42)

    def testBadIntegerConversion(self):
        with self.assertRaises(PyGithub.Blocking.Attributes._ConversionException):
            PyGithub.Blocking.Attributes.IntConverter(None, "42")

    def testStringConverterDescription(self):
        self.assertEqual(PyGithub.Blocking.Attributes.StringConverter.desc, "basestring")

    def testStringConversion(self):
        self.assertEqual(PyGithub.Blocking.Attributes.StringConverter(None, "42"), "42")

    def testBadStringConversion(self):
        with self.assertRaises(PyGithub.Blocking.Attributes._ConversionException):
            PyGithub.Blocking.Attributes.StringConverter(None, 42)

    def testDatetimeConverterDescription(self):
        self.assertEqual(PyGithub.Blocking.Attributes.DatetimeConverter.desc, "datetime")

    def testDatetimeConversionFromInt(self):
        self.assertEqual(PyGithub.Blocking.Attributes.DatetimeConverter(None, 1395971262), datetime.datetime(2014, 3, 28, 1, 47, 42))

    def testDatetimeConversionFromString(self):
        self.assertEqual(PyGithub.Blocking.Attributes.DatetimeConverter(None, "2010-07-09T06:10:06Z"), datetime.datetime(2010, 7, 9, 6, 10, 6))

    def testBadDatetimeConversion(self):
        with self.assertRaises(PyGithub.Blocking.Attributes._ConversionException):
            PyGithub.Blocking.Attributes.DatetimeConverter(None, 4.5)

    def testBadDatetimeConversionFromString(self):
        with self.assertRaises(PyGithub.Blocking.Attributes._ConversionException):
            PyGithub.Blocking.Attributes.DatetimeConverter(None, "foobar")


class ListConverterTestCase(unittest.TestCase):
    def setUp(self):
        self.mocks = MockMockMock.Engine()
        self.content = self.mocks.create("content")
        self.conv = PyGithub.Blocking.Attributes.ListConverter(self.content.object)

    def tearDown(self):
        self.mocks.tearDown()

    def testDescription(self):
        self.content.expect.desc.andReturn("desc")
        self.assertEqual(self.conv.desc, "list of desc")

    def testGoodConversion(self):
        self.content.expect(None, 42).andReturn("42")
        self.content.expect(None, 43).andReturn("43")

        self.assertEqual(self.conv(None, [42, 43]), ["42", "43"])

    def testNotAList(self):
        with self.assertRaises(PyGithub.Blocking.Attributes._ConversionException):
            self.conv(None, 42)

    def testBadElement(self):
        self.content.expect(None, 42).andReturn("42")
        self.content.expect(None, 43).andRaise(PyGithub.Blocking.Attributes._ConversionException())

        with self.assertRaises(PyGithub.Blocking.Attributes._ConversionException):
            self.conv(None, [42, 43, 44])

    def testSecondConversionKeepsInstance(self):
        self.content.expect(None, 42).andReturn("42")
        self.content.expect(None, 43).andReturn("43")
        self.content.expect(None, 44).andReturn("44")
        self.content.expect(None, 45).andReturn("45")

        list1 = self.conv(None, [42, 43])
        list2 = self.conv(list1, [44, 45])

        self.assertEqual(list2, ["44", "45"])
        self.assertIs(list2, list1)


class StructureConverterTestCase(unittest.TestCase):
    class TheStruct(object):
        def __init__(self, session, attributes):
            self.Session = session
            self.__foo = PyGithub.Blocking.Attributes.Attribute("TheStruct.foo", PyGithub.Blocking.Attributes.StringConverter, PyGithub.Blocking.Attributes.Absent)
            self._updateAttributes(**attributes)

        @property
        def foo(self):
            return self.__foo.value

        def _updateAttributes(self, foo=PyGithub.Blocking.Attributes.Absent, **kwds):
            self.__foo.update(foo)

    def setUp(self):
        self.session = (42,)
        self.conv = PyGithub.Blocking.Attributes.StructureConverter(self.session, self.TheStruct)

    def testDescription(self):
        self.assertEqual(self.conv.desc, "TheStruct")

    def testConversion(self):
        instance = self.conv(None, {"foo": "bar"})
        self.assertEqual(instance.foo, "bar")
        self.assertIs(instance.Session, self.session)

    def testConversionFromEmptyDict(self):
        instance = self.conv(None, {})
        self.assertEqual(instance.foo, None)

    def testConversionWithUnexpectedKeys(self):
        instance = self.conv(None, {"toto": "tutu"})
        self.assertEqual(instance.foo, None)

    def testTwoConversions(self):
        instance1 = self.conv(None, {"foo": "bar"})
        self.assertEqual(instance1.foo, "bar")
        instance2 = self.conv(instance1, {"foo": "baz"})
        self.assertIs(instance2, instance1)
        self.assertEqual(instance2.foo, "baz")

    def testFailedConversion(self):
        with self.assertRaises(PyGithub.Blocking.Attributes._ConversionException):
            self.conv(None, [])


class KeyedStructureUnionConverterTestCase(unittest.TestCase):
    def setUp(self):
        self.mocks = MockMockMock.Engine()
        self.conv1 = self.mocks.create("conv1")
        self.conv2 = self.mocks.create("conv2")
        self.instance1 = self.mocks.create("instance1")
        self.instance2 = self.mocks.create("instance2")
        self.conv = PyGithub.Blocking.Attributes.KeyedStructureUnionConverter(
            "key",
            {
                "val1": self.conv1.object,
                "val2": self.conv2.object,
            }
        )

    def tearDown(self):
        self.mocks.tearDown()

    def testOneConversion(self):
        instance = self.instance1.object

        self.conv1.expect(None, {"key": "val1"}).andReturn(instance)

        actual = self.conv(None, {"key": "val1"})
        self.assertIs(actual, instance)

    def testBadKey(self):
        with self.assertRaises(PyGithub.Blocking.Attributes._ConversionException):
            self.conv(None, {"key": "not_a_val"})

    def testNoKey(self):
        with self.assertRaises(PyGithub.Blocking.Attributes._ConversionException):
            self.conv(None, {})

    def testNotADict(self):
        with self.assertRaises(PyGithub.Blocking.Attributes._ConversionException):
            self.conv(None, 42)

    def testTwoConversionsOfSameKey(self):
        instance = self.instance1.object

        self.conv1.expect(None, {"key": "val1", "foo": "bar"}).andReturn(instance)
        self.instance1.expect.key.andReturn("val1")
        self.conv1.expect(instance, {"key": "val1", "foo": "baz"}).andReturn(instance)

        instance1 = self.conv(None, {"key": "val1", "foo": "bar"})
        instance2 = self.conv(instance1, {"key": "val1", "foo": "baz"})
        self.assertIs(instance1, instance)
        self.assertIs(instance2, instance1)

    def testTwoConversionsOfDifferentKeys(self):
        self.conv1.expect(None, {"key": "val1"}).andReturn(self.instance1.object)
        self.instance1.expect.key.andReturn("val1")
        self.conv2.expect(None, {"key": "val2"}).andReturn(self.instance2.object)

        instance1 = self.conv(None, {"key": "val1"})
        instance2 = self.conv(instance1, {"key": "val2"})
        self.assertIsNot(instance2, instance1)
