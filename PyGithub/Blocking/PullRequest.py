# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv

import PyGithub.Blocking.Issue


class PullRequest(PyGithub.Blocking.Issue.Issue):
    """
    Base class: :class:`.Issue`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Issue.create_pull`
      * :meth:`.Repository.create_pull`
      * :meth:`.Repository.get_pull`
      * :meth:`.Repository.get_pulls`

    Methods accepting instances of this class as parameter: none.
    """

    class End(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.PullRequest.base`
          * :attr:`.PullRequest.head`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, label=None, ref=None, repo=None, sha=None, user=None, **kwds):
            import PyGithub.Blocking.Repository
            import PyGithub.Blocking.User
            super(PullRequest.End, self)._initAttributes(**kwds)
            self.__label = _rcv.Attribute("PullRequest.End.label", _rcv.StringConverter, label)
            self.__ref = _rcv.Attribute("PullRequest.End.ref", _rcv.StringConverter, ref)
            self.__repo = _rcv.Attribute("PullRequest.End.repo", _rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository), repo)
            self.__sha = _rcv.Attribute("PullRequest.End.sha", _rcv.StringConverter, sha)
            self.__user = _rcv.Attribute("PullRequest.End.user", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), user)

        def _updateAttributes(self, label=None, ref=None, repo=None, sha=None, user=None, **kwds):
            super(PullRequest.End, self)._updateAttributes(**kwds)
            self.__label.update(label)
            self.__ref.update(ref)
            self.__repo.update(repo)
            self.__sha.update(sha)
            self.__user.update(user)

        @property
        def label(self):
            """
            :type: :class:`string`
            """
            return self.__label.value

        @property
        def ref(self):
            """
            :type: :class:`string`
            """
            return self.__ref.value

        @property
        def repo(self):
            """
            :type: :class:`.Repository`
            """
            return self.__repo.value

        @property
        def sha(self):
            """
            :type: :class:`string`
            """
            return self.__sha.value

        @property
        def user(self):
            """
            :type: :class:`.User`
            """
            return self.__user.value

    class File(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.PullRequest.get_files`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, additions=None, blob_url=None, changes=None, contents_url=None, deletions=None, filename=None, patch=None, raw_url=None, sha=None, status=None, **kwds):
            super(PullRequest.File, self)._initAttributes(**kwds)
            self.__additions = _rcv.Attribute("PullRequest.File.additions", _rcv.IntConverter, additions)
            self.__blob_url = _rcv.Attribute("PullRequest.File.blob_url", _rcv.StringConverter, blob_url)
            self.__changes = _rcv.Attribute("PullRequest.File.changes", _rcv.IntConverter, changes)
            self.__contents_url = _rcv.Attribute("PullRequest.File.contents_url", _rcv.StringConverter, contents_url)
            self.__deletions = _rcv.Attribute("PullRequest.File.deletions", _rcv.IntConverter, deletions)
            self.__filename = _rcv.Attribute("PullRequest.File.filename", _rcv.StringConverter, filename)
            self.__patch = _rcv.Attribute("PullRequest.File.patch", _rcv.StringConverter, patch)
            self.__raw_url = _rcv.Attribute("PullRequest.File.raw_url", _rcv.StringConverter, raw_url)
            self.__sha = _rcv.Attribute("PullRequest.File.sha", _rcv.StringConverter, sha)
            self.__status = _rcv.Attribute("PullRequest.File.status", _rcv.StringConverter, status)

        @property
        def additions(self):
            """
            :type: :class:`int`
            """
            return self.__additions.value

        @property
        def blob_url(self):
            """
            :type: :class:`string`
            """
            return self.__blob_url.value

        @property
        def changes(self):
            """
            :type: :class:`int`
            """
            return self.__changes.value

        @property
        def contents_url(self):
            """
            :type: :class:`string`
            """
            return self.__contents_url.value

        @property
        def deletions(self):
            """
            :type: :class:`int`
            """
            return self.__deletions.value

        @property
        def filename(self):
            """
            :type: :class:`string`
            """
            return self.__filename.value

        @property
        def patch(self):
            """
            :type: :class:`string`
            """
            return self.__patch.value

        @property
        def raw_url(self):
            """
            :type: :class:`string`
            """
            return self.__raw_url.value

        @property
        def sha(self):
            """
            :type: :class:`string`
            """
            return self.__sha.value

        @property
        def status(self):
            """
            :type: :class:`string`
            """
            return self.__status.value

    class MergeResult(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.PullRequest.merge`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, documentation_url=None, merged=None, message=None, sha=None, **kwds):
            super(PullRequest.MergeResult, self)._initAttributes(**kwds)
            self.__documentation_url = _rcv.Attribute("PullRequest.MergeResult.documentation_url", _rcv.StringConverter, documentation_url)
            self.__merged = _rcv.Attribute("PullRequest.MergeResult.merged", _rcv.BoolConverter, merged)
            self.__message = _rcv.Attribute("PullRequest.MergeResult.message", _rcv.StringConverter, message)
            self.__sha = _rcv.Attribute("PullRequest.MergeResult.sha", _rcv.StringConverter, sha)

        @property
        def documentation_url(self):
            """
            :type: :class:`string`
            """
            return self.__documentation_url.value

        @property
        def merged(self):
            """
            :type: :class:`bool`
            """
            return self.__merged.value

        @property
        def message(self):
            """
            :type: :class:`string`
            """
            return self.__message.value

        @property
        def sha(self):
            """
            :type: :class:`string`
            """
            return self.__sha.value

    def _initAttributes(self, additions=_rcv.Absent, base=_rcv.Absent, changed_files=_rcv.Absent, commits=_rcv.Absent, commits_url=_rcv.Absent, deletions=_rcv.Absent, diff_url=_rcv.Absent, head=_rcv.Absent, issue_url=_rcv.Absent, merge_commit_sha=_rcv.Absent, mergeable=_rcv.Absent, mergeable_state=_rcv.Absent, merged=_rcv.Absent, merged_at=_rcv.Absent, merged_by=_rcv.Absent, patch_url=_rcv.Absent, review_comment_url=_rcv.Absent, review_comments=_rcv.Absent, review_comments_url=_rcv.Absent, statuses_url=_rcv.Absent, _links=None, **kwds):
        import PyGithub.Blocking.User
        super(PullRequest, self)._initAttributes(**kwds)
        self.__additions = _rcv.Attribute("PullRequest.additions", _rcv.IntConverter, additions)
        self.__base = _rcv.Attribute("PullRequest.base", _rcv.StructureConverter(self.Session, PullRequest.End), base)
        self.__changed_files = _rcv.Attribute("PullRequest.changed_files", _rcv.IntConverter, changed_files)
        self.__commits = _rcv.Attribute("PullRequest.commits", _rcv.IntConverter, commits)
        self.__commits_url = _rcv.Attribute("PullRequest.commits_url", _rcv.StringConverter, commits_url)
        self.__deletions = _rcv.Attribute("PullRequest.deletions", _rcv.IntConverter, deletions)
        self.__diff_url = _rcv.Attribute("PullRequest.diff_url", _rcv.StringConverter, diff_url)
        self.__head = _rcv.Attribute("PullRequest.head", _rcv.StructureConverter(self.Session, PullRequest.End), head)
        self.__issue_url = _rcv.Attribute("PullRequest.issue_url", _rcv.StringConverter, issue_url)
        self.__merge_commit_sha = _rcv.Attribute("PullRequest.merge_commit_sha", _rcv.StringConverter, merge_commit_sha)
        self.__mergeable = _rcv.Attribute("PullRequest.mergeable", _rcv.BoolConverter, mergeable)
        self.__mergeable_state = _rcv.Attribute("PullRequest.mergeable_state", _rcv.StringConverter, mergeable_state)
        self.__merged = _rcv.Attribute("PullRequest.merged", _rcv.BoolConverter, merged)
        self.__merged_at = _rcv.Attribute("PullRequest.merged_at", _rcv.DatetimeConverter, merged_at)
        self.__merged_by = _rcv.Attribute("PullRequest.merged_by", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), merged_by)
        self.__patch_url = _rcv.Attribute("PullRequest.patch_url", _rcv.StringConverter, patch_url)
        self.__review_comment_url = _rcv.Attribute("PullRequest.review_comment_url", _rcv.StringConverter, review_comment_url)
        self.__review_comments = _rcv.Attribute("PullRequest.review_comments", _rcv.IntConverter, review_comments)
        self.__review_comments_url = _rcv.Attribute("PullRequest.review_comments_url", _rcv.StringConverter, review_comments_url)
        self.__statuses_url = _rcv.Attribute("PullRequest.statuses_url", _rcv.StringConverter, statuses_url)

    def _updateAttributes(self, eTag, additions=_rcv.Absent, base=_rcv.Absent, changed_files=_rcv.Absent, commits=_rcv.Absent, commits_url=_rcv.Absent, deletions=_rcv.Absent, diff_url=_rcv.Absent, head=_rcv.Absent, issue_url=_rcv.Absent, merge_commit_sha=_rcv.Absent, mergeable=_rcv.Absent, mergeable_state=_rcv.Absent, merged=_rcv.Absent, merged_at=_rcv.Absent, merged_by=_rcv.Absent, patch_url=_rcv.Absent, review_comment_url=_rcv.Absent, review_comments=_rcv.Absent, review_comments_url=_rcv.Absent, statuses_url=_rcv.Absent, _links=None, **kwds):
        super(PullRequest, self)._updateAttributes(eTag, **kwds)
        self.__additions.update(additions)
        self.__base.update(base)
        self.__changed_files.update(changed_files)
        self.__commits.update(commits)
        self.__commits_url.update(commits_url)
        self.__deletions.update(deletions)
        self.__diff_url.update(diff_url)
        self.__head.update(head)
        self.__issue_url.update(issue_url)
        self.__merge_commit_sha.update(merge_commit_sha)
        self.__mergeable.update(mergeable)
        self.__mergeable_state.update(mergeable_state)
        self.__merged.update(merged)
        self.__merged_at.update(merged_at)
        self.__merged_by.update(merged_by)
        self.__patch_url.update(patch_url)
        self.__review_comment_url.update(review_comment_url)
        self.__review_comments.update(review_comments)
        self.__review_comments_url.update(review_comments_url)
        self.__statuses_url.update(statuses_url)

    @property
    def additions(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__additions.needsLazyCompletion)
        return self.__additions.value

    @property
    def base(self):
        """
        :type: :class:`.PullRequest.End`
        """
        self._completeLazily(self.__base.needsLazyCompletion)
        return self.__base.value

    @property
    def changed_files(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__changed_files.needsLazyCompletion)
        return self.__changed_files.value

    @property
    def commits(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__commits.needsLazyCompletion)
        return self.__commits.value

    @property
    def commits_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__commits_url.needsLazyCompletion)
        return self.__commits_url.value

    @property
    def deletions(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__deletions.needsLazyCompletion)
        return self.__deletions.value

    @property
    def diff_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__diff_url.needsLazyCompletion)
        return self.__diff_url.value

    @property
    def head(self):
        """
        :type: :class:`.PullRequest.End`
        """
        self._completeLazily(self.__head.needsLazyCompletion)
        return self.__head.value

    @property
    def issue_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__issue_url.needsLazyCompletion)
        return self.__issue_url.value

    @property
    def merge_commit_sha(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__merge_commit_sha.needsLazyCompletion)
        return self.__merge_commit_sha.value

    @property
    def mergeable(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__mergeable.needsLazyCompletion)
        return self.__mergeable.value

    @property
    def mergeable_state(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__mergeable_state.needsLazyCompletion)
        return self.__mergeable_state.value

    @property
    def merged(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__merged.needsLazyCompletion)
        return self.__merged.value

    @property
    def merged_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__merged_at.needsLazyCompletion)
        return self.__merged_at.value

    @property
    def merged_by(self):
        """
        :type: :class:`.User`
        """
        self._completeLazily(self.__merged_by.needsLazyCompletion)
        return self.__merged_by.value

    @property
    def patch_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__patch_url.needsLazyCompletion)
        return self.__patch_url.value

    @property
    def review_comment_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__review_comment_url.needsLazyCompletion)
        return self.__review_comment_url.value

    @property
    def review_comments(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__review_comments.needsLazyCompletion)
        return self.__review_comments.value

    @property
    def review_comments_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__review_comments_url.needsLazyCompletion)
        return self.__review_comments_url.value

    @property
    def statuses_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__statuses_url.needsLazyCompletion)
        return self.__statuses_url.value

    def edit(self, title=None, body=None, state=None):
        """
        Calls the `PATCH /repos/:owner/:repo/pulls/:number <http://developer.github.com/v3/pulls#update-a-pull-request>`__ end point.

        This is the only method calling this end point.

        :param title: optional :class:`string`
        :param body: optional :class:`string` or :class:`Reset`
        :param state: optional "closed" or "open"
        :rtype: None
        """

        if title is not None:
            title = _snd.normalizeString(title)
        if body is not None:
            body = _snd.normalizeStringReset(body)
        if state is not None:
            state = _snd.normalizeEnum(state, "closed", "open")

        url = uritemplate.expand(self.url)
        postArguments = _snd.dictionary(body=body, state=state, title=title)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())

    def get_commits(self):
        """
        Calls the `GET /repos/:owner/:repo/pulls/:number/commits <http://developer.github.com/v3/pulls#list-commits-on-a-pull-request>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`list` of :class:`.Commit`
        """
        import PyGithub.Blocking.Commit

        url = uritemplate.expand(self.commits_url)
        r = self.Session._request("GET", url)
        return _rcv.ListConverter(_rcv.ClassConverter(self.Session, PyGithub.Blocking.Commit.Commit))(None, r.json())

    def get_files(self):
        """
        Calls the `GET /repos/:owner/:repo/pulls/:number/files <http://developer.github.com/v3/pulls#list-pull-requests-files>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`list` of :class:`.PullRequest.File`
        """

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/pulls/{number}/files", number=str(self.number), owner=self.base.repo.owner.login, repo=self.base.repo.name)
        r = self.Session._request("GET", url)
        return _rcv.ListConverter(_rcv.StructureConverter(self.Session, PullRequest.File))(None, r.json())

    def get_is_merged(self):
        """
        Calls the `GET /repos/:owner/:repo/pulls/:number/merge <http://developer.github.com/v3/pulls#get-if-a-pull-request-has-been-merged>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`bool`
        """

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/pulls/{number}/merge", number=str(self.number), owner=self.base.repo.owner.login, repo=self.base.repo.name)
        r = self.Session._request("GET", url, accept404=True)
        return _rcv.BoolConverter(None, r.status_code == 204)

    def merge(self, commit_message=None):
        """
        Calls the `PUT /repos/:owner/:repo/pulls/:number/merge <http://developer.github.com/v3/pulls#merge-a-pull-request-merge-button>`__ end point.

        This is the only method calling this end point.

        :param commit_message: optional :class:`string`
        :rtype: :class:`.PullRequest.MergeResult`
        """

        if commit_message is not None:
            commit_message = _snd.normalizeString(commit_message)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/pulls/{number}/merge", number=str(self.number), owner=self.base.repo.owner.login, repo=self.base.repo.name)
        postArguments = _snd.dictionary(commit_message=commit_message)
        r = self.Session._request("PUT", url, postArguments=postArguments)
        return _rcv.StructureConverter(self.Session, PullRequest.MergeResult)(None, r.json())
