# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import collections
import datetime
import logging
log = logging.getLogger(__name__)

import PyGithub.Blocking.Exceptions
import PyGithub.Blocking.PaginatedList

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

    def update(self, value, *args, **kwds):
        if value is Absent:
            return
        self.__exception = None
        if value is None:
            self.__value = None
        else:
            try:
                # Passing the previous value to conv(..) allows it to update
                # the value if needed (instead of just overriding it)
                if self.__value is Absent:
                    self.__value = self.__conv(None, value, *args, **kwds)
                else:
                    self.__value = self.__conv(self.__value, value, *args, **kwds)
            except _ConversionException as e:
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


class _BuiltinConverter(object):
    def __init__(self, type):
        self.__type = type

    def __call__(self, previousValue, value):
        if isinstance(value, self.__type):
            return value
        else:
            raise _ConversionException("Not a " + self.desc)

    @property
    def desc(self):
        return self.__type.__name__


IntConverter = _BuiltinConverter(int)
StringConverter = _BuiltinConverter(basestring)
BoolConverter = _BuiltinConverter(bool)


class _DatetimeConverter(object):
    desc = "datetime"

    def __call__(self, previousValue, value):
        if isinstance(value, int):
            return datetime.datetime.utcfromtimestamp(value)
        else:
            try:
                return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
            except (ValueError, TypeError) as e:
                raise _ConversionException(e)


DatetimeConverter = _DatetimeConverter()


class ListConverter(object):
    def __init__(self, content):
        self.__content = content

    def __call__(self, previousValue, value):
        if not isinstance(previousValue, list):
            previousValue = []
        if isinstance(value, list):
            if len(value) == len(previousValue):
                new = [self.__content(pv, v) for pv, v in zip(previousValue, value)]
            else:
                new = [self.__content(None, v) for v in value]
            previousValue[:] = new
            return previousValue
        else:
            raise _ConversionException("Not a list")

    @property
    def desc(self):
        return "list of " + self.__content.desc


class PaginatedListConverter(object):
    def __init__(self, session, content):
        self.__session = session
        self.__content = content

    def __call__(self, previousValue, r):
        return PyGithub.Blocking.PaginatedList.PaginatedList(self.__session, self.__content, r)

    @property
    def desc(self):
        return "PaginatedList of " + self.__content.desc


class DictConverter(object):
    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def __call__(self, previousValue, value):
        if not isinstance(previousValue, dict):
            previousValue = {}
        if isinstance(value, dict):
            new = {kk: self.__value(previousValue.get(kk), v) for kk, v in ((self.__key(None, k), v) for k, v in value.iteritems())}
            previousValue.clear()
            previousValue.update(new)
            return previousValue
        else:
            raise _ConversionException("Not a dict")

    @property
    def desc(self):
        return "dict of " + self.__key.desc + " to " + self.__value.desc


class _StructureConverter(object):
    def __init__(self, session, struct):
        self.__session = session
        self.__struct = struct

    def __call__(self, previousValue, value, eTag=None):
        if isinstance(value, dict):
            if previousValue is None or previousValue.__class__ is not self.__struct:
                return self.create(self.__struct, self.__session, value, eTag)
            else:
                self.update(previousValue, value, eTag)
                return previousValue
        else:
            raise _ConversionException("Not a dict")

    @property
    def desc(self):
        return self.__struct.__name__


class StructureConverter(_StructureConverter):
    def create(self, type, session, value, eTag):
        return type(session, value)

    def update(self, previousValue, value, eTag):
        previousValue._updateAttributes(**value)


class ClassConverter(_StructureConverter):
    def create(self, type, session, value, eTag):
        return type(session, value, eTag)

    def update(self, previousValue, value, eTag):
        previousValue._updateAttributes(eTag, **value)


class KeyedStructureUnionConverter(object):
    def __init__(self, key, convs):
        self.__key = key
        self.__convs = convs

    def __call__(self, previousValue, value):
        if isinstance(value, dict):
            key = value.get(self.__key)
            if key is None:
                raise _ConversionException("No " + self.__key + " attribute")
            else:
                conv = self.__convs.get(key)
                if conv is None:
                    raise _ConversionException("No converter for key " + key)
                else:
                    return conv(previousValue, value)
        else:
            raise _ConversionException("Not a dict")

    @property
    def desc(self):
        return " or ".join(sorted(c.desc for c in self.__convs.itervalues()))


class FileDirSubmoduleSymLinkUnionConverter(object):
    def __init__(self, file, dir, submodule, symlink):
        self.__file = file
        self.__dir = dir
        self.__submodule = submodule
        self.__symlink = symlink
        self.__convs = (file, dir, submodule, symlink)

    def __call__(self, previousValue, value):
        if isinstance(value, dict):
            type = value.get("type")
            gitUrl = value.get("git_url", "")
            if type == "file" and "/git/trees/" in gitUrl:  # https://github.com/github/developer.github.com/commit/1b329b04cece9f3087faa7b1e0382317a9b93490
                return self.__submodule(previousValue, value)
            elif type == "file":
                return self.__file(previousValue, value)
            elif type == "symlink":
                return self.__symlink(previousValue, value)
            elif type == "dir":
                return self.__dir(previousValue, value)
            else:
                raise _ConversionException()
        else:
            raise _ConversionException("Not a dict")

    @property
    def desc(self):
        return " or ".join(c.desc for c in self.__convs)


class FirstMatchUnionConverter(object):
    def __init__(self, *convs):
        self.__convs = convs

    def __call__(self, previousValue, value):
        for conv in self.__convs:
            try:
                return conv(previousValue, value)
            except _ConversionException:
                pass
        raise _ConversionException()

    @property
    def desc(self):
        return " or ".join(sorted(c.desc for c in self.__convs))
