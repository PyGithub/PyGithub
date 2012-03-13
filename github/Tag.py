from GithubObject import *

from Commit import Commit

Tag = GithubObject(
    "Tag",
    InternalSimpleAttributes(
        "name", "zipball_url", "tarball_url",
        "_repo",
    ),
    InternalObjectAttribute( "commit", Commit )
)
