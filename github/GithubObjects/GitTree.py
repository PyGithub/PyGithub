from GithubObject import *

GitTree = GithubObject(
    "GitTree",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/git/trees/" + obj.sha ),
    InternalSimpleAttributes(
        "sha", "url",
        "tree",
        "_repo",
    ),
)
