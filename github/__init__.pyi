from github.MainClass import Github as Github
from github.MainClass import GithubIntegration as GithubIntegration

from .GithubException import BadAttributeException as BadAttributeException
from .GithubException import BadCredentialsException as BadCredentialsException
from .GithubException import BadUserAgentException as BadUserAgentException
from .GithubException import GithubException as GithubException
from .GithubException import IncompletableObject as IncompleteableObject
from .GithubException import RateLimitExceededException as RateLimitExceededException
from .GithubException import TwoFactorException as TwoFactorException
from .GithubException import UnknownObjectException as UnknownObjectException
from .InputFileContent import InputFileContent as InputFileContent
from .InputGitAuthor import InputGitAuthor as InputGitAuthor
from .InputGitTreeElement import InputGitTreeElement as InputGitTreeElement

def enable_console_debug_logging() -> None: ...
