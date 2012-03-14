from GithubObject import *

from Authorization import Authorization
from UserKey import UserKey
from Event import Event
from NamedUser import NamedUser
from Organization import Organization
from Repository import Repository
from Gist import Gist

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
    Editable( [], [ "name", "email", "blog", "company", "location", "hireable", "bio" ] ),
    ExternalListOfSimpleTypes( "emails", "email", "string",
        ListGetable( [], [] ),
        SeveralElementsAddable(),
        SeveralElementsRemovable()
    ),
    ExternalListOfObjects( "authorizations", "authorization", Authorization,
        ListGetable( [], [] ),
        ElementGetable( [ "id" ], [] ),
        ElementCreatable( [], [ "scopes", "note", "note_url" ] ),
        url = "/authorizations",
    ),
    ExternalListOfObjects( "keys", "key", UserKey,
        ListGetable( [], [] ),
        ElementGetable( [ "id" ], [] ),
        ElementCreatable( [ "title", "key" ], [] ),
    ),
    ExternalListOfObjects( "events", "event", Event,
        ListGetable( [], [] ),
        url = "/events"
    ),
    ExternalListOfObjects( "followers", "follower", NamedUser,
        ListGetable( [], [] )
    ),
    ExternalListOfObjects( "following", "following", NamedUser,
        ListGetable( [], [] ),
        ElementAddable(),
        ElementRemovable(),
        ElementHasable()
    ),
    ExternalListOfObjects( "orgs", "org", Organization,
        ListGetable( [], [] )
    ),
    MethodFromCallable( "get_organization_events", [ "org" ], [], __getOrganizationEvents, SimpleTypePolicy( "list of `Event`" ) ),
    ExternalListOfObjects( "repos", "repo", Repository,
        ListGetable( [], [ "type" ] ),
        ElementGetable( [ "name" ], [], { "owner" : lambda user: { "login": user.login } } ),
        ElementCreatable( [ "name" ], [ "description", "homepage", "private", "has_issues", "has_wiki", "has_downloads", "team_id", ] )
    ),
    ExternalListOfObjects( "watched", "watched", Repository,
        ListGetable( [], [] ),
        ElementAddable(),
        ElementRemovable(),
        ElementHasable()
    ),
    SeveralAttributePolicies( [ MethodFromCallable( "create_fork", [ "repo" ], [], __createFork, ObjectTypePolicy( Repository ) ) ], "Forking" ),
    ExternalListOfObjects( "gists", "gist", Gist,
        ListGetable( [], [] ),
        ElementCreatable( [ "public", "files", ], [ "description" ] ),
        url = "/gists",
    ),
    MethodFromCallable( "get_starred_gists", [], [], __getStaredGists, SimpleTypePolicy( "list of `Gist`" ) ),
)
