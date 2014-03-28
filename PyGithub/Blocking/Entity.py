# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

########################################################################
###### This file is generated. Manual changes will likely be lost. #####
########################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking.BaseGithubObject
import PyGithub.Blocking.Parameters
import PyGithub.Blocking.Attributes


class Entity(PyGithub.Blocking.BaseGithubObject.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes:
      * :class:`.Organization`
      * :class:`.User`

    Methods and attributes returning instances of this class: none.
    """

    class Plan(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.Entity.plan`
        """

        def _initAttributes(self, collaborators=None, name=None, private_repos=None, space=None, **kwds):
            super(Entity.Plan, self)._initAttributes(**kwds)
            self.__collaborators = PyGithub.Blocking.Attributes.Attribute("Entity.Plan.collaborators", PyGithub.Blocking.Attributes.IntConverter, collaborators)
            self.__name = PyGithub.Blocking.Attributes.Attribute("Entity.Plan.name", PyGithub.Blocking.Attributes.StringConverter, name)
            self.__private_repos = PyGithub.Blocking.Attributes.Attribute("Entity.Plan.private_repos", PyGithub.Blocking.Attributes.IntConverter, private_repos)
            self.__space = PyGithub.Blocking.Attributes.Attribute("Entity.Plan.space", PyGithub.Blocking.Attributes.IntConverter, space)

        def _updateAttributes(self, collaborators=None, name=None, private_repos=None, space=None, **kwds):
            super(Entity.Plan, self)._updateAttributes(**kwds)
            self.__collaborators.update(collaborators)
            self.__name.update(name)
            self.__private_repos.update(private_repos)
            self.__space.update(space)

        @property
        def collaborators(self):
            """
            :type: :class:`int`
            """
            return self.__collaborators.value

        @property
        def name(self):
            """
            :type: :class:`string`
            """
            return self.__name.value

        @property
        def private_repos(self):
            """
            :type: :class:`int`
            """
            return self.__private_repos.value

        @property
        def space(self):
            """
            :type: :class:`int`
            """
            return self.__space.value

    def _initAttributes(self, avatar_url=PyGithub.Blocking.Attributes.Absent, blog=PyGithub.Blocking.Attributes.Absent, collaborators=PyGithub.Blocking.Attributes.Absent, company=PyGithub.Blocking.Attributes.Absent, created_at=PyGithub.Blocking.Attributes.Absent, disk_usage=PyGithub.Blocking.Attributes.Absent, email=PyGithub.Blocking.Attributes.Absent, events_url=PyGithub.Blocking.Attributes.Absent, followers=PyGithub.Blocking.Attributes.Absent, following=PyGithub.Blocking.Attributes.Absent, html_url=PyGithub.Blocking.Attributes.Absent, id=PyGithub.Blocking.Attributes.Absent, location=PyGithub.Blocking.Attributes.Absent, login=PyGithub.Blocking.Attributes.Absent, name=PyGithub.Blocking.Attributes.Absent, owned_private_repos=PyGithub.Blocking.Attributes.Absent, plan=PyGithub.Blocking.Attributes.Absent, private_gists=PyGithub.Blocking.Attributes.Absent, public_gists=PyGithub.Blocking.Attributes.Absent, public_repos=PyGithub.Blocking.Attributes.Absent, repos_url=PyGithub.Blocking.Attributes.Absent, total_private_repos=PyGithub.Blocking.Attributes.Absent, type=PyGithub.Blocking.Attributes.Absent, updated_at=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, **kwds):
        super(Entity, self)._initAttributes(**kwds)
        self.__avatar_url = PyGithub.Blocking.Attributes.Attribute("Entity.avatar_url", PyGithub.Blocking.Attributes.StringConverter, avatar_url)
        self.__blog = PyGithub.Blocking.Attributes.Attribute("Entity.blog", PyGithub.Blocking.Attributes.StringConverter, blog)
        self.__collaborators = PyGithub.Blocking.Attributes.Attribute("Entity.collaborators", PyGithub.Blocking.Attributes.IntConverter, collaborators)
        self.__company = PyGithub.Blocking.Attributes.Attribute("Entity.company", PyGithub.Blocking.Attributes.StringConverter, company)
        self.__created_at = PyGithub.Blocking.Attributes.Attribute("Entity.created_at", PyGithub.Blocking.Attributes.DatetimeConverter, created_at)
        self.__disk_usage = PyGithub.Blocking.Attributes.Attribute("Entity.disk_usage", PyGithub.Blocking.Attributes.IntConverter, disk_usage)
        self.__email = PyGithub.Blocking.Attributes.Attribute("Entity.email", PyGithub.Blocking.Attributes.StringConverter, email)
        self.__events_url = PyGithub.Blocking.Attributes.Attribute("Entity.events_url", PyGithub.Blocking.Attributes.StringConverter, events_url)
        self.__followers = PyGithub.Blocking.Attributes.Attribute("Entity.followers", PyGithub.Blocking.Attributes.IntConverter, followers)
        self.__following = PyGithub.Blocking.Attributes.Attribute("Entity.following", PyGithub.Blocking.Attributes.IntConverter, following)
        self.__html_url = PyGithub.Blocking.Attributes.Attribute("Entity.html_url", PyGithub.Blocking.Attributes.StringConverter, html_url)
        self.__id = PyGithub.Blocking.Attributes.Attribute("Entity.id", PyGithub.Blocking.Attributes.IntConverter, id)
        self.__location = PyGithub.Blocking.Attributes.Attribute("Entity.location", PyGithub.Blocking.Attributes.StringConverter, location)
        self.__login = PyGithub.Blocking.Attributes.Attribute("Entity.login", PyGithub.Blocking.Attributes.StringConverter, login)
        self.__name = PyGithub.Blocking.Attributes.Attribute("Entity.name", PyGithub.Blocking.Attributes.StringConverter, name)
        self.__owned_private_repos = PyGithub.Blocking.Attributes.Attribute("Entity.owned_private_repos", PyGithub.Blocking.Attributes.IntConverter, owned_private_repos)
        self.__plan = PyGithub.Blocking.Attributes.Attribute("Entity.plan", PyGithub.Blocking.Attributes.StructureConverter(self.Session, Entity.Plan), plan)
        self.__private_gists = PyGithub.Blocking.Attributes.Attribute("Entity.private_gists", PyGithub.Blocking.Attributes.IntConverter, private_gists)
        self.__public_gists = PyGithub.Blocking.Attributes.Attribute("Entity.public_gists", PyGithub.Blocking.Attributes.IntConverter, public_gists)
        self.__public_repos = PyGithub.Blocking.Attributes.Attribute("Entity.public_repos", PyGithub.Blocking.Attributes.IntConverter, public_repos)
        self.__repos_url = PyGithub.Blocking.Attributes.Attribute("Entity.repos_url", PyGithub.Blocking.Attributes.StringConverter, repos_url)
        self.__total_private_repos = PyGithub.Blocking.Attributes.Attribute("Entity.total_private_repos", PyGithub.Blocking.Attributes.IntConverter, total_private_repos)
        self.__type = PyGithub.Blocking.Attributes.Attribute("Entity.type", PyGithub.Blocking.Attributes.StringConverter, type)
        self.__updated_at = PyGithub.Blocking.Attributes.Attribute("Entity.updated_at", PyGithub.Blocking.Attributes.DatetimeConverter, updated_at)
        self.__url = PyGithub.Blocking.Attributes.Attribute("Entity.url", PyGithub.Blocking.Attributes.StringConverter, url)

    def _updateAttributes(self, eTag, avatar_url=PyGithub.Blocking.Attributes.Absent, blog=PyGithub.Blocking.Attributes.Absent, collaborators=PyGithub.Blocking.Attributes.Absent, company=PyGithub.Blocking.Attributes.Absent, created_at=PyGithub.Blocking.Attributes.Absent, disk_usage=PyGithub.Blocking.Attributes.Absent, email=PyGithub.Blocking.Attributes.Absent, events_url=PyGithub.Blocking.Attributes.Absent, followers=PyGithub.Blocking.Attributes.Absent, following=PyGithub.Blocking.Attributes.Absent, html_url=PyGithub.Blocking.Attributes.Absent, id=PyGithub.Blocking.Attributes.Absent, location=PyGithub.Blocking.Attributes.Absent, login=PyGithub.Blocking.Attributes.Absent, name=PyGithub.Blocking.Attributes.Absent, owned_private_repos=PyGithub.Blocking.Attributes.Absent, plan=PyGithub.Blocking.Attributes.Absent, private_gists=PyGithub.Blocking.Attributes.Absent, public_gists=PyGithub.Blocking.Attributes.Absent, public_repos=PyGithub.Blocking.Attributes.Absent, repos_url=PyGithub.Blocking.Attributes.Absent, total_private_repos=PyGithub.Blocking.Attributes.Absent, type=PyGithub.Blocking.Attributes.Absent, updated_at=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, **kwds):
        super(Entity, self)._updateAttributes(eTag, **kwds)
        self.__avatar_url.update(avatar_url)
        self.__blog.update(blog)
        self.__collaborators.update(collaborators)
        self.__company.update(company)
        self.__created_at.update(created_at)
        self.__disk_usage.update(disk_usage)
        self.__email.update(email)
        self.__events_url.update(events_url)
        self.__followers.update(followers)
        self.__following.update(following)
        self.__html_url.update(html_url)
        self.__id.update(id)
        self.__location.update(location)
        self.__login.update(login)
        self.__name.update(name)
        self.__owned_private_repos.update(owned_private_repos)
        self.__plan.update(plan)
        self.__private_gists.update(private_gists)
        self.__public_gists.update(public_gists)
        self.__public_repos.update(public_repos)
        self.__repos_url.update(repos_url)
        self.__total_private_repos.update(total_private_repos)
        self.__type.update(type)
        self.__updated_at.update(updated_at)
        self.__url.update(url)

    @property
    def avatar_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__avatar_url.needsLazyCompletion)
        return self.__avatar_url.value

    @property
    def blog(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__blog.needsLazyCompletion)
        return self.__blog.value

    @property
    def collaborators(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__collaborators.needsLazyCompletion)
        return self.__collaborators.value

    @property
    def company(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__company.needsLazyCompletion)
        return self.__company.value

    @property
    def created_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__created_at.needsLazyCompletion)
        return self.__created_at.value

    @property
    def disk_usage(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__disk_usage.needsLazyCompletion)
        return self.__disk_usage.value

    @property
    def email(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__email.needsLazyCompletion)
        return self.__email.value

    @property
    def events_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__events_url.needsLazyCompletion)
        return self.__events_url.value

    @property
    def followers(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__followers.needsLazyCompletion)
        return self.__followers.value

    @property
    def following(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__following.needsLazyCompletion)
        return self.__following.value

    @property
    def html_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__html_url.needsLazyCompletion)
        return self.__html_url.value

    @property
    def id(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__id.needsLazyCompletion)
        return self.__id.value

    @property
    def location(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__location.needsLazyCompletion)
        return self.__location.value

    @property
    def login(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__login.needsLazyCompletion)
        return self.__login.value

    @property
    def name(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__name.needsLazyCompletion)
        return self.__name.value

    @property
    def owned_private_repos(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__owned_private_repos.needsLazyCompletion)
        return self.__owned_private_repos.value

    @property
    def plan(self):
        """
        :type: :class:`.Plan`
        """
        self._completeLazily(self.__plan.needsLazyCompletion)
        return self.__plan.value

    @property
    def private_gists(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__private_gists.needsLazyCompletion)
        return self.__private_gists.value

    @property
    def public_gists(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__public_gists.needsLazyCompletion)
        return self.__public_gists.value

    @property
    def public_repos(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__public_repos.needsLazyCompletion)
        return self.__public_repos.value

    @property
    def repos_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__repos_url.needsLazyCompletion)
        return self.__repos_url.value

    @property
    def total_private_repos(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__total_private_repos.needsLazyCompletion)
        return self.__total_private_repos.value

    @property
    def type(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__type.needsLazyCompletion)
        return self.__type.value

    @property
    def updated_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__updated_at.needsLazyCompletion)
        return self.__updated_at.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value
