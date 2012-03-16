from Repository import *

from Team import *
from Event import *

Repository._addAttributePolicy(
    ExternalListOfObjects( "teams", "team", Team,
        ListGetable( Parameters( [], [] ) )
    )
)

Repository._addAttributePolicy(
    ExternalListOfObjects( "events", "event", Event,
        ListGetable( Parameters( [], [] ) )
    ),
)

def __getNetworkEvents( repo ):
    return [
        Event( repo._github, attributes, lazy = True )
        for attributes
        in repo._github._dataRequest( "GET", "/networks/" + repo.owner.login + "/" + repo.name + "/events", None, None )
    ]

Repository._addAttributePolicy(
    MethodFromCallable( "get_network_events", Parameters( [], [] ), __getNetworkEvents, SimpleTypePolicy( "list of `Event`" ) )
)
