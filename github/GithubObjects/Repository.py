from NamedUser import *
from IssueEvent import *
from RepositoryKey import *
from Hook import *
from GitBlob import *
from GitCommit import *
from GitRef import *
from GitTag import *
from GitTree import *
from Label import *
from Milestone import *
from Issue import *
from Download import *
from CommitComment import *
from Commit import *
from Tag import *
from Branch import *
from PullRequest import *

__modifyAttributesForObjectsReferingRepo = { "_repo": lambda repo: repo }
__modifyAttributesForGitTree = { "_repo": lambda repo: repo, "recursive": lambda repo: False }

def __compare( repo, base, head ):
    return repo._github._dataRequest( "GET", repo._baseUrl() + "/compare/" + base + "..." + head, None, None )

Repository = GithubObject(
    "Repository",
    BaseUrl( lambda obj: "/repos/" + obj.owner.login + "/" + obj.name ),
    Identity( lambda obj: obj.owner.login + "/" + obj.name ),
    InternalSimpleAttributes(
        "url", "html_url", "clone_url", "git_url", "ssh_url", "svn_url",
        "name", "description", "homepage", "language", "private",
        "fork", "forks", "watchers", "size", "master_branch", "open_issues",
        "pushed_at", "created_at", "organization",
        "has_issues", "has_wiki", "has_downloads",
        # Not documented
        "mirror_url", "updated_at", "id", "permissions",
    ),
    InternalObjectAttribute( "owner", NamedUser ),
)
Repository._addAttributePolicy( InternalObjectAttribute( "parent", Repository ) )
Repository._addAttributePolicy( InternalObjectAttribute( "source", Repository ) )
Repository._addAttributePolicy(
    ExternalListOfObjects( "issues/events", "issues_event", IssueEvent,
        ListGetable( Parameters( [], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( Parameters( [ "id" ], [] ), __modifyAttributesForObjectsReferingRepo ),
    )
)
Repository._addAttributePolicy(
    ExternalListOfObjects( "forks", "fork", Repository,
        ListGetable( Parameters( [], [] ) )
    )
)
Repository._addAttributePolicy(
    Editable( Parameters( [ "name" ], [ "description", "homepage", "public", "has_issues", "has_wiki", "has_downloads" ] ) )
)
Repository._addAttributePolicy(
    SeveralAttributePolicies( [ ExternalSimpleAttribute( "languages", "dictionary of strings to integers" ) ], "Languages" )
)
Repository._addAttributePolicy( SeveralAttributePolicies( [
    ExternalListOfObjects( "hooks", "hook", Hook,
        ListGetable( Parameters( [], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( Parameters( [ "id" ], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( Parameters( [ "name", "config" ], [ "events", "active" ] ), __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "keys", "key", RepositoryKey,
        ListGetable( Parameters( [], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( Parameters( [ "id" ], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( Parameters( [ "title", "key" ], [] ), __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "collaborators", "collaborator", NamedUser,
        ListGetable( Parameters( [], [] ) ),
        ElementAddable(),
        ElementRemovable(),
        ElementHasable()
    ),
    ExternalListOfObjects( "contributors", "contributor", NamedUser,
        ListGetable( Parameters( [], [] ) )
    ),
    ExternalListOfObjects( "watchers", "watcher", NamedUser,
        ListGetable( Parameters( [], [] ) )
    ),
    ExternalListOfObjects( "git/refs", "git_ref", GitRef,
        ListGetable( Parameters( [], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( Parameters( [ "ref" ], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( Parameters( [ "ref", "sha" ], [] ), __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "git/commits", "git_commit", GitCommit,
        ElementGetable( Parameters( [ "sha" ], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( Parameters( [ "message", "tree", "parents" ], [ "author", "committer" ] ), __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "git/trees", "git_tree", GitTree,
        ElementGetable( Parameters( [ "sha" ], [ "recursive" ] ), __modifyAttributesForGitTree ),
        ElementCreatable( Parameters( [ "tree" ], [ "base_tree" ] ), __modifyAttributesForGitTree )
    ),
    ExternalListOfObjects( "git/blobs", "git_blob", GitBlob,
        ElementGetable( Parameters( [ "sha" ], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( Parameters( [ "content", "encoding" ], [] ), __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "git/tags", "git_tag", GitTag,
        ElementGetable( Parameters( [ "sha" ], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( Parameters( [ "tag", "message", "object", "type" ], [ "tagger" ] ), __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "labels", "label", Label,
        ListGetable( Parameters( [], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( Parameters( [ "name" ], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( Parameters( [ "name", "color" ], [] ), __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "milestones", "milestone", Milestone,
        ListGetable( Parameters( [], [ "state", "sort", "direction" ] ), __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( Parameters( [ "number" ], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( Parameters( [ "title" ], [ "state", "description", "due_on" ] ), __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "issues", "issue", Issue,
        ListGetable( Parameters( [], [ "milestone", "state", "assignee", "mentioned", "labels", "sort", "direction", "since" ] ), __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( Parameters( [ "number" ], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( Parameters( [ "title" ], [ "body", "assignee", "milestone", "labels", ] ), __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "downloads", "download", Download,
        ListGetable( Parameters( [], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( Parameters( [ "id" ], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( Parameters( [ "name", "size" ], [ "description", "content_type" ] ), __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "comments", "comment", CommitComment,
        ListGetable( Parameters( [], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( Parameters( [ "id" ], [] ), __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "commits", "commit", Commit,
        ListGetable( Parameters( [], [ "sha", "path" ] ), __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( Parameters( [ "sha" ], [] ), __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "tags", "tag", Tag,
        ListGetable( Parameters( [], [] ), __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "branches", "branch", Branch,
        ListGetable( Parameters( [], [] ), __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "pulls", "pull", PullRequest,
        ListGetable( Parameters( [], [ "state" ] ), __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( Parameters( [ "number" ], [] ), __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( Alternative( Parameters( [ "title", "body", "base", "head" ], [] ), Parameters( [ "issue", "base", "head" ], [] ) ), __modifyAttributesForObjectsReferingRepo ),
    ),
    MethodFromCallable( "compare", Parameters( [ "base", "head" ], [] ), __compare, SimpleTypePolicy( None ) ),
] ) )
