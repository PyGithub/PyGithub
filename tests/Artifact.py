#!/usr/bin/env python3

from . import Framework


class Artifact(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("github/vscode-codeql")

    def testGetArtifactsFromWorkflow(self):
        artifact = self.repo.get_workflow_run(160995070).get_artifacts()[0]

        self.assertEqual(artifact.name, "vscode-codeql-extension")
        self.assertTrue(artifact.expired)
        self.assertEqual(
            repr(artifact), 'Artifact(name="vscode-codeql-extension", id=10495898)'
        )

    def testGetSingleArtifactFromRepo(self):
        artifact = self.repo.get_artifact(378970214)

        self.assertEqual(artifact.name, "vscode-codeql-extension")
        self.assertFalse(artifact.expired)
        self.assertEqual(
            repr(artifact), 'Artifact(name="vscode-codeql-extension", id=378970214)'
        )

    def testGetArtifactsFromRepo(self):
        artifact_id = 378970214
        artifacts = self.repo.get_artifacts()
        for item in artifacts:
            if item.id == artifact_id:
                artifact = item
                break
        else:
            assert False, f"No artifact {artifact_id} is found"

        self.assertEqual(
            repr(artifact),
            f'Artifact(name="vscode-codeql-extension", id={artifact_id})',
        )
