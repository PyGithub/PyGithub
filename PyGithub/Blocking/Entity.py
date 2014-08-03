# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class Entity(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes:
      * :class:`.Organization`
      * :class:`.User`

    Methods and attributes returning instances of this class: none.

    Methods accepting instances of this class as parameter: none.
    """

    class Plan(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.Entity.plan`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, collaborators=None, name=None, private_repos=None, space=None, **kwds):
            super(Entity.Plan, self)._initAttributes(**kwds)
            self.__collaborators = _rcv.Attribute("Entity.Plan.collaborators", _rcv.IntConverter, collaborators)
            self.__name = _rcv.Attribute("Entity.Plan.name", _rcv.StringConverter, name)
            self.__private_repos = _rcv.Attribute("Entity.Plan.private_repos", _rcv.IntConverter, private_repos)
            self.__space = _rcv.Attribute("Entity.Plan.space", _rcv.IntConverter, space)

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

    def _initAttributes(self, avatar_url=_rcv.Absent, blog=_rcv.Absent, collaborators=_rcv.Absent, company=_rcv.Absent, created_at=_rcv.Absent, disk_usage=_rcv.Absent, email=_rcv.Absent, events_url=_rcv.Absent, followers=_rcv.Absent, following=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, location=_rcv.Absent, login=_rcv.Absent, name=_rcv.Absent, owned_private_repos=_rcv.Absent, plan=_rcv.Absent, private_gists=_rcv.Absent, public_gists=_rcv.Absent, public_repos=_rcv.Absent, repos_url=_rcv.Absent, total_private_repos=_rcv.Absent, type=_rcv.Absent, updated_at=_rcv.Absent, **kwds):
        super(Entity, self)._initAttributes(**kwds)
        self.__avatar_url = _rcv.Attribute("Entity.avatar_url", _rcv.StringConverter, avatar_url)
        self.__blog = _rcv.Attribute("Entity.blog", _rcv.StringConverter, blog)
        self.__collaborators = _rcv.Attribute("Entity.collaborators", _rcv.IntConverter, collaborators)
        self.__company = _rcv.Attribute("Entity.company", _rcv.StringConverter, company)
        self.__created_at = _rcv.Attribute("Entity.created_at", _rcv.DatetimeConverter, created_at)
        self.__disk_usage = _rcv.Attribute("Entity.disk_usage", _rcv.IntConverter, disk_usage)
        self.__email = _rcv.Attribute("Entity.email", _rcv.StringConverter, email)
        self.__events_url = _rcv.Attribute("Entity.events_url", _rcv.StringConverter, events_url)
        self.__followers = _rcv.Attribute("Entity.followers", _rcv.IntConverter, followers)
        self.__following = _rcv.Attribute("Entity.following", _rcv.IntConverter, following)
        self.__html_url = _rcv.Attribute("Entity.html_url", _rcv.StringConverter, html_url)
        self.__id = _rcv.Attribute("Entity.id", _rcv.IntConverter, id)
        self.__location = _rcv.Attribute("Entity.location", _rcv.StringConverter, location)
        self.__login = _rcv.Attribute("Entity.login", _rcv.StringConverter, login)
        self.__name = _rcv.Attribute("Entity.name", _rcv.StringConverter, name)
        self.__owned_private_repos = _rcv.Attribute("Entity.owned_private_repos", _rcv.IntConverter, owned_private_repos)
        self.__plan = _rcv.Attribute("Entity.plan", _rcv.StructureConverter(self.Session, Entity.Plan), plan)
        self.__private_gists = _rcv.Attribute("Entity.private_gists", _rcv.IntConverter, private_gists)
        self.__public_gists = _rcv.Attribute("Entity.public_gists", _rcv.IntConverter, public_gists)
        self.__public_repos = _rcv.Attribute("Entity.public_repos", _rcv.IntConverter, public_repos)
        self.__repos_url = _rcv.Attribute("Entity.repos_url", _rcv.StringConverter, repos_url)
        self.__total_private_repos = _rcv.Attribute("Entity.total_private_repos", _rcv.IntConverter, total_private_repos)
        self.__type = _rcv.Attribute("Entity.type", _rcv.StringConverter, type)
        self.__updated_at = _rcv.Attribute("Entity.updated_at", _rcv.DatetimeConverter, updated_at)

    def _updateAttributes(self, eTag, avatar_url=_rcv.Absent, blog=_rcv.Absent, collaborators=_rcv.Absent, company=_rcv.Absent, created_at=_rcv.Absent, disk_usage=_rcv.Absent, email=_rcv.Absent, events_url=_rcv.Absent, followers=_rcv.Absent, following=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, location=_rcv.Absent, login=_rcv.Absent, name=_rcv.Absent, owned_private_repos=_rcv.Absent, plan=_rcv.Absent, private_gists=_rcv.Absent, public_gists=_rcv.Absent, public_repos=_rcv.Absent, repos_url=_rcv.Absent, total_private_repos=_rcv.Absent, type=_rcv.Absent, updated_at=_rcv.Absent, **kwds):
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
        :type: :class:`.Entity.Plan`
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
