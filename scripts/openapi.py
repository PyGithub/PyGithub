############################ Copyrights and license ############################
#                                                                              #
# Copyright                                                                    #
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

import abc
import argparse
import dataclasses
import difflib
import json
import os.path
import sys
from collections import Counter
from json import JSONEncoder
from os import listdir
from os.path import isfile, join
from tempfile import NamedTemporaryFile
from typing import Any, Sequence

import libcst as cst
import requests
from libcst import Expr, IndentedBlock, Module, SimpleStatementLine, SimpleString


@dataclasses.dataclass(frozen=True)
class PythonType:
    type: str
    inner_types: list[PythonType | GithubClass] | None = None

    def __repr__(self):
        return (
            f"{self.type}[{', '.join([str(inner) for inner in self.inner_types])}]" if self.inner_types else self.type
        )


@dataclasses.dataclass(frozen=True)
class GithubClass:
    ids: list[str]
    package: str
    module: str
    name: str
    filename: str
    bases: list[str]
    inheritance: list[str]
    methods: dict
    properties: dict
    schemas: list[str]
    docstring: str

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return ".".join([self.package, self.module, self.name])

    @property
    def short_class_name(self) -> str:
        return self.name.split(".")[-1]

    @property
    def full_class_name(self) -> str:
        return f"{self.package}.{self.module}.{self.name}"

    @property
    def test_filename(self) -> str:
        return f"tests/{self.module}.py"

    @staticmethod
    def from_class_name(class_name: str, index: dict[str, Any] | None = None) -> GithubClass:
        if "." in class_name:
            full_class_name = class_name
            package, module, class_name = full_class_name.split(".", 2)
            if index is not None:
                clazz = GithubClass.from_class_name(class_name, index)
                if clazz.package != package or clazz.module != module or clazz.name != class_name:
                    raise ValueError(f"Class mismatch: {full_class_name} vs {clazz}")
                return clazz
            else:
                return GithubClass(
                    ids=[],
                    package="github",
                    module=class_name,
                    name=class_name,
                    filename=f"{package}/{module}.py",
                    bases=[],
                    inheritance=[],
                    methods={},
                    properties={},
                    schemas=[],
                    docstring="",
                )
        else:
            if index is not None:
                classes = index.get("classes", {})
                if class_name not in classes:
                    raise ValueError(f"Unknown class {class_name}")
                cls = classes.get(class_name)
                if any(key not in cls for key in ["package", "module", "name"]):
                    raise KeyError(f"Missing package, module or name in {cls}")
                return GithubClass(**cls)
            else:
                return GithubClass.from_class_name(f"github.{class_name}.{class_name}")


@dataclasses.dataclass(frozen=True)
class Property:
    name: str
    data_type: PythonType | GithubClass | None
    deprecated: bool


class SimpleStringCollector(cst.CSTVisitor):
    def __init__(self):
        super().__init__()
        self._strings = []

    @property
    def strings(self):
        return self._strings

    def visit_SimpleString(self, node: cst.SimpleString) -> bool | None:
        self._strings.append(node.evaluated_value)


def get_class_docstring(node: cst.ClassDef) -> str | None:
    try:
        if (
            isinstance(node.body, IndentedBlock)
            and isinstance(node.body.body[0], SimpleStatementLine)
            and isinstance(node.body.body[0].body[0], Expr)
            and isinstance(node.body.body[0].body[0].value, SimpleString)
        ):
            return node.body.body[0].body[0].value.value
    except Exception as e:
        print(f"Extracting docstring of class {node.name.value} failed", e)


class CstMethods(abc.ABC):
    @staticmethod
    def contains_decorator(seq: Sequence[cst.Decorator], decorator_name: str):
        return any(d.decorator.value == decorator_name for d in seq if isinstance(d.decorator, cst.Name))

    @classmethod
    def is_github_object_property(cls, func_def: cst.FunctionDef):
        return cls.contains_decorator(func_def.decorators, "property")

    @classmethod
    def create_subscript(cls, name: str) -> cst.Subscript:
        fields = name.rstrip("]").split("[", maxsplit=1)
        name = fields[0]
        index = fields[1]
        sub = cst.Subscript(cst.Name(name), [cst.SubscriptElement(cst.Index(cst.Integer(index)))])
        return sub

    @classmethod
    def create_attribute(cls, names: list[str]) -> cst.BaseExpression:
        names = [cls.create_subscript(name) if "[" in name and name.endswith("]") else cst.Name(name) for name in names]
        if len(names) == 1:
            return names[0]
        attr = cst.Attribute(names[0], names[1])
        for name in names[2:]:
            attr = cst.Attribute(attr, name)
        return attr

    @classmethod
    def find_nodes(cls, node: cst.CSTNode, node_type: type[cst.CSTNode]) -> list[cst.CSTNode]:
        if isinstance(node, node_type):
            return [node]
        return [node for child in node.children for node in cls.find_nodes(child, node_type)]

    @staticmethod
    def parse_attribute(attr: cst.Attribute) -> list[str]:
        attrs = []
        while (
            isinstance(attr, cst.Attribute) or isinstance(attr, cst.Subscript) and isinstance(attr.value, cst.Attribute)
        ):
            if isinstance(attr, cst.Attribute):
                attrs.insert(0, attr.attr.value)
            elif isinstance(attr, cst.Subscript):
                # we do not extract a name, we skip to the subscript value
                pass
            attr = attr.value
        attrs.insert(0, attr.value)
        return attrs


class CstVisitorBase(cst.CSTVisitor, CstMethods, abc.ABC):
    def __init__(self):
        super().__init__()
        self.visit_class_name = []

    def visit_ClassDef(self, node: cst.ClassDef):
        self.visit_class_name.append(node.name.value)

    def leave_ClassDef(self, original_node: cst.ClassDef) -> None:
        self.visit_class_name.pop()

    @property
    def current_class_name(self) -> str:
        return ".".join(self.visit_class_name)


class CstTransformerBase(cst.CSTTransformer, CstMethods, abc.ABC):
    def __init__(self):
        super().__init__()
        self.visit_class_name = []

    def visit_ClassDef(self, node: cst.ClassDef):
        self.visit_class_name.append(node.name.value)

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef):
        self.visit_class_name.pop()
        return super().leave_ClassDef(original_node, updated_node)

    @property
    def current_class_name(self) -> str:
        return ".".join(self.visit_class_name)

    @staticmethod
    def is_github_import(stmt: cst.Import | cst.ImportFrom) -> bool:
        return (
            isinstance(stmt, cst.Import)
            and (
                isinstance(stmt.names[0].name, cst.Name)
                and stmt.names[0].name.value == "github"
                or isinstance(stmt.names[0].name, cst.Attribute)
                and stmt.names[0].name.value.value == "github"
            )
            or isinstance(stmt, cst.ImportFrom)
            and isinstance(stmt.module, cst.Attribute)
            and stmt.module.value.value == "github"
        )

    @staticmethod
    def is_datetime_import(stmt: cst.Import | cst.ImportFrom) -> bool:
        return (
            isinstance(stmt, cst.ImportFrom)
            and isinstance(stmt.module, cst.Name)
            and stmt.module.value == "datetime"
            and stmt.names
            and isinstance(stmt.names[0], cst.ImportAlias)
            and isinstance(stmt.names[0].name, cst.Name)
            and stmt.names[0].name.value == "datetime"
        )

    @staticmethod
    def add_datetime_import(node: cst.Module, index: int) -> cst.Module:
        import_stmt = cst.SimpleStatementLine(
            [
                cst.ImportFrom(
                    cst.Name("datetime"), [cst.ImportAlias(cst.Name("datetime")), cst.ImportAlias(cst.Name("timezone"))]
                )
            ]
        )
        stmts = list(node.body)
        return node.with_changes(body=stmts[:index] + [import_stmt] + stmts[index:])

    @staticmethod
    def add_future_import(node: cst.Module) -> cst.Module:
        stmts = list(node.body)
        first_stmt = stmts[0] if stmts else None
        if not (
            first_stmt
            and isinstance(first_stmt, cst.SimpleStatementLine)
            and isinstance(first_stmt.body[0], cst.ImportFrom)
            and isinstance(first_stmt.body[0].module, cst.Name)
            and first_stmt.body[0].module.value == "__future__"
            and first_stmt.body[0].names
            and isinstance(first_stmt.body[0].names[0], cst.ImportAlias)
            and isinstance(first_stmt.body[0].names[0].name, cst.Name)
            and first_stmt.body[0].names[0].name.value == "annotations"
        ):
            import_stmt = cst.SimpleStatementLine(
                [cst.ImportFrom(cst.Name("__future__"), [cst.ImportAlias(cst.Name("annotations"))])]
            )
            if (
                isinstance(first_stmt, cst.SimpleStatementLine)
                and isinstance(first_stmt.body[0], (cst.Import, cst.ImportFrom))
                and not first_stmt.leading_lines
            ):
                first_stmt = first_stmt.with_changes(leading_lines=[cst.EmptyLine()])
                stmts = [first_stmt] + stmts[1:]

            node = node.with_changes(body=[import_stmt] + stmts)

        return node


