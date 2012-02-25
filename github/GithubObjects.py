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

AuthenticatedUser._addAttributePolicy( ExternalListOfObjects( "followers", NamedUser, ListGetable( [], [] ) ) )
NamedUser._addAttributePolicy( ExternalListOfObjects( "followers", NamedUser, ListGetable( [], [] ) ) )

AuthenticatedUser._addAttributePolicy( ExternalListOfObjects( "following", NamedUser, ListGetable( [], [] ), ElementAddable(), ElementRemovable(), ElementHasable() ) )
NamedUser._addAttributePolicy( ExternalListOfObjects( "following", NamedUser, ListGetable( [], [] ) ) )

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
    ExternalListOfObjects( "public_members", NamedUser, ListGetable( [], [] ), ElementAddable(), ElementRemovable(), ElementHasable() ),
    ExternalListOfObjects( "members", NamedUser, ListGetable( [], [] ), ElementRemovable(), ElementHasable() ),
    Editable( [], [ "billing_email", "blog", "company", "email", "location", "name" ] ),
)

AuthenticatedUser._addAttributePolicy( ExternalListOfObjects( "orgs", Organization, ListGetable( [], [] ) ) )
NamedUser._addAttributePolicy( ExternalListOfObjects( "orgs", Organization, ListGetable( [], [] ) ) )

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
    ExternalListOfObjects( "labels", Label, ListGetable( [], [], lambda obj, attributes: dict( itertools.chain( attributes.iteritems(), { "_repo": obj._repo }.iteritems() ) ) ) ),
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
    ExternalListOfObjects( "labels", Label,
        ListGetable( [], [], lambda obj, attributes: dict( itertools.chain( attributes.iteritems(), { "_repo": obj._repo }.iteritems() ) ) ),
        SeveralElementsAddable(),
        ListSetable(),
        ListDeletable(),
        ElementRemovable(),
    ),
    ExternalListOfObjects( "comments", IssueComment,
        ListGetable( [], [], lambda obj, attributes: dict( itertools.chain( attributes.iteritems(), { "_repo": obj._repo }.iteritems() ) ) ),
        ElementGetable( "comment", lambda repo, id: { "_repo": repo, "id": id } ),
        ElementCreatable( "comment", [ "body" ], [], lambda obj, attributes: dict( itertools.chain( attributes.iteritems(), { "_repo": obj._repo }.iteritems() ) ) ),
    ),
)

