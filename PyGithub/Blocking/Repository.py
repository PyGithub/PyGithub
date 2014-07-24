# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class Repository(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.AuthenticatedUser.create_fork`
      * :meth:`.AuthenticatedUser.create_repo`
      * :meth:`.AuthenticatedUser.get_repo`
      * :meth:`.AuthenticatedUser.get_repos`
      * :meth:`.AuthenticatedUser.get_starred`
      * :meth:`.AuthenticatedUser.get_subscriptions`
      * :meth:`.Github.get_repo`
      * :meth:`.Github.get_repos`
      * :meth:`.Organization.create_fork`
      * :meth:`.Organization.create_repo`
      * :meth:`.Organization.get_repo`
      * :meth:`.Organization.get_repos`
      * :meth:`.Repository.get_forks`
      * :attr:`.Repository.parent`
      * :attr:`.Repository.source`
      * :meth:`.Team.get_repos`
      * :meth:`.User.get_repo`
      * :meth:`.User.get_repos`
      * :meth:`.User.get_starred`
      * :meth:`.User.get_subscriptions`

    Methods accepting instances of this class as parameter:
      * :meth:`.AuthenticatedUser.add_to_starred`
      * :meth:`.AuthenticatedUser.create_fork`
      * :meth:`.AuthenticatedUser.create_subscription`
      * :meth:`.AuthenticatedUser.get_subscription`
      * :meth:`.AuthenticatedUser.has_in_starred`
      * :meth:`.AuthenticatedUser.remove_from_starred`
      * :meth:`.Github.get_repos`
      * :meth:`.Organization.create_fork`
      * :meth:`.Organization.create_team`
      * :meth:`.Team.add_to_repos`
      * :meth:`.Team.has_in_repos`
      * :meth:`.Team.remove_from_repos`
    """

    class AnonymousContributor(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.Repository.get_contributors`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, contributions=None, name=None, type=None, **kwds):
            super(Repository.AnonymousContributor, self)._initAttributes(**kwds)
            self.__contributions = _rcv.Attribute("Repository.AnonymousContributor.contributions", _rcv.IntConverter, contributions)
            self.__name = _rcv.Attribute("Repository.AnonymousContributor.name", _rcv.StringConverter, name)
            self.__type = _rcv.Attribute("Repository.AnonymousContributor.type", _rcv.StringConverter, type)

        @property
        def contributions(self):
            """
            :type: :class:`int`
            """
            return self.__contributions.value

        @property
        def name(self):
            """
            :type: :class:`string`
            """
            return self.__name.value

        @property
        def type(self):
            """
            :type: :class:`string`
            """
            return self.__type.value

    class Branch(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.Repository.get_branch`
          * :meth:`.Repository.get_branches`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, commit=None, name=None, _links=None, **kwds):
            import PyGithub.Blocking.Commit
            super(Repository.Branch, self)._initAttributes(**kwds)
            self.__commit = _rcv.Attribute("Repository.Branch.commit", _rcv.ClassConverter(self.Session, PyGithub.Blocking.Commit.Commit), commit)
            self.__name = _rcv.Attribute("Repository.Branch.name", _rcv.StringConverter, name)

        @property
        def commit(self):
            """
            :type: :class:`.Commit`
            """
            return self.__commit.value

        @property
        def name(self):
            """
            :type: :class:`string`
            """
            return self.__name.value

    class ContentCommit(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.Repository.create_file`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, commit=None, content=None, **kwds):
            import PyGithub.Blocking.File
            import PyGithub.Blocking.GitCommit
            super(Repository.ContentCommit, self)._initAttributes(**kwds)
            self.__commit = _rcv.Attribute("Repository.ContentCommit.commit", _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitCommit.GitCommit), commit)
            self.__content = _rcv.Attribute("Repository.ContentCommit.content", _rcv.ClassConverter(self.Session, PyGithub.Blocking.File.File), content)

        @property
        def commit(self):
            """
            :type: :class:`.GitCommit`
            """
            return self.__commit.value

        @property
        def content(self):
            """
            :type: :class:`.File`
            """
            return self.__content.value

    class Permissions(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.Repository.permissions`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, admin=None, pull=None, push=None, **kwds):
            super(Repository.Permissions, self)._initAttributes(**kwds)
            self.__admin = _rcv.Attribute("Repository.Permissions.admin", _rcv.BoolConverter, admin)
            self.__pull = _rcv.Attribute("Repository.Permissions.pull", _rcv.BoolConverter, pull)
            self.__push = _rcv.Attribute("Repository.Permissions.push", _rcv.BoolConverter, push)

        def _updateAttributes(self, admin=None, pull=None, push=None, **kwds):
            super(Repository.Permissions, self)._updateAttributes(**kwds)
            self.__admin.update(admin)
            self.__pull.update(pull)
            self.__push.update(push)

        @property
        def admin(self):
            """
            :type: :class:`bool`
            """
            return self.__admin.value

        @property
        def pull(self):
            """
            :type: :class:`bool`
            """
            return self.__pull.value

        @property
        def push(self):
            """
            :type: :class:`bool`
            """
            return self.__push.value

    class Tag(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.Repository.get_tags`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, commit=None, name=None, tarball_url=None, zipball_url=None, **kwds):
            import PyGithub.Blocking.Commit
            super(Repository.Tag, self)._initAttributes(**kwds)
            self.__commit = _rcv.Attribute("Repository.Tag.commit", _rcv.ClassConverter(self.Session, PyGithub.Blocking.Commit.Commit), commit)
            self.__name = _rcv.Attribute("Repository.Tag.name", _rcv.StringConverter, name)
            self.__tarball_url = _rcv.Attribute("Repository.Tag.tarball_url", _rcv.StringConverter, tarball_url)
            self.__zipball_url = _rcv.Attribute("Repository.Tag.zipball_url", _rcv.StringConverter, zipball_url)

        @property
        def commit(self):
            """
            :type: :class:`.Commit`
            """
            return self.__commit.value

        @property
        def name(self):
            """
            :type: :class:`string`
            """
            return self.__name.value

        @property
        def tarball_url(self):
            """
            :type: :class:`string`
            """
            return self.__tarball_url.value

        @property
        def zipball_url(self):
            """
            :type: :class:`string`
            """
            return self.__zipball_url.value

    def _initAttributes(self, archive_url=_rcv.Absent, assignees_url=_rcv.Absent, blobs_url=_rcv.Absent, branches_url=_rcv.Absent, clone_url=_rcv.Absent, collaborators_url=_rcv.Absent, comments_url=_rcv.Absent, commits_url=_rcv.Absent, compare_url=_rcv.Absent, contents_url=_rcv.Absent, contributors_url=_rcv.Absent, created_at=_rcv.Absent, default_branch=_rcv.Absent, description=_rcv.Absent, downloads_url=_rcv.Absent, events_url=_rcv.Absent, fork=_rcv.Absent, forks_count=_rcv.Absent, forks_url=_rcv.Absent, full_name=_rcv.Absent, git_commits_url=_rcv.Absent, git_refs_url=_rcv.Absent, git_tags_url=_rcv.Absent, git_url=_rcv.Absent, has_issues=_rcv.Absent, has_wiki=_rcv.Absent, homepage=_rcv.Absent, hooks_url=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, issue_comment_url=_rcv.Absent, issue_events_url=_rcv.Absent, issues_url=_rcv.Absent, keys_url=_rcv.Absent, labels_url=_rcv.Absent, language=_rcv.Absent, languages_url=_rcv.Absent, merges_url=_rcv.Absent, milestones_url=_rcv.Absent, mirror_url=_rcv.Absent, name=_rcv.Absent, network_count=_rcv.Absent, notifications_url=_rcv.Absent, open_issues_count=_rcv.Absent, owner=_rcv.Absent, parent=_rcv.Absent, permissions=_rcv.Absent, private=_rcv.Absent, pulls_url=_rcv.Absent, pushed_at=_rcv.Absent, releases_url=_rcv.Absent, size=_rcv.Absent, source=_rcv.Absent, ssh_url=_rcv.Absent, stargazers_count=_rcv.Absent, stargazers_url=_rcv.Absent, statuses_url=_rcv.Absent, subscribers_count=_rcv.Absent, subscribers_url=_rcv.Absent, subscription_url=_rcv.Absent, svn_url=_rcv.Absent, tags_url=_rcv.Absent, teams_url=_rcv.Absent, trees_url=_rcv.Absent, updated_at=_rcv.Absent, watchers_count=_rcv.Absent, forks=None, has_downloads=None, master_branch=None, open_issues=None, organization=None, watchers=None, **kwds):
        import PyGithub.Blocking.Organization
        import PyGithub.Blocking.User
        super(Repository, self)._initAttributes(**kwds)
        self.__archive_url = _rcv.Attribute("Repository.archive_url", _rcv.StringConverter, archive_url)
        self.__assignees_url = _rcv.Attribute("Repository.assignees_url", _rcv.StringConverter, assignees_url)
        self.__blobs_url = _rcv.Attribute("Repository.blobs_url", _rcv.StringConverter, blobs_url)
        self.__branches_url = _rcv.Attribute("Repository.branches_url", _rcv.StringConverter, branches_url)
        self.__clone_url = _rcv.Attribute("Repository.clone_url", _rcv.StringConverter, clone_url)
        self.__collaborators_url = _rcv.Attribute("Repository.collaborators_url", _rcv.StringConverter, collaborators_url)
        self.__comments_url = _rcv.Attribute("Repository.comments_url", _rcv.StringConverter, comments_url)
        self.__commits_url = _rcv.Attribute("Repository.commits_url", _rcv.StringConverter, commits_url)
        self.__compare_url = _rcv.Attribute("Repository.compare_url", _rcv.StringConverter, compare_url)
        self.__contents_url = _rcv.Attribute("Repository.contents_url", _rcv.StringConverter, contents_url)
        self.__contributors_url = _rcv.Attribute("Repository.contributors_url", _rcv.StringConverter, contributors_url)
        self.__created_at = _rcv.Attribute("Repository.created_at", _rcv.DatetimeConverter, created_at)
        self.__default_branch = _rcv.Attribute("Repository.default_branch", _rcv.StringConverter, default_branch)
        self.__description = _rcv.Attribute("Repository.description", _rcv.StringConverter, description)
        self.__downloads_url = _rcv.Attribute("Repository.downloads_url", _rcv.StringConverter, downloads_url)
        self.__events_url = _rcv.Attribute("Repository.events_url", _rcv.StringConverter, events_url)
        self.__fork = _rcv.Attribute("Repository.fork", _rcv.BoolConverter, fork)
        self.__forks_count = _rcv.Attribute("Repository.forks_count", _rcv.IntConverter, forks_count)
        self.__forks_url = _rcv.Attribute("Repository.forks_url", _rcv.StringConverter, forks_url)
        self.__full_name = _rcv.Attribute("Repository.full_name", _rcv.StringConverter, full_name)
        self.__git_commits_url = _rcv.Attribute("Repository.git_commits_url", _rcv.StringConverter, git_commits_url)
        self.__git_refs_url = _rcv.Attribute("Repository.git_refs_url", _rcv.StringConverter, git_refs_url)
        self.__git_tags_url = _rcv.Attribute("Repository.git_tags_url", _rcv.StringConverter, git_tags_url)
        self.__git_url = _rcv.Attribute("Repository.git_url", _rcv.StringConverter, git_url)
        self.__has_issues = _rcv.Attribute("Repository.has_issues", _rcv.BoolConverter, has_issues)
        self.__has_wiki = _rcv.Attribute("Repository.has_wiki", _rcv.BoolConverter, has_wiki)
        self.__homepage = _rcv.Attribute("Repository.homepage", _rcv.StringConverter, homepage)
        self.__hooks_url = _rcv.Attribute("Repository.hooks_url", _rcv.StringConverter, hooks_url)
        self.__html_url = _rcv.Attribute("Repository.html_url", _rcv.StringConverter, html_url)
        self.__id = _rcv.Attribute("Repository.id", _rcv.IntConverter, id)
        self.__issue_comment_url = _rcv.Attribute("Repository.issue_comment_url", _rcv.StringConverter, issue_comment_url)
        self.__issue_events_url = _rcv.Attribute("Repository.issue_events_url", _rcv.StringConverter, issue_events_url)
        self.__issues_url = _rcv.Attribute("Repository.issues_url", _rcv.StringConverter, issues_url)
        self.__keys_url = _rcv.Attribute("Repository.keys_url", _rcv.StringConverter, keys_url)
        self.__labels_url = _rcv.Attribute("Repository.labels_url", _rcv.StringConverter, labels_url)
        self.__language = _rcv.Attribute("Repository.language", _rcv.StringConverter, language)
        self.__languages_url = _rcv.Attribute("Repository.languages_url", _rcv.StringConverter, languages_url)
        self.__merges_url = _rcv.Attribute("Repository.merges_url", _rcv.StringConverter, merges_url)
        self.__milestones_url = _rcv.Attribute("Repository.milestones_url", _rcv.StringConverter, milestones_url)
        self.__mirror_url = _rcv.Attribute("Repository.mirror_url", _rcv.StringConverter, mirror_url)
        self.__name = _rcv.Attribute("Repository.name", _rcv.StringConverter, name)
        self.__network_count = _rcv.Attribute("Repository.network_count", _rcv.IntConverter, network_count)
        self.__notifications_url = _rcv.Attribute("Repository.notifications_url", _rcv.StringConverter, notifications_url)
        self.__open_issues_count = _rcv.Attribute("Repository.open_issues_count", _rcv.IntConverter, open_issues_count)
        self.__owner = _rcv.Attribute("Repository.owner", _rcv.KeyedStructureUnionConverter("type", dict(Organization=_rcv.ClassConverter(self.Session, PyGithub.Blocking.Organization.Organization), User=_rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User))), owner)
        self.__parent = _rcv.Attribute("Repository.parent", _rcv.ClassConverter(self.Session, Repository), parent)
        self.__permissions = _rcv.Attribute("Repository.permissions", _rcv.StructureConverter(self.Session, Repository.Permissions), permissions)
        self.__private = _rcv.Attribute("Repository.private", _rcv.BoolConverter, private)
        self.__pulls_url = _rcv.Attribute("Repository.pulls_url", _rcv.StringConverter, pulls_url)
        self.__pushed_at = _rcv.Attribute("Repository.pushed_at", _rcv.DatetimeConverter, pushed_at)
        self.__releases_url = _rcv.Attribute("Repository.releases_url", _rcv.StringConverter, releases_url)
        self.__size = _rcv.Attribute("Repository.size", _rcv.IntConverter, size)
        self.__source = _rcv.Attribute("Repository.source", _rcv.ClassConverter(self.Session, Repository), source)
        self.__ssh_url = _rcv.Attribute("Repository.ssh_url", _rcv.StringConverter, ssh_url)
        self.__stargazers_count = _rcv.Attribute("Repository.stargazers_count", _rcv.IntConverter, stargazers_count)
        self.__stargazers_url = _rcv.Attribute("Repository.stargazers_url", _rcv.StringConverter, stargazers_url)
        self.__statuses_url = _rcv.Attribute("Repository.statuses_url", _rcv.StringConverter, statuses_url)
        self.__subscribers_count = _rcv.Attribute("Repository.subscribers_count", _rcv.IntConverter, subscribers_count)
        self.__subscribers_url = _rcv.Attribute("Repository.subscribers_url", _rcv.StringConverter, subscribers_url)
        self.__subscription_url = _rcv.Attribute("Repository.subscription_url", _rcv.StringConverter, subscription_url)
        self.__svn_url = _rcv.Attribute("Repository.svn_url", _rcv.StringConverter, svn_url)
        self.__tags_url = _rcv.Attribute("Repository.tags_url", _rcv.StringConverter, tags_url)
        self.__teams_url = _rcv.Attribute("Repository.teams_url", _rcv.StringConverter, teams_url)
        self.__trees_url = _rcv.Attribute("Repository.trees_url", _rcv.StringConverter, trees_url)
        self.__updated_at = _rcv.Attribute("Repository.updated_at", _rcv.DatetimeConverter, updated_at)
        self.__watchers_count = _rcv.Attribute("Repository.watchers_count", _rcv.IntConverter, watchers_count)

    def _updateAttributes(self, eTag, archive_url=_rcv.Absent, assignees_url=_rcv.Absent, blobs_url=_rcv.Absent, branches_url=_rcv.Absent, clone_url=_rcv.Absent, collaborators_url=_rcv.Absent, comments_url=_rcv.Absent, commits_url=_rcv.Absent, compare_url=_rcv.Absent, contents_url=_rcv.Absent, contributors_url=_rcv.Absent, created_at=_rcv.Absent, default_branch=_rcv.Absent, description=_rcv.Absent, downloads_url=_rcv.Absent, events_url=_rcv.Absent, fork=_rcv.Absent, forks_count=_rcv.Absent, forks_url=_rcv.Absent, full_name=_rcv.Absent, git_commits_url=_rcv.Absent, git_refs_url=_rcv.Absent, git_tags_url=_rcv.Absent, git_url=_rcv.Absent, has_issues=_rcv.Absent, has_wiki=_rcv.Absent, homepage=_rcv.Absent, hooks_url=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, issue_comment_url=_rcv.Absent, issue_events_url=_rcv.Absent, issues_url=_rcv.Absent, keys_url=_rcv.Absent, labels_url=_rcv.Absent, language=_rcv.Absent, languages_url=_rcv.Absent, merges_url=_rcv.Absent, milestones_url=_rcv.Absent, mirror_url=_rcv.Absent, name=_rcv.Absent, network_count=_rcv.Absent, notifications_url=_rcv.Absent, open_issues_count=_rcv.Absent, owner=_rcv.Absent, parent=_rcv.Absent, permissions=_rcv.Absent, private=_rcv.Absent, pulls_url=_rcv.Absent, pushed_at=_rcv.Absent, releases_url=_rcv.Absent, size=_rcv.Absent, source=_rcv.Absent, ssh_url=_rcv.Absent, stargazers_count=_rcv.Absent, stargazers_url=_rcv.Absent, statuses_url=_rcv.Absent, subscribers_count=_rcv.Absent, subscribers_url=_rcv.Absent, subscription_url=_rcv.Absent, svn_url=_rcv.Absent, tags_url=_rcv.Absent, teams_url=_rcv.Absent, trees_url=_rcv.Absent, updated_at=_rcv.Absent, watchers_count=_rcv.Absent, forks=None, has_downloads=None, master_branch=None, open_issues=None, organization=None, watchers=None, **kwds):
        super(Repository, self)._updateAttributes(eTag, **kwds)
        self.__archive_url.update(archive_url)
        self.__assignees_url.update(assignees_url)
        self.__blobs_url.update(blobs_url)
        self.__branches_url.update(branches_url)
        self.__clone_url.update(clone_url)
        self.__collaborators_url.update(collaborators_url)
        self.__comments_url.update(comments_url)
        self.__commits_url.update(commits_url)
        self.__compare_url.update(compare_url)
        self.__contents_url.update(contents_url)
        self.__contributors_url.update(contributors_url)
        self.__created_at.update(created_at)
        self.__default_branch.update(default_branch)
        self.__description.update(description)
        self.__downloads_url.update(downloads_url)
        self.__events_url.update(events_url)
        self.__fork.update(fork)
        self.__forks_count.update(forks_count)
        self.__forks_url.update(forks_url)
        self.__full_name.update(full_name)
        self.__git_commits_url.update(git_commits_url)
        self.__git_refs_url.update(git_refs_url)
        self.__git_tags_url.update(git_tags_url)
        self.__git_url.update(git_url)
        self.__has_issues.update(has_issues)
        self.__has_wiki.update(has_wiki)
        self.__homepage.update(homepage)
        self.__hooks_url.update(hooks_url)
        self.__html_url.update(html_url)
        self.__id.update(id)
        self.__issue_comment_url.update(issue_comment_url)
        self.__issue_events_url.update(issue_events_url)
        self.__issues_url.update(issues_url)
        self.__keys_url.update(keys_url)
        self.__labels_url.update(labels_url)
        self.__language.update(language)
        self.__languages_url.update(languages_url)
        self.__merges_url.update(merges_url)
        self.__milestones_url.update(milestones_url)
        self.__mirror_url.update(mirror_url)
        self.__name.update(name)
        self.__network_count.update(network_count)
        self.__notifications_url.update(notifications_url)
        self.__open_issues_count.update(open_issues_count)
        self.__owner.update(owner)
        self.__parent.update(parent)
        self.__permissions.update(permissions)
        self.__private.update(private)
        self.__pulls_url.update(pulls_url)
        self.__pushed_at.update(pushed_at)
        self.__releases_url.update(releases_url)
        self.__size.update(size)
        self.__source.update(source)
        self.__ssh_url.update(ssh_url)
        self.__stargazers_count.update(stargazers_count)
        self.__stargazers_url.update(stargazers_url)
        self.__statuses_url.update(statuses_url)
        self.__subscribers_count.update(subscribers_count)
        self.__subscribers_url.update(subscribers_url)
        self.__subscription_url.update(subscription_url)
        self.__svn_url.update(svn_url)
        self.__tags_url.update(tags_url)
        self.__teams_url.update(teams_url)
        self.__trees_url.update(trees_url)
        self.__updated_at.update(updated_at)
        self.__watchers_count.update(watchers_count)

    @property
    def archive_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__archive_url.needsLazyCompletion)
        return self.__archive_url.value

    @property
    def assignees_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__assignees_url.needsLazyCompletion)
        return self.__assignees_url.value

    @property
    def blobs_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__blobs_url.needsLazyCompletion)
        return self.__blobs_url.value

    @property
    def branches_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__branches_url.needsLazyCompletion)
        return self.__branches_url.value

    @property
    def clone_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__clone_url.needsLazyCompletion)
        return self.__clone_url.value

    @property
    def collaborators_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__collaborators_url.needsLazyCompletion)
        return self.__collaborators_url.value

    @property
    def comments_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__comments_url.needsLazyCompletion)
        return self.__comments_url.value

    @property
    def commits_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__commits_url.needsLazyCompletion)
        return self.__commits_url.value

    @property
    def compare_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__compare_url.needsLazyCompletion)
        return self.__compare_url.value

    @property
    def contents_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__contents_url.needsLazyCompletion)
        return self.__contents_url.value

    @property
    def contributors_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__contributors_url.needsLazyCompletion)
        return self.__contributors_url.value

    @property
    def created_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__created_at.needsLazyCompletion)
        return self.__created_at.value

    @property
    def default_branch(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__default_branch.needsLazyCompletion)
        return self.__default_branch.value

    @property
    def description(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__description.needsLazyCompletion)
        return self.__description.value

    @property
    def downloads_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__downloads_url.needsLazyCompletion)
        return self.__downloads_url.value

    @property
    def events_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__events_url.needsLazyCompletion)
        return self.__events_url.value

    @property
    def fork(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__fork.needsLazyCompletion)
        return self.__fork.value

    @property
    def forks_count(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__forks_count.needsLazyCompletion)
        return self.__forks_count.value

    @property
    def forks_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__forks_url.needsLazyCompletion)
        return self.__forks_url.value

    @property
    def full_name(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__full_name.needsLazyCompletion)
        return self.__full_name.value

    @property
    def git_commits_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__git_commits_url.needsLazyCompletion)
        return self.__git_commits_url.value

    @property
    def git_refs_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__git_refs_url.needsLazyCompletion)
        return self.__git_refs_url.value

    @property
    def git_tags_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__git_tags_url.needsLazyCompletion)
        return self.__git_tags_url.value

    @property
    def git_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__git_url.needsLazyCompletion)
        return self.__git_url.value

    @property
    def has_issues(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__has_issues.needsLazyCompletion)
        return self.__has_issues.value

    @property
    def has_wiki(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__has_wiki.needsLazyCompletion)
        return self.__has_wiki.value

    @property
    def homepage(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__homepage.needsLazyCompletion)
        return self.__homepage.value

    @property
    def hooks_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__hooks_url.needsLazyCompletion)
        return self.__hooks_url.value

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
    def issue_comment_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__issue_comment_url.needsLazyCompletion)
        return self.__issue_comment_url.value

    @property
    def issue_events_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__issue_events_url.needsLazyCompletion)
        return self.__issue_events_url.value

    @property
    def issues_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__issues_url.needsLazyCompletion)
        return self.__issues_url.value

    @property
    def keys_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__keys_url.needsLazyCompletion)
        return self.__keys_url.value

    @property
    def labels_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__labels_url.needsLazyCompletion)
        return self.__labels_url.value

    @property
    def language(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__language.needsLazyCompletion)
        return self.__language.value

    @property
    def languages_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__languages_url.needsLazyCompletion)
        return self.__languages_url.value

    @property
    def merges_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__merges_url.needsLazyCompletion)
        return self.__merges_url.value

    @property
    def milestones_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__milestones_url.needsLazyCompletion)
        return self.__milestones_url.value

    @property
    def mirror_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__mirror_url.needsLazyCompletion)
        return self.__mirror_url.value

    @property
    def name(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__name.needsLazyCompletion)
        return self.__name.value

    @property
    def network_count(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__network_count.needsLazyCompletion)
        return self.__network_count.value

    @property
    def notifications_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__notifications_url.needsLazyCompletion)
        return self.__notifications_url.value

    @property
    def open_issues_count(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__open_issues_count.needsLazyCompletion)
        return self.__open_issues_count.value

    @property
    def owner(self):
        """
        :type: :class:`.User` or :class:`.Organization`
        """
        self._completeLazily(self.__owner.needsLazyCompletion)
        return self.__owner.value

    @property
    def parent(self):
        """
        :type: :class:`.Repository`
        """
        self._completeLazily(self.__parent.needsLazyCompletion)
        return self.__parent.value

    @property
    def permissions(self):
        """
        :type: :class:`.Permissions`
        """
        self._completeLazily(self.__permissions.needsLazyCompletion)
        return self.__permissions.value

    @property
    def private(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__private.needsLazyCompletion)
        return self.__private.value

    @property
    def pulls_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__pulls_url.needsLazyCompletion)
        return self.__pulls_url.value

    @property
    def pushed_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__pushed_at.needsLazyCompletion)
        return self.__pushed_at.value

    @property
    def releases_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__releases_url.needsLazyCompletion)
        return self.__releases_url.value

    @property
    def size(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__size.needsLazyCompletion)
        return self.__size.value

    @property
    def source(self):
        """
        :type: :class:`.Repository`
        """
        self._completeLazily(self.__source.needsLazyCompletion)
        return self.__source.value

    @property
    def ssh_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__ssh_url.needsLazyCompletion)
        return self.__ssh_url.value

    @property
    def stargazers_count(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__stargazers_count.needsLazyCompletion)
        return self.__stargazers_count.value

    @property
    def stargazers_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__stargazers_url.needsLazyCompletion)
        return self.__stargazers_url.value

    @property
    def statuses_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__statuses_url.needsLazyCompletion)
        return self.__statuses_url.value

    @property
    def subscribers_count(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__subscribers_count.needsLazyCompletion)
        return self.__subscribers_count.value

    @property
    def subscribers_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__subscribers_url.needsLazyCompletion)
        return self.__subscribers_url.value

    @property
    def subscription_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__subscription_url.needsLazyCompletion)
        return self.__subscription_url.value

    @property
    def svn_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__svn_url.needsLazyCompletion)
        return self.__svn_url.value

    @property
    def tags_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__tags_url.needsLazyCompletion)
        return self.__tags_url.value

    @property
    def teams_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__teams_url.needsLazyCompletion)
        return self.__teams_url.value

    @property
    def trees_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__trees_url.needsLazyCompletion)
        return self.__trees_url.value

    @property
    def updated_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__updated_at.needsLazyCompletion)
        return self.__updated_at.value

    @property
    def watchers_count(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__watchers_count.needsLazyCompletion)
        return self.__watchers_count.value

    def add_to_collaborators(self, username):
        """
        Calls the `PUT /repos/:owner/:repo/collaborators/:username <http://developer.github.com/v3/repos/collaborators#add-collaborator>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.Entity.login`)
        :rtype: None
        """

        username = _snd.normalizeUserLogin(username)

        url = uritemplate.expand(self.collaborators_url, collaborator=username)
        r = self.Session._request("PUT", url)

    def create_file(self, path, message, content, branch=None, author=None, committer=None):
        """
        Calls the `PUT /repos/:owner/:repo/contents/:path <http://developer.github.com/v3/repos/contents#update-a-file>`__ end point.

        The following methods also call this end point:
          * :meth:`.File.edit`

        :param path: mandatory :class:`string`
        :param message: mandatory :class:`string`
        :param content: mandatory :class:`string`
        :param branch: optional :class:`string`
        :param author: optional :class:`GitAuthor`
        :param committer: optional :class:`GitAuthor`
        :rtype: :class:`.ContentCommit`
        """

        path = _snd.normalizeString(path)
        message = _snd.normalizeString(message)
        content = _snd.normalizeString(content)
        if branch is not None:
            branch = _snd.normalizeString(branch)
        if author is not None:
            author = _snd.normalizeGitAuthor(author)
        if committer is not None:
            committer = _snd.normalizeGitAuthor(committer)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/contents/{path}", owner=self.owner.login, path=path, repo=self.name)
        postArguments = _snd.dictionary(author=author, branch=branch, committer=committer, content=content, message=message)
        r = self.Session._request("PUT", url, postArguments=postArguments)
        return _rcv.StructureConverter(self.Session, Repository.ContentCommit)(None, r.json())

    def create_git_blob(self, content, encoding):
        """
        Calls the `POST /repos/:owner/:repo/git/blobs <http://developer.github.com/v3/git/blobs#create-a-blob>`__ end point.

        This is the only method calling this end point.

        :param content: mandatory :class:`string`
        :param encoding: mandatory :class:`string`
        :rtype: :class:`.GitBlob`
        """
        import PyGithub.Blocking.GitBlob

        content = _snd.normalizeString(content)
        encoding = _snd.normalizeString(encoding)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/git/blobs", owner=self.owner.login, repo=self.name)
        postArguments = _snd.dictionary(content=content, encoding=encoding)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitBlob.GitBlob)(None, r.json())

    def create_git_commit(self, message, tree, parents, committer=None, author=None):
        """
        Calls the `POST /repos/:owner/:repo/git/commits <http://developer.github.com/v3/git/commits#create-a-commit>`__ end point.

        This is the only method calling this end point.

        :param message: mandatory :class:`string`
        :param tree: mandatory :class:`.GitTree` or :class:`string` (its :attr:`.GitObject.sha`)
        :param parents: mandatory :class:`list` of :class:`.GitCommit` or :class:`string` (its :attr:`.GitObject.sha`)
        :param committer: optional :class:`GitAuthor`
        :param author: optional :class:`GitAuthor`
        :rtype: :class:`.GitCommit`
        """
        import PyGithub.Blocking.GitCommit

        message = _snd.normalizeString(message)
        tree = _snd.normalizeGitTreeSha(tree)
        parents = _snd.normalizeList(_snd.normalizeGitCommitSha, parents)
        if committer is not None:
            committer = _snd.normalizeGitAuthor(committer)
        if author is not None:
            author = _snd.normalizeGitAuthor(author)

        url = uritemplate.expand(self.git_commits_url, owner=self.owner.login, repo=self.name)
        postArguments = _snd.dictionary(author=author, committer=committer, message=message, parents=parents, tree=tree)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitCommit.GitCommit)(None, r.json(), r.headers.get("ETag"))

    def create_git_ref(self, ref, sha):
        """
        Calls the `POST /repos/:owner/:repo/git/refs <http://developer.github.com/v3/git/refs#create-a-reference>`__ end point.

        This is the only method calling this end point.

        :param ref: mandatory :class:`string`
        :param sha: mandatory :class:`string`
        :rtype: :class:`.GitRef`
        """
        import PyGithub.Blocking.GitRef

        ref = _snd.normalizeString(ref)
        sha = _snd.normalizeString(sha)

        url = uritemplate.expand(self.git_refs_url, owner=self.owner.login, repo=self.name)
        postArguments = _snd.dictionary(ref=ref, sha=sha)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitRef.GitRef)(None, r.json(), r.headers.get("ETag"))

    def create_git_tag(self, tag, message, object, type, tagger=None):
        """
        Calls the `POST /repos/:owner/:repo/git/tags <http://developer.github.com/v3/git/tags#create-a-tag-object>`__ end point.

        This is the only method calling this end point.

        :param tag: mandatory :class:`string`
        :param message: mandatory :class:`string`
        :param object: mandatory :class:`string`
        :param type: mandatory :class:`string`
        :param tagger: optional :class:`GitAuthor`
        :rtype: :class:`.GitTag`
        """
        import PyGithub.Blocking.GitTag

        tag = _snd.normalizeString(tag)
        message = _snd.normalizeString(message)
        object = _snd.normalizeString(object)
        type = _snd.normalizeString(type)
        if tagger is not None:
            tagger = _snd.normalizeGitAuthor(tagger)

        url = uritemplate.expand(self.git_tags_url, owner=self.owner.login, repo=self.name)
        postArguments = _snd.dictionary(message=message, object=object, tag=tag, tagger=tagger, type=type)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitTag.GitTag)(None, r.json(), r.headers.get("ETag"))

    def create_git_tree(self, tree):
        """
        Calls the `POST /repos/:owner/:repo/git/trees <http://developer.github.com/v3/git/trees#create-a-tree>`__ end point.

        The following methods also call this end point:
          * :meth:`.GitTree.create_modified_copy`

        :param tree: mandatory :class:`list` of :class:`dict`
        :rtype: :class:`.GitTree`
        """
        import PyGithub.Blocking.GitTree

        tree = _snd.normalizeList(_snd.normalizeDict, tree)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/git/trees", owner=self.owner.login, repo=self.name)
        postArguments = _snd.dictionary(tree=tree)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitTree.GitTree)(None, r.json(), r.headers.get("ETag"))

    def create_issue(self, title, body=None, assignee=None, milestone=None, labels=None):
        """
        Calls the `POST /repos/:owner/:repo/issues <http://developer.github.com/v3/issues#create-an-issue>`__ end point.

        This is the only method calling this end point.

        :param title: mandatory :class:`string`
        :param body: optional :class:`string`
        :param assignee: optional :class:`.User` or :class:`string` (its :attr:`.Entity.login`)
        :param milestone: optional :class:`.Milestone` or :class:`int` (its :attr:`.Milestone.number`)
        :param labels: optional :class:`list` of :class:`.Label` or :class:`string` (its :attr:`.Label.name`)
        :rtype: :class:`.Issue`
        """
        import PyGithub.Blocking.Issue

        title = _snd.normalizeString(title)
        if body is not None:
            body = _snd.normalizeString(body)
        if assignee is not None:
            assignee = _snd.normalizeUserLogin(assignee)
        if milestone is not None:
            milestone = _snd.normalizeMilestoneNumber(milestone)
        if labels is not None:
            labels = _snd.normalizeList(_snd.normalizeLabelName, labels)

        url = uritemplate.expand(self.issues_url)
        postArguments = _snd.dictionary(assignee=assignee, body=body, labels=labels, milestone=milestone, title=title)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Issue.Issue)(None, r.json(), r.headers.get("ETag"))

    def create_key(self, title, key):
        """
        Calls the `POST /repos/:owner/:repo/keys <http://developer.github.com/v3/repos/keys#create>`__ end point.

        This is the only method calling this end point.

        :param title: mandatory :class:`string`
        :param key: mandatory :class:`string`
        :rtype: :class:`.PublicKey`
        """
        import PyGithub.Blocking.PublicKey

        title = _snd.normalizeString(title)
        key = _snd.normalizeString(key)

        url = uritemplate.expand(self.keys_url)
        postArguments = _snd.dictionary(key=key, title=title)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.PublicKey.PublicKey)(None, r.json(), r.headers.get("ETag"))

    def delete(self):
        """
        Calls the `DELETE /repos/:owner/:repo <http://developer.github.com/v3/repos#delete-a-repository>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand(self.url)
        r = self.Session._request("DELETE", url)

    def edit(self, name=None, description=None, homepage=None, private=None, has_issues=None, has_wiki=None, default_branch=None):
        """
        Calls the `PATCH /repos/:owner/:repo <http://developer.github.com/v3/repos#edit>`__ end point.

        This is the only method calling this end point.

        :param name: optional :class:`string`
        :param description: optional :class:`string` or :class:`Reset`
        :param homepage: optional :class:`string` or :class:`Reset`
        :param private: optional :class:`bool`
        :param has_issues: optional :class:`bool`
        :param has_wiki: optional :class:`bool`
        :param default_branch: optional :class:`string`
        :rtype: None
        """

        if name is not None:
            name = _snd.normalizeString(name)
        if description is not None:
            description = _snd.normalizeStringReset(description)
        if homepage is not None:
            homepage = _snd.normalizeStringReset(homepage)
        if private is not None:
            private = _snd.normalizeBool(private)
        if has_issues is not None:
            has_issues = _snd.normalizeBool(has_issues)
        if has_wiki is not None:
            has_wiki = _snd.normalizeBool(has_wiki)
        if default_branch is not None:
            default_branch = _snd.normalizeString(default_branch)

        if name is None:
            name = self.name

        url = uritemplate.expand(self.url)
        postArguments = _snd.dictionary(default_branch=default_branch, description=description, has_issues=has_issues, has_wiki=has_wiki, homepage=homepage, name=name, private=private)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())

    def get_assignees(self, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/assignees <http://developer.github.com/v3/issues/assignees#list-assignees>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """
        import PyGithub.Blocking.User

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.assignees_url)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User))(None, r)

    def get_branch(self, branch):
        """
        Calls the `GET /repos/:owner/:repo/branches/:branch <http://developer.github.com/v3/repos#get-branch>`__ end point.

        This is the only method calling this end point.

        :param branch: mandatory :class:`string`
        :rtype: :class:`.Branch`
        """

        branch = _snd.normalizeString(branch)

        url = uritemplate.expand(self.branches_url, branch=branch)
        r = self.Session._request("GET", url)
        return _rcv.StructureConverter(self.Session, Repository.Branch)(None, r.json())

    def get_branches(self, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/branches <http://developer.github.com/v3/repos#list-branches>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Branch`
        """

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.branches_url)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.StructureConverter(self.Session, Repository.Branch))(None, r)

    def get_collaborators(self, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/collaborators <http://developer.github.com/v3/repos/collaborators#list>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """
        import PyGithub.Blocking.User

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.collaborators_url)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User))(None, r)

    def get_commit(self, sha):
        """
        Calls the `GET /repos/:owner/:repo/commits/:sha <http://developer.github.com/v3/repos/commits#get-a-single-commit>`__ end point.

        This is the only method calling this end point.

        :param sha: mandatory :class:`string`
        :rtype: :class:`.Commit`
        """
        import PyGithub.Blocking.Commit

        sha = _snd.normalizeString(sha)

        url = uritemplate.expand(self.commits_url, sha=sha)
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Commit.Commit)(None, r.json(), r.headers.get("ETag"))

    def get_commits(self, sha=None, path=None, author=None, since=None, until=None, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/commits <http://developer.github.com/v3/repos/commits#list-commits-on-a-repository>`__ end point.

        This is the only method calling this end point.

        :param sha: optional :class:`string`
        :param path: optional :class:`string`
        :param author: optional :class:`.User` or :class:`string` (its :attr:`.Entity.login`)
        :param since: optional :class:`datetime`
        :param until: optional :class:`datetime`
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Commit`
        """
        import PyGithub.Blocking.Commit

        if sha is not None:
            sha = _snd.normalizeString(sha)
        if path is not None:
            path = _snd.normalizeString(path)
        if author is not None:
            author = _snd.normalizeUserLogin(author)
        if since is not None:
            since = _snd.normalizeDatetime(since)
        if until is not None:
            until = _snd.normalizeDatetime(until)
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.commits_url)
        urlArguments = _snd.dictionary(author=author, path=path, per_page=per_page, sha=sha, since=since, until=until)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Commit.Commit))(None, r)

    def get_contents(self, path, ref=None):
        """
        Calls the `GET /repos/:owner/:repo/contents/:path <http://developer.github.com/v3/repos/contents#get-contents>`__ end point.

        The following methods also call this end point:
          * :meth:`.Dir.get_contents`

        :param path: mandatory :class:`string`
        :param ref: optional :class:`string`
        :rtype: :class:`.File` or :class:`.Submodule` or :class:`.SymLink` or :class:`list` of :class:`.File` or :class:`.Dir` or :class:`.Submodule` or :class:`.SymLink`
        """
        import PyGithub.Blocking.Dir
        import PyGithub.Blocking.File
        import PyGithub.Blocking.Submodule
        import PyGithub.Blocking.SymLink

        path = _snd.normalizeString(path)
        if ref is not None:
            ref = _snd.normalizeString(ref)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/contents/{path}", owner=self.owner.login, path=path, repo=self.name)
        urlArguments = _snd.dictionary(ref=ref)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.FirstMatchUnionConverter(_rcv.KeyedStructureUnionConverter("type", dict(file=_rcv.ClassConverter(self.Session, PyGithub.Blocking.File.File), submodule=_rcv.ClassConverter(self.Session, PyGithub.Blocking.Submodule.Submodule), symlink=_rcv.ClassConverter(self.Session, PyGithub.Blocking.SymLink.SymLink))), _rcv.ListConverter(_rcv.FileDirSubmoduleSymLinkUnionConverter(_rcv.ClassConverter(self.Session, PyGithub.Blocking.File.File), _rcv.ClassConverter(self.Session, PyGithub.Blocking.Dir.Dir), _rcv.ClassConverter(self.Session, PyGithub.Blocking.Submodule.Submodule), _rcv.ClassConverter(self.Session, PyGithub.Blocking.SymLink.SymLink))))(None, r.json())

    def get_contributors(self, anon=None, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/contributors <http://developer.github.com/v3/repos#list-contributors>`__ end point.

        This is the only method calling this end point.

        :param anon: optional :class:`bool`
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Contributor` or :class:`.AnonymousContributor`
        """
        import PyGithub.Blocking.Contributor

        if anon is not None:
            anon = _snd.normalizeBool(anon)
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.contributors_url)
        urlArguments = _snd.dictionary(anon=anon, per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.KeyedStructureUnionConverter("type", dict(Anonymous=_rcv.StructureConverter(self.Session, Repository.AnonymousContributor), User=_rcv.ClassConverter(self.Session, PyGithub.Blocking.Contributor.Contributor))))(None, r)

    def get_forks(self, sort=None, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/forks <http://developer.github.com/v3/repos/forks#list-forks>`__ end point.

        This is the only method calling this end point.

        :param sort: optional "newest" or "oldest" or "stargazers"
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """

        if sort is not None:
            sort = _snd.normalizeEnum(sort, "newest", "oldest", "stargazers")
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.forks_url)
        urlArguments = _snd.dictionary(per_page=per_page, sort=sort)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, Repository))(None, r)

    def get_git_blob(self, sha):
        """
        Calls the `GET /repos/:owner/:repo/git/blobs/:sha <http://developer.github.com/v3/git/blobs#get-a-blob>`__ end point.

        This is the only method calling this end point.

        :param sha: mandatory :class:`string`
        :rtype: :class:`.GitBlob`
        """
        import PyGithub.Blocking.GitBlob

        sha = _snd.normalizeString(sha)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/git/blobs/{sha}", owner=self.owner.login, repo=self.name, sha=sha)
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitBlob.GitBlob)(None, r.json(), r.headers.get("ETag"))

    def get_git_commit(self, sha):
        """
        Calls the `GET /repos/:owner/:repo/git/commits/:sha <http://developer.github.com/v3/git/commits#get-a-commit>`__ end point.

        This is the only method calling this end point.

        :param sha: mandatory :class:`string`
        :rtype: :class:`.GitCommit`
        """
        import PyGithub.Blocking.GitCommit

        sha = _snd.normalizeString(sha)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/git/commits/{sha}", owner=self.owner.login, repo=self.name, sha=sha)
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitCommit.GitCommit)(None, r.json(), r.headers.get("ETag"))

    def get_git_ref(self, ref):
        """
        Calls the `GET /repos/:owner/:repo/git/refs/:ref <http://developer.github.com/v3/git/refs#get-a-reference>`__ end point.

        This is the only method calling this end point.

        :param ref: mandatory :class:`string`
        :rtype: :class:`.GitRef`
        """
        import PyGithub.Blocking.GitRef

        ref = _snd.normalizeString(ref)

        assert ref.startswith("refs/")
        url = uritemplate.expand(self.git_refs_url) + ref[4:]
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitRef.GitRef)(None, r.json(), r.headers.get("ETag"))

    def get_git_refs(self, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/git/refs <http://developer.github.com/v3/git/refs#get-all-references>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.GitRef`
        """
        import PyGithub.Blocking.GitRef

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.git_refs_url)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitRef.GitRef))(None, r)

    def get_git_tag(self, sha):
        """
        Calls the `GET /repos/:owner/:repo/git/tags/:sha <http://developer.github.com/v3/git/tags#get-a-tag>`__ end point.

        This is the only method calling this end point.

        :param sha: mandatory :class:`string`
        :rtype: :class:`.GitTag`
        """
        import PyGithub.Blocking.GitTag

        sha = _snd.normalizeString(sha)

        url = uritemplate.expand(self.git_tags_url, sha=sha)
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitTag.GitTag)(None, r.json(), r.headers.get("ETag"))

    def get_git_tree(self, sha):
        """
        Calls the `GET /repos/:owner/:repo/git/trees/:sha <http://developer.github.com/v3/git/trees#get-a-tree>`__ end point.

        This is the only method calling this end point.

        :param sha: mandatory :class:`string`
        :rtype: :class:`.GitTree`
        """
        import PyGithub.Blocking.GitTree

        sha = _snd.normalizeString(sha)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/git/trees/{sha}", owner=self.owner.login, repo=self.name, sha=sha)
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitTree.GitTree)(None, r.json(), r.headers.get("ETag"))

    def get_issue(self, number):
        """
        Calls the `GET /repos/:owner/:repo/issues/:number <http://developer.github.com/v3/issues#get-a-single-issue>`__ end point.

        This is the only method calling this end point.

        :param number: mandatory :class:`int`
        :rtype: :class:`.Issue`
        """
        import PyGithub.Blocking.Issue

        number = _snd.normalizeInt(number)

        url = uritemplate.expand(self.issues_url, number=str(number))
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Issue.Issue)(None, r.json(), r.headers.get("ETag"))

    def get_issues(self, milestone=None, state=None, assignee=None, creator=None, mentioned=None, labels=None, sort=None, direction=None, since=None, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/issues <http://developer.github.com/v3/issues#list-issues-for-a-repository>`__ end point.

        This is the only method calling this end point.

        :param milestone: optional :class:`.Milestone` or :class:`int` (its :attr:`.Milestone.number`)
        :param state: optional "close" or "open"
        :param assignee: optional :class:`.User` or :class:`string` (its :attr:`.Entity.login`)
        :param creator: optional :class:`.User` or :class:`string` (its :attr:`.Entity.login`)
        :param mentioned: optional :class:`.User` or :class:`string` (its :attr:`.Entity.login`)
        :param labels: optional :class:`list` of :class:`.Label` or :class:`string` (its :attr:`.Label.name`)
        :param sort: optional "comments" or "created" or "updated"
        :param direction: optional "asc" or "desc"
        :param since: optional :class:`datetime`
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Issue`
        """
        import PyGithub.Blocking.Issue

        if milestone is not None:
            milestone = _snd.normalizeMilestoneNumber(milestone)
        if state is not None:
            state = _snd.normalizeEnum(state, "close", "open")
        if assignee is not None:
            assignee = _snd.normalizeUserLogin(assignee)
        if creator is not None:
            creator = _snd.normalizeUserLogin(creator)
        if mentioned is not None:
            mentioned = _snd.normalizeUserLogin(mentioned)
        if labels is not None:
            labels = _snd.normalizeList(_snd.normalizeLabelName, labels)
        if sort is not None:
            sort = _snd.normalizeEnum(sort, "comments", "created", "updated")
        if direction is not None:
            direction = _snd.normalizeEnum(direction, "asc", "desc")
        if since is not None:
            since = _snd.normalizeDatetime(since)
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.issues_url)
        urlArguments = _snd.dictionary(assignee=assignee, creator=creator, direction=direction, labels=labels, mentioned=mentioned, milestone=milestone, per_page=per_page, since=since, sort=sort, state=state)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Issue.Issue))(None, r)

    def get_key(self, id):
        """
        Calls the `GET /repos/:owner/:repo/keys/:id <http://developer.github.com/v3/repos/keys#get>`__ end point.

        This is the only method calling this end point.

        :param id: mandatory :class:`int`
        :rtype: :class:`.PublicKey`
        """
        import PyGithub.Blocking.PublicKey

        id = _snd.normalizeInt(id)

        url = uritemplate.expand(self.keys_url, key_id=str(id))
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.PublicKey.PublicKey)(None, r.json(), r.headers.get("ETag"))

    def get_keys(self):
        """
        Calls the `GET /repos/:owner/:repo/keys <http://developer.github.com/v3/repos/keys#list>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`list` of :class:`.PublicKey`
        """
        import PyGithub.Blocking.PublicKey

        url = uritemplate.expand(self.keys_url)
        r = self.Session._request("GET", url)
        return _rcv.ListConverter(_rcv.ClassConverter(self.Session, PyGithub.Blocking.PublicKey.PublicKey))(None, r.json())

    def get_label(self, name):
        """
        Calls the `GET /repos/:owner/:repo/labels/:name <http://developer.github.com/v3/issues/labels#get-a-single-label>`__ end point.

        This is the only method calling this end point.

        :param name: mandatory :class:`string`
        :rtype: :class:`.Label`
        """
        import PyGithub.Blocking.Label

        name = _snd.normalizeString(name)

        url = uritemplate.expand(self.labels_url, name=name)
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Label.Label)(None, r.json(), r.headers.get("ETag"))

    def get_milestone(self, number):
        """
        Calls the `GET /repos/:owner/:repo/milestones/:number <http://developer.github.com/v3/issues/milestones#get-a-single-milestone>`__ end point.

        This is the only method calling this end point.

        :param number: mandatory :class:`int`
        :rtype: :class:`.Milestone`
        """
        import PyGithub.Blocking.Milestone

        number = _snd.normalizeInt(number)

        url = uritemplate.expand(self.milestones_url, number=str(number))
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Milestone.Milestone)(None, r.json(), r.headers.get("ETag"))

    def get_readme(self, ref=None):
        """
        Calls the `GET /repos/:owner/:repo/readme <http://developer.github.com/v3/repos/contents#get-the-readme>`__ end point.

        This is the only method calling this end point.

        :param ref: optional :class:`string`
        :rtype: :class:`.File`
        """
        import PyGithub.Blocking.File

        if ref is not None:
            ref = _snd.normalizeString(ref)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/readme", owner=self.owner.login, repo=self.name)
        urlArguments = _snd.dictionary(ref=ref)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.File.File)(None, r.json(), r.headers.get("ETag"))

    def get_stargazers(self, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/stargazers <http://developer.github.com/v3/activity/starring#list-stargazers>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """
        import PyGithub.Blocking.User

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.stargazers_url)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User))(None, r)

    def get_subscribers(self, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/subscribers <http://developer.github.com/v3/activity/watching#list-watchers>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """
        import PyGithub.Blocking.User

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.subscribers_url)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User))(None, r)

    def get_tags(self, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/tags <http://developer.github.com/v3/repos#list-tags>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Tag`
        """

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.tags_url)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.StructureConverter(self.Session, Repository.Tag))(None, r)

    def get_teams(self, per_page=None):
        """
        Calls the `GET /repos/:owner/:repo/teams <http://developer.github.com/v3/repos#list-teams>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Team`
        """
        import PyGithub.Blocking.Team

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.teams_url)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Team.Team))(None, r)

    def has_in_assignees(self, assignee):
        """
        Calls the `GET /repos/:owner/:repo/assignees/:assignee <http://developer.github.com/v3/issues/assignees#check-assignee>`__ end point.

        This is the only method calling this end point.

        :param assignee: mandatory :class:`.User` or :class:`string` (its :attr:`.Entity.login`)
        :rtype: :class:`bool`
        """

        assignee = _snd.normalizeUserLogin(assignee)

        url = uritemplate.expand(self.assignees_url, user=assignee)
        r = self.Session._request("GET", url, accept404=True)
        return _rcv.BoolConverter(None, r.status_code == 204)

    def has_in_collaborators(self, username):
        """
        Calls the `GET /repos/:owner/:repo/collaborators/:username <http://developer.github.com/v3/repos/collaborators#get>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.Entity.login`)
        :rtype: :class:`bool`
        """

        username = _snd.normalizeUserLogin(username)

        url = uritemplate.expand(self.collaborators_url, collaborator=username)
        r = self.Session._request("GET", url, accept404=True)
        return _rcv.BoolConverter(None, r.status_code == 204)

    def remove_from_collaborators(self, username):
        """
        Calls the `DELETE /repos/:owner/:repo/collaborators/:username <http://developer.github.com/v3/repos/collaborators#remove-collaborator>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.Entity.login`)
        :rtype: None
        """

        username = _snd.normalizeUserLogin(username)

        url = uritemplate.expand(self.collaborators_url, collaborator=username)
        r = self.Session._request("DELETE", url)
