import github.DependabotAlert

from . import Framework


class DependabotAlert(Framework.TestCase):
    alert: github.DependabotAlert.DependabotAlert

    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("coopernetes/PyGithub")
        self.alert = self.repo.get_dependabot_alert(1)

    def testAttributes(self):
        self.assertEqual(self.alert.number, 1)
        self.assertEqual(self.alert.state, "open")
        self.assertEqual(self.alert.dependency["package"]["ecosystem"], "pip")
