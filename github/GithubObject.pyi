from typing import Any, Callable, Dict, List, Optional, Type, Union

from github.Commit import Commit
from github.GistFile import GistFile
from github.GitRelease import GitRelease
from github.NamedUser import NamedUser
from github.Organization import Organization
from github.PullRequestReview import PullRequestReview
from github.Requester import Requester

class GithubObject:
    def __init__(
        self,
        requester: Optional[Requester],
        headers: Dict[str, Union[str, int]],
        attributes: Any,
        completed: bool,
    ) -> None: ...
    @staticmethod
    def _makeBoolAttribute(value: Optional[bool]) -> _ValuedAttribute: ...
    def _makeClassAttribute(
        self, klass: Any, value: Any
    ) -> Union[_ValuedAttribute, _BadAttribute]: ...
    @staticmethod
    def _makeDatetimeAttribute(
        value: Optional[Union[int, str]]
    ) -> Union[_ValuedAttribute, _BadAttribute]: ...
    @staticmethod
    def _makeDictAttribute(value: Dict[str, Any]) -> _ValuedAttribute: ...
    def _makeDictOfStringsToClassesAttribute(
        self,
        klass: Type[GistFile],
        value: Dict[
            str,
            Union[int, Dict[str, Union[str, int, None]], Dict[str, Union[str, int]]],
        ],
    ) -> Union[_ValuedAttribute, _BadAttribute]: ...
    @staticmethod
    def _makeIntAttribute(
        value: Optional[Union[int, str]]
    ) -> Union[_ValuedAttribute, _BadAttribute]: ...
    def _makeListOfClassesAttribute(
        self, klass: Any, value: Any
    ) -> Union[_ValuedAttribute, _BadAttribute]: ...
    @staticmethod
    def _makeListOfDictsAttribute(
        value: List[Dict[str, Union[str, List[Dict[str, Union[str, List[int]]]]]]]
    ) -> _ValuedAttribute: ...
    @staticmethod
    def _makeListOfIntsAttribute(value: List[int]) -> _ValuedAttribute: ...
    @staticmethod
    def _makeListOfListOfStringsAttribute(
        value: List[List[str]],
    ) -> _ValuedAttribute: ...
    @staticmethod
    def _makeListOfStringsAttribute(
        value: Union[List[List[str]], List[str], List[Union[str, int]]]
    ) -> Union[_ValuedAttribute, _BadAttribute]: ...
    @staticmethod
    def __makeSimpleAttribute(
        value: Any, type: type
    ) -> Union[_ValuedAttribute, _BadAttribute]: ...
    @staticmethod
    def __makeSimpleListAttribute(
        value: list, type: type
    ) -> Union[_ValuedAttribute, _BadAttribute]: ...
    @staticmethod
    def __makeTransformedAttribute(
        value: Any, type: type, transform: Callable[..., Any]
    ) -> Union[_ValuedAttribute, _BadAttribute]: ...
    @staticmethod
    def _makeStringAttribute(
        value: Optional[Union[int, str]]
    ) -> Union[_ValuedAttribute, _BadAttribute]: ...
    @staticmethod
    def _makeTimestampAttribute(value: int) -> _ValuedAttribute: ...
    @staticmethod
    def _parentUrl(url: str) -> str: ...
    def _storeAndUseAttributes(
        self, headers: Dict[str, Union[str, int]], attributes: Any
    ) -> None: ...
    @property
    def etag(self) -> Optional[str]: ...
    def get__repr__(self, params: Dict[str, Any]) -> str: ...
    @property
    def last_modified(self) -> Optional[str]: ...
    @property
    def raw_data(self) -> Dict[str, Any]: ...
    @property
    def raw_headers(self) -> Dict[str, Union[str, int]]: ...
    @classmethod
    def setCheckAfterInitFlag(cls, flag: bool) -> None: ...

class NonCompletableGithubObject(GithubObject):
    def _completeIfNeeded(self) -> None: ...

class CompletableGithubObject(GithubObject):
    def __eq__(self, other: Any) -> bool: ...
    def __init__(
        self,
        requester: Requester,
        headers: Dict[str, Union[str, int]],
        attributes: Dict[str, Any],
        completed: bool,
    ) -> None: ...
    def __ne__(self, other: Any) -> bool: ...
    def _completeIfNeeded(self) -> None: ...
    def _completeIfNotSet(
        self, value: Union[_ValuedAttribute, _BadAttribute, _NotSetType]
    ) -> None: ...
    def update(self) -> bool: ...

class _BadAttribute:
    def __init__(
        self, value: Any, expectedType: Any, exception: Optional[ValueError] = ...
    ) -> None: ...
    @property
    def value(self) -> Any: ...

class _NotSetType:
    def __repr__(self) -> str: ...

class _ValuedAttribute:
    def __init__(self, value: Any) -> None: ...
