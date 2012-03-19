from GithubObject import *

UserKey = GithubObject(
    "UserKey",
    BaseUrl( lambda obj: "/user/keys/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "id", "title", "key",
    ),
    Editable( Parameters( [], [ "title", "key" ] ) ),
    Deletable(),
)
