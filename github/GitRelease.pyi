from datetime import datetime
from typing import Any, Dict, Union

from github.GithubObject import CompletableGithubObject, _NotSetType
from github.GitReleaseAsset import GitReleaseAsset
from github.NamedUser import NamedUser
from github.PaginatedList import PaginatedList

class GitRelease(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def author(self) -> NamedUser: ...
    @property
    def body(self) -> str: ...
    @property
    def created_at(self) -> datetime: ...
    def delete_release(self) -> None: ...
    @property
    def draft(self) -> bool: ...
    def get_assets(self) -> PaginatedList[GitReleaseAsset]: ...
    @property
    def html_url(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def prerelease(self) -> bool: ...
    @property
    def generate_release_notes(self) -> bool: ...
    @property
    def published_at(self) -> datetime: ...
    @property
    def tag_name(self) -> str: ...
    @property
    def tarball_url(self) -> str: ...
    @property
    def target_commitish(self) -> str: ...
    @property
    def title(self) -> str: ...
    def update_release(
        self,
        name: str,
        message: str,
        draft: bool = ...,
        prerelease: bool = ...,
        tag_name: Union[str, _NotSetType] = ...,
        target_commitish: Union[str, _NotSetType] = ...,
    ) -> GitRelease: ...
    def upload_asset(
        self,
        path: str,
        label: str = ...,
        content_type: Union[_NotSetType, str] = ...,
        name: Union[_NotSetType, str] = ...,
    ) -> GitReleaseAsset: ...
    @property
    def upload_url(self) -> str: ...
    @property
    def url(self) -> str: ...
    @property
    def zipball_url(self) -> str: ...
