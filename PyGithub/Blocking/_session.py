# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import logging
log = logging.getLogger(__name__)
import json

import requests

import PyGithub.Blocking.Github
import PyGithub.Blocking._receive as rcv
import PyGithub.Blocking._exceptions as exn


class Session(object):
    """
    Class representing a GitHub API v3 session.

    Don't create any instance of this class yourself. Use :class:`.Builder` to get a :class:`.Github`
    and then access its :attr:`.SessionedGithubObject.Session` attribute (or on any returned object).
    """

    def __init__(self, authenticator, netloc, perPage, userAgent):
        self.__authenticator = authenticator
        self.__netloc = netloc
        self.__perPage = perPage
        self.__userAgent = userAgent
        self.__anonymousRequestsSession = requests.Session()
        self.__anonymousRequestsSession.headers["User-Agent"] = self.__userAgent
        self.__anonymousRequestsSession.headers["Accept"] = "application/vnd.github.v3.full+json"
        self.__requestsSession = requests.Session()
        self.__requestsSession.headers["User-Agent"] = self.__userAgent
        self.__requestsSession.headers["Accept"] = "application/vnd.github.v3.full+json"
        self.__authenticator.prepareSession(self.__requestsSession)
        self.__rate_limit = rcv.Attribute("RateLimit", rcv.StructureConverter(self, PyGithub.Blocking.Github.Github.RateLimits), rcv.Absent)
        self.__oauth_scopes = None
        self.__accepted_oauth_scopes = None

    @property
    def RateLimit(self):
        """
        The last rate limit information received from GitHub (through headers x-ratelimit-...).

        :type: :class:`.RateLimits`
        """
        if self.__rate_limit.needsLazyCompletion:
            self._request("GET", "https://api.github.com/rate_limit")
        return self.__rate_limit.value

    @property
    def OAuthScopes(self):
        """
        The last oauth scopes information received from GitHub (through header x-oauth-scopes).

        :type: ``None`` or :class:`list` of :class:`string`
        """
        return self.__oauth_scopes

    @property
    def AcceptedOAuthScopes(self):
        """
        The last accepted oauth scopes information received from GitHub (through header x-accepted-oauth-scopes).

        :type: ``None`` or :class:`list` of :class:`string`
        """
        return self.__accepted_oauth_scopes

    @property
    def PerPage(self):
        """
        The value of the per_page argument sent in all paginated requests.

        See also :class:`.PaginatedList`.

        :type: ``None`` or :class:`int`.
        """
        return self.__perPage

    def _request(self, *args, **kwds):
        return self.__request(self.__requestsSession, *args, **kwds)

    def _requestAnonymous(self, *args, **kwds):
        return self.__request(self.__anonymousRequestsSession, *args, **kwds)

    def __request(self, requestsSession, verb, url, urlArguments=None, postArguments=None, headers=None, accept404=False):
        # @todoAlpha Remove this hack, let classes know only about the path, and let Session decide about protocol and netloc
        if self.__netloc is not None and url.startswith("https://api.github.com/"):
            url = "http://" + self.__netloc + "/api/v3/" + url[23:]

        data = None
        if postArguments is not None:
            data = json.dumps(postArguments)
        if urlArguments is not None:
            for k, v in urlArguments.iteritems():
                if isinstance(v, bool):
                    if v:
                        urlArguments[k] = "true"
                    else:
                        urlArguments[k] = "false"

        request = requests.Request(verb, url, params=urlArguments, data=data, headers=headers)
        prepared_request = requestsSession.prepare_request(request)
        response = requestsSession.send(prepared_request)
        self.__logTransaction(prepared_request, response)

        # @todoAlpha Send PR to list PyGithubOAuthDemo in http://developer.github.com/v3/oauth_authorizations/#more-information

        limit = response.headers.get("x-ratelimit-limit")
        remaining = response.headers.get("x-ratelimit-remaining")
        reset = response.headers.get("x-ratelimit-reset")
        if limit is not None and remaining is not None and reset is not None:
            self.__rate_limit.update({
                "limit": int(limit),
                "remaining": int(remaining),
                "reset": int(reset),
            })

        self.__oauth_scopes = self.__parseScopesHeader(response.headers.get("x-oauth-scopes"))
        self.__accepted_oauth_scopes = self.__parseScopesHeader(response.headers.get("x-accepted-oauth-scopes"))

        status = response.status_code
        exceptionClass = None
        if status >= 400:
            exceptionClass = exn.ClientErrorException
            if status == 401:
                exceptionClass = exn.UnauthorizedException
            if status == 403:
                exceptionClass = exn.ForbiddenException
                if self.RateLimit.remaining == 0:  # @todoBeta Check rate_limiting for search queries
                    exceptionClass = exn.RateLimitExceededException
            if status == 404:
                exceptionClass = exn.ObjectNotFoundException
                if accept404:
                    exceptionClass = None
            if status == 405:
                exceptionClass = exn.MethodNotAllowedException
            if status == 409:
                exceptionClass = exn.ConflictException
            if status == 422:
                exceptionClass = exn.UnprocessableEntityException
        if status >= 500:
            exceptionClass = exn.ServerErrorException
        if exceptionClass is not None:
            raise exceptionClass(status, dict(response.headers), response.json())

        return response

    def __logTransaction(self, request, response):
        if log.isEnabledFor(logging.DEBUG):
            requestHeaders = dict(request.headers)
            if 'Authorization' in requestHeaders:
                auth = request.headers["Authorization"]
                if auth.startswith("Basic ") and auth.endswith("="):
                    requestHeaders["Authorization"] = "Basic not_logged="
                elif auth.startswith("token "):
                    requestHeaders["Authorization"] = "token not_logged"
                else:
                    requestHeaders["Authorization"] = "Unknown not_logged"  # pragma no cover (defensive programming)
            elements = [request.method, request.url, sorted(requestHeaders.iteritems()), request.body, "=>", response.status_code, sorted(response.headers.iteritems()), response.text]
            log.debug(" ".join(str(e) for e in elements))

    def __parseScopesHeader(self, header):
        if header is None:
            return None
        elif header == "":
            return []
        else:
            return header.split(", ")
