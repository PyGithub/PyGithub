from GithubObject import *

GitRef = GithubObject(
    "GitRef",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/git/" + obj.ref ),
    InternalSimpleAttributes(
        "ref", "url",
        "object",
        "_repo",
    ),
    Editable( Parameters( [ "sha" ], [ "force" ] ) ),
    Deletable(),
)