__modifyAttributesForObjectsReferingRepo = lambda obj, attributes: dict( itertools.chain( attributes.iteritems(), { "_repo": obj }.iteritems() ) )
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
    ExternalListOfObjects( "collaborators", NamedUser, ListGetable( [], [] ), ElementAddable(), ElementRemovable(), ElementHasable() ),
    ExternalListOfObjects( "contributors", NamedUser, ListGetable( [], [] ) ),
    ExternalListOfObjects( "watchers", NamedUser, ListGetable( [], [] ) ),
    Editable( [ "name" ], [ "description", "homepage", "public", "has_issues", "has_wiki", "has_downloads" ] ),
    ExternalListOfObjects( "git/refs", GitRef,
        ListGetable( [], [], __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( "git_ref", lambda repo, ref: { "_repo": repo, "ref": ref } ),
        ElementCreatable( "git_ref", [ "ref", "sha" ], [], __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "git/commits", GitCommit,
        ElementGetable( "git_commit", lambda repo, sha: { "_repo": repo, "sha": sha } ),
        ElementCreatable( "git_commit", [ "message", "tree", "parents" ], [ "author", "commiter" ], __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "git/trees", GitTree,
        ElementGetable( "git_tree", lambda repo, sha: { "_repo": repo, "sha": sha } ),
        ElementCreatable( "git_tree", [ "tree" ], [], __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "git/blobs", GitBlob,
        ElementGetable( "git_blob", lambda repo, sha: { "_repo": repo, "sha": sha } ),
        ElementCreatable( "git_blob", [ "content", "encoding" ], [], __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "git/tags", GitTag,
        ElementGetable( "git_tag", lambda repo, sha: { "_repo": repo, "sha": sha } ),
        ElementCreatable( "git_tag", [ "tag", "message", "object", "type" ], [ "tagger" ], __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "labels", Label,
        ListGetable( [], [], __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( "label", lambda repo, name: { "_repo": repo, "name": name } ),
        ElementCreatable( "label", [ "name", "color" ], [], __modifyAttributesForObjectsReferingRepo ),
    ),
    ExternalListOfObjects( "milestones", Milestone,
        ListGetable( [], [ "state", "sort", "direction" ], __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( "milestone", lambda repo, number: { "_repo": repo, "number": number } ),
        ElementCreatable( "milestone", [ "title" ], [ "state", "description", "due_on" ], __modifyAttributesForObjectsReferingRepo )
    ),
    ExternalListOfObjects( "issues", Issue,
        ListGetable( [], [ "milestone", "state", "assignee", "mentioned", "labels", "sort", "direction", "since" ], __modifyAttributesForObjectsReferingRepo ),
        ElementGetable( "issue", lambda repo, number: { "_repo": repo, "number": number } ),
        ElementCreatable( "issue", [ "title" ], [ "body", "assignee", "milestone", "labels", ], __modifyAttributesForObjectsReferingRepo )
    ),
)
Repository._addAttributePolicy( InternalObjectAttribute( "parent", Repository ) )
Repository._addAttributePolicy( InternalObjectAttribute( "source", Repository ) )
Repository._addAttributePolicy( ExternalListOfObjects( "forks", Repository, ListGetable( [], [] ) ) )

__repoElementCreatable = ElementCreatable( "repo", [ "name" ], [ "description", "homepage", "private", "has_issues", "has_wiki", "has_downloads", "team_id", ] )
__repoElementGetable = ElementGetable( "repo", lambda obj, name: { "owner": { "login": obj.login }, "name": name } )
__repoListGetable = ListGetable( [], [] )
AuthenticatedUser._addAttributePolicy( ExternalListOfObjects( "repos", Repository, __repoListGetable, __repoElementGetable, __repoElementCreatable ) )
NamedUser._addAttributePolicy( ExternalListOfObjects( "repos", Repository, __repoListGetable, __repoElementGetable ) )
Organization._addAttributePolicy( ExternalListOfObjects( "repos", Repository, __repoListGetable, __repoElementGetable, __repoElementCreatable ) )

AuthenticatedUser._addAttributePolicy( ExternalListOfObjects( "watched", Repository, ListGetable( [], [] ), ElementAddable(), ElementRemovable(), ElementHasable() ) )
NamedUser._addAttributePolicy( ExternalListOfObjects( "watched", Repository, ListGetable( [], [] ) ) )

def __createForkForUser( user, repo ):
    assert isinstance( repo, Repository )
    return Repository( user._github, user._github._dataRequest( "POST", repo._baseUrl + "/forks", None, None ), lazy = True )
AuthenticatedUser._addAttributePolicy( MethodFromCallable( "create_fork", __createForkForUser ) )
def __createForkForOrg( org, repo ):
    assert isinstance( repo, Repository )
    return Repository( org._github, org._github._dataRequest( "POST", repo._baseUrl + "/forks", { "org": org.login }, None ), lazy = True )
Organization._addAttributePolicy( MethodFromCallable( "create_fork", __createForkForOrg ) )

Team = GithubObject(
    "Team",
    BaseUrl( lambda obj: "/teams/" + str( obj.id ) ),
    Identity( lambda obj: str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "name", "id", "permission", "members_count", "repos_count",
    ),
    Editable( [ "name" ], [ "permission" ] ),
    Deletable(),
    ExternalListOfObjects( "members", NamedUser, ListGetable( [], [] ), ElementAddable(), ElementRemovable(), ElementHasable() ),
    ExternalListOfObjects( "repos", Repository, ListGetable( [], [] ), ElementAddable(), ElementRemovable(), ElementHasable() ),
)

Organization._addAttributePolicy( ExternalListOfObjects( "teams", Team, ListGetable( [], [] ), ElementCreatable( "team", [ "name" ], [ "repo_names", "permission" ] ) ) )
Repository._addAttributePolicy( ExternalListOfObjects( "teams", Team, ListGetable( [], [] ) ) )
