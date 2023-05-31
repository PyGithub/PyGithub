from typing import List
import github.GithubObject
import github.EnvironmentProtectionRuleReviewer

class EnvironmentProtectionRule(github.GithubObject.CompletableGithubObject):
    @property
    def id(self) -> int: ...
    @property
    def node_id(self) -> str: ...
    @property
    def type(self) -> str: ...
    @property
    def reviewers(
        self,
    ) -> List[
        github.EnvironmentProtectionRuleReviewer.EnvironmentProtectionRuleReviewer
    ]: ...
    @property
    def wait_timer(self) -> int: ...
