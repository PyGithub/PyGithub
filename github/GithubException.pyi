from typing import Any, Dict, List, Optional, Tuple, Type, Union

class BadAttributeException:
    def __init__(
        self,
        actualValue: Any,
        expectedType: Union[
            Dict[Tuple[Type[str], Type[str]], Type[dict]],
            Tuple[Type[str], Type[str]],
            List[Type[dict]],
            List[Tuple[Type[str], Type[str]]],
        ],
        transformationException: Optional[ValueError],
    ) -> None: ...
    @property
    def actual_value(self) -> Any: ...
    @property
    def expected_type(
        self,
    ) -> Union[
        List[Type[dict]],
        Tuple[Type[str], Type[str]],
        Dict[Tuple[Type[str], Type[str]], Type[dict]],
        List[Tuple[Type[str], Type[str]]],
    ]: ...
    @property
    def transformation_exception(self) -> Optional[ValueError]: ...

class GithubException:
    def __init__(self, status: Union[int, str], data: Any,) -> None: ...
    def __str__(self) -> str: ...
    @property
    def data(self) -> Dict[str, Union[str, List[str], List[Dict[str, str]]]]: ...
    @property
    def status(self) -> int: ...
