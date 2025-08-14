############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
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

from typing import Any

import github
import github.GithubException
import github.Organization
import github.Repository
import github.RepositoryDiscussion
import github.RepositoryDiscussionComment
import github.Requester
from github import Github

from . import Framework


class GraphQl(Framework.TestCase):
    def setUp(self):
        super().setUp()

    def expected(self, base_url: str = "https://github.com") -> dict[Any, Any]:
        return {
            "actor": {
                "avatarUrl": "https://avatars.githubusercontent.com/u/14806300?u=786f9f8ef8782d45381b01580f7f7783cf9c7e37&v=4",
                "login": "heitorpolidoro",
                "resourcePath": "/heitorpolidoro",
                "url": f"{base_url}/heitorpolidoro",
            },
            "clientMutationId": None,
        }

    def testRequesterGraphQlPrefix(self):
        get_graphql_prefix = github.Requester.Requester.get_graphql_prefix
        assert "/graphql" == get_graphql_prefix(None)
        assert "/graphql" == get_graphql_prefix("")
        assert "/graphql" == get_graphql_prefix("/")
        assert "/api/graphql" == get_graphql_prefix("/api/v3")
        assert "/path/to/github/api/graphql" == get_graphql_prefix("/path/to/github/api/v3")
        assert "/path/to/github/graphql" == get_graphql_prefix("/path/to/github")

    def testDefaultUrl(self):
        pull = self.g.get_repo("PyGithub/PyGithub").get_pull(31)
        response = pull.disable_automerge()
        assert response == self.expected()

    def testOtherUrl(self):
        base_url = "https://my.enterprise.com/api/v3"
        gh = Github(base_url=base_url)
        pull = gh.get_repo("PyGithub/PyGithub").get_pull(31)
        response = pull.disable_automerge()
        assert response == self.expected(base_url)

    def testOtherPort(self):
        base_url = "https://my.enterprise.com:8080/api/v3"
        gh = Github(base_url=base_url)
        pull = gh.get_repo("PyGithub/PyGithub").get_pull(31)
        response = pull.disable_automerge()
        assert response == self.expected(base_url)

    def testNode(self):
        requester = self.g._Github__requester
        headers, data = requester.graphql_node("D_kwDOADYVqs4ATJZD", "title", "Discussion")
        self.assertTrue(headers)
        self.assertEqual(
            data.get("data", {}).get("node", {}).get("title"),
            "Is there a way to search if a string present in default branch?",
        )

        # non-existing node should throw a NOT FOUND exception
        with self.assertRaises(github.UnknownObjectException) as e:
            requester.graphql_node("D_abcdefgh", "title", "Discussion")
        self.assertEqual(e.exception.status, 404)
        self.assertEqual(
            e.exception.data,
            {
                "data": {"node": None},
                "errors": [
                    {
                        "type": "NOT_FOUND",
                        "path": ["node"],
                        "locations": [{"line": 3, "column": 15}],
                        "message": "Could not resolve to a node with the global id of 'D_abcdefgh'",
                    }
                ],
            },
        )
        self.assertEqual(e.exception.message, "Could not resolve to a node with the global id of 'D_abcdefgh'")

        # wrong type should throw an exception
        with self.assertRaises(github.GithubException) as e:
            requester.graphql_node("D_kwDOADYVqs4ATJZD", "login", "User")
        self.assertEqual(e.exception.message, "Retrieved User object is of different type: Discussion")
        self.assertEqual(e.exception.status, 400)
        self.assertEqual(e.exception.data, {"data": {"node": {"__typename": "Discussion"}}})

    def testNodeClass(self):
        requester = self.g._Github__requester
        discussion = requester.graphql_node_class(
            "D_kwDOADYVqs4ATJZD", "title", github.RepositoryDiscussion.RepositoryDiscussion, "Discussion"
        )
        self.assertEqual(discussion.title, "Is there a way to search if a string present in default branch?")

        # non-existing node should throw a NOT FOUND exception
        with self.assertRaises(github.UnknownObjectException) as e:
            requester.graphql_node_class(
                "D_abcdefgh", "title", github.RepositoryDiscussion.RepositoryDiscussion, "Discussion"
            )
        self.assertEqual(e.exception.status, 404)
        self.assertEqual(
            e.exception.data,
            {
                "data": {"node": None},
                "errors": [
                    {
                        "type": "NOT_FOUND",
                        "path": ["node"],
                        "locations": [{"line": 3, "column": 15}],
                        "message": "Could not resolve to a node with the global id of 'D_abcdefgh'",
                    }
                ],
            },
        )
        self.assertEqual(e.exception.message, "Could not resolve to a node with the global id of 'D_abcdefgh'")

        # wrong type should throw an exception
        with self.assertRaises(github.GithubException) as e:
            requester.graphql_node_class(
                "D_kwDOADYVqs4ATJZD", "login", github.RepositoryDiscussion.RepositoryDiscussion, "User"
            )
        self.assertEqual(e.exception.message, "Retrieved User object is of different type: Discussion")
        self.assertEqual(e.exception.status, 400)
        self.assertEqual(e.exception.data, {"data": {"node": {"__typename": "Discussion"}}})

    def testQuery(self):
        requester = self.g._Github__requester
        query = """
            query Q($owner: String!, $name: String!) {
              repository(owner: $owner, name: $name) { url }
            }"""
        variables = {"owner": "PyGithub", "name": "PyGithub"}
        header, data = requester.graphql_query(query, variables)
        self.assertTrue(header)
        self.assertEqual(data, {"data": {"repository": {"url": "https://github.com/PyGithub/PyGithub"}}})

    def testQueryRestClass(self):
        requester = self.g._Github__requester
        query = """
            query Q($owner: String!, $name: String!) {
              repository(owner: $owner, name: $name) { url }
            }"""
        variables = {"owner": "PyGithub", "name": "PyGithub"}
        repo = requester.graphql_query_class(query, variables, ["repository"], github.Repository.Repository)
        self.assertIsInstance(repo, github.Repository.Repository)
        self.assertEqual(repo.html_url, "https://github.com/PyGithub/PyGithub")

    def testQueryGraphQlClass(self):
        requester = self.g._Github__requester
        query = """
            query Q($id: ID!) {
              node(id: $id) { ... on DiscussionComment { url } }
            }"""
        variables = {"id": "DC_kwDOADYVqs4AU3Mg"}
        comment = requester.graphql_query_class(
            query, variables, ["node"], github.RepositoryDiscussionComment.RepositoryDiscussionComment
        )
        self.assertIsInstance(comment, github.RepositoryDiscussionComment.RepositoryDiscussionComment)
        self.assertEqual(
            comment.html_url, "https://github.com/PyGithub/PyGithub/discussions/2480#discussioncomment-5468960"
        )

    def testMutation(self):
        requester = self.g._Github__requester
        header, data = requester.graphql_named_mutation(
            "followOrganization", {"organizationId": "O_kgDOAKxBpA"}, "organization { name }"
        )
        self.assertTrue(header)
        self.assertEqual(data, {"organization": {"name": "PyGithub"}})

    def testMutationClass(self):
        requester = self.g._Github__requester
        org = requester.graphql_named_mutation_class(
            "followOrganization",
            {"organizationId": "O_kgDOAKxBpA"},
            "organization { name }",
            "organization",
            github.Organization.Organization,
        )
        self.assertEqual(org.name, "PyGithub")

    def testPaginationAndRestIntegration(self):
        repo = self.g.get_repo("PyGithub/PyGithub")
        discussion_schema = """
            id
            url
            number
            author {
              login
              avatarUrl
              url
            }
            repository {
              owner { login }
              name
              issues(first: 10) {
                totalCount
                pageInfo {
                  startCursor
                  endCursor
                  hasNextPage
                  hasPreviousPage
                }
                nodes {
                  databaseId
                  id
                  number
                  title
                }
              }
            }
            title
            createdAt
            comments(first: 10) {
              totalCount
              pageInfo {
                startCursor
                endCursor
                hasNextPage
                hasPreviousPage
              }
              nodes {
                id
                url
                createdAt
                author {
                  login
                  avatarUrl
                  url
                }
                isAnswer
                replies(first: 10) {
                  totalCount
                  pageInfo {
                    startCursor
                    endCursor
                    hasNextPage
                    hasPreviousPage
                  }
                  nodes {
                    id
                    url
                    createdAt
                    author {
                      login
                      avatarUrl
                      url
                    }
                  }
                }
              }
            }
            labels(first: 10) {
              totalCount
              pageInfo {
                startCursor
                endCursor
                hasNextPage
                hasPreviousPage
              }
              nodes {
                id
                name
                issues(first: 10) {
                  totalCount
                  pageInfo {
                    startCursor
                    endCursor
                    hasNextPage
                    hasPreviousPage
                  }
                  nodes {
                    databaseId
                    id
                    number
                    title
                  }
                }
              }
            }
          """
        discussions_pages = repo.get_discussions(discussion_schema)
        discussions = list(discussions_pages)
        # would perform an extra request if called before iterating discussions_pages
        self.assertEqual(discussions_pages.totalCount, 65)
        self.assertEqual(len(discussions), 65)
        self.assertEqual(discussions[0].number, 3044)
        self.assertEqual(discussions[-1].number, 1780)

        discussion = discussions[28]
        self.assertEqual(discussion.author.login, "arunanandhan")
        self.assertEqual(discussion.node_id, "D_kwDOADYVqs4ATJZD")
        self.assertEqual(
            discussion.author.avatar_url,
            "https://avatars.githubusercontent.com/u/48812131?u=571c345a5994a55100a16b45a9688f5d6d340730&v=4",
        )
        self.assertEqual(discussion.author.html_url, "https://github.com/arunanandhan")

        # inner page of GraphQL comments
        comments = discussion.get_comments("id")
        self.assertEqual(comments.totalCount, 1)  # does not perform an extra request
        comments = list(comments)
        self.assertEqual(len(comments), 1)
        comment = comments[0]
        self.assertEqual(comment.node_id, "DC_kwDOADYVqs4AU3Mg")
        self.assertEqual(
            comment.html_url, "https://github.com/PyGithub/PyGithub/discussions/2480#discussioncomment-5468960"
        )
        self.assertEqual(comment.author.login, "EnricoMi")

        # inner inner page of GraphQL replies
        replies = comment.get_replies()
        self.assertEqual(replies.totalCount, 5)  # does not perform an extra request
        self.assertEqual(replies[0].node_id, "DC_kwDOADYVqs4AU3Wg")

        # inner page of REST labels
        labels_pages = discussions[3].get_labels()
        self.assertEqual(labels_pages.totalCount, 1)
        label = labels_pages[0]
        self.assertEqual(label.name, "Call for Contribution")

        # inner REST repository
        repo = discussion.repository
        issues_pages = repo.get_issues()
        issue = issues_pages[0]
        # GraphQL retrieved 10 issues, but repo.get_issues() is not aware of that data
        # it calls the REST API
        self.assertEqual(issues_pages.totalCount, 341)
        self.assertEqual(issue.number, 3045)
