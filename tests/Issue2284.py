from unittest import mock

from . import Framework


class Issue2284(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.user = self.g.get_user()
        self.org = self.g.get_organization("smk-org")
        self.repo = self.org.get_repo("demo-repo-1")

    @mock.patch("github.PublicKey.encrypt")
    def testCreateActionsSecret(self, encrypt):
        # encrypt returns a non-deterministic value, we need to mock it so the replay data matches
        encrypt.return_value = "M+5Fm/BqTfB90h3nC7F3BoZuu3nXs+/KtpXwxm9gG211tbRo0F5UiN0OIfYT83CKcx9oKES9Va4E96/b"
        secret = self.org.create_secret("secret_name", "secret-value", visibility="all")
        self.assertIsNotNone(secret)

    @mock.patch("github.PublicKey.encrypt")
    def testCreateDependabotSecret(self, encrypt):
        # encrypt returns a non-deterministic value, we need to mock it so the replay data matches
        encrypt.return_value = "M+5Fm/BqTfB90h3nC7F3BoZuu3nXs+/KtpXwxm9gG211tbRo0F5UiN0OIfYT83CKcx9oKES9Va4E96/b"
        secret = self.org.create_secret("secret_name", "secret-value", secret_type="dependabot", visibility="all")
        self.assertIsNotNone(secret)

    @mock.patch("github.PublicKey.encrypt")
    def testCreateRepoActionsSecret(self, encrypt):
        # encrypt returns a non-deterministic value, we need to mock it so the replay data matches
        encrypt.return_value = "M+5Fm/BqTfB90h3nC7F3BoZuu3nXs+/KtpXwxm9gG211tbRo0F5UiN0OIfYT83CKcx9oKES9Va4E96/b"
        secret = self.repo.create_secret("secret_name", "secret-value", "actions")
        self.assertIsNotNone(secret)

    @mock.patch("github.PublicKey.encrypt")
    def testCreateRepoDependabotSecret(self, encrypt):
        # encrypt returns a non-deterministic value, we need to mock it so the replay data matches
        encrypt.return_value = "M+5Fm/BqTfB90h3nC7F3BoZuu3nXs+/KtpXwxm9gG211tbRo0F5UiN0OIfYT83CKcx9oKES9Va4E96/b"
        secret = self.repo.create_secret("secret_name", "secret-value", "dependabot")
        self.assertIsNotNone(secret)
