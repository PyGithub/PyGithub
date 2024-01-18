from unittest import mock

from . import Framework


class Issue2284(Framework.TestCase):
    def setUp(self):
        self.tokenAuthMode = True
        super().setUp()
        self.user = self.g.get_user()
        self.org = self.g.get_organization("pygithubtest")
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

    def testRepoGetSecretAssertion(self):
        try:
            self.repo.get_secret(secret_name="splat", secret_type="supersecret")
        except AssertionError:
            assert True

    def testOrgGetSecretAssertion(self):
        try:
            self.org.get_secret(secret_name="splat", secret_type="supersecret")
        except AssertionError:
            assert True

    @mock.patch("github.PublicKey.encrypt")
    def testCreateDependabotSecretSelected(self, encrypt):
        repos = [self.org.get_repo("demo-repo-1"), self.org.get_repo("demo-repo-2")]
        # encrypt returns a non-deterministic value, we need to mock it so the replay data matches
        encrypt.return_value = "M+5Fm/BqTfB90h3nC7F3BoZuu3nXs+/KtpXwxm9gG211tbRo0F5UiN0OIfYT83CKcx9oKES9Va4E96/b"
        secret = self.org.create_secret(
            secret_name="secret_dep_name",
            unencrypted_value="secret-value",
            visibility="selected",
            secret_type="dependabot",
            selected_repositories=repos,
        )

        self.assertIsNotNone(secret)
        self.assertEqual(secret.visibility, "selected")
        self.assertEqual(list(secret.selected_repositories), repos)

    @mock.patch("github.PublicKey.encrypt")
    def testOrgSecretEdit(self, encrypt):
        repos = [self.org.get_repo("demo-repo-1"), self.org.get_repo("demo-repo-2")]
        # encrypt returns a non-deterministic value, we need to mock it so the replay data matches
        encrypt.return_value = "M+5Fm/BqTfB90h3nC7F3BoZuu3nXs+/KtpXwxm9gG211tbRo0F5UiN0OIfYT83CKcx9oKES9Va4E96/b"
        secret = self.org.create_secret(
            secret_name="secret_act_name",
            unencrypted_value="secret-value",
            visibility="selected",
            secret_type="actions",
            selected_repositories=repos,
        )

        try:
            secret.edit(value="newvalue", secret_type="supersecret")
        except AssertionError:
            assert True
