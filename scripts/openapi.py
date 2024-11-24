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
from typing import Sequence, Optional, Any, Union

import libcst as cst
from libcst import SimpleStatementLine, Expr, IndentedBlock, SimpleString, Module, FlattenSentinel, RemovalSentinel


@dataclasses.dataclass(frozen=True)
class GithubClass:
    package: str
    module: str
    name: str
    filename: str
    bases: list[str]
    inheritance: list[str]
    methods: dict
    schemas: list[str]
    docstring: str

    def __hash__(self):
        return hash((self.package, self.module, self.name))

@dataclasses.dataclass(frozen=True)
class Property:
    name: str
    data_type: str | GithubClass | list[GithubClass] | None
    deprecated: bool


class SimpleStringCollector(cst.CSTVisitor):
    def __init__(self):
        super().__init__()
        self._strings = []

    @property
    def strings(self):
        return self._strings

    def visit_SimpleString(self, node: cst.SimpleString) -> Optional[bool]:
        self._strings.append(node.evaluated_value)



def get_class_docstring(node: cst.ClassDef) -> str | None:
    try:
        if (isinstance(node.body, IndentedBlock) and
                isinstance(node.body.body[0], SimpleStatementLine) and
                isinstance(node.body.body[0].body[0], Expr) and
                isinstance(node.body.body[0].body[0].value, SimpleString)):
            return node.body.body[0].body[0].value.value
    except Exception as e:
        print(f"Extracting docstring of class {node.name.value} failed", e)


class IndexPythonClassesVisitor(cst.CSTVisitor):
    def __init__(self):
        super().__init__()
        self._module = None
        self._package = None
        self._filename = None
        self._classes = {}
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

    def leave_ClassDef(self, node: cst.ClassDef) -> Optional[bool]:
        class_name = node.name.value
        class_docstring = get_class_docstring(node)
        class_docstring = class_docstring.strip('"\r\n ') if class_docstring else None
        class_schemas = []
        class_bases = [val if isinstance(val, str) else Module([]).code_for_node(val)
                       for base in node.bases for val in [base.value.value]]

        # extract OpenAPI schema
        if class_docstring:
            lines = class_docstring.splitlines()
            for idx, line in enumerate(lines):
                if "The OpenAPI schema can be found at" in line:
                    for schema in lines[idx+1:]:
                        if not schema.strip():
                            break
                        class_schemas.append(schema.strip())

        if class_name in self._classes:
            print(f"Duplicate class definition for {class_name}")

        self._classes[class_name] = {
            "name": class_name,
            "module": self._module,
            "package": self._package,
            "filename": self._filename,
            "docstring": class_docstring,
            "schemas": class_schemas,
            "bases": class_bases,
            "methods": self._methods
        }
        self._methods = {}

    def visit_FunctionDef(self, node: cst.FunctionDef) -> Optional[bool]:
        method_name = node.name.value
        returns = cst.Module([]).code_for_node(node.returns.annotation) if node.returns else None
        if returns:
            if "[" in returns and "]" in returns:
                prefix, remain = returns.split("[", maxsplit=1)
                inner, suffix = remain.split("]", maxsplit=1)
                inner = inner.split(".")[-1]
                returns = f"{prefix}[{inner}]{suffix}"
            else:
                returns = returns.split(".")[-1]

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
                        "docs": fields[2] if len(fields) > 2 else None
                    },
                    "returns": [returns]
                }


class BaseTransformer(cst.CSTTransformer, abc.ABC):
    def __init__(self):
        super().__init__()
        self.visit_class_name = []

    def visit_ClassDef(self, node: cst.ClassDef):
        self.visit_class_name.append(node.name.value)

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef):
        self.visit_class_name.pop()
        return updated_node

    @property
    def current_class_name(self) -> str:
        return ".".join(self.visit_class_name)


