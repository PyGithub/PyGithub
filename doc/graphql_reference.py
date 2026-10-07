# SPDX-License-Identifier: LGPL-3.0-or-later

from __future__ import annotations

import ast
import re
from collections import defaultdict
from pathlib import Path

GRAPHQL_CALL = re.compile(r"^:calls:\s+`GraphQL (query|mutation) ([\w.]+)\s+<([^>]+)>`__?", re.MULTILINE)


def collect_graphql_calls(source: str, module: str) -> dict[tuple[str, str, str], set[str]]:
    """
    Map documented GraphQL operations to their public Python methods.
    """
    calls: dict[tuple[str, str, str], set[str]] = defaultdict(set)
    for node in ast.parse(source).body:
        if not isinstance(node, ast.ClassDef):
            continue
        for method in node.body:
            if not isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)) or method.name.startswith("_"):
                continue
            for kind, name, url in GRAPHQL_CALL.findall(ast.get_docstring(method) or ""):
                calls[kind, name, url].add(f"{module}.{node.name}.{method.name}")
    return dict(calls)


def generate_graphql_reference(source_dir: Path) -> str:
    """
    Generate the GraphQL reference from :calls: annotations, without importing library code.
    """
    calls: dict[tuple[str, str, str], set[str]] = defaultdict(set)
    for source_path in sorted(source_dir.glob("*.py")):
        for operation, methods in collect_graphql_calls(
            source_path.read_text(encoding="utf-8"), f"github.{source_path.stem}"
        ).items():
            calls[operation].update(methods)

    lines = [
        "GraphQL API",
        "===========",
        "",
        "These GraphQL queries and mutations have dedicated PyGithub methods. On",
        "GitHub.com, they use ``POST /graphql``. The names below identify the GraphQL",
        "fields they access.",
        "Query methods may accept a selection set to choose the fields to return.",
        "See :doc:`graphql` for using custom queries and mutations.",
        "",
    ]
    for kind, title in [("query", "Queries"), ("mutation", "Mutations")]:
        lines.extend([title, "-" * len(title), ""])
        for (operation_kind, name, url), methods in sorted(calls.items()):
            if operation_kind == kind:
                lines.extend(
                    [
                        f"* `{name} <{url}>`__",
                        "",
                        "  " + " or ".join(f":meth:`{method}`" for method in sorted(methods)),
                        "",
                    ]
                )
    return "\n".join(lines)
