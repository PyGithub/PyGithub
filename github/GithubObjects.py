from GithubObject import *

AuthenticatedUser = GithubObject(
    "AuthenticatedUser",
    BaseUrl( lambda obj: "/user" ),
    Identity( lambda obj: obj.login ),
    BasicAttributes(
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
    BasicAttributes(
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

AuthenticatedUser._addAttributePolicy( ListOfReferences( "followers", NamedUser ) )
NamedUser._addAttributePolicy( ListOfReferences( "followers", NamedUser ) )

AuthenticatedUser._addAttributePolicy( ListOfReferences( "following", NamedUser, addable = True, removable = True, hasable = True ) )
NamedUser._addAttributePolicy( ListOfReferences( "following", NamedUser ) )

Organization = GithubObject(
    "Organization",
    BaseUrl( lambda obj: "/orgs/" + obj.login ),
    Identity( lambda obj: obj.login ),
    BasicAttributes(
        "login", "id", "url", "avatar_url", "name", "company", "blog",
        "location", "email", "public_repos", "public_gists", "followers",
        "following", "html_url", "created_at", "type",
        # Seen only by owners
        "disk_usage", "collaborators", "billing_email", "plan", "private_gists",
        "total_private_repos", "owned_private_repos",
    ),
    ListOfReferences( "public_members", NamedUser, addable = True, removable = True, hasable = True ),
    ListOfReferences( "members", NamedUser, removable = True, hasable = True ),
    Editable( [], [ "billing_email", "blog", "company", "email", "location", "name" ] ),
)

AuthenticatedUser._addAttributePolicy( ListOfReferences( "orgs", Organization ) )
NamedUser._addAttributePolicy( ListOfReferences( "orgs", Organization ) )

Repository = GithubObject(
    "Repository",
    BaseUrl( lambda obj: "/repos/" + obj.owner.login + "/" + obj.name ),
    Identity( lambda obj: obj.owner.login + "/" + obj.name ),
    BasicAttributes(
        "url", "html_url", "clone_url", "git_url", "ssh_url", "svn_url",
        "name", "description", "homepage", "language", "private",
        "fork", "forks", "watchers", "size", "master_branch", "open_issues",
        "pushed_at", "created_at", "organization",
        "has_issues", "has_wiki", "has_downloads",
        # Not documented
        "mirror_url", "updated_at", "id",
    ),
    ComplexAttribute( "owner", NamedUser ),
    ListOfReferences( "collaborators", NamedUser, addable = True, removable = True, hasable = True ),
    ListOfReferences( "contributors", NamedUser ),
    ListOfReferences( "watchers", NamedUser ),
    Editable( [ "name" ], [ "description", "homepage", "public", "has_issues", "has_wiki", "has_downloads" ] ),
)
Repository._addAttributePolicy( ComplexAttribute( "parent", Repository ) )
Repository._addAttributePolicy( ComplexAttribute( "source", Repository ) )
Repository._addAttributePolicy( ListOfReferences( "forks", Repository ) )

AuthenticatedUser._addAttributePolicy( ListOfObjects( "repos", Repository, creatable = True, singularName = "repo" ) )
NamedUser._addAttributePolicy( ListOfObjects( "repos", Repository ) )
Organization._addAttributePolicy( ListOfObjects( "repos", Repository, creatable = True, singularName = "repo" ) )

def __repoFromUser( user, name ):
    return Repository( user._github, { "name": name, "owner": { "login": user.login } }, lazy = False )
AuthenticatedUser._addAttributePolicy( MethodFromCallable( "get_repo", __repoFromUser ) )
NamedUser._addAttributePolicy( MethodFromCallable( "get_repo", __repoFromUser ) )
Organization._addAttributePolicy( MethodFromCallable( "get_repo", __repoFromUser ) )

AuthenticatedUser._addAttributePolicy( ListOfReferences( "watched", Repository, addable = True, removable = True, hasable = True ) )
NamedUser._addAttributePolicy( ListOfReferences( "watched", Repository ) )

def __createForkForUser( user, repo ):
    assert isinstance( repo, Repository )
    return Repository( user._github, user._github._dataRequest( "POST", repo._baseUrl + "/forks", None, None ), lazy = True )
AuthenticatedUser._addAttributePolicy( MethodFromCallable( "create_fork", __createForkForUser ) )
def __createForkForOrg( org, repo ):
    assert isinstance( repo, Repository )
    return Repository( org._github, org._github._dataRequest( "POST", repo._baseUrl + "/forks", { "org": org.login }, None ), lazy = True )
Organization._addAttributePolicy( MethodFromCallable( "create_fork", __createForkForOrg ) )
