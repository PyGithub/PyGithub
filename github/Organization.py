# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Steve English <steve.english@navetas.com>                     #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Sebastien Besson <seb.besson@gmail.com>                       #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Matthew Neal <meneal@matthews-mbp.raleigh.ibm.com>            #
# Copyright 2016 Michael Pereira <pereira.m@gmail.com>                         #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Balázs Rostás <rostas.balazs@gmail.com>                     #
# Copyright 2018 Anton Nguyen <afnguyen85@gmail.com>                           #
# Copyright 2018 Jacopo Notarstefano <jacopo.notarstefano@gmail.com>           #
# Copyright 2018 Jasper van Wanrooy <jasper@vanwanrooy.net>                    #
# Copyright 2018 Raihaan <31362124+res0nance@users.noreply.github.com>         #
# Copyright 2018 Tim Boring <tboring@hearst.com>                               #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
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

import datetime
import json

import github.GithubObject
import github.PaginatedList

import github.Plan
import github.Team
import github.Event
import github.Repository
import github.Project
import github.NamedUser

import Consts

class Organization(github.GithubObject.CompletableGithubObject):
    """
    This class represents Organizations. The reference can be found here http://developer.github.com/v3/orgs/
    """

    def __repr__(self):
        return self.get__repr__({"login": self._login.value})

    @property
    def avatar_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._avatar_url)
        return self._avatar_url.value

    @property
    def billing_email(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._billing_email)
        return self._billing_email.value

    @property
    def blog(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._blog)
        return self._blog.value

    @property
    def collaborators(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._collaborators)
        return self._collaborators.value

    @property
    def company(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._company)
        return self._company.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def description(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def disk_usage(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._disk_usage)
        return self._disk_usage.value

    @property
    def email(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._email)
        return self._email.value

    @property
    def events_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._events_url)
        return self._events_url.value

    @property
    def followers(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._followers)
        return self._followers.value

    @property
    def following(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._following)
        return self._following.value

    @property
    def gravatar_id(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._gravatar_id)
        return self._gravatar_id.value

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def location(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._location)
        return self._location.value

    @property
    def login(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._login)
        return self._login.value

    @property
    def members_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._members_url)
        return self._members_url.value

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def owned_private_repos(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._owned_private_repos)
        return self._owned_private_repos.value

    @property
    def plan(self):
        """
        :type: :class:`github.Plan.Plan`
        """
        self._completeIfNotSet(self._plan)
        return self._plan.value

    @property
    def private_gists(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._private_gists)
        return self._private_gists.value

    @property
    def public_gists(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._public_gists)
        return self._public_gists.value

    @property
    def public_members_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._public_members_url)
        return self._public_members_url.value

    @property
    def public_repos(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._public_repos)
        return self._public_repos.value

    @property
    def repos_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._repos_url)
        return self._repos_url.value

    @property
    def total_private_repos(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._total_private_repos)
        return self._total_private_repos.value

    @property
    def type(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._type)
        return self._type.value

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    def add_to_members(self, member, role=github.GithubObject.NotSet):
        """
        :calls: `PUT /orgs/:org/memberships/:user <https://developer.github.com/v3/orgs/members/#add-or-update-organization-membership>`_
        :param member: :class:`github.NamedUser.NamedUser`
        :param role: string
        :rtype: None
        """
        assert isinstance(role, (str, unicode)), role
        assert isinstance(member, github.NamedUser.NamedUser), member
        url_parameters = {
            "role": role,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            self.url + "/memberships/" + member._identity, parameters=url_parameters
        )

    def add_to_public_members(self, public_member):
        """
        :calls: `PUT /orgs/:org/public_members/:user <http://developer.github.com/v3/orgs/members>`_
        :param public_member: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(public_member, github.NamedUser.NamedUser), public_member
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            self.url + "/public_members/" + public_member._identity
        )

    def create_fork(self, repo):
        """
        :calls: `POST /repos/:owner/:repo/forks <http://developer.github.com/v3/repos/forks>`_
        :param repo: :class:`github.Repository.Repository`
        :rtype: :class:`github.Repository.Repository`
        """
        assert isinstance(repo, github.Repository.Repository), repo
        url_parameters = {
            "org": self.login,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            "/repos/" + repo.owner.login + "/" + repo.name + "/forks",
            parameters=url_parameters
        )
        return github.Repository.Repository(self._requester, headers, data, completed=True)

    def create_hook(self, name, config, events=github.GithubObject.NotSet, active=github.GithubObject.NotSet):
        """
        :calls: `POST /orgs/:owner/hooks <http://developer.github.com/v3/orgs/hooks>`_
        :param name: string
        :param config: dict
        :param events: list of string
        :param active: bool
        :rtype: :class:`github.Hook.Hook`
        """
        assert isinstance(name, (str, unicode)), name
        assert isinstance(config, dict), config
        assert events is github.GithubObject.NotSet or all(isinstance(element, (str, unicode)) for element in events), events
        assert active is github.GithubObject.NotSet or isinstance(active, bool), active
        post_parameters = {
            "name": name,
            "config": config,
        }
        if events is not github.GithubObject.NotSet:
            post_parameters["events"] = events
        if active is not github.GithubObject.NotSet:
            post_parameters["active"] = active
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/hooks",
            input=post_parameters
        )
        return github.Hook.Hook(self._requester, headers, data, completed=True)

    def create_repo(self, name, description=github.GithubObject.NotSet, homepage=github.GithubObject.NotSet,
                    private=github.GithubObject.NotSet, has_issues=github.GithubObject.NotSet,
                    has_wiki=github.GithubObject.NotSet, has_downloads=github.GithubObject.NotSet,
                    has_projects=github.GithubObject.NotSet, team_id=github.GithubObject.NotSet,
                    auto_init=github.GithubObject.NotSet, license_template=github.GithubObject.NotSet,
                    gitignore_template=github.GithubObject.NotSet, allow_squash_merge=github.GithubObject.NotSet,
                    allow_merge_commit=github.GithubObject.NotSet, allow_rebase_merge=github.GithubObject.NotSet):
        """
        :calls: `POST /orgs/:org/repos <http://developer.github.com/v3/repos>`_
        :param name: string
        :param description: string
        :param homepage: string
        :param private: bool
        :param has_issues: bool
        :param has_wiki: bool
        :param has_downloads: bool
        :param has_projects: bool
        :param team_id: : int
        :param auto_init: bool
        :param license_template: string
        :param gitignore_template: string
        :param allow_squash_merge: bool
        :param allow_merge_commit: bool
        :param allow_rebase_merge: bool
        :rtype: :class:`github.Repository.Repository`
        """
        assert isinstance(name, (str, unicode)), name
        assert description is github.GithubObject.NotSet or isinstance(description, (str, unicode)), description
        assert homepage is github.GithubObject.NotSet or isinstance(homepage, (str, unicode)), homepage
        assert private is github.GithubObject.NotSet or isinstance(private, bool), private
        assert has_issues is github.GithubObject.NotSet or isinstance(has_issues, bool), has_issues
        assert has_wiki is github.GithubObject.NotSet or isinstance(has_wiki, bool), has_wiki
        assert has_downloads is github.GithubObject.NotSet or isinstance(has_downloads, bool), has_downloads
        assert has_projects is github.GithubObject.NotSet or isinstance(has_projects, bool), has_projects
        assert team_id is github.GithubObject.NotSet or isinstance(team_id, (int, long)), team_id
        assert auto_init is github.GithubObject.NotSet or isinstance(auto_init, bool), auto_init
        assert license_template is github.GithubObject.NotSet or isinstance(license_template, (str, unicode)), license_template
        assert gitignore_template is github.GithubObject.NotSet or isinstance(gitignore_template, (str, unicode)), gitignore_template
        assert allow_squash_merge is github.GithubObject.NotSet or isinstance(allow_squash_merge, bool), allow_squash_merge
        assert allow_merge_commit is github.GithubObject.NotSet or isinstance(allow_merge_commit, bool), allow_merge_commit
        assert allow_rebase_merge is github.GithubObject.NotSet or isinstance(allow_rebase_merge, bool), allow_rebase_merge
        post_parameters = {
            "name": name,
        }
        if description is not github.GithubObject.NotSet:
            post_parameters["description"] = description
        if homepage is not github.GithubObject.NotSet:
            post_parameters["homepage"] = homepage
        if private is not github.GithubObject.NotSet:
            post_parameters["private"] = private
        if has_issues is not github.GithubObject.NotSet:
            post_parameters["has_issues"] = has_issues
        if has_wiki is not github.GithubObject.NotSet:
            post_parameters["has_wiki"] = has_wiki
        if has_downloads is not github.GithubObject.NotSet:
            post_parameters["has_downloads"] = has_downloads
        if has_projects is not github.GithubObject.NotSet:
            post_parameters["has_projects"] = has_projects
        if team_id is not github.GithubObject.NotSet:
            post_parameters["team_id"] = team_id
        if auto_init is not github.GithubObject.NotSet:
            post_parameters["auto_init"] = auto_init
        if license_template is not github.GithubObject.NotSet:
            post_parameters["license_template"] = license_template
        if gitignore_template is not github.GithubObject.NotSet:
            post_parameters["gitignore_template"] = gitignore_template
        if allow_squash_merge is not github.GithubObject.NotSet:
            post_parameters["allow_squash_merge"] = allow_squash_merge
        if allow_merge_commit is not github.GithubObject.NotSet:
            post_parameters["allow_merge_commit"] = allow_merge_commit
        if allow_rebase_merge is not github.GithubObject.NotSet:
            post_parameters["allow_rebase_merge"] = allow_rebase_merge
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/repos",
            input=post_parameters
        )
        return github.Repository.Repository(self._requester, headers, data, completed=True)

    def create_team(self, name, repo_names=github.GithubObject.NotSet, permission=github.GithubObject.NotSet, privacy=github.GithubObject.NotSet):
        """
        :calls: `POST /orgs/:org/teams <http://developer.github.com/v3/orgs/teams>`_
        :param name: string
        :param repo_names: list of :class:`github.Repository.Repository`
        :param permission: string
        :param privacy: string
        :rtype: :class:`github.Team.Team`
        """
        assert isinstance(name, (str, unicode)), name
        assert repo_names is github.GithubObject.NotSet or all(isinstance(element, github.Repository.Repository) for element in repo_names), repo_names
        assert permission is github.GithubObject.NotSet or isinstance(permission, (str, unicode)), permission
        assert privacy is github.GithubObject.NotSet or isinstance(privacy, (str, unicode)), privacy
        post_parameters = {
            "name": name,
        }
        if repo_names is not github.GithubObject.NotSet:
            post_parameters["repo_names"] = [element._identity for element in repo_names]
        if permission is not github.GithubObject.NotSet:
            post_parameters["permission"] = permission
        if privacy is not github.GithubObject.NotSet:
            post_parameters['privacy'] = privacy
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/teams",
            input=post_parameters
        )
        return github.Team.Team(self._requester, headers, data, completed=True)

    def delete_hook(self, id):
        """
        :calls: `DELETE /orgs/:owner/hooks/:id <http://developer.github.com/v3/orgs/hooks>`_
        :param id: integer
        :rtype: None`
        """
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url + "/hooks/" + str(id)
        )

    def edit(self, billing_email=github.GithubObject.NotSet, blog=github.GithubObject.NotSet, company=github.GithubObject.NotSet, description=github.GithubObject.NotSet, email=github.GithubObject.NotSet, location=github.GithubObject.NotSet, name=github.GithubObject.NotSet):
        """
        :calls: `PATCH /orgs/:org <http://developer.github.com/v3/orgs>`_
        :param billing_email: string
        :param blog: string
        :param company: string
        :param description: string
        :param email: string
        :param location: string
        :param name: string
        :rtype: None
        """
        assert billing_email is github.GithubObject.NotSet or isinstance(billing_email, (str, unicode)), billing_email
        assert blog is github.GithubObject.NotSet or isinstance(blog, (str, unicode)), blog
        assert company is github.GithubObject.NotSet or isinstance(company, (str, unicode)), company
        assert description is github.GithubObject.NotSet or isinstance(description, (str, unicode)), description
        assert email is github.GithubObject.NotSet or isinstance(email, (str, unicode)), email
        assert location is github.GithubObject.NotSet or isinstance(location, (str, unicode)), location
        assert name is github.GithubObject.NotSet or isinstance(name, (str, unicode)), name
        post_parameters = dict()
        if billing_email is not github.GithubObject.NotSet:
            post_parameters["billing_email"] = billing_email
        if blog is not github.GithubObject.NotSet:
            post_parameters["blog"] = blog
        if company is not github.GithubObject.NotSet:
            post_parameters["company"] = company
        if description is not github.GithubObject.NotSet:
            post_parameters["description"] = description
        if email is not github.GithubObject.NotSet:
            post_parameters["email"] = email
        if location is not github.GithubObject.NotSet:
            post_parameters["location"] = location
        if name is not github.GithubObject.NotSet:
            post_parameters["name"] = name
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=post_parameters
        )
        self._useAttributes(data)

    def edit_hook(self, id, name, config, events=github.GithubObject.NotSet, active=github.GithubObject.NotSet):
        """
        :calls: `PATCH /orgs/:owner/hooks/:id <http://developer.github.com/v3/orgs/hooks>`_
        :param id: integer
        :param name: string
        :param config: dict
        :param events: list of string
        :param active: bool
        :rtype: :class:`github.Hook.Hook`
        """
        assert isinstance(id, (int, long)), id
        assert isinstance(name, (str, unicode)), name
        assert isinstance(config, dict), config
        assert events is github.GithubObject.NotSet or all(isinstance(element, (str, unicode)) for element in events), events
        assert active is github.GithubObject.NotSet or isinstance(active, bool), active
        post_parameters = {
            "name": name,
            "config": config,
        }
        if events is not github.GithubObject.NotSet:
            post_parameters["events"] = events
        if active is not github.GithubObject.NotSet:
            post_parameters["active"] = active
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url + "/hooks/" + str(id),
            input=post_parameters
        )
        return github.Hook.Hook(self._requester, headers, data, completed=True)

    def get_events(self):
        """
        :calls: `GET /orgs/:org/events <http://developer.github.com/v3/activity/events>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Event.Event`
        """
        return github.PaginatedList.PaginatedList(
            github.Event.Event,
            self._requester,
            self.url + "/events",
            None
        )

    def get_hook(self, id):
        """
        :calls: `GET /orgs/:owner/hooks/:id <http://developer.github.com/v3/orgs/hooks>`_
        :param id: integer
        :rtype: :class:`github.Hook.Hook`
        """
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/hooks/" + str(id)
        )
        return github.Hook.Hook(self._requester, headers, data, completed=True)

    def get_hooks(self):
        """
        :calls: `GET /orgs/:owner/hooks <http://developer.github.com/v3/orgs/hooks>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Hook.Hook`
        """
        return github.PaginatedList.PaginatedList(
            github.Hook.Hook,
            self._requester,
            self.url + "/hooks",
            None
        )

    def get_issues(self, filter=github.GithubObject.NotSet, state=github.GithubObject.NotSet, labels=github.GithubObject.NotSet, sort=github.GithubObject.NotSet, direction=github.GithubObject.NotSet, since=github.GithubObject.NotSet):
        """
        :calls: `GET /orgs/:org/issues <http://developer.github.com/v3/issues>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Issue.Issue`
        :param filter: string
        :param state: string
        :param labels: list of :class:`github.Label.Label`
        :param sort: string
        :param direction: string
        :param since: datetime.datetime
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Issue.Issue`
        """
        assert filter is github.GithubObject.NotSet or isinstance(filter, (str, unicode)), filter
        assert state is github.GithubObject.NotSet or isinstance(state, (str, unicode)), state
        assert labels is github.GithubObject.NotSet or all(isinstance(element, github.Label.Label) for element in labels), labels
        assert sort is github.GithubObject.NotSet or isinstance(sort, (str, unicode)), sort
        assert direction is github.GithubObject.NotSet or isinstance(direction, (str, unicode)), direction
        assert since is github.GithubObject.NotSet or isinstance(since, datetime.datetime), since
        url_parameters = dict()
        if filter is not github.GithubObject.NotSet:
            url_parameters["filter"] = filter
        if state is not github.GithubObject.NotSet:
            url_parameters["state"] = state
        if labels is not github.GithubObject.NotSet:
            url_parameters["labels"] = ",".join(label.name for label in labels)
        if sort is not github.GithubObject.NotSet:
            url_parameters["sort"] = sort
        if direction is not github.GithubObject.NotSet:
            url_parameters["direction"] = direction
        if since is not github.GithubObject.NotSet:
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return github.PaginatedList.PaginatedList(
            github.Issue.Issue,
            self._requester,
            self.url + "/issues",
            url_parameters
        )

    def get_members(self, filter_=github.GithubObject.NotSet,
                    role=github.GithubObject.NotSet):
        """
        :calls: `GET /orgs/:org/members <http://developer.github.com/v3/orgs/members>`_
        :param filter_: string
        :param role: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        assert (filter_ is github.GithubObject.NotSet or
                isinstance(filter_, (str, unicode))), filter_
        assert (role is github.GithubObject.NotSet or
                isinstance(role, (str, unicode))), role

        url_parameters = {}
        if filter_ is not github.GithubObject.NotSet:
            url_parameters["filter"] = filter_
        if role is not github.GithubObject.NotSet:
            url_parameters["role"] = role
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/members",
            url_parameters
        )

    def get_projects(self, state=github.GithubObject.NotSet):
        """
        :calls: `GET /orgs/:org/projects <https://developer.github.com/v3/projects/#list-organization-projects>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Project.Project`
        :param state: string
        """
        
        url_parameters = dict()
        if state is not github.GithubObject.NotSet:
            url_parameters["state"] = state
            
        return github.PaginatedList.PaginatedList(
            github.Project.Project,
            self._requester,
            self.url + "/projects",
            url_parameters,
            {"Accept": Consts.mediaTypeProjectsPreview}
        )
        
    def get_public_members(self):
        """
        :calls: `GET /orgs/:org/public_members <http://developer.github.com/v3/orgs/members>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/public_members",
            None
        )

    def get_outside_collaborators(self, filter_=github.GithubObject.NotSet):
        """
        :calls: `GET /orgs/:org/outside_collaborators <http://developer.github.com/v3/orgs/outside_collaborators>`_
        :param filter_: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        assert (filter_ is github.GithubObject.NotSet or
                isinstance(filter_, (str, unicode))), filter_

        url_parameters = {}
        if filter_ is not github.GithubObject.NotSet:
            url_parameters["filter"] = filter_
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/outside_collaborators",
            url_parameters
        )

    def remove_outside_collaborator(self, collaborator):
        """
        :calls: `DELETE /orgs/:org/outside_collaborators/:username <https://developer.github.com/v3/orgs/outside_collaborators>`_
        :param collaborator: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(collaborator, github.NamedUser.NamedUser), collaborator
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url + "/outside_collaborators/" + collaborator._identity
        )

    def convert_to_outside_collaborator(self, member):
        """
        :calls: `PUT /orgs/:org/outside_collaborators/:username <https://developer.github.com/v3/orgs/outside_collaborators>`_
        :param member: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            self.url + "/outside_collaborators/" + member._identity
        )

    def get_repo(self, name):
        """
        :calls: `GET /repos/:owner/:repo <http://developer.github.com/v3/repos>`_
        :param name: string
        :rtype: :class:`github.Repository.Repository`
        """
        assert isinstance(name, (str, unicode)), name
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            "/repos/" + self.login + "/" + name
        )
        return github.Repository.Repository(self._requester, headers, data, completed=True)

    def get_repos(self, type=github.GithubObject.NotSet):
        """
        :calls: `GET /orgs/:org/repos <http://developer.github.com/v3/repos>`_
        :param type: string ('all', 'public', 'private', 'forks', 'sources', 'member')
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        assert type is github.GithubObject.NotSet or isinstance(type, (str, unicode)), type
        url_parameters = dict()
        if type is not github.GithubObject.NotSet:
            url_parameters["type"] = type
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self._requester,
            self.url + "/repos",
            url_parameters
        )

    def get_team(self, id):
        """
        :calls: `GET /teams/:id <http://developer.github.com/v3/orgs/teams>`_
        :param id: integer
        :rtype: :class:`github.Team.Team`
        """
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            "/teams/" + str(id)
        )
        return github.Team.Team(self._requester, headers, data, completed=True)

    def get_teams(self):
        """
        :calls: `GET /orgs/:org/teams <http://developer.github.com/v3/orgs/teams>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Team.Team`
        """
        return github.PaginatedList.PaginatedList(
            github.Team.Team,
            self._requester,
            self.url + "/teams",
            None
        )

    def invite_user(self, user=github.GithubObject.NotSet, email=github.GithubObject.NotSet, role=github.GithubObject.NotSet, teams=github.GithubObject.NotSet):
        """
        :calls: `POST /orgs/:org/invitations <http://developer.github.com/v3/orgs/members>`_
        :param user: :class:`github.NamedUser.NamedUser`
        :param email: string
        :param role: string
        :param teams: array of :class:`github.Team.Team`
        :rtype: None
        """
        assert user is github.GithubObject.NotSet or isinstance(user, github.NamedUser.NamedUser), user
        assert email is github.GithubObject.NotSet or isinstance(email, (str, unicode)), email
        assert (email is github.GithubObject.NotSet) ^ (user is github.GithubObject.NotSet), "specify only one of email or user"
        parameters = {}
        if user is not github.GithubObject.NotSet:
            parameters["invitee_id"] = user.id
        elif email is not github.GithubObject.NotSet:
            parameters["email"] = email
        if role is not github.GithubObject.NotSet:
            assert isinstance(role, (str, unicode)), role
            assert role in ['admin', 'direct_member', 'billing_manager']
            parameters["role"] = role
        if teams is not github.GithubObject.NotSet:
            assert all(isinstance(team, github.Team.Team) for team in teams)
            parameters["team_ids"] = [t.id for t in teams]
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/invitations",
            headers={'Accept': Consts.mediaTypeOrganizationInvitationPreview},
            input=parameters
        )

    def has_in_members(self, member):
        """
        :calls: `GET /orgs/:org/members/:user <http://developer.github.com/v3/orgs/members>`_
        :param member: :class:`github.NamedUser.NamedUser`
        :rtype: bool
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        status, headers, data = self._requester.requestJson(
            "GET",
            self.url + "/members/" + member._identity
        )
        if status == 302:
            status, headers, data = self._requester.requestJson(
                "GET",
                headers['location']
            )
        return status == 204

    def has_in_public_members(self, public_member):
        """
        :calls: `GET /orgs/:org/public_members/:user <http://developer.github.com/v3/orgs/members>`_
        :param public_member: :class:`github.NamedUser.NamedUser`
        :rtype: bool
        """
        assert isinstance(public_member, github.NamedUser.NamedUser), public_member
        status, headers, data = self._requester.requestJson(
            "GET",
            self.url + "/public_members/" + public_member._identity
        )
        return status == 204

    def remove_from_membership(self, member):
        """
        :calls: `DELETE /orgs/:org/memberships/:user <https://developer.github.com/v3/orgs/members/#remove-organization-membership>`_
        :param member: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url + "/memberships/" + member._identity
        )

    def remove_from_members(self, member):
        """
        :calls: `DELETE /orgs/:org/members/:user <http://developer.github.com/v3/orgs/members>`_
        :param member: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url + "/members/" + member._identity
        )

    def remove_from_public_members(self, public_member):
        """
        :calls: `DELETE /orgs/:org/public_members/:user <http://developer.github.com/v3/orgs/members>`_
        :param public_member: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(public_member, github.NamedUser.NamedUser), public_member
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url + "/public_members/" + public_member._identity
        )

    def create_migration(self, repos, lock_repositories=github.GithubObject.NotSet, exclude_attachments=github.GithubObject.NotSet):
        """
        :calls: `POST /orgs/:org/migrations`_
        :param repos: list or tuple of str
        :param lock_repositories: bool
        :param exclude_attachments: bool
        :rtype: :class:`github.Migration.Migration`
        """
        assert isinstance(repos, (list, tuple)), repos
        assert all(isinstance(repo, (str, unicode)) for repo in repos), repos
        assert lock_repositories is github.GithubObject.NotSet or isinstance(lock_repositories, bool), lock_repositories
        assert exclude_attachments is github.GithubObject.NotSet or isinstance(exclude_attachments, bool), exclude_attachments
        post_parameters = {
            "repositories": repos
        }
        if lock_repositories is not github.GithubObject.NotSet:
            post_parameters["lock_repositories"] = lock_repositories
        if exclude_attachments is not github.GithubObject.NotSet:
            post_parameters["exclude_attachments"] = exclude_attachments
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            "/orgs/" + self.login + "/migrations",
            input=post_parameters,
            headers={
                "Accept": Consts.mediaTypeMigrationPreview
            }
        )
        return github.Migration.Migration(self._requester, headers, data, completed=True)

    def get_migrations(self):
        """
        :calls: `GET /orgs/:org/migrations`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Migration.Migration`
        """
        return github.PaginatedList.PaginatedList(
            github.Migration.Migration,
            self._requester,
            "/orgs/" + self.login + "/migrations",
            None,
            headers={
                "Accept": Consts.mediaTypeMigrationPreview
            }
        )

    def _initAttributes(self):
        self._avatar_url = github.GithubObject.NotSet
        self._billing_email = github.GithubObject.NotSet
        self._blog = github.GithubObject.NotSet
        self._collaborators = github.GithubObject.NotSet
        self._company = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._description = github.GithubObject.NotSet
        self._disk_usage = github.GithubObject.NotSet
        self._email = github.GithubObject.NotSet
        self._events_url = github.GithubObject.NotSet
        self._followers = github.GithubObject.NotSet
        self._following = github.GithubObject.NotSet
        self._gravatar_id = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._location = github.GithubObject.NotSet
        self._login = github.GithubObject.NotSet
        self._members_url = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._owned_private_repos = github.GithubObject.NotSet
        self._plan = github.GithubObject.NotSet
        self._private_gists = github.GithubObject.NotSet
        self._public_gists = github.GithubObject.NotSet
        self._public_members_url = github.GithubObject.NotSet
        self._public_repos = github.GithubObject.NotSet
        self._repos_url = github.GithubObject.NotSet
        self._total_private_repos = github.GithubObject.NotSet
        self._type = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "avatar_url" in attributes:  # pragma no branch
            self._avatar_url = self._makeStringAttribute(attributes["avatar_url"])
        if "billing_email" in attributes:  # pragma no branch
            self._billing_email = self._makeStringAttribute(attributes["billing_email"])
        if "blog" in attributes:  # pragma no branch
            self._blog = self._makeStringAttribute(attributes["blog"])
        if "collaborators" in attributes:  # pragma no branch
            self._collaborators = self._makeIntAttribute(attributes["collaborators"])
        if "company" in attributes:  # pragma no branch
            self._company = self._makeStringAttribute(attributes["company"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "disk_usage" in attributes:  # pragma no branch
            self._disk_usage = self._makeIntAttribute(attributes["disk_usage"])
        if "email" in attributes:  # pragma no branch
            self._email = self._makeStringAttribute(attributes["email"])
        if "events_url" in attributes:  # pragma no branch
            self._events_url = self._makeStringAttribute(attributes["events_url"])
        if "followers" in attributes:  # pragma no branch
            self._followers = self._makeIntAttribute(attributes["followers"])
        if "following" in attributes:  # pragma no branch
            self._following = self._makeIntAttribute(attributes["following"])
        if "gravatar_id" in attributes:  # pragma no branch
            self._gravatar_id = self._makeStringAttribute(attributes["gravatar_id"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "location" in attributes:  # pragma no branch
            self._location = self._makeStringAttribute(attributes["location"])
        if "login" in attributes:  # pragma no branch
            self._login = self._makeStringAttribute(attributes["login"])
        if "members_url" in attributes:  # pragma no branch
            self._members_url = self._makeStringAttribute(attributes["members_url"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "owned_private_repos" in attributes:  # pragma no branch
            self._owned_private_repos = self._makeIntAttribute(attributes["owned_private_repos"])
        if "plan" in attributes:  # pragma no branch
            self._plan = self._makeClassAttribute(github.Plan.Plan, attributes["plan"])
        if "private_gists" in attributes:  # pragma no branch
            self._private_gists = self._makeIntAttribute(attributes["private_gists"])
        if "public_gists" in attributes:  # pragma no branch
            self._public_gists = self._makeIntAttribute(attributes["public_gists"])
        if "public_members_url" in attributes:  # pragma no branch
            self._public_members_url = self._makeStringAttribute(attributes["public_members_url"])
        if "public_repos" in attributes:  # pragma no branch
            self._public_repos = self._makeIntAttribute(attributes["public_repos"])
        if "repos_url" in attributes:  # pragma no branch
            self._repos_url = self._makeStringAttribute(attributes["repos_url"])
        if "total_private_repos" in attributes:  # pragma no branch
            self._total_private_repos = self._makeIntAttribute(attributes["total_private_repos"])
        if "type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["type"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
