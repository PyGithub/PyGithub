from GithubObject import *

Event = GithubObject(
    "Event",
    InternalSimpleAttributes(
        "type", "public", "payload", "created_at", "id", "commit_id", "url",
        "event", "issue",
    ),
)
