from Authorization import *
from UserKey import *
from Event import *
from NamedUser import *
from Organization import *
from Repository import *
from Gist import *
from Issue import *

def __getOrganizationEvents( user, org ):
    return [
        Event( user._github, attributes, lazy = True )
        for attributes
        in user._github._dataRequest( "GET", "/users/" + user.login + "/events/orgs/" + org.login, None, None )
    ]

def __createFork( user, repo ):
    assert isinstance( repo, Repository )
    return Repository( user._github, user._github._dataRequest( "POST", repo._baseUrl() + "/forks", None, None ), lazy = True )

def __getStaredGists( user ):
    return [
        Gist( user._github, attributes, lazy = True )
        for attributes in user._github._dataRequest( "GET", "/gists/starred", None, None )
    ]

AuthenticatedUser = GithubObject(
    "AuthenticatedUser",
    BaseUrl( lambda obj: "/user" ),
    Identity( lambda obj: obj.login ),
    InternalSimpleAttributes(
        "login", "id", "avatar_url", "gravatar_id", "url", "name", "company",
        "blog", "location", "email", "hireable", "bio", "public_repos",
        "public_gists", "followers", "following", "html_url", "created_at",
        "type", "total_private_repos", "owned_private_repos", "private_gists",
        "disk_usage", "collaborators", "plan",
    ),
    Editable( Parameters( [], [ "name", "email", "blog", "company", "location", "hireable", "bio" ] ) ),
    ExternalListOfSimpleTypes( "emails", "email", "string",
        ListGetable( Parameters( [], [] ) ),
        SeveralElementsAddable(),
        SeveralElementsRemovable()
    ),
    ExternalListOfObjects( "authorizations", "authorization", Authorization,
        ListGetable( Parameters( [], [] ) ),
        ElementGetable( Parameters( [ "id" ], [] ) ),
        ElementCreatable( Parameters( [], [ "scopes", "note", "note_url" ] ) ),
        url = "/authorizations",
    ),
    ExternalListOfObjects( "keys", "key", UserKey,
        ListGetable( Parameters( [], [] ) ),
        ElementGetable( Parameters( [ "id" ], [] ) ),
        ElementCreatable( Parameters( [ "title", "key" ], [] ) ),
    ),
    ExternalListOfObjects( "events", "event", Event,
        ListGetable( Parameters( [], [] ) ),
        url = "/events"
    ),
    ExternalListOfObjects( "followers", "follower", NamedUser,
        ListGetable( Parameters( [], [] ) )
    ),
    ExternalListOfObjects( "following", "following", NamedUser,
        ListGetable( Parameters( [], [] ) ),
        ElementAddable(),
        ElementRemovable(),
        ElementHasable()
    ),
    ExternalListOfObjects( "orgs", "org", Organization,
        ListGetable( Parameters( [], [] ) )
    ),
    MethodFromCallable( "get_organization_events", Parameters( [ "org" ], [] ), __getOrganizationEvents, SimpleTypePolicy( "list of `Event`" ) ),
    ExternalListOfObjects( "repos", "repo", Repository,
        ListGetable( Parameters( [], [ "type" ] ) ),
        ElementGetable( Parameters( [ "name" ], [] ), { "owner" : lambda user: { "login": user.login } } ),
        ElementCreatable( Parameters( [ "name" ], [ "description", "homepage", "private", "has_issues", "has_wiki", "has_downloads", "team_id", ] ) )
    ),
    ExternalListOfObjects( "watched", "watched", Repository,
        ListGetable( Parameters( [], [] ) ),
        ElementAddable(),
        ElementRemovable(),
        ElementHasable()
    ),
    SeveralAttributePolicies( [ MethodFromCallable( "create_fork", Parameters( [ "repo" ], [] ), __createFork, ObjectTypePolicy( Repository ) ) ], "Forking" ),
    ExternalListOfObjects( "gists", "gist", Gist,
        ListGetable( Parameters( [], [] ) ),
        ElementCreatable( Parameters( [ "public", "files", ], [ "description" ] ) ),
        url = "/gists",
    ),
    MethodFromCallable( "get_starred_gists", Parameters( [], [] ), __getStaredGists, SimpleTypePolicy( "list of `Gist`" ) ),
    ExternalListOfObjects( "issues", "issue", Issue,
        ListGetable( Parameters( [], [] ) ),
        url = "/issues",
    ),
)
