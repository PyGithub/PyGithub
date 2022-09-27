#!/usr/bin/env python3

from . import Framework


class Artifact(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.artifact = (
            self.g.get_repo("github/vscode-codeql")
            .get_workflow_run(160995070)
            .get_artifacts()[0]
        )

    def testAttributes(self):
        self.assertEqual(self.artifact.name, "vscode-codeql-extension")

        self.assertTrue(self.artifact.expired)
        self.assertEqual(
            repr(self.artifact), 'Artifact(name="vscode-codeql-extension", id=10495898)'
        )
