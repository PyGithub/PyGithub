from . import Framework


class SecretScanningAlert(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_user().get_repo("PyGithub")

    def testAttributes(self):
        alert = self.repo.get_secret_scanning_alerts()[0]

        self.assertEqual(2, alert.number)
        self.assertIn("2020-11-06T18:48:51Z", alert.created_at)
        self.assertIn(
            "https://api.github.com/repos/owner/private-repo/secret-scanning/alerts/2",
            alert.url,
        )
        self.assertIn(
            "https://github.com/owner/private-repo/security/secret-scanning/2",
            alert.html_url,
        )
        self.assertIn(
            "https://api.github.com/repos/owner/private-repo/secret-scanning/alerts/2/locations",
            alert.locations_url,
        )
        self.assertIn("resolved", alert.state)
        self.assertIn("false_positive", alert.resolution)
        self.assertIn("2020-11-07T02:47:13Z", alert.resolved_at)
        self.assertIn("monalisa", alert.resolved_by.login)
        self.assertIn("adafruit_io_key", alert.secret_type)
        self.assertIn("Adafruit IO Key", alert.secret_type_display_name)
        self.assertIn("aio_XXXXXXXXXXXXXXXXXXXXXXXXXXXX", alert.secret)
        self.assertIn("monalisa", alert.push_protection_bypassed_by.login)
        self.assertEqual(True, alert.push_protection_bypassed)
        self.assertIn("2020-11-06T21:48:51Z", alert.push_protection_bypassed_at)
        self.assertIn("Example comment", alert.resolution_comment)
        self.assertIn("2020-11-06T18:48:51Z", alert.updated_at)
