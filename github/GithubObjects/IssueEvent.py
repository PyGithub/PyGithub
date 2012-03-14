from NamedUser import *

IssueEvent = GithubObject(
    "IssueEvent",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/issues/events/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "id", "url", "created_at", "issue", "event", "commit_id",
        "_repo",
    ),
    InternalObjectAttribute( "actor", NamedUser ),
)
