# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import GithubObject


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
            newElements = self.__grow()
            for element in newElements:
                yield element

    def _isBiggerThan(self, index):
        return len(self.__elements) > index or self._couldGrow()

    def __fetchToIndex(self, index):
        while len(self.__elements) <= index and self._couldGrow():
            self.__grow()

    def __grow(self):
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
    def __init__(self, contentClass, requester, firstUrl, firstParams):
        PaginatedListBase.__init__(self)
        self.__requester = requester
        self.__contentClass = contentClass
        self.__firstUrl = firstUrl
        self.__firstParams = firstParams
        self.__nextUrl = firstUrl
        self.__nextParams = firstParams

    def _couldGrow(self):
        return self.__nextUrl is not None

    def _fetchNextPage(self):
        headers, data = self.__requester.requestAndCheck("GET", self.__nextUrl, self.__nextParams, None)

        links = self.__parseLinkHeader(headers)
        if len(data) > 0 and "next" in links:
            self.__nextUrl = links["next"]
        else:
            self.__nextUrl = None
        self.__nextParams = None

        return [
            self.__contentClass(self.__requester, element, completed=False)
            for element in data
        ]

    def __parseLinkHeader(self, headers):
        links = {}
        if "link" in headers:
            linkHeaders = headers["link"].split(",")
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
        headers, data = self.__requester.requestAndCheck("GET", self.__firstUrl, params, None)

        return [
            self.__contentClass(self.__requester, element, completed=False)
            for element in data
        ]
