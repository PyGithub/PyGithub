############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
# Copyright 2014 Andy Casey <acasey@mso.anu.edu.au>                            #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 John Eskew <jeskew@edx.org>                                   #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Danilo Martins <mawkee@gmail.com>                             #
# Copyright 2020 Dhruv Manilawala <dhruvmanila@gmail.com>                      #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 iarspider <iarspider@gmail.com>                               #
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

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import github.CheckRun
import github.CheckSuite
import github.CommitCombinedStatus
import github.CommitComment
import github.CommitStats
import github.CommitStatus
import github.File
import github.GitCommit
import github.NamedUser
import github.PaginatedList
from github.GithubObject import Attribute, CompletableGithubObject, NotSet, Opt, is_optional
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.CheckRun import CheckRun
    from github.CheckSuite import CheckSuite
    from github.CommitCombinedStatus import CommitCombinedStatus
    from github.CommitComment import CommitComment
    from github.CommitStats import CommitStats
    from github.CommitStatus import CommitStatus
    from github.File import File
    from github.GitCommit import GitCommit
    from github.NamedUser import NamedUser
    from github.PullRequest import PullRequest


class Commit(CompletableGithubObject):
    """
    This class represents Commits.

    The reference can be found here
    https://docs.github.com/en/rest/reference/git#commits

    """

    def _initAttributes(self) -> None:
        self._author: Attribute[NamedUser] = NotSet
        self._comments_url: Attribute[str] = NotSet
        self._commit: Attribute[GitCommit] = NotSet
        self._committer: Attribute[NamedUser] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._parents: Attribute[list[Commit]] = NotSet
        self._sha: Attribute[str] = NotSet
        self._stats: Attribute[CommitStats] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"sha": self._sha.value})

    @property
    def author(self) -> NamedUser:
        self._completeIfNotSet(self._author)
        return self._author.value

    @property
    def comments_url(self) -> str:
        self._completeIfNotSet(self._comments_url)
        return self._comments_url.value

    @property
    def commit(self) -> GitCommit:
        self._completeIfNotSet(self._commit)
        return self._commit.value

    @property
    def committer(self) -> NamedUser:
        self._completeIfNotSet(self._committer)
        return self._committer.value

    # This should be a method, but this used to be a property and cannot be changed without breaking user code
    # TODO: remove @property on version 3
    @property
    def files(self) -> PaginatedList[File]:
        return PaginatedList(
            github.File.File,
            self._requester,
            self.url,
            {},
            None,
            "files",
            "total_files",
            self.raw_data,
            self.raw_headers,
        )

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def parents(self) -> list[Commit]:
        self._completeIfNotSet(self._parents)
        return self._parents.value

    @property
    def sha(self) -> str:
        self._completeIfNotSet(self._sha)
        return self._sha.value

    @property
    def stats(self) -> CommitStats:
        self._completeIfNotSet(self._stats)
        return self._stats.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def create_comment(
        self,
        body: str,
        line: Opt[int] = NotSet,
        path: Opt[str] = NotSet,
        position: Opt[int] = NotSet,
    ) -> CommitComment:
        """
        :calls: `POST /repos/{owner}/{repo}/commits/{sha}/comments <https://docs.github.com/en/rest/reference/repos#comments>`_
        """
        assert isinstance(body, str), body
        assert is_optional(line, int), line
        assert is_optional(path, str), path
        assert is_optional(position, int), position
        post_parameters = NotSet.remove_unset_items({"body": body, "line": line, "path": path, "position": position})

        headers, data = self._requester.requestJsonAndCheck("POST", f"{self.url}/comments", input=post_parameters)
        return github.CommitComment.CommitComment(self._requester, headers, data, completed=True)

    def create_status(
        self,
        state: str,
        target_url: Opt[str] = NotSet,
        description: Opt[str] = NotSet,
        context: Opt[str] = NotSet,
    ) -> CommitStatus:
        """
        :calls: `POST /repos/{owner}/{repo}/statuses/{sha} <https://docs.github.com/en/rest/reference/repos#statuses>`_
        """
        assert isinstance(state, str), state
        assert is_optional(target_url, str), target_url
        assert is_optional(description, str), description
        assert is_optional(context, str), context
        post_parameters = NotSet.remove_unset_items(
            {
                "state": state,
                "target_url": target_url,
                "description": description,
                "context": context,
            }
        )

        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            f"{self._parentUrl(self._parentUrl(self.url))}/statuses/{self.sha}",
            input=post_parameters,
        )
        return github.CommitStatus.CommitStatus(self._requester, headers, data, completed=True)

    def get_comments(self) -> PaginatedList[CommitComment]:
        """
        :calls: `GET /repos/{owner}/{repo}/commits/{sha}/comments <https://docs.github.com/en/rest/reference/repos#comments>`_
        """
        return PaginatedList(
            github.CommitComment.CommitComment,
            self._requester,
            f"{self.url}/comments",
            None,
        )

    def get_statuses(self) -> PaginatedList[CommitStatus]:
        """
        :calls: `GET /repos/{owner}/{repo}/statuses/{ref} <https://docs.github.com/en/rest/reference/repos#statuses>`_
        """
        return PaginatedList(
            github.CommitStatus.CommitStatus,
            self._requester,
            f"{self._parentUrl(self._parentUrl(self.url))}/statuses/{self.sha}",
            None,
        )

    def get_combined_status(self) -> CommitCombinedStatus:
        """
        :calls: `GET /repos/{owner}/{repo}/commits/{ref}/status/ <http://docs.github.com/en/rest/reference/repos#statuses>`_
        """
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self.url}/status")
        return github.CommitCombinedStatus.CommitCombinedStatus(self._requester, headers, data, completed=True)

    def get_pulls(self) -> PaginatedList[PullRequest]:
        """
        :calls: `GET /repos/{owner}/{repo}/commits/{sha}/pulls <https://docs.github.com/en/rest/reference/repos#list-pull-requests-associated-with-a-commit>`_
        """
        return PaginatedList(
            github.PullRequest.PullRequest,
            self._requester,
            f"{self.url}/pulls",
            None,
            headers={"Accept": "application/vnd.github.groot-preview+json"},
        )

    def get_check_runs(
        self,
        check_name: Opt[str] = NotSet,
        status: Opt[str] = NotSet,
        filter: Opt[str] = NotSet,
    ) -> PaginatedList[CheckRun]:
        """
        :calls: `GET /repos/{owner}/{repo}/commits/{sha}/check-runs <https://docs.github.com/en/rest/reference/checks#list-check-runs-for-a-git-reference>`_
        """
        assert is_optional(check_name, str), check_name
        assert is_optional(status, str), status
        assert is_optional(filter, str), filter
        url_parameters = NotSet.remove_unset_items({"check_name": check_name, "status": status, "filter": filter})

        return PaginatedList(
            github.CheckRun.CheckRun,
            self._requester,
            f"{self.url}/check-runs",
            url_parameters,
            headers={"Accept": "application/vnd.github.v3+json"},
            list_item="check_runs",
        )

    def get_check_suites(self, app_id: Opt[int] = NotSet, check_name: Opt[str] = NotSet) -> PaginatedList[CheckSuite]:
        """
        :class: `GET /repos/{owner}/{repo}/commits/{ref}/check-suites <https://docs.github.com/en/rest/reference/checks#list-check-suites-for-a-git-reference>`_
        """
        assert is_optional(app_id, int), app_id
        assert is_optional(check_name, str), check_name
        parameters = NotSet.remove_unset_items({"app_id": app_id, "check_name": check_name})

        request_headers = {"Accept": "application/vnd.github.v3+json"}
        return PaginatedList(
            github.CheckSuite.CheckSuite,
            self._requester,
            f"{self.url}/check-suites",
            parameters,
            headers=request_headers,
            list_item="check_suites",
        )

    @property
    def _identity(self) -> str:
        return self.sha

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "author" in attributes:  # pragma no branch
            self._author = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["author"])
        if "comments_url" in attributes:  # pragma no branch
            self._comments_url = self._makeStringAttribute(attributes["comments_url"])
        if "commit" in attributes:  # pragma no branch
            self._commit = self._makeClassAttribute(github.GitCommit.GitCommit, attributes["commit"])
        if "committer" in attributes:  # pragma no branch
            self._committer = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["committer"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "parents" in attributes:  # pragma no branch
            self._parents = self._makeListOfClassesAttribute(Commit, attributes["parents"])
        if "sha" in attributes:  # pragma no branch
            self._sha = self._makeStringAttribute(attributes["sha"])
        if "stats" in attributes:  # pragma no branch
            self._stats = self._makeClassAttribute(github.CommitStats.CommitStats, attributes["stats"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
