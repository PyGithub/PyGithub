from NamedUser import *
from Repository import *

Team = GithubObject(
    "Team",
    BaseUrl( lambda obj: "/teams/" + str( obj.id ) ),
    Identity( lambda obj: str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "name", "id", "permission", "members_count", "repos_count",
    ),
    Editable( Parameters( [ "name" ], [ "permission" ] ) ),
    Deletable(),
    ExternalListOfObjects( "members", "member", NamedUser,
        ListGetable( Parameters( [], [] ) ),
        ElementAddable(),
        ElementRemovable(),
        ElementHasable()
    ),
    ExternalListOfObjects( "repos", "repo", Repository,
        ListGetable( Parameters( [], [] ) ),
        ElementAddable(),
        ElementRemovable(),
        ElementHasable()
    ),
)
