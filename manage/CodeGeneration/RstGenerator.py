# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>


class RstGenerator:
    def generateApis(self, endPoints):
        yield "From Github API v3 to PyGithub"
        yield "=============================="
        yield ""
        yield "Here are all the end points I'm aware of, and if/where they are implemented in PyGithub."
        yield "If something is not listed here, please `open an issue <http://github.com/jacquev6/PyGithub/issues>`__ with a link to the corresponding documentation of Github API v3."
        yield ""
        for endPoint in endPoints:
            title = endPoint.verb + " " + endPoint.url
            yield title
            yield "-" * len(title)
            yield ""
            yield "(`Reference documentation of Github API v3 <{}>`__)".format(endPoint.doc)
            yield ""
            if len(endPoint.methods) != 0:
                yield "Implemented in PyGithub by:"
                for method in endPoint.methods:
                    yield "  * :meth:`.{}.{}`".format(method.containerClass.name, method.name)
            else:
                yield "Not yet implemented in PyGithub."
            yield ""

    def generateClass(self, klass):
        yield klass.name
        yield "=" * len(klass.name)
        yield ""
        yield ".. automodule:: PyGithub.Blocking.{}".format(klass.name)
        yield ""
        yield ".. autoclass:: PyGithub.Blocking.{0}::{0}()".format(klass.name)
        yield "    :members:"
        if len(klass.structures) != 0:
            yield "    :exclude-members: {}".format(", ".join(struct.name for struct in klass.structures))  # pragma no branch
            yield ""
            for struct in klass.structures:
                yield "    .. autoclass:: PyGithub.Blocking.{0}::{0}.{1}()".format(klass.name, struct.name)
                yield "        :members:"
