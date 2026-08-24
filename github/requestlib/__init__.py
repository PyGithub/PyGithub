active = None

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
    import urllib3
    from requests import Response, Session, adapters, exceptions, utils
    from requests.models import PreparedRequest
    from requests.structures import CaseInsensitiveDict
    from requests.utils import get_encoding_from_headers
    from urllib3 import Retry
    from urllib3.util import Url

    class netrc_auth_utils:
        @staticmethod
        def cache_clear():
            pass

    active = "requests"


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
