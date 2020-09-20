import github

from . import Framework


class OrganizationTeamMgmt(Framework.TestCase):

    teamName = "MyTeam"

    def setUp(self):
        super().setUp()
        self.org = self.g.get_organization("ThoughtCamera")
        self.org.create_team(name=self.teamName, privacy="closed")
        self.MyTeam = self.org.get_team_by_slug(self.teamName)
        self.assertEqual(self.MyTeam.name, self.teamName)

    def test_delete_team_by_id(self):
        self.org.remove_team(team_id=self.MyTeam.id)
        with self.assertRaises(github.UnknownObjectException):
            self.org.get_team(id=self.MyTeam.id)

    def test_delete_team_by_slug(self):
        self.assertIsNone(self.org.remove_team_by_slug(team_slug=self.MyTeam.slug))
        with self.assertRaises(github.UnknownObjectException):
            self.org.get_team_by_slug(slug=self.MyTeam.slug)

    def test_team_parent(self):
        self.org.create_team(name="ChildTeam", parent_team_id=self.MyTeam.id)
        self.assertTrue(self.org.get_team_by_slug("ChildTeam"))
        self.assertIsNone(self.org.remove_team_by_slug(team_slug=self.MyTeam.slug))
