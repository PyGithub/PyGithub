# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>


class AnonymousAuthenticator:
    def prepareSession(self, session):
        pass


class LoginAuthenticator:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    def prepareSession(self, session):
        session.auth = (self.__login, self.__password)


class OauthAuthenticator:
    def __init__(self, token):
        self.__token = token

    def prepareSession(self, session):
        session.headers["Authorization"] = "token " + self.__token
