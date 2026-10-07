# SPDX-License-Identifier: LGPL-3.0-or-later

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from doc.graphql_reference import collect_graphql_calls, generate_graphql_reference


class GraphqlReference(unittest.TestCase):
    def testCallsAreScopedToTheirClassAndMethod(self):
        source = '''
class First:
    """https://docs.github.com/en/graphql/reference/objects#discussion"""

    def get(self):
        """
        :calls: `GraphQL query Query.node
            <https://docs.github.com/en/graphql/reference/queries#node>`_
        """

    def rest(self):
        """:calls: `GET /issues <https://docs.github.com/en/rest/issues>`_"""

class Second:
    def get(self):
        """
        :calls: `GraphQL query Query.node <https://docs.github.com/en/graphql/reference/queries#node>`__
        :calls: `GraphQL query Query.node <https://docs.github.com/en/graphql/reference/queries#node>`__
        """

    def _helper(self):
        """:calls: `GraphQL query Query.node <https://docs.github.com/en/graphql/reference/queries#node>`_"""
'''
        self.assertEqual(
            collect_graphql_calls(source, "github.Example"),
            {
                ("query", "Query.node", "https://docs.github.com/en/graphql/reference/queries#node"): {
                    "github.Example.First.get",
                    "github.Example.Second.get",
                }
            },
        )

    def testUnannotatedLinksAreNotOperations(self):
        source = '''
class Example:
    def method(self):
        """
        Related documentation:
        https://docs.github.com/en/graphql/reference/mutations#minimizecomment

        Example annotation::

            :calls: `GraphQL mutation minimizeComment <https://docs.github.com/en/graphql/reference/mutations#minimizecomment>`_
        """
'''
        self.assertEqual(collect_graphql_calls(source, "github.Example"), {})

    def testReferenceIsSortedAndDoesNotImportSources(self):
        with tempfile.TemporaryDirectory() as directory:
            source_dir = Path(directory)
            source_dir.joinpath("Example.py").write_text(
                '''
raise RuntimeError("Documentation must not execute this module")

class Example:
    def z_method(self):
        """:calls: `GraphQL mutation addDiscussionComment <https://docs.github.com/en/graphql/reference/mutations#adddiscussioncomment>`_"""

    def a_method(self):
        """:calls: `GraphQL mutation addDiscussionComment <https://docs.github.com/en/graphql/reference/mutations#adddiscussioncomment>`_"""

    def query(self):
        """:calls: `GraphQL query Repository.discussion <https://docs.github.com/en/graphql/reference/objects#repository>`_"""
''',
                encoding="utf-8",
            )
            reference = generate_graphql_reference(source_dir)
        self.assertLess(reference.index("Queries\n"), reference.index("Mutations\n"))
        self.assertLess(reference.index("Repository.discussion"), reference.index("addDiscussionComment"))
        self.assertEqual(reference.count("* `addDiscussionComment"), 1)
        self.assertIn(":meth:`github.Example.Example.a_method` or :meth:`github.Example.Example.z_method`", reference)

    def testSupportedLibraryOperationsAreIndexed(self):
        reference = generate_graphql_reference(Path(__file__).resolve().parents[1] / "github")
        methods = {
            "MainClass.Github.get_repository_discussion",
            "Repository.Repository.get_discussion",
            "Repository.Repository.get_discussions",
            "RepositoryDiscussion.RepositoryDiscussion.get_comments",
            "RepositoryDiscussion.RepositoryDiscussion.add_comment",
            "RepositoryDiscussionComment.RepositoryDiscussionComment.edit",
            "RepositoryDiscussionComment.RepositoryDiscussionComment.delete",
            "PullRequest.PullRequest.enable_automerge",
            "PullRequest.PullRequest.disable_automerge",
            "PullRequest.PullRequest.convert_to_draft",
            "PullRequest.PullRequest.mark_ready_for_review",
            "IssueComment.IssueComment.minimize",
            "IssueComment.IssueComment.unminimize",
        }
        for method in methods:
            with self.subTest(method=method):
                self.assertIn(f":meth:`github.{method}`", reference)
        self.assertNotIn(".get_labels`", reference)
        self.assertNotIn(".get_reactions`", reference)
        self.assertNotIn(".get_replies`", reference)
