# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking
import PyGithub.Blocking.Dir
import PyGithub.Blocking.File
import PyGithub.Blocking.User

import PyGithub.Blocking.tests.Framework as Framework


class RepositoryTestCase(Framework.SimpleLoginTestCase):
    def testAttributesOfOwnedRepository(self):
        r = self.g.get_repo("jacquev6/PyGithub")
        self.assertEqual(r.archive_url, "https://api.github.com/repos/jacquev6/PyGithub/{archive_format}{/ref}")
        self.assertEqual(r.assignees_url, "https://api.github.com/repos/jacquev6/PyGithub/assignees{/user}")
        self.assertEqual(r.blobs_url, "https://api.github.com/repos/jacquev6/PyGithub/git/blobs{/sha}")
        self.assertEqual(r.branches_url, "https://api.github.com/repos/jacquev6/PyGithub/branches{/branch}")
        self.assertEqual(r.clone_url, "https://github.com/jacquev6/PyGithub.git")
        self.assertEqual(r.collaborators_url, "https://api.github.com/repos/jacquev6/PyGithub/collaborators{/collaborator}")
        self.assertEqual(r.comments_url, "https://api.github.com/repos/jacquev6/PyGithub/comments{/number}")
        self.assertEqual(r.commits_url, "https://api.github.com/repos/jacquev6/PyGithub/commits{/sha}")
        self.assertEqual(r.compare_url, "https://api.github.com/repos/jacquev6/PyGithub/compare/{base}...{head}")
        self.assertEqual(r.contents_url, "https://api.github.com/repos/jacquev6/PyGithub/contents/{+path}")
        self.assertEqual(r.contributors_url, "https://api.github.com/repos/jacquev6/PyGithub/contributors")
        self.assertEqual(r.created_at, datetime.datetime(2012, 2, 25, 12, 53, 47))
        self.assertEqual(r.default_branch, "master")
        self.assertEqual(r.description, "Python library implementing the full Github API v3")
        self.assertEqual(r.downloads_url, "https://api.github.com/repos/jacquev6/PyGithub/downloads")
        self.assertEqual(r.events_url, "https://api.github.com/repos/jacquev6/PyGithub/events")
        self.assertEqual(r.fork, False)
        self.assertEqual(r.forks, 89)
        self.assertEqual(r.forks_count, 89)
        self.assertEqual(r.forks_url, "https://api.github.com/repos/jacquev6/PyGithub/forks")
        self.assertEqual(r.full_name, "jacquev6/PyGithub")
        self.assertEqual(r.git_commits_url, "https://api.github.com/repos/jacquev6/PyGithub/git/commits{/sha}")
        self.assertEqual(r.git_refs_url, "https://api.github.com/repos/jacquev6/PyGithub/git/refs{/sha}")
        self.assertEqual(r.git_tags_url, "https://api.github.com/repos/jacquev6/PyGithub/git/tags{/sha}")
        self.assertEqual(r.git_url, "git://github.com/jacquev6/PyGithub.git")
        self.assertEqual(r.has_issues, True)
        self.assertEqual(r.has_wiki, True)
        self.assertEqual(r.homepage, "http://jacquev6.github.com/PyGithub")
        self.assertEqual(r.hooks_url, "https://api.github.com/repos/jacquev6/PyGithub/hooks")
        self.assertEqual(r.html_url, "https://github.com/jacquev6/PyGithub")
        self.assertEqual(r.id, 3544490)
        self.assertEqual(r.issue_comment_url, "https://api.github.com/repos/jacquev6/PyGithub/issues/comments/{number}")
        self.assertEqual(r.issue_events_url, "https://api.github.com/repos/jacquev6/PyGithub/issues/events{/number}")
        self.assertEqual(r.issues_url, "https://api.github.com/repos/jacquev6/PyGithub/issues{/number}")
        self.assertEqual(r.keys_url, "https://api.github.com/repos/jacquev6/PyGithub/keys{/key_id}")
        self.assertEqual(r.labels_url, "https://api.github.com/repos/jacquev6/PyGithub/labels{/name}")
        self.assertEqual(r.language, "Python")
        self.assertEqual(r.languages_url, "https://api.github.com/repos/jacquev6/PyGithub/languages")
        self.assertEqual(r.merges_url, "https://api.github.com/repos/jacquev6/PyGithub/merges")
        self.assertEqual(r.milestones_url, "https://api.github.com/repos/jacquev6/PyGithub/milestones{/number}")
        self.assertEqual(r.mirror_url, None)
        self.assertEqual(r.name, "PyGithub")
        self.assertEqual(r.network_count, 89)
        self.assertEqual(r.notifications_url, "https://api.github.com/repos/jacquev6/PyGithub/notifications{?since,all,participating}")
        self.assertEqual(r.open_issues, 26)
        self.assertEqual(r.open_issues_count, 26)
        self.assertEqual(r.owner.login, "jacquev6")
        self.assertEqual(r.owner.type, "User")
        self.assertTrue(isinstance(r.owner, PyGithub.Blocking.User.User))
        self.assertEqual(r.permissions.admin, True)
        self.assertEqual(r.permissions.push, True)
        self.assertEqual(r.permissions.pull, True)
        self.assertEqual(r.private, False)
        self.assertEqual(r.pulls_url, "https://api.github.com/repos/jacquev6/PyGithub/pulls{/number}")
        self.assertEqual(r.pushed_at, datetime.datetime(2013, 12, 16, 2, 11, 29))
        self.assertEqual(r.releases_url, "https://api.github.com/repos/jacquev6/PyGithub/releases{/id}")
        self.assertEqual(r.size, 8785)
        self.assertEqual(r.ssh_url, "git@github.com:jacquev6/PyGithub.git")
        self.assertEqual(r.stargazers_count, 315)
        self.assertEqual(r.stargazers_url, "https://api.github.com/repos/jacquev6/PyGithub/stargazers")
        self.assertEqual(r.statuses_url, "https://api.github.com/repos/jacquev6/PyGithub/statuses/{sha}")
        self.assertEqual(r.subscribers_count, 32)
        self.assertEqual(r.subscribers_url, "https://api.github.com/repos/jacquev6/PyGithub/subscribers")
        self.assertEqual(r.subscription_url, "https://api.github.com/repos/jacquev6/PyGithub/subscription")
        self.assertEqual(r.svn_url, "https://github.com/jacquev6/PyGithub")
        self.assertEqual(r.tags_url, "https://api.github.com/repos/jacquev6/PyGithub/tags")
        self.assertEqual(r.teams_url, "https://api.github.com/repos/jacquev6/PyGithub/teams")
        self.assertEqual(r.trees_url, "https://api.github.com/repos/jacquev6/PyGithub/git/trees{/sha}")
        self.assertEqual(r.updated_at, datetime.datetime(2013, 12, 19, 9, 39, 44))
        self.assertEqual(r.url, "https://api.github.com/repos/jacquev6/PyGithub")
        self.assertEqual(r.watchers, 315)
        self.assertEqual(r.watchers_count, 315)

    def testAttributesOfOtherRepository(self):
        r = self.g.get_repo("nvie/gitflow")
        self.assertEqual(r.archive_url, "https://api.github.com/repos/nvie/gitflow/{archive_format}{/ref}")
        self.assertEqual(r.assignees_url, "https://api.github.com/repos/nvie/gitflow/assignees{/user}")
        self.assertEqual(r.blobs_url, "https://api.github.com/repos/nvie/gitflow/git/blobs{/sha}")
        self.assertEqual(r.branches_url, "https://api.github.com/repos/nvie/gitflow/branches{/branch}")
        self.assertEqual(r.clone_url, "https://github.com/nvie/gitflow.git")
        self.assertEqual(r.collaborators_url, "https://api.github.com/repos/nvie/gitflow/collaborators{/collaborator}")
        self.assertEqual(r.comments_url, "https://api.github.com/repos/nvie/gitflow/comments{/number}")
        self.assertEqual(r.commits_url, "https://api.github.com/repos/nvie/gitflow/commits{/sha}")
        self.assertEqual(r.compare_url, "https://api.github.com/repos/nvie/gitflow/compare/{base}...{head}")
        self.assertEqual(r.contents_url, "https://api.github.com/repos/nvie/gitflow/contents/{+path}")
        self.assertEqual(r.contributors_url, "https://api.github.com/repos/nvie/gitflow/contributors")
        self.assertEqual(r.created_at, datetime.datetime(2010, 1, 20, 23, 14, 12))
        self.assertEqual(r.default_branch, "develop")
        self.assertEqual(r.description, "Git extensions to provide high-level repository operations for Vincent Driessen's branching model.")
        self.assertEqual(r.downloads_url, "https://api.github.com/repos/nvie/gitflow/downloads")
        self.assertEqual(r.events_url, "https://api.github.com/repos/nvie/gitflow/events")
        self.assertEqual(r.fork, False)
        self.assertEqual(r.forks, 897)
        self.assertEqual(r.forks_count, 897)
        self.assertEqual(r.forks_url, "https://api.github.com/repos/nvie/gitflow/forks")
        self.assertEqual(r.full_name, "nvie/gitflow")
        self.assertEqual(r.git_commits_url, "https://api.github.com/repos/nvie/gitflow/git/commits{/sha}")
        self.assertEqual(r.git_refs_url, "https://api.github.com/repos/nvie/gitflow/git/refs{/sha}")
        self.assertEqual(r.git_tags_url, "https://api.github.com/repos/nvie/gitflow/git/tags{/sha}")
        self.assertEqual(r.git_url, "git://github.com/nvie/gitflow.git")
        self.assertEqual(r.has_issues, True)
        self.assertEqual(r.has_wiki, True)
        self.assertEqual(r.homepage, "http://nvie.com/posts/a-successful-git-branching-model/")
        self.assertEqual(r.hooks_url, "https://api.github.com/repos/nvie/gitflow/hooks")
        self.assertEqual(r.html_url, "https://github.com/nvie/gitflow")
        self.assertEqual(r.id, 481366)
        self.assertEqual(r.issue_comment_url, "https://api.github.com/repos/nvie/gitflow/issues/comments/{number}")
        self.assertEqual(r.issue_events_url, "https://api.github.com/repos/nvie/gitflow/issues/events{/number}")
        self.assertEqual(r.issues_url, "https://api.github.com/repos/nvie/gitflow/issues{/number}")
        self.assertEqual(r.keys_url, "https://api.github.com/repos/nvie/gitflow/keys{/key_id}")
        self.assertEqual(r.labels_url, "https://api.github.com/repos/nvie/gitflow/labels{/name}")
        self.assertEqual(r.language, "Shell")
        self.assertEqual(r.languages_url, "https://api.github.com/repos/nvie/gitflow/languages")
        self.assertEqual(r.merges_url, "https://api.github.com/repos/nvie/gitflow/merges")
        self.assertEqual(r.milestones_url, "https://api.github.com/repos/nvie/gitflow/milestones{/number}")
        self.assertEqual(r.mirror_url, None)
        self.assertEqual(r.name, "gitflow")
        self.assertEqual(r.network_count, 897)
        self.assertEqual(r.notifications_url, "https://api.github.com/repos/nvie/gitflow/notifications{?since,all,participating}")
        self.assertEqual(r.open_issues, 176)
        self.assertEqual(r.open_issues_count, 176)
        self.assertEqual(r.owner.login, "nvie")
        self.assertEqual(r.owner.type, "User")
        self.assertTrue(isinstance(r.owner, PyGithub.Blocking.User.User))
        self.assertEqual(r.permissions.admin, False)
        self.assertEqual(r.permissions.push, False)
        self.assertEqual(r.permissions.pull, True)
        self.assertEqual(r.private, False)
        self.assertEqual(r.pulls_url, "https://api.github.com/repos/nvie/gitflow/pulls{/number}")
        self.assertEqual(r.pushed_at, datetime.datetime(2012, 9, 26, 10, 25, 25))
        self.assertEqual(r.releases_url, "https://api.github.com/repos/nvie/gitflow/releases{/id}")
        self.assertEqual(r.size, 5662)
        self.assertEqual(r.ssh_url, "git@github.com:nvie/gitflow.git")
        self.assertEqual(r.stargazers_count, 7973)
        self.assertEqual(r.stargazers_url, "https://api.github.com/repos/nvie/gitflow/stargazers")
        self.assertEqual(r.statuses_url, "https://api.github.com/repos/nvie/gitflow/statuses/{sha}")
        self.assertEqual(r.subscribers_count, 369)
        self.assertEqual(r.subscribers_url, "https://api.github.com/repos/nvie/gitflow/subscribers")
        self.assertEqual(r.subscription_url, "https://api.github.com/repos/nvie/gitflow/subscription")
        self.assertEqual(r.svn_url, "https://github.com/nvie/gitflow")
        self.assertEqual(r.tags_url, "https://api.github.com/repos/nvie/gitflow/tags")
        self.assertEqual(r.teams_url, "https://api.github.com/repos/nvie/gitflow/teams")
        self.assertEqual(r.trees_url, "https://api.github.com/repos/nvie/gitflow/git/trees{/sha}")
        self.assertEqual(r.updated_at, datetime.datetime(2013, 12, 20, 5, 57, 21))
        self.assertEqual(r.url, "https://api.github.com/repos/nvie/gitflow")
        self.assertEqual(r.watchers, 7973)
        self.assertEqual(r.watchers_count, 7973)

    def testAttributesOfFork(self):
        r = self.g.get_repo("lentty/PyGithub")
        self.assertEqual(r.fork, True)
        self.assertEqual(r.parent.owner.login, "akfish")
        self.assertEqual(r.source.owner.login, "jacquev6")

    def testAttributesOfOrganizationRepository(self):
        # @todoSomeday Open an issue because repo.owner contains silly attributes when owner is an org (following_url, etc. See deprecated_attributes in Organization.yml)
        # @todoSomeday Open an issue because repo contains a "organization" attribute when owner is an org
        r = self.g.get_repo("graphite-project/whisper")
        self.assertEqual(r.owner.login, "graphite-project")
        self.assertEqual(r.owner.type, "Organization")
        self.assertTrue(isinstance(r.owner, PyGithub.Blocking.Organization.Organization))

    def testAttributesOfForkOfOrganizationRepository(self):
        r = self.g.get_repo("ryansndrs/whisper")
        self.assertEqual(r.owner.login, "ryansndrs")
        self.assertEqual(r.owner.type, "User")
        self.assertTrue(isinstance(r.owner, PyGithub.Blocking.User.User))
        self.assertEqual(r.parent.owner.login, "richg")
        self.assertEqual(r.parent.owner.type, "User")
        self.assertTrue(isinstance(r.parent.owner, PyGithub.Blocking.User.User))
        self.assertEqual(r.source.owner.login, "graphite-project")
        self.assertEqual(r.source.owner.type, "Organization")
        self.assertTrue(isinstance(r.source.owner, PyGithub.Blocking.Organization.Organization))

    def testGetStargazers(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_stargazers(per_page=3)
        self.assertEqual(users[0].login, "ybakos")
        self.assertEqual(users[1].login, "huxley")

    def testGetAssignees(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_assignees()
        self.assertEqual(users[0].login, "jacquev6")

    def testGetAssignees_allParameters(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_assignees(per_page=3)
        self.assertEqual(users[0].login, "jacquev6")

    def testHasInAssignees(self):
        repo = self.g.get_repo("jacquev6/PyGithub")
        self.assertTrue(repo.has_in_assignees("jacquev6"))
        self.assertFalse(repo.has_in_assignees("nvie"))

    def testGetCollaborators(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_collaborators()
        self.assertEqual(users[0].login, "jacquev6")

    def testGetCollaborators_allParameters(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_collaborators(per_page=3)
        self.assertEqual(users[0].login, "jacquev6")

    def testAddRemoveCollaborators(self):
        repo = self.g.get_repo("jacquev6/PyGithub")
        self.assertFalse(repo.has_in_collaborators("Lyloa"))
        repo.add_to_collaborators("Lyloa")
        self.assertTrue(repo.has_in_collaborators("Lyloa"))
        repo.remove_from_collaborators("Lyloa")
        self.assertFalse(repo.has_in_collaborators("Lyloa"))

    def testGetContributors(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_contributors()
        self.assertEqual(len(list(users)), 25)
        self.assertEqual(users[0].login, "jacquev6")
        self.assertEqual(users[0].contributions, 1041)
        self.assertTrue(isinstance(users[0], PyGithub.Blocking.User.User))
        self.assertEqual(users[1].login, "akfish")

    def testGetContributors_allParameters(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_contributors(anon=True, per_page=3)
        self.assertEqual(len(list(users)), 26)
        self.assertEqual(users[17].type, "Anonymous")
        self.assertEqual(users[17].name, "Petteri Muilu")
        self.assertEqual(users[17].contributions, 1)
        self.assertTrue(isinstance(users[17], PyGithub.Blocking.Repository.Repository.AnonymousContributor))

    def testGetContributorsWithAnonExplicitelyFalse(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_contributors(anon=False)
        self.assertEqual(len(list(users)), 25)

    def testUpdatingContributorKeepsContributions(self):
        user = self.g.get_repo("jacquev6/JellyNoSolver").get_contributors(per_page=3)[0]
        self.assertEqual(user.contributions, 117)
        user.update()
        self.assertEqual(user.contributions, 117)

    @Framework.SharesDataWith(testUpdatingContributorKeepsContributions)
    def testLazyCompletionOfContributorKeepsContributions(self):
        user = self.g.get_repo("jacquev6/JellyNoSolver").get_contributors(per_page=3)[0]
        self.assertEqual(user.contributions, 117)
        self.assertEqual(user.name, "Vincent Jacques")
        self.assertEqual(user.contributions, 117)

    def testGetSubscribers(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_subscribers()
        self.assertEqual(users[0].login, "jacquev6")
        self.assertEqual(users[1].login, "equus12")

    def testGetSubscribers_allParameters(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_subscribers(per_page=3)
        self.assertEqual(users[0].login, "jacquev6")
        self.assertEqual(users[1].login, "equus12")

    def testEditNothing(self):
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        repo.edit()

    def testEditName(self):
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        self.assertEqual(repo.name, "JellyNoSolver")
        repo.edit(name="JellyNoSolver2")
        self.assertEqual(repo.name, "JellyNoSolver2")
        repo.edit(name="JellyNoSolver")
        self.assertEqual(repo.name, "JellyNoSolver")
        with self.assertRaises(TypeError):
            repo.edit(name=PyGithub.Blocking.Reset)

    def testEditDescription(self):
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        self.assertEqual(repo.description, "Solver for Jelly no Puzzle")
        repo.edit(description=PyGithub.Blocking.Reset)
        self.assertEqual(repo.description, None)
        repo.edit(description="Solver for Jelly no Puzzle")
        self.assertEqual(repo.description, "Solver for Jelly no Puzzle")

    def testEditHomepage(self):
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        self.assertEqual(repo.homepage, None)
        repo.edit(homepage="http://foo.bar")
        self.assertEqual(repo.homepage, "http://foo.bar")
        repo.edit(homepage=PyGithub.Blocking.Reset)
        self.assertEqual(repo.homepage, None)

    def testEditPrivate(self):
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        self.assertEqual(repo.private, False)
        repo.edit(private=True)
        self.assertEqual(repo.private, True)
        repo.edit(private=False)
        self.assertEqual(repo.private, False)
        with self.assertRaises(TypeError):
            repo.edit(private=PyGithub.Blocking.Reset)

    def testEditHasIssues(self):
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        self.assertEqual(repo.has_issues, False)
        repo.edit(has_issues=True)
        self.assertEqual(repo.has_issues, True)
        repo.edit(has_issues=False)
        self.assertEqual(repo.has_issues, False)
        with self.assertRaises(TypeError):
            repo.edit(has_issues=PyGithub.Blocking.Reset)

    def testEditHasWiki(self):
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        self.assertEqual(repo.has_wiki, False)
        repo.edit(has_wiki=True)
        self.assertEqual(repo.has_wiki, True)
        repo.edit(has_wiki=False)
        self.assertEqual(repo.has_wiki, False)
        with self.assertRaises(TypeError):
            repo.edit(has_wiki=PyGithub.Blocking.Reset)

    def testEditDefaultBranch(self):
        # @todoBeta test with a Branch instance
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        self.assertEqual(repo.default_branch, "master")
        repo.edit(default_branch="develop")
        self.assertEqual(repo.default_branch, "develop")
        repo.edit(default_branch="master")
        self.assertEqual(repo.default_branch, "master")
        with self.assertRaises(TypeError):
            repo.edit(default_branch=PyGithub.Blocking.Reset)

    def testGetForks(self):
        repos = self.g.get_repo("jacquev6/PyGithub").get_forks()
        self.assertEqual(repos[0].owner.login, "Web5design")
        self.assertEqual(repos[1].owner.login, "pelson")

    def testGetForks_allParameters(self):
        repos = self.g.get_repo("jacquev6/PyGithub").get_forks(sort="stargazers", per_page=3)
        self.assertEqual(repos[0].owner.login, "roverdotcom")
        self.assertEqual(repos[0].stargazers_count, 1)
        self.assertEqual(repos[1].owner.login, "pmuilu")
        self.assertEqual(repos[1].stargazers_count, 1)

    def testGetTeamsOfPersonalRepo(self):
        teams = self.g.get_repo("jacquev6/PyGithub").get_teams()
        self.assertEqual(len(list(teams)), 0)

    def testGetTeamsOfOrgRepo(self):
        teams = self.g.get_repo("BeaverSoftware/FatherBeaver").get_teams()
        self.assertEqual(teams[0].name, "Members")

    def testGetTeams_allParameters(self):
        teams = self.g.get_repo("BeaverSoftware/FatherBeaver").get_teams(per_page=1)
        self.assertEqual(teams[0].name, "Members")

    def testGetKeys(self):
        keys = self.g.get_repo("jacquev6/CodingDojos").get_keys()
        self.assertEqual(len(keys), 1)
        self.assertEqual(keys[0].id, 6941367)

    def testGetKey(self):
        key = self.g.get_repo("jacquev6/CodingDojos").get_key(6941367)
        self.assertEqual(key.title, "dojo@dojo")

    def testCreateKey(self):
        key = self.g.get_repo("jacquev6/CodingDojos").create_key("vincent@test", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCkQih2DtSwBzLUtSNYEKULlI5M1qa6vnq42xt9qZpkLav3G9eD/GqJRST+zZMsyfpP62PtiYKXJdLJX2MQIzUgI2PzNy+iMy+ldiTEABYEOCa+BH9+x2R5xXGlmmCPblpamx3kstGtCTa3LSkyIvxbt5vjbXCyThhJaSKyh+42Uedcz7l0y/TODhnkpid/5eiBz6k0VEbFfhM6h71eBdCFpeMJIhGaPTjbKsEjXIK0SRe0v0UQnpXJQkhAINbm+q/2yjt7zwBF74u6tQjRqJK7vQO2k47ZmFMAGeIxS6GheI+JPmwtHkxvfaJjy2lIGX+rt3lkW8xEUxiMTlxeh+0R")
        self.assertEqual(key.id, 7229238)

    def testGetReadme(self):
        readme = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_readme()
        self.assertEqual(readme.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/README.md?ref=master")

    def testGetReadme_allParameters(self):
        # @todoAlpha ref can also be a GitObject
        readme = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_readme(ref="develop")
        self.assertEqual(readme.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/README.md?ref=develop")

    def testGetFileContent(self):
        f = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_file_content("README.md")
        self.assertEqual(f.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/README.md?ref=master")

    def testGetFileContentWithinDirectory(self):
        f = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_file_content("a/foo.md")
        self.assertEqual(f.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/a/foo.md?ref=master")

    def testGetFileContent_allParameters(self):
        f = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_file_content("toto.md", ref="develop")
        self.assertEqual(f.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/toto.md?ref=develop")

    def testGetRootDirContent(self):
        contents = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_dir_content("")
        self.assertEqual(len(contents), 2)
        self.assertIsInstance(contents[0], PyGithub.Blocking.File.File)
        self.assertIsInstance(contents[1], PyGithub.Blocking.Dir.Dir)

    def testDirContent_allParameters(self):
        contents = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_dir_content("a/b", ref="master")
        self.assertEqual(len(contents), 1)
        self.assertIsInstance(contents[0], PyGithub.Blocking.Dir.Dir)
