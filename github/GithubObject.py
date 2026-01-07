############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Andrew Scheller <github@loowis.durge.org>                     #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jakub Wilk <jwilk@jwilk.net>                                  #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2016 Sam Corbett <sam.corbett@cloudsoftcorp.com>                   #
# Copyright 2018 Shubham Singh <41840111+singh811@users.noreply.github.com>    #
# Copyright 2018 h.shi <10385628+AnYeMoWang@users.noreply.github.com>          #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Adam Baratz <adam.baratz@gmail.com>                           #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Christoph Reiter <reiter.christoph@gmail.com>                 #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Jonathan Greg <31892308+jmgreg31@users.noreply.github.com>    #
# Copyright 2023 Jonathan Leitschuh <jonathan.leitschuh@gmail.com>             #
# Copyright 2023 Joseph Henrich <crimsonknave@gmail.com>                       #
# Copyright 2023 Nicolas Schweitzer <nicolas.schweitzer@datadoghq.com>         #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Min RK <benjaminrk@gmail.com>                                 #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
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

from __future__ import annotations

import email.utils
import re
import typing
from abc import ABC
from datetime import datetime, timezone
from decimal import Decimal
from operator import itemgetter
from typing import TYPE_CHECKING, Any, Callable, Union, overload

from typing_extensions import ParamSpec, Protocol, Self, TypeGuard, TypeVar

from . import Consts
from .GithubException import BadAttributeException, IncompletableObject

if TYPE_CHECKING:
    from .Requester import Requester

T = typing.TypeVar("T")
K = typing.TypeVar("K")
T_co = typing.TypeVar("T_co", covariant=True)
T_gh = typing.TypeVar("T_gh", bound="GithubObject")


class Attribute(Protocol[T_co]):
    @property
    def value(self) -> T_co:
        raise NotImplementedError


def _datetime_from_http_date(value: str) -> datetime:
    """
    Convert an HTTP date to a datetime object.

    Raises ValueError for invalid dates.

    """

    dt = email.utils.parsedate_to_datetime(value)
    if dt.tzinfo is None:
        # RFC7231 states that UTC is assumed if no timezone info is present
        return dt.replace(tzinfo=timezone.utc)
    return dt


def _datetime_from_github_isoformat(value: str) -> datetime:
    """
    Convert an GitHub API timestamps to a datetime object.

    Raises ValueError for invalid timestamps.

    """

    # Github always returns YYYY-MM-DDTHH:MM:SSZ, so we can use the stdlib parser
    # with some minor adjustments for Python < 3.11 which doesn't support "Z"
    # https://docs.github.com/en/rest/overview/resources-in-the-rest-api#schema
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    return datetime.fromisoformat(value)


class _NotSetType(Attribute[Any]):
    def __repr__(self) -> str:
        return "NotSet"

    @property
    def value(self) -> Any:
        return None

    @staticmethod
    def remove_unset_items(data: dict[str, Any]) -> dict[str, Any]:
        return {key: value for key, value in data.items() if not isinstance(value, _NotSetType)}


NotSet = _NotSetType()

Opt = Union[T, _NotSetType]


def is_defined(v: T | _NotSetType) -> TypeGuard[T]:
    return not isinstance(v, _NotSetType)


def is_undefined(v: T | _NotSetType) -> TypeGuard[_NotSetType]:
    return isinstance(v, _NotSetType)


def is_optional(v: Any, type: type | tuple[type, ...]) -> bool:
    return isinstance(v, _NotSetType) or isinstance(v, type)


def is_optional_list(v: Any, type: type | tuple[type, ...]) -> bool:
    return isinstance(v, _NotSetType) or isinstance(v, list) and all(isinstance(element, type) for element in v)


camel_to_snake_case_regexp = re.compile(r"(?<!^)(?=[A-Z])")


@overload
def as_rest_api_attributes(graphql_attributes: dict[str, Any]) -> dict[str, Any]:
    ...


@overload
def as_rest_api_attributes(graphql_attributes: None) -> None:
    ...


