from NamedUser import *
from Milestone import *
from Label import *
from IssueComment import *
from IssueEvent import *

__modifyAttributesForObjectsReferingReferedRepo = { "_repo": lambda obj: obj._repo }

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
    Editable( Parameters( [], [ "title", "body", "assignee", "state", "milestone", "labels" ] ) ),
    ExternalListOfObjects( "labels", "label", Label,
        ListGetable( Parameters( [], [] ), __modifyAttributesForObjectsReferingReferedRepo ),
        SeveralElementsAddable(),
        ListSetable(),
        ListDeletable(),
        ElementRemovable(),
    ),
    ExternalListOfObjects( "comments", "comment", IssueComment,
        ListGetable( Parameters( [], [] ), __modifyAttributesForObjectsReferingReferedRepo ),
        ElementGetable( Parameters( [ "id" ], [] ), __modifyAttributesForObjectsReferingReferedRepo ),
        ElementCreatable( Parameters( [ "body" ], [] ), __modifyAttributesForObjectsReferingReferedRepo ),
    ),
    ExternalListOfObjects( "events", "event", IssueEvent,
        ListGetable( Parameters( [], [] ), __modifyAttributesForObjectsReferingReferedRepo )
    ),
)
