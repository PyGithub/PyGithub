# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import collections
import datetime
import logging
log = logging.getLogger(__name__)

import PyGithub.Blocking.Exceptions

"""
This module is a bit contrieved because of the following goals:

1) Lazy completion should be done only when strictly necessary, that is when the user
accesses an attribute that has never been returned by GitHub.

2) Whenever GitHub returns data that PyGithub can't interpret as the expected type,
we want to log a warning as soon as possible, but we want to defer raising the actual
exception for as long as we can.

A few examples:

If PyGithub expects a bool and GitHub sends a string, then PyGithub should raise the
BadAttributeException when the user accesses the attribute.

If PyGithub expects a list of bool and GitHub sends [true, false, "foobar"],
PyGithub should raise the BadAttributeException only when the user accesses the attribute.
(We can't raise later because we need to present the attribute as a plain list of booleans)

If PyGithub expects a list of a Structured type with a boolean attribute b, and GitHub
returns [{"b": true}, {"b": "foobar"}], then PyGithub should raise when the user accesses
the .b property of the second element of the list.
"""


Absent = collections.namedtuple("Absent", "")()


class _ConversionException(Exception):
    pass


class Attribute(object):
    def __init__(self, name, conv, value):
        self.__name = name
        self.__conv = conv
        self.__type = conv.desc
        self.__value = Absent
        self.__exception = None
        self.update(value)

    def update(self, value):
        if value is Absent:
            return
        self.__exception = None
        if value is None:
            self.__value = None
        else:
            try:
                # Passing the previous value to conv(..) allows it to update
                # the value if needed (instead of just overriding it)
                self.__value = self.__conv(None if self.__value is Absent else self.__value, value)
            except _ConversionException, e:
                log.warn("Attribute " + self.__name + " is expected to be a " + self.__type + " but GitHub API v3 returned " + repr(value))
                self.__exception = PyGithub.Blocking.Exceptions.BadAttributeException(self.__name, self.__type, value, e)

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        if self.__exception is None:
            if self.__value is Absent:
                return None
            else:
                return self.__value
        else:
            raise self.__exception

    @property
    def needsLazyCompletion(self):
        return self.__value is Absent and self.__exception is None


class BuiltinConverter(object):
    def __init__(self, type):
        self.__type = type

    def __call__(self, previousValue, value):
        if isinstance(value, self.__type):
            return value
        else:
            raise _ConversionException()

    @property
    def desc(self):
        return self.__type.__name__


IntConverter = BuiltinConverter(int)
StringConverter = BuiltinConverter(basestring)
BoolConverter = BuiltinConverter(bool)


class _DatetimeConverter(object):
    desc = "datetime"

    def __call__(self, previousValue, value):
        if isinstance(value, int):
            return datetime.datetime.utcfromtimestamp(value)
        else:
            try:
                return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
            except (ValueError, TypeError), e:
                raise _ConversionException(e)


DatetimeConverter = _DatetimeConverter()


class ListConverter(object):
    def __init__(self, content):
        self.__content = content

    def __call__(self, previousValue, value):
        if isinstance(value, list):
            new = [self.__content(None, v) for v in value]  # @todoAlpha Pass the previousValue instead of None
            if previousValue is None:
                return new
            else:
                previousValue[:] = new
                return previousValue
        else:
            raise _ConversionException()

    @property
    def desc(self):
        return "list of " + self.__content.desc


class _StructureConverter(object):
    def __init__(self, session, struct):
        self.__session = session
        self.__struct = struct

    def __call__(self, previousValue, value):
        if isinstance(value, dict):
            if previousValue is None:
                return self.create(self.__struct, self.__session, value)
            else:
                self.update(previousValue, value)
                return previousValue
        else:
            raise _ConversionException()

    @property
    def desc(self):
        return self.__struct.__name__


class StructureConverter(_StructureConverter):
    def create(self, type, session, value):
        return type(session, value)

    def update(self, previousValue, value):
        previousValue._updateAttributes(**value)


class ClassConverter(_StructureConverter):
    def create(self, type, session, value):
        return type(session, value, None)

    def update(self, previousValue, value):
        previousValue._updateAttributes(None, **value)


class KeyedStructureUnionConverter(object):
    def __init__(self, key, factories):
        self.__key = key
        self.__factories = factories

    def __call__(self, previousValue, value):
        if isinstance(value, dict):
            key = value.get(self.__key)
            if key is None:
                raise _ConversionException()
            else:
                factory = self.__factories.get(key)
                if factory is None:
                    raise _ConversionException()
                else:
                    if previousValue is not None and getattr(previousValue, self.__key) != key:
                        previousValue = None
                    return factory(previousValue, value)
        else:
            raise _ConversionException()

    @property
    def desc(self):
        return " or ".join(sorted(c.desc for c in self.__factories.values()))
