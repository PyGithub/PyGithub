from typing import Any, Dict

from github.GithubObject import CompletableGithubObject

class SourceImport(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def authors_count(self) -> int: ...
    @property
    def authors_url(self) -> str: ...
    @property
    def has_large_files(self) -> bool: ...
    @property
    def html_url(self) -> str: ...
    @property
    def large_files_count(self) -> int: ...
    @property
    def large_files_size(self) -> int: ...
    @property
    def repository_url(self) -> str: ...
    @property
    def status(self) -> str: ...
    @property
    def status_text(self) -> str: ...
    @property
    def url(self) -> str: ...
    @property
    def use_lfs(self) -> str: ...
    @property
    def vcs(self) -> str: ...
    @property
    def vcs_url(self) -> str: ...
