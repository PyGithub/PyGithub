from datetime import datetime

from github.GithubObject import NonCompletableGithubObject

class StatsCodeFrequency(NonCompletableGithubObject):
    @property
    def additions(self) -> int: ...
    @property
    def deletions(self) -> int: ...
    @property
    def week(self) -> datetime: ...