class ApplySchemaBaseTransformer(BaseTransformer, abc.ABC):
    def __init__(self, module_name: str, class_name: str, properties: dict[str, (str | dict | list | None, bool)], deprecate: bool):
        super().__init__()
        self.module_name = module_name
        self.class_name = class_name
        self.properties = sorted([Property(name=k, data_type=GithubClass(**v[0]) if isinstance(v[0], dict) else (
            [GithubClass(**v) for v in v[0]] if isinstance(v[0], list) else v[0]), deprecated=v[1])
                                  for k, v in properties.items()],
                                 key=lambda p: p.name)
        self.all_properties = self.properties.copy()
        self.deprecate = deprecate

    @property
    def current_property(self) -> Property | None:
        if not self.properties:
            return None
        return self.properties[0]


class ApplySchemaTransformer(ApplySchemaBaseTransformer):
    def __init__(self, module_name: str, class_name: str, properties: dict[str, (str | dict | list | None, bool)], deprecate: bool):
        super().__init__(module_name, class_name, properties, deprecate)

    @staticmethod
    def contains_decorator(seq: Sequence[cst.Decorator], decorator_name: str):
        return any(d.decorator.value == decorator_name for d in seq if isinstance(d.decorator, cst.Name))

    @classmethod
    def is_github_object_property(cls, func_def: cst.FunctionDef):
        return cls.contains_decorator(func_def.decorators, "property")

    @staticmethod
    def deprecate_function(node: cst.FunctionDef) -> cst.FunctionDef:
        decorators = list(node.decorators)
        decorators.append(cst.Decorator(decorator=cst.Name(value="deprecated")))
        return node.with_changes(decorators=decorators)

    def leave_Module(self, original_node: "Module", updated_node: "Module") -> "Module":
        i = 0
        node = updated_node
        property_classes = {p.data_type for p in self.all_properties if isinstance(p.data_type, GithubClass) and p.data_type.module != self.module_name and p.data_type.name != self.class_name}
        import_classes = sorted(property_classes, key=lambda c: c.module)
        typing_classes = sorted(property_classes, key=lambda c: c.module)
        # TODO: do not import this file itself
        in_github_imports = False
        # insert import classes if needed
        while i < len(node.body) and isinstance(node.body[i], cst.SimpleStatementLine) and isinstance(node.body[i].body[0], (cst.Import, cst.ImportFrom)):
            if not in_github_imports and isinstance(node.body[i].body[0].names[0].name, cst.Attribute) and node.body[i].body[0].names[0].name.value.value == 'github':
                in_github_imports = True
            if in_github_imports and import_classes:
                imported_module = node.body[i].body[0].names[0].name.attr.value
                while import_classes and import_classes[0].module < imported_module:
                    import_module = import_classes[0]
                    import_stmt = cst.SimpleStatementLine([
                        cst.Import([cst.ImportAlias(cst.Attribute(cst.Name(import_module.package), cst.Name(import_module.module)))])
                    ])

                    stmts = node.body
                    node = node.with_changes(body=tuple(stmts[:i]) + (import_stmt, ) + tuple(stmts[i:]))
                    import_classes = import_classes[1:]
                if import_classes and import_classes[0].module == imported_module:
                    import_classes = import_classes[1:]
            i = i + 1

        # insert typing classes if needed
        if isinstance(node.body[-2], cst.If):
            if_node = node.body[-2]
            i = 0
            while i < len(if_node.body.body) and isinstance(if_node.body.body[i].body[0], (cst.Import, cst.ImportFrom)):
                imported_module = if_node.body.body[i].body[0].module.attr.value
                while typing_classes and typing_classes[0].module < imported_module:
                    typing_class = typing_classes[0]
                    import_stmt = cst.SimpleStatementLine([
                        cst.ImportFrom(
                            module=cst.Attribute(cst.Name(typing_class.package), cst.Name(typing_class.module)),
                            names=[cst.ImportAlias(cst.Name(typing_class.name))])
                    ])

                    stmts = if_node.body.body
                    if_node = if_node.with_changes(body=if_node.body.with_changes(body=tuple(stmts[:i]) + (import_stmt, ) + tuple(stmts[i:])))
                    typing_classes = typing_classes[1:]
                if typing_classes and typing_classes[0].module == imported_module:
                    typing_classes = typing_classes[1:]
                i = i + 1
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

        while self.current_property and (updated_node_is_github_object_property and self.current_property.name < updated_node.name.value or not updated_node_is_github_object_property):
            prop = self.properties.pop(0)
            node = self.create_property_function(prop.name, prop.data_type, prop.deprecated)
            nodes.append(cst.EmptyLine(indent=False))
            nodes.append(node)

        if updated_node_is_github_object_property:
            if not self.current_property or updated_node.name.value != self.current_property.name or self.current_property.deprecated:
                nodes.append(self.deprecate_function(updated_node) if self.deprecate else updated_node)
            else:
                nodes.append(updated_node)
            if self.current_property and updated_node.name.value == self.current_property.name:
                self.properties.pop(0)
        else:
            nodes.append(updated_node)

        return cst.FlattenSentinel(nodes=nodes)

    @classmethod
    def create_property_function(cls, name: str, data_type: str | GithubClass | None, deprecated: bool) -> cst.FunctionDef:
        docstring_type = data_type
        if isinstance(data_type, GithubClass):
            docstring_type = f":class:`{data_type.package}.{data_type.module}.{data_type.name}`"
            data_type = data_type.name

        return cst.FunctionDef(
            decorators=[cst.Decorator(decorator=cst.Name(value="property"))],
            name=cst.Name(value=name),
            params=cst.Parameters(params=[cst.Param(cst.Name("self"))]),
            returns=cst.Annotation(annotation=cst.Name(data_type)) if data_type else None,
            body=cst.IndentedBlock(body=[
                cst.SimpleStatementLine(body=[
                    cst.Expr(cst.Call(
                        func=cst.Attribute(value=cst.Name(value="self"), attr=cst.Name(value="_completeIfNotSet")),
                        args=[cst.Arg(cst.Attribute(value=cst.Name(value="self"), attr=cst.Name(value=f"_{name}")))]
                    ))
                ]),
                cst.SimpleStatementLine(body=[cst.Return(cst.Attribute(value=cst.Attribute(value=cst.Name(value="self"), attr=cst.Name(value=f"_{name}")), attr=cst.Name(value="value")))])
            ])
        )

    @classmethod
    def create_type(cls, data_type: str | GithubClass | list[GithubClass], short_class_name: bool = False) -> cst.BaseExpression:
        if isinstance(data_type, list):
            if len(data_type) == 0:
                return cst.Name("None")
            if len(data_type) == 1:
                return cls.create_type(data_type[0], short_class_name)
            result = cst.BinaryOperation(cls.create_type(data_type[0]), cst.BitOr(), cls.create_type(data_type[1]))
            for dt in data_type[2:]:
                result = cst.BinaryOperation(result, cst.BitOr(), cls.create_type(dt))
            return result
        if isinstance(data_type, GithubClass):
            if short_class_name:
                return cst.Name(data_type.name)
            return cst.Attribute(cst.Attribute(cst.Name(data_type.package), cst.Name(data_type.module)), cst.Name(data_type.name))

        if data_type and "[" in data_type:
            base = data_type[:data_type.find("[")]
            index = data_type[data_type.find("[")+1:data_type.find("]")]
            return cst.Subscript(cst.Name(base), slice=[cst.SubscriptElement(cst.Index(cst.Name(index)))])
        return cst.Name(data_type or "None")

    @classmethod
    def create_init_attr(cls, prop: Property) -> cst.SimpleStatementLine:
        return cst.SimpleStatementLine([cst.AnnAssign(
            target=cst.Attribute(value=cst.Name("self"), attr=cst.Name(f"_{prop.name}")),
            annotation=cst.Annotation(annotation=cst.Subscript(
                value=cst.Name("Attribute"),
                slice=[cst.SubscriptElement(slice=cst.Index(cls.create_type(prop.data_type, short_class_name=True)))]
            )),
            value=cst.Name("NotSet")
        )])

    @classmethod
    def make_attribute(cls, prop: Property) -> cst.Call:
        attr = cst.Subscript(
            value=cst.Name("attributes"),
            slice=[cst.SubscriptElement(slice=cst.Index(cst.SimpleString(f'"{prop.name}"')))]
        )
        if prop.data_type == "bool":
            func_name = "_makeBoolAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type == "int":
            func_name = "_makeIntAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type == "float":
            func_name = "_makeFloatAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type == "datetime":
            func_name = "_makeDatetimeAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type == "str":
            func_name = "_makeStringAttribute"
            args = [cst.Arg(attr)]
        elif isinstance(prop.data_type, GithubClass):
            func_name = "_makeClassAttribute"
            args = [cst.Arg(cls.create_type(prop.data_type)), cst.Arg(attr)]
        elif prop.data_type == "list[int]":
            func_name = "_makeListOfIntAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type == "list[str]":
            func_name = "_makeListOfStringAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type == "list[None]":
            func_name = "_makeListOfClassAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type is None:
            func_name = "_makeClassAttribute"
            args = [cst.Arg(cst.Name("None")), cst.Arg(attr)]
        else:
            raise ValueError(f"Unsupported data type {prop.data_type}")
        return cst.Call(func=cst.Attribute(cst.Name("self"), cst.Name(func_name)), args=args)

    @classmethod
    def create_use_attr(cls, prop: Property) -> cst.BaseStatement:
        return cst.If(
                test=cst.Comparison(
                    left=cst.SimpleString(f'"{prop.name}"'),
                    comparisons=[cst.ComparisonTarget(operator=cst.In(), comparator=cst.Name("attributes"))]
                ),
                body=cst.IndentedBlock(
                    header=cst.TrailingWhitespace(
                        whitespace=cst.SimpleWhitespace("  "),
                        comment=cst.Comment("# pragma no branch")
                    ),
                    body=[
                    cst.SimpleStatementLine([
                        cst.Assign(
                            targets=[cst.AssignTarget(cst.Attribute(cst.Name("self"), cst.Name(f'_{prop.name}')))],
                            value=cls.make_attribute(prop)
                        )
                    ])
                ])
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

        return func.with_changes(body=func.body.with_changes(body=updated_statements))

    def update_use_attrs(self, func: cst.FunctionDef) -> cst.FunctionDef:
        # adds only missing attributes, does not update existing ones
        statements = func.body.body
        new_statements = [self.create_use_attr(p) for p in self.all_properties]
        updated_statements = []

        for statement in statements:
            while new_statements and new_statements[0].test.left.value < statement.test.left.value:
                updated_statements.append(new_statements.pop(0))
            if new_statements and new_statements[0].test.left.value == statement.test.left.value:
                updated_statements.append(statement)
                new_statements.pop(0)
            else:
                updated_statements.append(statement)

        return func.with_changes(body=func.body.with_changes(body=updated_statements))


class ApplySchemaTestTransformer(ApplySchemaBaseTransformer):
    def __init__(self, module_name: str, class_name: str, properties: dict[str, (str | dict | list | None, bool)], deprecate: bool):
        super().__init__(module_name, class_name, properties, deprecate)

    def get_value(self, data_type: str | GithubClass | list[GithubClass]) -> Any:
        if isinstance(data_type, (GithubClass, list)):
            return cst.Call(func=cst.Name("object"))
        if data_type == "bool":
            return cst.Expr(cst.Name("False"))
        if data_type == "int":
            return cst.Expr(cst.Integer("0"))
        if data_type == "float":
            return cst.Expr(cst.Float("0.0"))
        if data_type == "datetime":
            equal = cst.AssignEqual(cst.SimpleWhitespace(""), cst.SimpleWhitespace(""))
            return cst.Call(func=cst.Name("datetime"), args=[
                cst.Arg(cst.Integer("2020")),
                cst.Arg(cst.Integer("1")),
                cst.Arg(cst.Integer("2")),
                cst.Arg(cst.Integer("12")),
                cst.Arg(cst.Integer("34")),
                cst.Arg(cst.Integer("56")),
                cst.Arg(keyword=cst.Name("tzinfo"), equal=equal, value=cst.Attribute(cst.Name("timezone"), cst.Name("utc"))),
            ])
        if data_type == "str":
            return cst.Expr(cst.SimpleString('""'))
        else:
            return cst.SimpleString(f'"{data_type}"')

    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef):
        if updated_node.name.value == 'testAttributes':
            # first we detect the attribute that is used to test this class
            candidates = [attr.value.attr.value
                          for stmt in updated_node.body.body if isinstance(stmt, cst.SimpleStatementLine)
                          for expr in stmt.body if isinstance(expr, cst.Expr) and isinstance(expr.value, cst.Call)
                          for call in [expr.value] if isinstance(call.func, cst.Attribute) and
                             isinstance(call.func.value, cst.Name) and call.func.value.value == "self" and
                             isinstance(call.func.attr, cst.Name) and call.func.attr.value.startswith("assert") and
                             len(call.args) > 0
                          for arg in [call.args[0]] if isinstance(arg.value, cst.Attribute)
                          for attr in [arg.value] if  isinstance(attr.value, cst.Attribute) and
                             isinstance(attr.value.value, cst.Name) and attr.value.value.value == "self" and
                             isinstance(attr.value.attr, cst.Name)]
            attribute = list(Counter(candidates).items())[0][0]

            i = 0
            while i < len(updated_node.body.body):
                attr = updated_node.body.body[i].body[0].value.args[0].value
                if isinstance(attr, cst.Attribute) and attr.value.value.value == "self" and attr.value.attr.value == attribute:
                    asserted_property = attr.attr.value
                    while self.properties and self.properties[0].name < asserted_property:
                        prop = self.properties.pop(0)
                        stmt = cst.SimpleStatementLine([
                            cst.Expr(cst.Call(
                                func=cst.Attribute(cst.Name("self"), cst.Name("assertEqual")),
                                args=[
                                    cst.Arg(cst.Attribute(cst.Attribute(cst.Name("self"), cst.Name(attribute)), cst.Name(prop.name))),
                                    cst.Arg(self.get_value(prop.data_type))
                                ]
                            ))
                        ])
                        stmts = updated_node.body.body
                        updated_node = updated_node.with_changes(body=updated_node.body.with_changes(body=tuple(stmts[:i]) + (stmt, ) + tuple(stmts[i:])))
                        i = i + 1
                    if self.properties and self.properties[0].name == asserted_property:
                        self.properties.pop(0)
                i = i + 1
        return updated_node


