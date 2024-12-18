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
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 netsgnut <284779+netsgnut@users.noreply.github.com>           #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Emir Hodzic <emir.hodzich@gmail.com>                          #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Andrew Dawes <53574062+AndrewJDawes@users.noreply.github.com> #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2023 YugoHino <henom06@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
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

from typing import Any, Callable, Dict, Generic, Iterator, List, Optional, Type, TypeVar, Union
from urllib.parse import parse_qs

from github.GithubObject import GithubObject
from github.Requester import Requester

T = TypeVar("T", bound=GithubObject)


class PaginatedListBase(Generic[T]):
    __elements: List[T]

    def _couldGrow(self) -> bool:
        raise NotImplementedError

    def _fetchNextPage(self) -> List[T]:
        raise NotImplementedError

    def __init__(self, elements: Optional[List[T]] = None) -> None:
        self.__elements = [] if elements is None else elements

    def __getitem__(self, index: Union[int, slice]) -> Any:
        assert isinstance(index, (int, slice))
        if isinstance(index, int):
            self.__fetchToIndex(index)
            return self.__elements[index]
        else:
            return self._Slice(self, index)

    def __iter__(self) -> Iterator[T]:
        yield from self.__elements
        while self._couldGrow():
            newElements = self._grow()
            yield from newElements

    def _isBiggerThan(self, index: int) -> bool:
        return len(self.__elements) > index or self._couldGrow()

    def __fetchToIndex(self, index: int) -> None:
        while len(self.__elements) <= index and self._couldGrow():
            self._grow()

    def _grow(self) -> List[T]:
        newElements = self._fetchNextPage()
        self.__elements += newElements
        return newElements

    class _Slice:
        def __init__(self, theList: "PaginatedListBase[T]", theSlice: slice):
            self.__list = theList
            self.__start = theSlice.start or 0
            self.__stop = theSlice.stop
            self.__step = theSlice.step or 1

        def __iter__(self) -> Iterator[T]:
            index = self.__start
            while not self.__finished(index):
                if self.__list._isBiggerThan(index):
                    yield self.__list[index]
                    index += self.__step
                else:
                    return

        def __finished(self, index: int) -> bool:
            return self.__stop is not None and index >= self.__stop


