from NamedUser import *

IssueComment = GithubObject(
    "IssueComment",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/issues/comments/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "body", "created_at", "updated_at", "id",
        "_repo",
    ),
    InternalObjectAttribute( "user", NamedUser ),
    Editable( Parameters( [ "body" ], [] ) ),
    Deletable(),
)
