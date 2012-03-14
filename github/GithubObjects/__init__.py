from GithubObject import *

from AuthenticatedUser import *
from NamedUser import *
from Organization import *
from Repository import *
from Gist import *
from Team import *

#### Complete NamedUser

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "orgs", "org", Organization,
        ListGetable( [], [] )
    )
)

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "events", "event", Event,
        ListGetable( [], [] )
    )
)

def __getPublicEvents( user ):
    return [
        Event( user._github, attributes, lazy = True )
        for attributes
        in user._github._dataRequest( "GET", user._baseUrl() + "/events/public", None, None )
    ]

NamedUser._addAttributePolicy(
    MethodFromCallable( "get_public_events", [], [], __getPublicEvents, SimpleTypePolicy( "list of `Event`" ) )
)

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "received_events", "received_event", Event,
        ListGetable( [], [] )
    )
)

def __getPublicReceivedEvents( user ):
    return [
        Event( user._github, attributes, lazy = True )
        for attributes
        in user._github._dataRequest( "GET", user._baseUrl() + "/received_events/public", None, None )
    ]

NamedUser._addAttributePolicy(
    MethodFromCallable( "get_public_received_events", [], [], __getPublicReceivedEvents, SimpleTypePolicy( "list of `Event`" ) )
)

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "repos", "repo", Repository,
        ListGetable( [], [ "type" ] ),
        ElementGetable( [ "name" ], [], { "owner" : lambda user: { "login": user.login } } )
    )
)

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "watched", "watched", Repository,
        ListGetable( [], [] )
    )
)

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "gists", "gist", Gist,
        ListGetable( [], [] ),
    )
)

#### Complete Repository

Repository._addAttributePolicy(
    ExternalListOfObjects( "teams", "team", Team,
        ListGetable( [], [] )
    )
)

Repository._addAttributePolicy(
    ExternalListOfObjects( "events", "event", Event,
        ListGetable( [], [] )
    ),
)

def __getNetworkEvents( repo ):
    return [
        Event( repo._github, attributes, lazy = True )
        for attributes
        in repo._github._dataRequest( "GET", "/networks/" + repo.owner.login + "/" + repo.name + "/events", None, None )
    ]

Repository._addAttributePolicy(
    MethodFromCallable( "get_network_events", [], [], __getNetworkEvents, SimpleTypePolicy( "list of `Event`" ) )
)

#### Complete Organization

Organization._addAttributePolicy(
    ExternalListOfObjects( "repos", "repo", Repository,
        ListGetable( [], [ "type" ] ),
        ElementGetable( [ "name" ], [], { "owner" : lambda user: { "login": user.login } } ),
        ElementCreatable( [ "name" ], [ "description", "homepage", "private", "has_issues", "has_wiki", "has_downloads", "team_id", ] )
    )
)

def __createForkForOrg( org, repo ):
    assert isinstance( repo, Repository )
    return Repository( org._github, org._github._dataRequest( "POST", repo._baseUrl() + "/forks", { "org": org.login }, None ), lazy = True )

Organization._addAttributePolicy(
    SeveralAttributePolicies( [ MethodFromCallable( "create_fork", [ "repo" ], [], __createForkForOrg, ObjectTypePolicy( Repository ) ) ], "Forking" )
)

Organization._addAttributePolicy(
    ExternalListOfObjects( "teams", "team", Team,
        ListGetable( [], [] ),
        ElementCreatable( [ "name" ], [ "repo_names", "permission" ] )
    )
)

Organization._addAttributePolicy(
    ExternalListOfObjects( "events", "event", Event,
        ListGetable( [], [] )
    ),
)
