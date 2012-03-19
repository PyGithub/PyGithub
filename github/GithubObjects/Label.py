import urllib

from GithubObject import *

Label = GithubObject(
    "Label",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/labels/" + obj._identity ),
    Identity( lambda obj: urllib.quote( obj.name ) ),
    InternalSimpleAttributes(
        "url", "name", "color",
        "_repo",
    ),
    Editable( Parameters( [ "name", "color" ], [] ) ),
    Deletable(),
)
