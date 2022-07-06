import datetime
from unittest import mock

import github

from . import Framework


class Secret(Framework.TestCase):

    def testAttributes(self):
        org = self.g.get_organization("samdevo-test-organization")
        s = org.get_secret("TESTSECRET")
        self.assertEqual(s.name, "TESTSECRET")
        self.assertIsInstance(s.created_at, datetime.datetime)
        self.assertIsInstance(s.updated_at, datetime.datetime)
        self.assertEqual(s.visibility, "selected")
        self.assertIsInstance(s.selected_repositories, list)
        self.assertEqual(s.url, f"{org.url}/actions/secrets/{s.name}")

    def testAddRemoveRepos(self):
        org = self.g.get_organization("samdevo-test-organization")
        s = org.get_secret("TESTSECRET")
        self.assertEqual(s.visibility, "selected")
        for repo in s.selected_repositories.copy():
            s.remove_repo(repo)
        self.assertEqual(len(s.selected_repositories), 0)
        for repo_name in ["repo1", "repo2"]:
            s.add_repo(org.get_repo(repo_name))
        self.assertListEqual(
            sorted([si.name for si in s.selected_repositories]),
            ["repo1", "repo2"]
        )

    def testCreateDelete(self):
        org = self.g.get_organization("samdevo-test-organization")
        s = org.create_secret("NEWSECRET", "value", "all")
        self.assertEqual(s.name, "NEWSECRET")
        self.assertEqual(s.visibility, "all")
        self.assertIn(s, org.get_secrets())
        self.assertEqual(s.selected_repositories, None)
        org.delete_secret("NEWSECRET")
        self.assertNotIn(s, org.get_secrets())
