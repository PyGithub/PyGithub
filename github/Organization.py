# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import GithubObject
import PaginatedList

import Plan
import Team
import Event
import Repository
import NamedUser


class Organization(GithubObject.GithubObject):
    @property
    def avatar_url(self):
        self._completeIfNotSet(self._avatar_url)
        return self._NoneIfNotSet(self._avatar_url)

    @property
    def billing_email(self):
        self._completeIfNotSet(self._billing_email)
        return self._NoneIfNotSet(self._billing_email)

    @property
    def blog(self):
        self._completeIfNotSet(self._blog)
        return self._NoneIfNotSet(self._blog)

    @property
    def collaborators(self):
        self._completeIfNotSet(self._collaborators)
        return self._NoneIfNotSet(self._collaborators)

    @property
    def company(self):
        self._completeIfNotSet(self._company)
        return self._NoneIfNotSet(self._company)

    @property
    def created_at(self):
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def disk_usage(self):
        self._completeIfNotSet(self._disk_usage)
        return self._NoneIfNotSet(self._disk_usage)

    @property
    def email(self):
        self._completeIfNotSet(self._email)
        return self._NoneIfNotSet(self._email)

    @property
    def followers(self):
        self._completeIfNotSet(self._followers)
        return self._NoneIfNotSet(self._followers)

    @property
    def following(self):
        self._completeIfNotSet(self._following)
        return self._NoneIfNotSet(self._following)

    @property
    def gravatar_id(self):
        self._completeIfNotSet(self._gravatar_id)
        return self._NoneIfNotSet(self._gravatar_id)

    @property
    def html_url(self):
        self._completeIfNotSet(self._html_url)
        return self._NoneIfNotSet(self._html_url)

    @property
    def id(self):
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def location(self):
        self._completeIfNotSet(self._location)
        return self._NoneIfNotSet(self._location)

    @property
    def login(self):
        self._completeIfNotSet(self._login)
        return self._NoneIfNotSet(self._login)

    @property
    def name(self):
        self._completeIfNotSet(self._name)
        return self._NoneIfNotSet(self._name)

    @property
    def owned_private_repos(self):
        self._completeIfNotSet(self._owned_private_repos)
        return self._NoneIfNotSet(self._owned_private_repos)

    @property
    def plan(self):
        self._completeIfNotSet(self._plan)
        return self._NoneIfNotSet(self._plan)

    @property
    def private_gists(self):
        self._completeIfNotSet(self._private_gists)
        return self._NoneIfNotSet(self._private_gists)

    @property
    def public_gists(self):
        self._completeIfNotSet(self._public_gists)
        return self._NoneIfNotSet(self._public_gists)

    @property
    def public_repos(self):
        self._completeIfNotSet(self._public_repos)
        return self._NoneIfNotSet(self._public_repos)

    @property
    def total_private_repos(self):
        self._completeIfNotSet(self._total_private_repos)
        return self._NoneIfNotSet(self._total_private_repos)

    @property
    def type(self):
        self._completeIfNotSet(self._type)
        return self._NoneIfNotSet(self._type)

    @property
    def url(self):
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    def add_to_public_members(self, public_member):
        assert isinstance(public_member, NamedUser.NamedUser), public_member
        headers, data = self._requester.requestAndCheck(
            "PUT",
            self.url + "/public_members/" + public_member._identity,
            None,
            None
        )

    def create_fork(self, repo):
        assert isinstance(repo, Repository.Repository), repo
        url_parameters = {
            "org": self.login,
        }
        headers, data = self._requester.requestAndCheck(
            "POST",
            "/repos/" + repo.owner.login + "/" + repo.name + "/forks",
            url_parameters,
            None
        )
        return Repository.Repository(self._requester, data, completed=True)

    def create_repo(self, name, description=GithubObject.NotSet, homepage=GithubObject.NotSet, private=GithubObject.NotSet, has_issues=GithubObject.NotSet, has_wiki=GithubObject.NotSet, has_downloads=GithubObject.NotSet, team_id=GithubObject.NotSet, auto_init=GithubObject.NotSet, gitignore_template=GithubObject.NotSet):
        assert isinstance(name, (str, unicode)), name
        assert description is GithubObject.NotSet or isinstance(description, (str, unicode)), description
        assert homepage is GithubObject.NotSet or isinstance(homepage, (str, unicode)), homepage
        assert private is GithubObject.NotSet or isinstance(private, bool), private
        assert has_issues is GithubObject.NotSet or isinstance(has_issues, bool), has_issues
        assert has_wiki is GithubObject.NotSet or isinstance(has_wiki, bool), has_wiki
        assert has_downloads is GithubObject.NotSet or isinstance(has_downloads, bool), has_downloads
        assert team_id is GithubObject.NotSet or isinstance(team_id, Team.Team), team_id
        assert auto_init is GithubObject.NotSet or isinstance(auto_init, bool), auto_init
        assert gitignore_template is GithubObject.NotSet or isinstance(gitignore_template, (str, unicode)), gitignore_template
        post_parameters = {
            "name": name,
        }
        if description is not GithubObject.NotSet:
            post_parameters["description"] = description
        if homepage is not GithubObject.NotSet:
            post_parameters["homepage"] = homepage
        if private is not GithubObject.NotSet:
            post_parameters["private"] = private
        if has_issues is not GithubObject.NotSet:
            post_parameters["has_issues"] = has_issues
        if has_wiki is not GithubObject.NotSet:
            post_parameters["has_wiki"] = has_wiki
        if has_downloads is not GithubObject.NotSet:
            post_parameters["has_downloads"] = has_downloads
        if team_id is not GithubObject.NotSet:
            post_parameters["team_id"] = team_id._identity
        if auto_init is not GithubObject.NotSet:
            post_parameters["auto_init"] = auto_init
        if gitignore_template is not GithubObject.NotSet:
            post_parameters["gitignore_template"] = gitignore_template
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/repos",
            None,
            post_parameters
        )
        return Repository.Repository(self._requester, data, completed=True)

    def create_team(self, name, repo_names=GithubObject.NotSet, permission=GithubObject.NotSet):
        assert isinstance(name, (str, unicode)), name
        assert repo_names is GithubObject.NotSet or all(isinstance(element, Repository.Repository) for element in repo_names), repo_names
        assert permission is GithubObject.NotSet or isinstance(permission, (str, unicode)), permission
        post_parameters = {
            "name": name,
        }
        if repo_names is not GithubObject.NotSet:
            post_parameters["repo_names"] = [element._identity for element in repo_names]
        if permission is not GithubObject.NotSet:
            post_parameters["permission"] = permission
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/teams",
            None,
            post_parameters
        )
        return Team.Team(self._requester, data, completed=True)

    def edit(self, billing_email=GithubObject.NotSet, blog=GithubObject.NotSet, company=GithubObject.NotSet, email=GithubObject.NotSet, location=GithubObject.NotSet, name=GithubObject.NotSet):
        assert billing_email is GithubObject.NotSet or isinstance(billing_email, (str, unicode)), billing_email
        assert blog is GithubObject.NotSet or isinstance(blog, (str, unicode)), blog
        assert company is GithubObject.NotSet or isinstance(company, (str, unicode)), company
        assert email is GithubObject.NotSet or isinstance(email, (str, unicode)), email
        assert location is GithubObject.NotSet or isinstance(location, (str, unicode)), location
        assert name is GithubObject.NotSet or isinstance(name, (str, unicode)), name
        post_parameters = dict()
        if billing_email is not GithubObject.NotSet:
            post_parameters["billing_email"] = billing_email
        if blog is not GithubObject.NotSet:
            post_parameters["blog"] = blog
        if company is not GithubObject.NotSet:
            post_parameters["company"] = company
        if email is not GithubObject.NotSet:
            post_parameters["email"] = email
        if location is not GithubObject.NotSet:
            post_parameters["location"] = location
        if name is not GithubObject.NotSet:
            post_parameters["name"] = name
        headers, data = self._requester.requestAndCheck(
            "PATCH",
            self.url,
            None,
            post_parameters
        )
        self._useAttributes(data)

    def get_events(self):
        return PaginatedList.PaginatedList(
            Event.Event,
            self._requester,
            self.url + "/events",
            None
        )

    def get_members(self):
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self._requester,
            self.url + "/members",
            None
        )

    def get_public_members(self):
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self._requester,
            self.url + "/public_members",
            None
        )

    def get_repo(self, name):
        assert isinstance(name, (str, unicode)), name
        headers, data = self._requester.requestAndCheck(
            "GET",
            "/repos/" + self.login + "/" + name,
            None,
            None
        )
        return Repository.Repository(self._requester, data, completed=True)

    def get_repos(self, type=GithubObject.NotSet):
        assert type is GithubObject.NotSet or isinstance(type, (str, unicode)), type
        url_parameters = dict()
        if type is not GithubObject.NotSet:
            url_parameters["type"] = type
        return PaginatedList.PaginatedList(
            Repository.Repository,
            self._requester,
            self.url + "/repos",
            url_parameters
        )

    def get_team(self, id):
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestAndCheck(
            "GET",
            "/teams/" + str(id),
            None,
            None
        )
        return Team.Team(self._requester, data, completed=True)

    def get_teams(self):
        return PaginatedList.PaginatedList(
            Team.Team,
            self._requester,
            self.url + "/teams",
            None
        )

    def has_in_members(self, member):
        assert isinstance(member, NamedUser.NamedUser), member
        status, headers, data = self._requester.requestRaw(
            "GET",
            self.url + "/members/" + member._identity,
            None,
            None
        )
        return status == 204

    def has_in_public_members(self, public_member):
        assert isinstance(public_member, NamedUser.NamedUser), public_member
        status, headers, data = self._requester.requestRaw(
            "GET",
            self.url + "/public_members/" + public_member._identity,
            None,
            None
        )
        return status == 204

    def remove_from_members(self, member):
        assert isinstance(member, NamedUser.NamedUser), member
        headers, data = self._requester.requestAndCheck(
            "DELETE",
            self.url + "/members/" + member._identity,
            None,
            None
        )

    def remove_from_public_members(self, public_member):
        assert isinstance(public_member, NamedUser.NamedUser), public_member
        headers, data = self._requester.requestAndCheck(
            "DELETE",
            self.url + "/public_members/" + public_member._identity,
            None,
            None
        )

    def _initAttributes(self):
        self._avatar_url = GithubObject.NotSet
        self._billing_email = GithubObject.NotSet
        self._blog = GithubObject.NotSet
        self._collaborators = GithubObject.NotSet
        self._company = GithubObject.NotSet
        self._created_at = GithubObject.NotSet
        self._disk_usage = GithubObject.NotSet
        self._email = GithubObject.NotSet
        self._followers = GithubObject.NotSet
        self._following = GithubObject.NotSet
        self._gravatar_id = GithubObject.NotSet
        self._html_url = GithubObject.NotSet
        self._id = GithubObject.NotSet
        self._location = GithubObject.NotSet
        self._login = GithubObject.NotSet
        self._name = GithubObject.NotSet
        self._owned_private_repos = GithubObject.NotSet
        self._plan = GithubObject.NotSet
        self._private_gists = GithubObject.NotSet
        self._public_gists = GithubObject.NotSet
        self._public_repos = GithubObject.NotSet
        self._total_private_repos = GithubObject.NotSet
        self._type = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "avatar_url" in attributes:  # pragma no branch
            assert attributes["avatar_url"] is None or isinstance(attributes["avatar_url"], (str, unicode)), attributes["avatar_url"]
            self._avatar_url = attributes["avatar_url"]
        if "billing_email" in attributes:  # pragma no branch
            assert attributes["billing_email"] is None or isinstance(attributes["billing_email"], (str, unicode)), attributes["billing_email"]
            self._billing_email = attributes["billing_email"]
        if "blog" in attributes:  # pragma no branch
            assert attributes["blog"] is None or isinstance(attributes["blog"], (str, unicode)), attributes["blog"]
            self._blog = attributes["blog"]
        if "collaborators" in attributes:  # pragma no branch
            assert attributes["collaborators"] is None or isinstance(attributes["collaborators"], (int, long)), attributes["collaborators"]
            self._collaborators = attributes["collaborators"]
        if "company" in attributes:  # pragma no branch
            assert attributes["company"] is None or isinstance(attributes["company"], (str, unicode)), attributes["company"]
            self._company = attributes["company"]
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "disk_usage" in attributes:  # pragma no branch
            assert attributes["disk_usage"] is None or isinstance(attributes["disk_usage"], (int, long)), attributes["disk_usage"]
            self._disk_usage = attributes["disk_usage"]
        if "email" in attributes:  # pragma no branch
            assert attributes["email"] is None or isinstance(attributes["email"], (str, unicode)), attributes["email"]
            self._email = attributes["email"]
        if "followers" in attributes:  # pragma no branch
            assert attributes["followers"] is None or isinstance(attributes["followers"], (int, long)), attributes["followers"]
            self._followers = attributes["followers"]
        if "following" in attributes:  # pragma no branch
            assert attributes["following"] is None or isinstance(attributes["following"], (int, long)), attributes["following"]
            self._following = attributes["following"]
        if "gravatar_id" in attributes:  # pragma no branch
            assert attributes["gravatar_id"] is None or isinstance(attributes["gravatar_id"], (str, unicode)), attributes["gravatar_id"]
            self._gravatar_id = attributes["gravatar_id"]
        if "html_url" in attributes:  # pragma no branch
            assert attributes["html_url"] is None or isinstance(attributes["html_url"], (str, unicode)), attributes["html_url"]
            self._html_url = attributes["html_url"]
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "location" in attributes:  # pragma no branch
            assert attributes["location"] is None or isinstance(attributes["location"], (str, unicode)), attributes["location"]
            self._location = attributes["location"]
        if "login" in attributes:  # pragma no branch
            assert attributes["login"] is None or isinstance(attributes["login"], (str, unicode)), attributes["login"]
            self._login = attributes["login"]
        if "name" in attributes:  # pragma no branch
            assert attributes["name"] is None or isinstance(attributes["name"], (str, unicode)), attributes["name"]
            self._name = attributes["name"]
        if "owned_private_repos" in attributes:  # pragma no branch
            assert attributes["owned_private_repos"] is None or isinstance(attributes["owned_private_repos"], (int, long)), attributes["owned_private_repos"]
            self._owned_private_repos = attributes["owned_private_repos"]
        if "plan" in attributes:  # pragma no branch
            assert attributes["plan"] is None or isinstance(attributes["plan"], dict), attributes["plan"]
            self._plan = None if attributes["plan"] is None else Plan.Plan(self._requester, attributes["plan"], completed=False)
        if "private_gists" in attributes:  # pragma no branch
            assert attributes["private_gists"] is None or isinstance(attributes["private_gists"], (int, long)), attributes["private_gists"]
            self._private_gists = attributes["private_gists"]
        if "public_gists" in attributes:  # pragma no branch
            assert attributes["public_gists"] is None or isinstance(attributes["public_gists"], (int, long)), attributes["public_gists"]
            self._public_gists = attributes["public_gists"]
        if "public_repos" in attributes:  # pragma no branch
            assert attributes["public_repos"] is None or isinstance(attributes["public_repos"], (int, long)), attributes["public_repos"]
            self._public_repos = attributes["public_repos"]
        if "total_private_repos" in attributes:  # pragma no branch
            assert attributes["total_private_repos"] is None or isinstance(attributes["total_private_repos"], (int, long)), attributes["total_private_repos"]
            self._total_private_repos = attributes["total_private_repos"]
        if "type" in attributes:  # pragma no branch
            assert attributes["type"] is None or isinstance(attributes["type"], (str, unicode)), attributes["type"]
            self._type = attributes["type"]
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
