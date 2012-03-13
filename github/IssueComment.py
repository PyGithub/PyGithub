from GithubObject import *

from NamedUser import NamedUser

IssueComment = GithubObject(
    "IssueComment",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/issues/comments/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "body", "created_at", "updated_at", "id",
        "_repo",
    ),
    InternalObjectAttribute( "user", NamedUser ),
    Editable( [ "body" ], [] ),
    Deletable(),
)
