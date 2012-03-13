import urllib

from GithubObject import *

from Event import Event
from Hook import Hook
from Authorization import Authorization
from UserKey import UserKey
from AuthenticatedUser import AuthenticatedUser
from NamedUser import NamedUser
from Organization import Organization

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "orgs", "org", Organization,
        ListGetable( [], [] )
    )
)

def __getOrganizationEvents( user, org ):
    return [
        Event( user._github, attributes, lazy = True )
        for attributes
        in user._github._dataRequest( "GET", "/users/" + user.login + "/events/orgs/" + org.login, None, None )
    ]
AuthenticatedUser._addAttributePolicy(
    MethodFromCallable( "get_organization_events", [ "org" ], [], __getOrganizationEvents, SimpleTypePolicy( "list of `Event`" ) )
)

GitRef = GithubObject(
    "GitRef",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/git/" + obj.ref ),
    InternalSimpleAttributes(
        "ref", "url",
        "object",
        "_repo",
    ),
    Editable( [ "sha" ], [ "force" ] ),
)

GitTree = GithubObject(
    "GitTree",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/git/trees/" + obj.sha ),
    InternalSimpleAttributes(
        "sha", "url",
        "tree",
        "_repo",
    ),
)

GitCommit = GithubObject(
    "GitCommit",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/git/commits/" + obj.sha ),
    InternalSimpleAttributes(
        "sha", "url", "message",
        "parents",
        "author", "committer",
        "_repo",
    ),
    InternalObjectAttribute( "tree", GitTree ),
)

GitBlob = GithubObject(
    "GitBlob",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/git/blobs/" + obj.sha ),
    InternalSimpleAttributes(
        "sha", "size", "url",
        "content", "encoding",
        "_repo",
    ),
)

GitTag = GithubObject(
    "GitTag",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/git/tags/" + obj.sha ),
    InternalSimpleAttributes(
        "tag", "sha", "url",
        "message",
        "tagger",
        "object",
        "_repo",
    ),
)

Label = GithubObject(
    "Label",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/labels/" + obj._identity ),
    Identity( lambda obj: urllib.quote( obj.name ) ),
    InternalSimpleAttributes(
        "url", "name", "color",
        "_repo",
    ),
    Editable( [ "name", "color" ], [] ),
    Deletable(),
)

__modifyAttributesForObjectsReferingReferedRepo = { "_repo": lambda obj: obj._repo }

Milestone = GithubObject(
    "Milestone",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/milestones/" + str( obj.number ) ),
    InternalSimpleAttributes(
        "url", "number", "state", "title", "description", "open_issues",
        "closed_issues", "created_at", "due_on",
        "_repo",
    ),
    InternalObjectAttribute( "creator", NamedUser ),
    Editable( [ "title" ], [ "state", "description", "due_on" ] ),
    Deletable(),
    ExternalListOfObjects( "labels", "label", Label,
        ListGetable( [], [], __modifyAttributesForObjectsReferingReferedRepo )
    ),
)

IssueComment = GithubObject(
    "IssueComment",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/issues/comments/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "body", "created_at", "updated_at", "id",
        "_repo",
    ),
    InternalObjectAttribute( "user", NamedUser ),
    Editable( [ "body" ], [] ),
    Deletable(),
)

IssueEvent = GithubObject(
    "IssueEvent",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/issues/events/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "id", "url", "created_at", "issue", "event", "commit_id",
        "_repo",
    ),
    InternalObjectAttribute( "actor", NamedUser ),
)

