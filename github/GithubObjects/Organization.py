from NamedUser import *

Organization = GithubObject(
    "Organization",
    BaseUrl( lambda obj: "/orgs/" + obj.login ),
    Identity( lambda obj: obj.login ),
    InternalSimpleAttributes(
        "login", "id", "url", "avatar_url", "name", "company", "blog",
        "location", "email", "public_repos", "public_gists", "followers",
        "following", "html_url", "created_at", "type", "gravatar_id",
        # Seen only by owners
        "disk_usage", "collaborators", "billing_email", "plan", "private_gists",
        "total_private_repos", "owned_private_repos",
    ),
    Editable( Parameters( [], [ "billing_email", "blog", "company", "email", "location", "name" ] ) ),
    ExternalListOfObjects( "public_members", "public_member", NamedUser,
        ListGetable( Parameters( [], [] ) ),
        ElementAddable(),
        ElementRemovable(),
        ElementHasable()
    ),
    ExternalListOfObjects( "members", "member", NamedUser,
        ListGetable( Parameters( [], [] ) ),
        ElementRemovable(),
        ElementHasable()
    ),
)
