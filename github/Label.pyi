from __future__ import annotations

from typing import Any, Dict, Optional, Union

from github.GithubObject import CompletableGithubObject, _NotSetType

class Label(CompletableGithubObject):
    def __repr__(self) -> str: ...
    @property
    def _identity(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def color(self) -> str: ...
    def delete(self) -> None: ...
    @property
    def description(self) -> Optional[str]: ...
    def edit(self, name: str, color: str, description: Union[str, _NotSetType] = ...) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def url(self) -> str: ...
