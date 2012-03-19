from GitTree import *

GitCommit = GithubObject(
    "GitCommit",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/git/commits/" + obj.sha ),
    InternalSimpleAttributes(
        "sha", "url", "message",
        "parents",
        "author", "committer",
        "_repo",
    ),
    InternalObjectAttribute( "tree", GitTree ),
)
