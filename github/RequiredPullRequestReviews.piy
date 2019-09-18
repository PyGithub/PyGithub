from github.NamedUser import NamedUser
from github.Team import Team
from typing import (
    Dict,
    List,
    Optional,
    Union,
)


class RequiredPullRequestReviews:
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(
        self,
        attributes: Dict[str, Union[str, Dict[str, Union[str, List[Dict[str, Union[int, str, Dict[str, Union[str, int]]]]], List[Dict[str, Union[str, int]]]]], int, Dict[str, Union[str, List[Dict[str, Union[int, str, Dict[str, Union[str, int]]]]]]]]]
    ) -> None: ...
    @property
    def dismiss_stale_reviews(self) -> bool: ...
    @property
    def dismissal_teams(self) -> Optional[List[Team]]: ...
    @property
    def dismissal_users(self) -> Optional[List[NamedUser]]: ...
    @property
    def require_code_owner_reviews(self) -> bool: ...
    @property
    def required_approving_review_count(self) -> int: ...