class IndexPythonClassesVisitor(CstVisitorBase):
    def __init__(self, classes: dict[str, Any] | None = None):
        super().__init__()
        self._module = None
        self._package = None
        self._filename = None
        self._classes = classes if classes is not None else {}
        self._ids = []
        self._properties = {}
        self._methods = {}

    def module(self, module: str):
        self._module = module

    def package(self, package: str):
        self._package = package

    def filename(self, filename: str):
        self._filename = filename

    @property
    def classes(self) -> dict[str, Any]:
        return self._classes

    def leave_ClassDef(self, node: cst.ClassDef) -> bool | None:
        class_name = self.current_class_name
        class_name_short = node.name.value
        class_docstring = get_class_docstring(node)
        class_docstring = class_docstring.strip('"\r\n ') if class_docstring else None
        class_schemas = []
        class_bases = [
            val if isinstance(val, str) else Module([]).code_for_node(val).split(".")[-1]
            for base in node.bases
            for val in [base.value.value]
        ]

        # extract OpenAPI schema
        if class_docstring:
            lines = class_docstring.splitlines()
            for idx, line in enumerate(lines):
                if "The OpenAPI schema can be found at" in line:
                    for schema in lines[idx + 1 :]:
                        if not schema.strip().lstrip("- "):
                            break
                        class_schemas.append(schema.strip().lstrip("- "))

        if class_name_short in self._classes:
            print(f"Duplicate class definition for {class_name_short}")

        # TODO: ideally, the key should be the fully qualified class name and there
        #       should be an index from class_name to the fully qualified class name
        self._classes[class_name_short] = {
            "ids": self._ids,
            "name": class_name,
            "module": self._module,
            "package": self._package,
            "filename": self._filename,
            "docstring": class_docstring,
            "schemas": class_schemas,
            "bases": class_bases,
            "properties": self._properties,
            "methods": self._methods,
        }
        self._ids = []
        self._properties = {}
        self._methods = {}

        return super().leave_ClassDef(node)

    @staticmethod
    def return_types(return_type: str | None) -> list[str]:
        if return_type is None:
            return []

        return_type = return_type.strip()
        none = []
        if return_type.startswith("None | "):
            none = ["None"]
            return_type = return_type[7:]
        elif return_type.endswith("| None"):
            none = ["None"]
            return_type = return_type[:-7]

        types = [return_type] + none
        if "|" in return_type and "[" not in return_type:
            types = return_type.split("|") + none

        return [rt.strip().replace('"', "") for rt in types]

    def visit_FunctionDef(self, node: cst.FunctionDef) -> None:
        method_name = node.name.value
        returns = self.return_types(cst.Module([]).code_for_node(node.returns.annotation) if node.returns else None)

        if self.is_github_object_property(node):
            self._properties[method_name] = {"name": method_name, "returns": returns}

        visitor = SimpleStringCollector()
        node.body.visit(visitor)
        if visitor.strings:
            string = [line for line in visitor.strings[0].splitlines() if ":calls:" in line]
            if string:
                fields = string[0].split(":calls:")[1].strip(" `").split(" ", maxsplit=2)
                self._methods[method_name] = {
                    "name": method_name,
                    "call": {
                        "method": fields[0] if len(fields) > 0 else None,
                        "path": fields[1] if len(fields) > 1 else None,
                        "docs": fields[2] if len(fields) > 2 else None,
                    },
                    "returns": returns,
                }

        if method_name == "__repr__":
            # extract properties used here as ids
            visitor = DictKeyCollector(self._ids)
            node.visit(visitor)


class DictKeyCollector(cst.CSTVisitor):
    def __init__(self, keys: list[str]):
        super().__init__()
        self.keys = keys

    def visit_DictElement_key(self, node: cst.DictElement):
        self.keys.append(node.key.value.strip('"'))


class ApplySchemaBaseTransformer(CstTransformerBase, abc.ABC):
    def __init__(
        self,
        module_name: str,
        class_name: str,
        properties: dict[str, (PythonType | GithubClass | None, bool)],
        deprecate: bool,
    ):
        super().__init__()
        self.module_name = module_name
        self.class_name = class_name
        properties = [Property(name=n, data_type=t, deprecated=d) for n, (t, d) in properties.items()]
        self.properties = sorted(properties, key=lambda p: p.name)
        self.all_properties = self.properties.copy()
        self.deprecate = deprecate

    @property
    def current_property(self) -> Property | None:
        if not self.properties:
            return None
        return self.properties[0]


