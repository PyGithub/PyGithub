#!/usr/bin/env python3

import github

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

    def testGetNonexistentArtifact(self):
        artifact_id = 396724437
        repo_name = "lexa/PyGithub"
        repo = self.g.get_repo(repo_name)
        with self.assertRaises(github.GithubException):
            repo.get_artifact(artifact_id)

    def testDelete(self):
        artifact_id = 396724439
        repo_name = "lexa/PyGithub"
        repo = self.g.get_repo(repo_name)
        artifact = repo.get_artifact(artifact_id)
        self.assertTrue(artifact.delete())
        with self.assertRaises(github.GithubException):
            repo.get_artifact(artifact_id)
