# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import sys
assert sys.hexversion >= 0x03040000


class Call:
    def __init__(self, method):
        self.__method = method
        self.__args = []

    def arg(self, arg):
        # if not isinstance(arg, str):
        #     name, value = arg
        #     arg = name + "=" + value
        self.__args.append(arg)
        return self

    # def args(self, args):
    #     for arg in args:
    #         self.arg(arg)
    #     return self

    def __str__(self):
        return self.__method + "(" + ", ".join(self.__args) + ")"


def indent(gen):
    for line in gen:
        if line == "":
            yield line
        else:
            yield "    " + line


class DocString:
    def __init__(self, lines):
        self.__lines = list(lines)

    def __iter__(self):
        if len(self.__lines) != 0:
            yield '"""'
            yield from self.__lines
            yield '"""'


class DocstringContainer:
    def __init__(self):
        self.__docstring = []

    def docstring(self, *args):
        for arg in args:
            if isinstance(arg, str):
                self.__docstring.append(arg)
            else:
                self.__docstring += list(arg)
        return self

    def getDocstring(self):
        return DocString(self.__docstring)


class Class(DocstringContainer):
    def __init__(self, name):
        DocstringContainer.__init__(self)
        self.__name = name
        self.__base = None
        self.__elements = []

    def base(self, name):
        self.__base = name
        return self

    # def element(self, e):
    #     self.__elements.append(e)
    #     return self

    def elements(self, es):
        self.__elements += list(es)
        return self

    def __iter__(self):
        yield "class " + self.__name + "(" + self.__base + "):"
        yield from indent(self.getDocstring())
        for element in self.__elements:
            yield ""
            yield from indent(element)


class Function(DocstringContainer):
    def __init__(self, name):
        DocstringContainer.__init__(self)
        self.__name = name
        self.__decorators = []
        self.__parameters = []
        self.__body = []

    def decorator(self, d):
        self.__decorators.append(d)
        return self

    def parameter(self, p):
        if not isinstance(p, str):
            name, value = p
            p = name + "=" + value
        self.__parameters.append(p)
        return self

    def parameters(self, ps):
        for p in ps:
            self.parameter(p)
        return self

    def body(self, *args):
        for arg in args:
            if isinstance(arg, str):
                self.__body.append(arg)
            else:
                self.__body += list(arg)
        return self

    def __iter__(self):
        for d in self.__decorators:
            yield "@" + d
        yield "def " + self.__name + "(" + ", ".join(self.__parameters) + "):"
        yield from indent(self.getDocstring())
        yield from indent(self.__body)


class Method(Function):
    def __init__(self, name):
        Function.__init__(self, name)
        self.parameter("self")


class Property(Method):
    def __init__(self, name):
        Method.__init__(self, name)
        self.decorator("property")
