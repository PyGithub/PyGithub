from GithubObject import *

Authorization = GithubObject(
    "Authorization",
    BaseUrl( lambda obj: "/authorizations/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "id", "url", "scopes", "token", "app", "note", "note_url", "updated_at",
        "created_at",
    ),
    Editable( Parameters( [], [ "scopes", "add_scopes", "remove_scopes", "note", "note_url" ] ) ),
    Deletable(),
)
