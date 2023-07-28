from decimal import Decimal

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class CVSS(NonCompletableGithubObject):
    """
    This class represents a CVSS.
    The reference can be found here <https://docs.github.com/en/rest/security-advisories/global-advisories>
    """

    def _initAttributes(self) -> None:
        self._vector_string: Attribute[str] = NotSet
        self._score: Attribute[str] = NotSet

    @property
    def score(self) -> Decimal:
        return Decimal(self._score)

    @property
    def cvss_version(self) -> Decimal:
        return Decimal(self._vector_string.split(":")[0])

    @property
    def vector_string(self) -> str:
        return self._vector_string
