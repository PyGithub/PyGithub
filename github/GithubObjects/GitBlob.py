from GithubObject import *

GitBlob = GithubObject(
    "GitBlob",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/git/blobs/" + obj.sha ),
    InternalSimpleAttributes(
        "sha", "size", "url",
        "content", "encoding",
        "_repo",
    ),
)
