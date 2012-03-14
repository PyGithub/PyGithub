from GithubObject import *

from NamedUser import NamedUser
from Milestone import Milestone
from Label import Label
from IssueComment import IssueComment
from IssueEvent import IssueEvent

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
