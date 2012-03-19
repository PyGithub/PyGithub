from GithubObject import *

GitTree = GithubObject(
    "GitTree",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/git/trees/" + obj.sha + ( "?recursive=1" if obj.recursive else "" ) ),
    InternalSimpleAttributes(
        "sha", "url",
        "tree",
        "_repo", "recursive",
    ),
)
