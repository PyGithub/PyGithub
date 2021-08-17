from . import Framework


class Organization(Framework.TestCase):
    def testIssue2030CreateProject(self):
        super().setUp()
        project = "ultratendency"
        self.user = self.g.get_user("karthik-kadajji-t")
        self.org = self.g.get_organization("testkarthik")
        self.org.create_project(project)
        success = False
        projects = self.org.get_projects()
        for project in projects:
            if project.name == "ultratendency":
                success = True
                break

        self.assertEqual(True, success)
