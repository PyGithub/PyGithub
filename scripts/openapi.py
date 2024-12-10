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
import sys
from collections import Counter
from json import JSONEncoder
from os import listdir
from os.path import isfile, join
from typing import Any, Sequence

import libcst as cst
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
            val if isinstance(val, str) else Module([]).code_for_node(val)
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

    def leave_Module(self, original_node: Module, updated_node: Module) -> Module:
        i = 0
        node = updated_node
        property_classes = {
            p.data_type
            for p in self.all_properties
            if isinstance(p.data_type, GithubClass)
            and p.data_type.module != self.module_name
            and p.data_type.name != self.class_name
        }
        import_classes = sorted(property_classes, key=lambda c: c.module)
        typing_classes = sorted(property_classes, key=lambda c: c.module)
        # TODO: do not import this file itself
        in_github_imports = False
        # insert import classes if needed
        while (
            i < len(node.body)
            and isinstance(node.body[i], cst.SimpleStatementLine)
            and isinstance(node.body[i].body[0], (cst.Import, cst.ImportFrom))
        ):
            if (
                not in_github_imports
                and isinstance(node.body[i].body[0].names[0].name, cst.Attribute)
                and node.body[i].body[0].names[0].name.value.value == "github"
            ):
                in_github_imports = True
            if in_github_imports and import_classes:
                import_node = node.body[i].body[0]
                imported_module = (
                    (import_node.module.value if isinstance(import_node.module, cst.Name) else import_node.module.attr.value)
                    if isinstance(import_node, cst.ImportFrom)
                    else import_node.names[0].name.attr.value
                )
                while import_classes and import_classes[0].module < imported_module:
                    import_module = import_classes.pop(0)
                    import_stmt = cst.SimpleStatementLine(
                        [
                            cst.Import(
                                [
                                    cst.ImportAlias(
                                        cst.Attribute(cst.Name(import_module.package), cst.Name(import_module.module))
                                    )
                                ]
                            )
                        ]
                    )

                    stmts = node.body
                    node = node.with_changes(body=tuple(stmts[:i]) + (import_stmt,) + tuple(stmts[i:]))
                if import_classes and import_classes[0].module == imported_module:
                    import_classes.pop(0)
            i = i + 1

        while import_classes:
            import_module = import_classes.pop(0)
            import_stmt = cst.SimpleStatementLine(
                [
                    cst.Import(
                        [
                            cst.ImportAlias(
                                cst.Attribute(cst.Name(import_module.package), cst.Name(import_module.module))
                            )
                        ]
                    )
                ]
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
                                module=cst.Attribute(cst.Name(typing_class.package), cst.Name(typing_class.module)),
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
                            module=cst.Attribute(cst.Name(typing_class.package), cst.Name(typing_class.module)),
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

        if updated_node.name.value == "_useAttributes":
            return self.update_use_attrs(updated_node)

        nodes = []
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
        complete_if_completable_stmt = cst.SimpleStatementLine(
            body=[
                cst.Expr(
                    cst.Call(
                        func=cst.Attribute(value=cst.Name(value="self"), attr=cst.Name(value="_completeIfNotSet")),
                        args=[cst.Arg(cst.Attribute(value=cst.Name(value="self"), attr=cst.Name(value=f"_{name}")))],
                    )
                )
            ]
        )
        return_stmt = cst.SimpleStatementLine(
            body=[
                cst.Return(
                    cst.Attribute(
                        value=cst.Attribute(value=cst.Name(value="self"), attr=cst.Name(value=f"_{name}")),
                        attr=cst.Name(value="value"),
                    )
                )
            ]
        )
        stmts = ([complete_if_completable_stmt] if self.completable else []) + [return_stmt]

        return cst.FunctionDef(
            decorators=[cst.Decorator(decorator=cst.Name(value="property"))],
            name=cst.Name(value=name),
            params=cst.Parameters(params=[cst.Param(cst.Name("self"))]),
            returns=cst.Annotation(annotation=self.create_type(data_type)),
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
                return cst.Name(data_type.name)
            return cst.Attribute(
                cst.Attribute(cst.Name(data_type.package), cst.Name(data_type.module)), cst.Name(data_type.name)
            )
        if data_type.type == "union":
            if len(data_type.inner_types) == 0:
                return cst.Name("None")
            if len(data_type.inner_types) == 1:
                return cls.create_type(data_type.inner_types[0], short_class_name)
            result = cst.BinaryOperation(
                cls.create_type(data_type.inner_types[0]), cst.BitOr(), cls.create_type(data_type.inner_types[1])
            )
            for dt in data_type.inner_types[2:]:
                result = cst.BinaryOperation(result, cst.BitOr(), cls.create_type(dt))
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
        return cst.SimpleStatementLine(
            [
                cst.AnnAssign(
                    target=cst.Attribute(value=cst.Name("self"), attr=cst.Name(f"_{prop.name}")),
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
                func_name = "_makeListOfIntAttribute"
                args = [cst.Arg(attr)]
            elif prop.data_type.inner_types[0].type == "str":
                func_name = "_makeListOfStringAttribute"
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
        return cst.Call(func=cst.Attribute(cst.Name("self"), cst.Name(func_name)), args=args)

    @classmethod
    def create_use_attr(cls, prop: Property) -> cst.BaseStatement:
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
                                targets=[cst.AssignTarget(cst.Attribute(cst.Name("self"), cst.Name(f"_{prop.name}")))],
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
                        value=cst.Attribute(cst.Name("timezone"), cst.Name("utc")),
                    ),
                ],
            )
        return cst.SimpleString(f'"{data_type}"')

    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef):
        def create_statement(prop: Property) -> cst.SimpleStatementLine:
            if isinstance(prop.data_type, GithubClass) and prop.data_type.ids:
                id = prop.data_type.ids[0]
                return cst.SimpleStatementLine(
                    [
                        cst.Expr(
                            cst.Call(
                                func=cst.Attribute(cst.Name("self"), cst.Name("assertEqual")),
                                args=[
                                    cst.Arg(
                                        cst.Attribute(
                                            cst.Attribute(
                                                cst.Attribute(cst.Name("self"), cst.Name(attribute)),
                                                cst.Name(prop.name),
                                            ),
                                            cst.Name(id),
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
                            func=cst.Attribute(cst.Name("self"), cst.Name("assertEqual")),
                            args=[
                                cst.Arg(
                                    cst.Attribute(
                                        cst.Attribute(cst.Name("self"), cst.Name(attribute)), cst.Name(prop.name)
                                    )
                                ),
                                cst.Arg(self.get_value(prop.data_type)),
                            ],
                        )
                    )
                ]
            )

        if updated_node.name.value == "testAttributes":
            # first we detect the attribute that is used to test this class
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

            def parse_attribute(attr: cst.Attribute) -> list[str]:
                attrs = []
                while isinstance(attr, cst.Attribute):
                    attrs.insert(0, attr.attr.value)
                    attr = attr.value
                attrs.insert(0, attr.value)
                return attrs

            i = 0
            while i < len(updated_node.body.body):
                attr = updated_node.body.body[i].body[0].value.args[0].value
                attrs = parse_attribute(attr) if isinstance(attr, cst.Attribute) else []
                if len(attrs) >= 3 and attrs[0] == "self" and attrs[1] == attribute:
                    asserted_property = attrs[2]
                    while self.properties and self.properties[0].name < asserted_property:
                        prop = self.properties.pop(0)
                        stmt = create_statement(prop)
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
                stmt = create_statement(prop)
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
        tree = cst.parse_module(code)
        tree.visit(visitor)


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
        if schema.get("type") == "object":
            # extract the inner type of pagination objects
            if "properties" in schema:
                props = schema.get("properties")
                list_items = [n for n, p in props.items() if p.get("type") == "array" and "items" in p]
                if "total_count" in props and len(list_items) == 1:
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
    def add_schema_to_class(cls, class_name: str, filename: str, schemas: list[str], dry_run: bool) -> int:
        with open(filename) as r:
            code = "".join(r.readlines())

        transformer = AddSchemasTransformer(class_name, schemas)
        tree = cst.parse_module(code)
        updated_tree = tree.visit(transformer)
        cls.write_code(code, updated_tree.code, filename, dry_run)
        return transformer.schema_added

    @staticmethod
    def write_code(orig_code: str, updated_code: str, filename: str, dry_run: bool):
        if dry_run:
            diff = difflib.unified_diff(orig_code.splitlines(1), updated_code.splitlines(1))
            print("Diff:")
            print("".join(diff))
        else:
            if updated_code != orig_code:
                with open(filename, "w") as w:
                    w.write(updated_code)

    def apply(self, spec_file: str, index_filename: str, class_name: str, dry_run: bool, tests: bool):
        full_class_name = class_name
        if "." not in class_name:
            full_class_name = f"github.{class_name}.{class_name}"
        package, module, class_name = full_class_name.split(".", maxsplit=2)
        class_name_short = class_name.split(".")[-1]
        filename = f"{package}/{module}.py"
        test_filename = f"tests/{module}.py"

        print(f"Applying spec {spec_file} to {full_class_name} ({filename})")
        with open(spec_file) as r:
            spec = json.load(r)
        with open(index_filename) as r:
            index = json.load(r)

        cls = index.get("classes", {}).get(class_name_short, {})
        completable = "CompletableGithubObject" in cls.get("inheritance", [])
        cls_schemas = cls.get("schemas", [])
        for schema_name in cls_schemas:
            print(f"Applying schema {schema_name}")
            schema_path, schema = self.get_schema(spec, schema_name)

            properties = {
                k: (self.as_python_type(v, schema_path + ["properties", k]), v.get("deprecated", False))
                for k, v in schema.get("properties", {}).items()
            }

            with open(filename) as r:
                code = "".join(r.readlines())

            transformer = ApplySchemaTransformer(
                module, class_name, properties.copy(), completable=completable, deprecate=False
            )
            tree = cst.parse_module(code)
            tree_updated = tree.visit(transformer)
            self.write_code(code, tree_updated.code, filename, dry_run)

            if tests:
                with open(test_filename) as r:
                    code = "".join(r.readlines())

                transformer = ApplySchemaTestTransformer(
                    cls.get("ids", []), module, class_name, properties.copy(), deprecate=False
                )
                tree = cst.parse_module(code)
                tree_updated = tree.visit(transformer)
                self.write_code(code, tree_updated.code, test_filename, dry_run)

    def index(self, github_path: str, index_filename: str):
        import multiprocessing

        files = [f for f in listdir(github_path) if isfile(join(github_path, f)) and f.endswith(".py")]
        print(f"Indexing {len(files)} Python files")

        # index files in parallel
        manager = multiprocessing.Manager()
        classes = manager.dict()
        indexer = IndexFileWorker(classes)
        with multiprocessing.Pool() as pool:
            pool.map(indexer.index_file, iterable=[join(github_path, file) for file in files])
        classes = dict(classes)

        # construct inheritance list
        while self.extend_inheritance(classes):
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

        with open(index_filename, "w") as w:
            json.dump(data, w, indent=2, sort_keys=True, ensure_ascii=False, cls=JsonSerializer)

    def suggest(self, spec_file: str, index_filename: str, class_names: list[str] | None, add: bool, dry_run: bool):
        print(f"Using spec {spec_file}")
        with open(spec_file) as r:
            spec = json.load(r)
        with open(index_filename) as r:
            index = json.load(r)

        schemas_added = 0

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
                # inner type of dicts is the value type
                return inner_return_type(return_type[return_type.index(",") + 1 : -1])

            # now that we have removed outer types, we can look for alternatives
            if "|" in return_type:
                return [rt for alt in return_type.split("|") for rt in inner_return_type(alt)]

            # return the pure class name, no outer class, module or package names
            if "." in return_type:
                return [return_type.split(".")[-1]]

            return [return_type]

        # suggest schemas based on properties of classes
        available_schemas = {}
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
                            available_schemas[cls_name][key].extend(spec_type)

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
                    if "content" in response
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

        print(f"Added {schemas_added} schemas")

    @staticmethod
    def parse_args():
        args_parser = argparse.ArgumentParser(description="Applies OpenAPI spec to GithubObject classes")
        args_parser.add_argument(
            "--dry-run", default=False, action="store_true", help="Show prospect changes and do not modify any files"
        )
        args_parser.add_argument("--verbose", default=False, action="store_true", help="Provide more information")

        subparsers = args_parser.add_subparsers(dest="subcommand")
        index_parser = subparsers.add_parser("index")
        index_parser.add_argument("github_path", help="Path to Github Python files")
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
        apply_parser.add_argument("class_name", help="PyGithub GithubObject class name")

        if len(sys.argv) == 1:
            args_parser.print_help()
            sys.exit(1)
        return args_parser.parse_args()

    def main(self):
        if args.subcommand == "index":
            self.index(self.args.github_path, self.args.index_filename)
        elif self.args.subcommand == "suggest":
            self.suggest(
                self.args.spec, self.args.index_filename, self.args.class_name, self.args.add, self.args.dry_run
            )
        elif self.args.subcommand == "apply":
            self.apply(
                self.args.spec, self.args.index_filename, self.args.class_name, self.args.dry_run, self.args.tests
            )
        else:
            raise RuntimeError("Subcommand not implemented " + args.subcommand)


if __name__ == "__main__":
    args = OpenApi.parse_args()
    OpenApi(args).main()
