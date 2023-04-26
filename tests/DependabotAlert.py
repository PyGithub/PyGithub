from . import Framework


class DependabotAlert(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_user().get_repo("PyGithub")

    def testAttributes(self):
        alert = self.repo.get_dependabot_alerts()[0]

        self.assertIn("2022-06-15T07:43:03Z", alert.created_at)
        self.assertIn("pip", alert.dependency.package.ecosystem)
        self.assertIn("django", alert.dependency.package.name)
        self.assertIn("path/to/requirements.txt", alert.dependency.manifest_path)
        self.assertIn("pip", alert.security_vulnerability.package.ecosystem)
        self.assertIn("django", alert.security_vulnerability.package.name)
        self.assertIn("high", alert.security_vulnerability.severity)
        self.assertIn(
            ">= 2.0.0, < 2.0.2", alert.security_vulnerability.vulnerable_version_range
        )
        self.assertIn(
            "2.0.2", alert.security_vulnerability.first_patched_version.identifier
        )
        self.assertIn("2022-08-23T14:29:47Z", alert.dismissed_at)
        self.assertIn(
            "This alert is accurate but we use a sanitizer.", alert.dismissed_comment
        )
        self.assertIn("tolerable_risk", alert.dismissed_reason)
        self.assertEqual(None, alert.fixed_at)
        self.assertIn(
            "https://github.com/octocat/hello-world/security/dependabot/2",
            alert.html_url,
        )
        self.assertEqual(2, alert.number)
        self.assertIn("dismissed", alert.state)
        self.assertIn("2022-08-23T14:29:47Z", alert.updated_at)
        self.assertIn(
            "https://api.github.com/repos/octocat/hello-world/dependabot/alerts/2",
            alert.url,
        )
        self.assertIn("octocat", alert.dismissed_by.login)
        self.assertEqual(None, alert.auto_dismissed_at)
        self.assertIn("high", alert.security_vulnerability.severity)
