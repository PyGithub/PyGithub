# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import urllib
import datetime

import GithubObject
import PaginatedList

import Branch
import IssueEvent
import ContentFile
import Label
import InputGitAuthor
import GitBlob
import Organization
import GitRef
import Issue
import Repository
import PullRequest
import RepositoryKey
import NamedUser
import Milestone
import InputGitTreeElement
import Comparison
import CommitComment
import GitCommit
import Team
import Commit
import GitTree
import Hook
import Tag
import GitTag
import Download
import Permissions
import Event
import Legacy


class Repository(GithubObject.GithubObject):
    @property
    def clone_url(self):
        self._completeIfNotSet(self._clone_url)
        return self._NoneIfNotSet(self._clone_url)

    @property
    def created_at(self):
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def description(self):
        self._completeIfNotSet(self._description)
        return self._NoneIfNotSet(self._description)

    @property
    def fork(self):
        self._completeIfNotSet(self._fork)
        return self._NoneIfNotSet(self._fork)

    @property
    def forks(self):
        self._completeIfNotSet(self._forks)
        return self._NoneIfNotSet(self._forks)

    @property
    def full_name(self):
        self._completeIfNotSet(self._full_name)
        return self._NoneIfNotSet(self._full_name)

    @property
    def git_url(self):
        self._completeIfNotSet(self._git_url)
        return self._NoneIfNotSet(self._git_url)

    @property
    def has_downloads(self):
        self._completeIfNotSet(self._has_downloads)
        return self._NoneIfNotSet(self._has_downloads)

    @property
    def has_issues(self):
        self._completeIfNotSet(self._has_issues)
        return self._NoneIfNotSet(self._has_issues)

    @property
    def has_wiki(self):
        self._completeIfNotSet(self._has_wiki)
        return self._NoneIfNotSet(self._has_wiki)

    @property
    def homepage(self):
        self._completeIfNotSet(self._homepage)
        return self._NoneIfNotSet(self._homepage)

    @property
    def html_url(self):
        self._completeIfNotSet(self._html_url)
        return self._NoneIfNotSet(self._html_url)

    @property
    def id(self):
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def language(self):
        self._completeIfNotSet(self._language)
        return self._NoneIfNotSet(self._language)

    @property
    def master_branch(self):
        self._completeIfNotSet(self._master_branch)
        return self._NoneIfNotSet(self._master_branch)

    @property
    def name(self):
        self._completeIfNotSet(self._name)
        return self._NoneIfNotSet(self._name)

    @property
    def open_issues(self):
        self._completeIfNotSet(self._open_issues)
        return self._NoneIfNotSet(self._open_issues)

    @property
    def organization(self):
        self._completeIfNotSet(self._organization)
        return self._NoneIfNotSet(self._organization)

    @property
    def owner(self):
        self._completeIfNotSet(self._owner)
        return self._NoneIfNotSet(self._owner)

    @property
    def parent(self):
        self._completeIfNotSet(self._parent)
        return self._NoneIfNotSet(self._parent)

    @property
    def permissions(self):
        self._completeIfNotSet(self._permissions)
        return self._NoneIfNotSet(self._permissions)

    @property
    def private(self):
        self._completeIfNotSet(self._private)
        return self._NoneIfNotSet(self._private)

    @property
    def pushed_at(self):
        self._completeIfNotSet(self._pushed_at)
        return self._NoneIfNotSet(self._pushed_at)

    @property
    def size(self):
        self._completeIfNotSet(self._size)
        return self._NoneIfNotSet(self._size)

    @property
    def source(self):
        self._completeIfNotSet(self._source)
        return self._NoneIfNotSet(self._source)

    @property
    def ssh_url(self):
        self._completeIfNotSet(self._ssh_url)
        return self._NoneIfNotSet(self._ssh_url)

    @property
    def svn_url(self):
        self._completeIfNotSet(self._svn_url)
        return self._NoneIfNotSet(self._svn_url)

    @property
    def updated_at(self):
        self._completeIfNotSet(self._updated_at)
        return self._NoneIfNotSet(self._updated_at)

    @property
    def url(self):
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    @property
    def watchers(self):
        self._completeIfNotSet(self._watchers)
        return self._NoneIfNotSet(self._watchers)

    def add_to_collaborators(self, collaborator):
        assert isinstance(collaborator, NamedUser.NamedUser), collaborator
        headers, data = self._requester.requestAndCheck(
            "PUT",
            self.url + "/collaborators/" + collaborator._identity,
            None,
            None
        )

    def compare(self, base, head):
        assert isinstance(base, (str, unicode)), base
        assert isinstance(head, (str, unicode)), head
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/compare/" + base + "..." + head,
            None,
            None
        )
        return Comparison.Comparison(self._requester, data, completed=True)

    def create_download(self, name, size, description=GithubObject.NotSet, content_type=GithubObject.NotSet):
        assert isinstance(name, (str, unicode)), name
        assert isinstance(size, (int, long)), size
        assert description is GithubObject.NotSet or isinstance(description, (str, unicode)), description
        assert content_type is GithubObject.NotSet or isinstance(content_type, (str, unicode)), content_type
        post_parameters = {
            "name": name,
            "size": size,
        }
        if description is not GithubObject.NotSet:
            post_parameters["description"] = description
        if content_type is not GithubObject.NotSet:
            post_parameters["content_type"] = content_type
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/downloads",
            None,
            post_parameters
        )
        return Download.Download(self._requester, data, completed=True)

    def create_git_blob(self, content, encoding):
        assert isinstance(content, (str, unicode)), content
        assert isinstance(encoding, (str, unicode)), encoding
        post_parameters = {
            "content": content,
            "encoding": encoding,
        }
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/git/blobs",
            None,
            post_parameters
        )
        return GitBlob.GitBlob(self._requester, data, completed=True)

    def create_git_commit(self, message, tree, parents, author=GithubObject.NotSet, committer=GithubObject.NotSet):
        assert isinstance(message, (str, unicode)), message
        assert isinstance(tree, GitTree.GitTree), tree
        assert all(isinstance(element, GitCommit.GitCommit) for element in parents), parents
        assert author is GithubObject.NotSet or isinstance(author, InputGitAuthor.InputGitAuthor), author
        assert committer is GithubObject.NotSet or isinstance(committer, InputGitAuthor.InputGitAuthor), committer
        post_parameters = {
            "message": message,
            "tree": tree._identity,
            "parents": [element._identity for element in parents],
        }
        if author is not GithubObject.NotSet:
            post_parameters["author"] = author._identity
        if committer is not GithubObject.NotSet:
            post_parameters["committer"] = committer._identity
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/git/commits",
            None,
            post_parameters
        )
        return GitCommit.GitCommit(self._requester, data, completed=True)

    def create_git_ref(self, ref, sha):
        assert isinstance(ref, (str, unicode)), ref
        assert isinstance(sha, (str, unicode)), sha
        post_parameters = {
            "ref": ref,
            "sha": sha,
        }
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/git/refs",
            None,
            post_parameters
        )
        return GitRef.GitRef(self._requester, data, completed=True)

    def create_git_tag(self, tag, message, object, type, tagger=GithubObject.NotSet):
        assert isinstance(tag, (str, unicode)), tag
        assert isinstance(message, (str, unicode)), message
        assert isinstance(object, (str, unicode)), object
        assert isinstance(type, (str, unicode)), type
        assert tagger is GithubObject.NotSet or isinstance(tagger, InputGitAuthor.InputGitAuthor), tagger
        post_parameters = {
            "tag": tag,
            "message": message,
            "object": object,
            "type": type,
        }
        if tagger is not GithubObject.NotSet:
            post_parameters["tagger"] = tagger._identity
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/git/tags",
            None,
            post_parameters
        )
        return GitTag.GitTag(self._requester, data, completed=True)

    def create_git_tree(self, tree, base_tree=GithubObject.NotSet):
        assert all(isinstance(element, InputGitTreeElement.InputGitTreeElement) for element in tree), tree
        assert base_tree is GithubObject.NotSet or isinstance(base_tree, GitTree.GitTree), base_tree
        post_parameters = {
            "tree": [element._identity for element in tree],
        }
        if base_tree is not GithubObject.NotSet:
            post_parameters["base_tree"] = base_tree._identity
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/git/trees",
            None,
            post_parameters
        )
        return GitTree.GitTree(self._requester, data, completed=True)

    def create_hook(self, name, config, events=GithubObject.NotSet, active=GithubObject.NotSet):
        assert isinstance(name, (str, unicode)), name
        assert isinstance(config, dict), config
        assert events is GithubObject.NotSet or all(isinstance(element, (str, unicode)) for element in events), events
        assert active is GithubObject.NotSet or isinstance(active, bool), active
        post_parameters = {
            "name": name,
            "config": config,
        }
        if events is not GithubObject.NotSet:
            post_parameters["events"] = events
        if active is not GithubObject.NotSet:
            post_parameters["active"] = active
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/hooks",
            None,
            post_parameters
        )
        return Hook.Hook(self._requester, data, completed=True)

    def create_issue(self, title, body=GithubObject.NotSet, assignee=GithubObject.NotSet, milestone=GithubObject.NotSet, labels=GithubObject.NotSet):
        assert isinstance(title, (str, unicode)), title
        assert body is GithubObject.NotSet or isinstance(body, (str, unicode)), body
        assert assignee is GithubObject.NotSet or isinstance(assignee, NamedUser.NamedUser), assignee
        assert milestone is GithubObject.NotSet or isinstance(milestone, Milestone.Milestone), milestone
        assert labels is GithubObject.NotSet or all(isinstance(element, Label.Label) for element in labels), labels
        post_parameters = {
            "title": title,
        }
        if body is not GithubObject.NotSet:
            post_parameters["body"] = body
        if assignee is not GithubObject.NotSet:
            post_parameters["assignee"] = assignee._identity
        if milestone is not GithubObject.NotSet:
            post_parameters["milestone"] = milestone._identity
        if labels is not GithubObject.NotSet:
            post_parameters["labels"] = [element.name for element in labels]
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/issues",
            None,
            post_parameters
        )
        return Issue.Issue(self._requester, data, completed=True)

    def create_key(self, title, key):
        assert isinstance(title, (str, unicode)), title
        assert isinstance(key, (str, unicode)), key
        post_parameters = {
            "title": title,
            "key": key,
        }
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/keys",
            None,
            post_parameters
        )
        return RepositoryKey.RepositoryKey(self._requester, data, completed=True, repoUrl=self._url)

    def create_label(self, name, color):
        assert isinstance(name, (str, unicode)), name
        assert isinstance(color, (str, unicode)), color
        post_parameters = {
            "name": name,
            "color": color,
        }
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/labels",
            None,
            post_parameters
        )
        return Label.Label(self._requester, data, completed=True)

    def create_milestone(self, title, state=GithubObject.NotSet, description=GithubObject.NotSet, due_on=GithubObject.NotSet):
        assert isinstance(title, (str, unicode)), title
        assert state is GithubObject.NotSet or isinstance(state, (str, unicode)), state
        assert description is GithubObject.NotSet or isinstance(description, (str, unicode)), description
        assert due_on is GithubObject.NotSet or isinstance(due_on, datetime.date), due_on
        post_parameters = {
            "title": title,
        }
        if state is not GithubObject.NotSet:
            post_parameters["state"] = state
        if description is not GithubObject.NotSet:
            post_parameters["description"] = description
        if due_on is not GithubObject.NotSet:
            post_parameters["due_on"] = due_on.strftime("%Y-%m-%d")
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/milestones",
            None,
            post_parameters
        )
        return Milestone.Milestone(self._requester, data, completed=True)

    def create_pull(self, *args, **kwds):
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
        assert isinstance(issue, Issue.Issue), issue
        assert isinstance(base, (str, unicode)), base
        assert isinstance(head, (str, unicode)), head
        return self.__create_pull(issue=issue._identity, base=base, head=head)

    def __create_pull(self, **kwds):
        post_parameters = kwds
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/pulls",
            None,
            post_parameters
        )
        return PullRequest.PullRequest(self._requester, data, completed=True)

    def delete(self):
        headers, data = self._requester.requestAndCheck(
            "DELETE",
            self.url,
            None,
            None
        )

    def edit(self, name, description=GithubObject.NotSet, homepage=GithubObject.NotSet, public=GithubObject.NotSet, has_issues=GithubObject.NotSet, has_wiki=GithubObject.NotSet, has_downloads=GithubObject.NotSet, default_branch=GithubObject.NotSet):
        assert isinstance(name, (str, unicode)), name
        assert description is GithubObject.NotSet or isinstance(description, (str, unicode)), description
        assert homepage is GithubObject.NotSet or isinstance(homepage, (str, unicode)), homepage
        assert public is GithubObject.NotSet or isinstance(public, bool), public
        assert has_issues is GithubObject.NotSet or isinstance(has_issues, bool), has_issues
        assert has_wiki is GithubObject.NotSet or isinstance(has_wiki, bool), has_wiki
        assert has_downloads is GithubObject.NotSet or isinstance(has_downloads, bool), has_downloads
        assert default_branch is GithubObject.NotSet or isinstance(default_branch, (str, unicode)), default_branch
        post_parameters = {
            "name": name,
        }
        if description is not GithubObject.NotSet:
            post_parameters["description"] = description
        if homepage is not GithubObject.NotSet:
            post_parameters["homepage"] = homepage
        if public is not GithubObject.NotSet:
            post_parameters["public"] = public
        if has_issues is not GithubObject.NotSet:
            post_parameters["has_issues"] = has_issues
        if has_wiki is not GithubObject.NotSet:
            post_parameters["has_wiki"] = has_wiki
        if has_downloads is not GithubObject.NotSet:
            post_parameters["has_downloads"] = has_downloads
        if default_branch is not GithubObject.NotSet:
            post_parameters["default_branch"] = default_branch
        headers, data = self._requester.requestAndCheck(
            "PATCH",
            self.url,
            None,
            post_parameters
        )
        self._useAttributes(data)

    def get_archive_link(self, archive_format, ref=GithubObject.NotSet):
        assert isinstance(archive_format, (str, unicode)), archive_format
        assert ref is GithubObject.NotSet or isinstance(ref, (str, unicode)), ref
        url = self.url + "/" + archive_format
        if ref is not GithubObject.NotSet:
            url += "/" + ref
        headers, data = self._requester.requestAndCheck(
            "GET",
            url,
            None,
            None
        )
        return headers["location"]

    def get_assignees(self):
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self._requester,
            self.url + "/assignees",
            None
        )

    def get_branch(self, branch):
        assert isinstance(branch, (str, unicode)), branch
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/branches/" + branch,
            None,
            None
        )
        return Branch.Branch(self._requester, data, completed=True)

    def get_branches(self):
        return PaginatedList.PaginatedList(
            Branch.Branch,
            self._requester,
            self.url + "/branches",
            None
        )

    def get_collaborators(self):
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self._requester,
            self.url + "/collaborators",
            None
        )

    def get_comment(self, id):
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/comments/" + str(id),
            None,
            None
        )
        return CommitComment.CommitComment(self._requester, data, completed=True)

    def get_comments(self):
        return PaginatedList.PaginatedList(
            CommitComment.CommitComment,
            self._requester,
            self.url + "/comments",
            None
        )

    def get_commit(self, sha):
        assert isinstance(sha, (str, unicode)), sha
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/commits/" + sha,
            None,
            None
        )
        return Commit.Commit(self._requester, data, completed=True)

    def get_commits(self, sha=GithubObject.NotSet, path=GithubObject.NotSet):
        assert sha is GithubObject.NotSet or isinstance(sha, (str, unicode)), sha
        assert path is GithubObject.NotSet or isinstance(path, (str, unicode)), path
        url_parameters = dict()
        if sha is not GithubObject.NotSet:
            url_parameters["sha"] = sha
        if path is not GithubObject.NotSet:
            url_parameters["path"] = path
        return PaginatedList.PaginatedList(
            Commit.Commit,
            self._requester,
            self.url + "/commits",
            url_parameters
        )

    def get_contents(self, path):
        assert isinstance(path, (str, unicode)), path
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/contents" + path,
            None,
            None
        )
        return ContentFile.ContentFile(self._requester, data, completed=True)

    def get_contributors(self):
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self._requester,
            self.url + "/contributors",
            None
        )

    def get_download(self, id):
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/downloads/" + str(id),
            None,
            None
        )
        return Download.Download(self._requester, data, completed=True)

    def get_downloads(self):
        return PaginatedList.PaginatedList(
            Download.Download,
            self._requester,
            self.url + "/downloads",
            None
        )

    def get_events(self):
        return PaginatedList.PaginatedList(
            Event.Event,
            self._requester,
            self.url + "/events",
            None
        )

    def get_forks(self):
        return PaginatedList.PaginatedList(
            Repository,
            self._requester,
            self.url + "/forks",
            None
        )

    def get_git_blob(self, sha):
        assert isinstance(sha, (str, unicode)), sha
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/git/blobs/" + sha,
            None,
            None
        )
        return GitBlob.GitBlob(self._requester, data, completed=True)

    def get_git_commit(self, sha):
        assert isinstance(sha, (str, unicode)), sha
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/git/commits/" + sha,
            None,
            None
        )
        return GitCommit.GitCommit(self._requester, data, completed=True)

    def get_git_ref(self, ref):
        prefix = "/git/refs/"
        if not self._requester.FIX_REPO_GET_GIT_REF:
            prefix = "/git/"
        assert isinstance(ref, (str, unicode)), ref
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + prefix + ref,
            None,
            None
        )
        return GitRef.GitRef(self._requester, data, completed=True)

    def get_git_refs(self):
        return PaginatedList.PaginatedList(
            GitRef.GitRef,
            self._requester,
            self.url + "/git/refs",
            None
        )

    def get_git_tag(self, sha):
        assert isinstance(sha, (str, unicode)), sha
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/git/tags/" + sha,
            None,
            None
        )
        return GitTag.GitTag(self._requester, data, completed=True)

    def get_git_tree(self, sha, recursive=GithubObject.NotSet):
        assert isinstance(sha, (str, unicode)), sha
        assert recursive is GithubObject.NotSet or isinstance(recursive, bool), recursive
        url_parameters = dict()
        if recursive is not GithubObject.NotSet:
            url_parameters["recursive"] = recursive
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/git/trees/" + sha,
            url_parameters,
            None
        )
        return GitTree.GitTree(self._requester, data, completed=True)

    def get_hook(self, id):
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/hooks/" + str(id),
            None,
            None
        )
        return Hook.Hook(self._requester, data, completed=True)

    def get_hooks(self):
        return PaginatedList.PaginatedList(
            Hook.Hook,
            self._requester,
            self.url + "/hooks",
            None
        )

    def get_issue(self, number):
        assert isinstance(number, (int, long)), number
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/issues/" + str(number),
            None,
            None
        )
        return Issue.Issue(self._requester, data, completed=True)

    def get_issues(self, milestone=GithubObject.NotSet, state=GithubObject.NotSet, assignee=GithubObject.NotSet, mentioned=GithubObject.NotSet, labels=GithubObject.NotSet, sort=GithubObject.NotSet, direction=GithubObject.NotSet, since=GithubObject.NotSet):
        assert milestone is GithubObject.NotSet or milestone == "*" or milestone == "none" or isinstance(milestone, Milestone.Milestone), milestone
        assert state is GithubObject.NotSet or isinstance(state, (str, unicode)), state
        assert assignee is GithubObject.NotSet or assignee == "*" or assignee == "none" or isinstance(assignee, NamedUser.NamedUser), assignee
        assert mentioned is GithubObject.NotSet or isinstance(mentioned, NamedUser.NamedUser), mentioned
        assert labels is GithubObject.NotSet or all(isinstance(element, Label.Label) for element in labels), labels
        assert sort is GithubObject.NotSet or isinstance(sort, (str, unicode)), sort
        assert direction is GithubObject.NotSet or isinstance(direction, (str, unicode)), direction
        assert since is GithubObject.NotSet or isinstance(since, datetime.datetime), since
        url_parameters = dict()
        if milestone is not GithubObject.NotSet:
            if isinstance(milestone, str):
                url_parameters["milestone"] = milestone
            else:
                url_parameters["milestone"] = milestone._identity
        if state is not GithubObject.NotSet:
            url_parameters["state"] = state
        if assignee is not GithubObject.NotSet:
            if isinstance(assignee, str):
                url_parameters["assignee"] = assignee
            else:
                url_parameters["assignee"] = assignee._identity
        if mentioned is not GithubObject.NotSet:
            url_parameters["mentioned"] = mentioned._identity
        if labels is not GithubObject.NotSet:
            url_parameters["labels"] = ",".join(label.name for label in labels)
        if sort is not GithubObject.NotSet:
            url_parameters["sort"] = sort
        if direction is not GithubObject.NotSet:
            url_parameters["direction"] = direction
        if since is not GithubObject.NotSet:
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return PaginatedList.PaginatedList(
            Issue.Issue,
            self._requester,
            self.url + "/issues",
            url_parameters
        )

    def get_issues_event(self, id):
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/issues/events/" + str(id),
            None,
            None
        )
        return IssueEvent.IssueEvent(self._requester, data, completed=True)

    def get_issues_events(self):
        return PaginatedList.PaginatedList(
            IssueEvent.IssueEvent,
            self._requester,
            self.url + "/issues/events",
            None
        )

    def get_key(self, id):
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/keys/" + str(id),
            None,
            None
        )
        return RepositoryKey.RepositoryKey(self._requester, data, completed=True, repoUrl=self._url)

    def get_keys(self):
        return PaginatedList.PaginatedList(
            lambda requester, data, completed: RepositoryKey.RepositoryKey(requester, data, completed, repoUrl=self._url),
            self._requester,
            self.url + "/keys",
            None
        )

    def get_label(self, name):
        assert isinstance(name, (str, unicode)), name
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/labels/" + urllib.quote(name),
            None,
            None
        )
        return Label.Label(self._requester, data, completed=True)

    def get_labels(self):
        return PaginatedList.PaginatedList(
            Label.Label,
            self._requester,
            self.url + "/labels",
            None
        )

    def get_languages(self):
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/languages",
            None,
            None
        )
        return data

    def get_milestone(self, number):
        assert isinstance(number, (int, long)), number
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/milestones/" + str(number),
            None,
            None
        )
        return Milestone.Milestone(self._requester, data, completed=True)

    def get_milestones(self, state=GithubObject.NotSet, sort=GithubObject.NotSet, direction=GithubObject.NotSet):
        assert state is GithubObject.NotSet or isinstance(state, (str, unicode)), state
        assert sort is GithubObject.NotSet or isinstance(sort, (str, unicode)), sort
        assert direction is GithubObject.NotSet or isinstance(direction, (str, unicode)), direction
        url_parameters = dict()
        if state is not GithubObject.NotSet:
            url_parameters["state"] = state
        if sort is not GithubObject.NotSet:
            url_parameters["sort"] = sort
        if direction is not GithubObject.NotSet:
            url_parameters["direction"] = direction
        return PaginatedList.PaginatedList(
            Milestone.Milestone,
            self._requester,
            self.url + "/milestones",
            url_parameters
        )

    def get_network_events(self):
        return PaginatedList.PaginatedList(
            Event.Event,
            self._requester,
            "/networks/" + self.owner.login + "/" + self.name + "/events",
            None
        )

    def get_pull(self, number):
        assert isinstance(number, (int, long)), number
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/pulls/" + str(number),
            None,
            None
        )
        return PullRequest.PullRequest(self._requester, data, completed=True)

    def get_pulls(self, state=GithubObject.NotSet):
        assert state is GithubObject.NotSet or isinstance(state, (str, unicode)), state
        url_parameters = dict()
        if state is not GithubObject.NotSet:
            url_parameters["state"] = state
        return PaginatedList.PaginatedList(
            PullRequest.PullRequest,
            self._requester,
            self.url + "/pulls",
            url_parameters
        )

    def get_readme(self):
        headers, data = self._requester.requestAndCheck(
            "GET",
            self.url + "/readme",
            None,
            None
        )
        return ContentFile.ContentFile(self._requester, data, completed=True)

    def get_stargazers(self):
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self._requester,
            self.url + "/stargazers",
            None
        )

    def get_subscribers(self):
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self._requester,
            self.url + "/subscribers",
            None
        )

    def get_tags(self):
        return PaginatedList.PaginatedList(
            Tag.Tag,
            self._requester,
            self.url + "/tags",
            None
        )

    def get_teams(self):
        return PaginatedList.PaginatedList(
            Team.Team,
            self._requester,
            self.url + "/teams",
            None
        )

    def get_watchers(self):
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self._requester,
            self.url + "/watchers",
            None
        )

    def has_in_assignees(self, assignee):
        assert isinstance(assignee, NamedUser.NamedUser), assignee
        status, headers, data = self._requester.requestRaw(
            "GET",
            self.url + "/assignees/" + assignee._identity,
            None,
            None
        )
        return status == 204

    def has_in_collaborators(self, collaborator):
        assert isinstance(collaborator, NamedUser.NamedUser), collaborator
        status, headers, data = self._requester.requestRaw(
            "GET",
            self.url + "/collaborators/" + collaborator._identity,
            None,
            None
        )
        return status == 204

    def legacy_search_issues(self, state, keyword):
        assert state in ["open", "closed"], state
        assert isinstance(keyword, (str, unicode)), keyword
        headers, data = self._requester.requestAndCheck(
            "GET",
            "/legacy/issues/search/" + self.owner.login + "/" + self.name + "/" + state + "/" + urllib.quote(keyword),
            None,
            None
        )
        return [
            Issue.Issue(self._requester, Legacy.convertIssue(element), completed=False)
            for element in data["issues"]
        ]

    def merge(self, base, head, commit_message=GithubObject.NotSet):
        assert isinstance(base, (str, unicode)), base
        assert isinstance(head, (str, unicode)), head
        assert commit_message is GithubObject.NotSet or isinstance(commit_message, (str, unicode)), commit_message
        post_parameters = {
            "base": base,
            "head": head,
        }
        if commit_message is not GithubObject.NotSet:
            post_parameters["commit_message"] = commit_message
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/merges",
            None,
            post_parameters
        )
        if data is None:
            return None
        else:
            return Commit.Commit(self._requester, data, completed=True)

    def remove_from_collaborators(self, collaborator):
        assert isinstance(collaborator, NamedUser.NamedUser), collaborator
        headers, data = self._requester.requestAndCheck(
            "DELETE",
            self.url + "/collaborators/" + collaborator._identity,
            None,
            None
        )

    @property
    def _identity(self):
        return self.owner.login + "/" + self.name

    def _initAttributes(self):
        self._clone_url = GithubObject.NotSet
        self._created_at = GithubObject.NotSet
        self._description = GithubObject.NotSet
        self._fork = GithubObject.NotSet
        self._forks = GithubObject.NotSet
        self._full_name = GithubObject.NotSet
        self._git_url = GithubObject.NotSet
        self._has_downloads = GithubObject.NotSet
        self._has_issues = GithubObject.NotSet
        self._has_wiki = GithubObject.NotSet
        self._homepage = GithubObject.NotSet
        self._html_url = GithubObject.NotSet
        self._id = GithubObject.NotSet
        self._language = GithubObject.NotSet
        self._master_branch = GithubObject.NotSet
        self._name = GithubObject.NotSet
        self._open_issues = GithubObject.NotSet
        self._organization = GithubObject.NotSet
        self._owner = GithubObject.NotSet
        self._parent = GithubObject.NotSet
        self._permissions = GithubObject.NotSet
        self._private = GithubObject.NotSet
        self._pushed_at = GithubObject.NotSet
        self._size = GithubObject.NotSet
        self._source = GithubObject.NotSet
        self._ssh_url = GithubObject.NotSet
        self._svn_url = GithubObject.NotSet
        self._updated_at = GithubObject.NotSet
        self._url = GithubObject.NotSet
        self._watchers = GithubObject.NotSet

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
            self._organization = None if attributes["organization"] is None else Organization.Organization(self._requester, attributes["organization"], completed=False)
        if "owner" in attributes:  # pragma no branch
            assert attributes["owner"] is None or isinstance(attributes["owner"], dict), attributes["owner"]
            self._owner = None if attributes["owner"] is None else NamedUser.NamedUser(self._requester, attributes["owner"], completed=False)
        if "parent" in attributes:  # pragma no branch
            assert attributes["parent"] is None or isinstance(attributes["parent"], dict), attributes["parent"]
            self._parent = None if attributes["parent"] is None else Repository(self._requester, attributes["parent"], completed=False)
        if "permissions" in attributes:  # pragma no branch
            assert attributes["permissions"] is None or isinstance(attributes["permissions"], dict), attributes["permissions"]
            self._permissions = None if attributes["permissions"] is None else Permissions.Permissions(self._requester, attributes["permissions"], completed=False)
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
