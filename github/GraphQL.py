############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Michael Stead <michael.stead@gmail.com>                       #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 @tmshn <tmshn@r.recruit.co.jp>                                #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Aaron Levine <allevin@sandia.gov>                             #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Ben Yohay <ben@lightricks.com>                                #
# Copyright 2018 Gilad Shefer <gshefer@redhat.com>                             #
# Copyright 2018 Martin Monperrus <monperrus@users.noreply.github.com>         #
# Copyright 2018 Matt Babineau <9685860+babineaum@users.noreply.github.com>    #
# Copyright 2018 Shinichi TAMURA <shnch.tmr@gmail.com>                         #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Thibault Jamet <tjamet@users.noreply.github.com>              #
# Copyright 2018 per1234 <accounts@perglass.com>                               #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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

from github.GithubObject import (
    NotSet,
    Opt,
    is_optional,
    is_undefined,
)

if TYPE_CHECKING:
    from .Requester import Requester


class GraphQL:
    """
    This class make GraphQL requests easier. The reference can be found here https://docs.github.com/en/graphql
    """

    def __init__(
        self,
        requester: Requester,
        headers: dict[str, str | int],
    ):
        self._requester = requester
        self._headers = headers

    def query(self, query: str, variables: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
        """
        :calls: `POST /graphql <https://docs.github.com/en/graphql>`_
        """
        input_ = {"query": query, "variables": {"input": NotSet.remove_unset_items(variables)}}

        response_headers, data = self._requester.requestJsonAndCheck(
            "POST", "https://api.github.com/graphql", input=input_
        )
        if "errors" in data:
            raise self._requester.createException(400, response_headers, data)
        return response_headers, data

    def mutation(
        self, mutation_name: str, variables: dict[str, Any], output: str | None = ""
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        """
        Create a mutation in the format:
            mutation MutationName($input: MutationNameInput!) {
                mutationName(input: $input) {
                    <output>
                }
            }
        and call the self.query method
        """
        title = "".join([x.capitalize() for x in mutation_name.split("_")])
        mutation_name = title[:1].lower() + title[1:]
        query = f"mutation {title}($input: {title}Input!) {{ {mutation_name}(input: $input) {{ {output} }} }}"

        return self.query(query, variables)

    def enable_pull_request_auto_merge(
        self,
        pull_request_id: str,
        author_email: Opt[str] = NotSet,
        client_mutation_id: Opt[str] = NotSet,
        commit_body: Opt[str] = NotSet,
        commit_headline: Opt[str] = NotSet,
        expected_head_oid: Opt[str] = NotSet,
        merge_method: Opt[str] = "MERGE",
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        """
        :calls: `POST /graphql <https://docs.github.com/en/graphql>`_ with a mutation to enable pull request auto merge
        <https://docs.github.com/en/graphql/reference/mutations#enablepullrequestautomerge>
        """
        assert isinstance(pull_request_id, str), pull_request_id
        assert is_optional(author_email, str), author_email
        assert is_optional(client_mutation_id, str), client_mutation_id
        assert is_optional(commit_body, str), commit_body
        assert is_optional(commit_headline, str), commit_headline
        assert is_optional(expected_head_oid, str), expected_head_oid
        assert is_undefined(merge_method) or merge_method in ["MERGE", "REBASE", "SQUASH"], merge_method

        # Define the variables
        variables = {
            "pullRequestId": pull_request_id,
            "authorEmail": author_email,
            "clientMutationId": client_mutation_id,
            "commitBody": commit_body,
            "commitHeadline": commit_headline,
            "expectedHeadOid": expected_head_oid,
            "mergeMethod": merge_method,
        }

        # Make the request
        return self.mutation(
            mutation_name="enable_pull_request_auto_merge",
            variables=variables,
            output="actor { avatarUrl login resourcePath url } clientMutationId",
        )

    def disable_pull_request_auto_merge(
        self,
        pull_request_id: str,
        client_mutation_id: Opt[str] = NotSet,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        """
        :calls: `POST /graphql <https://docs.github.com/en/graphql>`_ with a mutation to disable pull request auto merge
        <https://docs.github.com/en/graphql/reference/mutations#disablepullrequestautomerge>
        """
        assert isinstance(pull_request_id, str), pull_request_id
        assert is_optional(client_mutation_id, str), client_mutation_id

        # Define the variables
        variables = {
            "pullRequestId": pull_request_id,
            "clientMutationId": client_mutation_id,
        }

        # Make the request
        return self.mutation(
            mutation_name="disable_pull_request_auto_merge",
            variables=variables,
            output="actor { avatarUrl login resourcePath url } clientMutationId",
        )
