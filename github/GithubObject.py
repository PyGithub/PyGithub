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

from __future__ import with_statement

import datetime
import pickle

import GithubException
import Consts


class _NotSetType:
    def __repr__(self):
        return "NotSet"
NotSet = _NotSetType()


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
        if self.CHECK_AFTER_INIT_FLAG:
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

    @staticmethod
    def _parentUrl(url):
        return "/".join(url.split("/")[: -1])

    @staticmethod
    def _NoneIfNotSet(value):
        if value is NotSet:
            return None
        else:
            return value

    @staticmethod
    def _parseDatetime(s):
        if s is None:
            return None
        elif len(s) == 24:
            return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.000Z")
        elif len(s) == 25:
            return datetime.datetime.strptime(s[:19], "%Y-%m-%dT%H:%M:%S") + (1 if s[19] == '-' else -1) * datetime.timedelta(hours=int(s[20:22]), minutes=int(s[23:25]))
        else:
            return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")

    def save(self, file_name):  # #193: Could we use file-like objects? It would be more "pythonic" than passing filenames.
        '''
        Save instance to a file
        :param file_name: the full path of target file
        '''
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)  # #193: This will also save self._requester, and the login/password of the user. She might not appriciate.
            # #193: May be better to pickle only self._rawData and self._headers and restore the object with Github.create_from_raw_data

    @classmethod  # #193: Could be a @staticmethod? The docstring would be simpler (no need to explain the type will be same as saved).
    def load(cls, file_name):  # #193: Could we use file-like objects? It would be more "pythonic" than passing filenames.
        '''
        Load saved instance from file
        :param file_name: the full path to saved file
        :rtype: saved instance. The type of loaded instance remains its orginal one and will not be affected by from which derived class the method is called.
        '''
        with open(file_name, 'rb') as f:
            return pickle.load(f)

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

    # #193: Should be only in CompletableGithubObject, NonCompletableGithubObjects don't have urls
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
            self._url,
            conditionalRequestHeader,
            None
        )
        if status == 304:
            return False
        else:
            headers, data = self._requester._Requester__check(status, responseHeaders, output)
            self._storeAndUseAttributes(headers, data)
            self.__completed = True
            return True


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
            self._url,
            None,
            None
        )
        self._storeAndUseAttributes(headers, data)
        self.__completed = True
