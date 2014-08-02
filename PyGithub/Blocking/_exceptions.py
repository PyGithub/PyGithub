# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

"""
Error handling in PyGithub is done with exceptions. All exceptions derive (indireclty) from
:class:`PyGithubException`.

@todoSomeday generate the exception hierarchy graph
"""


class PyGithubException(Exception):
    """
    Base class for all exceptions raised by PyGithub.
    """


class BadAttributeException(PyGithubException):
    """
    Raised when GitHub API v3 returns an attribute that doesn't match the expected type or format.
    """


class ClientErrorException(PyGithubException):
    """
    Base class for exceptions raised by PyGithub when GitHub API v3 returns a 4XX HTTP status code.
    """


class ObjectNotFoundException(ClientErrorException):
    """
    Raised by PyGithub when GitHub API v3 returns an unexpected 404 HTTP status code.
    """


class MethodNotAllowedException(ClientErrorException):
    """
    Raised by PyGithub when GitHub API v3 returns a 405 HTTP status code. For example when :meth:`.PullRequest.merge` is called and :attr:`.PullRequest.meargeable` was false.
    """


class ConflictException(ClientErrorException):
    """
    Raised by PyGithub when GitHub API v3 returns a 409 HTTP status code. For example when there is a conflict in :meth:`.Repository.merge`.
    """


class UnauthorizedException(ClientErrorException):
    """
    Raised by PyGithub when GitHub API v3 returns a 401 HTTP status code.
    """


class ForbiddenException(ClientErrorException):
    """
    Base class for exceptions raised by PyGithub when GitHub API v3 returns a 403 HTTP status code.
    """


class RateLimitExceededException(ForbiddenException):
    """
    Raised by PyGithub when GitHub API v3 returns a 403 HTTP status code and the remaining rate limit is null.
    """


class UnprocessableEntityException(ClientErrorException):
    """
    Base class for exceptions raised by PyGithub when GitHub API v3 returns a 422 HTTP status code.
    """


class ServerErrorException(PyGithubException):
    """
    Base class for exceptions raised by PyGithub when GitHub API v3 returns a 5XX HTTP status code.
    """
