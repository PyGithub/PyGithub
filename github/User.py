from GithubObject import *

AuthenticatedUser = GithubObject(
    "AuthenticatedUser",
    BaseUrl( lambda obj: "/user" ),
    SimpleScalarAttributes(
        "login", "id", "avatar_url", "gravatar_id", "url", "name", "company",
        "blog", "location", "email", "hireable", "bio", "public_repos",
        "public_gists", "followers", "following", "html_url", "created_at",
        "type", "total_private_repos", "owned_private_repos", "private_gists",
        "disk_usage", "collaborators", "plan",
    ),
)

NamedUser = GithubObject(
    "NamedUser",
    BaseUrl( lambda obj: "/users/" + obj.login ),
    SimpleScalarAttributes(
        "login", "id", "avatar_url", "gravatar_id", "url", "name", "company",
        "blog", "location", "email", "hireable", "bio", "public_repos",
        "public_gists", "followers", "following", "html_url", "created_at",
        "type",
    ),
)

Repository = GithubObject(
    "Repository",
    BaseUrl( lambda obj: "/repos/" + obj.owner.login + "/" + obj.name ),
    SimpleScalarAttributes(
        "url", "html_url", "clone_url", "git_url", "ssh_url", "svn_url",
        "name", "description", "homepage", "language", "private",
        "fork", "forks", "watchers", "size", "master_branch", "open_issues",
        "pushed_at", "created_at", "organization", "parent", "source",
        "has_issues", "has_wiki", "has_downloads",
        # Not documented
        "mirror_url", "updated_at", "id",
    ),
    ExtendedScalarAttribute( "owner", NamedUser ),
)

AuthenticatedUser._addAttributePolicy( ExtendedListAttribute( "repos", Repository ) )
NamedUser._addAttributePolicy( ExtendedListAttribute( "repos", Repository ) )
