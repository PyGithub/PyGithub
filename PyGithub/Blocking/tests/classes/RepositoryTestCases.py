# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class RepositoryAttributes(TestCase):
    @Enterprise("electra")
    def testOwned(self):
        r = self.g.get_repo(("electra", "immutable"))
        self.assertEqual(r.archive_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/{archive_format}{/ref}")
        self.assertEqual(r.assignees_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/assignees{/user}")
        self.assertEqual(r.blobs_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/git/blobs{/sha}")
        self.assertEqual(r.branches_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/branches{/branch}")
        self.assertEqual(r.clone_url, "http://github.home.jacquev6.net/electra/immutable.git")
        self.assertEqual(r.collaborators_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/collaborators{/collaborator}")
        self.assertEqual(r.comments_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/comments{/number}")
        self.assertEqual(r.commits_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/commits{/sha}")
        self.assertEqual(r.compare_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/compare/{base}...{head}")
        self.assertEqual(r.contents_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/contents/{+path}")
        self.assertEqual(r.contributors_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/contributors")
        self.assertEqual(r.created_at, datetime.datetime(2014, 8, 4, 2, 5, 7))
        self.assertEqual(r.default_branch, "master")
        self.assertEqual(r.description, None)
        self.assertEqual(r.downloads_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/downloads")
        self.assertEqual(r.events_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/events")
        self.assertEqual(r.fork, False)
        self.assertEqual(r.forks_count, 2)
        self.assertEqual(r.forks_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/forks")
        self.assertEqual(r.full_name, "electra/immutable")
        self.assertEqual(r.git_commits_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/git/commits{/sha}")
        self.assertEqual(r.git_refs_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/git/refs{/sha}")
        self.assertEqual(r.git_tags_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/git/tags{/sha}")
        self.assertEqual(r.git_url, "git://github.home.jacquev6.net/electra/immutable.git")
        self.assertEqual(r.has_issues, True)
        self.assertEqual(r.has_wiki, True)
        self.assertEqual(r.homepage, None)
        self.assertEqual(r.hooks_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/hooks")
        self.assertEqual(r.html_url, "http://github.home.jacquev6.net/electra/immutable")
        self.assertEqual(r.id, 34)
        self.assertEqual(r.issue_comment_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/issues/comments/{number}")
        self.assertEqual(r.issue_events_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/issues/events{/number}")
        self.assertEqual(r.issues_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/issues{/number}")
        self.assertEqual(r.keys_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/keys{/key_id}")
        self.assertEqual(r.labels_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/labels{/name}")
        self.assertEqual(r.language, None)
        self.assertEqual(r.languages_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/languages")
        self.assertEqual(r.merges_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/merges")
        self.assertEqual(r.milestones_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/milestones{/number}")
        self.assertEqual(r.mirror_url, None)
        self.assertEqual(r.name, "immutable")
        self.assertEqual(r.network_count, 2)
        self.assertEqual(r.notifications_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/notifications{?since,all,participating}")
        self.assertEqual(r.open_issues_count, 0)
        self.assertEqual(r.owner.login, "electra")
        self.assertEqual(r.parent, None)
        self.assertEqual(r.permissions.admin, True)
        self.assertEqual(r.permissions.pull, True)
        self.assertEqual(r.permissions.push, True)
        self.assertEqual(r.private, False)
        self.assertEqual(r.pulls_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/pulls{/number}")
        self.assertEqual(r.pushed_at, datetime.datetime(2014, 8, 4, 2, 5, 9))
        self.assertEqual(r.releases_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/releases{/id}")
        self.assertEqual(r.size, 0)
        self.assertEqual(r.source, None)
        self.assertEqual(r.ssh_url, "git@github.home.jacquev6.net:electra/immutable.git")
        self.assertEqual(r.stargazers_count, 0)
        self.assertEqual(r.stargazers_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/stargazers")
        self.assertEqual(r.statuses_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/statuses/{sha}")
        self.assertEqual(r.subscribers_count, 1)
        self.assertEqual(r.subscribers_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/subscribers")
        self.assertEqual(r.subscription_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/subscription")
        self.assertEqual(r.svn_url, "http://github.home.jacquev6.net/electra/immutable")
        self.assertEqual(r.tags_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/tags")
        self.assertEqual(r.teams_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/teams")
        self.assertEqual(r.trees_url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable/git/trees{/sha}")
        self.assertEqual(r.updated_at, datetime.datetime(2014, 8, 4, 2, 5, 9))
        self.assertEqual(r.url, "http://github.home.jacquev6.net/api/v3/repos/electra/immutable")
        self.assertEqual(r.watchers_count, 0)
        self.assertIsInstance(r.owner, PyGithub.Blocking.User.User)

    @Enterprise("electra")
    def testForkByOrg(self):
        r = self.g.get_repo(("olympus", "immutable"))
        self.assertEqual(r.fork, True)
        self.assertEqual(r.parent.owner.login, "electra")
        self.assertEqual(r.source.owner.login, "electra")
        self.assertIsInstance(r.owner, PyGithub.Blocking.Organization.Organization)
        self.assertIsInstance(r.parent.owner, PyGithub.Blocking.User.User)
        self.assertIsInstance(r.source.owner, PyGithub.Blocking.User.User)

    @Enterprise("electra")
    def testForkOfFork(self):
        r = self.g.get_repo(("penelope", "immutable"))
        self.assertEqual(r.parent.owner.login, "olympus")
        self.assertEqual(r.source.owner.login, "electra")
        self.assertIsInstance(r.owner, PyGithub.Blocking.User.User)
        self.assertIsInstance(r.parent.owner, PyGithub.Blocking.Organization.Organization)
        self.assertIsInstance(r.source.owner, PyGithub.Blocking.User.User)


class RepositoryCollaborators(TestCase):
    @Enterprise("electra")
    def testGetCollaborators(self):
        r = self.g.get_repo(("electra", "mutable"))
        collaborators = r.get_collaborators()
        self.assertEqual([c.login for c in collaborators], ["electra", "zeus", "penelope"])

    @Enterprise("electra")
    def testGetCollaborators_allParameters(self):
        r = self.g.get_repo(("electra", "mutable"))
        collaborators = r.get_collaborators(per_page=1)
        self.assertEqual([c.login for c in collaborators], ["electra", "zeus", "penelope"])

    @Enterprise("electra")
    def testAddToAndRemoveFromCollaborators(self):
        r = self.g.get_repo(("electra", "mutable"))
        self.assertTrue(r.has_in_collaborators("penelope"))
        r.remove_from_collaborators("penelope")
        self.assertFalse(r.has_in_collaborators("penelope"))
        r.add_to_collaborators("penelope")
        self.assertTrue(r.has_in_collaborators("penelope"))


class RepositoryContributors(TestCase):
    @Enterprise("electra")
    def testGetContributors(self):
        r = self.g.get_repo(("electra", "contributors"))
        contributors = r.get_contributors()
        self.assertEqual([c.login for c in contributors], ["electra", "penelope", "zeus"])

    @Enterprise("electra")
    def testGetContributors_allParameters(self):
        r = self.g.get_repo(("electra", "contributors"))
        contributors = r.get_contributors(anon=True, per_page=1)
        self.assertEqual(len(list(contributors)), 4)
        self.assertIsInstance(contributors[0], PyGithub.Blocking.User.User)
        self.assertEqual(contributors[0].login, "electra")
        self.assertIsInstance(contributors[1], PyGithub.Blocking.Repository.Repository.AnonymousContributor)
        self.assertEqual(contributors[1].contributions, 1)
        self.assertEqual(contributors[1].name, "Oedipus")
        self.assertEqual(contributors[1].type, "Anonymous")
        self.assertIsInstance(contributors[2], PyGithub.Blocking.User.User)
        self.assertEqual(contributors[2].login, "penelope")
        self.assertIsInstance(contributors[3], PyGithub.Blocking.User.User)
        self.assertEqual(contributors[3].login, "zeus")


class RepositoryDelete(TestCase):
    @Enterprise("electra")
    def test(self):
        r = self.g.get_authenticated_user().create_repo("ephemeral")
        r.delete()


class RepositoryEdit(TestCase):
    @Enterprise("electra")
    def testName(self):
        r = self.g.get_repo(("electra", "mutable"))
        self.assertEqual(r.name, "mutable")
        r.edit(name="mutable-bis")
        self.assertEqual(r.name, "mutable-bis")
        r.edit(name="mutable")
        self.assertEqual(r.name, "mutable")

    @Enterprise("electra")
    def testDescription(self):
        r = self.g.get_repo(("electra", "mutable"))
        self.assertEqual(r.description, None)
        r.edit(description="Mutable repository")
        self.assertEqual(r.description, "Mutable repository")
        r.edit(description=PyGithub.Blocking.Reset)
        self.assertEqual(r.description, None)

    @Enterprise("electra")
    def testHomepage(self):
        r = self.g.get_repo(("electra", "mutable"))
        self.assertEqual(r.homepage, None)
        r.edit(homepage="http://jacquev6.net/mutable")
        self.assertEqual(r.homepage, "http://jacquev6.net/mutable")
        r.edit(homepage=PyGithub.Blocking.Reset)
        self.assertEqual(r.homepage, None)

    @Enterprise("electra")
    def testPrivate(self):
        r = self.g.get_repo(("electra", "mutable"))
        self.assertEqual(r.private, False)
        r.edit(private=True)
        self.assertEqual(r.private, True)
        r.edit(private=False)
        self.assertEqual(r.private, False)

    @Enterprise("electra")
    def testHasIssues(self):
        r = self.g.get_repo(("electra", "mutable"))
        self.assertEqual(r.has_issues, True)
        r.edit(has_issues=False)
        self.assertEqual(r.has_issues, False)
        r.edit(has_issues=True)
        self.assertEqual(r.has_issues, True)

    @Enterprise("electra")
    def testHasWiki(self):
        r = self.g.get_repo(("electra", "mutable"))
        self.assertEqual(r.has_wiki, True)
        r.edit(has_wiki=False)
        self.assertEqual(r.has_wiki, False)
        r.edit(has_wiki=True)
        self.assertEqual(r.has_wiki, True)

    @Enterprise("electra")
    def testDefaultBranch(self):
        r = self.g.get_repo(("electra", "mutable"))
        self.assertEqual(r.default_branch, "master")
        # @todoAlpha test with a Branch instance
        r.edit(default_branch="develop")
        self.assertEqual(r.default_branch, "develop")
        r.edit(default_branch="master")
        self.assertEqual(r.default_branch, "master")


class RepositoryGitStuff(TestCase):
    @Enterprise("electra")
    def testGetBranches(self):
        r = self.g.get_repo(("electra", "git-objects"))
        branches = r.get_branches()
        self.assertEqual([b.name for b in branches], ["develop", "master"])

    @Enterprise("electra")
    def testGetBranches_allParameters(self):
        r = self.g.get_repo(("electra", "git-objects"))
        branches = r.get_branches(per_page=1)
        self.assertEqual([b.name for b in branches], ["develop", "master"])

    @Enterprise("electra")
    def testGetBranch(self):
        r = self.g.get_repo(("electra", "git-objects"))
        b = r.get_branch("develop")
        self.assertEqual(b.commit.author.login, "electra")

    # @todoSomeday Consider opening an issue to GitHub to fix inconsistency with Branch:
    # Branch.update can be tested like this if Branch is modified to take its url attribute from _links["self"]
    # but _links is returned only by Repository.get_branch, not by Repository.get_branches
    # so we have no way to make Branch generaly updatable
    # @Enterprise("electra")
    # def testUpdateBranch(self):
    #     r = self.g.get_repo(("electra", "git-objects"))
    #     b = r.get_branch("test_update")
    #     self.assertEqual(b.commit.sha, "e078f69fb050b75fe5f3c7aa70adc24d692e75b8")
    #     self.assertFalse(b.update())
    #     self.assertEqual(b.commit.sha, "e078f69fb050b75fe5f3c7aa70adc24d692e75b8")
    #     r.get_git_ref("refs/heads/test_update").edit(sha="7820fadc2429652016611e98fdc21766ba075161")
    #     self.assertTrue(b.update())
    #     self.assertEqual(b.commit.sha, "7820fadc2429652016611e98fdc21766ba075161")
    #     r.get_git_ref("refs/heads/test_update").edit(sha="e078f69fb050b75fe5f3c7aa70adc24d692e75b8", force=True)

    @Enterprise("electra")
    def testGetCommits(self):
        r = self.g.get_repo(("electra", "git-objects"))
        commits = r.get_commits()
        self.assertEqual([c.commit.message for c in commits], ["Modify README.md", "Create foo.md", "Initial commit"])

    @Enterprise("electra")
    def testGetCommits_allParameters(self):
        r = self.g.get_repo(("electra", "git-objects"))
        commits = r.get_commits(sha="refs/heads/master", path="README.md", author="electra", since=datetime.datetime(2014, 1, 1, 0, 0, 0), until=datetime.datetime(2049, 12, 31, 23, 59, 59), per_page=1)
        self.assertEqual([c.commit.message for c in commits], ["Modify README.md", "Initial commit"])

    @Enterprise("electra")
    def testGetCommit(self):
        r = self.g.get_repo(("electra", "git-objects"))
        c = r.get_commit("refs/heads/master")
        self.assertEqual(c.commit.message, "Modify README.md")

    @Enterprise("electra")
    def testGetTags(self):
        r = self.g.get_repo(("electra", "git-objects"))
        tags = r.get_tags()
        self.assertEqual([t.name for t in tags], ["light-tag-2", "light-tag-1"])

    @Enterprise("electra")
    def testGetTags_allParameters(self):
        r = self.g.get_repo(("electra", "git-objects"))
        tags = r.get_tags(per_page=1)
        self.assertEqual([t.name for t in tags], ["light-tag-2", "light-tag-1"])

    @Enterprise("electra")
    def testGetGitTag(self):
        r = self.g.get_repo(("electra", "git-objects"))
        t = r.get_git_tag("b55a47efb4f8c891b6719a3d85a80c7f875e33ec")
        self.assertEqual(t.tag, "heavy-tag")

    @Enterprise("electra")
    def testGetGitRefs(self):
        r = self.g.get_repo(("electra", "git-objects"))
        refs = r.get_git_refs()
        # @todoAlpha What about GET /repos/.../git/refs/heads? It returns a list of refs as well
        self.assertEqual([r.ref for r in refs], ["refs/heads/develop", "refs/heads/master", "refs/tags/light-tag-1", "refs/tags/light-tag-2"])

    @Enterprise("electra")
    def testGetGitRefs_allParameters(self):
        r = self.g.get_repo(("electra", "git-objects"))
        refs = r.get_git_refs(per_page=2)
        self.assertEqual([r.ref for r in refs], ["refs/heads/develop", "refs/heads/master", "refs/tags/light-tag-1", "refs/tags/light-tag-2"])

    @Enterprise("electra")
    def testGetGitRef(self):
        r = self.g.get_repo(("electra", "git-objects"))
        ref = r.get_git_ref("refs/heads/develop")
        # @todoAlpha Test get_git_ref with a string not starting with "refs/"
        self.assertEqual(ref.ref, "refs/heads/develop")

    @Enterprise("electra")
    def testCreateGitBlob(self):
        r = self.g.get_repo(("electra", "git-objects"))
        blob = r.create_git_blob("This is some content", "utf8")
        self.assertEqual(blob.sha, "3daf0da6bca38181ab52610dd6af6e92f1a5469d")

    @Enterprise("electra")
    def testGetGitBlob(self):
        r = self.g.get_repo(("electra", "git-objects"))
        blob = r.get_git_blob("3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(blob.content, "VGhpcyBpcyBzb21lIGNvbnRlbnQ=\n")

    @Enterprise("electra")
    def testCreateGitTree(self):
        r = self.g.get_repo(("electra", "git-objects"))
        tree = r.create_git_tree(tree=[{"path": "test.txt", "mode": "100644", "type": "blob", "sha": "3daf0da6bca38181ab52610dd6af6e92f1a5469d"}])
        self.assertEqual(tree.sha, "65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")

    @Enterprise("electra")
    def testGetGitTree(self):
        r = self.g.get_repo(("electra", "git-objects"))
        tree = r.get_git_tree("65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")
        self.assertEqual(len(tree.tree), 1)

    @Enterprise("electra")
    def testGetGitCommit(self):
        r = self.g.get_repo(("electra", "git-objects"))
        commit = r.get_git_commit("f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")
        self.assertEqual(commit.message, "first commit")

    @Enterprise("electra")
    def testCreateInitialGitCommit(self):
        r = self.g.get_repo(("electra", "git-objects"))
        commit = r.create_git_commit(tree="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", message="first commit", parents=[])
        self.assertEqual(commit.message, "first commit")
        self.assertEqual(commit.tree.sha, "65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")
        self.assertEqual(len(commit.parents), 0)

    @Enterprise("electra")
    def testCreateInitialGitCommit_allParameters(self):
        r = self.g.get_repo(("electra", "git-objects"))
        commit = r.create_git_commit(tree="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", message="first commit", parents=[], author={"name": "John Doe", "email": "john@doe.com", "date": "1999-12-31T23:59:59Z"}, committer={"name": "Jane Doe", "email": "jane@doe.com", "date": "2000-01-01T00:00:00Z"})
        self.assertEqual(commit.author.name, "John Doe")
        self.assertEqual(commit.author.email, "john@doe.com")
        self.assertEqual(commit.author.date, datetime.datetime(1999, 12, 31, 23, 59, 59))
        self.assertEqual(commit.committer.name, "Jane Doe")
        self.assertEqual(commit.committer.email, "jane@doe.com")
        self.assertEqual(commit.committer.date, datetime.datetime(2000, 1, 1, 0, 0, 0))
        self.assertEqual(commit.sha, "f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")

    @Enterprise("electra")
    def testCreateSubsequentGitCommit(self):
        r = self.g.get_repo(("electra", "git-objects"))
        commit = r.create_git_commit(tree="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", message="second commit", parents=["f739e7ae2fd0e7b2bce99c073bcc7b57d713877e"])
        self.assertEqual(commit.parents[0].sha, "f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")

    @Enterprise("electra")
    def testCreateGitRef_commit(self):
        r = self.g.get_repo(("electra", "git-objects"))
        ref = r.create_git_ref(ref="refs/tests/commit_ref", sha="f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")
        self.assertEqual(ref.ref, "refs/tests/commit_ref")
        self.assertEqual(ref.object.type, "commit")
        self.assertIsInstance(ref.object, PyGithub.Blocking.GitCommit.GitCommit)
        ref.delete()

    @Enterprise("electra")
    def testCreateGitRef_tree(self):
        r = self.g.get_repo(("electra", "git-objects"))
        ref = r.create_git_ref(ref="refs/tests/tree_ref", sha="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")
        self.assertEqual(ref.ref, "refs/tests/tree_ref")
        self.assertEqual(ref.object.type, "tree")
        self.assertIsInstance(ref.object, PyGithub.Blocking.GitTree.GitTree)
        ref.delete()

    @Enterprise("electra")
    def testCreateGitRef_blob(self):
        r = self.g.get_repo(("electra", "git-objects"))
        ref = r.create_git_ref(ref="refs/tests/blob_ref", sha="3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(ref.ref, "refs/tests/blob_ref")
        self.assertEqual(ref.object.type, "blob")
        self.assertIsInstance(ref.object, PyGithub.Blocking.GitBlob.GitBlob)
        ref.delete()

    @Enterprise("electra")
    def testCreateGitRef_tag(self):
        r = self.g.get_repo(("electra", "git-objects"))
        ref = r.create_git_ref(ref="refs/tests/tag_ref", sha="b55a47efb4f8c891b6719a3d85a80c7f875e33ec")
        self.assertEqual(ref.ref, "refs/tests/tag_ref")
        self.assertEqual(ref.object.type, "tag")
        self.assertIsInstance(ref.object, PyGithub.Blocking.GitTag.GitTag)
        ref.delete()

    @Enterprise("electra")
    def testCreateGitRef_existing(self):
        r = self.g.get_repo(("electra", "git-objects"))
        with self.assertRaises(PyGithub.Blocking.UnprocessableEntityException):
            r.create_git_ref(ref="refs/heads/master", sha="f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")

    @Enterprise("electra")
    def testCreateGitTag_allParameters(self):
        r = self.g.get_repo(("electra", "git-objects"))
        tag = r.create_git_tag(tag="heavy-tag", message="This is a tag", object="f739e7ae2fd0e7b2bce99c073bcc7b57d713877e", type="commit", tagger={"name": "John Doe", "email": "john@doe.com", "date": "1999-12-31T23:59:59Z"})
        self.assertEqual(tag.tagger.name, "John Doe")
        self.assertEqual(tag.tagger.email, "john@doe.com")
        self.assertEqual(tag.tagger.date, datetime.datetime(1999, 12, 31, 23, 59, 59))
        self.assertEqual(tag.sha, "b55a47efb4f8c891b6719a3d85a80c7f875e33ec")

    @Enterprise("electra")
    def testCreateGitTag_commit(self):
        r = self.g.get_repo(("electra", "git-objects"))
        tag = r.create_git_tag(tag="commit_tag", message="This is a commit tag", object="f739e7ae2fd0e7b2bce99c073bcc7b57d713877e", type="commit")
        self.assertEqual(tag.object.type, "commit")
        self.assertIsInstance(tag.object, PyGithub.Blocking.GitCommit.GitCommit)

    @Enterprise("electra")
    def testCreateGitTag_tree(self):
        r = self.g.get_repo(("electra", "git-objects"))
        tag = r.create_git_tag(tag="tree_tag", message="This is a tree tag", object="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", type="tree")
        self.assertEqual(tag.object.type, "tree")
        self.assertIsInstance(tag.object, PyGithub.Blocking.GitTree.GitTree)

    @Enterprise("electra")
    def testCreateGitTag_blob(self):
        r = self.g.get_repo(("electra", "git-objects"))
        tag = r.create_git_tag(tag="blob_tag", message="This is a blob tag", object="3daf0da6bca38181ab52610dd6af6e92f1a5469d", type="blob")
        self.assertEqual(tag.object.type, "blob")
        self.assertIsInstance(tag.object, PyGithub.Blocking.GitBlob.GitBlob)

    @Enterprise("electra")
    def testCreateGitTag_tag(self):
        r = self.g.get_repo(("electra", "git-objects"))
        tag = r.create_git_tag(tag="tag_tag", message="This is a tag tag", object="b55a47efb4f8c891b6719a3d85a80c7f875e33ec", type="tag")
        self.assertEqual(tag.object.type, "tag")
        self.assertIsInstance(tag.object, PyGithub.Blocking.GitTag.GitTag)

    @Enterprise("electra")
    def testCreateGitTag_badType(self):
        r = self.g.get_repo(("electra", "git-objects"))
        with self.assertRaises(PyGithub.Blocking.UnprocessableEntityException):
            r.create_git_tag(tag="bad_tag", message="This is a tag to a commit, pretending to be a blob", object="f739e7ae2fd0e7b2bce99c073bcc7b57d713877e", type="blob")


class RepositoryIssues(TestCase):
    @Enterprise("electra")
    def testCreateIssue(self):
        r = self.g.get_repo(("electra", "mutable"))
        issue = r.create_issue("Created by PyGithub")
        self.assertEqual(issue.title, "Created by PyGithub")
        self.assertIsNone(issue.body)
        self.assertIsNone(issue.assignee)
        self.assertIsNone(issue.milestone)
        self.assertEqual(len(issue.labels), 0)
        issue.edit(state="closed")

    @Enterprise("electra")
    def testCreateIssue_allParameters(self):
        r = self.g.get_repo(("electra", "mutable"))
        issue = r.create_issue("Also created by PyGithub", body="Body", assignee="electra", milestone=1, labels=["question"])
        self.assertEqual(issue.title, "Also created by PyGithub")
        self.assertEqual(issue.body, "Body")
        self.assertEqual(issue.assignee.login, "electra")
        self.assertEqual(issue.milestone.number, 1)
        self.assertEqual(len(issue.labels), 1)
        issue.edit(state="closed")

    @Enterprise("electra")
    def testGetIssue(self):
        r = self.g.get_repo(("electra", "issues"))
        issue = r.get_issue(1)
        self.assertEqual(issue.title, "Immutable issue")

    @Enterprise("electra")
    def testGetIssues(self):
        r = self.g.get_repo(("electra", "issues"))
        issues = r.get_issues()
        self.assertEqual([i.title for i in issues], ["Mutable issue", "Immutable issue"])

    @Enterprise("electra")
    def testGetIssues_allParameters(self):
        r = self.g.get_repo(("electra", "issues"))
        issues = r.get_issues(milestone=1, state="closed", assignee="electra", creator="penelope", mentioned="electra", labels=["question"], sort="created", direction="asc", since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=1)
        self.assertEqual([i.title for i in issues], ["Closed issue 1", "Closed issue 2"])

    @Enterprise("electra")
    def testHasInAssignees(self):
        r = self.g.get_repo(("electra", "issues"))
        self.assertTrue(r.has_in_assignees("penelope"))
        self.assertFalse(r.has_in_assignees("zeus"))

    @Enterprise("electra")
    def testGetAssignees(self):
        r = self.g.get_repo(("electra", "issues"))
        assignees = r.get_assignees()
        self.assertEqual([a.login for a in assignees], ["electra", "penelope"])

    @Enterprise("electra")
    def testGetAssignees_allParameters(self):
        r = self.g.get_repo(("electra", "issues"))
        assignees = r.get_assignees(per_page=1)
        self.assertEqual([a.login for a in assignees], ["electra", "penelope"])

    @Enterprise("electra")
    def testGetLabels(self):
        r = self.g.get_repo(("electra", "issues"))
        labels = r.get_labels()
        self.assertEqual([l.name for l in labels], ["bug", "duplicate", "enhancement", "help wanted", "invalid", "question", "wontfix"])

    @Enterprise("electra")
    def testCreateLabel(self):
        r = self.g.get_repo(("electra", "mutable"))
        label = r.create_label("to_be_deleted", "FF0000")
        self.assertEqual(label.color, "FF0000")
        label.delete()

    @Enterprise("electra")
    def testGetLabel(self):
        r = self.g.get_repo(("electra", "issues"))
        label = r.get_label("bug")
        self.assertEqual(label.color, "fc2929")

    # @todoAlpha follow-up with issue opened to github for labels with % sign
    # def testGetLabelWithWeirdName(self):
    #     label = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_label("space é % space")
    #     self.assertEqual(label.name, "space é % space".decode("utf-8"))

    @Enterprise("electra")
    def testCreateMilestone(self):
        r = self.g.get_repo(("electra", "mutable"))
        milestone = r.create_milestone("Created by PyGithub")
        self.assertEqual(milestone.title, "Created by PyGithub")
        self.assertEqual(milestone.state, "open")
        self.assertIsNone(milestone.description)
        self.assertIsNone(milestone.due_on)
        milestone.delete()

    @Enterprise("electra")
    def testCreateMilestone_allParameters(self):
        r = self.g.get_repo(("electra", "mutable"))
        milestone = r.create_milestone("Created by PyGithub", state="closed", description="Body", due_on="2014-08-01T00:00:00Z")
        self.assertEqual(milestone.title, "Created by PyGithub")
        self.assertEqual(milestone.state, "closed")
        self.assertEqual(milestone.description, "Body")
        self.assertEqual(milestone.due_on, datetime.datetime(2014, 8, 1, 0, 0, 0))
        milestone.delete()

    @Enterprise("electra")
    def testGetMilestone(self):
        r = self.g.get_repo(("electra", "issues"))
        milestone = r.get_milestone(1)
        self.assertEqual(milestone.title, "Immutable milestone")

    @Enterprise("electra")
    def testGetMilestones(self):
        r = self.g.get_repo(("electra", "issues"))
        milestones = r.get_milestones()
        self.assertEqual([m.title for m in milestones], ["Immutable milestone", "Mutable milestone"])

    @Enterprise("electra")
    def testGetMilestones_allParameters(self):
        r = self.g.get_repo(("electra", "issues"))
        milestones = r.get_milestones(state="open", sort="due_date", direction="asc", per_page=1)
        self.assertEqual([m.title for m in milestones], ["Immutable milestone", "Mutable milestone"])

    @Enterprise("electra")
    def testCreatePull(self):
        r = self.g.get_repo(("electra", "pulls"))
        p = r.create_pull("Created by PyGithub", "penelope:issue_to_pull", "master")
        self.assertEqual(p.title, "Created by PyGithub")
        self.assertEqual(p.base.label, "electra:master")
        self.assertEqual(p.head.label, "penelope:issue_to_pull")
        self.assertEqual(p.body, None)
        p.edit(state="closed")

    @Enterprise("electra")
    def testCreatePull_allParameters(self):
        r = self.g.get_repo(("electra", "pulls"))
        p = r.create_pull("Also created by PyGithub", "penelope:issue_to_pull", "master", "Body body body")
        self.assertEqual(p.title, "Also created by PyGithub")
        self.assertEqual(p.base.label, "electra:master")
        self.assertEqual(p.head.label, "penelope:issue_to_pull")
        self.assertEqual(p.body, "Body body body")
        p.edit(state="closed")

    @Enterprise("electra")
    def testGetPulls(self):
        r = self.g.get_repo(("electra", "pulls"))
        pulls = r.get_pulls()
        self.assertEqual([p.title for p in pulls], ["Mutable pull", "Conflict pull", "Mergeable pull"])

    @Enterprise("electra")
    def testGetPulls_almostAllParameters(self):
        r = self.g.get_repo(("electra", "pulls"))
        pulls = r.get_pulls(state="open", head="penelope:mergeable", sort="updated", direction="asc")
        self.assertEqual([p.title for p in pulls], ["Mergeable pull"])

    @Enterprise("electra")
    def testGetPulls_base(self):
        r = self.g.get_repo(("electra", "pulls"))
        pulls = r.get_pulls(base="master", per_page=1)
        self.assertEqual([p.title for p in pulls], ["Mutable pull", "Conflict pull", "Mergeable pull"])

    @Enterprise("electra")
    def testGetPull(self):
        r = self.g.get_repo(("electra", "pulls"))
        pull = r.get_pull(1)
        self.assertEqual(pull.title, "Merged pull")
