# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class RepositoryAttributes(TestCase):
    @Enterprise.User(1)
    def testOwned(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        self.assertEqual(r.archive_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/{archive_format}{/ref}")
        self.assertEqual(r.assignees_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/assignees{/user}")
        self.assertEqual(r.blobs_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/git/blobs{/sha}")
        self.assertEqual(r.branches_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/branches{/branch}")
        self.assertEqual(r.clone_url, "http://github.home.jacquev6.net/ghe-user-1/repo-user-1-1.git")
        self.assertEqual(r.collaborators_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/collaborators{/collaborator}")
        self.assertEqual(r.comments_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/comments{/number}")
        self.assertEqual(r.commits_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/commits{/sha}")
        self.assertEqual(r.compare_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/compare/{base}...{head}")
        self.assertEqual(r.contents_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/contents/{+path}")
        self.assertEqual(r.contributors_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/contributors")
        self.assertEqual(r.created_at, datetime.datetime(2014, 7, 13, 18, 19, 21))
        self.assertEqual(r.default_branch, "master")
        self.assertEqual(r.description, "")
        self.assertEqual(r.downloads_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/downloads")
        self.assertEqual(r.events_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/events")
        self.assertEqual(r.fork, False)
        self.assertEqual(r.forks_count, 0)
        self.assertEqual(r.forks_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/forks")
        self.assertEqual(r.full_name, "ghe-user-1/repo-user-1-1")
        self.assertEqual(r.git_commits_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/git/commits{/sha}")
        self.assertEqual(r.git_refs_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/git/refs{/sha}")
        self.assertEqual(r.git_tags_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/git/tags{/sha}")
        self.assertEqual(r.git_url, "git://github.home.jacquev6.net/ghe-user-1/repo-user-1-1.git")
        self.assertEqual(r.has_issues, True)
        self.assertEqual(r.has_wiki, True)
        self.assertIsNone(r.homepage)
        self.assertEqual(r.hooks_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/hooks")
        self.assertEqual(r.html_url, "http://github.home.jacquev6.net/ghe-user-1/repo-user-1-1")
        self.assertEqual(r.id, 1)
        self.assertEqual(r.issue_comment_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/issues/comments/{number}")
        self.assertEqual(r.issue_events_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/issues/events{/number}")
        self.assertEqual(r.issues_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/issues{/number}")
        self.assertEqual(r.keys_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/keys{/key_id}")
        self.assertEqual(r.labels_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/labels{/name}")
        self.assertIsNone(r.language)
        self.assertEqual(r.languages_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/languages")
        self.assertEqual(r.merges_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/merges")
        self.assertEqual(r.milestones_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/milestones{/number}")
        self.assertIsNone(r.mirror_url)
        self.assertEqual(r.name, "repo-user-1-1")
        self.assertEqual(r.network_count, 0)
        self.assertEqual(r.notifications_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/notifications{?since,all,participating}")
        self.assertEqual(r.open_issues_count, 5)
        self.assertIsInstance(r.owner, PyGithub.Blocking.User.User)
        self.assertEqual(r.owner.login, "ghe-user-1")
        self.assertIsNone(r.parent)
        self.assertEqual(r.permissions.pull, True)
        self.assertEqual(r.permissions.push, True)
        self.assertEqual(r.permissions.admin, True)
        self.assertEqual(r.private, False)
        self.assertEqual(r.pulls_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/pulls{/number}")
        self.assertEqual(r.pushed_at, datetime.datetime(2014, 7, 23, 4, 52, 2))
        self.assertEqual(r.releases_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/releases{/id}")
        self.assertEqual(r.size, 444)
        self.assertIsNone(r.source)
        self.assertEqual(r.ssh_url, "git@github.home.jacquev6.net:ghe-user-1/repo-user-1-1.git")
        self.assertEqual(r.stargazers_count, 1)
        self.assertEqual(r.stargazers_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/stargazers")
        self.assertEqual(r.statuses_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/statuses/{sha}")
        self.assertEqual(r.subscribers_count, 2)
        self.assertEqual(r.subscribers_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/subscribers")
        self.assertEqual(r.subscription_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/subscription")
        self.assertEqual(r.svn_url, "http://github.home.jacquev6.net/ghe-user-1/repo-user-1-1")
        self.assertEqual(r.tags_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/tags")
        self.assertEqual(r.teams_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/teams")
        self.assertEqual(r.trees_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/git/trees{/sha}")
        self.assertEqual(r.updated_at, datetime.datetime(2014, 7, 23, 4, 52, 2))
        self.assertEqual(r.url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1")
        self.assertEqual(r.watchers_count, 1)

    @Enterprise.User(1)
    def testFork(self):
        r = self.g.get_repo(("ghe-user-3", "repo-user-1-1"))
        self.assertEqual(r.fork, True)
        self.assertIsInstance(r.parent.owner, PyGithub.Blocking.User.User)
        self.assertEqual(r.parent.owner.login, "ghe-user-1")
        self.assertIsInstance(r.source.owner, PyGithub.Blocking.User.User)
        self.assertEqual(r.source.owner.login, "ghe-user-1")

    @Enterprise.User(1)
    def testOrg(self):
        r = self.g.get_repo(("ghe-org-1", "repo-org-1-1"))
        self.assertIsInstance(r.owner, PyGithub.Blocking.Organization.Organization)
        self.assertEqual(r.owner.login, "ghe-org-1")

    @Enterprise.User(1)
    def testForkOfOrg(self):
        r = self.g.get_repo(("ghe-user-3", "repo-org-1-1"))
        self.assertIsInstance(r.owner, PyGithub.Blocking.User.User)
        self.assertIsInstance(r.parent.owner, PyGithub.Blocking.Organization.Organization)
        self.assertEqual(r.parent.owner.login, "ghe-org-1")
        self.assertIsInstance(r.source.owner, PyGithub.Blocking.Organization.Organization)
        self.assertEqual(r.source.owner.login, "ghe-org-1")


class RepositoryGitStuff(TestCase):
    @Enterprise.User(1)
    def testGetBranches(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        branches = r.get_branches()
        self.assertEqual([b.name for b in branches], ["develop", "master"])

    @Enterprise.User(1)
    def testGetBranches_allParameters(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        branches = r.get_branches(per_page=1)
        self.assertEqual([b.name for b in branches], ["develop", "master"])

    @Enterprise.User(1)
    def testGetBranch(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        b = r.get_branch("develop")
        self.assertEqual(b.commit.author.login, "ghe-user-1")

    # @todoSomeday Consider opening an issue to GitHub to fix inconsistency with Branch:
    # Branch.update can be tested like this if Branch is modified to take its url attribute from _links["self"]
    # but _links is returned only by Repository.get_branch, not by Repository.get_branches
    # so we have no way to make Branch generaly updatable
    # @Enterprise.User(1)
    # def testUpdateBranch(self):
    #     r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
    #     b = r.get_branch("test_update")
    #     self.assertEqual(b.commit.sha, "e078f69fb050b75fe5f3c7aa70adc24d692e75b8")
    #     self.assertFalse(b.update())
    #     self.assertEqual(b.commit.sha, "e078f69fb050b75fe5f3c7aa70adc24d692e75b8")
    #     r.get_git_ref("refs/heads/test_update").edit(sha="7820fadc2429652016611e98fdc21766ba075161")
    #     self.assertTrue(b.update())
    #     self.assertEqual(b.commit.sha, "7820fadc2429652016611e98fdc21766ba075161")
    #     r.get_git_ref("refs/heads/test_update").edit(sha="e078f69fb050b75fe5f3c7aa70adc24d692e75b8", force=True)

    @Enterprise.User(1)
    def testGetCommits(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        commits = r.get_commits()
        self.assertEqual([c.sha for c in commits], ["e078f69fb050b75fe5f3c7aa70adc24d692e75b8"])

    @Enterprise.User(1)
    def testGetCommits_allParameters(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        commits = r.get_commits(sha="7820fad", path="README.md", author="ghe-user-1", since=datetime.datetime(2014, 1, 1, 0, 0, 0), until=datetime.datetime(2014, 12, 31, 23, 59, 59), per_page=1)
        self.assertEqual([c.sha for c in commits], ["7820fadc2429652016611e98fdc21766ba075161", "e078f69fb050b75fe5f3c7aa70adc24d692e75b8"])

    @Enterprise.User(1)
    def testGetCommit(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        c = r.get_commit("7820fad")
        self.assertEqual(c.author.login, "ghe-user-1")
        self.assertEqual(c.commit.comment_count, 0)  # @todoAlpha Understand why this attribute is returned here, but not in r.get_git_commit

    @Enterprise.User(1)
    def testGetTags(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        tags = r.get_tags()
        self.assertEqual([t.name for t in tags], ["v0.1-beta.2", "v0.1-beta.1"])

    @Enterprise.User(1)
    def testGetTags_allParameters(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        tags = r.get_tags(per_page=1)
        self.assertEqual([t.name for t in tags], ["v0.1-beta.2", "v0.1-beta.1"])

    @Enterprise.User(1)
    def testGetGitTag(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        t = r.get_git_tag("43bafe50b11378c5546dbef02032941bb8a46099")
        self.assertEqual(t.sha, "43bafe50b11378c5546dbef02032941bb8a46099")

    @Enterprise.User(1)
    def testGetGitRefs(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        refs = r.get_git_refs()
        # @todoAlpha What about GET /repos/.../git/refs/heads? It returns a list of refs as well
        self.assertEqual([r.ref for r in refs], ["refs/heads/develop", "refs/heads/master", "refs/tags/v0.1-beta.1", "refs/tags/v0.1-beta.2"])

    @Enterprise.User(1)
    def testGetGitRefs_allParameters(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        refs = r.get_git_refs(per_page=2)
        self.assertEqual([r.ref for r in refs], ["refs/heads/develop", "refs/heads/master", "refs/tags/v0.1-beta.1", "refs/tags/v0.1-beta.2"])

    @Enterprise.User(1)
    def testGetGitRef(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        ref = r.get_git_ref("refs/heads/develop")
        # @todoAlpha Test get_git_ref with a string not starting with "refs/"
        self.assertEqual(ref.ref, "refs/heads/develop")

    @Enterprise.User(1)
    def testCreateGitBlob(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        blob = r.create_git_blob("This is some content", "utf8")
        self.assertEqual(blob.sha, "3daf0da6bca38181ab52610dd6af6e92f1a5469d")

    @Enterprise.User(1)
    def testCreateGitTree(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        tree = r.create_git_tree(tree=[{"path": "test.txt", "mode": "100644", "type": "blob", "sha": "3daf0da6bca38181ab52610dd6af6e92f1a5469d"}])
        self.assertEqual(tree.sha, "65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")

    @Enterprise.User(1)
    def testCreateInitialGitCommit(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        commit = r.create_git_commit(tree="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", message="first commit", parents=[])
        self.assertEqual(commit.message, "first commit")
        self.assertEqual(commit.tree.sha, "65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")
        self.assertEqual(len(commit.parents), 0)

    @Enterprise.User(1)
    def testCreateInitialGitCommit_allParameters(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        commit = r.create_git_commit(tree="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", message="first commit", parents=[], author={"name": "John Doe", "email": "john@doe.com", "date": "1999-12-31T23:59:59Z"}, committer={"name": "Jane Doe", "email": "jane@doe.com", "date": "2000-01-01T00:00:00Z"})
        self.assertEqual(commit.author.name, "John Doe")
        self.assertEqual(commit.author.email, "john@doe.com")
        self.assertEqual(commit.author.date, datetime.datetime(1999, 12, 31, 23, 59, 59))
        self.assertEqual(commit.committer.name, "Jane Doe")
        self.assertEqual(commit.committer.email, "jane@doe.com")
        self.assertEqual(commit.committer.date, datetime.datetime(2000, 1, 1, 0, 0, 0))

    @Enterprise.User(1)
    def testCreateSubsequentGitCommit(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        commit = r.create_git_commit(tree="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", message="second commit", parents=["7b96628d495239a926958bb5b8b935245668cc6a"])
        self.assertEqual(commit.parents[0].sha, "7b96628d495239a926958bb5b8b935245668cc6a")

    @Enterprise.User(1)
    def testCreateCommitGitRef(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        ref = r.create_git_ref(ref="refs/tests/commit_ref", sha="7b96628d495239a926958bb5b8b935245668cc6a")
        self.assertEqual(ref.ref, "refs/tests/commit_ref")
        self.assertEqual(ref.object.type, "commit")
        self.assertIsInstance(ref.object, PyGithub.Blocking.GitCommit.GitCommit)
        ref.delete()

    @Enterprise.User(1)
    def testCreateTreeGitRef(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        ref = r.create_git_ref(ref="refs/tests/tree_ref", sha="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")
        self.assertEqual(ref.ref, "refs/tests/tree_ref")
        self.assertEqual(ref.object.type, "tree")
        self.assertIsInstance(ref.object, PyGithub.Blocking.GitTree.GitTree)
        ref.delete()

    @Enterprise.User(1)
    def testCreateBlobGitRef(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        ref = r.create_git_ref(ref="refs/tests/blob_ref", sha="3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(ref.ref, "refs/tests/blob_ref")
        self.assertEqual(ref.object.type, "blob")
        self.assertIsInstance(ref.object, PyGithub.Blocking.GitBlob.GitBlob)
        ref.delete()

    @Enterprise.User(1)
    def testCreateTagGitRef(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        ref = r.create_git_ref(ref="refs/tests/tag_ref", sha="43bafe50b11378c5546dbef02032941bb8a46099")
        self.assertEqual(ref.ref, "refs/tests/tag_ref")
        self.assertEqual(ref.object.type, "tag")
        self.assertIsInstance(ref.object, PyGithub.Blocking.GitTag.GitTag)
        ref.delete()

    @Enterprise.User(1)
    def testCreateExistingGitRef(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        ref = r.create_git_ref(ref="refs/tests/commit_ref", sha="7b96628d495239a926958bb5b8b935245668cc6a")
        with self.assertRaises(PyGithub.Blocking.UnprocessableEntityException):
            r.create_git_ref(ref="refs/tests/commit_ref", sha="7b96628d495239a926958bb5b8b935245668cc6a")
        ref.delete()

    @Enterprise.User(1)
    def testCreateCommitGitTag(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        tag = r.create_git_tag(tag="commit_tag", message="This is a commit tag", object="7b96628d495239a926958bb5b8b935245668cc6a", type="commit")
        self.assertEqual(tag.object.type, "commit")
        self.assertIsInstance(tag.object, PyGithub.Blocking.GitCommit.GitCommit)

    @Enterprise.User(1)
    def testCreateGitTagWithBadType(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        with self.assertRaises(PyGithub.Blocking.UnprocessableEntityException):
            r.create_git_tag(tag="commit_tag", message="This is a commit tag", object="7b96628d495239a926958bb5b8b935245668cc6a", type="blob")

    @Enterprise.User(1)
    def testCreateGitTag_allParameters(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        tag = r.create_git_tag(tag="commit_tag", message="This is a commit tag", object="7b96628d495239a926958bb5b8b935245668cc6a", type="commit", tagger={"name": "John Doe", "email": "john@doe.com", "date": "1999-12-31T23:59:59Z"})
        self.assertEqual(tag.tagger.name, "John Doe")
        self.assertEqual(tag.tagger.email, "john@doe.com")
        self.assertEqual(tag.tagger.date, datetime.datetime(1999, 12, 31, 23, 59, 59))

    @Enterprise.User(1)
    def testCreateTreeGitTag(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        tag = r.create_git_tag(tag="tree_tag", message="This is a tree tag", object="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", type="tree")
        self.assertEqual(tag.object.type, "tree")
        self.assertIsInstance(tag.object, PyGithub.Blocking.GitTree.GitTree)

    @Enterprise.User(1)
    def testCreateBlobGitTag(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        tag = r.create_git_tag(tag="blob_tag", message="This is a blob tag", object="3daf0da6bca38181ab52610dd6af6e92f1a5469d", type="blob")
        self.assertEqual(tag.object.type, "blob")
        self.assertIsInstance(tag.object, PyGithub.Blocking.GitBlob.GitBlob)

    @Enterprise.User(1)
    def testCreateTagGitTag(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        tag = r.create_git_tag(tag="tag_tag", message="This is a tag tag", object="43bafe50b11378c5546dbef02032941bb8a46099", type="tag")
        self.assertEqual(tag.object.type, "tag")
        self.assertIsInstance(tag.object, PyGithub.Blocking.GitTag.GitTag)


class RepositoryIssues(TestCase):
    @Enterprise.User(2)
    def testCreateIssue(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        issue = r.create_issue("Created by PyGithub")
        self.assertEqual(issue.title, "Created by PyGithub")
        self.assertIsNone(issue.body)
        self.assertIsNone(issue.assignee)
        self.assertIsNone(issue.milestone)
        self.assertEqual(len(issue.labels), 0)

    @Enterprise.User(1)
    def testCreateIssue_allParameters(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        issue = r.create_issue("Also created by PyGithub", body="Body", assignee="ghe-user-1", milestone=1, labels=["question"])
        self.assertEqual(issue.title, "Also created by PyGithub")
        self.assertEqual(issue.body, "Body")
        self.assertEqual(issue.assignee.login, "ghe-user-1")
        self.assertEqual(issue.milestone.number, 1)
        self.assertEqual(len(issue.labels), 1)

    @Enterprise.User(2)
    def testGetIssues(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        issues = r.get_issues()
        self.assertEqual([i.title for i in issues[-3:]], ["Also created by PyGithub", "Created by PyGithub", "First issue"])

    @Enterprise.User(2)
    def testGetIssues_allParameters(self):
        r = self.g.get_repo(("ghe-user-1", "repo-user-1-1"))
        issues = r.get_issues(milestone=1, state="open", assignee="ghe-user-1", creator="ghe-user-1", mentioned="ghe-user-2", labels=["question"], sort="created", direction="asc", since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=1)
        self.assertEqual([i.title for i in issues], ["Also created by PyGithub"])
