############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

from __future__ import annotations

import argparse
import difflib
import json
import multiprocessing
import sys
from typing import Sequence

import libcst as cst


class SortMethodsTransformer(cst.CSTTransformer):
    def __init__(self, class_name: str | None = None, sort_funcs: bool = False):
        super().__init__()
        self.visit_class_name = []
        self.class_name = class_name
        self.sort_funcs = sort_funcs

    @property
    def current_class_name(self) -> str:
        return ".".join(self.visit_class_name)

    def visit_ClassDef(self, node: cst.ClassDef):
        self.visit_class_name.append(node.name.value)

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef):
        try:
            if self.class_name is not None and self.current_class_name != self.class_name:
                return updated_node
            if not any(
                base.value.value.endswith("GithubObject")
                if isinstance(base.value, cst.Name)
                else (
                    base.value.value.value.endswith("GithubObject")
                    if isinstance(base.value.value, cst.Name)
                    else base.value.value.attr.value.endswith("GithubObject")
                )
                for base in updated_node.bases
            ):
                return updated_node

            statements = list(updated_node.body.body)
            if sum(1 for s in statements if isinstance(s, cst.FunctionDef)) == 0:
                raise ValueError(f"There are no functions in class {self.current_class_name}")
            first = next(idx for idx, s in enumerate(statements) if isinstance(s, cst.FunctionDef))
            last = len(statements) - next(
                idx for idx, s in enumerate(reversed(statements)) if isinstance(s, cst.FunctionDef)
            )
            if any(not isinstance(s, cst.FunctionDef) for s in statements[first:last]):
                raise ValueError(f"There is no consecutive block of functions in class {self.current_class_name}")

            # noinspection PyTypeChecker
            function_defs: list[cst.FunctionDef] = statements[first:last]
            prolog = statements[:first]

            init = self.find_func(function_defs, "__init__")
            init = [init] if init is not None else []

            init_attrs = self.find_func(function_defs, "_initAttributes")
            init_attrs = [init_attrs] if init_attrs is not None else []

            dunders = list(
                s
                for s in function_defs
                if s.name.value.startswith("__") and s.name.value.endswith("__") and s.name.value != "__init__"
            )
            properties = list(s for s in function_defs if self.contains_decorator(s.decorators, "property"))

            use_attrs = self.find_func(function_defs, "_useAttributes")
            use_attrs = [use_attrs] if use_attrs is not None else []

            funcs = list(s for s in function_defs if s not in init + init_attrs + use_attrs + dunders + properties)
            epilog = statements[last:]

            sorted_dunders = self.sort_func_defs(dunders)
            sorted_properties = self.sort_func_defs(properties)
            maybe_sorted_funcs = self.sort_func_defs(funcs) if self.sort_funcs else funcs
            sorted_functions = (
                prolog
                + init
                + init_attrs
                + sorted_dunders
                + sorted_properties
                + maybe_sorted_funcs
                + use_attrs
                + epilog
            )
            return updated_node.with_changes(body=updated_node.body.with_changes(body=sorted_functions))

        finally:
            self.visit_class_name.pop()

    def find_func(self, funcs: Sequence[cst.FunctionDef], func_name: str) -> cst.FunctionDef | None:
        funcs = list(s for s in funcs if s.name.value == func_name)
        if len(funcs) == 0:
            return None
        if len(funcs) > 1:
            raise ValueError(f"Multiple functions {func_name} exist in class {self.current_class_name}")
        return funcs[0]

    @staticmethod
    def contains_decorator(seq: Sequence[cst.Decorator], decorator_name: str):
        return any(d.decorator.value == decorator_name for d in seq if isinstance(d.decorator, cst.Name))

    @staticmethod
    def sort_func_defs(funcs: list[cst.FunctionDef]) -> list[cst.FunctionDef]:
        return sorted(funcs, key=lambda d: d.name.value)

    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef):
        if self.class_name is not None and self.current_class_name != self.class_name:
            return updated_node
        if updated_node.name.value == "_initAttributes":
            attrs = list(
                [
                    idx
                    for idx, stmt in enumerate(updated_node.body.body)
                    if isinstance(stmt, cst.SimpleStatementLine) and isinstance(stmt.body[0], cst.AnnAssign)
                ]
            )
            if attrs:
                start_attr, end_attr = attrs[0], attrs[-1] + 1
                stmts = updated_node.body.body
                attrs = sorted(
                    stmts[start_attr:end_attr],
                    key=lambda stmt: stmt.body[0].target.attr.value
                    if isinstance(stmt.body[0], cst.AnnAssign)
                    else stmt.body[0].targets[0].target.attr.value,
                )
                updated_node = updated_node.with_changes(
                    body=updated_node.body.with_changes(
                        body=tuple(stmts[:start_attr]) + tuple(attrs) + tuple(stmts[end_attr:])
                    )
                )
        if updated_node.name.value == "_useAttributes":
            ifs = list([idx for idx, stmt in enumerate(updated_node.body.body) if isinstance(stmt, cst.If)])
            if ifs:
                start_if, end_if = ifs[0], ifs[-1] + 1
                stmts = updated_node.body.body
                ifs = sorted(
                    stmts[start_if:end_if],
                    key=lambda stmt: stmt.test.left.value
                    if isinstance(stmt.test, cst.Comparison)
                    else stmt.test.children[0].left.value,
                )
                updated_node = updated_node.with_changes(
                    body=updated_node.body.with_changes(
                        body=tuple(stmts[:start_if]) + tuple(ifs) + tuple(stmts[end_if:])
                    )
                )
        return updated_node


