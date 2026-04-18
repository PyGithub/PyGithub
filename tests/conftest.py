############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Matthew Neal <meneal@matthews-mbp.raleigh.ibm.com>            #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2016 Sam Corbett <sam.corbett@cloudsoftcorp.com>                   #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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
import typing
from sys import modules

import niquests
from niquests.packages import urllib3

# responses is tied to Requests
# and Niquests is entirely compatible with it.
# we can fool it without effort.
modules["requests"] = niquests
modules["requests.adapters"] = niquests.adapters
modules["requests.models"] = niquests.models
modules["requests.exceptions"] = niquests.exceptions
modules["requests.packages.urllib3"] = urllib3

# make 'responses' mock both sync and async
# 'Requests' ever only supported sync
# Fortunately interfaces are mirrored in 'Niquests'
from unittest import mock as std_mock  # noqa: E402

import responses  # noqa: E402

from . import Framework  # noqa: E402


class NiquestsMock(responses.RequestsMock):
    """
    Asynchronous support for responses.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(  # type: ignore[misc]
            *args,
            target="niquests.adapters.HTTPAdapter.send",
            **kwargs,
        )

        self._patcher_async = None

    def unbound_on_async_send(self):
        async def send(
            adapter: "niquests.adapters.AsyncHTTPAdapter",
            request: "niquests.PreparedRequest",
            *args: typing.Any,
            **kwargs: typing.Any,
        ) -> "niquests.Response":
            if args:
                # that probably means that the request was sent from the custom adapter
                # It is fully legit to send positional args from adapter, although,
                # `requests` implementation does it always with kwargs
                # See for more info: https://github.com/getsentry/responses/issues/642
                try:
                    kwargs["stream"] = args[0]
                    kwargs["timeout"] = args[1]
                    kwargs["verify"] = args[2]
                    kwargs["cert"] = args[3]
                    kwargs["proxies"] = args[4]
                except IndexError:
                    # not all kwargs are required
                    pass

            resp = self._on_request(adapter, request, **kwargs)  # type: ignore[arg-type]

            if kwargs["stream"]:
                return resp  # type: ignore[return-value]

            resp.__class__ = niquests.Response  # type: ignore[assignment]
            return resp  # type: ignore[return-value]

        return send

    def unbound_on_send(self):
        def send(
            adapter: "niquests.adapters.HTTPAdapter",
            request: "niquests.PreparedRequest",
            *args: typing.Any,
            **kwargs: typing.Any,
        ) -> "niquests.Response":
            if args:
                # that probably means that the request was sent from the custom adapter
                # It is fully legit to send positional args from adapter, although,
                # `requests` implementation does it always with kwargs
                # See for more info: https://github.com/getsentry/responses/issues/642
                try:
                    kwargs["stream"] = args[0]
                    kwargs["timeout"] = args[1]
                    kwargs["verify"] = args[2]
                    kwargs["cert"] = args[3]
                    kwargs["proxies"] = args[4]
                except IndexError:
                    # not all kwargs are required
                    pass

            return self._on_request(adapter, request, **kwargs)  # type: ignore[arg-type,return-value]

        return send

    def start(self) -> None:
        if self._patcher:  # type: ignore[has-type]
            # we must not override value of the _patcher if already applied
            # this prevents issues when one decorated function is called from
            # another decorated function
            return

        self._patcher = std_mock.patch(target=self.target, new=self.unbound_on_send())
        self._patcher_async = std_mock.patch(  # type: ignore[assignment]
            target=self.target.replace("HTTPAdapter", "AsyncHTTPAdapter"), new=self.unbound_on_async_send()
        )

        self._patcher.start()
        self._patcher_async.start()  # type: ignore[attr-defined]

    def stop(self, allow_assert: bool = True) -> None:
        if self._patcher:
            # prevent stopping unstarted patchers
            self._patcher.stop()
            self._patcher_async.stop()  # type: ignore[attr-defined]

            # once patcher is stopped, clean it. This is required to create a new
            # fresh patcher on self.start()
            self._patcher = None  # type: ignore[assignment]
            self._patcher_async = None

        if not self.assert_all_requests_are_fired:
            return

        if not allow_assert:
            return

        not_called = [m for m in self.registered() if m.call_count == 0]
        if not_called:
            raise AssertionError(
                f"Not all requests have been executed {[(match.method, match.url) for match in not_called]!r}"
            )


mock = _default_mock = NiquestsMock(assert_all_requests_are_fired=False)

setattr(responses, "mock", mock)
setattr(responses, "_default_mock", _default_mock)

for kw in [
    "activate",
    "add",
    "_add_from_file",
    "add_callback",
    "add_passthru",
    "assert_call_count",
    "calls",
    "delete",
    "DELETE",
    "get",
    "GET",
    "head",
    "HEAD",
    "options",
    "OPTIONS",
    "patch",
    "PATCH",
    "post",
    "POST",
    "put",
    "PUT",
    "registered",
    "remove",
    "replace",
    "reset",
    "response_callback",
    "start",
    "stop",
    "upsert",
]:
    if not hasattr(responses, kw):
        continue
    setattr(responses, kw, getattr(mock, kw))


def pytest_addoption(parser):
    parser.addoption("--record", action="store_true", help="record mode")


def pytest_configure(config):
    if config.getoption("record"):
        Framework.activateRecordMode()
