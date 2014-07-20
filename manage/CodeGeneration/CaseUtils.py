# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import unittest


def toUpperCamel(s):
    return "".join(c[0].capitalize() + c[1:] for c in s.split("_") if c != "")


class TestCase(unittest.TestCase):
    def testUnderscoreToUpperCamelCase(self):
        self.assertEqual(toUpperCamel("foo"), "Foo")
        self.assertEqual(toUpperCamel("_foo"), "Foo")
        self.assertEqual(toUpperCamel("_foo_"), "Foo")
        self.assertEqual(toUpperCamel("foo_"), "Foo")
        self.assertEqual(toUpperCamel("foo_bar"), "FooBar")
        self.assertEqual(toUpperCamel("foo_bar_baz"), "FooBarBaz")

    def testUpperCamelToUpperCamel(self):
        self.assertEqual(toUpperCamel("Foo"), "Foo")
        self.assertEqual(toUpperCamel("FooBar"), "FooBar")