def as_rest_api_attributes(graphql_attributes: dict[str, Any] | None) -> dict[str, Any] | None:
    """
    Converts attributes from GraphQL schema to REST API schema.

    The GraphQL API uses lower camel case (e.g. createdAt), whereas REST API uses snake case (created_at). Initializing
    REST API GithubObjects from GraphQL API attributes requires transformation provided by this method.

    Further renames GraphQL attributes to REST API attributes where the case conversion is not sufficient. For example,
    GraphQL attribute 'id' is equivalent to REST API attribute 'node_id'.

    """
    if graphql_attributes is None:
        return None

    attribute_translation = {
        "id": "node_id",
        "databaseId": "id",  # must be after 'id': 'node_id'!
        "url": "html_url",
    }

    def translate(attr: str) -> str:
        def un_capitalize(match: re.Match) -> str:
            return match.group(1) + match.group(2).lower()

        attr = attribute_translation.get(attr, attr)
        attr = re.sub(r"([A-Z])([A-Z]+)", un_capitalize, attr)
        attr = camel_to_snake_case_regexp.sub("_", attr)
        attr = attr.lower()

        return attr

    return {
        translate(k): as_rest_api_attributes(v)
        if isinstance(v, dict)
        else (as_rest_api_attributes_list(v) if isinstance(v, list) else v)
        for k, v in graphql_attributes.items()
    }


def as_rest_api_attributes_list(graphql_attributes: list[dict[str, Any] | None]) -> list[dict[str, Any] | None]:
    return [as_rest_api_attributes(v) if isinstance(v, dict) else v for v in graphql_attributes]


class _ValuedAttribute(Attribute[T]):
    def __init__(self, value: T):
        self._value = value

    @property
    def value(self) -> T:
        return self._value


class _BadAttribute(Attribute[T]):
    def __init__(self, value: Any, expectedType: Any, exception: Exception | None = None):
        self.__value = value
        self.__expectedType = expectedType
        self.__exception = exception

    @property
    def value(self) -> T:
        raise BadAttributeException(self.__value, self.__expectedType, self.__exception)


