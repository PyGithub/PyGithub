from typing import Any, Dict, List

from github.GithubObject import NonCompletableGithubObject

class StatsParticipation(NonCompletableGithubObject):
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, List[int]]) -> None: ...
    @property
    def all(self) -> List[int]: ...
    @property
    def owner(self) -> List[int]: ...