class ApplySchemaTransformer(ApplySchemaBaseTransformer):
    def __init__(
        self,
        module_name: str,
        class_name: str,
        properties: dict[str, (PythonType | GithubClass | None, bool)],
        completable: bool,
        deprecate: bool,
    ):
        super().__init__(module_name, class_name, properties, deprecate)
        self.completable = completable

    @staticmethod
    def deprecate_function(node: cst.FunctionDef) -> cst.FunctionDef:
        decorators = list(node.decorators)
        decorators.append(cst.Decorator(decorator=cst.Name(value="deprecated")))
        return node.with_changes(decorators=decorators)

    def inner_github_type(self, data_type: PythonType | GithubClass | list[PythonType | GithubClass]) -> [GithubClass]:
        if data_type is None:
            return []
        if isinstance(data_type, list):
            return [ght for dt in data_type for ght in self.inner_github_type(dt)]
        if isinstance(data_type, PythonType):
            return self.inner_github_type(data_type.inner_types)
        if isinstance(data_type, GithubClass):
            return [data_type]
        raise ValueError("Unsupported data type", data_type)

    def leave_Module(self, original_node: Module, updated_node: Module) -> Module:
        i = 0
        node = updated_node

        # add from __future__ import annotations if not the first import
        node = self.add_future_import(node)

        property_classes = {
            ghc
            for p in self.all_properties
            for ghc in self.inner_github_type(p.data_type)
            if ghc.module != self.module_name and ghc.name != self.class_name
        }
        import_classes = sorted(property_classes, key=lambda c: c.module)
        typing_classes = sorted(property_classes, key=lambda c: c.module)
        # TODO: do not import this file itself
        datetime_exists = False
        in_github_imports = False
        needs_datetime_import = any(
            p.data_type.type == "datetime" for p in self.all_properties if isinstance(p.data_type, PythonType)
        )

        # insert import classes if needed
        while (
            i < len(node.body)
            and isinstance(node.body[i], cst.SimpleStatementLine)
            and isinstance(node.body[i].body[0], (cst.Import, cst.ImportFrom))
        ):
            if self.is_datetime_import(node.body[i].body[0]):
                datetime_exists = True

            if not in_github_imports and self.is_github_import(node.body[i].body[0]):
                in_github_imports = True

                # emit datetime import if needed
                if needs_datetime_import and not datetime_exists:
                    node = self.add_datetime_import(node, i)
                    datetime_exists = True
                    i = i + 1

            if in_github_imports and import_classes:
                import_node = node.body[i].body[0]
                imported_module = (
                    (
                        import_node.module.value
                        if isinstance(import_node.module, cst.Name)
                        else import_node.module.attr.value
                    )
                    if isinstance(import_node, cst.ImportFrom)
                    else import_node.names[0].name.attr.value
                )
                while import_classes and import_classes[0].module < imported_module:
                    import_module = import_classes.pop(0)
                    import_stmt = cst.SimpleStatementLine(
                        [
                            cst.Import(
                                [cst.ImportAlias(self.create_attribute([import_module.package, import_module.module]))]
                            )
                        ]
                    )

                    stmts = node.body
                    node = node.with_changes(body=tuple(stmts[:i]) + (import_stmt,) + tuple(stmts[i:]))
                if import_classes and import_classes[0].module == imported_module:
                    import_classes.pop(0)
            i = i + 1

        # emit datetime import if needed
        if needs_datetime_import and not datetime_exists:
            node = self.add_datetime_import(node, i)
            i = i + 1

        while import_classes:
            import_module = import_classes.pop(0)
            import_stmt = cst.SimpleStatementLine(
                [cst.Import([cst.ImportAlias(self.create_attribute([import_module.package, import_module.module]))])]
            )
            stmts = node.body
            node = node.with_changes(body=tuple(stmts[:i]) + (import_stmt,) + tuple(stmts[i:]))

        # insert typing classes if needed
        if isinstance(node.body[-2], cst.If):
            if_node = node.body[-2]
            i = 0
            while i < len(if_node.body.body) and isinstance(if_node.body.body[i].body[0], (cst.Import, cst.ImportFrom)):
                imported_module = if_node.body.body[i].body[0].module.attr.value
                while typing_classes and typing_classes[0].module < imported_module:
                    typing_class = typing_classes.pop(0)
                    import_stmt = cst.SimpleStatementLine(
                        [
                            cst.ImportFrom(
                                module=self.create_attribute([typing_class.package, typing_class.module]),
                                names=[cst.ImportAlias(cst.Name(typing_class.name))],
                            )
                        ]
                    )

                    stmts = if_node.body.body
                    if_node = if_node.with_changes(
                        body=if_node.body.with_changes(body=tuple(stmts[:i]) + (import_stmt,) + tuple(stmts[i:]))
                    )
                if typing_classes and typing_classes[0].module == imported_module:
                    typing_classes.pop(0)
                i = i + 1

            while typing_classes:
                typing_class = typing_classes.pop(0)
                import_stmt = cst.SimpleStatementLine(
                    [
                        cst.ImportFrom(
                            module=self.create_attribute([typing_class.package, typing_class.module]),
                            names=[cst.ImportAlias(cst.Name(typing_class.name))],
                        )
                    ]
                )

                stmts = if_node.body.body
                if_node = if_node.with_changes(
                    body=if_node.body.with_changes(body=tuple(stmts[:i]) + (import_stmt,) + tuple(stmts[i:]))
                )

            node = node.with_changes(body=tuple(node.body[:-2]) + (if_node, node.body[-1]))

        return node

    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef):
        if self.current_class_name != self.class_name:
            return updated_node
        if updated_node.name.value.startswith("__") and updated_node.name.value.endswith("__"):
            return updated_node
        if updated_node.name.value == "_initAttributes":
            return self.update_init_attrs(updated_node)

        nodes = []
        if updated_node.name.value == "_useAttributes":
            while self.current_property:
                prop = self.properties.pop(0)
                node = self.create_property_function(prop.name, prop.data_type, prop.deprecated)
                nodes.append(cst.EmptyLine(indent=False))
                nodes.append(node)
            nodes.append(self.update_use_attrs(updated_node))
            return cst.FlattenSentinel(nodes=nodes)

        updated_node_is_github_object_property = self.is_github_object_property(updated_node)

        while self.current_property and (
            updated_node_is_github_object_property
            and self.current_property.name < updated_node.name.value
            or not updated_node_is_github_object_property
        ):
            prop = self.properties.pop(0)
            node = self.create_property_function(prop.name, prop.data_type, prop.deprecated)
            nodes.append(cst.EmptyLine(indent=False))
            nodes.append(node)

        if updated_node_is_github_object_property:
            if (
                not self.current_property
                or updated_node.name.value != self.current_property.name
                or self.current_property.deprecated
            ):
                nodes.append(self.deprecate_function(updated_node) if self.deprecate else updated_node)
            else:
                nodes.append(updated_node)
            if self.current_property and updated_node.name.value == self.current_property.name:
                self.properties.pop(0)
        else:
            nodes.append(updated_node)

        return cst.FlattenSentinel(nodes=nodes)

    def create_property_function(
        self, name: str, data_type: PythonType | GithubClass | None, deprecated: bool
    ) -> cst.FunctionDef:
        # we need to make the 'headers' attribute truly private,
        # otherwise it conflicts with GithubObject._headers
        attr_name = f"__{name}" if name == "headers" else f"_{name}"
        complete_if_completable_stmt = cst.SimpleStatementLine(
            body=[
                cst.Expr(
                    cst.Call(
                        func=self.create_attribute(["self", "_completeIfNotSet"]),
                        args=[cst.Arg(self.create_attribute(["self", attr_name]))],
                    )
                )
            ]
        )
        return_stmt = cst.SimpleStatementLine(body=[cst.Return(self.create_attribute(["self", attr_name, "value"]))])
        stmts = ([complete_if_completable_stmt] if self.completable else []) + [return_stmt]

        return cst.FunctionDef(
            decorators=[cst.Decorator(decorator=cst.Name(value="property"))],
            name=cst.Name(value=name),
            params=cst.Parameters(params=[cst.Param(cst.Name("self"))]),
            returns=cst.Annotation(annotation=self.create_type(data_type, short_class_name=True)),
            body=cst.IndentedBlock(body=stmts),
        )

    @classmethod
    def create_type(
        cls, data_type: PythonType | GithubClass | None, short_class_name: bool = False
    ) -> cst.BaseExpression:
        if data_type is None:
            return cst.Name("None")
        if isinstance(data_type, GithubClass):
            if short_class_name:
                return cst.Name(data_type.name.split(".")[-1])
            return cls.create_attribute([data_type.package, data_type.module] + data_type.name.split("."))
        if data_type.type == "union":
            if len(data_type.inner_types) == 0:
                return cst.Name("None")
            if len(data_type.inner_types) == 1:
                return cls.create_type(data_type.inner_types[0], short_class_name)
            result = cst.BinaryOperation(
                cls.create_type(data_type.inner_types[0], short_class_name),
                cst.BitOr(),
                cls.create_type(data_type.inner_types[1], short_class_name),
            )
            for dt in data_type.inner_types[2:]:
                result = cst.BinaryOperation(result, cst.BitOr(), cls.create_type(dt, short_class_name))
            return result
        if data_type.inner_types:
            elems = [
                cst.SubscriptElement(cst.Index(cls.create_type(elem, short_class_name)))
                for elem in data_type.inner_types
            ]
            return cst.Subscript(cst.Name(data_type.type), slice=elems)
        return cst.Name(data_type.type)

    @classmethod
    def create_init_attr(cls, prop: Property) -> cst.SimpleStatementLine:
        # we need to make the 'headers' attribute truly private,
        # otherwise it conflicts with GithubObject._headers
        attr_name = f"__{prop.name}" if prop.name == "headers" else f"_{prop.name}"
        return cst.SimpleStatementLine(
            [
                cst.AnnAssign(
                    target=cls.create_attribute(["self", attr_name]),
                    annotation=cst.Annotation(
                        annotation=cst.Subscript(
                            value=cst.Name("Attribute"),
                            slice=[
                                cst.SubscriptElement(
                                    slice=cst.Index(cls.create_type(prop.data_type, short_class_name=True))
                                )
                            ],
                        )
                    ),
                    value=cst.Name("NotSet"),
                )
            ]
        )

    @classmethod
    def make_attribute(cls, prop: Property) -> cst.Call:
        func_name = None
        attr = cst.Subscript(
            value=cst.Name("attributes"),
            slice=[cst.SubscriptElement(slice=cst.Index(cst.SimpleString(f'"{prop.name}"')))],
        )
        if prop.data_type is None:
            func_name = "_makeClassAttribute"
            args = [cst.Arg(cst.Name("None")), cst.Arg(attr)]
            # TODO: warn about unknown / supported type
        elif isinstance(prop.data_type, GithubClass):
            func_name = "_makeClassAttribute"
            args = [cst.Arg(cls.create_type(prop.data_type)), cst.Arg(attr)]
        elif prop.data_type.type == "bool":
            func_name = "_makeBoolAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type.type == "int":
            func_name = "_makeIntAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type.type == "float":
            func_name = "_makeFloatAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type.type == "datetime":
            func_name = "_makeDatetimeAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type.type == "str":
            func_name = "_makeStringAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type.type == "dict":
            if isinstance(prop.data_type.inner_types[1], GithubClass):
                func_name = "_makeDictOfStringsToClassesAttribute"
                args = [cst.Arg(cls.create_type(prop.data_type.inner_types[1])), cst.Arg(attr)]
            else:
                func_name = "_makeDictAttribute"
                args = [cst.Arg(attr)]
        elif prop.data_type.type == "list":
            if prop.data_type.inner_types[0] is None:
                func_name = "_makeListOfClassesAttribute"
                args = [cst.Arg(attr)]
                # TODO: warn about unknown / supported type
            elif isinstance(prop.data_type.inner_types[0], GithubClass):
                func_name = "_makeListOfClassesAttribute"
                args = [cst.Arg(cls.create_type(prop.data_type.inner_types[0])), cst.Arg(attr)]
                # TODO: warn about unknown / supported type
            elif prop.data_type.inner_types[0].type == "int":
                func_name = "_makeListOfIntsAttribute"
                args = [cst.Arg(attr)]
            elif prop.data_type.inner_types[0].type == "str":
                func_name = "_makeListOfStringsAttribute"
                args = [cst.Arg(attr)]
            elif prop.data_type.inner_types[0].type == "dict":
                func_name = "_makeListOfDictsAttribute"
                args = [cst.Arg(attr)]
            elif (
                prop.data_type.inner_types[0].type == "list"
                and prop.data_type.inner_types[0].inner_types[0].type == "str"
            ):
                func_name = "_makeListOfListOfStringsAttribute"
                args = [cst.Arg(attr)]
        elif (
            prop.data_type.type == "union"
            and prop.data_type.inner_types
            and isinstance(prop.data_type.inner_types[0], GithubClass)
        ):
            func_name = "_makeClassAttribute"
            args = [cst.Arg(cls.create_type(prop.data_type)), cst.Arg(attr)]
        if func_name is None:
            raise ValueError(f"Unsupported data type {prop.data_type}")
        return cst.Call(func=cls.create_attribute(["self", func_name]), args=args)

    @classmethod
    def create_use_attr(cls, prop: Property) -> cst.BaseStatement:
        # we need to make the 'headers' attribute truly private,
        # otherwise it conflicts with GithubObject._headers
        attr_name = f"__{prop.name}" if prop.name == "headers" else f"_{prop.name}"
        return cst.If(
            test=cst.Comparison(
                left=cst.SimpleString(f'"{prop.name}"'),
                comparisons=[cst.ComparisonTarget(operator=cst.In(), comparator=cst.Name("attributes"))],
            ),
            body=cst.IndentedBlock(
                header=cst.TrailingWhitespace(
                    whitespace=cst.SimpleWhitespace("  "), comment=cst.Comment("# pragma no branch")
                ),
                body=[
                    cst.SimpleStatementLine(
                        [
                            cst.Assign(
                                targets=[cst.AssignTarget(cls.create_attribute(["self", attr_name]))],
                                value=cls.make_attribute(prop),
                            )
                        ]
                    )
                ],
            ),
        )

    def update_init_attrs(self, func: cst.FunctionDef) -> cst.FunctionDef:
        # adds only missing attributes, does not update existing ones
        statements = func.body.body
        new_statements = [self.create_init_attr(p) for p in self.all_properties]
        updated_statements = []

        for statement in statements:
            if not isinstance(statement, cst.SimpleStatementLine) or not isinstance(statement.body[0], cst.AnnAssign):
                updated_statements.append(statement)
                continue
            while new_statements and new_statements[0].body[0].target.attr.value < statement.body[0].target.attr.value:
                updated_statements.append(new_statements.pop(0))
            if new_statements and new_statements[0].body[0].target.attr.value == statement.body[0].target.attr.value:
                updated_statements.append(statement)
                new_statements.pop(0)
            else:
                updated_statements.append(statement)
        while new_statements:
            updated_statements.append(new_statements.pop(0))

        return func.with_changes(body=func.body.with_changes(body=updated_statements))

    def update_use_attrs(self, func: cst.FunctionDef) -> cst.FunctionDef:
        # adds only missing attributes, does not update existing ones
        statements = func.body.body
        new_statements = [
            self.create_use_attr(p)
            for p in self.all_properties
            # list of data types not supported
            if not isinstance(p.data_type, list)
        ]
        updated_statements = []

        for statement in statements:
            if not isinstance(statement, cst.If):
                updated_statements.append(statement)
                continue
            comparison = statement.test if isinstance(statement.test, cst.Comparison) else statement.test.left
            while new_statements and new_statements[0].test.left.value < comparison.left.value:
                updated_statements.append(new_statements.pop(0))
            if new_statements and new_statements[0].test.left.value == comparison.left.value:
                updated_statements.append(statement)
                new_statements.pop(0)
            else:
                updated_statements.append(statement)
        while new_statements:
            updated_statements.append(new_statements.pop(0))

        return func.with_changes(body=func.body.with_changes(body=updated_statements))


