from GithubObject import *

PullRequestFile = GithubObject(
    "PullRequestFile",
    InternalSimpleAttributes(
        "sha", "filename", "status", "additions", "deletions", "changes",
        "blob_url", "raw_url", "patch",
    ),
)
