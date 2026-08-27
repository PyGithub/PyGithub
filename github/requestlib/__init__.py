from typing import Any

active: str | None = None

netrc_auth_utils: Any

try:
    import niquests
    from niquests import Response, Session, adapters, exceptions, utils
    from niquests import RetryConfiguration as Retry
    from niquests.models import CaseInsensitiveDict, PreparedRequest
    from niquests.packages import urllib3
    from niquests.packages.urllib3.util import Url
    from niquests.utils import get_encoding_from_headers

    requests = niquests
    netrc_auth_utils = niquests.utils.get_netrc_auth

    active = "niquests"
except ModuleNotFoundError:
    try:
        import urllib3
        from requests import Response, Session, adapters, exceptions, utils
        from requests.models import PreparedRequest
        from requests.structures import CaseInsensitiveDict
        from requests.utils import get_encoding_from_headers
        from urllib3 import Retry
        from urllib3.util import Url

        def noop() -> None:
            pass

        netrc_auth_utils = noop
        netrc_auth_utils.cache_clear = noop

        active = "requests"
    except ModuleNotFoundError:
        raise ModuleNotFoundError(
            "Neither requests nor niquests package found, please install one. "
            "Install them together with PyGithub via 'pip install PyGithub[requests]' "
            "or 'pip install PyGithub[niquests]'."
        )


__all__ = [
    "active",
    "adapters",
    "exceptions",
    "utils",
    "Response",
    "Session",
    "PreparedRequest",
    "CaseInsensitiveDict",
    "Retry",
    "Url",
    "urllib3",
    "get_encoding_from_headers",
    "netrc_auth_utils",
]
