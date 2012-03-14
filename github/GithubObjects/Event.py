from Repository import *
from NamedUser import *
from Organization import *

Event = GithubObject(
    "Event",
    InternalSimpleAttributes(
        "type", "public", "payload", "created_at", "id", "commit_id", "url",
        "event", "issue",
    ),
    InternalObjectAttribute( "repo", Repository ),
    InternalObjectAttribute( "actor", NamedUser ),
    InternalObjectAttribute( "org", Organization ),
)