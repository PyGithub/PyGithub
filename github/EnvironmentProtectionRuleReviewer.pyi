from typing import Union
import github.GithubObject
import github.NamedUser
import github.Team

class EnvironmentProtectionRuleReviewer(github.GithubObject.NonCompletableGithubObject):
    @property
    def type(self) -> str: ...
    @property
    def reviewer(self) -> Union[github.NamedUser.NamedUser, github.Team.Team]: ...

class ReviewerParams:
    def __init__(self, type_: str, id_: int): ...
    def _asdict(self) -> dict: ...
