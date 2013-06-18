# -*- coding: utf-8 -*-

# Copyright 2012 Christopher Gilbert christopher.john.gilbert@gmail.com
# Copyright 2012 Steve English steve.english@navetas.com
# Copyright 2012 Vincent Jacques vincent@vincent-jacques.net
# Copyright 2012 Zearin zearin@gonk.net
# Copyright 2013 Vincent Jacques vincent@vincent-jacques.net
# Copyright 2013 Mark Roddy markroddy@gmail.com
# Copyright 2013 martinqt m.ki2@laposte.net

# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import urllib
import datetime

import github.GithubObject
import github.PaginatedList

import github.Branch
import github.IssueEvent
import github.ContentFile
import github.Label
import github.GitBlob
import github.Organization
import github.GitRef
import github.Issue
import github.Repository
import github.PullRequest
import github.RepositoryKey
import github.NamedUser
import github.Milestone
import github.Comparison
import github.CommitComment
import github.GitCommit
import github.Team
import github.Commit
import github.GitTree
import github.Hook
import github.Tag
import github.GitTag
import github.Download
import github.Permissions
import github.Event
import github.Legacy


class Repository(github.GithubObject.CompletableGithubObject):
    """
    This class represents Repositorys. The reference can be found here http://developer.github.com/v3/repos/
    """

    @property
    def clone_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._clone_url)
        return self._NoneIfNotSet(self._clone_url)

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def description(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._description)
        return self._NoneIfNotSet(self._description)

    @property
    def fork(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._fork)
        return self._NoneIfNotSet(self._fork)

    @property
    def forks(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._forks)
        return self._NoneIfNotSet(self._forks)

    @property
    def full_name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._full_name)
        return self._NoneIfNotSet(self._full_name)

    @property
    def git_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._git_url)
        return self._NoneIfNotSet(self._git_url)

    @property
    def has_downloads(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._has_downloads)
        return self._NoneIfNotSet(self._has_downloads)

    @property
    def has_issues(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._has_issues)
        return self._NoneIfNotSet(self._has_issues)

    @property
    def has_wiki(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._has_wiki)
        return self._NoneIfNotSet(self._has_wiki)

    @property
    def homepage(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._homepage)
        return self._NoneIfNotSet(self._homepage)

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._NoneIfNotSet(self._html_url)

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def language(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._language)
        return self._NoneIfNotSet(self._language)

    @property
    def master_branch(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._master_branch)
        return self._NoneIfNotSet(self._master_branch)

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._NoneIfNotSet(self._name)

    @property
    def open_issues(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._open_issues)
        return self._NoneIfNotSet(self._open_issues)

    @property
    def organization(self):
        """
        :type: :class:`github.Organization.Organization`
        """
        self._completeIfNotSet(self._organization)
        return self._NoneIfNotSet(self._organization)

    @property
    def owner(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._owner)
        return self._NoneIfNotSet(self._owner)

    @property
    def parent(self):
        """
        :type: :class:`github.Repository.Repository`
        """
        self._completeIfNotSet(self._parent)
        return self._NoneIfNotSet(self._parent)

    @property
    def permissions(self):
        """
        :type: :class:`github.Permissions.Permissions`
        """
        self._completeIfNotSet(self._permissions)
        return self._NoneIfNotSet(self._permissions)

    @property
    def private(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._private)
        return self._NoneIfNotSet(self._private)

    @property
    def pushed_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._pushed_at)
        return self._NoneIfNotSet(self._pushed_at)

    @property
    def size(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._size)
        return self._NoneIfNotSet(self._size)

    @property
    def source(self):
        """
        :type: :class:`github.Repository.Repository`
        """
        self._completeIfNotSet(self._source)
        return self._NoneIfNotSet(self._source)

    @property
    def ssh_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._ssh_url)
        return self._NoneIfNotSet(self._ssh_url)

    @property
    def svn_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._svn_url)
        return self._NoneIfNotSet(self._svn_url)

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._NoneIfNotSet(self._updated_at)

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    @property
    def watchers(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._watchers)
        return self._NoneIfNotSet(self._watchers)

    def add_to_collaborators(self, collaborator):
        """
        :calls: `PUT /repos/:user/:repo/collaborators/:user <http://developer.github.com/v3/todo>`_
        :param collaborator: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(collaborator, github.NamedUser.NamedUser), collaborator
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            self.url + "/collaborators/" + collaborator._identity,
            None,
            None
        )

    def compare(self, base, head):
        """
        :calls: `GET /repos/:user/:repo/compare/:base...:head <http://developer.github.com/v3/todo>`_
        :param base: string
        :param head: string
        :rtype: :class:`github.Comparison.Comparison`
        """
        assert isinstance(base, (str, unicode)), base
        assert isinstance(head, (str, unicode)), head
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/compare/" + base + "..." + head,
            None,
            None
        )
        return github.Comparison.Comparison(self._requester, data, completed=True)

    def create_download(self, name, size, description=github.GithubObject.NotSet, content_type=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:user/:repo/downloads <http://developer.github.com/v3/todo>`_
        :param name: string
        :param size: integer
        :param description: string
        :param content_type: string
        :rtype: :class:`github.Download.Download`
        """
        assert isinstance(name, (str, unicode)), name
        assert isinstance(size, (int, long)), size
        assert description is github.GithubObject.NotSet or isinstance(description, (str, unicode)), description
        assert content_type is github.GithubObject.NotSet or isinstance(content_type, (str, unicode)), content_type
        post_parameters = {
            "name": name,
            "size": size,
        }
        if description is not github.GithubObject.NotSet:
            post_parameters["description"] = description
        if content_type is not github.GithubObject.NotSet:
            post_parameters["content_type"] = content_type
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/downloads",
            None,
            post_parameters
        )
        return github.Download.Download(self._requester, data, completed=True)

    def create_git_blob(self, content, encoding):
        """
        :calls: `POST /repos/:user/:repo/git/blobs <http://developer.github.com/v3/todo>`_
        :param content: string
        :param encoding: string
        :rtype: :class:`github.GitBlob.GitBlob`
        """
        assert isinstance(content, (str, unicode)), content
        assert isinstance(encoding, (str, unicode)), encoding
        post_parameters = {
            "content": content,
            "encoding": encoding,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/git/blobs",
            None,
            post_parameters
        )
        return github.GitBlob.GitBlob(self._requester, data, completed=True)

    def create_git_commit(self, message, tree, parents, author=github.GithubObject.NotSet, committer=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:user/:repo/git/commits <http://developer.github.com/v3/todo>`_
        :param message: string
        :param tree: :class:`github.GitTree.GitTree`
        :param parents: list of :class:`github.GitCommit.GitCommit`
        :param author: :class:`github.InputGitAuthor.InputGitAuthor`
        :param committer: :class:`github.InputGitAuthor.InputGitAuthor`
        :rtype: :class:`github.GitCommit.GitCommit`
        """
        assert isinstance(message, (str, unicode)), message
        assert isinstance(tree, github.GitTree.GitTree), tree
        assert all(isinstance(element, github.GitCommit.GitCommit) for element in parents), parents
        assert author is github.GithubObject.NotSet or isinstance(author, github.InputGitAuthor), author
        assert committer is github.GithubObject.NotSet or isinstance(committer, github.InputGitAuthor), committer
        post_parameters = {
            "message": message,
            "tree": tree._identity,
            "parents": [element._identity for element in parents],
        }
        if author is not github.GithubObject.NotSet:
            post_parameters["author"] = author._identity
        if committer is not github.GithubObject.NotSet:
            post_parameters["committer"] = committer._identity
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/git/commits",
            None,
            post_parameters
        )
        return github.GitCommit.GitCommit(self._requester, data, completed=True)

    def create_git_ref(self, ref, sha):
        """
        :calls: `POST /repos/:user/:repo/git/refs <http://developer.github.com/v3/todo>`_
        :param ref: string
        :param sha: string
        :rtype: :class:`github.GitRef.GitRef`
        """
        assert isinstance(ref, (str, unicode)), ref
        assert isinstance(sha, (str, unicode)), sha
        post_parameters = {
            "ref": ref,
            "sha": sha,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/git/refs",
            None,
            post_parameters
        )
        return github.GitRef.GitRef(self._requester, data, completed=True)

    def create_git_tag(self, tag, message, object, type, tagger=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:user/:repo/git/tags <http://developer.github.com/v3/todo>`_
        :param tag: string
        :param message: string
        :param object: string
        :param type: string
        :param tagger: :class:`github.InputGitAuthor.InputGitAuthor`
        :rtype: :class:`github.GitTag.GitTag`
        """
        assert isinstance(tag, (str, unicode)), tag
        assert isinstance(message, (str, unicode)), message
        assert isinstance(object, (str, unicode)), object
        assert isinstance(type, (str, unicode)), type
        assert tagger is github.GithubObject.NotSet or isinstance(tagger, github.InputGitAuthor), tagger
        post_parameters = {
            "tag": tag,
            "message": message,
            "object": object,
            "type": type,
        }
        if tagger is not github.GithubObject.NotSet:
            post_parameters["tagger"] = tagger._identity
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/git/tags",
            None,
            post_parameters
        )
        return github.GitTag.GitTag(self._requester, data, completed=True)

    def create_git_tree(self, tree, base_tree=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:user/:repo/git/trees <http://developer.github.com/v3/todo>`_
        :param tree: list of :class:`github.InputGitTreeElement.InputGitTreeElement`
        :param base_tree: :class:`github.GitTree.GitTree`
        :rtype: :class:`github.GitTree.GitTree`
        """
        assert all(isinstance(element, github.InputGitTreeElement) for element in tree), tree
        assert base_tree is github.GithubObject.NotSet or isinstance(base_tree, github.GitTree.GitTree), base_tree
        post_parameters = {
            "tree": [element._identity for element in tree],
        }
        if base_tree is not github.GithubObject.NotSet:
            post_parameters["base_tree"] = base_tree._identity
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/git/trees",
            None,
            post_parameters
        )
        return github.GitTree.GitTree(self._requester, data, completed=True)

    def create_hook(self, name, config, events=github.GithubObject.NotSet, active=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:user/:repo/hooks <http://developer.github.com/v3/todo>`_
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
            None,
            post_parameters
        )
        return github.Hook.Hook(self._requester, data, completed=True)

    def create_issue(self, title, body=github.GithubObject.NotSet, assignee=github.GithubObject.NotSet, milestone=github.GithubObject.NotSet, labels=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:user/:repo/issues <http://developer.github.com/v3/todo>`_
        :param title: string
        :param body: string
        :param assignee: :class:`github.NamedUser.NamedUser`
        :param milestone: :class:`github.Milestone.Milestone`
        :param labels: list of :class:`github.Label.Label`
        :rtype: :class:`github.Issue.Issue`
        """
        assert isinstance(title, (str, unicode)), title
        assert body is github.GithubObject.NotSet or isinstance(body, (str, unicode)), body
        assert assignee is github.GithubObject.NotSet or isinstance(assignee, github.NamedUser.NamedUser), assignee
        assert milestone is github.GithubObject.NotSet or isinstance(milestone, github.Milestone.Milestone), milestone
        assert labels is github.GithubObject.NotSet or all(isinstance(element, github.Label.Label) for element in labels), labels
        post_parameters = {
            "title": title,
        }
        if body is not github.GithubObject.NotSet:
            post_parameters["body"] = body
        if assignee is not github.GithubObject.NotSet:
            post_parameters["assignee"] = assignee._identity
        if milestone is not github.GithubObject.NotSet:
            post_parameters["milestone"] = milestone._identity
        if labels is not github.GithubObject.NotSet:
            post_parameters["labels"] = [element.name for element in labels]
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/issues",
            None,
            post_parameters
        )
        return github.Issue.Issue(self._requester, data, completed=True)

    def create_key(self, title, key):
        """
        :calls: `POST /repos/:user/:repo/keys <http://developer.github.com/v3/todo>`_
        :param title: string
        :param key: string
        :rtype: :class:`github.RepositoryKey.RepositoryKey`
        """
        assert isinstance(title, (str, unicode)), title
        assert isinstance(key, (str, unicode)), key
        post_parameters = {
            "title": title,
            "key": key,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/keys",
            None,
            post_parameters
        )
        return github.RepositoryKey.RepositoryKey(self._requester, data, completed=True, repoUrl=self._url)

    def create_label(self, name, color):
        """
        :calls: `POST /repos/:user/:repo/labels <http://developer.github.com/v3/todo>`_
        :param name: string
        :param color: string
        :rtype: :class:`github.Label.Label`
        """
        assert isinstance(name, (str, unicode)), name
        assert isinstance(color, (str, unicode)), color
        post_parameters = {
            "name": name,
            "color": color,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/labels",
            None,
            post_parameters
        )
        return github.Label.Label(self._requester, data, completed=True)

    def create_milestone(self, title, state=github.GithubObject.NotSet, description=github.GithubObject.NotSet, due_on=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:user/:repo/milestones <http://developer.github.com/v3/todo>`_
        :param title: string
        :param state: string
        :param description: string
        :param due_on: date
        :rtype: :class:`github.Milestone.Milestone`
        """
        assert isinstance(title, (str, unicode)), title
        assert state is github.GithubObject.NotSet or isinstance(state, (str, unicode)), state
        assert description is github.GithubObject.NotSet or isinstance(description, (str, unicode)), description
        assert due_on is github.GithubObject.NotSet or isinstance(due_on, datetime.date), due_on
        post_parameters = {
            "title": title,
        }
        if state is not github.GithubObject.NotSet:
            post_parameters["state"] = state
        if description is not github.GithubObject.NotSet:
            post_parameters["description"] = description
        if due_on is not github.GithubObject.NotSet:
            post_parameters["due_on"] = due_on.strftime("%Y-%m-%d")
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/milestones",
            None,
            post_parameters
        )
        return github.Milestone.Milestone(self._requester, data, completed=True)

    def create_pull(self, *args, **kwds):
        """
        :calls: `POST /repos/:user/:repo/pulls <http://developer.github.com/v3/todo>`_
        :param title: string
        :param body: string
        :param issue: :class:`github.Issue.Issue`
        :param base: string
        :param head: string
        :rtype: :class:`github.PullRequest.PullRequest`
        """
        if len(args) + len(kwds) == 4:
            return self.__create_pull_1(*args, **kwds)
        else:
            return self.__create_pull_2(*args, **kwds)

    def __create_pull_1(self, title, body, base, head):
        assert isinstance(title, (str, unicode)), title
        assert isinstance(body, (str, unicode)), body
        assert isinstance(base, (str, unicode)), base
        assert isinstance(head, (str, unicode)), head
        return self.__create_pull(title=title, body=body, base=base, head=head)

    def __create_pull_2(self, issue, base, head):
        assert isinstance(issue, github.Issue.Issue), issue
        assert isinstance(base, (str, unicode)), base
        assert isinstance(head, (str, unicode)), head
        return self.__create_pull(issue=issue._identity, base=base, head=head)

    def __create_pull(self, **kwds):
        post_parameters = kwds
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/pulls",
            None,
            post_parameters
        )
        return github.PullRequest.PullRequest(self._requester, data, completed=True)

    def delete(self):
        """
        :calls: `DELETE /repos/:user/:repo <http://developer.github.com/v3/todo>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url,
            None,
            None
        )

    def edit(self, name, description=github.GithubObject.NotSet, homepage=github.GithubObject.NotSet, public=github.GithubObject.NotSet, has_issues=github.GithubObject.NotSet, has_wiki=github.GithubObject.NotSet, has_downloads=github.GithubObject.NotSet, default_branch=github.GithubObject.NotSet):
        """
        :calls: `PATCH /repos/:user/:repo <http://developer.github.com/v3/todo>`_
        :param name: string
        :param description: string
        :param homepage: string
        :param public: bool
        :param has_issues: bool
        :param has_wiki: bool
        :param has_downloads: bool
        :param default_branch: string
        :rtype: None
        """
        assert isinstance(name, (str, unicode)), name
        assert description is github.GithubObject.NotSet or isinstance(description, (str, unicode)), description
        assert homepage is github.GithubObject.NotSet or isinstance(homepage, (str, unicode)), homepage
        assert public is github.GithubObject.NotSet or isinstance(public, bool), public
        assert has_issues is github.GithubObject.NotSet or isinstance(has_issues, bool), has_issues
        assert has_wiki is github.GithubObject.NotSet or isinstance(has_wiki, bool), has_wiki
        assert has_downloads is github.GithubObject.NotSet or isinstance(has_downloads, bool), has_downloads
        assert default_branch is github.GithubObject.NotSet or isinstance(default_branch, (str, unicode)), default_branch
        post_parameters = {
            "name": name,
        }
        if description is not github.GithubObject.NotSet:
            post_parameters["description"] = description
        if homepage is not github.GithubObject.NotSet:
            post_parameters["homepage"] = homepage
        if public is not github.GithubObject.NotSet:
            post_parameters["public"] = public
        if has_issues is not github.GithubObject.NotSet:
            post_parameters["has_issues"] = has_issues
        if has_wiki is not github.GithubObject.NotSet:
            post_parameters["has_wiki"] = has_wiki
        if has_downloads is not github.GithubObject.NotSet:
            post_parameters["has_downloads"] = has_downloads
        if default_branch is not github.GithubObject.NotSet:
            post_parameters["default_branch"] = default_branch
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            None,
            post_parameters
        )
        self._useAttributes(data)

    def get_archive_link(self, archive_format, ref=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:user/:repo/:archive_format/:ref <http://developer.github.com/v3/todo>`_
        :param archive_format: string
        :param ref: string
        :rtype: string
        """
        assert isinstance(archive_format, (str, unicode)), archive_format
        assert ref is github.GithubObject.NotSet or isinstance(ref, (str, unicode)), ref
        url = self.url + "/" + archive_format
        if ref is not github.GithubObject.NotSet:
            url += "/" + ref
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            url,
            None,
            None
        )
        return headers["location"]

    def get_assignees(self):
        """
        :calls: `GET /repos/:user/:repo/assignees <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/assignees",
            None
        )

    def get_branch(self, branch):
        """
        :calls: `GET /repos/:user/:repo/branches/:branch <http://developer.github.com/v3/todo>`_
        :param branch: string
        :rtype: :class:`github.Branch.Branch`
        """
        assert isinstance(branch, (str, unicode)), branch
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/branches/" + branch,
            None,
            None
        )
        return github.Branch.Branch(self._requester, data, completed=True)

    def get_branches(self):
        """
        :calls: `GET /repos/:user/:repo/branches <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Branch.Branch`
        """
        return github.PaginatedList.PaginatedList(
            github.Branch.Branch,
            self._requester,
            self.url + "/branches",
            None
        )

    def get_collaborators(self):
        """
        :calls: `GET /repos/:user/:repo/collaborators <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/collaborators",
            None
        )

    def get_comment(self, id):
        """
        :calls: `GET /repos/:user/:repo/comments/:id <http://developer.github.com/v3/todo>`_
        :param id: integer
        :rtype: :class:`github.CommitComment.CommitComment`
        """
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/comments/" + str(id),
            None,
            None
        )
        return github.CommitComment.CommitComment(self._requester, data, completed=True)

    def get_comments(self):
        """
        :calls: `GET /repos/:user/:repo/comments <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.CommitComment.CommitComment`
        """
        return github.PaginatedList.PaginatedList(
            github.CommitComment.CommitComment,
            self._requester,
            self.url + "/comments",
            None
        )

    def get_commit(self, sha):
        """
        :calls: `GET /repos/:user/:repo/commits/:sha <http://developer.github.com/v3/todo>`_
        :param sha: string
        :rtype: :class:`github.Commit.Commit`
        """
        assert isinstance(sha, (str, unicode)), sha
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/commits/" + sha,
            None,
            None
        )
        return github.Commit.Commit(self._requester, data, completed=True)

    def get_commits(self, sha=github.GithubObject.NotSet, path=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:user/:repo/commits <http://developer.github.com/v3/todo>`_
        :param sha: string
        :param path: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Commit.Commit`
        """
        assert sha is github.GithubObject.NotSet or isinstance(sha, (str, unicode)), sha
        assert path is github.GithubObject.NotSet or isinstance(path, (str, unicode)), path
        url_parameters = dict()
        if sha is not github.GithubObject.NotSet:
            url_parameters["sha"] = sha
        if path is not github.GithubObject.NotSet:
            url_parameters["path"] = path
        return github.PaginatedList.PaginatedList(
            github.Commit.Commit,
            self._requester,
            self.url + "/commits",
            url_parameters
        )

    def get_contents(self, path, ref=github.GithubObject.NotSet):
        """
        :param path: string
        :param ref: string
        :rtype: :class:`github.ContentFile.ContentFile`
        """
        return self.get_file_contents(path, ref)

    def get_file_contents(self, path, ref=github.GithubObject.NotSet):
        """
        :param path: string
        :param ref: string
        :rtype: :class:`github.ContentFile.ContentFile`
        """
        assert isinstance(path, (str, unicode)), path
        assert ref is github.GithubObject.NotSet or isinstance(ref, (str, unicode)), ref
        url_parameters = dict()
        if ref is not github.GithubObject.NotSet:
            url_parameters["ref"] = ref
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/contents" + path,
            url_parameters,
            None
        )
        return github.ContentFile.ContentFile(self._requester, data, completed=True)

    def get_dir_contents(self, path, ref=github.GithubObject.NotSet):
        """
        :param path: string
        :param ref: string
        :rtype: list of :class:`github.ContentFile.ContentFile`
        """
        assert isinstance(path, (str, unicode)), path
        assert ref is github.GithubObject.NotSet or isinstance(ref, (str, unicode)), ref
        url_parameters = dict()
        if ref is not github.GithubObject.NotSet:
            url_parameters["ref"] = ref
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/contents" + path,
            url_parameters,
            None
        )

        # Handle 302 redirect response
        if headers.get('status') == '302 Found' and headers.get('location'):
            headers, data = self._requester.requestJsonAndCheck(
                "GET",
                headers['location'],
                url_parameters,
                None
            )

        return [
            github.ContentFile.ContentFile(self._requester, attributes, completed=(attributes["type"] != "file"))  # Lazy completion only makes sense for files. See discussion here: https://github.com/jacquev6/PyGithub/issues/140#issuecomment-13481130
            for attributes in data
        ]

    def get_contributors(self):
        """
        :calls: `GET /repos/:user/:repo/contributors <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/contributors",
            None
        )

    def get_download(self, id):
        """
        :calls: `GET /repos/:user/:repo/downloads/:id <http://developer.github.com/v3/todo>`_
        :param id: integer
        :rtype: :class:`github.Download.Download`
        """
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/downloads/" + str(id),
            None,
            None
        )
        return github.Download.Download(self._requester, data, completed=True)

    def get_downloads(self):
        """
        :calls: `GET /repos/:user/:repo/downloads <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Download.Download`
        """
        return github.PaginatedList.PaginatedList(
            github.Download.Download,
            self._requester,
            self.url + "/downloads",
            None
        )

    def get_events(self):
        """
        :calls: `GET /repos/:user/:repo/events <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Event.Event`
        """
        return github.PaginatedList.PaginatedList(
            github.Event.Event,
            self._requester,
            self.url + "/events",
            None
        )

    def get_forks(self):
        """
        :calls: `GET /repos/:user/:repo/forks <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        return github.PaginatedList.PaginatedList(
            Repository,
            self._requester,
            self.url + "/forks",
            None
        )

    def get_git_blob(self, sha):
        """
        :calls: `GET /repos/:user/:repo/git/blobs/:sha <http://developer.github.com/v3/todo>`_
        :param sha: string
        :rtype: :class:`github.GitBlob.GitBlob`
        """
        assert isinstance(sha, (str, unicode)), sha
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/git/blobs/" + sha,
            None,
            None
        )
        return github.GitBlob.GitBlob(self._requester, data, completed=True)

    def get_git_commit(self, sha):
        """
        :calls: `GET /repos/:user/:repo/git/commits/:sha <http://developer.github.com/v3/todo>`_
        :param sha: string
        :rtype: :class:`github.GitCommit.GitCommit`
        """
        assert isinstance(sha, (str, unicode)), sha
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/git/commits/" + sha,
            None,
            None
        )
        return github.GitCommit.GitCommit(self._requester, data, completed=True)

    def get_git_ref(self, ref):
        """
        :calls: `GET /repos/:user/:repo/git/refs/:ref <http://developer.github.com/v3/todo>`_
        :param ref: string
        :rtype: :class:`github.GitRef.GitRef`
        """
        prefix = "/git/refs/"
        if not self._requester.FIX_REPO_GET_GIT_REF:
            prefix = "/git/"
        assert isinstance(ref, (str, unicode)), ref
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + prefix + ref,
            None,
            None
        )
        return github.GitRef.GitRef(self._requester, data, completed=True)

    def get_git_refs(self):
        """
        :calls: `GET /repos/:user/:repo/git/refs <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.GitRef.GitRef`
        """
        return github.PaginatedList.PaginatedList(
            github.GitRef.GitRef,
            self._requester,
            self.url + "/git/refs",
            None
        )

    def get_git_tag(self, sha):
        """
        :calls: `GET /repos/:user/:repo/git/tags/:sha <http://developer.github.com/v3/todo>`_
        :param sha: string
        :rtype: :class:`github.GitTag.GitTag`
        """
        assert isinstance(sha, (str, unicode)), sha
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/git/tags/" + sha,
            None,
            None
        )
        return github.GitTag.GitTag(self._requester, data, completed=True)

    def get_git_tree(self, sha, recursive=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:user/:repo/git/trees/:sha <http://developer.github.com/v3/todo>`_
        :param sha: string
        :param recursive: bool
        :rtype: :class:`github.GitTree.GitTree`
        """
        assert isinstance(sha, (str, unicode)), sha
        assert recursive is github.GithubObject.NotSet or isinstance(recursive, bool), recursive
        url_parameters = dict()
        if recursive is not github.GithubObject.NotSet:
            url_parameters["recursive"] = recursive
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/git/trees/" + sha,
            url_parameters,
            None
        )
        return github.GitTree.GitTree(self._requester, data, completed=True)

    def get_hook(self, id):
        """
        :calls: `GET /repos/:user/:repo/hooks/:id <http://developer.github.com/v3/todo>`_
        :param id: integer
        :rtype: :class:`github.Hook.Hook`
        """
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/hooks/" + str(id),
            None,
            None
        )
        return github.Hook.Hook(self._requester, data, completed=True)

    def get_hooks(self):
        """
        :calls: `GET /repos/:user/:repo/hooks <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Hook.Hook`
        """
        return github.PaginatedList.PaginatedList(
            github.Hook.Hook,
            self._requester,
            self.url + "/hooks",
            None
        )

    def get_issue(self, number):
        """
        :calls: `GET /repos/:user/:repo/issues/:number <http://developer.github.com/v3/todo>`_
        :param number: integer
        :rtype: :class:`github.Issue.Issue`
        """
        assert isinstance(number, (int, long)), number
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/issues/" + str(number),
            None,
            None
        )
        return github.Issue.Issue(self._requester, data, completed=True)

    def get_issues(self, milestone=github.GithubObject.NotSet, state=github.GithubObject.NotSet, assignee=github.GithubObject.NotSet, mentioned=github.GithubObject.NotSet, labels=github.GithubObject.NotSet, sort=github.GithubObject.NotSet, direction=github.GithubObject.NotSet, since=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:user/:repo/issues <http://developer.github.com/v3/todo>`_
        :param milestone: :class:`github.Milestone.Milestone` or "none" or "*"
        :param state: string
        :param assignee: :class:`github.NamedUser.NamedUser` or "none" or "*"
        :param mentioned: :class:`github.NamedUser.NamedUser`
        :param labels: list of :class:`github.Label.Label`
        :param sort: string
        :param direction: string
        :param since: datetime.datetime
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Issue.Issue`
        """
        assert milestone is github.GithubObject.NotSet or milestone == "*" or milestone == "none" or isinstance(milestone, github.Milestone.Milestone), milestone
        assert state is github.GithubObject.NotSet or isinstance(state, (str, unicode)), state
        assert assignee is github.GithubObject.NotSet or assignee == "*" or assignee == "none" or isinstance(assignee, github.NamedUser.NamedUser), assignee
        assert mentioned is github.GithubObject.NotSet or isinstance(mentioned, github.NamedUser.NamedUser), mentioned
        assert labels is github.GithubObject.NotSet or all(isinstance(element, github.Label.Label) for element in labels), labels
        assert sort is github.GithubObject.NotSet or isinstance(sort, (str, unicode)), sort
        assert direction is github.GithubObject.NotSet or isinstance(direction, (str, unicode)), direction
        assert since is github.GithubObject.NotSet or isinstance(since, datetime.datetime), since
        url_parameters = dict()
        if milestone is not github.GithubObject.NotSet:
            if isinstance(milestone, str):
                url_parameters["milestone"] = milestone
            else:
                url_parameters["milestone"] = milestone._identity
        if state is not github.GithubObject.NotSet:
            url_parameters["state"] = state
        if assignee is not github.GithubObject.NotSet:
            if isinstance(assignee, str):
                url_parameters["assignee"] = assignee
            else:
                url_parameters["assignee"] = assignee._identity
        if mentioned is not github.GithubObject.NotSet:
            url_parameters["mentioned"] = mentioned._identity
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

    def get_issues_comments(self, sort=github.GithubObject.NotSet, direction=github.GithubObject.NotSet, since=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:user/:repo/issues/comments <http://developer.github.com/v3/todo>`_
        :param sort: string
        :param direction: string
        :param since: datetime.datetime
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.IssueComment.IssueComment`
        """
        assert sort is github.GithubObject.NotSet or isinstance(sort, (str, unicode)), sort
        assert direction is github.GithubObject.NotSet or isinstance(direction, (str, unicode)), direction
        assert since is github.GithubObject.NotSet or isinstance(since, datetime.datetime), since
        url_parameters = dict()
        if sort is not github.GithubObject.NotSet:
            url_parameters["sort"] = sort
        if direction is not github.GithubObject.NotSet:
            url_parameters["direction"] = direction
        if since is not github.GithubObject.NotSet:
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return github.PaginatedList.PaginatedList(
            github.IssueComment.IssueComment,
            self._requester,
            self.url + "/issues/comments",
            url_parameters
        )

    def get_issues_event(self, id):
        """
        :calls: `GET /repos/:user/:repo/issues/events/:id <http://developer.github.com/v3/todo>`_
        :param id: integer
        :rtype: :class:`github.IssueEvent.IssueEvent`
        """
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/issues/events/" + str(id),
            None,
            None
        )
        return github.IssueEvent.IssueEvent(self._requester, data, completed=True)

    def get_issues_events(self):
        """
        :calls: `GET /repos/:user/:repo/issues/events <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.IssueEvent.IssueEvent`
        """
        return github.PaginatedList.PaginatedList(
            github.IssueEvent.IssueEvent,
            self._requester,
            self.url + "/issues/events",
            None
        )

    def get_key(self, id):
        """
        :calls: `GET /repos/:user/:repo/keys/:id <http://developer.github.com/v3/todo>`_
        :param id: integer
        :rtype: :class:`github.RepositoryKey.RepositoryKey`
        """
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/keys/" + str(id),
            None,
            None
        )
        return github.RepositoryKey.RepositoryKey(self._requester, data, completed=True, repoUrl=self._url)

    def get_keys(self):
        """
        :calls: `GET /repos/:user/:repo/keys <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.RepositoryKey.RepositoryKey`
        """
        return github.PaginatedList.PaginatedList(
            lambda requester, data, completed: github.RepositoryKey.RepositoryKey(requester, data, completed, repoUrl=self._url),
            self._requester,
            self.url + "/keys",
            None
        )

    def get_label(self, name):
        """
        :calls: `GET /repos/:user/:repo/labels/:name <http://developer.github.com/v3/todo>`_
        :param name: string
        :rtype: :class:`github.Label.Label`
        """
        assert isinstance(name, (str, unicode)), name
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/labels/" + urllib.quote(name),
            None,
            None
        )
        return github.Label.Label(self._requester, data, completed=True)

    def get_labels(self):
        """
        :calls: `GET /repos/:user/:repo/labels <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Label.Label`
        """
        return github.PaginatedList.PaginatedList(
            github.Label.Label,
            self._requester,
            self.url + "/labels",
            None
        )

    def get_languages(self):
        """
        :calls: `GET /repos/:user/:repo/languages <http://developer.github.com/v3/todo>`_
        :rtype: dict of string to integer
        """
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/languages",
            None,
            None
        )
        return data

    def get_milestone(self, number):
        """
        :calls: `GET /repos/:user/:repo/milestones/:number <http://developer.github.com/v3/todo>`_
        :param number: integer
        :rtype: :class:`github.Milestone.Milestone`
        """
        assert isinstance(number, (int, long)), number
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/milestones/" + str(number),
            None,
            None
        )
        return github.Milestone.Milestone(self._requester, data, completed=True)

    def get_milestones(self, state=github.GithubObject.NotSet, sort=github.GithubObject.NotSet, direction=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:user/:repo/milestones <http://developer.github.com/v3/todo>`_
        :param state: string
        :param sort: string
        :param direction: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Milestone.Milestone`
        """
        assert state is github.GithubObject.NotSet or isinstance(state, (str, unicode)), state
        assert sort is github.GithubObject.NotSet or isinstance(sort, (str, unicode)), sort
        assert direction is github.GithubObject.NotSet or isinstance(direction, (str, unicode)), direction
        url_parameters = dict()
        if state is not github.GithubObject.NotSet:
            url_parameters["state"] = state
        if sort is not github.GithubObject.NotSet:
            url_parameters["sort"] = sort
        if direction is not github.GithubObject.NotSet:
            url_parameters["direction"] = direction
        return github.PaginatedList.PaginatedList(
            github.Milestone.Milestone,
            self._requester,
            self.url + "/milestones",
            url_parameters
        )

    def get_network_events(self):
        """
        :calls: `GET /networks/:user/:repo/events <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Event.Event`
        """
        return github.PaginatedList.PaginatedList(
            github.Event.Event,
            self._requester,
            "/networks/" + self.owner.login + "/" + self.name + "/events",
            None
        )

    def get_pull(self, number):
        """
        :calls: `GET /repos/:user/:repo/pulls/:number <http://developer.github.com/v3/todo>`_
        :param number: integer
        :rtype: :class:`github.PullRequest.PullRequest`
        """
        assert isinstance(number, (int, long)), number
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/pulls/" + str(number),
            None,
            None
        )
        return github.PullRequest.PullRequest(self._requester, data, completed=True)

    def get_pulls(self, state=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:user/:repo/pulls <http://developer.github.com/v3/todo>`_
        :param state: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.PullRequest.PullRequest`
        """
        assert state is github.GithubObject.NotSet or isinstance(state, (str, unicode)), state
        url_parameters = dict()
        if state is not github.GithubObject.NotSet:
            url_parameters["state"] = state
        return github.PaginatedList.PaginatedList(
            github.PullRequest.PullRequest,
            self._requester,
            self.url + "/pulls",
            url_parameters
        )

    def get_pulls_comments(self, sort=github.GithubObject.NotSet, direction=github.GithubObject.NotSet, since=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:user/:repo/pulls/comments <http://developer.github.com/v3/todo>`_
        :param sort: string
        :param direction: string
        :param since: datetime.datetime
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.PullRequestComment.PullRequestComment`
        """
        return self.get_pulls_review_comments(sort, direction, since)

    def get_pulls_review_comments(self, sort=github.GithubObject.NotSet, direction=github.GithubObject.NotSet, since=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:user/:repo/pulls/comments <http://developer.github.com/v3/todo>`_
        :param sort: string
        :param direction: string
        :param since: datetime.datetime
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.PullRequestComment.PullRequestComment`
        """
        assert sort is github.GithubObject.NotSet or isinstance(sort, (str, unicode)), sort
        assert direction is github.GithubObject.NotSet or isinstance(direction, (str, unicode)), direction
        assert since is github.GithubObject.NotSet or isinstance(since, datetime.datetime), since
        url_parameters = dict()
        if sort is not github.GithubObject.NotSet:
            url_parameters["sort"] = sort
        if direction is not github.GithubObject.NotSet:
            url_parameters["direction"] = direction
        if since is not github.GithubObject.NotSet:
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return github.PaginatedList.PaginatedList(
            github.IssueComment.IssueComment,
            self._requester,
            self.url + "/pulls/comments",
            url_parameters
        )

    def get_readme(self, ref=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:user/:repo/readme <http://developer.github.com/v3/todo>`_
        :param ref: string
        :rtype: :class:`github.ContentFile.ContentFile`
        """
        assert ref is github.GithubObject.NotSet or isinstance(ref, (str, unicode)), ref
        url_parameters = dict()
        if ref is not github.GithubObject.NotSet:
            url_parameters["ref"] = ref
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/readme",
            url_parameters,
            None
        )
        return github.ContentFile.ContentFile(self._requester, data, completed=True)

    def get_stargazers(self):
        """
        :calls: `GET /repos/:user/:repo/stargazers <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/stargazers",
            None
        )

    def get_subscribers(self):
        """
        :calls: `GET /repos/:user/:repo/subscribers <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/subscribers",
            None
        )

    def get_tags(self):
        """
        :calls: `GET /repos/:user/:repo/tags <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Tag.Tag`
        """
        return github.PaginatedList.PaginatedList(
            github.Tag.Tag,
            self._requester,
            self.url + "/tags",
            None
        )

    def get_teams(self):
        """
        :calls: `GET /repos/:user/:repo/teams <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Team.Team`
        """
        return github.PaginatedList.PaginatedList(
            github.Team.Team,
            self._requester,
            self.url + "/teams",
            None
        )

    def get_watchers(self):
        """
        :calls: `GET /repos/:user/:repo/watchers <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/watchers",
            None
        )

    def has_in_assignees(self, assignee):
        """
        :calls: `GET /repos/:user/:repo/assignees/:assignee <http://developer.github.com/v3/todo>`_
        :param assignee: :class:`github.NamedUser.NamedUser`
        :rtype: bool
        """
        assert isinstance(assignee, github.NamedUser.NamedUser), assignee
        status, headers, data = self._requester.requestJson(
            "GET",
            self.url + "/assignees/" + assignee._identity,
            None,
            None
        )
        return status == 204

    def has_in_collaborators(self, collaborator):
        """
        :calls: `GET /repos/:user/:repo/collaborators/:user <http://developer.github.com/v3/todo>`_
        :param collaborator: :class:`github.NamedUser.NamedUser`
        :rtype: bool
        """
        assert isinstance(collaborator, github.NamedUser.NamedUser), collaborator
        status, headers, data = self._requester.requestJson(
            "GET",
            self.url + "/collaborators/" + collaborator._identity,
            None,
            None
        )
        return status == 204

    def legacy_search_issues(self, state, keyword):
        """
        :calls: `GET /legacy/issues/search/:owner/:repository/:state/:keyword <http://developer.github.com/v3/todo>`_
        :param state: "open" or "closed"
        :param keyword: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Issue.Issue`
        """
        assert state in ["open", "closed"], state
        assert isinstance(keyword, (str, unicode)), keyword
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            "/legacy/issues/search/" + self.owner.login + "/" + self.name + "/" + state + "/" + urllib.quote(keyword),
            None,
            None
        )
        return [
            github.Issue.Issue(self._requester, github.Legacy.convertIssue(element), completed=False)
            for element in data["issues"]
        ]

    def merge(self, base, head, commit_message=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:user/:repo/merges <http://developer.github.com/v3/todo>`_
        :param base: string
        :param head: string
        :param commit_message: string
        :rtype: :class:`github.Commit.Commit`
        """
        assert isinstance(base, (str, unicode)), base
        assert isinstance(head, (str, unicode)), head
        assert commit_message is github.GithubObject.NotSet or isinstance(commit_message, (str, unicode)), commit_message
        post_parameters = {
            "base": base,
            "head": head,
        }
        if commit_message is not github.GithubObject.NotSet:
            post_parameters["commit_message"] = commit_message
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/merges",
            None,
            post_parameters
        )
        if data is None:
            return None
        else:
            return github.Commit.Commit(self._requester, data, completed=True)

    def remove_from_collaborators(self, collaborator):
        """
        :calls: `DELETE /repos/:user/:repo/collaborators/:user <http://developer.github.com/v3/todo>`_
        :param collaborator: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(collaborator, github.NamedUser.NamedUser), collaborator
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url + "/collaborators/" + collaborator._identity,
            None,
            None
        )

    def subscribe_to_hub(self, event, callback, secret=github.GithubObject.NotSet):
        """
        :calls: `POST /hub <http://developer.github.com/v3/todo>`_
        :param event: string
        :param callback: string
        :param secret: string
        :rtype: None
        """
        return self._hub("subscribe", event, callback, secret)

    def unsubscribe_from_hub(self, event, callback):
        """
        :calls: `POST /hub <http://developer.github.com/v3/todo>`_
        :param event: string
        :param callback: string
        :param secret: string
        :rtype: None
        """
        return self._hub("unsubscribe", event, callback, github.GithubObject.NotSet)

    def _hub(self, mode, event, callback, secret):
        assert isinstance(mode, (str, unicode)), mode
        assert isinstance(event, (str, unicode)), event
        assert isinstance(callback, (str, unicode)), callback
        assert secret is github.GithubObject.NotSet or isinstance(secret, (str, unicode)), secret

        post_parameters = {
            "hub.mode": mode,
            "hub.topic": "https://github.com/" + self._full_name + "/events/" + event,
            "hub.callback": callback,
        }
        if secret is not github.GithubObject.NotSet:
            post_parameters["hub.secret"] = secret

        responseHeaders, output = self._requester.requestMultipartAndCheck(
            "POST",
            "/hub",
            None,
            post_parameters,
        )

    @property
    def _identity(self):
        return self.owner.login + "/" + self.name

    def _initAttributes(self):
        self._clone_url = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._description = github.GithubObject.NotSet
        self._fork = github.GithubObject.NotSet
        self._forks = github.GithubObject.NotSet
        self._full_name = github.GithubObject.NotSet
        self._git_url = github.GithubObject.NotSet
        self._has_downloads = github.GithubObject.NotSet
        self._has_issues = github.GithubObject.NotSet
        self._has_wiki = github.GithubObject.NotSet
        self._homepage = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._language = github.GithubObject.NotSet
        self._master_branch = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._open_issues = github.GithubObject.NotSet
        self._organization = github.GithubObject.NotSet
        self._owner = github.GithubObject.NotSet
        self._parent = github.GithubObject.NotSet
        self._permissions = github.GithubObject.NotSet
        self._private = github.GithubObject.NotSet
        self._pushed_at = github.GithubObject.NotSet
        self._size = github.GithubObject.NotSet
        self._source = github.GithubObject.NotSet
        self._ssh_url = github.GithubObject.NotSet
        self._svn_url = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._watchers = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "clone_url" in attributes:  # pragma no branch
            assert attributes["clone_url"] is None or isinstance(attributes["clone_url"], (str, unicode)), attributes["clone_url"]
            self._clone_url = attributes["clone_url"]
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "description" in attributes:  # pragma no branch
            assert attributes["description"] is None or isinstance(attributes["description"], (str, unicode)), attributes["description"]
            self._description = attributes["description"]
        if "fork" in attributes:  # pragma no branch
            assert attributes["fork"] is None or isinstance(attributes["fork"], bool), attributes["fork"]
            self._fork = attributes["fork"]
        if "forks" in attributes:  # pragma no branch
            assert attributes["forks"] is None or isinstance(attributes["forks"], (int, long)), attributes["forks"]
            self._forks = attributes["forks"]
        if "full_name" in attributes:  # pragma no branch
            assert attributes["full_name"] is None or isinstance(attributes["full_name"], (str, unicode)), attributes["full_name"]
            self._full_name = attributes["full_name"]
        if "git_url" in attributes:  # pragma no branch
            assert attributes["git_url"] is None or isinstance(attributes["git_url"], (str, unicode)), attributes["git_url"]
            self._git_url = attributes["git_url"]
        if "has_downloads" in attributes:  # pragma no branch
            assert attributes["has_downloads"] is None or isinstance(attributes["has_downloads"], bool), attributes["has_downloads"]
            self._has_downloads = attributes["has_downloads"]
        if "has_issues" in attributes:  # pragma no branch
            assert attributes["has_issues"] is None or isinstance(attributes["has_issues"], bool), attributes["has_issues"]
            self._has_issues = attributes["has_issues"]
        if "has_wiki" in attributes:  # pragma no branch
            assert attributes["has_wiki"] is None or isinstance(attributes["has_wiki"], bool), attributes["has_wiki"]
            self._has_wiki = attributes["has_wiki"]
        if "homepage" in attributes:  # pragma no branch
            assert attributes["homepage"] is None or isinstance(attributes["homepage"], (str, unicode)), attributes["homepage"]
            self._homepage = attributes["homepage"]
        if "html_url" in attributes:  # pragma no branch
            assert attributes["html_url"] is None or isinstance(attributes["html_url"], (str, unicode)), attributes["html_url"]
            self._html_url = attributes["html_url"]
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "language" in attributes:  # pragma no branch
            assert attributes["language"] is None or isinstance(attributes["language"], (str, unicode)), attributes["language"]
            self._language = attributes["language"]
        if "master_branch" in attributes:  # pragma no branch
            assert attributes["master_branch"] is None or isinstance(attributes["master_branch"], (str, unicode)), attributes["master_branch"]
            self._master_branch = attributes["master_branch"]
        if "name" in attributes:  # pragma no branch
            assert attributes["name"] is None or isinstance(attributes["name"], (str, unicode)), attributes["name"]
            self._name = attributes["name"]
        if "open_issues" in attributes:  # pragma no branch
            assert attributes["open_issues"] is None or isinstance(attributes["open_issues"], (int, long)), attributes["open_issues"]
            self._open_issues = attributes["open_issues"]
        if "organization" in attributes:  # pragma no branch
            assert attributes["organization"] is None or isinstance(attributes["organization"], dict), attributes["organization"]
            self._organization = None if attributes["organization"] is None else github.Organization.Organization(self._requester, attributes["organization"], completed=False)
        if "owner" in attributes:  # pragma no branch
            assert attributes["owner"] is None or isinstance(attributes["owner"], dict), attributes["owner"]
            self._owner = None if attributes["owner"] is None else github.NamedUser.NamedUser(self._requester, attributes["owner"], completed=False)
        if "parent" in attributes:  # pragma no branch
            assert attributes["parent"] is None or isinstance(attributes["parent"], dict), attributes["parent"]
            self._parent = None if attributes["parent"] is None else Repository(self._requester, attributes["parent"], completed=False)
        if "permissions" in attributes:  # pragma no branch
            assert attributes["permissions"] is None or isinstance(attributes["permissions"], dict), attributes["permissions"]
            self._permissions = None if attributes["permissions"] is None else github.Permissions.Permissions(self._requester, attributes["permissions"], completed=False)
        if "private" in attributes:  # pragma no branch
            assert attributes["private"] is None or isinstance(attributes["private"], bool), attributes["private"]
            self._private = attributes["private"]
        if "pushed_at" in attributes:  # pragma no branch
            assert attributes["pushed_at"] is None or isinstance(attributes["pushed_at"], (str, unicode)), attributes["pushed_at"]
            self._pushed_at = self._parseDatetime(attributes["pushed_at"])
        if "size" in attributes:  # pragma no branch
            assert attributes["size"] is None or isinstance(attributes["size"], (int, long)), attributes["size"]
            self._size = attributes["size"]
        if "source" in attributes:  # pragma no branch
            assert attributes["source"] is None or isinstance(attributes["source"], dict), attributes["source"]
            self._source = None if attributes["source"] is None else Repository(self._requester, attributes["source"], completed=False)
        if "ssh_url" in attributes:  # pragma no branch
            assert attributes["ssh_url"] is None or isinstance(attributes["ssh_url"], (str, unicode)), attributes["ssh_url"]
            self._ssh_url = attributes["ssh_url"]
        if "svn_url" in attributes:  # pragma no branch
            assert attributes["svn_url"] is None or isinstance(attributes["svn_url"], (str, unicode)), attributes["svn_url"]
            self._svn_url = attributes["svn_url"]
        if "updated_at" in attributes:  # pragma no branch
            assert attributes["updated_at"] is None or isinstance(attributes["updated_at"], (str, unicode)), attributes["updated_at"]
            self._updated_at = self._parseDatetime(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
        if "watchers" in attributes:  # pragma no branch
            assert attributes["watchers"] is None or isinstance(attributes["watchers"], (int, long)), attributes["watchers"]
            self._watchers = attributes["watchers"]
