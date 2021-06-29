from datetime import datetime
from typing import Any, Dict, Union

from github.Branch import Branch
from github.Commit import Commit
from github.GithubObject import CompletableGithubObject, _NotSetType
from github.NamedUser import NamedUser
from github.PaginatedList import PaginatedList
from github.Tag import Tag
from github.WorkflowRun import WorkflowRun

# PyGithub extension class Artifact


import github.GithubObject
import requests
import re
from pathlib import Path
import logging


_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


class Artifact(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    def get_file_content(self) -> (str, bytes): ...
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def size_in_bytes(self) -> int: ...
    @property
    def url(self) -> str: ...
    @property
    def archive_download_url(self) -> str: ...
    @property
    def expired(self) -> bool: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def expires_at(self) -> datetime: ...
    @property
    def updated_at(self) -> datetime: ...