class ApplySchemaTestTransformer(ApplySchemaBaseTransformer):
    def __init__(
        self,
        ids: dict[str, list[str]],
        module_name: str,
        class_name: str,
        properties: dict[str, (str | dict | list | None, bool)],
        deprecate: bool,
    ):
        super().__init__(module_name, class_name, properties, deprecate)
        self.ids = ids

    def get_value(self, data_type: PythonType | GithubClass | None) -> Any:
        if data_type is None:
            return cst.Name("None")
        if isinstance(data_type, GithubClass):
            return cst.Name(data_type.name.split(".")[-1])
        # data_type is PythonType
        if data_type.type == "bool":
            return cst.Name("False")
        if data_type.type == "int":
            return cst.Integer("0")
        if data_type.type == "float":
            return cst.Float("0.0")
        if data_type.type == "str":
            return cst.SimpleString('""')
        if data_type.type == "datetime":
            equal = cst.AssignEqual(cst.SimpleWhitespace(""), cst.SimpleWhitespace(""))
            return cst.Call(
                func=cst.Name("datetime"),
                args=[
                    cst.Arg(cst.Integer("2020")),
                    cst.Arg(cst.Integer("1")),
                    cst.Arg(cst.Integer("2")),
                    cst.Arg(cst.Integer("12")),
                    cst.Arg(cst.Integer("34")),
                    cst.Arg(cst.Integer("56")),
                    cst.Arg(
                        keyword=cst.Name("tzinfo"),
                        equal=equal,
                        value=self.create_attribute(["timezone", "utc"]),
                    ),
                ],
            )
        return cst.SimpleString(f'"{data_type}"')

    def leave_Module(self, original_node: Module, updated_node: Module) -> Module:
        # add from __future__ import annotations if not the first import
        updated_node = self.add_future_import(updated_node)

        needs_datetime_import = any(
            p.data_type.type == "datetime" for p in self.all_properties if isinstance(p.data_type, PythonType)
        )

        if not needs_datetime_import:
            return updated_node

        i = 0
        node = updated_node
        datetime_exists = False
        in_github_imports = False
        while (
            i < len(node.body)
            and isinstance(node.body[i], cst.SimpleStatementLine)
            and isinstance(node.body[i].body[0], (cst.Import, cst.ImportFrom))
        ):
            import_stmt = node.body[i].body[0]
            if self.is_datetime_import(import_stmt):
                datetime_exists = True

            if not in_github_imports and self.is_github_import(import_stmt):
                in_github_imports = True

                # emit datetime import if needed
                if needs_datetime_import and not datetime_exists:
                    node = self.add_datetime_import(node, i)
                    datetime_exists = True
                    i = i + 1

            i = i + 1

        # emit datetime import if needed
        if needs_datetime_import and not datetime_exists:
            node = self.add_datetime_import(node, i)

        return node

    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef):
        def create_statement(prop: Property, self_attribute: bool) -> cst.SimpleStatementLine:
            # turn a list of GithubClasses into the first element of the list
            if (
                isinstance(prop.data_type, PythonType)
                and prop.data_type.type == "list"
                and isinstance(prop.data_type.inner_types[0], GithubClass)
                and prop.data_type.inner_types[0].ids
            ):
                prop = dataclasses.replace(prop, name=f"{prop.name}[0]", data_type=prop.data_type.inner_types[0])

            if (
                isinstance(prop.data_type, GithubClass)
                or isinstance(prop.data_type, PythonType)
                and prop.data_type.type == "union"
                and any(isinstance(inner, GithubClass) for inner in prop.data_type.inner_types)
            ):
                ids = []
                if isinstance(prop.data_type, PythonType):
                    ids_sets = [
                        set(inner.ids) for inner in prop.data_type.inner_types if isinstance(inner, GithubClass)
                    ]
                    if len(ids_sets) == 1:
                        ids = list(ids_sets[0])
                    elif len(ids_sets) > 1:
                        ids = ids_sets[0]
                        for ids_set in ids_sets[1:]:
                            ids = ids.intersection(ids_set)
                        ids = list(ids)
                else:
                    if prop.data_type.ids:
                        ids = prop.data_type.ids

                if ids:
                    id = ids[0]
                    return cst.SimpleStatementLine(
                        [
                            cst.Expr(
                                cst.Call(
                                    func=self.create_attribute(["self", "assertEqual"]),
                                    args=[
                                        cst.Arg(
                                            self.create_attribute(
                                                (["self"] if self_attribute else []) + [attribute, prop.name, id]
                                            )
                                        ),
                                        cst.Arg(cst.SimpleString('""')),
                                    ],
                                )
                            )
                        ]
                    )

            return cst.SimpleStatementLine(
                [
                    cst.Expr(
                        cst.Call(
                            func=self.create_attribute(["self", "assertEqual"]),
                            args=[
                                cst.Arg(
                                    self.create_attribute((["self"] if self_attribute else []) + [attribute, prop.name])
                                ),
                                cst.Arg(self.get_value(prop.data_type)),
                            ],
                        )
                    )
                ]
            )

        if updated_node.name.value == "testAttributes":
            # first we detect the attribute that is used to test this class
            # either the first line assigns a local variable with that attribute,
            # or we check assertions for the most common attribute
            if (
                isinstance(updated_node.body.body[0], cst.SimpleStatementLine)
                and isinstance(updated_node.body.body[0].body[0], cst.Assign)
                and not isinstance(updated_node.body.body[0].body[0].targets[0].target, cst.Attribute)
            ):
                attribute = updated_node.body.body[0].body[0].targets[0].target.value
                self_attribute = False
            else:
                candidates = [
                    attr.value.attr.value
                    for stmt in updated_node.body.body
                    if isinstance(stmt, cst.SimpleStatementLine)
                    for expr in stmt.body
                    if isinstance(expr, cst.Expr) and isinstance(expr.value, cst.Call)
                    for call in [expr.value]
                    if isinstance(call.func, cst.Attribute)
                    and isinstance(call.func.value, cst.Name)
                    and call.func.value.value == "self"
                    and isinstance(call.func.attr, cst.Name)
                    and call.func.attr.value.startswith("assert")
                    and len(call.args) > 0
                    for arg in [call.args[0]]
                    if isinstance(arg.value, cst.Attribute)
                    for attr in [arg.value]
                    if isinstance(attr.value, cst.Attribute)
                    and isinstance(attr.value.value, cst.Name)
                    and attr.value.value.value == "self"
                    and isinstance(attr.value.attr, cst.Name)
                ]
                if not list(Counter(candidates).items()):
                    raise Exception("Could not find the attribute to test this class")
                attribute = list(Counter(candidates).items())[0][0]
                self_attribute = True

            # now we detect all properties that are already tested
            # this is done in case properties are not tested in alphabetical order,
            # otherwise we would duplicate tests
            # this is the same logic as is used to come up with 'asserted_property' below
            existing_properties = {
                attrs[1]
                for node in updated_node.body.body
                if isinstance(node.body[0].value, cst.Call) and node.body[0].value.args
                for attr_nodes in [self.find_nodes(node.body[0].value.args[0].value, cst.Attribute)]
                if attr_nodes
                for attr_node in [attr_nodes[0]]
                for attrs_with_self in [self.parse_attribute(attr_node) if isinstance(attr_node, cst.Attribute) else []]
                for attrs in [
                    attrs_with_self[1:]
                    if attrs_with_self and self_attribute and attrs_with_self[0] == "self"
                    else attrs_with_self
                ]
                if len(attrs) >= 2 and attrs[0] == attribute
            }

            # we can remove all properties that already exist in the test file
            self.properties = [property for property in self.properties if property.name not in existing_properties]

            i = 0
            while i < len(updated_node.body.body):
                if (
                    not isinstance(updated_node.body.body[i].body[0].value, cst.Call)
                    or not updated_node.body.body[i].body[0].value.args
                ):
                    i = i + 1
                    continue

                attr_nodes = self.find_nodes(updated_node.body.body[i].body[0].value.args[0].value, cst.Attribute)
                if not attr_nodes:
                    i = i + 1
                    continue

                attr = attr_nodes[0]
                attrs = self.parse_attribute(attr) if isinstance(attr, cst.Attribute) else []
                if attrs and self_attribute and attrs[0] == "self":
                    attrs.pop(0)

                if len(attrs) >= 2 and attrs[0] == attribute:
                    asserted_property = attrs[1]
                    while self.properties and self.properties[0].name < asserted_property:
                        prop = self.properties.pop(0)
                        stmt = create_statement(prop, self_attribute)
                        stmts = updated_node.body.body
                        updated_node = updated_node.with_changes(
                            body=updated_node.body.with_changes(body=tuple(stmts[:i]) + (stmt,) + tuple(stmts[i:]))
                        )
                        i = i + 1
                    if self.properties and self.properties[0].name == asserted_property:
                        self.properties.pop(0)
                i = i + 1
            while self.properties:
                prop = self.properties.pop(0)
                stmt = create_statement(prop, self_attribute)
                stmts = updated_node.body.body
                updated_node = updated_node.with_changes(
                    body=updated_node.body.with_changes(body=tuple(stmts) + (stmt,))
                )
        return updated_node