# v3: add * to edit function of all GithubObject implementations,
#     this allows to rename attributes and maintain the order of attributes
class GithubObject(ABC):
    """
    Base class for all classes representing objects returned by the API.
    """

    """
    A global debug flag to enable header validation by requester for all objects
    """
    CHECK_AFTER_INIT_FLAG = False
    _url: Attribute[str]

    @classmethod
    def is_rest(cls) -> bool:
        return not cls.is_graphql()

    @classmethod
    def is_graphql(cls) -> bool:
        return False

    @classmethod
    def setCheckAfterInitFlag(cls, flag: bool) -> None:
        cls.CHECK_AFTER_INIT_FLAG = flag

    def __init__(
        self,
        requester: Requester,
        headers: dict[str, str | int],
        attributes: Any,
    ):
        self._requester = requester
        self._initAttributes()
        self._storeAndUseAttributes(headers, attributes)

        # Ask requester to do some checking, for debug and test purpose
        # Since it's most handy to access and kinda all-knowing
        if self.CHECK_AFTER_INIT_FLAG:  # pragma no branch (Flag always set in tests)
            requester.check_me(self)

    def _storeAndUseAttributes(self, headers: dict[str, str | int], attributes: Any) -> None:
        # Make sure headers are assigned before calling _useAttributes
        # (Some derived classes will use headers in _useAttributes)
        self._headers = headers
        self._rawData = attributes
        self._useAttributes(attributes)

    @property
    def requester(self) -> Requester:
        """
        Return my Requester object.

        For example, to make requests to API endpoints not yet supported by PyGitHub.

        """
        return self._requester

    @property
    def raw_data(self) -> dict[str, Any]:
        """
        :type: dict
        """
        return self._rawData

    @property
    def raw_headers(self) -> dict[str, str | int]:
        """
        :type: dict
        """
        return self._headers

    @staticmethod
    def _parentUrl(url: str) -> str:
        return "/".join(url.split("/")[:-1])

    @staticmethod
    def __makeSimpleAttribute(value: Any, type: type[T]) -> Attribute[T]:
        if value is None or isinstance(value, type):
            return _ValuedAttribute(value)  # type: ignore
        else:
            return _BadAttribute(value, type)  # type: ignore

    @staticmethod
    def __makeSimpleListAttribute(value: list, type: type[T]) -> Attribute[T]:
        if isinstance(value, list) and all(isinstance(element, type) for element in value):
            return _ValuedAttribute(value)  # type: ignore
        else:
            return _BadAttribute(value, [type])  # type: ignore

    @staticmethod
    def __makeTransformedAttribute(value: T, type: type[T], transform: Callable[[T], K]) -> Attribute[K]:
        if value is None:
            return _ValuedAttribute(None)  # type: ignore
        elif isinstance(value, type):
            try:
                return _ValuedAttribute(transform(value))
            except Exception as e:
                return _BadAttribute(value, type, e)  # type: ignore
        else:
            return _BadAttribute(value, type)  # type: ignore

    @staticmethod
    def _makeStringAttribute(value: int | str | None) -> Attribute[str]:
        return GithubObject.__makeSimpleAttribute(value, str)

    @staticmethod
    def _makeIntAttribute(value: int | str | None) -> Attribute[int]:
        return GithubObject.__makeSimpleAttribute(value, int)

    @staticmethod
    def _makeDecimalAttribute(value: Decimal | None) -> Attribute[Decimal]:
        return GithubObject.__makeSimpleAttribute(value, Decimal)

    @staticmethod
    def _makeFloatAttribute(value: float | None) -> Attribute[float]:
        return GithubObject.__makeSimpleAttribute(value, float)

    @staticmethod
    def _makeBoolAttribute(value: bool | None) -> Attribute[bool]:
        return GithubObject.__makeSimpleAttribute(value, bool)

    @staticmethod
    def _makeDictAttribute(value: dict[str, Any]) -> Attribute[dict[str, Any]]:
        return GithubObject.__makeSimpleAttribute(value, dict)

    @staticmethod
    def _makeTimestampAttribute(value: int) -> Attribute[datetime]:
        return GithubObject.__makeTransformedAttribute(
            value,
            int,
            lambda t: datetime.fromtimestamp(t, tz=timezone.utc),
        )

    @staticmethod
    def _makeDatetimeAttribute(value: str | None) -> Attribute[datetime]:
        return GithubObject.__makeTransformedAttribute(value, str, _datetime_from_github_isoformat)  # type: ignore

    @staticmethod
    def _makeHttpDatetimeAttribute(value: str | None) -> Attribute[datetime]:
        return GithubObject.__makeTransformedAttribute(value, str, _datetime_from_http_date)  # type: ignore

    def _makeClassAttribute(self, klass: type[T_gh], value: Any) -> Attribute[T_gh]:
        return GithubObject.__makeTransformedAttribute(
            value,
            dict,
            lambda value: klass(self._requester, self._headers, value),
        )

    def _makeUnionClassAttributeFromTypeName(
        self, type_name: str | None, fallback_type: str | None, value: Any, *class_and_names: tuple[type[T_gh], str]
    ) -> Attribute[T_gh]:
        if value is None or type_name is None:
            return _ValuedAttribute(None)  # type: ignore
        fallback_class = None
        for klass, name in class_and_names:
            if type_name == name:
                return self._makeClassAttribute(klass, value)
            if fallback_type == name:
                fallback_class = klass
        if fallback_type is not None:
            if fallback_class is None:
                # this is misconfiguration in PyGithub code, not a user's fault
                raise ValueError(
                    f"Fallback type {fallback_type} is not among classes and names: {[name for klass, name in class_and_names]}"
                )
            return self._makeClassAttribute(fallback_class, value)
        return _BadAttribute(value, type)  # type: ignore

    def _makeUnionClassAttributeFromTypeKey(
        self,
        type_key: str,
        default_type: str | None,
        value: Any,
        *class_and_names: tuple[type[T_gh], str],
    ) -> Attribute[T_gh]:
        if value is None or not isinstance(value, dict):
            return _ValuedAttribute(None)  # type: ignore
        return self._makeUnionClassAttributeFromTypeName(
            value.get(type_key, default_type), default_type, value, *class_and_names
        )

    def _makeUnionClassAttributeFromTypeKeyAndValueKey(
        self,
        type_key: str,
        value_key: str,
        default_type: str | None,
        value: Any,
        *class_and_names: tuple[type[T_gh], str],
    ) -> Attribute[T_gh]:
        if value is None or not isinstance(value, dict):
            return _ValuedAttribute(None)  # type: ignore
        return self._makeUnionClassAttributeFromTypeName(
            value.get(type_key, default_type), default_type, value.get(value_key), *class_and_names
        )

    @staticmethod
    def _makeListOfStringsAttribute(value: list[list[str]] | list[str] | list[str | int]) -> Attribute:
        return GithubObject.__makeSimpleListAttribute(value, str)

    @staticmethod
    def _makeListOfIntsAttribute(value: list[int]) -> Attribute:
        return GithubObject.__makeSimpleListAttribute(value, int)

    @staticmethod
    def _makeListOfDictsAttribute(value: list[dict[str, str | list[dict[str, str | list[int]]]]]) -> Attribute:
        return GithubObject.__makeSimpleListAttribute(value, dict)

    @staticmethod
    def _makeListOfListOfStringsAttribute(
        value: list[list[str]],
    ) -> Attribute:
        return GithubObject.__makeSimpleListAttribute(value, list)

    def _makeListOfClassesAttribute(self, klass: type[T_gh], value: Any) -> Attribute[list[T_gh]]:
        if isinstance(value, list) and all(isinstance(element, dict) for element in value):
            return _ValuedAttribute([klass(self._requester, self._headers, element) for element in value])
        else:
            return _BadAttribute(value, [dict])

    def _makeDictOfStringsToClassesAttribute(
        self,
        klass: type[T_gh],
        value: dict[
            str,
            int | dict[str, Any],
        ],
    ) -> Attribute[dict[str, T_gh]]:
        if isinstance(value, dict) and all(
            isinstance(key, str) and isinstance(element, dict) for key, element in value.items()
        ):
            return _ValuedAttribute(
                {key: klass(self._requester, self._headers, element) for key, element in value.items()}
            )
        else:
            return _BadAttribute(value, {str: dict})

    @property
    def etag(self) -> str | None:
        """
        :type: str
        """
        return self._headers.get(Consts.RES_ETAG)  # type: ignore

    @property
    def last_modified(self) -> str | None:
        """
        :type: str
        """
        return self._headers.get(Consts.RES_LAST_MODIFIED)  # type: ignore

    @property
    def last_modified_datetime(self) -> datetime | None:
        """
        :type: datetime
        """
        return self._makeHttpDatetimeAttribute(self.last_modified).value  # type: ignore

    def get__repr__(self, params: dict[str, Any]) -> str:
        """
        Converts the object to a nicely printable string.
        """

        def format_params(params: dict[str, Any]) -> typing.Generator[str, None, None]:
            items = list(params.items())
            for k, v in sorted(items, key=itemgetter(0), reverse=True):
                if isinstance(v, bytes):
                    v = v.decode("utf-8")
                if isinstance(v, str):
                    v = f'"{v}"'
                yield f"{k}={v}"

        return "{class_name}({params})".format(
            class_name=self.__class__.__name__,
            params=", ".join(list(format_params(params))),
        )

    def _initAttributes(self) -> None:
        raise NotImplementedError("BUG: Not Implemented _initAttributes")

    def _useAttributes(self, attributes: Any) -> None:
        raise NotImplementedError("BUG: Not Implemented _useAttributes")


