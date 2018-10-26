# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Bill Mill <bill.mill@gmail.com>                               #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 davidbrai <davidbrai@gmail.com>                               #
# Copyright 2014 Thialfihar <thi@thialfihar.org>                               #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Dan Vanderkam <danvdk@gmail.com>                              #
# Copyright 2015 Eliot Walker <eliot@lyft.com>                                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2018 Gilad Shefer <gshefer@redhat.com>                             #
# Copyright 2018 Joel Koglin <JoelKoglin@gmail.com>                            #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
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

try:
    from urllib.parse import parse_qs
except ImportError:
    from urlparse import parse_qs

import github.GithubObject


class PaginatedListBase:
    def __init__(self):
        self.__elements = list()

    def __getitem__(self, index):
        assert isinstance(index, (int, slice))
        if isinstance(index, (int, long)):
            self.__fetchToIndex(index)
            return self.__elements[index]
        else:
            return self._Slice(self, index)

    def __iter__(self):
        for element in self.__elements:
            yield element
        while self._couldGrow():
            newElements = self._grow()
            for element in newElements:
                yield element

    def _isBiggerThan(self, index):
        return len(self.__elements) > index or self._couldGrow()

    def __fetchToIndex(self, index):
        while len(self.__elements) <= index and self._couldGrow():
            self._grow()

    def _grow(self):
        newElements = self._fetchNextPage()
        self.__elements += newElements
        return newElements

    class _Slice:
        def __init__(self, theList, theSlice):
            self.__list = theList
            self.__start = theSlice.start or 0
            self.__stop = theSlice.stop
            self.__step = theSlice.step or 1

        def __iter__(self):
            index = self.__start
            while not self.__finished(index):
                if self.__list._isBiggerThan(index):
                    yield self.__list[index]
                    index += self.__step
                else:
                    return

        def __finished(self, index):
            return self.__stop is not None and index >= self.__stop


class PaginatedList(PaginatedListBase):
    """
    This class abstracts the `pagination of the API <http://developer.github.com/v3/#pagination>`_.

    You can simply enumerate through instances of this class::

        for repo in user.get_repos():
            print(repo.name)

    If you want to know the total number of items in the list::

        print(user.get_repos().totalCount)
        print(len(user.get_repos()))

    You can also index them or take slices::

        second_repo = user.get_repos()[1]
        first_repos = user.get_repos()[:10]

    If you want to iterate in reversed order, just do::

        for repo in user.get_repos().reversed:
            print(repo.name)

    And if you really need it, you can explicitly access a specific page::

        some_repos = user.get_repos().get_page(0)
        some_other_repos = user.get_repos().get_page(3)
    """

    def __init__(self, contentClass, requester, firstUrl, firstParams, headers=None, list_item="items"):
        PaginatedListBase.__init__(self)
        self.__requester = requester
        self.__contentClass = contentClass
        self.__firstUrl = firstUrl
        self.__firstParams = firstParams or ()
        self.__nextUrl = firstUrl
        self.__nextParams = firstParams or {}
        self.__headers = headers
        self.__list_item = list_item
        if self.__requester.per_page != 30:
            self.__nextParams["per_page"] = self.__requester.per_page
        self._reversed = False
        self.__totalCount = None

    @property
    def totalCount(self):
        if not self.__totalCount:
            params = {} if self.__nextParams is None else self.__nextParams.copy()
            # set per_page = 1 so the totalCount is just the number of pages
            params.update({"per_page": 1})
            headers, data = self.__requester.requestJsonAndCheck(
                "GET",
                self.__firstUrl,
                parameters=params,
                headers=self.__headers
            )
            if 'link' not in headers:
                self.__totalCount = len(data) if data else 0
            else:
                links = self.__parseLinkHeader(headers)
                lastUrl = links.get("last")
                self.__totalCount = int(parse_qs(lastUrl)['page'][0])
        return self.__totalCount

    def _getLastPageUrl(self):
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            self.__firstUrl,
            parameters=self.__nextParams,
            headers=self.__headers
        )
        links = self.__parseLinkHeader(headers)
        lastUrl = links.get("last")
        return lastUrl

    @property
    def reversed(self):
        r = PaginatedList(self.__contentClass, self.__requester, self.__firstUrl, self.__firstParams, self.__headers, self.__list_item)
        r.__reverse()
        return r

    def __reverse(self):
        self._reversed = True
        lastUrl = self._getLastPageUrl()
        if lastUrl:
            self.__nextUrl = lastUrl

    def _couldGrow(self):
        return self.__nextUrl is not None

    def _fetchNextPage(self):
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            self.__nextUrl,
            parameters=self.__nextParams,
            headers=self.__headers
        )
        data = data if data else []

        self.__nextUrl = None
        if len(data) > 0:
            links = self.__parseLinkHeader(headers)
            if self._reversed:
                if "prev" in links:
                    self.__nextUrl = links["prev"]
            elif "next" in links:
                self.__nextUrl = links["next"]
        self.__nextParams = None

        if self.__list_item in data:
            self.__totalCount = data.get('total_count')
            data = data[self.__list_item]

        content = [
            self.__contentClass(self.__requester, headers, element, completed=False)
            for element in data if element is not None
        ]
        if self._reversed:
            return content[::-1]
        return content

    def __parseLinkHeader(self, headers):
        links = {}
        if "link" in headers:
            linkHeaders = headers["link"].split(", ")
            for linkHeader in linkHeaders:
                (url, rel) = linkHeader.split("; ")
                url = url[1:-1]
                rel = rel[5:-1]
                links[rel] = url
        return links

    def get_page(self, page):
        params = dict(self.__firstParams)
        if page != 0:
            params["page"] = page + 1
        if self.__requester.per_page != 30:
            params["per_page"] = self.__requester.per_page
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            self.__firstUrl,
            parameters=params,
            headers=self.__headers
        )

        if self.__list_item in data:
            self.__totalCount = data.get('total_count')
            data = data[self.__list_item]

        return [
            self.__contentClass(self.__requester, headers, element, completed=False)
            for element in data
        ]
