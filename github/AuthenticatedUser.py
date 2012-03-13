from GithubObject import *

from Authorization import Authorization
from UserKey import UserKey
from Event import Event
from NamedUser import NamedUser
from Organization import Organization

def __getOrganizationEvents( user, org ):
    return [
        Event( user._github, attributes, lazy = True )
        for attributes
        in user._github._dataRequest( "GET", "/users/" + user.login + "/events/orgs/" + org.login, None, None )
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
)
