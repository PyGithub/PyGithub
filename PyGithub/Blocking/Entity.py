# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking._base_github_object as bgo
import PyGithub.Blocking._send as snd
import PyGithub.Blocking._receive as rcv


class Entity(bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes:
      * :class:`.Organization`
      * :class:`.User`

    Methods and attributes returning instances of this class: none.
    """

    class Plan(bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.Entity.plan`
        """

        def _initAttributes(self, collaborators=None, name=None, private_repos=None, space=None, **kwds):
            super(Entity.Plan, self)._initAttributes(**kwds)
            self.__collaborators = rcv.Attribute("Entity.Plan.collaborators", rcv.IntConverter, collaborators)
            self.__name = rcv.Attribute("Entity.Plan.name", rcv.StringConverter, name)
            self.__private_repos = rcv.Attribute("Entity.Plan.private_repos", rcv.IntConverter, private_repos)
            self.__space = rcv.Attribute("Entity.Plan.space", rcv.IntConverter, space)

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

    def _initAttributes(self, avatar_url=rcv.Absent, blog=rcv.Absent, collaborators=rcv.Absent, company=rcv.Absent, created_at=rcv.Absent, disk_usage=rcv.Absent, email=rcv.Absent, events_url=rcv.Absent, followers=rcv.Absent, following=rcv.Absent, html_url=rcv.Absent, id=rcv.Absent, location=rcv.Absent, login=rcv.Absent, name=rcv.Absent, owned_private_repos=rcv.Absent, plan=rcv.Absent, private_gists=rcv.Absent, public_gists=rcv.Absent, public_repos=rcv.Absent, repos_url=rcv.Absent, suspended_at=rcv.Absent, total_private_repos=rcv.Absent, type=rcv.Absent, updated_at=rcv.Absent, url=rcv.Absent, **kwds):
        super(Entity, self)._initAttributes(**kwds)
        self.__avatar_url = rcv.Attribute("Entity.avatar_url", rcv.StringConverter, avatar_url)
        self.__blog = rcv.Attribute("Entity.blog", rcv.StringConverter, blog)
        self.__collaborators = rcv.Attribute("Entity.collaborators", rcv.IntConverter, collaborators)
        self.__company = rcv.Attribute("Entity.company", rcv.StringConverter, company)
        self.__created_at = rcv.Attribute("Entity.created_at", rcv.DatetimeConverter, created_at)
        self.__disk_usage = rcv.Attribute("Entity.disk_usage", rcv.IntConverter, disk_usage)
        self.__email = rcv.Attribute("Entity.email", rcv.StringConverter, email)
        self.__events_url = rcv.Attribute("Entity.events_url", rcv.StringConverter, events_url)
        self.__followers = rcv.Attribute("Entity.followers", rcv.IntConverter, followers)
        self.__following = rcv.Attribute("Entity.following", rcv.IntConverter, following)
        self.__html_url = rcv.Attribute("Entity.html_url", rcv.StringConverter, html_url)
        self.__id = rcv.Attribute("Entity.id", rcv.IntConverter, id)
        self.__location = rcv.Attribute("Entity.location", rcv.StringConverter, location)
        self.__login = rcv.Attribute("Entity.login", rcv.StringConverter, login)
        self.__name = rcv.Attribute("Entity.name", rcv.StringConverter, name)
        self.__owned_private_repos = rcv.Attribute("Entity.owned_private_repos", rcv.IntConverter, owned_private_repos)
        self.__plan = rcv.Attribute("Entity.plan", rcv.StructureConverter(self.Session, Entity.Plan), plan)
        self.__private_gists = rcv.Attribute("Entity.private_gists", rcv.IntConverter, private_gists)
        self.__public_gists = rcv.Attribute("Entity.public_gists", rcv.IntConverter, public_gists)
        self.__public_repos = rcv.Attribute("Entity.public_repos", rcv.IntConverter, public_repos)
        self.__repos_url = rcv.Attribute("Entity.repos_url", rcv.StringConverter, repos_url)
        self.__suspended_at = rcv.Attribute("Entity.suspended_at", rcv.DatetimeConverter, suspended_at)
        self.__total_private_repos = rcv.Attribute("Entity.total_private_repos", rcv.IntConverter, total_private_repos)
        self.__type = rcv.Attribute("Entity.type", rcv.StringConverter, type)
        self.__updated_at = rcv.Attribute("Entity.updated_at", rcv.DatetimeConverter, updated_at)
        self.__url = rcv.Attribute("Entity.url", rcv.StringConverter, url)

    def _updateAttributes(self, eTag, avatar_url=rcv.Absent, blog=rcv.Absent, collaborators=rcv.Absent, company=rcv.Absent, created_at=rcv.Absent, disk_usage=rcv.Absent, email=rcv.Absent, events_url=rcv.Absent, followers=rcv.Absent, following=rcv.Absent, html_url=rcv.Absent, id=rcv.Absent, location=rcv.Absent, login=rcv.Absent, name=rcv.Absent, owned_private_repos=rcv.Absent, plan=rcv.Absent, private_gists=rcv.Absent, public_gists=rcv.Absent, public_repos=rcv.Absent, repos_url=rcv.Absent, suspended_at=rcv.Absent, total_private_repos=rcv.Absent, type=rcv.Absent, updated_at=rcv.Absent, url=rcv.Absent, **kwds):
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
        self.__suspended_at.update(suspended_at)
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
    def suspended_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__suspended_at.needsLazyCompletion)
        return self.__suspended_at.value

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
