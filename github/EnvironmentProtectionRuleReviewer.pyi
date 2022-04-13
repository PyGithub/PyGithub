import datetime
from typing import List, Union
import github.GithubObject
import github.NamedUser
import github.Team


class EnvironmentProtectionRuleReviewer(github.GithubObject.NonCompletableGithubObject):
    @property
    def type(self) -> str: ...
    @property
    def reviewer(self) -> Union[github.NamedUser.NamedUser, github.Team.Team]: ...
