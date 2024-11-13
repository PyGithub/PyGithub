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

import argparse
import dataclasses
import difflib
import json
import sys
from argparse import Namespace
from typing import Sequence

import libcst as cst


@dataclasses.dataclass(frozen=True)
class Property:
    name: str
    data_type: str | None
    deprecated: bool


class ApplySchemaTransformer(cst.CSTTransformer):
    def __init__(self, class_name: str, properties: dict[str, (str | None, bool)], deprecate: bool):
        super().__init__()
        self.visit_class_name = []
        self.class_name = class_name
        self.properties = sorted([Property(name=k, data_type=v[0], deprecated=v[1]) for k, v in properties.items()], key=lambda p: p.name)
        self.all_properties = self.properties.copy()
        self.deprecate = deprecate

    @property
    def current_class_name(self) -> str:
        return ".".join(self.visit_class_name)

    @property
    def current_property(self) -> Property | None:
        if not self.properties:
            return None
        return self.properties[0]

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

    def visit_ClassDef(self, node: cst.ClassDef):
        self.visit_class_name.append(node.name.value)

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef):
        self.visit_class_name.pop()
        return updated_node

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

    @staticmethod
    def create_property_function(name: str, data_type: str | None, deprecated: bool) -> cst.FunctionDef:
        return cst.FunctionDef(
            decorators=[cst.Decorator(decorator=cst.Name(value="property"))],
            name=cst.Name(value=name),
            params=cst.Parameters(params=[cst.Param(cst.Name("self"))]),
            returns=cst.Annotation(annotation=cst.Name(value=data_type)) if data_type else None,
            body=cst.IndentedBlock(body=[
                cst.SimpleStatementLine(body=[
                    cst.Expr(cst.SimpleString(f'"""\n        :type: {data_type}\n        """'))
                ]),
                cst.SimpleStatementLine(body=[
                    cst.Expr(cst.Call(
                        func=cst.Attribute(value=cst.Name(value="self"), attr=cst.Name(value="_completeIfNotSet")),
                        args=[cst.Arg(cst.Attribute(value=cst.Name(value="self"), attr=cst.Name(value=f"_{name}")))]
                    ))
                ]),
                cst.SimpleStatementLine(body=[cst.Return(cst.Attribute(value=cst.Attribute(value=cst.Name(value="self"), attr=cst.Name(value=f"_{name}")), attr=cst.Name(value="value")))])
            ])
        )

    @staticmethod
    def create_type(data_type: str) -> cst.BaseExpression:
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
                slice=[cst.SubscriptElement(slice=cst.Index(cls.create_type(prop.data_type)))]
            )),
            value=cst.Name("NotSet")
        )])

    @staticmethod
    def make_attribute(prop: Property) -> cst.Call:
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
        elif prop.data_type == "list[int]":
            func_name = "_makeListOfIntAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type == "list[str]":
            func_name = "_makeListOfStringAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type == "str":
            func_name = "_makeStringAttribute"
            args = [cst.Arg(attr)]
        else:
            func_name = "_makeClassAttribute"
            args = [cst.Arg(cst.Name(prop.data_type or "None")), cst.Arg(attr)]
        return cst.Call(func=cst.Attribute(cst.Name("self"), cst.Name(func_name)), args=args)

    @classmethod
    def create_use_attr(cls, prop: Property) -> cst.BaseStatement:
        return cst.If(
                test=cst.Comparison(
                    left=cst.SimpleString(f'"{prop.name}"'),
                    comparisons=[cst.ComparisonTarget(operator=cst.In(), comparator=cst.Name("attributes"))]
                ),
                body=cst.IndentedBlock([
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

def as_python_type(data_type: str | None, format: str | None) -> str | None:
    if data_type is None:
        return None

    data_types = {
        "array": "list",
        "boolean": "bool",
        "integer": "int",
        "object": "GithubObject",
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
            return f"{maybe_with_format}[{as_python_type(format, None)}]"
        return maybe_with_format

    if format not in maybe_with_format:
        raise ValueError(f"Unsupported data type format: {format}")

    return maybe_with_format.get(format)

def apply(spec_file: str, schema_name: str, class_name: str, filename: str | None):
    print(f"Using spec {spec_file} for {schema_name} {class_name}")
    with open(spec_file, 'r') as r:
        spec = json.load(r)

    schemas = spec.get('components', {}).get('schemas', {})
    schema = schemas.get(schema_name, {})
    properties = {k: (as_python_type(v.get("type"), v.get("format") or v.get("items", {}).get("type") or v.get("items", {}).get("$ref")), v.get("deprecated", False)) for k, v in schema.get("properties", {}).items()}
    print(schema)
    print(properties)

    if filename is None:
        filename = f"github/{class_name}.py"
    with open(filename, "r") as r:
        code = "".join(r.readlines())

    tree = cst.parse_module(code)
    tree_updated = tree.visit(ApplySchemaTransformer(class_name, properties, deprecate=False))

    diff = difflib.unified_diff(code.splitlines(1), tree_updated.code.splitlines(1))
    print("Diff:")
    print("".join(diff))


def parse_args():
    args_parser = argparse.ArgumentParser(description="Applies OpenAPI spec to GithubObject classes")
    args_parser.add_argument("--dry-run", default=False, action="store_true", help="show prospect changes and do not modify any files")

    subparsers = args_parser.add_subparsers(dest="subcommand")
    apply_parser = subparsers.add_parser("apply")
    apply_parser.add_argument("spec", help="Github API OpenAPI spec file")
    apply_parser.add_argument("schema_name", help="Name of schema under /components/schemas/")
    apply_parser.add_argument("class_name", help="Python class name")
    apply_parser.add_argument("filename", nargs="?", help="Python file")

    if len(sys.argv) == 1:
        args_parser.print_help()
        sys.exit(1)
    return args_parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.subcommand == "apply":
        apply(args.spec, args.schema_name, args.class_name, args.filename)
