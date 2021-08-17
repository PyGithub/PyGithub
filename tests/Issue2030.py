from . import Framework


class Organization(Framework.TestCase):
    def testIssue2030CreateProject(self):
        super().setUp()
        project = "ultratendency"
        self.user = self.g.get_user("karthik-kadajji-t")
        self.org = self.g.get_organization("testkarthik")
        self.org.create_project(project)
        project = self.org.get_projects()[0].name

        self.assertEqual("ultratendency", project)
