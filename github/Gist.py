from GithubObject import *

from NamedUser import NamedUser
from GistComment import GistComment

def __isStarred( gist ):
    return gist._github._statusRequest( "GET", gist._baseUrl() + "/star", None, None ) == 204
def __setStarred( gist ):
    gist._github._statusRequest( "PUT", gist._baseUrl() + "/star", None, None )
def __resetStarred( gist ):
    gist._github._statusRequest( "DELETE", gist._baseUrl() + "/star", None, None )
Gist = GithubObject(
    "Gist",
    BaseUrl( lambda obj: "/gists/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "id", "description", "public", "files", "comments", "html_url",
        "git_pull_url", "git_push_url", "created_at", "forks", "history",
        "updated_at",
    ),
    InternalObjectAttribute( "user", NamedUser ),
    Editable( [], [ "description", "files" ] ),
    Deletable(),
    ExternalListOfObjects( "comments", "comment", GistComment,
        ListGetable( [], [] ),
        ElementGetable( [ "id" ], [] ),
        ElementCreatable( [ "body" ], [] ),
    ),
    SeveralAttributePolicies( [
        MethodFromCallable( "is_starred", [], [], __isStarred, SimpleTypePolicy( "bool" ) ),
        MethodFromCallable( "set_starred", [], [], __setStarred, SimpleTypePolicy( None ) ),
        MethodFromCallable( "reset_starred", [], [], __resetStarred, SimpleTypePolicy( None ) ),
    ], "Starring" ),
)
def __createFork( gist ):
    return Gist( gist._github, gist._github._dataRequest( "POST", gist._baseUrl() + "/fork", None, None ), lazy = True )
Gist._addAttributePolicy(    SeveralAttributePolicies( [
        MethodFromCallable( "create_fork", [], [], __createFork, ObjectTypePolicy( Gist ) ),
    ], "Forking" ),
)
