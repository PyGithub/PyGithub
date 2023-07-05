from github.GithubObject import NonCompletableGithubObject

class StatsPunchCard(NonCompletableGithubObject):
    def get(self, day: int, hour: int) -> int: ...
