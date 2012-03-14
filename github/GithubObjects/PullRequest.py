from GithubObject import *

from NamedUser import NamedUser
from Commit import Commit
from PullRequestFile import PullRequestFile
from PullRequestComment import PullRequestComment

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
    Editable( [], [ "title", "body", "state" ] ),
    ExternalListOfObjects( "commits", "commit", Commit,
        ListGetable( [], [], __modifyAttributesForObjectsReferingReferedRepo ),
    ),
    ExternalListOfObjects( "files", "file", PullRequestFile,
        ListGetable( [], [] ),
    ),
    ExternalListOfObjects( "comments", "comment", PullRequestComment,
        ListGetable( [], [], __modifyAttributesForObjectsReferingReferedRepo ),
        ElementGetable( [ "id" ], [], __modifyAttributesForObjectsReferingReferedRepo ),
        ElementCreatable( [ "body", "commit_id", "path", "position" ], [], __modifyAttributesForObjectsReferingReferedRepo ),
    ),
    MethodFromCallable( "is_merged", [], [], __pullRequestIsMerged, SimpleTypePolicy( "bool" ) ),
    MethodFromCallable( "merge", [], [ "commit_message" ], __mergePullRequest, SimpleTypePolicy( None ) ),
)
