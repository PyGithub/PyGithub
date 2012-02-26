import itertools
import urllib

from GithubObject import *

AuthenticatedUser = GithubObject(
    "AuthenticatedUser",
    BaseUrl( lambda obj: "/user" ),
    Identity( lambda obj: obj.login ),
    InternalSimpleAttributes(
        "login", "id", "avatar_url", "gravatar_id", "url", "name", "company",
        "blog", "location", "email", "hireable", "bio", "public_repos",
        "public_gists", "followers", "following", "html_url", "created_at",
        "type", "total_private_repos", "owned_private_repos", "private_gists",
        "disk_usage", "collaborators", "plan",
    ),
    Editable( [], [ "name", "email", "blog", "company", "location", "hireable", "bio" ] ),
    ExternalListOfSimpleTypes( "emails", "email", "string",
        ListGetable( [], [] ),
        SeveralElementsAddable(),
        SeveralElementsRemovable()
    ),
)

NamedUser = GithubObject(
    "NamedUser",
    BaseUrl( lambda obj: "/users/" + obj.login ),
    Identity( lambda obj: obj.login ),
    InternalSimpleAttributes(
        "login", "id", "avatar_url", "gravatar_id", "url", "name", "company",
        "blog", "location", "email", "hireable", "bio", "public_repos",
        "public_gists", "followers", "following", "html_url", "created_at",
        "type",
        # Only in Repository.get_contributors()
        "contributions",
        # Seen only by user herself
        "disk_usage", "collaborators", "plan", "total_private_repos",
        "owned_private_repos", "private_gists",
    ),
)

AuthenticatedUser._addAttributePolicy(
    ExternalListOfObjects( "followers", "follower", NamedUser,
        ListGetable( [], [] )
    )
)
NamedUser._addAttributePolicy(
    ExternalListOfObjects( "followers", "follower", NamedUser,
        ListGetable( [], [] )
    )
)

AuthenticatedUser._addAttributePolicy(
    ExternalListOfObjects( "following", "following", NamedUser,
        ListGetable( [], [] ),
        ElementAddable(),
        ElementRemovable(),
        ElementHasable()
    )
)
NamedUser._addAttributePolicy(
    ExternalListOfObjects( "following", "following", NamedUser,
        ListGetable( [], [] )
    )
)

Organization = GithubObject(
    "Organization",
    BaseUrl( lambda obj: "/orgs/" + obj.login ),
    Identity( lambda obj: obj.login ),
    InternalSimpleAttributes(
        "login", "id", "url", "avatar_url", "name", "company", "blog",
        "location", "email", "public_repos", "public_gists", "followers",
        "following", "html_url", "created_at", "type",
        # Seen only by owners
        "disk_usage", "collaborators", "billing_email", "plan", "private_gists",
        "total_private_repos", "owned_private_repos",
    ),
    Editable( [], [ "billing_email", "blog", "company", "email", "location", "name" ] ),
    ExternalListOfObjects( "public_members", "public_member", NamedUser,
        ListGetable( [], [] ),
        ElementAddable(),
        ElementRemovable(),
        ElementHasable()
    ),
    ExternalListOfObjects( "members", "member", NamedUser,
        ListGetable( [], [] ),
        ElementRemovable(),
        ElementHasable()
    ),
)

AuthenticatedUser._addAttributePolicy(
    ExternalListOfObjects( "orgs", "org", Organization,
        ListGetable( [], [] )
    )
)
NamedUser._addAttributePolicy(
    ExternalListOfObjects( "orgs", "org", Organization,
        ListGetable( [], [] )
    )
)

GitRef = GithubObject(
    "GitRef",
    BaseUrl( lambda obj: obj._repo._baseUrl + "/git/" + obj.ref ),
    InternalSimpleAttributes(
        "ref", "url",
        "object", ### @todo Structure
        "_repo", ### Ugly hack
    ),
    Editable( [ "sha" ], [ "force" ] ),
)

GitCommit = GithubObject(
    "GitCommit",
    BaseUrl( lambda obj: obj._repo._baseUrl + "/git/commits/" + obj.sha ),
    InternalSimpleAttributes(
        "sha", "url", "message",
        "author", ### @todo Structure
        "committer", ### @todo Structure
        "tree", ### @todo Structure
        "parents", ### @todo Structure
        "_repo", ### Ugly hack
    ),
)

GitTree = GithubObject(
    "GitTree",
    BaseUrl( lambda obj: obj._repo._baseUrl + "/git/trees/" + obj.sha ),
    InternalSimpleAttributes(
        "sha", "url",
        "tree", ### @todo Structure
        "_repo", ### Ugly hack
    ),
)

GitBlob = GithubObject(
    "GitBlob",
    BaseUrl( lambda obj: obj._repo._baseUrl + "/git/blobs/" + obj.sha ),
    InternalSimpleAttributes(
        "sha", "size", "url",
        "content", "encoding",
        "_repo", ### Ugly hack
    ),
)

GitTag = GithubObject(
    "GitTag",
    BaseUrl( lambda obj: obj._repo._baseUrl + "/git/tags/" + obj.sha ),
    InternalSimpleAttributes(
        "tag", "sha", "url",
        "message",
        "tagger", ### @todo Structure
        "object", ### @todo Structure
        "_repo", ### Ugly hack
    ),
)