class AddSchemasTransformer(CstTransformerBase):
    def __init__(self, class_name: str, schemas: list[str]):
        super().__init__()
        self.class_name = class_name
        self.schemas = schemas
        self.schema_added = 0

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef):
        if self.current_class_name == self.class_name:
            docstring = get_class_docstring(updated_node)
            if not docstring:
                print("Class has no docstring")
            else:
                lines = docstring.splitlines()
                first_line = lines[1]
                indent = first_line[: len(first_line) - len(first_line.lstrip())]
                heading = len(lines) - 1  # if there is no heading, we place it before the last line (the closing """)
                empty_footing = lines[-2].strip() == ""
                schema_lines = []
                for idx, line in enumerate(lines):
                    if "The OpenAPI schema can be found at" in line:
                        heading = idx
                        schema_lines = lines[idx + 1 : -2 if empty_footing else -1]
                        break
                before = len(schema_lines)
                schema_lines = sorted(list(set(schema_lines).union({f"{indent}- {schema}" for schema in self.schemas})))
                after = len(schema_lines)
                lines = (
                    lines[:heading]
                    +
                    # we add an empty line before the schema lines if there is none
                    ([""] if lines[heading - 1].strip() else [])
                    + [indent + "The OpenAPI schema can be found at"]
                    + schema_lines
                    + [""]
                    + lines[-1:]
                )
                docstring = "\n".join(lines)
                stmt = cst.SimpleStatementLine([cst.Expr(cst.SimpleString(docstring))])
                stmts = [stmt] + list(updated_node.body.body[1:])
                updated_node = updated_node.with_changes(body=updated_node.body.with_changes(body=stmts))
                self.schema_added += after - before

        return super().leave_ClassDef(original_node, updated_node)


