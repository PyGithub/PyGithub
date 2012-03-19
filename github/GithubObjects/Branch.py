from Commit import *

Branch = GithubObject(
    "Branch",
    InternalSimpleAttributes(
        "name",
        "_repo",
    ),
    InternalObjectAttribute( "commit", Commit )
)
