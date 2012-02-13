from GithubObject import *

AuthenticatedUser = GithubObject(
    "AuthenticatedUser",
    BaseUrl( lambda obj: "/user" ),
    Identity( lambda obj: obj.login ),
    SimpleScalarAttributes(
        "login", "id", "avatar_url", "gravatar_id", "url", "name", "company",
        "blog", "location", "email", "hireable", "bio", "public_repos",
        "public_gists", "followers", "following", "html_url", "created_at",
        "type", "total_private_repos", "owned_private_repos", "private_gists",
        "disk_usage", "collaborators", "plan",
    ),
    Editable( [], [ "name", "email", "blog", "company", "location", "hireable", "bio" ] ),
)

NamedUser = GithubObject(
    "NamedUser",
    BaseUrl( lambda obj: "/users/" + obj.login ),
    Identity( lambda obj: obj.login ),
    SimpleScalarAttributes(
        "login", "id", "avatar_url", "gravatar_id", "url", "name", "company",
        "blog", "location", "email", "hireable", "bio", "public_repos",
        "public_gists", "followers", "following", "html_url", "created_at",
        "type",
        # Only in Repository.get_contributors()
        "contributions",
    ),
)

AuthenticatedUser._addAttributePolicy( ExtendedListAttribute( "followers", NamedUser ) )
NamedUser._addAttributePolicy( ExtendedListAttribute( "followers", NamedUser ) )

AuthenticatedUser._addAttributePolicy( ExtendedListAttribute( "following", NamedUser, True, True ) )
NamedUser._addAttributePolicy( ExtendedListAttribute( "following", NamedUser ) )

Organization = GithubObject(
    "Organization",
    BaseUrl( lambda obj: "/orgs/" + obj.login ),
    Identity( lambda obj: obj.login ),
    SimpleScalarAttributes(
        "login", "id", "url", "avatar_url", "name", "company", "blog",
        "location", "email", "public_repos", "public_gists", "followers",
        "following", "html_url", "created_at", "type",
        # Seen only by owners
        "disk_usage", "collaborators", "billing_email", "plan", "private_gists",
        "total_private_repos", "owned_private_repos",
    ),
    ExtendedListAttribute( "public_members", NamedUser, True, True ),
    ExtendedListAttribute( "members", NamedUser, removable = True ),
    Editable( [], [ "billing_email", "blog", "company", "email", "location", "name" ] ),
)

AuthenticatedUser._addAttributePolicy( ExtendedListAttribute( "orgs", Organization ) )
NamedUser._addAttributePolicy( ExtendedListAttribute( "orgs", Organization ) )

Repository = GithubObject(
    "Repository",
    BaseUrl( lambda obj: "/repos/" + obj.owner.login + "/" + obj.name ),
    Identity( lambda obj: obj.owner.login + "/" + obj.name ),
    SimpleScalarAttributes(
        "url", "html_url", "clone_url", "git_url", "ssh_url", "svn_url",
        "name", "description", "homepage", "language", "private",
        "fork", "forks", "watchers", "size", "master_branch", "open_issues",
        "pushed_at", "created_at", "organization",
        "has_issues", "has_wiki", "has_downloads",
        # Not documented
        "mirror_url", "updated_at", "id",
    ),
    ExtendedScalarAttribute( "owner", NamedUser ),
    ExtendedListAttribute( "collaborators", NamedUser ),
    ExtendedListAttribute( "contributors", NamedUser ),
    ExtendedListAttribute( "watchers", NamedUser ),
    Editable( [ "name" ], [ "description", "homepage", "public", "has_issues", "has_wiki", "has_downloads" ] ),
)
Repository._addAttributePolicy( ExtendedScalarAttribute( "parent", Repository ) )
Repository._addAttributePolicy( ExtendedScalarAttribute( "source", Repository ) )
Repository._addAttributePolicy( ExtendedListAttribute( "forks", Repository ) )

AuthenticatedUser._addAttributePolicy( ExtendedListAttribute( "repos", Repository ) )
NamedUser._addAttributePolicy( ExtendedListAttribute( "repos", Repository ) )
Organization._addAttributePolicy( ExtendedListAttribute( "repos", Repository ) )

AuthenticatedUser._addAttributePolicy( ExtendedListAttribute( "watched", Repository, True, True ) )
NamedUser._addAttributePolicy( ExtendedListAttribute( "watched", Repository ) )
