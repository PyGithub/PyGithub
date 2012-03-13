from GithubObject import *

Download = GithubObject(
    "Download",
    BaseUrl( lambda obj: obj._repo._baseUrl() + "/downloads/" + str( obj.id ) ),
    InternalSimpleAttributes(
        "url", "html_url", "id", "name", "description", "size",
        "download_count", "content_type", "policy", "signature", "bucket",
        "accesskeyid", "path", "acl", "expirationdate", "prefix", "mime_type",
        "redirect", "s3_url", "created_at",
        "_repo",
    ),
    Deletable(),
)
