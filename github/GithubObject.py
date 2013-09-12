# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
#                                                                              #
# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/          #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

import datetime

import GithubException
import Consts


class _NotSetType:
    def __repr__(self):
        return "NotSet"

    value = None
NotSet = _NotSetType()


class ValuedAttribute:
    def __init__(self, value):
        self.value = value


class GithubObject(object):
    """
    Base class for all classes representing objects returned by the API.
    """

    '''
    A global debug flag to enable header validation by requester for all objects
    '''
    CHECK_AFTER_INIT_FLAG = False

    @classmethod
    def setCheckAfterInitFlag(cls, flag):
        cls.CHECK_AFTER_INIT_FLAG = flag

    def __init__(self, requester, headers, attributes, completed):
        self._requester = requester
        self._initAttributes()
        self._storeAndUseAttributes(headers, attributes)

        # Ask requester to do some checking, for debug and test purpose
        # Since it's most handy to access and kinda all-knowing
        if self.CHECK_AFTER_INIT_FLAG:  # pragma no branch (Flag always set in tests)
            requester.check_me(self)

    def _storeAndUseAttributes(self, headers, attributes):
        # Make sure headers are assigned before calling _useAttributes
        # (Some derived classes will use headers in _useAttributes)
        self._headers = headers
        self._rawData = attributes
        self._useAttributes(attributes)

    @property
    def raw_data(self):
        """
        :type: dict
        """
        self._completeIfNeeded()
        return self._rawData

    @property
    def raw_headers(self):
        """
        :type: dict
        """
        self._completeIfNeeded()
        return self._headers

    @staticmethod
    def _parentUrl(url):
        return "/".join(url.split("/")[: -1])

    @staticmethod
    def __makeSimpleAttribute(value, type):
        if value is None or isinstance(value, type):
            return ValuedAttribute(value)
        else:
            return BadAttribute(value, type)

    @staticmethod
    def __makeSimpleListAttribute(value, type):
        if isinstance(value, list) and all(isinstance(element, type) for element in value):
            return ValuedAttribute(value)
        else:
            return BadAttribute(value, type)

    @staticmethod
    def __makeTransformedAttribute(value, type, transform):
        if value is None:
            return ValuedAttribute(None)
        elif isinstance(value, type):
            try:
                return ValuedAttribute(transform(value))
            except exception, e:
                return BadAttribute(value, type, e)
        else:
            return BadAttribute(value, type)

    @staticmethod
    def __makeTransformedListAttribute(value, type, transform):
        if isinstance(value, list) and all(isinstance(element, type) for element in value):
            try:
                return ValuedAttribute([transform(element) for element in value])
            except exception, e:
                return BadAttribute(value, type, e)
        else:
            return BadAttribute(value, type)

    @staticmethod
    def __makeTransformedDictAttribute(value, keyType, type, transform):
        if isinstance(value, dict) and all(isinstance(key, keyType) and isinstance(element, type) for key, element in value.iteritems()):
            try:
                return ValuedAttribute(dict((key, transform(element)) for key, element in value.iteritems()))
            except exception, e:
                return BadAttribute(value, type, e)
        else:
            return BadAttribute(value, type)

    @staticmethod
    def _makeStringAttribute(value):
        return GithubObject.__makeSimpleAttribute(value, (str, unicode))

    @staticmethod
    def _makeIntAttribute(value):
        return GithubObject.__makeSimpleAttribute(value, (int, long))

    @staticmethod
    def _makeBoolAttribute(value):
        return GithubObject.__makeSimpleAttribute(value, bool)

    @staticmethod
    def _makeDictAttribute(value):
        return GithubObject.__makeSimpleAttribute(value, dict)

    @staticmethod
    def _makeTimestampAttribute(value):
        return GithubObject.__makeTransformedAttribute(value, (int, long), datetime.datetime.utcfromtimestamp)

    @staticmethod
    def _makeDatetimeAttribute(value):
        def parseDatetime(s):
            if len(s) == 24:
                return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.000Z")
            elif len(s) == 25:
                return datetime.datetime.strptime(s[:19], "%Y-%m-%dT%H:%M:%S") + (1 if s[19] == '-' else -1) * datetime.timedelta(hours=int(s[20:22]), minutes=int(s[23:25]))
            else:
                return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")

        return GithubObject.__makeTransformedAttribute(value, (str, unicode), parseDatetime)

    def _makeClassAttribute(self, klass, value):
        return GithubObject.__makeTransformedAttribute(value, dict, lambda value: klass(self._requester, self._headers, value, completed=False))

    @staticmethod
    def _makeListOfStringsAttribute(value):
        return GithubObject.__makeSimpleListAttribute(value, (str, unicode))

    @staticmethod
    def _makeListOfListOfStringsAttribute(value):
        return GithubObject.__makeSimpleListAttribute(value, list)

    def _makeListOfClassesAttribute(self, klass, value):
        return GithubObject.__makeTransformedListAttribute(value, dict, lambda value: klass(self._requester, self._headers, value, completed=False))

    def _makeDictOfStringsToClassesAttribute(self, klass, value):
        return GithubObject.__makeTransformedDictAttribute(value, (str, unicode), dict, lambda value: klass(self._requester, self._headers, value, completed=False))

    @property
    def etag(self):
        '''
        :type str
        '''
        return self._headers.get(Consts.RES_ETAG)

    @property
    def last_modified(self):
        '''
        :type str
        '''
        return self._headers.get(Consts.RES_LAST_MODIFED)


class NonCompletableGithubObject(GithubObject):
    def _completeIfNeeded(self):
        pass


class CompletableGithubObject(GithubObject):
    def __init__(self, requester, headers, attributes, completed):
        GithubObject.__init__(self, requester, headers, attributes, completed)
        self.__completed = completed

    def _completeIfNotSet(self, value):
        if value is NotSet:
            self._completeIfNeeded()

    def _completeIfNeeded(self):
        if not self.__completed:
            self.__complete()

    def __complete(self):
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self._url.value
        )
        self._storeAndUseAttributes(headers, data)
        self.__completed = True

    def update(self):
        '''
        Check and update the object with conditional request
        :rtype: Boolean value indicating whether the object is changed
        '''
        conditionalRequestHeader = dict()
        if self.etag is not None:
            conditionalRequestHeader[Consts.REQ_IF_NONE_MATCH] = self.etag
        if self.last_modified is not None:
            conditionalRequestHeader[Consts.REQ_IF_MODIFIED_SINCE] = self.last_modified

        status, responseHeaders, output = self._requester.requestJson(
            "GET",
            self._url.value,
            headers=conditionalRequestHeader
        )
        if status == 304:
            return False
        else:
            headers, data = self._requester._Requester__check(status, responseHeaders, output)
            self._storeAndUseAttributes(headers, data)
            self.__completed = True
            return True
