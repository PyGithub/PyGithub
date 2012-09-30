# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import Framework

import github
import datetime


class Repository(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.repo = self.g.get_user().get_repo("PyGithub")

    def testAttributes(self):
        self.assertEqual(self.repo.clone_url, "https://github.com/jacquev6/PyGithub.git")
        self.assertEqual(self.repo.created_at, datetime.datetime(2012, 2, 25, 12, 53, 47))
        self.assertEqual(self.repo.description, "Python library implementing the full Github API v3")
        self.assertEqual(self.repo.fork, False)
        self.assertEqual(self.repo.forks, 3)
        self.assertEqual(self.repo.full_name, "jacquev6/PyGithub")
        self.assertEqual(self.repo.git_url, "git://github.com/jacquev6/PyGithub.git")
        self.assertEqual(self.repo.has_downloads, True)
        self.assertEqual(self.repo.has_issues, True)
        self.assertEqual(self.repo.has_wiki, False)
        self.assertEqual(self.repo.homepage, "http://vincent-jacques.net/PyGithub")
        self.assertEqual(self.repo.html_url, "https://github.com/jacquev6/PyGithub")
        self.assertEqual(self.repo.id, 3544490)
        self.assertEqual(self.repo.language, "Python")
        self.assertEqual(self.repo.master_branch, None)
        self.assertEqual(self.repo.name, "PyGithub")
        self.assertEqual(self.repo.open_issues, 16)
        self.assertEqual(self.repo.organization, None)
        self.assertEqual(self.repo.owner.login, "jacquev6")
        self.assertEqual(self.repo.parent, None)
        self.assertEqual(self.repo.permissions.admin, True)
        self.assertEqual(self.repo.permissions.pull, True)
        self.assertEqual(self.repo.permissions.push, True)
        self.assertEqual(self.repo.private, False)
        self.assertEqual(self.repo.pushed_at, datetime.datetime(2012, 5, 27, 6, 0, 28))
        self.assertEqual(self.repo.size, 308)
        self.assertEqual(self.repo.source, None)
        self.assertEqual(self.repo.ssh_url, "git@github.com:jacquev6/PyGithub.git")
        self.assertEqual(self.repo.svn_url, "https://github.com/jacquev6/PyGithub")
        self.assertEqual(self.repo.updated_at, datetime.datetime(2012, 5, 27, 6, 55, 28))
        self.assertEqual(self.repo.url, "https://api.github.com/repos/jacquev6/PyGithub")
        self.assertEqual(self.repo.watchers, 15)

    def testEditWithoutArguments(self):
        self.repo.edit("PyGithub")

    def testEditWithAllArguments(self):
        self.repo.edit("PyGithub", "Description edited by PyGithub", "http://vincent-jacques.net/PyGithub", public=True, has_issues=True, has_wiki=False, has_downloads=True)
        self.assertEqual(self.repo.description, "Description edited by PyGithub")
        self.repo.edit("PyGithub", "Python library implementing the full Github API v3")
        self.assertEqual(self.repo.description, "Python library implementing the full Github API v3")

    def testDelete(self):
        repo = self.g.get_user().get_repo("TestPyGithub")
        repo.delete()

    def testGetContributors(self):
        self.assertListKeyEqual(self.repo.get_contributors(), lambda c: (c.login, c.contributions), [("jacquev6", 355)])

    def testCreateMilestone(self):
        milestone = self.repo.create_milestone("Milestone created by PyGithub", state="open", description="Description created by PyGithub", due_on=datetime.date(2012, 6, 15))
        self.assertEqual(milestone.number, 5)

    def testCreateMilestoneWithMinimalArguments(self):
        milestone = self.repo.create_milestone("Milestone also created by PyGithub")
        self.assertEqual(milestone.number, 6)

    def testCreateIssue(self):
        issue = self.repo.create_issue("Issue created by PyGithub")
        self.assertEqual(issue.number, 28)

    def testCreateIssueWithAllArguments(self):
        user = self.g.get_user("jacquev6")
        milestone = self.repo.get_milestone(2)
        question = self.repo.get_label("Question")
        issue = self.repo.create_issue("Issue also created by PyGithub", "Body created by PyGithub", user, milestone, [question])
        self.assertEqual(issue.number, 30)

    def testCreateLabel(self):
        label = self.repo.create_label("Label with silly name % * + created by PyGithub", "00ff00")
        self.assertEqual(label.color, "00ff00")
        self.assertEqual(label.name, "Label with silly name % * + created by PyGithub")
        self.assertEqual(label.url, "https://api.github.com/repos/jacquev6/PyGithub/labels/Label+with+silly+name+%25+%2A+%2B+created+by+PyGithub")

    def testGetLabel(self):
        label = self.repo.get_label("Label with silly name % * + created by PyGithub")
        self.assertEqual(label.color, "00ff00")
        self.assertEqual(label.name, "Label with silly name % * + created by PyGithub")
        self.assertEqual(label.url, "https://api.github.com/repos/jacquev6/PyGithub/labels/Label+with+silly+name+%25+%2A+%2B+created+by+PyGithub")

    def testCreateHookWithMinimalParameters(self):
        hook = self.repo.create_hook("web", {"url": "http://foobar.com"})
        self.assertEqual(hook.id, 257967)

    def testCreateHookWithAllParameters(self):
        hook = self.repo.create_hook("web", {"url": "http://foobar.com"}, ["fork"], False)
        self.assertEqual(hook.active, True)  # WTF
        self.assertEqual(hook.id, 257993)

    def testCreateDownloadWithMinimalArguments(self):
        download = self.repo.create_download("Foobar.txt", 1024)
        self.assertEqual(download.id, 242562)

    def testCreateDownloadWithAllArguments(self):
        download = self.repo.create_download("Foobar.txt", 1024, "Download created by PyGithub", "text/richtext")
        self.assertEqual(download.accesskeyid, "1DWESVTPGHQVTX38V182")
        self.assertEqual(download.acl, "public-read")
        self.assertEqual(download.bucket, "github")
        self.assertEqual(download.content_type, "text/richtext")
        self.assertEqual(download.created_at, datetime.datetime(2012, 5, 22, 19, 11, 49))
        self.assertEqual(download.description, "Download created by PyGithub")
        self.assertEqual(download.download_count, 0)
        self.assertEqual(download.expirationdate, datetime.datetime(2112, 5, 22, 19, 11, 49))
        self.assertEqual(download.html_url, "https://github.com/downloads/jacquev6/PyGithub/Foobar.txt")
        self.assertEqual(download.id, 242556)
        self.assertEqual(download.mime_type, "text/richtext")
        self.assertEqual(download.name, "Foobar.txt")
        self.assertEqual(download.path, "downloads/jacquev6/PyGithub/Foobar.txt")
        self.assertEqual(download.policy, "ewogICAgJ2V4cGlyYXRpb24nOiAnMjExMi0wNS0yMlQxOToxMTo0OS4wMDBaJywKICAgICdjb25kaXRpb25zJzogWwogICAgICAgIHsnYnVja2V0JzogJ2dpdGh1Yid9LAogICAgICAgIHsna2V5JzogJ2Rvd25sb2Fkcy9qYWNxdWV2Ni9QeUdpdGh1Yi9Gb29iYXIudHh0J30sCiAgICAgICAgeydhY2wnOiAncHVibGljLXJlYWQnfSwKICAgICAgICB7J3N1Y2Nlc3NfYWN0aW9uX3N0YXR1cyc6ICcyMDEnfSwKICAgICAgICBbJ3N0YXJ0cy13aXRoJywgJyRGaWxlbmFtZScsICcnXSwKICAgICAgICBbJ3N0YXJ0cy13aXRoJywgJyRDb250ZW50LVR5cGUnLCAnJ10KICAgIF0KfQ==")
        self.assertEqual(download.prefix, "downloads/jacquev6/PyGithub")
        self.assertEqual(download.redirect, False)
        self.assertEqual(download.s3_url, "https://github.s3.amazonaws.com/")
        self.assertEqual(download.signature, "8FCU/4rgT3ohXfE9N6HO7JgbuK4=")
        self.assertEqual(download.size, 1024)
        self.assertEqual(download.url, "https://api.github.com/repos/jacquev6/PyGithub/downloads/242556")

    def testCreateGitRef(self):
        ref = self.repo.create_git_ref("refs/heads/BranchCreatedByPyGithub", "4303c5b90e2216d927155e9609436ccb8984c495")
        self.assertEqual(ref.url, "https://api.github.com/repos/jacquev6/PyGithub/git/refs/heads/BranchCreatedByPyGithub")

    def testCreateGitBlob(self):
        blob = self.repo.create_git_blob("Blob created by PyGithub", "latin1")
        self.assertEqual(blob.sha, "5dd930f591cd5188e9ea7200e308ad355182a1d8")

    def testCreateGitTree(self):
        tree = self.repo.create_git_tree(
            [github.InputGitTreeElement(
                "Foobar.txt",
                "100644",
                "blob",
                content="File created by PyGithub"
            )]
        )
        self.assertEqual(tree.sha, "41cf8c178c636a018d537cb20daae09391efd70b")

    def testCreateGitTreeWithBaseTree(self):
        base_tree = self.repo.get_git_tree("41cf8c178c636a018d537cb20daae09391efd70b")
        tree = self.repo.create_git_tree(
            [github.InputGitTreeElement(
                "Barbaz.txt",
                "100644",
                "blob",
                content="File also created by PyGithub"
            )],
            base_tree
        )
        self.assertEqual(tree.sha, "107139a922f33bab6fbeb9f9eb8787e7f19e0528")

    def testCreateGitTreeWithSha(self):
        tree = self.repo.create_git_tree(
            [github.InputGitTreeElement(
                "Barbaz.txt",
                "100644",
                "blob",
                sha="5dd930f591cd5188e9ea7200e308ad355182a1d8"
            )]
        )
        self.assertEqual(tree.sha, "fae707821159639589bf94f3fb0a7154ec5d441b")

    def testCreateGitCommit(self):
        tree = self.repo.get_git_tree("107139a922f33bab6fbeb9f9eb8787e7f19e0528")
        commit = self.repo.create_git_commit("Commit created by PyGithub", tree, [])
        self.assertEqual(commit.sha, "0b820628236ab8bab3890860fc414fa757ca15f4")

    def testCreateGitCommitWithParents(self):
        parents = [
            self.repo.get_git_commit("7248e66831d4ffe09ef1f30a1df59ec0a9331ece"),
            self.repo.get_git_commit("12d427464f8d91c8e981043a86ba8a2a9e7319ea"),
        ]
        tree = self.repo.get_git_tree("fae707821159639589bf94f3fb0a7154ec5d441b")
        commit = self.repo.create_git_commit("Commit created by PyGithub", tree, parents)
        self.assertEqual(commit.sha, "6adf9ea25ff8a8f2a42bcb1c09e42526339037cd")

    def testCreateGitCommitWithAllArguments(self):
        tree = self.repo.get_git_tree("107139a922f33bab6fbeb9f9eb8787e7f19e0528")
        commit = self.repo.create_git_commit("Commit created by PyGithub", tree, [], github.InputGitAuthor("John Doe", "j.doe@vincent-jacques.net", "2008-07-09T16:13:30+12:00"), github.InputGitAuthor("John Doe", "j.doe@vincent-jacques.net", "2008-07-09T16:13:30+12:00"))
        self.assertEqual(commit.sha, "526946197ae9da59c6507cacd13ad6f1cfb686ea")

    def testCreateGitTag(self):
        tag = self.repo.create_git_tag("TaggedByPyGithub", "Tag created by PyGithub", "0b820628236ab8bab3890860fc414fa757ca15f4", "commit")
        self.assertEqual(tag.sha, "5ba561eaa2b7ca9015662510157b15d8f3b0232a")

    def testCreateGitTagWithAllArguments(self):
        tag = self.repo.create_git_tag("TaggedByPyGithub2", "Tag also created by PyGithub", "526946197ae9da59c6507cacd13ad6f1cfb686ea", "commit", github.InputGitAuthor("John Doe", "j.doe@vincent-jacques.net", "2008-07-09T16:13:30+12:00"))
        self.assertEqual(tag.sha, "f0e99a8335fbc84c53366c4a681118468f266625")

    def testCreateKey(self):
        key = self.repo.create_key("Key added through PyGithub", "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA2Mm0RjTNAYFfSCtUpO54usdseroUSIYg5KX4JoseTpqyiB/hqewjYLAdUq/tNIQzrkoEJWSyZrQt0ma7/YCyMYuNGd3DU6q6ZAyBeY3E9RyCiKjO3aTL2VKQGFvBVVmGdxGVSCITRphAcsKc/PF35/fg9XP9S0anMXcEFtdfMHz41SSw+XtE+Vc+6cX9FuI5qUfLGbkv8L1v3g4uw9VXlzq4GfTA+1S7D6mcoGHopAIXFlVr+2RfDKdSURMcB22z41fljO1MW4+zUS/4FyUTpL991es5fcwKXYoiE+x06VJeJJ1Krwx+DZj45uweV6cHXt2JwJEI9fWB6WyBlDejWw== vincent@IDEE")
        self.assertEqual(key.id, 2626761)

    def testCollaborators(self):
        lyloa = self.g.get_user("Lyloa")
        self.assertFalse(self.repo.has_in_collaborators(lyloa))
        self.repo.add_to_collaborators(lyloa)
        self.assertTrue(self.repo.has_in_collaborators(lyloa))
        self.assertListKeyEqual(self.repo.get_collaborators(), lambda u: u.login, ["jacquev6", "Lyloa"])
        self.repo.remove_from_collaborators(lyloa)
        self.assertFalse(self.repo.has_in_collaborators(lyloa))

    def testCompare(self):
        comparison = self.repo.compare("v0.6", "v0.7")
        self.assertEqual(comparison.status, "ahead")
        self.assertEqual(comparison.ahead_by, 4)
        self.assertEqual(comparison.behind_by, 0)
        self.assertEqual(comparison.diff_url, "https://github.com/jacquev6/PyGithub/compare/v0.6...v0.7.diff")
        self.assertEqual(comparison.html_url, "https://github.com/jacquev6/PyGithub/compare/v0.6...v0.7")
        self.assertEqual(comparison.url, "https://api.github.com/repos/jacquev6/PyGithub/compare/v0.6...v0.7")
        self.assertEqual(comparison.patch_url, "https://github.com/jacquev6/PyGithub/compare/v0.6...v0.7.patch")
        self.assertEqual(comparison.permalink_url, "https://github.com/jacquev6/PyGithub/compare/jacquev6:4303c5b...jacquev6:ecda065")
        self.assertEqual(comparison.total_commits, 4)
        self.assertListKeyEqual(comparison.files, lambda f: f.filename, ["ReferenceOfClasses.md", "github/Github.py", "github/Requester.py", "setup.py"])
        self.assertEqual(comparison.base_commit.sha, "4303c5b90e2216d927155e9609436ccb8984c495")
        self.assertListKeyEqual(comparison.commits, lambda c: c.sha, ["5bb654d26dd014d36794acd1e6ecf3736f12aad7", "cb0313157bf904f2d364377d35d9397b269547a5", "0cec0d25e606c023a62a4fc7cdc815309ebf6d16", "ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7"])

    def testGetComments(self):
        self.assertListKeyEqual(
            self.repo.get_comments(),
            lambda c: c.body,
            [
                "probably a noob question: does this completion refer to autocompletion in IDE's/editors? \nI have observed that this is pretty erratic sometimes. I'm using PyDev+Eclipse.\nFor example, in the tutorial from the readme, `g.get_u` gets autocompleted correctly, but `g.get_user().get_r` (or any method or attribute applicable to NamedUsers/AuthenticatedUser, really) does not show autocompletion to `g.get_user().get_repo()`. Is that by design? It makes exploring the library/API a bit cumbersome. ",
                "No, it has nothing to do with auto-completion in IDEs :D\n\nGithub API v3 sends only the main part of objects in reply to some requests. So, if the user wants an attribute that has not been received yet, I have to do another request to complete the object.\n\nYet, in version 1.0 (see the milesone), my library will be much more readable for IDEs and their auto-completion mechanisms, because I am giving up the meta-description that I used until 0.6, and I'm now generating much more traditional code, that you will be able to explore as if it was written manually.\n\nIf you want to take the time to open an issue about auto-completion in IDEs, I'll deal with it in milestone 1.0.\n\nThanks !",
                "Ah, thanks for the clarification. :blush:\n\nI made issue #27 for the autocompletion. I already suspected something like this meta-description magic, since I tried to read some of the code and it was pretty arcane. I attributed that to my pythonic noobness, though. Thank you. ",
                "Comment created by PyGithub"
            ]
        )

    def testGetCommits(self):
        self.assertListKeyBegin(self.repo.get_commits(), lambda c: c.sha, [u'ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7', u'0cec0d25e606c023a62a4fc7cdc815309ebf6d16', u'cb0313157bf904f2d364377d35d9397b269547a5', u'5bb654d26dd014d36794acd1e6ecf3736f12aad7', u'4303c5b90e2216d927155e9609436ccb8984c495', u'2a7e80e6421c5d4d201d60619068dea6bae612cb', u'0af24499a98e85f8ab2191898e8b809e5cebd4c5', u'e5ae923a68a9ae295ce5aa20b1227253de60e918', u'2f64b625f7e2afc9bef61d0decb459e2ef65c550', u'590798d349cba7de6e83b43aa5d4f8b0a38e685d', u'e7dca9143a23b8e2045a4a910a4a329007b10086', u'ab3f9b422cb3043d35cf6002fc9c042f8ead8c2a', u'632d8b63c32a2b79e87eb3b93e1ad228724de4bd', u'64c6a1e975e61b9c1449bed016cd19f33ee4b1c5', u'99963536fc81db3b9986c761b9dd08de22089aa2', u'8d57522bbd15d1fb6b616fae795cd8721deb1c4d', u'1140a91f3e45d09bc15463724f178a7ebf8e3149', u'936f4a97f1a86392637ec002bbf89ff036a5062d', u'e10470481795506e2c232720e2a9ecf588c8b567', u'e456549e5265406f8090ae5145255c8ca9ea5e4e', u'a91131be42eb328ae030f584af500f56aa08424b', u'2469c6e1aeb7919126a8271f6980b555b167e8b0', u'a655d0424135befd3a0d53f3f7eff2d1c754854f', u'ce62e91268aa34dad0ba0dbee4769933e3a71e50', u'1c88ee221b7f995855a1fdfac7d0ba19db918739', u'bd1a5dff3c547c634b2d89f5847218820e343883', u'b226b5b4e2f44107dde674e7a5d3e88d4e3518df', u'25dbd4053e982402c7d92139f167dbe46008c932', u'a0cc821c1beada4aa9ca0d5218664c5372720936', u'c1440bdf20bfeb62684c6d1779448719dce9d2df', u'1095d304b7fab3818dcb4c42093c8c56d3ac05e4', u'bd39726f7cf86ea7ffb33b5718241fdab5fc8f53', u'1d2b27824d20612066d84be42d6691c66bb18ef4', u'6af2bfd0d46bc0eeb8c37b85c7b3003e0e4ae297', u'a475d685d8ae709095d09094ea0962ac182d33f0', u'a85de99ea5b5e7b38bd68e076d09c49207b8687e', u'd24cf209ddd1758188c5f35344f76df818d09a46', u'0909fec395bb1f97e2580d6a029cfc64b352aff9', u'6e421e9e85e12008758870bc046bc2c6120af72a', u'32ed0ebc377efbed5b482b3d49ff54bf1715d55a', u'8213df1d744f251aa8e52229643a9f6ce352f3c0', u'69cc298fd159f19eb204dd09f17d31dc4abc3d41', u'85eef756353e13efcb24c726320cd2617c2a7bd8', u'50ac55b25ceba555b84709839f80447552450697', u'767d75a580279e457f9bc52bc308a17ff8ea0509', u'75e72ffa3066693291f7da03070666e8f885097a', u'504047e218e6b34a3828ccc408431634f17b9504', u'960db1d5c9853e9f5fbbc9237c2c166ceef1f080', u'877dde23e140bbf038f9a2d8f0f07b4e3a965c61', u'1c95ddfa09ec0aa1f07ee9ad50a77be1dd74b55e', u'99564c1cab139d1e4678f5f83f60d26f1210db7e', u'231926207709ceaa61e87b64e34e17d85adecd9c', u'fb722625dddb9a32f75190723f7da12683b7c4b2', u'cab9d71603e127bdd1f600a759dccea1781fa1ab', u'e648e5aeb5edc1fbf83e9d37d2a3cb57c005019a', u'4a5cf98e7f959f1b5d9af484760c25cd27d9180d', u'5d1add448e0b0b1dadb8c6094a9e5e19b255f67e', u'0d9fc99a4b5d1ec6473c9c81c888917c132ffa65', u'b56aa09011378b014221f86dffb8304957a9e6bd', u'3e8169c0a98ce1e2c6a32ae1256ae0f735065df5', u'378558f6cac6183b4a7100c0ce5eaad1cfff6717', u'58b4396aa0e7cb72911b75cb035798143a06e0ee', u'a3be28756101370fbc689eec3a7825c4c385a6c9', u'3d6bd49ce229243fea4bb46a937622d0ec7d4d1c', u'58cb0dbdef9765e0e913c726f923a47315aaf80e', u'7b7ac20c6fa27f72a24483c73ab1bf4deffc89f0', u'97f308e67383368a2d15788cac28e126c8528bb2', u'fc33a6de4f0e08d7ff2de05935517ec3932d212e', u'cc6d0fc044eadf2e6fde5da699f61654c1e691f3', u'2dd71f3777b87f2ba61cb20d2c67f10401e3eb2c', u'366ca58ca004b9129f9d435db8204ce0f5bc57c3', u'0d3b3ffd1e5c143af8725fdee808101f626f683d', u'157f9c13275738b6b39b8d7a874f5f0aee47cb18'])

    def testGetCommitsWithArguments(self):
        self.assertListKeyEqual(self.repo.get_commits("topic/RewriteWithGeneratedCode", "codegen/GenerateCode.py"), lambda c: c.sha, ["de386d5dc9cf103c90c4128eeca0e6abdd382065", "5b44982f6111bff2454243869df2e1c3086ccbba", "d6835ff949141957a733c8ddfa147026515ae493", "075d3d961d4614a2a0835d5583248adfc0687a7d", "8956796e7f462a49f499eac52fab901cdb59abdb", "283da5e7de6a4a3b6aaae7045909d70b643ad380", "d631e83b7901b0a0b6061b361130700a79505319"])

    def testGetDownloads(self):
        self.assertListKeyEqual(self.repo.get_downloads(), lambda d: d.id, [245143])

    def testGetEvents(self):
        self.assertListKeyBegin(self.repo.get_events(), lambda e: e.type, ["DownloadEvent", "DownloadEvent", "PushEvent", "IssuesEvent", "MemberEvent", "MemberEvent"])

    def testGetForks(self):
        self.assertListKeyEqual(self.repo.get_forks(), lambda r: r.owner.login, ["abersager"])

    def testGetGitRefs(self):
        self.assertListKeyEqual(self.repo.get_git_refs(), lambda r: r.ref, ["refs/heads/develop", "refs/heads/master", "refs/heads/topic/DependencyGraph", "refs/heads/topic/RewriteWithGeneratedCode", "refs/tags/v0.1", "refs/tags/v0.2", "refs/tags/v0.3", "refs/tags/v0.4", "refs/tags/v0.5", "refs/tags/v0.6", "refs/tags/v0.7"])

    def testGetGitTreeWithRecursive(self):
        tree = self.repo.get_git_tree("f492784d8ca837779650d1fb406a1a3587a764ad", True)
        self.assertEqual(len(tree.tree), 90)
        self.assertEqual(tree.tree[50].path, "github/GithubObjects/Gist.py")

    def testGetHooks(self):
        self.assertListKeyEqual(self.repo.get_hooks(), lambda h: h.id, [257993])

    def testGetIssues(self):
        self.assertListKeyEqual(self.repo.get_issues(), lambda i: i.id, [4769659, 4639931, 4452000, 4356743, 3716033, 3715946, 3643837, 3628022, 3624595, 3624570, 3624561, 3624556, 3619973, 3527266, 3527245, 3527231])

    def testGetIssuesWithArguments(self):
        milestone = self.repo.get_milestone(3)
        user = self.g.get_user("jacquev6")
        otherUser = self.g.get_user("Lyloa")
        bug = self.repo.get_label("Bug")
        self.assertListKeyEqual(self.repo.get_issues(milestone, "closed"), lambda i: i.id, [3624472, 3620132, 3619658, 3561926])
        self.assertListKeyEqual(self.repo.get_issues(labels=[bug]), lambda i: i.id, [4780155])
        self.assertListKeyEqual(self.repo.get_issues(assignee=user, sort="comments", direction="asc"), lambda i: i.id, [4793106, 3527231, 3527266, 3624556, 4793216, 3619973, 3624595, 4452000, 3643837, 3628022, 3527245, 4793162, 4356743, 4780155])
        self.assertListKeyEqual(self.repo.get_issues(since=datetime.datetime(2012, 5, 28, 23, 0, 0)), lambda i: i.id, [4793216, 4793162, 4793106, 3624556, 3619973, 3527266])
        self.assertListKeyEqual(self.repo.get_issues(mentioned=otherUser), lambda i: i.id, [4793162])

    def testGetIssuesWithWildcards(self):
        self.assertListKeyEqual(self.repo.get_issues(milestone="*"), lambda i: i.id, [4809786, 4793216, 4789817, 4452000, 3628022, 3624595, 3619973, 3527231])
        self.assertListKeyEqual(self.repo.get_issues(milestone="none"), lambda i: i.id, [4823331, 4809803, 4809778, 4793106, 3643837, 3527245])
        self.assertListKeyEqual(self.repo.get_issues(assignee="*"), lambda i: i.id, [4823331, 4809803, 4809786, 4809778, 4793216, 4793106, 4789817, 4452000, 3643837, 3628022, 3624595, 3527245, 3527231])
        self.assertListKeyEqual(self.repo.get_issues(assignee="none"), lambda i: i.id, [3619973])

    def testGetKeys(self):
        self.assertListKeyEqual(self.repo.get_keys(), lambda k: k.title, ["Key added through PyGithub"])

    def testGetLabels(self):
        self.assertListKeyEqual(self.repo.get_labels(), lambda l: l.name, ["Refactoring", "Public interface", "Functionalities", "Project management", "Bug", "Question"])

    def testGetLanguages(self):
        self.assertEqual(self.repo.get_languages(), {"Python": 127266, "Shell": 673})

    def testGetMilestones(self):
        self.assertListKeyEqual(self.repo.get_milestones(), lambda m: m.id, [93547])

    def testGetMilestonesWithArguments(self):
        self.assertListKeyEqual(self.repo.get_milestones("closed", "due_date", "asc"), lambda m: m.id, [93546, 95354, 108652, 124045])

    def testGetIssuesEvents(self):
        self.assertListKeyBegin(self.repo.get_issues_events(), lambda e: e.event, ["assigned", "subscribed", "closed", "assigned", "closed"])

    def testGetNetworkEvents(self):
        self.assertListKeyBegin(self.repo.get_network_events(), lambda e: e.type, ["DownloadEvent", "DownloadEvent", "PushEvent", "IssuesEvent", "MemberEvent"])

    def testGetTeams(self):
        repo = self.g.get_organization("BeaverSoftware").get_repo("FatherBeaver")
        self.assertListKeyEqual(repo.get_teams(), lambda t: t.name, ["Members"])

    def testGetWatchers(self):
        self.assertListKeyEqual(self.repo.get_watchers(), lambda u: u.login, ["Stals", "att14", "jardon-u", "huxley", "mikofski", "L42y", "fanzeyi", "abersager", "waylan", "adericbourg", "tallforasmurf", "pvicente", "roskakori", "michaelpedersen", "BeaverSoftware"])

    def testGetStargazers(self):
        self.assertListKeyEqual(self.repo.get_stargazers(), lambda u: u.login, ["Stals", "att14", "jardon-u", "huxley", "mikofski", "L42y", "fanzeyi", "abersager", "waylan", "adericbourg", "tallforasmurf", "pvicente", "roskakori", "michaelpedersen", "stefanfoulis", "equus12", "JuRogn", "joshmoore", "jsilter", "dasapich", "ritratt", "hcilab", "vxnick", "pmuilu", "herlo", "malexw", "ahmetvurgun", "PengGu", "cosmin", "Swop", "kennethreitz", "bryandyck", "jason2506", "zsiciarz", "waawal", "gregorynicholas", "sente", "richmiller55", "thouis", "mazubieta", "michaelhood", "engie", "jtriley", "oangeor", "coryking", "noddi", "alejo8591", "omab", "Carreau", "bilderbuchi", "schwa", "rlerallut", "PengHub", "zoek1", "xobb1t", "notgary", "hattya", "ZebtinRis", "aaronhall", "youngsterxyf", "ailling", "gregwjacobs", "n0rmrx", "awylie", "firstthumb", "joshbrand", "berndca"])

    def testGetSubscribers(self):
        self.assertListKeyEqual(self.repo.get_subscribers(), lambda u: u.login, ["jacquev6", "equus12", "bilderbuchi", "hcilab", "hattya", "firstthumb", "gregwjacobs", "sagarsane", "liang456", "berndca", "Lyloa"])

    def testCreatePull(self):
        pull = self.repo.create_pull("Pull request created by PyGithub", "Body of the pull request", "topic/RewriteWithGeneratedCode", "BeaverSoftware:master")
        self.assertEqual(pull.id, 1436215)

    def testCreatePullFromIssue(self):
        issue = self.repo.get_issue(32)
        pull = self.repo.create_pull(issue, "topic/RewriteWithGeneratedCode", "BeaverSoftware:master")
        self.assertEqual(pull.id, 1436310)

    def testGetPulls(self):
        self.assertListKeyEqual(self.repo.get_pulls(), lambda p: p.id, [1436310])

    def testGetPullsWithArguments(self):
        self.assertListKeyEqual(self.repo.get_pulls("closed"), lambda p: p.id, [1448168, 1436310, 1436215])

    def testLegacySearchIssues(self):
        issues = self.repo.legacy_search_issues("open", "search")
        self.assertListKeyEqual(issues, lambda i: i.title, ["Support new Search API"])

        # Attributes retrieved from legacy API without lazy completion call
        self.assertEqual(issues[0].number, 49)
        self.assertEqual(issues[0].created_at, datetime.datetime(2012, 6, 21, 12, 27, 38))
        self.assertEqual(issues[0].comments, 4)
        self.assertEqual(issues[0].body[: 20], "New API ported from ")
        self.assertEqual(issues[0].title, "Support new Search API")
        self.assertEqual(issues[0].updated_at, datetime.datetime(2012, 6, 28, 21, 13, 25))
        self.assertEqual(issues[0].user.login, "kukuts")
        self.assertEqual(issues[0].user.url, "/users/kukuts")
        self.assertListKeyEqual(issues[0].labels, lambda l: l.name, ["Functionalities", "RequestedByUser"])
        self.assertEqual(issues[0].state, "open")

    def testAssignees(self):
        lyloa = self.g.get_user("Lyloa")
        jacquev6 = self.g.get_user("jacquev6")
        self.assertTrue(self.repo.has_in_assignees(jacquev6))
        self.assertFalse(self.repo.has_in_assignees(lyloa))
        self.repo.add_to_collaborators(lyloa)
        self.assertTrue(self.repo.has_in_assignees(lyloa))
        self.assertListKeyEqual(self.repo.get_assignees(), lambda u: u.login, ["jacquev6", "Lyloa"])
        self.repo.remove_from_collaborators(lyloa)
        self.assertFalse(self.repo.has_in_assignees(lyloa))

    def testGetContents(self):
        self.assertEqual(len(self.repo.get_readme().content), 10212)
        self.assertEqual(len(self.repo.get_contents("doc/ReferenceOfClasses.md").content), 38121)

    def testGetArchiveLink(self):
        self.assertEqual(self.repo.get_archive_link("tarball"), "https://nodeload.github.com/jacquev6/PyGithub/tarball/master")
        self.assertEqual(self.repo.get_archive_link("zipball"), "https://nodeload.github.com/jacquev6/PyGithub/zipball/master")
        self.assertEqual(self.repo.get_archive_link("zipball", "master"), "https://nodeload.github.com/jacquev6/PyGithub/zipball/master")
        self.assertEqual(self.repo.get_archive_link("tarball", "develop"), "https://nodeload.github.com/jacquev6/PyGithub/tarball/develop")

    def testGetBranch(self):
        branch = self.repo.get_branch("develop")
        self.assertEqual(branch.commit.sha, "03058a36164d2a7d946db205f25538434fa27d94")

    def testMergeWithoutMessage(self):
        commit = self.repo.merge("branchForBase", "branchForHead")
        self.assertEqual(commit.commit.message, "Merge branchForHead into branchForBase")

    def testMergeWithMessage(self):
        commit = self.repo.merge("branchForBase", "branchForHead", "Commit message created by PyGithub")
        self.assertEqual(commit.commit.message, "Commit message created by PyGithub")

    def testMergeWithNothingToDo(self):
        commit = self.repo.merge("branchForBase", "branchForHead", "Commit message created by PyGithub")
        self.assertEqual(commit, None)

    def testMergeWithConflict(self):
        try:
            commit = self.repo.merge("branchForBase", "branchForHead")
            self.fail("Should have raised")
        except github.GithubException, exception:
            self.assertEqual(exception.status, 409)
            self.assertEqual(exception.data, {"message": "Merge conflict"})
