from GithubObject import *

from Event import Event

def __getPublicEvents( user ):
    return [
        Event( user._github, attributes, lazy = True )
        for attributes
        in user._github._dataRequest( "GET", user._baseUrl() + "/events/public", None, None )
    ]

def __getPublicReceivedEvents( user ):
    return [
        Event( user._github, attributes, lazy = True )
        for attributes
        in user._github._dataRequest( "GET", user._baseUrl() + "/received_events/public", None, None )
    ]

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
    ExternalListOfObjects( "events", "event", Event,
        ListGetable( [], [] )
    ),
    MethodFromCallable( "get_public_events", [], [], __getPublicEvents, SimpleTypePolicy( "list of `Event`" ) ),
    ExternalListOfObjects( "received_events", "received_event", Event,
        ListGetable( [], [] )
    ),
    MethodFromCallable( "get_public_received_events", [], [], __getPublicReceivedEvents, SimpleTypePolicy( "list of `Event`" ) ),
)

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "followers", "follower", NamedUser,
        ListGetable( [], [] )
    )
)

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "following", "following", NamedUser,
        ListGetable( [], [] )
    )
)
