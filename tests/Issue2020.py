from . import Framework


class Organization(Framework.TestCase):
    def testIssue2020UpdateEdit(self):
        super().setUp()
        self.user = self.g.get_user("karthik-kadajji-t")
        self.org = self.g.get_organization("testkarthik")
        self.g.get_organization("testkarthik").edit(twitter_username="twittertest")
        self.g.get_organization("testkarthik").edit(has_organization_projects=True)
        self.g.get_organization("testkarthik").edit(
            default_repository_permission="admin"
        )
        self.g.get_organization("testkarthik").edit(members_can_create_pages=True)
        self.g.get_organization("testkarthik").edit(
            members_can_create_public_pages=False
        )
        self.g.get_organization("testkarthik").edit(
            members_can_create_private_pages=True
        )

        self.twitter_username = self.org.twitter_username
        self.has_organization_projects = self.org.has_organization_projects
        self.default_repository_permission = self.org.default_repository_permission
        self.members_can_create_pages = self.org.members_can_create_pages
        self.members_can_create_public_pages = self.org.members_can_create_public_pages
        self.members_can_create_private_pages = (
            self.org.members_can_create_private_pages
        )
        self.assertEqual(self.twitter_username, "twittertest")
        # self.assertEqual(self.has_organization_projects, True)
        # self.assertEqual(self.default_repository_permission, "admin")
        # self.assertEqual(self.members_can_create_pages, True)
        # self.assertEqual(self.members_can_create_public_pages, False)
        # self.assertEqual(self.members_can_create_private_pages, True)