Issue = GithubObject(
    "Issue",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/issues/" + str( obj.number ) ),
    InternalSimpleAttributes(
        "url", "html_url", "number", "state", "title", "body", "labels",
        "comments", "closed_at", "created_at", "updated_at", "id", "closed_by",
        "pull_request",
        "_repo",
    ),
    InternalObjectAttribute( "user", NamedUser ),
    InternalObjectAttribute( "assignee", NamedUser ),
    InternalObjectAttribute( "milestone", Milestone ),
    Editable( [], [ "title", "body", "assignee", "state", "milestone", "labels" ] ),
    ExternalListOfObjects( "labels", "label", Label,
        ListGetable( [], [], __modifyAttributesForObjectsReferingReferedRepo ),
        SeveralElementsAddable(),
        ListSetable(),
        ListDeletable(),
        ElementRemovable(),
    ),
    ExternalListOfObjects( "comments", "comment", IssueComment,
        ListGetable( [], [], __modifyAttributesForObjectsReferingReferedRepo ),
        ElementGetable( [ "id" ], [], __modifyAttributesForObjectsReferingReferedRepo ),
        ElementCreatable( [ "body" ], [], __modifyAttributesForObjectsReferingReferedRepo ),
    ),
    ExternalListOfObjects( "events", "event", IssueEvent,
        ListGetable( [], [], __modifyAttributesForObjectsReferingReferedRepo )
    ),
)

Download = GithubObject(
    "Download",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/downloads/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "html_url", "id", "name", "description", "size",
        "download_count", "content_type", "policy", "signature", "bucket",
        "accesskeyid", "path", "acl", "expirationdate", "prefix", "mime_type",
        "redirect", "s3_url", "created_at",
        "_repo",
    ),
    Deletable(),
)

CommitComment = GithubObject(
    "CommitComment",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/comments/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "id", "body", "path", "position", "commit_id",
        "created_at", "updated_at", "html_url", "line",
        "_repo",
    ),
    InternalObjectAttribute( "user", NamedUser ),
    Editable( [ "body" ], [] ),
    Deletable(),
)

Commit = GithubObject(
    "Commit",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/commits/" + str( obj.sha ) ),
    InternalSimpleAttributes(
        "sha", "url",
        "parents",
        "stats",
        "files",
        "_repo",
    ),
    InternalObjectAttribute( "commit", GitCommit ),
    InternalObjectAttribute( "author", NamedUser ),
    InternalObjectAttribute( "committer", NamedUser ),
    ExternalListOfObjects( "comments", "comment", CommitComment,
        ListGetable( [], [], __modifyAttributesForObjectsReferingReferedRepo ),
        ElementCreatable( [ "body" ], [ "commit_id", "line", "path", "position" ], __modifyAttributesForObjectsReferingReferedRepo ),
    ),
)

Tag = GithubObject(
    "Tag",
    InternalSimpleAttributes(
        "name", "zipball_url", "tarball_url",
        "_repo",
    ),
    InternalObjectAttribute( "commit", Commit )
)

Branch = GithubObject(
    "Branch",
    InternalSimpleAttributes(
        "name",
        "_repo",
    ),
    InternalObjectAttribute( "commit", Commit )
)

__modifyAttributesForObjectsReferingRepo = { "_repo": lambda repo: repo }
PullRequestFile = GithubObject(
    "PullRequestFile",
    InternalSimpleAttributes(
        "sha", "filename", "status", "additions", "deletions", "changes",
        "blob_url", "raw_url", "patch",
    ),
)

PullRequestComment = GithubObject(
    "PullRequestComment",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/pulls/comments/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "id", "body", "path", "position", "commit_id",
        "created_at", "updated_at", "html_url", "line",
        "_repo",
    ),
    InternalObjectAttribute( "user", NamedUser ),
    Editable( [ "body" ], [] ),
    Deletable(),
)

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

