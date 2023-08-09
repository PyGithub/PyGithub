from datetime import datetime
from typing import Any, Dict

from github.GithubObject import CompletableGithubObject
from github.NamedUser import NamedUser

class GitReleaseAsset(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def browser_download_url(self) -> str: ...
    @property
    def content_type(self) -> str: ...
    @property
    def created_at(self) -> datetime: ...
    def delete_asset(self) -> bool: ...
    @property
    def download_count(self) -> int: ...
    @property
    def id(self) -> int: ...
    @property
    def label(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def size(self) -> int: ...
    @property
    def state(self) -> str: ...
    def update_asset(self, name: str, label: str = ...) -> GitReleaseAsset: ...
    @property
    def updated_at(self) -> datetime: ...
    @property
    def uploader(self) -> NamedUser: ...
    @property
    def url(self) -> str: ...
