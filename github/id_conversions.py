"""This module contains the functions allowing you to convert IDs of GitHub REST and GraphQL APIs to each other without wasting queries to GitHub API"""

__all__ = ("db_id_and_type_to_node_id", "node_id_to_db_id_and_type")

__license__ = "Unlicense"

import typing
from base64 import b64decode, b64encode


def _db_id_and_type_to_node_id(db_id: int, type_name: str) -> str:
    return "0" + str(len(type_name)) + ":" + type_name + str(db_id)


def db_id_and_type_to_node_id(db_id: int, type_name: str) -> str:
    """Converts GitHub DB ID of an object into its GraphQL ID."""
    return b64encode(
        _db_id_and_type_to_node_id(db_id, type_name).encode("ascii")
    ).decode("ascii")


def _node_id_to_db_id_and_type(node_id: str) -> typing.Tuple[int, str]:
    type_len_str, rest = node_id.split(":")
    if not type_len_str or type_len_str[0] != "0":
        raise ValueError("Node ID must start from 0")

    type_len: int = int(type_len_str[1:])
    del type_len_str
    if type_len <= 0:
        raise ValueError("Type length must be natural")

    return int(rest[type_len:]), rest[:type_len]


def node_id_to_db_id_and_type(node_id: str) -> typing.Tuple[int, str]:
    """Converts GitHub GraphQL ID of an object into its DB ID."""
    return _node_id_to_db_id_and_type(b64decode(node_id).decode("ascii"))
