############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
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

from datetime import datetime, timezone

from . import Framework


class RepositoryDiscussion(Framework.TestCase):
    discussion_schema = """
        answer {
          author { login }
          body
          bodyHTML
          bodyText
          createdAt
          databaseId
          discussion { id }
          editor { login }
          id
          lastEditedAt
          updatedAt
          url
        }
        author { login }
        body
        bodyHTML
        bodyText
        category {
          createdAt
          description
          emoji
          emojiHTML
          id
          isAnswerable
          name
          repository { owner { login } name }
          slug
          updatedAt
        }
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
          }
        }
        createdAt
        databaseId
        editor { login }
        id
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
          }
        }
        lastEditedAt
        number
        reactions(first: 10) {
          totalCount
          pageInfo {
            startCursor
            endCursor
            hasNextPage
            hasPreviousPage
          }
          nodes {
            id
          }
        }
        repository {
          owner { login }
          name
        }
        title
        updatedAt
        url
      """

    def setUp(self):
        super().setUp()
        self.discussion = self.g.get_repository_discussion("D_kwDOADYVqs4AaHoG", self.discussion_schema)

    def testAttributes(self):
        self.assertEqual(self.discussion.answer.author.login, "dawngerpony")
        self.assertEqual(
            self.discussion.answer.body,
            """[This comment](https://github.com/PyGithub/PyGithub/issues/2895#issue-2118964108) contains the answer to your question:\r\n\r\n```python\r\nmy_repo.raw_data["custom_properties"]\r\n```\r\n\r\n#2968 appears to add proper support for custom properties, but doesn't look like it's made it into a release yet.""",
        )
        self.assertEqual(
            self.discussion.answer.body_html,
            """<p dir="auto"><a href="https://github.com/PyGithub/PyGithub/issues/2895#issue-2118964108" data-hovercard-type="issue" data-hovercard-url="/PyGithub/PyGithub/issues/2895/hovercard">This comment</a> contains the answer to your question:</p>\n<div class="highlight highlight-source-python notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="my_repo.raw_data[&quot;custom_properties&quot;]"><pre class="notranslate"><span class="pl-s1">my_repo</span>.<span class="pl-s1">raw_data</span>[<span class="pl-s">"custom_properties"</span>]</pre></div>\n<p dir="auto"><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="2293897055" data-permission-text="Title is private" data-url="https://github.com/PyGithub/PyGithub/issues/2968" data-hovercard-type="pull_request" data-hovercard-url="/PyGithub/PyGithub/pull/2968/hovercard" href="https://github.com/PyGithub/PyGithub/pull/2968">#2968</a> appears to add proper support for custom properties, but doesn't look like it's made it into a release yet.</p>""",
        )
        self.assertEqual(
            self.discussion.answer.body_text,
            "This comment contains the answer to your question:\nmy_repo.raw_data[\"custom_properties\"]\n#2968 appears to add proper support for custom properties, but doesn't look like it's made it into a release yet.",
        )
        self.assertEqual(self.discussion.answer.created_at, datetime(2024, 8, 23, 6, 36, 50, tzinfo=timezone.utc))
        self.assertEqual(self.discussion.answer.database_id, 10426644)
        self.assertEqual(self.discussion.answer.discussion.node_id, "D_kwDOADYVqs4AaHoG")
        self.assertIsNone(self.discussion.answer.editor)
        self.assertEqual(self.discussion.answer.node_id, "DC_kwDOADYVqs4AnxkU")
        self.assertIsNone(self.discussion.answer.last_edited_at)
        self.assertEqual(self.discussion.answer.updated_at, datetime(2024, 8, 23, 6, 36, 51, tzinfo=timezone.utc))
        self.assertEqual(
            self.discussion.answer.html_url,
            "https://github.com/PyGithub/PyGithub/discussions/2993#discussioncomment-10426644",
        )
        self.assertEqual(self.discussion.author.login, "heitorPB")
        self.assertEqual(
            self.discussion.body,
            """What is the equivalent of `https://api.github.com/repos/OWNER/REPO/properties/values`? I'm interested in getting/setting custom properties for my repos. I can do that with `curl`, but couldn't find a way to do it via this project.\r\n\r\nDocs here: [Get all custom property values for a repository](https://docs.github.com/en/rest/repos/custom-properties?apiVersion=2022-11-28#get-all-custom-property-values-for-a-repository).""",
        )
        self.assertEqual(
            self.discussion.body_html,
            """<p dir="auto">What is the equivalent of <code class="notranslate">https://api.github.com/repos/OWNER/REPO/properties/values</code>? I'm interested in getting/setting custom properties for my repos. I can do that with <code class="notranslate">curl</code>, but couldn't find a way to do it via this project.</p>\n<p dir="auto">Docs here: <a href="https://docs.github.com/en/rest/repos/custom-properties?apiVersion=2022-11-28#get-all-custom-property-values-for-a-repository">Get all custom property values for a repository</a>.</p>""",
        )
        self.assertEqual(
            self.discussion.body_text,
            """What is the equivalent of https://api.github.com/repos/OWNER/REPO/properties/values? I'm interested in getting/setting custom properties for my repos. I can do that with curl, but couldn't find a way to do it via this project.\nDocs here: Get all custom property values for a repository.""",
        )
        self.assertEqual(self.discussion.category.created_at, datetime(2020, 12, 8, 23, 29, 13, tzinfo=timezone.utc))
        self.assertEqual(self.discussion.category.description, "Ask the community for help")
        self.assertEqual(self.discussion.category.emoji, ":pray:")
        self.assertEqual(self.discussion.category.emoji_html, "<div>🙏</div>")
        self.assertEqual(self.discussion.category.id, "MDE4OkRpc2N1c3Npb25DYXRlZ29yeTMyMDI5MDYx")
        self.assertEqual(self.discussion.category.is_answerable, True)
        self.assertEqual(self.discussion.category.name, "Q&A")
        self.assertEqual(self.discussion.category.repository.owner.login, "PyGithub")
        self.assertEqual(self.discussion.category.repository.name, "PyGithub")
        self.assertEqual(self.discussion.category.slug, "q-a")
        self.assertEqual(self.discussion.category.updated_at, datetime(2020, 12, 8, 23, 29, 13, tzinfo=timezone.utc))
        self.assertEqual(self.discussion.created_at, datetime(2024, 6, 21, 13, 11, 38, tzinfo=timezone.utc))
        self.assertEqual(self.discussion.database_id, 6846982)
        self.assertIsNone(self.discussion.editor)
        self.assertEqual(self.discussion.node_id, "D_kwDOADYVqs4AaHoG")
        self.assertIsNone(self.discussion.last_edited_at)
        self.assertEqual(self.discussion.number, 2993)
        self.assertEqual(self.discussion.repository.owner.login, "PyGithub")
        self.assertEqual(self.discussion.repository.name, "PyGithub")
        self.assertEqual(self.discussion.title, "How to get a list of custom repository properties?")
        self.assertEqual(self.discussion.updated_at, datetime(2024, 8, 29, 16, 1, 0, tzinfo=timezone.utc))

        self.assertListEqual(
            [c.node_id for c in self.discussion.get_comments("id")], ["DC_kwDOADYVqs4AnxkU", "DC_kwDOADYVqs4AoA2V"]
        )
        self.assertEqual(self.discussion.get_labels().totalCount, 0)
        self.assertEqual(self.discussion.get_reactions().totalCount, 0)

    def testGetComments(self):
        discussion = self.g.get_repository_discussion("D_kwDOADYVqs4AaHoG", "id")
        comments_pages = discussion.get_comments("id")
        comments = list(comments_pages)
        self.assertEqual(comments_pages.totalCount, 2)
        self.assertEqual(len(comments), 2)
        self.assertListEqual([c.id for c in comments], ["DC_kwDOADYVqs4AnxkU", "DC_kwDOADYVqs4AoA2V"])

    def testGetCommentsWithoutNodeId(self):
        discussion = self.g.get_repository_discussion("D_kwDOADYVqs4AaHoG", "title")
        with self.assertRaises(RuntimeError) as e:
            discussion.get_comments("id")
        self.assertEqual(e.exception.args, ("Retrieving discussion comments requires the discussion field 'id'",))

    def testAddAndDeleteComment(self):
        discussion = self.g.get_repository_discussion("D_kwDOADYVqs4AaHoG", "id")
        comment = discussion.add_comment("test comment", output_schema="id body")
        self.assertEqual(comment.id, "DC_kwDOADYVqs4AovYk")
        self.assertEqual(comment.body, "test comment")

        reply = discussion.add_comment("test reply", reply_to=comment, output_schema="id body")
        self.assertEqual(reply.id, "DC_kwDOADYVqs4AovYl")
        self.assertEqual(reply.body, "test reply")

        reply_by_id_str = discussion.add_comment(
            "test reply by string id", reply_to=comment.id, output_schema="id body"
        )
        self.assertEqual(reply_by_id_str.id, "DC_kwDOADYVqs4AovYm")
        self.assertEqual(reply_by_id_str.body, "test reply by string id")

        # cleanup that discussion
        # replies have to be deleted first to be able to fully delete a comment
        self.assertEqual(reply_by_id_str.delete().id, "DC_kwDOADYVqs4AovYm")
        self.assertEqual(reply.delete().id, "DC_kwDOADYVqs4AovYl")
        self.assertEqual(comment.delete().id, "DC_kwDOADYVqs4AovYk")
