# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

"""
All the configuration of how to use the GitHub API v3 is done by calling several methods
on a :class:`.Builder` object and finally calling its :meth:`.Builder.Build` method.

For example, you choose the authentication type by calling :meth:`.Builder.OAuth` or :meth:`.Builder.Login`.

A complete example::

    >>> import PyGithub

    >>> b = PyGithub.BlockingBuilder()
    >>> b.Login("your_login", "your_password")  # doctest: +ELLIPSIS
    <...Builder object at 0x...>
    >>> b.UserAgent("MyWonderfulApplication-1.0.0")  # doctest: +ELLIPSIS
    <...Builder object at 0x...>
    >>> g = b.Build()

Because all methods return the builder itself, you can chain calls::

    >>> g = PyGithub.BlockingBuilder().Login("your_login", "your_password").UserAgent("MyWonderfulApplication-1.0.0").Build()

For reference, see :class:`.Builder`.
"""

import PyGithub
import PyGithub.Blocking.Github
import PyGithub.Blocking._session as _session


class _AnonymousAuthenticator:
    def prepareSession(self, session):
        pass


class _LoginAuthenticator:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    def prepareSession(self, session):
        session.auth = (self.__login, self.__password)


class _OauthAuthenticator:
    def __init__(self, token):
        self.__token = token

    def prepareSession(self, session):
        session.headers["Authorization"] = "token " + self.__token


class Builder(object):
    """
    Class used to configure the GitHub session. See the :ref:`User Guide <configuration>` for an introduction.
    """

    defaultUserAgent = "jacquev6/PyGithub/" + PyGithub.Version

    def __init__(self):
        self.__authenticator = _AnonymousAuthenticator()
        self.__perPage = None
        self.__userAgent = Builder.defaultUserAgent

    def Login(self, login, password):
        """
        Use `basic authentication via username and password <http://developer.github.com/v3/auth/#via-username-and-password>`_.
        """
        self.__authenticator = _LoginAuthenticator(login, password)
        return self

    def OAuth(self, token):
        """
        Use `OAuth authentication <http://developer.github.com/v3/oauth/>`_.
        """
        self.__authenticator = _OauthAuthenticator(token)
        return self

    def PerPage(self, per_page):
        """
        Set the default `per_page` url argument for `paginated requests <http://developer.github.com/v3/#pagination>`_.
        """
        self.__perPage = per_page
        return self

    def UserAgent(self, user_agent):
        """
        Set the user agent sent by PyGithub to GitHub API v3. Defaults to "{0}".
        """
        self.__userAgent = user_agent
        return self
    UserAgent.__doc__ = UserAgent.__doc__.format(defaultUserAgent)

    def Build(self):
        """
        Build and return a new instance of :class:`.Github`.
        """
        return PyGithub.Blocking.Github.Github(
            _session.Session(self.__authenticator, self.__perPage, self.__userAgent),
            {}
        )
