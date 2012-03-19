from NamedUser import *
from Label import *

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
    Editable( Parameters( [ "title" ], [ "state", "description", "due_on" ] ) ),
    Deletable(),
    ExternalListOfObjects( "labels", "label", Label,
        ListGetable( Parameters( [], [] ), __modifyAttributesForObjectsReferingReferedRepo )
    ),
)