class AddSchemasTransformer(BaseTransformer):
    def __init__(self, class_name: str, schemas: list[str]):
        super().__init__()
        self.class_name = class_name
        self.schemas = schemas

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef):
        if self.current_class_name == self.class_name:
            docstring = get_class_docstring(updated_node)
            if not docstring:
                print(f"Class has no docstring")
            else:
                lines = docstring.splitlines()
                heading = len(lines)-1  # if there is no heading, we place it before the last line (the closing """)
                schema_lines = []
                for idx, line in enumerate(lines):
                    if "The OpenAPI schema can be found at" in line:
                        heading = idx
                        schema_lines = lines[idx+1:-1]
                        break
                schema_lines = sorted(list(set(schema_lines).union(set([f"    {schema}" for schema in self.schemas]))))
                lines = lines[:heading] + ["    The OpenAPI schema can be found at"] + schema_lines + lines[-1:]
                docstring = "\n".join(lines)
                stmt = cst.SimpleStatementLine([cst.Expr(cst.SimpleString(docstring))])
                stmts = [stmt] + list(updated_node.body.body[1:])
                updated_node = updated_node.with_changes(body=updated_node.body.with_changes(body=stmts))

        return super().leave_ClassDef(original_node, updated_node)

class JsonSerializer(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(sorted(obj))
        return super().default(obj)


class OpenApi:
    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.subcommand = args.subcommand
        self.dry_run = args.dry_run

        index = OpenApi.read_index(args.index_filename) if self.subcommand != "index" and 'index_filename' in args else {}
        self.classes = index.get("classes", {})
        self.schema_to_class = index.get("indices", {}).get("schema_to_classes", {})
        self.schema_to_class['default'] = ["GithubObject"]

    @staticmethod
    def read_index(filename: str) -> dict[str, Any]:
        with open(filename, 'r') as r:
            return json.load(r)

    def as_python_type(self, data_type: str | None, format: str | None) -> str | dict | list | None:
        if data_type is None:
            return None

        data_types = {
            "array": "list",
            "boolean": "bool",
            "integer": "int",
            "object": self.schema_to_class,
            "string": {
                None: "str",
                "date-time": "datetime",
                "uri": "str",
            },
        }

        if data_type not in data_types:
            raise ValueError(f"Unsupported data type: {data_type}")

        maybe_with_format = data_types.get(data_type)

        if isinstance(maybe_with_format, str):
            if data_type == "array":
                return f"{maybe_with_format}[{self.as_python_type(format, None)}]"
            return maybe_with_format

        if 'default' not in maybe_with_format and format not in maybe_with_format:
            raise ValueError(f"Unsupported data type format: {format}")

        python_type = maybe_with_format.get(format, maybe_with_format.get('default'))
        if data_type == "object":
            if not isinstance(python_type, list):
                raise ValueError(f"Expected list of types for data type: {data_type}")
            if len(python_type) == 0:
                raise ValueError(f"Expected non-empty list of types for data type: {data_type}")
            if len(python_type) == 1:
                return self.classes.get(python_type[0], python_type[0])
            return [self.classes.get(cls, cls) for cls in python_type]
        return python_type

    @staticmethod
    def extend_inheritance(classes: dict[str, Any]) -> bool:
        extended_classes = {}
        updated = False

        for name, cls in classes.items():
            orig_inheritance = cls.get("inheritance", set()).union(set(cls.get("bases", [])))
            inheritance = orig_inheritance.union(ancestor
                                                 for base in cls.get("bases", [])
                                                 for ancestor in classes.get(base, {}).get("inheritance", []))
            cls["inheritance"] = inheritance
            extended_classes[name] = cls
            updated = updated or inheritance != orig_inheritance

        return updated

    @classmethod
    def add_schema_to_class(cls, class_name: str, filename: str, schemas: list[str], dry_run: bool):
        with open(filename, "r") as r:
            code = "".join(r.readlines())

        transformer = AddSchemasTransformer(class_name, schemas)
        tree = cst.parse_module(code)
        updated_tree = tree.visit(transformer)
        cls.write_code(code, updated_tree.code, filename, dry_run)

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
        if '.' not in class_name:
            full_class_name = f'github.{class_name}.{class_name}'
        package, module, class_name = full_class_name.split('.', maxsplit=2)
        filename = f"{package}/{module}.py"
        test_filename = f"tests/{module}.py"

        print(f"Applying spec {spec_file} to {full_class_name} ({filename})")
        with open(spec_file, 'r') as r:
            spec = json.load(r)
        with open(index_filename, "r") as r:
            index = json.load(r)

        schemas = spec.get('components', {}).get('schemas', {})
        for schema_name in index.get("classes", {}).get(class_name, {}).get("schemas", []):
            if not schema_name.startswith('/components/schemas/'):
                print(f"Unsupported schema {schema_name}")
                continue
            schema_name = schema_name[20:]

            print(f"Applying schema {schema_name}")
            schema = schemas.get(schema_name, {})
            properties = {k: (self.as_python_type(v.get("type") or "object", v.get("format") or v.get("$ref", "").strip("# ") or v.get("items", {}).get("type") or v.get("items", {}).get("$ref")), v.get("deprecated", False)) for k, v in schema.get("properties", {}).items()}

            with open(filename, "r") as r:
                code = "".join(r.readlines())

            transformer = ApplySchemaTransformer(class_name, class_name, properties.copy(), deprecate=False)
            tree = cst.parse_module(code)
            tree_updated = tree.visit(transformer)
            self.write_code(code, tree_updated.code, filename, dry_run)

            if tests:
                with open(test_filename, "r") as r:
                    code = "".join(r.readlines())

                transformer = ApplySchemaTestTransformer(class_name, class_name, properties.copy(), deprecate=False)
                tree = cst.parse_module(code)
                tree_updated = tree.visit(transformer)
                self.write_code(code, tree_updated.code, test_filename, dry_run)

    def index(self, github_path: str, index_filename: str, verbose: bool):
        files = [f for f in listdir(github_path) if isfile(join(github_path, f)) and f.endswith(".py")]
        print(f"Indexing {len(files)} Python files")

        visitor = IndexPythonClassesVisitor()
        visitor.package("github")
        for file in files:
            filename = join(github_path, file)
            with open(filename, "r") as r:
                code = "".join(r.readlines())

            visitor.module(file.removesuffix(".py"))
            visitor.filename(filename)
            tree = cst.parse_module(code)
            tree.visit(visitor)

        # construct inheritance list
        classes = visitor.classes
        while self.extend_inheritance(classes):
            pass

        # construct class_to_descendants
        class_to_descendants = {}
        for name, descendant in classes.items():
            for cls in descendant.get("inheritance", []):
                if cls not in class_to_descendants:
                    class_to_descendants[cls] = []
                class_to_descendants[cls].append(name)
        class_to_descendants = {cls: sorted(descendants)
                                for cls, descendants in class_to_descendants.items()}

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
                    if verbose:
                        print(f"Unknown verb for path {path} of class {name}")
                    continue

                if not path.startswith("/") and verbose:
                    print(f"Unsupported path: {path}")
                returns = method.get("returns", [])
                if not path in path_to_classes:
                    path_to_classes[path] = {}
                if verb not in path_to_classes[path]:
                    path_to_classes[path][verb] = set()
                path_to_classes[path][verb] = sorted(list(set(path_to_classes[path][verb]).union(set(returns))))

            # construct schema-to-class index
            for schema in cls.get("schemas"):
                if not schema in schema_to_classes:
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
            }
        }

        with open(index_filename, "w") as w:
            json.dump(data, w, indent=2, sort_keys=True, ensure_ascii=False, cls=JsonSerializer)

    def suggest(self, spec_file: str, index_filename: str, class_name: str | None, add: bool, dry_run: bool, verbose: bool):
        print(f"Using spec {spec_file}")
        with open(spec_file, 'r') as r:
            spec = json.load(r)
        with open(index_filename, "r") as r:
            index = json.load(r)

        if class_name:
            print(f"Suggesting API schemas for PyGithub class {class_name}")
        else:
            print("Suggesting API schemas for PyGithub classes")

        def inner_return_type(return_type: str) -> str:
            return_type = return_type.strip()
            if return_type.startswith("None | "):
                return_type = return_type[7:]
            if return_type.endswith(" | None"):
                return_type = return_type[:-7]
            if return_type.startswith("list[") and return_type.endswith("]"):
                return_type = return_type[5:-1]
            if return_type.startswith("PaginatedList[") and return_type.endswith("]"):
                return_type = return_type[14:-1]
            return return_type

        available_schemas = {}
        paths = set(spec.get('paths', {}).keys()).union(index.get("indices", {}).get("path_to_classes", {}).keys())
        for path in paths:
            for verb in spec.get("paths", {}).get(path, {}).keys():
                responses_of_path = spec.get("paths", {}).get(path, {}).get(verb, {}).get("responses", {})
                # we ignore wrapping types like lists / arrays here and assume methods comply with schema in that sense
                schemas_of_path = [components.lstrip("#")
                                   for response in responses_of_path.values() if "content" in response
                                   for schema in [response.get("content").get("application/json", {}).get("schema", {})]
                                   for components in ([schema.get("$ref")] if "$ref" in schema else
                                                      [component.get("$ref") for component in schema.get("oneOf", [schema.get("items")] if "items" in schema else []) if "$ref" in component])]
                classes_of_path = index.get("indices", {}).get("path_to_classes", {}).get(path, {}).get(verb, [])

                for cls in classes_of_path:
                    # we ignore wrapping types like lists / arrays here and assume methods comply with schema in that sense
                    while True:
                        inner_cls = inner_return_type(cls)
                        if inner_cls == cls:
                            break
                        cls = inner_cls

                    # handle some special cases where cls == "list[T] | T",
                    # which for our purposes is equivalent to "T | T" which is "T"
                    if "|" in cls:
                        fields = cls.split("|")
                        if len(fields) == 2 and inner_return_type(fields[0]) == inner_return_type(fields[1]):
                            cls = inner_return_type(fields[0])

                    if cls not in available_schemas:
                        available_schemas[cls] = {}
                    if verb not in available_schemas[cls]:
                        available_schemas[cls][verb] = {}
                    available_schemas[cls][verb][path] = set(schemas_of_path)

        classes = index.get("classes", {})
        for cls, available_verbs in sorted(available_schemas.items(), key=lambda v: v[0]):
            if cls in ['bool', 'str', 'None']:
                continue
            if cls not in classes:
                if verbose:
                    print(f"Unknown class {cls}")
                continue
            if class_name and cls != class_name:
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
            schemas_to_remove = sorted(list(set(implemented).difference(available)))
            if schemas_to_implement or schemas_to_remove:
                print()
                print(f"Class {cls}:")
                for schema_to_implement in sorted(schemas_to_implement):
                    print(f"- should implement schema {schema_to_implement}")
                for schema_to_remove in sorted(schemas_to_remove):
                    print(f"- should not implement schema {schema_to_remove}")
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
                    self.add_schema_to_class(cls, filename, schemas_to_implement, dry_run)

    @staticmethod
    def parse_args():
        args_parser = argparse.ArgumentParser(description="Applies OpenAPI spec to GithubObject classes")
        args_parser.add_argument("--dry-run", default=False, action="store_true", help="Show prospect changes and do not modify any files")
        args_parser.add_argument("--verbose", default=False, action="store_true", help="Provide more information")

        subparsers = args_parser.add_subparsers(dest="subcommand")
        index_parser = subparsers.add_parser("index")
        index_parser.add_argument("github_path", help="Path to Github Python files")
        index_parser.add_argument("index_filename", help="Path of index file")

        suggest_parser = subparsers.add_parser("suggest")
        suggest_parser.add_argument("--add", default=False, action="store_true", help="Add suggested schemas to source code")
        suggest_parser.add_argument("spec", help="Github API OpenAPI spec file")
        suggest_parser.add_argument("index_filename", help="Path of index file")
        suggest_parser.add_argument("class_name", help="Name of the class to get suggestions for", nargs="?")

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
            self.index(self.args.github_path, self.args.index_filename, self.args.verbose)
        elif self.args.subcommand == "suggest":
            self.suggest(self.args.spec, self.args.index_filename, self.args.class_name, self.args.add, self.args.dry_run, self.args.verbose)
        elif self.args.subcommand == "apply":
            self.apply(self.args.spec, self.args.index_filename, self.args.class_name, self.args.dry_run, self.args.tests)
        else:
            raise RuntimeError("Subcommand not implemented " + args.subcommand)


if __name__ == "__main__":
    args = OpenApi.parse_args()
    OpenApi(args).main()
