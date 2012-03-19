from Organization import *

from Repository import *
from Team import *
from Event import *

Organization._addAttributePolicy(
    ExternalListOfObjects( "repos", "repo", Repository,
        ListGetable( Parameters( [], [ "type" ] ) ),
        ElementGetable( Parameters( [ "name" ], [] ), { "owner" : lambda user: { "login": user.login } } ),
        ElementCreatable( Parameters( [ "name" ], [ "description", "homepage", "private", "has_issues", "has_wiki", "has_downloads", "team_id", ] ) )
    )
)

def __createForkForOrg( org, repo ):
    assert isinstance( repo, Repository )
    return Repository( org._github, org._github._dataRequest( "POST", repo._baseUrl() + "/forks", { "org": org.login }, None ), lazy = True )

Organization._addAttributePolicy(
    SeveralAttributePolicies( [ MethodFromCallable( "create_fork", Parameters( [ "repo" ], [] ), __createForkForOrg, ObjectTypePolicy( Repository ) ) ], "Forking" )
)

Organization._addAttributePolicy(
    ExternalListOfObjects( "teams", "team", Team,
        ListGetable( Parameters( [], [] ) ),
        ElementCreatable( Parameters( [ "name" ], [ "repo_names", "permission" ] ) )
    )
)

Organization._addAttributePolicy(
    ExternalListOfObjects( "events", "event", Event,
        ListGetable( Parameters( [], [] ) )
    ),
)
