from NamedUser import *
from Commit import *
from PullRequestFile import *
from PullRequestComment import *

__modifyAttributesForObjectsReferingReferedRepo = { "_repo": lambda obj: obj._repo }

def __pullRequestIsMerged( r ):
    return r._github._statusRequest( "GET", r._baseUrl() + "/merge", None, None ) == 204

def __mergePullRequest( r, **data ):
    r._github._statusRequest( "PUT", r._baseUrl() + "/merge", None, data )

PullRequest = GithubObject(
    "PullRequest",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/pulls/" + str( obj.number ) ),
    InternalSimpleAttributes(
        "id", "url", "html_url", "diff_url", "patch_url", "issue_url", "number",
        "state", "title", "body", "created_at", "updated_at", "closed_at",
        "merged_at", "_links", "merged", "mergeable", "comments", "commits",
        "additions", "deletions", "changed_files", "head", "base", "merged_by",
        "review_comments",
        "_repo",
    ),
    InternalObjectAttribute( "user", NamedUser ),
    Editable( Parameters( [], [ "title", "body", "state" ] ) ),
    ExternalListOfObjects( "commits", "commit", Commit,
        ListGetable( Parameters( [], [] ), __modifyAttributesForObjectsReferingReferedRepo ),
    ),
    ExternalListOfObjects( "files", "file", PullRequestFile,
        ListGetable( Parameters( [], [] ) ),
    ),
    ExternalListOfObjects( "comments", "comment", PullRequestComment,
        ListGetable( Parameters( [], [] ), __modifyAttributesForObjectsReferingReferedRepo ),
        ElementGetable( Parameters( [ "id" ], [] ), __modifyAttributesForObjectsReferingReferedRepo ),
        ElementCreatable( Alternative( Parameters( [ "body", "commit_id", "path", "position" ], [] ), Parameters( [ "body", "in_reply_to" ], [] ) ), __modifyAttributesForObjectsReferingReferedRepo ),
    ),
    MethodFromCallable( "is_merged", Parameters( [], [] ), __pullRequestIsMerged, SimpleTypePolicy( "bool" ) ),
    MethodFromCallable( "merge", Parameters( [], [ "commit_message" ] ), __mergePullRequest, SimpleTypePolicy( None ) ),
)