class GraphQlObject:
    @classmethod
    def is_graphql(cls) -> bool:
        return True


class NonCompletableGithubObject(GithubObject, ABC):
    def __init__(
        self,
        requester: Requester,
        headers: dict[str, str | int],
        attributes: dict[str, Any],
    ):
        super().__init__(requester, headers, attributes)


class CompletableGithubObject(GithubObject, ABC):
    def __init__(
        self,
        requester: Requester,
        headers: dict[str, str | int] | None = None,
        attributes: dict[str, Any] | None = None,
        completed: bool | None = None,
        *,
        url: str | None = None,
        accept: str | None = None,
    ):
        """
        A CompletableGithubObject can be partially initialised (completed=False). Accessing attributes that are not
        initialized will then trigger a request to complete all attributes.

        A partially initialized CompletableGithubObject (completed=False) can be completed
        via complete(). This requires the url to be given via parameter `url` or `attributes`.

        With a requester where `Requester.is_lazy == True`, this CompletableGithubObjects is
        partially initialized. This requires the url to be given via parameter `url` or `attributes`.
        Any CompletableGithubObject created from this lazy object will be lazy itself if created with
        parameter `url` or `attributes`.

        :param requester: requester
        :param headers: response headers
        :param attributes: attributes to initialize
        :param completed: do not update non-initialized attributes when True
        :param url: url of this instance, overrides attributes['url']
        :param accept: use this accept header when completing this instance

        """
        response_given = headers is not None

        if headers is None:
            headers = {}
        if attributes is None:
            attributes = {}
        if url is not None:
            attributes["url"] = url
        super().__init__(requester, headers, attributes)
        self.__completed = completed if isinstance(completed, bool) else False
        self.__completeHeaders = {"Accept": accept} if accept else None

        # complete this completable object when requester indicates non-laziness and
        # neither of complete and headers are given
        if requester.is_not_lazy and completed is None and not response_given:
            self.complete()

    def __eq__(self, other: Any) -> bool:
        return (
            other.__class__ is self.__class__
            and other.requester.base_url == self.requester.base_url
            and other._url.value.removeprefix(other.requester.base_url)
            == self._url.value.removeprefix(self.requester.base_url)
        )

    def __hash__(self) -> int:
        return hash(self._url.value)

    def __ne__(self, other: Any) -> bool:
        return not self == other

    @property
    def completed(self) -> bool:
        return self.__completed

    @property
    def raw_data(self) -> dict[str, Any]:
        """
        :type: dict
        """
        self._completeIfNeeded()
        return super().raw_data

    @property
    def raw_headers(self) -> dict[str, str | int]:
        """
        :type: dict
        """
        self._completeIfNeeded()
        return super().raw_headers

    def complete(self) -> Self:
        self._completeIfNeeded()
        return self

    def _completeIfNotSet(self, value: Attribute) -> None:
        if isinstance(value, _NotSetType):
            self._completeIfNeeded()

    def _completeIfNeeded(self) -> None:
        if not self.__completed:
            self.__complete()

    def __complete(self) -> None:
        if self._url.value is None:
            raise IncompletableObject(400, message="Cannot complete object as it contains no URL")
        headers, data = self._requester.requestJsonAndCheck("GET", self._url.value, headers=self.__completeHeaders)
        self._storeAndUseAttributes(headers, data)
        self._set_complete()

    def _set_complete(self) -> None:
        self.__completed = True

    def update(self, additional_headers: dict[str, Any] | None = None) -> bool:
        """
        Check and update the object with conditional request :rtype: Boolean value indicating whether the object is
        changed.
        """
        conditionalRequestHeader = dict()
        if self.etag is not None:
            conditionalRequestHeader[Consts.REQ_IF_NONE_MATCH] = self.etag
        if self.last_modified is not None:
            conditionalRequestHeader[Consts.REQ_IF_MODIFIED_SINCE] = self.last_modified
        if additional_headers is not None:
            conditionalRequestHeader.update(additional_headers)

        status, responseHeaders, output = self._requester.requestJson(
            "GET", self._url.value, headers=conditionalRequestHeader
        )
        if status == 304:
            return False
        else:
            headers, data = self._requester._Requester__check(status, responseHeaders, output)  # type: ignore
            self._storeAndUseAttributes(headers, data)
            self.__completed = True
            return True

    def _initAttributes(self) -> None:
        self._url: Attribute[str] = NotSet

    @property
    def url(self) -> str:
        # strip off any query parameters to get a clean URL
        return self.full_url.split("?", 1)[0]

    @property
    def full_url(self) -> str:
        # this url may contain query parameters like pagination
        return self._url.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])

    @staticmethod
    def _url_path_elements(path: str, element: int = -1) -> list[str]:
        return path.split("?", 1)[0].split("/")