class PaginatedList(PaginatedListBase[T]):
    """
    This class abstracts the `pagination of the REST API <https://docs.github.com/en/rest/guides/traversing-with-pagination>`_
    and the GraphQl API <https://docs.github.com/en/graphql/guides/using-pagination-in-the-graphql-api>`_.

    You can simply enumerate through instances of this class::

        for repo in user.get_repos():
            print(repo.name)

    If you want to know the total number of items in the list::

        print(user.get_repos().totalCount)

    You can also index them or take slices::

        second_repo = user.get_repos()[1]
        first_repos = user.get_repos()[:10]

    If you want to iterate in reversed order, just do::

        for repo in user.get_repos().reversed:
            print(repo.name)

    And if you really need it, you can explicitly access a specific page::

        repos = user.get_repos()
        assert repos.is_rest, "get_page not supported by the GraphQL API"

        some_repos = repos.get_page(0)
        some_other_repos = repos.get_page(3)
    """

    # v3: move * before firstUrl and fix call sites
    def __init__(
        self,
        contentClass: Type[T],
        requester: Requester,
        firstUrl: Optional[str] = None,
        firstParams: Optional[Dict[str, Any]] = None,
        *,
        headers: Optional[Dict[str, str]] = None,
        list_item: Union[str, List[str]] = "items",
        total_count_item: str = "total_count",
        firstData: Optional[Any] = None,
        firstHeaders: Optional[Dict[str, Union[str, int]]] = None,
        attributesTransformer: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]] = None,
        graphql_query: Optional[str] = None,
        graphql_variables: Optional[Dict[str, Any]] = None,
    ):
        if firstUrl is None and firstData is None and graphql_query is None:
            raise ValueError("Either firstUrl or graphql_query must be given")
        if firstUrl is not None and graphql_query is not None:
            raise ValueError("Only one of firstUrl or graphql_query can be given")
        if graphql_query is not None:
            if not (isinstance(list_item, list) and all(isinstance(item, str) for item in list_item)):
                raise ValueError("With graphql_query given, item_list must be a list of strings")

        self.__requester = requester
        self.__contentClass = contentClass

        self.__is_rest = firstUrl is not None or firstData is not None
        self.__firstUrl = firstUrl
        self.__firstParams: Dict[str, Any] = firstParams or {}
        self.__nextUrl = firstUrl
        self.__nextParams: Dict[str, Any] = firstParams or {}
        self.__headers = headers
        self.__list_item = list_item
        self.__total_count_item = total_count_item
        if self.__requester.per_page != 30:
            self.__nextParams["per_page"] = self.__requester.per_page
        self._reversed = False
        self.__totalCount: Optional[int] = None
        self._attributesTransformer = attributesTransformer

        self.__graphql_query = graphql_query
        self.__graphql_variables = graphql_variables or {}
        self.__page_info = None

        first_page = []
        if firstData is not None:
            first_page = self._getPage(firstData, firstHeaders)
            # this paginated list contains a single page
            if self.__nextUrl is None and self.__totalCount is None:
                self.__totalCount = len(first_page)
        super().__init__(first_page)

    @property
    def is_rest(self) -> bool:
        return self.__is_rest

    @property
    def is_graphql(self) -> bool:
        return not self.is_rest

    def _transformAttributes(self, element: Dict[str, Any]) -> Dict[str, Any]:
        if self._attributesTransformer is None:
            return element
        return self._attributesTransformer(element)

    @property
    def totalCount(self) -> int:
        if self.__totalCount is None:
            if self.is_rest:
                params = self.__nextParams.copy()
                # set per_page = 1 so the totalCount is just the number of pages
                params.update({"per_page": 1})
                headers, data = self.__requester.requestJsonAndCheck(
                    "GET", self.__firstUrl, parameters=params, headers=self.__headers  # type: ignore
                )
                if "link" not in headers:
                    if data and "total_count" in data:
                        self.__totalCount = data["total_count"]
                    elif data:
                        if isinstance(data, dict):
                            data = data[self.__list_item]
                        self.__totalCount = len(data)
                    else:
                        self.__totalCount = 0
                else:
                    links = self.__parseLinkHeader(headers)
                    lastUrl = links.get("last")
                    if lastUrl:
                        self.__totalCount = int(parse_qs(lastUrl)["page"][0])
                    else:
                        self.__totalCount = 0
            else:
                variables = self.__graphql_variables.copy()
                if not self._reversed:
                    variables["first"] = 1
                    variables["after"] = None
                else:
                    variables["last"] = 1
                    variables["before"] = None

                _, data = self.__requester.graphql_query(self.__graphql_query, variables)  # type: ignore
                pagination = self._get_graphql_pagination(data["data"], self.__list_item)  # type: ignore
                self.__totalCount = pagination.get("totalCount")
        return self.__totalCount  # type: ignore

    def _getLastPageUrl(self) -> Optional[str]:
        headers, data = self.__requester.requestJsonAndCheck(
            "GET", self.__firstUrl, parameters=self.__nextParams, headers=self.__headers  # type: ignore
        )
        links = self.__parseLinkHeader(headers)
        return links.get("last")

    @property
    def reversed(self) -> "PaginatedList[T]":
        r = PaginatedList(
            self.__contentClass,
            self.__requester,
            self.__firstUrl,
            self.__firstParams,
            headers=self.__headers,
            list_item=self.__list_item,
            attributesTransformer=self._attributesTransformer,
            graphql_query=self.__graphql_query,
            graphql_variables=self.__graphql_variables,
        )
        r.__reverse()
        return r

    def __reverse(self) -> None:
        self._reversed = True
        if self.is_rest:
            lastUrl = self._getLastPageUrl()
            if lastUrl:
                self.__nextUrl = lastUrl
                if self.__nextParams:
                    # #2929: remove all parameters from self.__nextParams contained in self.__nextUrl
                    self.__nextParams = {
                        k: v
                        for k, v in self.__nextParams.items()
                        if k not in Requester.get_parameters_of_url(self.__nextUrl).keys()
                    }

    def _couldGrow(self) -> bool:
        return (
            self.is_rest
            and self.__nextUrl is not None
            or self.is_graphql
            and (
                self.__page_info is None
                or not self._reversed
                and self.__page_info["hasNextPage"]
                or self._reversed
                and self.__page_info["hasPreviousPage"]
            )
        )

    def _get_graphql_pagination(self, data: Dict[str, Any], path: List[str]) -> Dict[str, Any]:
        for item in path:
            if item not in data:
                raise RuntimeError(f"Pagination path {path} not found in data: {self.paths_of_dict(data)}")
            data = data[item]
        return data

    def _fetchNextPage(self) -> List[T]:
        if self.is_rest:
            # REST API pagination
            headers, data = self.__requester.requestJsonAndCheck(
                "GET", self.__nextUrl, parameters=self.__nextParams, headers=self.__headers  # type: ignore
            )
            data = data if data else []
            return self._getPage(data, headers)
        else:
            # GraphQL API pagination
            variables = self.__graphql_variables.copy()
            if not self._reversed:
                variables["first"] = self.__requester.per_page
                if self.__page_info is not None:
                    variables["after"] = self.__page_info["endCursor"]
            else:
                variables["last"] = self.__requester.per_page
                if self.__page_info is not None:
                    variables["before"] = self.__page_info["startCursor"]

            _, data = self.__requester.graphql_query(self.__graphql_query, variables)  # type: ignore

            pagination = self._get_graphql_pagination(data["data"], self.__list_item)  # type: ignore
            return self._getPage(pagination, {})

    def _getPage(self, data: Any, headers: Optional[Dict[str, Union[str, int]]]) -> List[T]:
        if self.is_rest:
            self.__nextUrl = None  # type: ignore
            if len(data) > 0:
                links = self.__parseLinkHeader(headers)  # type: ignore
                if self._reversed:
                    if "prev" in links:
                        self.__nextUrl = links["prev"]
                elif "next" in links:
                    self.__nextUrl = links["next"]
            self.__nextParams = {}
            if self.__list_item in data:
                self.__totalCount = data.get(self.__total_count_item)
                data = data[self.__list_item]
            content = [
                self.__contentClass(self.__requester, headers, self._transformAttributes(element))  # type: ignore
                for element in data
                if element is not None
            ]
            if self._reversed:
                return content[::-1]
            return content
        else:
            if "pageInfo" not in data:
                raise RuntimeError(f"Query must provide pagination with pageInfo:\n{self.__graphql_query}")

            self.__page_info = data["pageInfo"]
            if any(
                item not in self.__page_info  # type: ignore
                for item in ["startCursor", "endCursor", "hasNextPage", "hasPreviousPage"]
            ):
                raise RuntimeError(f"Query must provide pagination with pageInfo\n{self.__graphql_query}")

            if self.__totalCount is None:
                if "totalCount" not in data:
                    raise RuntimeError(f"Query must provide totalCount\n{self.__graphql_query}")
                self.__totalCount = data["totalCount"]

            if "nodes" not in data:
                raise RuntimeError(
                    f"No nodes found under pagination path {self.__list_item}: {self.paths_of_dict(data)}"
                )

            nodes = data["nodes"]
            if self._reversed:
                nodes = nodes[::-1]
            return [self.__contentClass(self.__requester, {}, element) for element in nodes if element is not None]

    def __parseLinkHeader(self, headers: Dict[str, Union[str, int]]) -> Dict[str, str]:
        links = {}
        if "link" in headers and isinstance(headers["link"], str):
            linkHeaders = headers["link"].split(", ")
            for linkHeader in linkHeaders:
                url, rel, *rest = linkHeader.split("; ")
                url = url[1:-1]
                rel = rel[5:-1]
                links[rel] = url
        return links

    def get_page(self, page: int) -> List[T]:
        if self.is_graphql:
            raise RuntimeError("Not supported for GraphQL pagination")

        params = dict(self.__firstParams)
        if page != 0:
            params["page"] = page + 1
        if self.__requester.per_page != 30:
            params["per_page"] = self.__requester.per_page
        headers, data = self.__requester.requestJsonAndCheck(
            "GET", self.__firstUrl, parameters=params, headers=self.__headers  # type: ignore
        )

        if self.__list_item in data:
            self.__totalCount = data.get("total_count")
            data = data[self.__list_item]
        return [self.__contentClass(self.__requester, headers, self._transformAttributes(element)) for element in data]

    @classmethod
    def override_attributes(cls, overrides: Dict[str, Any]) -> Callable[[Dict[str, Any]], Dict[str, Any]]:
        def attributes_transformer(element: Dict[str, Any]) -> Dict[str, Any]:
            # Recursively merge overrides with attributes, overriding attributes with overrides
            element = cls.merge_dicts(element, overrides)
            return element

        return attributes_transformer

    @classmethod
    def merge_dicts(cls, d1: Dict[str, Any], d2: Dict[str, Any]) -> Dict[str, Any]:
        # clone d1
        d1 = d1.copy()
        for k, v in d2.items():
            if isinstance(v, dict):
                d1[k] = cls.merge_dicts(d1.get(k, {}), v)
            else:
                d1[k] = v
        return d1

    @classmethod
    def paths_of_dict(cls, d: dict) -> dict:
        return {key: cls.paths_of_dict(val) if isinstance(val, dict) else None for key, val in d.items()}
