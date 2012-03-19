from GithubObject import *

RepositoryKey = GithubObject(
    "RepositoryKey",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/keys/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "id", "title", "key",
        "_repo",
    ),
    Editable( Parameters( [ "title", "key" ], [] ) ),
    Deletable()
)
