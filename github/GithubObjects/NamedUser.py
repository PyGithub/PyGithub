from GithubObject import *

NamedUser = GithubObject(
    "NamedUser",
    BaseUrl( lambda obj: "/users/" + obj.login ),
    Identity( lambda obj: obj.login ),
    InternalSimpleAttributes(
        "login", "id", "avatar_url", "gravatar_id", "url", "name", "company",
        "blog", "location", "email", "hireable", "bio", "public_repos",
        "public_gists", "followers", "following", "html_url", "created_at",
        "type",
        # Only in Repository.get_contributors()
        "contributions",
        # Seen only by user herself
        "disk_usage", "collaborators", "plan", "total_private_repos",
        "owned_private_repos", "private_gists",
    ),
)

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "followers", "follower", NamedUser,
        ListGetable( Parameters( [], [] ) )
    )
)

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "following", "following", NamedUser,
        ListGetable( Parameters( [], [] ) )
    )
)
