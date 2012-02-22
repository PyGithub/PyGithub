import itertools

from GithubObject import *

AuthenticatedUser = GithubObject(
    "AuthenticatedUser",
    BaseUrl( lambda obj: "/user" ),
    Identity( lambda obj: obj.login ),
    BasicAttributes(
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
    BasicAttributes(
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

AuthenticatedUser._addAttributePolicy( ListAttribute( "followers", NamedUser, ListGetable( [], [] ) ) )
NamedUser._addAttributePolicy( ListAttribute( "followers", NamedUser, ListGetable( [], [] ) ) )

AuthenticatedUser._addAttributePolicy( ListAttribute( "following", NamedUser, ListGetable( [], [] ), ElementAddable(), ElementRemovable(), ElementHasable() ) )
NamedUser._addAttributePolicy( ListAttribute( "following", NamedUser, ListGetable( [], [] ) ) )

Organization = GithubObject(
    "Organization",
    BaseUrl( lambda obj: "/orgs/" + obj.login ),
    Identity( lambda obj: obj.login ),
    BasicAttributes(
        "login", "id", "url", "avatar_url", "name", "company", "blog",
        "location", "email", "public_repos", "public_gists", "followers",
        "following", "html_url", "created_at", "type",
        # Seen only by owners
        "disk_usage", "collaborators", "billing_email", "plan", "private_gists",
        "total_private_repos", "owned_private_repos",
    ),
    ListAttribute( "public_members", NamedUser, ListGetable( [], [] ), ElementAddable(), ElementRemovable(), ElementHasable() ),
    ListAttribute( "members", NamedUser, ListGetable( [], [] ), ElementRemovable(), ElementHasable() ),
    Editable( [], [ "billing_email", "blog", "company", "email", "location", "name" ] ),
)

AuthenticatedUser._addAttributePolicy( ListAttribute( "orgs", Organization, ListGetable( [], [] ) ) )
NamedUser._addAttributePolicy( ListAttribute( "orgs", Organization, ListGetable( [], [] ) ) )

GitRef = GithubObject(
    "GitRef",
    BaseUrl( lambda obj: obj._repo._baseUrl + "/git/" + obj.ref ),
    BasicAttributes(
        "ref", "url",
        "object", ### @todo Structure
        "_repo", ### Ugly hack
    ),
    Editable( [ "sha" ], [ "force" ] ),
)

GitCommit = GithubObject(
    "GitCommit",
    BaseUrl( lambda obj: obj._repo._baseUrl + "/git/commits/" + obj.sha ),
    BasicAttributes(
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
    BasicAttributes(
        "sha", "url",
        "tree", ### @todo Structure
        "_repo", ### Ugly hack
    ),
)

GitBlob = GithubObject(
    "GitBlob",
    BaseUrl( lambda obj: obj._repo._baseUrl + "/git/blobs/" + obj.sha ),
    BasicAttributes(
        "sha", "size", "url",
        "content", "encoding",
        "_repo", ### Ugly hack
    ),
)

GitTag = GithubObject(
    "GitTag",
    BaseUrl( lambda obj: obj._repo._baseUrl + "/git/tags/" + obj.sha ),
    BasicAttributes(
        "tag", "sha", "url",
        "message",
        "tagger", ### @todo Structure
        "object", ### @todo Structure
        "_repo", ### Ugly hack
    ),
)

__modifyAttributesForGitObjects = lambda obj, attributes: dict( itertools.chain( attributes.iteritems(), { "_repo": obj }.iteritems() ) )
Repository = GithubObject(
    "Repository",
    BaseUrl( lambda obj: "/repos/" + obj.owner.login + "/" + obj.name ),
    Identity( lambda obj: obj.owner.login + "/" + obj.name ),
    BasicAttributes(
        "url", "html_url", "clone_url", "git_url", "ssh_url", "svn_url",
        "name", "description", "homepage", "language", "private",
        "fork", "forks", "watchers", "size", "master_branch", "open_issues",
        "pushed_at", "created_at", "organization",
        "has_issues", "has_wiki", "has_downloads",
        # Not documented
        "mirror_url", "updated_at", "id",
    ),
    ComplexAttribute( "owner", NamedUser ),
    ListAttribute( "collaborators", NamedUser, ListGetable( [], [] ), ElementAddable(), ElementRemovable(), ElementHasable() ),
    ListAttribute( "contributors", NamedUser, ListGetable( [], [] ) ),
    ListAttribute( "watchers", NamedUser, ListGetable( [], [] ) ),
    Editable( [ "name" ], [ "description", "homepage", "public", "has_issues", "has_wiki", "has_downloads" ] ),
    ListAttribute( "git/refs", GitRef,
        ListGetable( [], [], __modifyAttributesForGitObjects ),
        ElementGetable( "git_ref", lambda repo, ref: { "_repo": repo, "ref": ref } ),
        ElementCreatable( "git_ref", [ "ref", "sha" ], [], __modifyAttributesForGitObjects )
    ),
    ListAttribute( "git/commits", GitCommit,
        ElementGetable( "git_commit", lambda repo, sha: { "_repo": repo, "sha": sha } ),
        ElementCreatable( "git_commit", [ "message", "tree", "parents" ], [ "author", "commiter" ], __modifyAttributesForGitObjects )
    ),
    ListAttribute( "git/trees", GitTree,
        ElementGetable( "git_tree", lambda repo, sha: { "_repo": repo, "sha": sha } ),
        ElementCreatable( "git_tree", [ "tree" ], [], __modifyAttributesForGitObjects )
    ),
    ListAttribute( "git/blobs", GitBlob,
        ElementGetable( "git_blob", lambda repo, sha: { "_repo": repo, "sha": sha } ),
        ElementCreatable( "git_blob", [ "content", "encoding" ], [], __modifyAttributesForGitObjects )
    ),
    ListAttribute( "git/tags", GitTag,
        ElementGetable( "git_tag", lambda repo, sha: { "_repo": repo, "sha": sha } ),
        ElementCreatable( "git_tag", [ "tag", "message", "object", "type" ], [ "tagger" ], __modifyAttributesForGitObjects )
    ),
)
Repository._addAttributePolicy( ComplexAttribute( "parent", Repository ) )
Repository._addAttributePolicy( ComplexAttribute( "source", Repository ) )
Repository._addAttributePolicy( ListAttribute( "forks", Repository, ListGetable( [], [] ) ) )

__repoElementCreatable = ElementCreatable( "repo", [ "name" ], [ "description", "homepage", "private", "has_issues", "has_wiki", "has_downloads", "team_id", ] )
__repoElementGetable = ElementGetable( "repo", lambda obj, name: { "owner": { "login": obj.login }, "name": name } )
__repoListGetable = ListGetable( [], [] )
AuthenticatedUser._addAttributePolicy( ListAttribute( "repos", Repository, __repoListGetable, __repoElementGetable, __repoElementCreatable ) )
NamedUser._addAttributePolicy( ListAttribute( "repos", Repository, __repoListGetable, __repoElementGetable ) )
Organization._addAttributePolicy( ListAttribute( "repos", Repository, __repoListGetable, __repoElementGetable, __repoElementCreatable ) )

AuthenticatedUser._addAttributePolicy( ListAttribute( "watched", Repository, ListGetable( [], [] ), ElementAddable(), ElementRemovable(), ElementHasable() ) )
NamedUser._addAttributePolicy( ListAttribute( "watched", Repository, ListGetable( [], [] ) ) )

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
    BasicAttributes(
        "url", "name", "id", "permission", "members_count", "repos_count",
    ),
    Editable( [ "name" ], [ "permission" ] ),
    Deletable(),
    ListAttribute( "members", NamedUser, ListGetable( [], [] ), ElementAddable(), ElementRemovable(), ElementHasable() ),
    ListAttribute( "repos", Repository, ListGetable( [], [] ), ElementAddable(), ElementRemovable(), ElementHasable() ),
)

Organization._addAttributePolicy( ListAttribute( "teams", Team, ListGetable( [], [] ), ElementCreatable( "team", [ "name" ], [ "repo_names", "permission" ] ) ) )
Repository._addAttributePolicy( ListAttribute( "teams", Team, ListGetable( [], [] ) ) )
