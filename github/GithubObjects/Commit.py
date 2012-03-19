from GitCommit import *
from NamedUser import *
from CommitComment import *

__modifyAttributesForObjectsReferingReferedRepo = { "_repo": lambda obj: obj._repo }

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
        ListGetable( Parameters( [], [] ), __modifyAttributesForObjectsReferingReferedRepo ),
        ElementCreatable( Parameters( [ "body" ], [ "commit_id", "line", "path", "position" ] ), __modifyAttributesForObjectsReferingReferedRepo ),
    ),
)