class JsonSerializer(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(sorted(obj))
        return super().default(obj)


class IndexFileWorker:
    def __init__(self, classes: dict[str, Any]):
        self.classes = classes

    def index_file(self, filename: str):
        with open(filename) as r:
            code = "".join(r.readlines())

        from pathlib import Path

        visitor = IndexPythonClassesVisitor(self.classes)
        visitor.package("github")
        visitor.module(Path(filename.removesuffix(".py")).name)
        visitor.filename(filename)
        try:
            tree = cst.parse_module(code)
            tree.visit(visitor)
        except Exception as e:
            raise RuntimeError(f"Failed to parse {filename}", e)


class OpenApi:
    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.subcommand = args.subcommand
        self.dry_run = args.dry_run
        self.verbose = args.verbose

        index = (
            OpenApi.read_index(args.index_filename) if self.subcommand != "index" and "index_filename" in args else {}
        )
        self.classes = index.get("classes", {})
        self.schema_to_class = index.get("indices", {}).get("schema_to_classes", {})
        self.schema_to_class["default"] = ["GithubObject"]

    @staticmethod
    def read_index(filename: str) -> dict[str, Any]:
        with open(filename) as r:
            return json.load(r)

    @staticmethod
    def get_schema(spec: dict[str, Any], path: str) -> (list[str], dict[str, Any]):
        steps = []
        source_path = path.strip("/")
        while True:
            if source_path.startswith('"'):
                if '"' not in source_path[1:]:
                    raise ValueError(f"Unclosed quote in path: {path}")
                start = source_path.index('"', 1)
                if "/" not in source_path[start:]:
                    steps.append(source_path)
                    break
                split = source_path[start:].index("/") + start
                step = source_path[1 : split - 1]
                source_path = source_path[split + 1 :]
            else:
                if "/" not in source_path:
                    steps.append(source_path)
                    break
                step, source_path = source_path.split("/", maxsplit=1)
            steps.append(step)

        schema = spec
        for step in steps:
            if isinstance(schema, list):
                schema = schema[int(step)]
            else:
                schema = schema.get(step, {})
        return steps, schema

    def get_inner_spec_types(self, schema: dict, schema_path: list[str | int]) -> list[str]:
        """
        Returns inner spec type, ignores outer datastructures like lists or pagination.
        """
        if "$ref" in schema:
            return [schema.get("$ref")]
        if "oneOf" in schema:
            return [
                spec_type
                for idx, component in enumerate(schema.get("oneOf"))
                for spec_type in self.get_inner_spec_types(component, schema_path + ["oneOf", str(idx)])
            ]
        if "allOf" in schema and len(schema.get("allOf")) == 1:
            return [schema.get("allOf")[0].get("$ref")]
        if schema.get("type") == "object":
            # extract the inner type of pagination objects
            if "properties" in schema:
                props = schema.get("properties")
                list_items = [n for n, p in props.items() if p.get("type") == "array" and "items" in p]
                total_count_items = [
                    n for n, p in props.items() if n.startswith("total_") and p.get("type") == "integer"
                ]
                if len(list_items) == 1 and len(total_count_items) == 1:
                    list_item = list_items[0]
                    return self.get_inner_spec_types(
                        props.get(list_item).get("items"), schema_path + ["properties", list_item, "items"]
                    )
            return ["/".join(["#"] + schema_path)]
        if schema.get("type") == "array" and "items" in schema:
            return self.get_inner_spec_types(schema.get("items"), schema_path + ["items"])
        return []

    def as_python_type(self, schema_type: dict[str, Any], schema_path: list[str]) -> PythonType | GithubClass | None:
        schema = None
        data_type = schema_type.get("type")
        if "$ref" in schema_type:
            schema = schema_type.get("$ref").strip("# ")
        elif "allOf" in schema_type and len(schema_type.get("allOf")) == 1:
            return self.as_python_type(schema_type.get("allOf")[0], schema_path + ["allOf", "0"])
        if data_type == "object":
            schema = "/".join([""] + schema_path)
        if schema is not None:
            if schema in self.schema_to_class:
                classes = self.schema_to_class[schema]
                if not isinstance(classes, list):
                    raise ValueError(f"Expected list of types for schema: {schema}")
                if len(classes) == 0:
                    raise ValueError(f"Expected non-empty list of types for schema: {schema}")
                if len(classes) == 1:
                    class_name = classes[0]
                    if class_name not in self.classes:
                        if self.verbose:
                            print(f"Class not found in index: {class_name}")
                        return None
                    return GithubClass(**self.classes.get(class_name))
                if self.verbose:
                    for class_name in classes:
                        if class_name not in self.classes:
                            print(f"Class not found in index: {class_name}")
                return PythonType(
                    type="union",
                    inner_types=[GithubClass(**self.classes.get(cls)) for cls in classes if cls in self.classes],
                )
            if self.verbose:
                print(f"Schema not implemented: {'.'.join([''] + schema_path)}")
            return PythonType(type="dict", inner_types=[PythonType("str"), PythonType("Any")])

        if data_type is None:
            if self.verbose:
                print(f"There is no $ref and no type in schema: {json.dumps(schema_type)}")
            return None

        if data_type == "array":
            return PythonType(
                type="list", inner_types=[self.as_python_type(schema_type.get("items"), schema_path + ["items"])]
            )

        format = schema_type.get("format")
        data_types = {
            "boolean": {None: "bool"},
            "integer": {None: "int"},
            "number": {None: "float"},
            "string": {
                None: "str",
                "date-time": "datetime",
                "uri": "str",
            },
        }

        if data_type not in data_types:
            if self.verbose:
                print(f"Unsupported data type: {data_type}")
            return None

        formats = data_types.get(data_type)
        return PythonType(type=formats.get(format) or formats.get(None))

    @staticmethod
    def extend_inheritance(classes: dict[str, Any]) -> bool:
        extended_classes = {}
        updated = False

        for name, cls in classes.items():
            orig_inheritance = cls.get("inheritance", set()).union(set(cls.get("bases", [])))
            inheritance = orig_inheritance.union(
                ancestor for base in cls.get("bases", []) for ancestor in classes.get(base, {}).get("inheritance", [])
            )
            cls["inheritance"] = inheritance
            extended_classes[name] = cls
            updated = updated or inheritance != orig_inheritance

        return updated

    @classmethod
    def propagate_ids(cls, classes: dict[str, Any]) -> bool:
        updated = False

        def get_ids(class_name: str) -> list[str]:
            clazz = classes.get(class_name, {})
            ids = clazz.get("ids", [])
            if ids:
                return ids
            for base in clazz.get("bases", []):
                ids = get_ids(base)
                if ids:
                    return ids
            return []

        for name, clazz in sorted(classes.items(), key=lambda v: v[0]):
            if not clazz.get("ids", []):
                base_ids = get_ids(name)
                if base_ids:
                    clazz["ids"] = base_ids
                    updated = True

        return updated

    @classmethod
    def add_schema_to_class(cls, class_name: str, filename: str, schemas: list[str], dry_run: bool) -> int:
        with open(filename) as r:
            code = "".join(r.readlines())

        transformer = AddSchemasTransformer(class_name, schemas)
        tree = cst.parse_module(code)
        updated_tree = tree.visit(transformer)
        cls.write_code(code, updated_tree.code, filename, dry_run)
        return transformer.schema_added

    @staticmethod
    def write_code(orig_code: str, updated_code: str, filename: str, dry_run: bool) -> bool:
        if dry_run:
            diff = difflib.unified_diff(orig_code.splitlines(1), updated_code.splitlines(1))
            changes = "".join(diff)
            print("Diff:")
            print(changes)
            return len(changes) > 0
        else:
            if updated_code != orig_code:
                with open(filename, "w") as w:
                    w.write(updated_code)
            return True

    def apply(self, spec_file: str, index_filename: str, class_names: list[str], dry_run: bool, tests: bool) -> bool:
        with open(spec_file) as r:
            spec = json.load(r)
        with open(index_filename) as r:
            index = json.load(r)
        classes = index.get("classes", {})

        for class_name in class_names:
            clazz = GithubClass.from_class_name(class_name, index)

            print(f"Applying spec {spec_file} to {clazz.full_class_name} ({clazz.filename})")
            cls = classes.get(clazz.short_class_name, {})
            irrelevant_bases = {
                inheritance
                for base in ["GithubObject", "CompletableGithubObject", "NonCompletableGithubObject"]
                for inheritance in classes.get(base, {}).get("inheritance", [])
            }
            relevant_bases = set(cls.get("inheritance", [])).difference(irrelevant_bases)
            inherited_properties = {
                property for base in relevant_bases for property in classes.get(base, {}).get("properties", {}).keys()
            }
            completable = "CompletableGithubObject" in cls.get("inheritance", [])
            cls_schemas = cls.get("schemas", [])
            for schema_name in cls_schemas:
                print(f"Applying schema {schema_name}")
                schema_path, schema = self.get_schema(spec, schema_name)

                all_properties = {
                    k: (self.as_python_type(v, schema_path + ["properties", k]), v.get("deprecated", False))
                    for k, v in schema.get("properties", {}).items()
                }
                genuine_properties = {k: v for k, v in all_properties.items() if k not in inherited_properties}

                with open(clazz.filename) as r:
                    code = "".join(r.readlines())

                transformer = ApplySchemaTransformer(
                    clazz.module, class_name, genuine_properties.copy(), completable=completable, deprecate=False
                )
                tree = cst.parse_module(code)
                tree_updated = tree.visit(transformer)
                changed = self.write_code(code, tree_updated.code, clazz.filename, dry_run)

                if tests and os.path.exists(clazz.test_filename):
                    with open(clazz.test_filename) as r:
                        code = "".join(r.readlines())

                    transformer = ApplySchemaTestTransformer(
                        cls.get("ids", []), clazz.module, class_name, all_properties.copy(), deprecate=False
                    )
                    tree = cst.parse_module(code)
                    tree_updated = tree.visit(transformer)
                    changed = self.write_code(code, tree_updated.code, clazz.test_filename, dry_run) or changed

                return changed

    def fetch(self, api: str, api_version: str, commit: str | None, spec_file: str) -> bool:
        ref = "refs/heads/main" if commit is None else commit
        base_url = f"https://github.com/github/rest-api-description/raw/{ref}/descriptions"
        url = f"{base_url}/{api}/{api}.{api_version}.json"
        response = requests.get(url)
        response.raise_for_status()
        written = 0
        with open(spec_file, "wb") as w:
            print(f"fetching {url}")
            for chunk in response.iter_content(131072):
                w.write(chunk)
                print(".", end="")
                written += len(chunk)
            print()
            print(f"written {written // 1024 / 1024:.3f} MBytes")
        return True

    def index(self, github_path: str, index_filename: str, dry_run: bool) -> bool:
        import multiprocessing

        files = [f for f in listdir(github_path) if isfile(join(github_path, f)) and f.endswith(".py")]
        print(f"Indexing {len(files)} Python files")

        # index files in parallel
        with multiprocessing.Manager() as manager:
            classes = manager.dict()
            indexer = IndexFileWorker(classes)
            with multiprocessing.Pool() as pool:
                pool.map(indexer.index_file, iterable=[join(github_path, file) for file in files])
            classes = dict(classes)

            # construct inheritance list
            while self.extend_inheritance(classes):
                pass

            # propagate ids of base classes to derived classes
            while self.propagate_ids(classes):
                pass

            # construct class_to_descendants
            class_to_descendants = {}
            for name, descendant in classes.items():
                for cls in descendant.get("inheritance", []):
                    if cls not in class_to_descendants:
                        class_to_descendants[cls] = []
                    class_to_descendants[cls].append(name)
            class_to_descendants = {cls: sorted(descendants) for cls, descendants in class_to_descendants.items()}

            path_to_classes = {}
            schema_to_classes = {}
            for name, cls in classes.items():
                # construct path-to-class index
                for method in cls.get("methods", {}).values():
                    path = method.get("call", {}).get("path")
                    if not path:
                        continue
                    verb = method.get("call", {}).get("method", "").lower()
                    if not verb:
                        if self.verbose:
                            print(f"Unknown verb for path {path} of class {name}")
                        continue

                    if not path.startswith("/") and self.verbose:
                        print(f"Unsupported path: {path}")
                    returns = method.get("returns", [])
                    if path not in path_to_classes:
                        path_to_classes[path] = {}
                    if verb not in path_to_classes[path]:
                        path_to_classes[path][verb] = set()
                    path_to_classes[path][verb] = sorted(list(set(path_to_classes[path][verb]).union(set(returns))))

                # construct schema-to-class index
                for schema in cls.get("schemas"):
                    if schema not in schema_to_classes:
                        schema_to_classes[schema] = []
                    schema_to_classes[schema].append(name)

            print(f"Indexed {len(classes)} classes")
            print(f"Indexed {len(path_to_classes)} paths")
            print(f"Indexed {len(schema_to_classes)} schemas")

            data = {
                "sources": github_path,
                "classes": classes,
                "indices": {
                    "class_to_descendants": class_to_descendants,
                    "path_to_classes": path_to_classes,
                    "schema_to_classes": schema_to_classes,
                },
            }

            if dry_run:
                if os.path.exists(index_filename):
                    with open(index_filename) as w:
                        orig_json = w.read()
                    # compare the serialized json for stability, not the dict
                    data_json = json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False, cls=JsonSerializer)
                    return orig_json != data_json
            else:
                with open(index_filename, "w") as w:
                    json.dump(data, w, indent=2, sort_keys=True, ensure_ascii=False, cls=JsonSerializer)

            return True

    def suggest(
        self, spec_file: str, index_filename: str, class_names: list[str] | None, add: bool, dry_run: bool
    ) -> bool:
        print(f"Using spec {spec_file}")
        with open(spec_file) as r:
            spec = json.load(r)
        with open(index_filename) as r:
            index = json.load(r)

        schemas_added = 0
        schemas_suggested = 0

        if class_names:
            if len(class_names) == 1:
                print(f"Suggesting API schemas for PyGithub class {class_names[0]}")
            else:
                print(f"Suggesting API schemas for PyGithub {len(class_names)} classes")
        else:
            print("Suggesting API schemas for PyGithub classes")

        def inner_return_type(return_type: str) -> list[str]:
            return_type = return_type.strip()
            if return_type == "None":
                return []
            if return_type.startswith("Optional[") and return_type.endswith("]"):
                return inner_return_type(return_type[9:-1])
            if return_type.startswith("PaginatedList[") and return_type.endswith("]"):
                return inner_return_type(return_type[14:-1])
            if return_type.startswith("list[") and return_type.endswith("]"):
                return inner_return_type(return_type[5:-1])
            if return_type.startswith("dict[") and "," in return_type and return_type.endswith("]"):
                # a dict of types indicates a wrapping object containing these types
                return []

            # now that we have removed outer types, we can look for alternatives
            if "|" in return_type:
                return [rt for alt in return_type.split("|") for rt in inner_return_type(alt)]

            # return the pure class name, no outer class, module or package names
            if "." in return_type:
                return [return_type.split(".")[-1]]

            return [return_type]

        # suggest schemas based on properties of classes
        available_schemas = {}
        unimplemented_schemas = set()
        for cls in self.classes.values():
            schemas: list[str] = cls.get("schemas", [])
            properties: dict[str, Any] = cls.get("properties", {})
            if not schemas or not properties:
                continue

            for schema_name in schemas:
                schema_path, schema = self.get_schema(spec, schema_name)

                if not schema:
                    print(f"Schema {schema_name} of class {cls.get('name')} not found in spec")
                    continue

                for property_name, property_spec_type in schema.get("properties", {}).items():
                    property = properties.get(property_name, {})
                    returns = property.get("returns", [])
                    for ret in returns:
                        cls_names = set(inner_return_type(ret))
                        for cls_name in cls_names:
                            if class_names and cls_name not in class_names:
                                continue
                            if cls_name in ["bool", "int", "str", "datetime", "list", "dict", "Any"]:
                                continue
                            if cls_name not in available_schemas:
                                available_schemas[cls_name] = {}
                            key = (cls.get("name"), property_name)
                            if key not in available_schemas[cls_name]:
                                available_schemas[cls_name][key] = []
                            spec_type = self.get_inner_spec_types(
                                property_spec_type, schema_path + ["properties", property_name]
                            )
                            for st in spec_type:
                                if st.lstrip("#") not in index.get("indices", {}).get("schema_to_classes", {}):
                                    unimplemented_schemas.add(st.lstrip("#"))
                            available_schemas[cls_name][key].extend(spec_type)

        for schema in sorted(list(unimplemented_schemas)):
            print(f"schema not implemented: {schema}")

        classes = index.get("classes", {})

        for cls, provided_schemas in sorted(available_schemas.items()):
            available = set()
            implemented = classes.get(cls, {}).get("schemas", [])
            providing_properties = []

            for providing_property, spec_types in provided_schemas.items():
                available = available.union([t.lstrip("#") for t in spec_types])
                providing_properties.append(providing_property)

            schemas_to_implement = sorted(list(available.difference(set(implemented))))
            # schemas_to_remove = sorted(list(set(implemented).difference(available)))
            if schemas_to_implement:  # or schemas_to_remove:
                print()
                print(f"Class {cls}:")
                for schema_to_implement in sorted(schemas_to_implement):
                    print(f"- should implement schema {schema_to_implement}")
                # for schema_to_remove in sorted(schemas_to_remove):
                #    print(f"- should not implement schema {schema_to_remove}")
                print("Properties returning the class:")
                for providing_class, providing_property in sorted(providing_properties):
                    print(f"- {providing_class}.{providing_property}")

                if add and schemas_to_implement:
                    clazz = classes.get(cls, {})
                    filename = clazz.get("filename")
                    clazz_name = clazz.get("name")
                    if not filename or not clazz_name:
                        print(f"Class name or filename for class {cls} not known")
                        sys.exit(1)

                    print(f"Adding schemas to {cls}")
                    added = self.add_schema_to_class(clazz_name, filename, schemas_to_implement, dry_run)
                    schemas_added += added
            schemas_suggested += len(schemas_to_implement)

        # suggest schemas based on API calls
        available_schemas = {}
        paths = set(spec.get("paths", {}).keys()).union(index.get("indices", {}).get("path_to_classes", {}).keys())
        for path in paths:
            for verb in spec.get("paths", {}).get(path, {}).keys():
                responses_of_path = spec.get("paths", {}).get(path, {}).get(verb, {}).get("responses", {})
                schema_path = ["paths", f'"{path}"', verb, "responses"]
                # we ignore wrapping types like lists / arrays here and assume methods comply with schema in that sense
                schemas_of_path = [
                    components.lstrip("#")
                    for status, response in responses_of_path.items()
                    if status.isnumeric() and int(status) < 400 and "content" in response
                    for schema in [response.get("content").get("application/json", {}).get("schema", {})]
                    for components in self.get_inner_spec_types(
                        schema, schema_path + [str(status), "content", '"application/json"', "schema"]
                    )
                ]
                classes_of_path = index.get("indices", {}).get("path_to_classes", {}).get(path, {}).get(verb, [])

                for cls in classes_of_path:
                    # we ignore wrapping types like lists / arrays here and assume methods comply with schema in that sense
                    return_types = set(inner_return_type(cls))

                    for cls in return_types:
                        if cls not in available_schemas:
                            available_schemas[cls] = {}
                        if verb not in available_schemas[cls]:
                            available_schemas[cls][verb] = {}
                        available_schemas[cls][verb][path] = set(schemas_of_path)

        for cls, available_verbs in sorted(available_schemas.items(), key=lambda v: v[0]):
            if cls in ["bool", "str", "None"]:
                continue
            if cls not in classes:
                if self.verbose:
                    print(f"Unknown class {cls}")
                continue
            if class_names and cls not in class_names:
                continue

            paths = {}
            available = set()
            implemented = classes.get(cls, {}).get("schemas", [])

            for verb, available_paths in available_verbs.items():
                if verb not in paths:
                    paths[verb] = set()
                paths[verb] = paths[verb].union(available_paths.keys())
                available = available.union({a for s in available_paths.values() for a in s})

            schemas_to_implement = sorted(list(available.difference(set(implemented))))
            # schemas_to_remove = sorted(list(set(implemented).difference(available)))
            if schemas_to_implement:  # or schemas_to_remove:
                print()
                print(f"Class {cls}:")
                for schema_to_implement in sorted(schemas_to_implement):
                    print(f"- should implement schema {schema_to_implement}")
                # for schema_to_remove in sorted(schemas_to_remove):
                #    print(f"- should not implement schema {schema_to_remove}")
                print("Paths returning the class:")
                for verb, verb_paths in sorted(paths.items(), key=lambda v: v[0]):
                    for path in sorted(verb_paths):
                        print(f"- {verb.upper()} {path}")

                if add and schemas_to_implement:
                    filename = classes.get(cls, {}).get("filename")
                    if not filename:
                        print(f"Filename for class {cls} not known")
                        sys.exit(1)

                    print(f"Adding schemas to {cls}")
                    added = self.add_schema_to_class(cls, filename, schemas_to_implement, dry_run)
                    schemas_added += added
            schemas_suggested += len(schemas_to_implement)

        print(f"Suggested {schemas_suggested} schemas")
        print(f"Added {schemas_added} schemas")
        return schemas_suggested > 0

    def create(
        self,
        github_path: str,
        spec_file: str,
        index_filename: str,
        class_name: str,
        parent_name: str,
        docs_url: str,
        schemas: list[str],
        dry_run: bool,
        tests: bool,
    ) -> bool:
        with open(index_filename) as r:
            index = json.load(r)

        clazz = GithubClass.from_class_name(class_name)
        parent_class = GithubClass.from_class_name(parent_name, index)
        print(f"Creating class {clazz.full_class_name} with parent {parent_class.full_class_name} in {clazz.filename}")
        if os.path.exists(clazz.filename):
            raise ValueError(f"File exists already: {clazz.filename}")
        if tests and os.path.exists(clazz.test_filename):
            raise ValueError(f"File exists already: {clazz.test_filename}")

        source = (
            f"############################ Copyrights and license ############################\n"
            f"#                                                                              #\n"
            f"#                                                                              #\n"
            f"# This file is part of PyGithub.                                               #\n"
            f"# http://pygithub.readthedocs.io/                                              #\n"
            f"#                                                                              #\n"
            f"# PyGithub is free software: you can redistribute it and/or modify it under    #\n"
            f"# the terms of the GNU Lesser General Public License as published by the Free  #\n"
            f"# Software Foundation, either version 3 of the License, or (at your option)    #\n"
            f"# any later version.                                                           #\n"
            f"#                                                                              #\n"
            f"# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #\n"
            f"# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #\n"
            f"# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #\n"
            f"# details.                                                                     #\n"
            f"#                                                                              #\n"
            f"# You should have received a copy of the GNU Lesser General Public License     #\n"
            f"# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #\n"
            f"#                                                                              #\n"
            f"################################################################################\n"
            f"\n"
            f"from __future__ import annotations\n"
            f"\n"
            f"from typing import Any, TYPE_CHECKING\n"
            f"\n"
            f"from {parent_class.package}.{parent_class.module} import {parent_class.name}\n"
            f"from github.GithubObject import Attribute, NotSet\n"
            f"\n"
            f"if TYPE_CHECKING:\n"
            f"    from {parent_class.package}.{parent_class.module} import {parent_class.name}\n"
            f"\n"
            f"\n"
            f"class {clazz.name}({parent_class.name}):\n"
            f'    """\n'
            f"    This class represents {clazz.name}.\n"
            f"\n"
            f"    The reference can be found here\n"
            f"    {docs_url}\n"
            f"\n"
            f"    The OpenAPI schema can be found at\n" + "".join(f"    - {schema}\n" for schema in schemas) + "\n"
            '    """\n'
            "\n"
            "    def _initAttributes(self) -> None:\n"
            "        # TODO: remove if parent does not implement this\n"
            "        super()._initAttributes()\n"
            "\n"
            "    def __repr__(self) -> str:\n"
            '        # TODO: replace "some_attribute" with uniquely identifying attributes in the dict, then run:\n'
            '        return self.get__repr__({"some_attribute": self._some_attribute.value})\n'
            "\n"
            "    def _useAttributes(self, attributes: dict[str, Any]) -> None:\n"
            "        # TODO: remove if parent does not implement this\n"
            "        super()._useAttributes(attributes)\n"
            "\n"
        )
        self.write_code("", source, clazz.filename, dry_run=False)

        if tests:
            source = (
                f"############################ Copyrights and license ############################\n"
                f"#                                                                              #\n"
                f"#                                                                              #\n"
                f"# This file is part of PyGithub.                                               #\n"
                f"# http://pygithub.readthedocs.io/                                              #\n"
                f"#                                                                              #\n"
                f"# PyGithub is free software: you can redistribute it and/or modify it under    #\n"
                f"# the terms of the GNU Lesser General Public License as published by the Free  #\n"
                f"# Software Foundation, either version 3 of the License, or (at your option)    #\n"
                f"# any later version.                                                           #\n"
                f"#                                                                              #\n"
                f"# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #\n"
                f"# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #\n"
                f"# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #\n"
                f"# details.                                                                     #\n"
                f"#                                                                              #\n"
                f"# You should have received a copy of the GNU Lesser General Public License     #\n"
                f"# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #\n"
                f"#                                                                              #\n"
                f"################################################################################\n"
                f"\n"
                f"from __future__ import annotations\n"
                f"\n"
                f"from datetime import datetime, timezone\n"
                f"\n"
                f"from . import Framework\n"
                f"\n"
                f"\n"
                f"class {clazz.name}(Framework.TestCase):\n"
                f"    def setUp(self):\n"
                f"        super().setUp()\n"
                f"        # TODO: create an instance of type {clazz.name} and assign to self.attr, then run:\n"
                f"        #   pytest {clazz.test_filename} -k testAttributes --record --auth_with_token\n"
                f'        #   sed -i -e "s/token private_token_removed/Basic login_and_password_removed/" tests/ReplayData/{clazz.name}.setUp.txt\n'
                f"        #   ./scripts/update-assertions.sh {clazz.test_filename} testAttributes\n"
                f"        #   pre-commit run --all-files\n"
                f"        self.attr = None\n"
                f"\n"
                f"    def testAttributes(self):\n"
                f'        self.assertEqual(self.attr.url, "")\n'
            )
            self.write_code("", source, clazz.test_filename, dry_run=False)

        success = True
        try:
            if dry_run:
                with NamedTemporaryFile(delete_on_close=False) as f:
                    f.close()
                    print(f"Updating temporary index {f.name}")
                    self.index(github_path, f.name, dry_run=False)
                    self.apply(spec_file, f.name, [clazz.name], dry_run=False, tests=tests)
            else:
                print("Updating index")
                self.index(github_path, index_filename, dry_run=False)
                self.apply(spec_file, index_filename, [clazz.name], dry_run=False, tests=tests)
        except Exception as e:
            success = False
            raise e
        finally:
            if dry_run:
                if success:
                    # print created files
                    files = [clazz.filename] + ([clazz.test_filename] if tests else [])
                    for filename in files:
                        print()
                        print(f"{filename}:")
                        with open(filename) as r:
                            for line in r.readlines():
                                print(f"+{line}", end="")

                # Remove created files
                os.unlink(clazz.filename)
                if tests:
                    os.unlink(clazz.test_filename)
        return True

    @staticmethod
    def parse_args():
        args_parser = argparse.ArgumentParser(
            description="Applies OpenAPI spec to PyGithub GithubObject classes",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        )
        args_parser.add_argument(
            "--dry-run", default=False, action="store_true", help="Show prospect changes and do not modify any files"
        )
        args_parser.add_argument(
            "--exit-code", default=False, action="store_true", help="Indicate changes via non-zeor exit code"
        )
        args_parser.add_argument("--verbose", default=False, action="store_true", help="Provide more information")

        subparsers = args_parser.add_subparsers(dest="subcommand")
        fetch_parser = subparsers.add_parser("fetch")
        fetch_parser.add_argument(
            "api",
            help="Github API, e.g. api.github.com, ghec, ghes-3.15. See https://github.com/github/rest-api-description/tree/main/descriptions",
        )
        fetch_parser.add_argument("--commit", help="Specific commit to fetch file from", nargs="?")
        fetch_parser.add_argument("api_version", help="Github API version date, e.g. 2022-11-28")
        fetch_parser.add_argument("spec", help="Github API OpenAPI spec file to be written")

        index_parser = subparsers.add_parser("index")
        index_parser.add_argument("github_path", help="Path to PyGithub Python files")
        index_parser.add_argument("index_filename", help="Path of index file")

        suggest_parser = subparsers.add_parser("suggest")
        suggest_parser.add_argument(
            "--add", default=False, action="store_true", help="Add suggested schemas to source code"
        )
        suggest_parser.add_argument("spec", help="Github API OpenAPI spec file")
        suggest_parser.add_argument("index_filename", help="Path of index file")
        suggest_parser.add_argument("class_name", help="Name of the class to get suggestions for", nargs="*")

        apply_parser = subparsers.add_parser("apply", description="Apply schema to source code")
        apply_parser.add_argument("--tests", help="Also apply spec to test files", action="store_true")
        apply_parser.add_argument("spec", help="Github API OpenAPI spec file")
        apply_parser.add_argument("index_filename", help="Path of index file")
        apply_parser.add_argument("class_name", help="PyGithub GithubObject class name", nargs="*")

        create_parser = subparsers.add_parser("create", description="Create PyGithub classes")
        create_parser.add_argument(
            "--completable",
            help="New PyGithub class is completable, implies --parent CompletableGithubObject",
            dest="parent",
            action="store_const",
            const="CompletableGithubObject",
            default="NonCompletableGithubObject",
        )
        create_parser.add_argument("--parent", help="A parent PyGithub class")
        create_parser.add_argument("--tests", help="Also create test file", action="store_true")
        create_parser.add_argument("github_path", help="Path to PyGithub Python files")
        create_parser.add_argument("spec", help="Github API OpenAPI spec file")
        create_parser.add_argument("index_filename", help="Path of index file")
        create_parser.add_argument("class_name", help="PyGithub GithubObject class name")
        create_parser.add_argument(
            "docs_url",
            help="Github REST API documentation URL, for instance https://docs.github.com/en/rest/commits/commits#get-a-commit-object",
        )
        create_parser.add_argument("schema", help="Github API OpenAPI schema name", nargs="*")

        if len(sys.argv) == 1:
            args_parser.print_help()
            sys.exit(1)
        return args_parser.parse_args()

    def main(self):
        changes = False
        if args.subcommand == "fetch":
            changes = self.fetch(self.args.api, self.args.api_version, self.args.commit, self.args.spec)
        elif args.subcommand == "index":
            changes = self.index(self.args.github_path, self.args.index_filename, self.args.dry_run)
        elif self.args.subcommand == "suggest":
            changes = self.suggest(
                self.args.spec, self.args.index_filename, self.args.class_name, self.args.add, self.args.dry_run
            )
        elif self.args.subcommand == "apply":
            changes = self.apply(
                self.args.spec, self.args.index_filename, self.args.class_name, self.args.dry_run, self.args.tests
            )
        elif self.args.subcommand == "create":
            changes = self.create(
                self.args.github_path,
                self.args.spec,
                self.args.index_filename,
                self.args.class_name,
                self.args.parent,
                self.args.docs_url,
                self.args.schema,
                self.args.dry_run,
                self.args.tests,
            )
        else:
            raise RuntimeError("Subcommand not implemented " + args.subcommand)

        # indicate changes via exit code
        if self.args.exit_code and changes:
            sys.exit(1)


if __name__ == "__main__":
    args = OpenApi.parse_args()
    OpenApi(args).main()