class CompletableGithubObjectWithPaginatedProperty(CompletableGithubObject):
    """
    A CompletableGithubObject that has a property that is subject to pagination.

    An instance created from a Requester with a non-default value for `per_page` must have the
    `per_page` value in the URL in order for the paginated property to use the `per_page` value.

    """

    def __init__(
        self,
        requester: Requester,
        headers: dict[str, str | int] | None = None,
        attributes: dict[str, Any] | None = None,
        completed: bool | None = None,
        *,
        url: str | None = None,
        accept: str | None = None,
        per_page: int | None = None,
    ):
        assert per_page is None or isinstance(per_page, int) and per_page > 0, per_page

        # add per_page to URL if instance is incomplete
        # we only modify the URL if this instance is incomplete
        if not completed:
            if per_page is None:
                # we use the default per_page (not Consts.DEFAULT_PER_PAGE as this URL might have a different default)
                # we set page=1 to get pagination links, PaginatedList can work from there
                url = self.set_if_not_set(attributes, url, page=1)
            else:
                # we set the given per_page
                url = self.set_if_not_set(attributes, url, per_page=per_page, page=1)

        super().__init__(requester, headers, attributes, completed, url=url, accept=accept)

    def _useAttributes(self, attributes: Any) -> None:
        # this object might have been created with an url while completing the object
        # provides another url, which might reset initial pagination information
        # we recover those pagination information here
        if is_defined(self._url) and "url" in attributes:
            parameters = self.requester.get_parameters_of_url(self.full_url)
            pagination_params = {"per_page", "page"}
            pagination = {
                k: v[0] for k, v in parameters.items() if k in pagination_params and isinstance(v, list) and len(v) == 1
            }
            attributes["url"] = self.set_values_if_not_set(attributes["url"], unless=pagination_params, **pagination)
        super()._useAttributes(attributes)

    @classmethod
    def set_if_not_set(
        cls, attributes: dict[str, Any] | None, url: str | None, unless: set[str] | None = None, **kwargs: Any
    ) -> str | None:
        # add values to the URL in the attributes
        if attributes is not None and "url" in attributes:
            attributes["url"] = cls.set_values_if_not_set(attributes["url"], unless, **kwargs)
        # add values to the request URL
        return cls.set_values_if_not_set(url, unless, **kwargs)

    @staticmethod
    def set_values_if_not_set(url: str | None, unless: set[str] | None = None, **kwargs: Any) -> str | None:
        if url is None:
            return url

        if unless is None:
            unless = set()

        from .Requester import Requester

        params = Requester.get_parameters_of_url(url)
        if any(p in params for p in unless):
            return url

        for k, v in kwargs.items():
            if k not in params:
                params[k] = [str(v)]
        return Requester.add_parameters_to_url(url, params)


Param = ParamSpec("Param")
RetType = TypeVar("RetType")


# decorator to annotate methods with OpenAPI metadata
def method_returns(
    *, schema_property: str | None = None
) -> Callable[[Callable[Param, RetType]], Callable[Param, RetType]]:
    def openapi_method_decorator(fn: Callable[Param, RetType]) -> Callable[Param, RetType]:
        return fn

    return openapi_method_decorator
