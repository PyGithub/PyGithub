from GithubObject import *

def __testHook( hook ):
    hook._github._statusRequest( "POST", hook._baseUrl() + "/test", None, None )
Hook = GithubObject(
    "Hook",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/hooks/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "updated_at", "created_at", "name", "events", "active", "config",
        "id", "last_response",
        "_repo",
    ),
    Editable( Parameters( [ "name", "config" ], [ "events", "add_events", "remove_events", "active" ] ) ),
    Deletable(),
    SeveralAttributePolicies( [ MethodFromCallable( "test", Parameters( [], [] ), __testHook, SimpleTypePolicy( None ) ) ], "Testing" )
)
