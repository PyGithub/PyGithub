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
from json import JSONEncoder
from os import listdir
from os.path import isfile, join
from typing import Sequence, Optional, Any

import libcst as cst
from libcst import SimpleStatementLine, Expr, IndentedBlock, SimpleString, Module


@dataclasses.dataclass(frozen=True)
class GithubClass:
    package: str
    module: str
    name: str
    filename: str
    bases: list[str]
    inheritance: list[str]
    schemas: list[str]
    docstring: str

    def __hash__(self):
        return hash((self.package, self.module, self.name))

@dataclasses.dataclass(frozen=True)
class Property:
    name: str
    data_type: str | GithubClass | None
    deprecated: bool


class IndexPythonClassesVisitor(cst.CSTVisitor):
    def __init__(self):
        super().__init__()
        self._module = None
        self._package = None
        self._filename = None
        self._classes = {}

    def module(self, module: str):
        self._module = module

    def package(self, package: str):
        self._package = package

    def filename(self, filename: str):
        self._filename = filename

    @property
    def classes(self) -> dict[str, Any]:
        return self._classes

    def visit_ClassDef(self, node: cst.ClassDef) -> Optional[bool]:
        class_name = node.name.value
        class_docstring = None
        class_schemas = []
        class_bases = [val if isinstance(val, str) else Module([]).code_for_node(val)
                       for base in node.bases for val in [base.value.value]]

        # extract class docstring
        try:
            if (isinstance(node.body, IndentedBlock) and
                    isinstance(node.body.body[0], SimpleStatementLine) and
                    isinstance(node.body.body[0].body[0], Expr) and
                    isinstance(node.body.body[0].body[0].value, SimpleString)):
                class_docstring = node.body.body[0].body[0].value.value.strip('"\r\n ')
        except Exception as e:
            print(f"Extracting docstring of class {class_name} failed", e)

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
        }
        return False


class ApplySchemaTransformer(cst.CSTTransformer):
    def __init__(self, module_name: str, class_name: str, properties: dict[str, (str | dict | None, bool)], deprecate: bool):
        super().__init__()
        self.visit_class_name = []
        self.module_name = module_name
        self.class_name = class_name
        self.properties = sorted([Property(name=k, data_type=GithubClass(**v[0]) if isinstance(v[0], dict) else v[0], deprecated=v[1])
                                  for k, v in properties.items()],
                                 key=lambda p: p.name)
        self.all_properties = self.properties.copy()
        self.deprecate = deprecate

    @property
    def current_class_name(self) -> str:
        return ".".join(self.visit_class_name)

    @property
    def current_property(self) -> Property | GithubClass | None:
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
                    cst.Expr(cst.SimpleString(f'"""\n        :type: {docstring_type}\n        """'))
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
    def create_type(data_type: str | GithubClass, short_class_name: bool = False) -> cst.BaseExpression:
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
        elif prop.data_type == "list[int]":
            func_name = "_makeListOfIntAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type == "list[str]":
            func_name = "_makeListOfStringAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type == "list[None]":
            func_name = "_makeListOfClassAttribute"
            args = [cst.Arg(attr)]
        elif prop.data_type == "str":
            func_name = "_makeStringAttribute"
            args = [cst.Arg(attr)]
        elif isinstance(prop.data_type, GithubClass):
            func_name = "_makeClassAttribute"
            args = [cst.Arg(cls.create_type(prop.data_type)), cst.Arg(attr)]
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
        self.schema_to_class['default'] = "GithubObject"

    @staticmethod
    def read_index(filename: str) -> dict[str, Any]:
        with open(filename, 'r') as r:
            return json.load(r)

    def as_python_type(self, data_type: str | None, format: str | None) -> str | None:
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

        if isinstance(maybe_with_format.get(format), dict):
            pass

        python_type = maybe_with_format.get(format, maybe_with_format.get('default'))
        if data_type == "object":
            return self.classes.get(python_type, python_type)

    def apply(self, spec_file: str, schema_name: str, class_name: str, filename: str | None, dry_run: bool):
        print(f"Using spec {spec_file} for {schema_name} {class_name}")
        with open(spec_file, 'r') as r:
            spec = json.load(r)

        schemas = spec.get('components', {}).get('schemas', {})
        schema = schemas.get(schema_name, {})
        properties = {k: (self.as_python_type(v.get("type") or "object", v.get("format") or v.get("$ref", "").strip("# ") or v.get("items", {}).get("type") or v.get("items", {}).get("$ref")), v.get("deprecated", False)) for k, v in schema.get("properties", {}).items()}

        if filename is None:
            filename = f"github/{class_name}.py"
        with open(filename, "r") as r:
            code = "".join(r.readlines())

        tree = cst.parse_module(code)
        tree_updated = tree.visit(ApplySchemaTransformer(class_name, class_name, properties, deprecate=False))

        if dry_run:
            diff = difflib.unified_diff(code.splitlines(1), tree_updated.code.splitlines(1))
            print("Diff:")
            print("".join(diff))
        else:
            if not tree_updated.deep_equals(tree):
                with open(filename, "w") as w:
                    w.write(tree_updated.code)


    def extend_inheritance(self, classes: dict[str, Any]) -> bool:
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

    def index(self, github_path: str, index_filename: str):
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

        # construct schema-to-class index
        schema_to_classes = {}
        for name, cls in classes.items():
            for schema in cls.get("schemas"):
                if schema in schema_to_classes:
                    print(f"Multiple classes for schema found: {name} and {schema_to_classes[schema]}")
                schema_to_classes[schema] = name

        print(f"Indexed {len(classes)} classes")
        print(f"Indexed {len([cls for cls in classes.values() if cls.get('schema')])} schemas")

        data = {
            "sources": github_path,
            "classes": classes,
            "indices": {
                "schema_to_classes": schema_to_classes,
            }
        }

        with open(index_filename, "w") as w:
            json.dump(data, w, indent=2, sort_keys=True, ensure_ascii=False, cls=JsonSerializer)

    @staticmethod
    def parse_args():
        args_parser = argparse.ArgumentParser(description="Applies OpenAPI spec to GithubObject classes")
        args_parser.add_argument("--index-filename", help="filename of the index file")
        args_parser.add_argument("--dry-run", default=False, action="store_true", help="show prospect changes and do not modify any files")

        subparsers = args_parser.add_subparsers(dest="subcommand")
        apply_parser = subparsers.add_parser("apply")
        apply_parser.add_argument("spec", help="Github API OpenAPI spec file")
        apply_parser.add_argument("schema_name", help="Name of schema under /components/schemas/")
        apply_parser.add_argument("class_name", help="Python class name")
        apply_parser.add_argument("filename", nargs="?", help="Python file")

        index_parser = subparsers.add_parser("index")
        index_parser.add_argument("github_path", help="Path to Github Python files")
        index_parser.add_argument("index_filename", help="Path of index file")

        if len(sys.argv) == 1:
            args_parser.print_help()
            sys.exit(1)
        return args_parser.parse_args()

    def main(self):
        if self.args.subcommand == "apply":
            self.apply(self.args.spec, self.args.schema_name, self.args.class_name, self.args.filename, self.args.dry_run)
        elif args.subcommand == "index":
            self.index(self.args.github_path, self.args.index_filename)
        else:
            raise RuntimeError("Subcommand not implemented " + args.subcommand)


if __name__ == "__main__":
    args = OpenApi.parse_args()
    OpenApi(args).main()
