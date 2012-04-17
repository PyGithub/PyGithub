from NamedUser import *

from Organization import *
from Event import *
from Repository import *
from Gist import *

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "orgs", "org", Organization,
        ListGetable( Parameters( [], [] ) )
    )
)

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "events", "event", Event,
        ListGetable( Parameters( [], [] ) )
    )
)

def __getPublicEvents( user ):
    return [
        Event( user._github, attributes, lazy = True )
        for attributes
        in user._github._dataRequest( "GET", user._baseUrl() + "/events/public", None, None )
    ]

NamedUser._addAttributePolicy(
    MethodFromCallable( "get_public_events", Parameters( [], [] ), __getPublicEvents, SimpleTypePolicy( "list of `Event`" ) )
)

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "received_events", "received_event", Event,
        ListGetable( Parameters( [], [] ) )
    )
)

def __getPublicReceivedEvents( user ):
    return [
        Event( user._github, attributes, lazy = True )
        for attributes
        in user._github._dataRequest( "GET", user._baseUrl() + "/received_events/public", None, None )
    ]

NamedUser._addAttributePolicy(
    MethodFromCallable( "get_public_received_events", Parameters( [], [] ), __getPublicReceivedEvents, SimpleTypePolicy( "list of `Event`" ) )
)

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "repos", "repo", Repository,
        ListGetable( Parameters( [], [ "type" ] ) ),
        ElementGetable( Parameters( [ "name" ], [] ), { "owner" : lambda user: { "login": user.login } } )
    )
)

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "watched", "watched", Repository,
        ListGetable( Parameters( [], [] ) )
    )
)

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "gists", "gist", Gist,
        ListGetable( Parameters( [], [] ) ),
        ElementCreatable( Parameters( [ "public", "files" ], [ "description" ] ) ),
    )
)
