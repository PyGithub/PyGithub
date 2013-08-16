# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
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

import pickle


class _NotSetType:
    def __repr__(self):
        return "NotSet"
NotSet = _NotSetType()


class GithubObject(object):
    """
    Base class for all classes representing objects returned by the API.
    """
    def __init__(self, requester, attributes, completed):
        self._requester = requester
        self._initConditionalRequestAttributes()
        self._initAttributes()
        self._storeAndUseAttributes(attributes)

    def _initConditionalRequestAttributes(self):
        self._etag = NotSet
        self._last_modified = NotSet

    def _useConditionalRequestAttributes(self, attributes):
        if "etag" in attributes:
            self._etag = attributes["etag"]
        if "last-modified" in attributes:
            self._last_modified = attributes["last-modified"]
  
    def _storeAndUseAttributes(self, attributes):
        self._useConditionalRequestAttributes(attributes)
        self._useAttributes(attributes)
        self._rawData = attributes

    @property
    def etag(self):
        """
        :type: str
        """
        return self._etag

    @property
    def last_modified(self):
        """
        :type: str
        """
        return self._last_modified

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
    
    def save(self, file_name):
        '''
        Save instance to a file
        
        :param file_name: the full path of target file
        '''

        with open(file_name, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, file_name):
        '''
        Load saved instance from file
        :param file_name: the full path to saved file
        :rtype: saved instance. The type of loaded instance remains its orginal one and  will not be affected by from which derived class the method is called.   
        '''
        with open(file_name, 'rb') as f:
            return pickle.load(f)
        

class NonCompletableGithubObject(GithubObject):
    def _completeIfNeeded(self):
        pass


class CompletableGithubObject(GithubObject):
    def __init__(self, requester, attributes, completed):
        GithubObject.__init__(self, requester, attributes, completed)
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
        self._storeAndUseAttributes(data)
        self.__completed = True
    
    def update(self):
        '''
        Check and update the object with conditional request
        :rtype: Boolean value indicating whether the object is changed
        '''
        conditionalRequestHeader = dict()
        if self._etag is not NotSet:
            conditionalRequestHeader["If-None-Match"] = self._etag
        if self._last_modified is not NotSet:
            conditionalRequestHeader["If-Modified-Since"] = self._last_modified


        try:
            headers, data = self._requester.requestJsonAndCheck(
                "GET",
                self._url,
                conditionalRequestHeader,
                None
            )
            self._storeAndUseAttributes(data)
            self.__completed = True
            return True
        except GithubException.NotModifiedException:
            return False