def sort_class(class_name: str, filename: str, dry_run: bool, locks: dict[str, multiprocessing.Lock]):
    print(f"Sorting {class_name} ({filename})")

    file_lock = locks.get(filename) if not dry_run else None
    stdout_lock = locks.get("stdout")

    if file_lock:
        file_lock.acquire()
    try:
        with open(filename) as r:
            code = "".join(r.readlines())

        tree = cst.parse_module(code)
        transformer = SortMethodsTransformer(class_name)
        tree_updated = tree.visit(transformer)

        if dry_run:
            diff = "".join(difflib.unified_diff(code.splitlines(1), tree_updated.code.splitlines(1)))
            if diff:
                stdout_lock.acquire()
                print(f"Diff of {class_name}:")
                print(diff)
                print()
                stdout_lock.release()
        else:
            if not tree_updated.deep_equals(tree):
                with open(filename, "w") as w:
                    w.write(tree_updated.code)
    finally:
        if file_lock:
            file_lock.release()


class SortFileWorker:
    def __init__(self, dry_run: bool, locks: dict[str, multiprocessing.Lock]):
        self.dry_run = dry_run
        self.locks = locks

    def sort(self, class_name_and_file: tuple[str, str]):
        class_name, filename = class_name_and_file
        sort_class(class_name, filename, self.dry_run, self.locks)


def main(index_filename: str, class_names: list[str], dry_run: bool):
    if len(class_names) > 1:
        print(f"Sorting {len(class_names)} Python files")

    with open(index_filename) as r:
        index = json.load(r)

    filenames = {}
    for class_name in class_names:
        full_class_name = class_name
        if "." not in class_name:
            cls = index.get("classes", {}).get(class_name)
            if not cls:
                raise ValueError(f"Class {class_name} does not exist in index")
            full_class_name = f'{cls.get("package")}.{cls.get("module")}.{cls.get("name")}'
        package, module, class_name = full_class_name.split(".", maxsplit=2)
        filename = f"{package}/{module}.py"
        filenames[class_name] = filename

    with multiprocessing.Manager() as manager:
        locks = {filename: manager.Lock() for filename in filenames}
        locks.update({"stdout": manager.Lock()})

        # sort files in parallel
        worker = SortFileWorker(dry_run, locks)
        with multiprocessing.Pool() as pool:
            pool.map(worker.sort, iterable=filenames.items())


def parse_args():
    args_parser = argparse.ArgumentParser(
        description="Sorts methods of GithubObject classes, also sorts attributes in _initAttributes and _useAttributes"
    )
    args_parser.add_argument("index_filename", help="Path of index file")
    args_parser.add_argument(
        "class_name",
        nargs="+",
        help="GithubObject class to sort, e.g. HookDelivery or github.HookDelivery.HookDeliverySummary",
    )
    args_parser.add_argument(
        "--dry-run", default=False, action="store_true", help="show prospect changes and do not modify the file"
    )
    if len(sys.argv) == 1:
        args_parser.print_help()
        sys.exit(1)
    return args_parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args.index_filename, args.class_name, args.dry_run)