RepositoryKey = GithubObject(
    "RepositoryKey",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/keys/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "id", "title", "key",
        "_repo",
    ),
    Editable( [ "title", "key" ], [] ),
    Deletable()
)

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
        "mirror_url", "updated_at", "id",
    ),
    InternalObjectAttribute( "owner", NamedUser ),
)
Repository._addAttributePolicy( InternalObjectAttribute( "parent", Repository ) )
Repository._addAttributePolicy( InternalObjectAttribute( "source", Repository ) )
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
Repository._addAttributePolicy(
    ExternalListOfObjects( "issues/events", "issues_event", IssueEvent,
        ListGetable( [], [], __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( [ "id" ], [], __modifyAttributesForObjectsReferingRepo ),
    )
)
Repository._addAttributePolicy(
    ExternalListOfObjects( "forks", "fork", Repository,
        ListGetable( [], [] )
    )
)
Repository._addAttributePolicy(
    Editable( [ "name" ], [ "description", "homepage", "public", "has_issues", "has_wiki", "has_downloads" ] )
)
Repository._addAttributePolicy(
    SeveralAttributePolicies( [ ExternalSimpleAttribute( "languages", "dictionary of strings to integers" ) ], "Languages" )
)
Repository._addAttributePolicy( SeveralAttributePolicies( [
    ExternalListOfObjects( "hooks", "hook", Hook,
        ListGetable( [], [], __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( [ "id" ], [], __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( [ "name", "config" ], [ "events", "active" ], __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "keys", "key", RepositoryKey,
        ListGetable( [], [], __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( [ "id" ], [], __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( [ "title", "key" ], [], __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "collaborators", "collaborator", NamedUser,
        ListGetable( [], [] ),
        ElementAddable(),
        ElementRemovable(),
        ElementHasable()
    ),
    ExternalListOfObjects( "contributors", "contributor", NamedUser,
        ListGetable( [], [] )
    ),
    ExternalListOfObjects( "watchers", "watcher", NamedUser,
        ListGetable( [], [] )
    ),
    ExternalListOfObjects( "git/refs", "git_ref", GitRef,
        ListGetable( [], [], __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( [ "ref" ], [], __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( [ "ref", "sha" ], [], __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "git/commits", "git_commit", GitCommit,
        ElementGetable( [ "sha" ], [], __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( [ "message", "tree", "parents" ], [ "author", "committer" ], __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "git/trees", "git_tree", GitTree,
        ElementGetable( [ "sha" ], [], __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( [ "tree" ], [], __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "git/blobs", "git_blob", GitBlob,
        ElementGetable( [ "sha" ], [], __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( [ "content", "encoding" ], [], __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "git/tags", "git_tag", GitTag,
        ElementGetable( [ "sha" ], [], __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( [ "tag", "message", "object", "type" ], [ "tagger" ], __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "labels", "label", Label,
        ListGetable( [], [], __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( [ "name" ], [], __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( [ "name", "color" ], [], __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "milestones", "milestone", Milestone,
        ListGetable( [], [ "state", "sort", "direction" ], __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( [ "number" ], [], __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( [ "title" ], [ "state", "description", "due_on" ], __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "issues", "issue", Issue,
        ListGetable( [], [ "milestone", "state", "assignee", "mentioned", "labels", "sort", "direction", "since" ], __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( [ "number" ], [], __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( [ "title" ], [ "body", "assignee", "milestone", "labels", ], __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "downloads", "download", Download,
        ListGetable( [], [], __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( [ "id" ], [], __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( [ "name", "size" ], [ "description", "content_type" ], __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "comments", "comment", CommitComment,
        ListGetable( [], [], __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( [ "id" ], [], __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "commits", "commit", Commit,
        ListGetable( [], [ "sha", "path" ], __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( [ "sha" ], [], __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "tags", "tag", Tag,
        ListGetable( [], [], __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "branches", "branch", Branch,
        ListGetable( [], [], __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "pulls", "pull", PullRequest,
        ListGetable( [], [ "state" ], __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( [ "number" ], [], __modifyAttributesForObjectsReferingRepo ),
        ElementCreatable( [ "title", "body", "base", "head" ], [], __modifyAttributesForObjectsReferingRepo ),
    ),
] ) )

__repoElementCreatable = ElementCreatable( [ "name" ], [ "description", "homepage", "private", "has_issues", "has_wiki", "has_downloads", "team_id", ] )
__repoElementGetable = ElementGetable( [ "name" ], [], { "owner" : lambda user: { "login": user.login } } )
__repoListGetable = ListGetable( [], [ "type" ] )
AuthenticatedUser._addAttributePolicy(
    ExternalListOfObjects( "repos", "repo", Repository,
        __repoListGetable,
        __repoElementGetable,
        __repoElementCreatable
    )
)
NamedUser._addAttributePolicy(
    ExternalListOfObjects( "repos", "repo", Repository,
        __repoListGetable,
        __repoElementGetable
    )
)
Organization._addAttributePolicy(
    ExternalListOfObjects( "repos", "repo", Repository,
        __repoListGetable,
        __repoElementGetable,
        __repoElementCreatable
    )
)

AuthenticatedUser._addAttributePolicy(
    ExternalListOfObjects( "watched", "watched", Repository,
        ListGetable( [], [] ),
        ElementAddable(),
        ElementRemovable(),
        ElementHasable()
    )
)
NamedUser._addAttributePolicy(
    ExternalListOfObjects( "watched", "watched", Repository,
        ListGetable( [], [] )
    )
)

def __createForkForUser( user, repo ):
    assert isinstance( repo, Repository )
    return Repository( user._github, user._github._dataRequest( "POST", repo._baseUrl() + "/forks", None, None ), lazy = True )
AuthenticatedUser._addAttributePolicy( SeveralAttributePolicies( [ MethodFromCallable( "create_fork", [ "repo" ], [], __createForkForUser, ObjectTypePolicy( Repository ) ) ], "Forking" ) )
def __createForkForOrg( org, repo ):
    assert isinstance( repo, Repository )
    return Repository( org._github, org._github._dataRequest( "POST", repo._baseUrl() + "/forks", { "org": org.login }, None ), lazy = True )
Organization._addAttributePolicy( SeveralAttributePolicies( [ MethodFromCallable( "create_fork", [ "repo" ], [], __createForkForOrg, ObjectTypePolicy( Repository ) ) ], "Forking" ) )

Team = GithubObject(
    "Team",
    BaseUrl( lambda obj: "/teams/" + str( obj.id ) ),
    Identity( lambda obj: str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "name", "id", "permission", "members_count", "repos_count",
    ),
    Editable( [ "name" ], [ "permission" ] ),
    Deletable(),
    ExternalListOfObjects( "members", "member", NamedUser,
        ListGetable( [], [] ),
        ElementAddable(),
        ElementRemovable(),
        ElementHasable()
    ),
    ExternalListOfObjects( "repos", "repo", Repository,
        ListGetable( [], [] ),
        ElementAddable(),
        ElementRemovable(),
        ElementHasable()
    ),
)

Organization._addAttributePolicy(
    ExternalListOfObjects( "teams", "team", Team,
        ListGetable( [], [] ),
        ElementCreatable( [ "name" ], [ "repo_names", "permission" ] )
    )
)
Repository._addAttributePolicy(
    ExternalListOfObjects( "teams", "team", Team,
        ListGetable( [], [] )
    )
)

GistComment = GithubObject(
    "GistComment",
    BaseUrl( lambda obj: "/gists/comments/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "id", "url", "body", "created_at",
        "updated_at",
    ),
    InternalObjectAttribute( "user", NamedUser ),
    Editable( [ "body" ], [] ),
    Deletable(),
)

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

NamedUser._addAttributePolicy(
    ExternalListOfObjects( "gists", "gist", Gist,
        ListGetable( [], [] ),
    )
)

AuthenticatedUser._addAttributePolicy(
    ExternalListOfObjects( "gists", "gist", Gist,
        ListGetable( [], [] ),
        ElementCreatable( [ "public", "files", ], [ "description" ] ),
        url = "/gists",
    )
)
def __getStaredGists( user ):
    return [
        Gist( user._github, attributes, lazy = True )
        for attributes in user._github._dataRequest( "GET", "/gists/starred", None, None )
    ]
AuthenticatedUser._addAttributePolicy(
    MethodFromCallable( "get_starred_gists", [], [], __getStaredGists, SimpleTypePolicy( "list of `Gist`" ) ),
)

Event._addAttributePolicy(
    InternalObjectAttribute( "repo", Repository ),
)
Event._addAttributePolicy(
    InternalObjectAttribute( "actor", NamedUser ),
)
Event._addAttributePolicy(
    InternalObjectAttribute( "org", Organization ),
)
