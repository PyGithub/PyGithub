from typing import (
    Dict,
    List,
    Union,
)


class HookDescription:
    def _initAttributes(self) -> None: ...
    def _useAttributes(
        self,
        attributes: Dict[str, Union[str, List[Union[str, int]], List[str], List[List[str]]]]
    ) -> None: ...
    @property
    def events(self) -> List[str]: ...
    @property
    def schema(self) -> List[List[str]]: ...
    @property
    def supported_events(self) -> List[str]: ...
