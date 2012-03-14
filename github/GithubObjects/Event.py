from GithubObject import *

from Repository import Repository
from NamedUser import NamedUser
from Organization import Organization

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