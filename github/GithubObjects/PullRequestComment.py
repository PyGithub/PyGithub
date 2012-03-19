from NamedUser import *

PullRequestComment = GithubObject(
    "PullRequestComment",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/pulls/comments/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "id", "body", "path", "position", "commit_id",
        "created_at", "updated_at", "html_url", "line",
        "_repo",
    ),
    InternalObjectAttribute( "user", NamedUser ),
    Editable( Parameters( [ "body" ], [] ) ),
    Deletable(),
)
