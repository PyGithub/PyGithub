from GithubObject import *

GitTag = GithubObject(
    "GitTag",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/git/tags/" + obj.sha ),
    InternalSimpleAttributes(
        "tag", "sha", "url",
        "message",
        "tagger",
        "object",
        "_repo",
    ),
)