Label = GithubObject(
    "Label",
    BaseUrl( lambda obj: obj._repo._baseUrl + "/labels/" + obj._identity ),
    Identity( lambda obj: urllib.quote( obj.name ) ),
    InternalSimpleAttributes(
        "url", "name", "color",
        "_repo", ### Ugly hack
    ),
    Editable( [ "name", "color" ], [] ),
    Deletable(),
)

__modifyAttributesForObjectsReferingReferedRepo = { "_repo": lambda obj: obj._repo }

Milestone = GithubObject(
    "Milestone",
    BaseUrl( lambda obj: obj._repo._baseUrl + "/milestones/" + str( obj.number ) ),
    InternalSimpleAttributes(
        "url", "number", "state", "title", "description", "open_issues",
        "closed_issues", "created_at", "due_on",
        "_repo", ### Ugly hack
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
    BaseUrl( lambda obj: obj._repo._baseUrl + "/issues/comment" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "body", "created_at", "updated_at", "id",
        "_repo", ### Ugly hack
    ),
    InternalObjectAttribute( "user", NamedUser ),
    Editable( [ "body" ], [] ),
    Deletable(),
)

Issue = GithubObject(
    "Issue",
    BaseUrl( lambda obj: obj._repo._baseUrl + "/issues/" + str( obj.number ) ),
    InternalSimpleAttributes(
        "url", "html_url", "number", "state", "title", "body", "labels",
        "comments", "closed_at", "created_at", "updated_at", "id", "closed_by",
        "pull_request", ### @todo Structure
        "_repo", ### Ugly hack
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
)

Download = GithubObject(
    "Download",
    BaseUrl( lambda obj: obj._repo._baseUrl + "/downloads/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "html_url", "id", "name", "description", "size",
        "download_count", "content_type", "policy", "signature", "bucket",
        "accesskeyid", "path", "acl", "expirationdate", "prefix", "mime_type",
        "redirect", "s3_url", "created_at",
        "_repo", ### Ugly hack
    ),
    Deletable(),
)

CommitComment = GithubObject(
    "CommitComment",
    BaseUrl( lambda obj: obj._repo._baseUrl + "/comments/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "id", "body", "path", "position", "commit_id",
        "created_at", "updated_at", "html_url", "line",
        "_repo", ### Ugly hack
    ),
    InternalObjectAttribute( "user", NamedUser ),
    Editable( [ "body" ], [] ),
    Deletable(),
)

Commit = GithubObject(
    "Commit",
    BaseUrl( lambda obj: obj._repo._baseUrl + "/commits/" + str( obj.sha ) ),
    InternalSimpleAttributes(
        "sha", "url",
        "parents", ### @todo Structure
        "stats", ### @todo Structure
        "files", ### @todo Structure
        "_repo", ### Ugly hack
    ),
    InternalObjectAttribute( "commit", GitCommit ),
    InternalObjectAttribute( "author", NamedUser ),
    InternalObjectAttribute( "committer", NamedUser ),
    ExternalListOfObjects( "comments", "comment", CommitComment,
        ListGetable( [], [] ),
        ElementCreatable( [ "body", "commit_id", "line", "path", "position" ], [] ),
    ),
)

Tag = GithubObject(
    "Tag",
    InternalSimpleAttributes(
        "name", "zipball_url", "tarball_url",
        "_repo", ### Ugly hack
    ),
    InternalObjectAttribute( "commit", Commit )
)

Branch = GithubObject(
    "Branch",
    InternalSimpleAttributes(
        "name",
        "_repo", ### Ugly hack
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
    BaseUrl( lambda obj: obj._repo._baseUrl + "/pulls/comments/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "id", "body", "path", "position", "commit_id",
        "created_at", "updated_at", "html_url", "line",
        "_repo", ### Ugly hack
    ),
    InternalObjectAttribute( "user", NamedUser ),
    Editable( [ "body" ], [] ),
    Deletable(),
)

PullRequest = GithubObject(
    "PullRequest",
    BaseUrl( lambda obj: obj._repo._baseUrl + "/pulls/" + str( obj.number ) ),
    InternalSimpleAttributes(
        "id", "url", "html_url", "diff_url", "patch_url", "issue_url", "number",
        "state", "title", "body", "created_at", "updated_at", "closed_at",
        "merged_at", "_links", "merged", "mergeable", "comments", "commits",
        "additions", "deletions", "changed_files", "head", "base", "merged_by",
        "review_comments",
        "_repo", ### Ugly hack
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
        ElementCreatable( [ "message", "tree", "parents" ], [ "author", "commiter" ], __modifyAttributesForObjectsReferingRepo )
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
        ElementGetable( [ "id" ], [], __modifyAttributesForObjectsReferingRepo ),
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
    return Repository( user._github, user._github._dataRequest( "POST", repo._baseUrl + "/forks", None, None ), lazy = True )
AuthenticatedUser._addAttributePolicy( SeveralAttributePolicies( [ MethodFromCallable( "create_fork", [ "repo" ], [], __createForkForUser, ObjectTypePolicy( Repository ) ) ], "Forking" ) )
def __createForkForOrg( org, repo ):
    assert isinstance( repo, Repository )
    return Repository( org._github, org._github._dataRequest( "POST", repo._baseUrl + "/forks", { "org": org.login }, None ), lazy = True )
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
