from GithubObject import *

from Commit import Commit

Branch = GithubObject(
    "Branch",
    InternalSimpleAttributes(
        "name",
        "_repo",
    ),
    InternalObjectAttribute( "commit", Commit )
)
