# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime
import logging
log = logging.getLogger(__name__)

import PyGithub.Blocking.Exceptions


class _Absent:
    pass
Absent = _Absent()


class _ValueHandler:
    needsLazyCompletion = False

    def getValidValue(self):
        return None


class __NoneValueHandler(_ValueHandler):
    def get(self):
        return None
_NoneValueHandler = __NoneValueHandler()


class __AbsentValueHandler(_ValueHandler):
    needsLazyCompletion = True

    def get(self):
        return None
_AbsentValueHandler = __AbsentValueHandler()


class _ValidValueHandler(_ValueHandler):
    def __init__(self, value):
        self.__value = value

    def get(self):
        return self.__value

    def getValidValue(self):
        return self.__value


class _InvalidValueHandler(_ValueHandler):
    def __init__(self, name, value, type):
        self.__exception = PyGithub.Blocking.Exceptions.BadAttributeException(name, type, value)
        log.warning(self.__exception)

    def get(self):
        raise self.__exception


class _Attribute(object):
    def __init__(self, name, value):
        self.__name = name
        self.__valueHandler = _AbsentValueHandler
        self.update(value)

    def setValidValue(self, value):
        self.__valueHandler = _ValidValueHandler(value)

    def setInvalidValue(self, value, type):
        self.__valueHandler = _InvalidValueHandler(self.__name, value, type)

    @property
    def value(self):
        return self.__valueHandler.get()

    def update(self, value):
        if value is None:
            self.__valueHandler = _NoneValueHandler
        elif value is not Absent:
            self.doUpdate(value)

    @property
    def needsLazyCompletion(self):
        return self.__valueHandler.needsLazyCompletion

    def getValidValue(self):
        return self.__valueHandler.getValidValue()


class DatetimeAttribute(_Attribute):
    def doUpdate(self, value):
        # @todoBeta Return "aware" datetimes
        # See https://gist.github.com/jul1an/5488075 for a start
        if isinstance(value, int):
            self.setValidValue(datetime.datetime.utcfromtimestamp(value))
        else:
            try:
                self.setValidValue(datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ"))
            except (ValueError, TypeError):
                self.setInvalidValue(value, datetime.datetime)


class _BuiltinAttribute(_Attribute):
    def __init__(self, name, type, value):
        self.__type = type
        _Attribute.__init__(self, name, value)

    def doUpdate(self, value):
        if isinstance(value, self.__type):
            self.setValidValue(value)
        else:
            self.setInvalidValue(value, self.__type)


class StringAttribute(_BuiltinAttribute):
    def __init__(self, name, value):
        _BuiltinAttribute.__init__(self, name, basestring, value)


class IntAttribute(_BuiltinAttribute):
    def __init__(self, name, value):
        _BuiltinAttribute.__init__(self, name, int, value)


class BoolAttribute(_BuiltinAttribute):
    def __init__(self, name, value):
        _BuiltinAttribute.__init__(self, name, bool, value)


class ListOfStringAttribute(_Attribute):
    def __init__(self, name, value):
        _Attribute.__init__(self, name, value)

    def doUpdate(self, value):
        if isinstance(value, list) and all(isinstance(e, basestring) for e in value):
            self.setValidValue(value)
        else:
            self.setInvalidValue(value, [str])


class ClassAttribute(_Attribute):
    def __init__(self, name, session, klass, value):
        self.__session = session
        self.__class = klass
        _Attribute.__init__(self, name, value)

    def doUpdate(self, value):
        if isinstance(value, dict):
            valid = self.getValidValue()
            if valid is None:
                self.setValidValue(self.__class(self.__session, value, None))
            else:
                valid._updateAttributes(None, **value)
        else:
            self.setInvalidValue(value, self.__class)


class StructAttribute(_Attribute):
    def __init__(self, name, session, struct, value):
        self.__session = session
        self.__struct = struct
        _Attribute.__init__(self, name, value)

    def doUpdate(self, value):
        if isinstance(value, dict):
            valid = self.getValidValue()
            if valid is None:
                self.setValidValue(self.__struct(self.__session, value))
            else:
                valid._updateAttributes(**value)
        else:
            self.setInvalidValue(value, self.__struct)


class Switch:
    def __init__(self, key, factories):
        self.__key = key
        self.__factories = factories

    def __call__(self, session, attributes, eTag):
        if self.__key in attributes:
            factory = self.__factories.get(attributes[self.__key])
            if factory is not None:
                return factory(session, attributes, eTag)
        return None

    def types(self):
        return sorted(self.__factories.itervalues(), key=lambda c: c.__name__)


class UnionAttribute(_Attribute):
    def __init__(self, name, session, key, factories, value):
        self.__session = session
        self.__switch = Switch(key, factories)
        _Attribute.__init__(self, name, value)

    def doUpdate(self, value):
        if isinstance(value, dict):
            valid = self.getValidValue()
            if valid is None:
                sValue = self.__switch(self.__session, value, None)
                if sValue is None:
                    self.__setInvalidValue(value)
                else:
                    self.setValidValue(sValue)
            else:
                valid._updateAttributes(None, **value)
        else:
            self.__setInvalidValue(value)

    def __setInvalidValue(self, value):
        self.setInvalidValue(value, self.__switch.types())
