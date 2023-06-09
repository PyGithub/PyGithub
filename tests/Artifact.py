#!/usr/bin/env python3

import github

from . import Framework


class Artifact(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("transmission-web-control/transmission-web-control")

    def testGetArtifactsFromWorkflow(self):
        artifact = self.repo.get_workflow_run(5138169628).get_artifacts()[0]

        self.assertEqual(artifact.name, "build-tar")
        self.assertFalse(artifact.expired)
        self.assertEqual(repr(artifact), 'Artifact(name="build-tar", id=724958104)')

    def testGetArtifactsFromRepoWithName(self):
        artifacts = self.repo.get_artifacts(name="build-tar")
        self.assertEqual(artifacts.totalCount, 296)
        assert all(x.name == "build-tar" for x in artifacts)

        artifact = artifacts[0]

        self.assertEqual(artifact.name, "build-tar")
        self.assertEqual(repr(artifact), 'Artifact(name="build-tar", id=724959170)')

    def testGetSingleArtifactFromRepo(self):
        artifact = self.repo.get_artifact(719509139)

        self.assertEqual(artifact.name, "build-zip")
        self.assertFalse(artifact.expired)
        self.assertEqual(repr(artifact), 'Artifact(name="build-zip", id=719509139)')

    def testGetArtifactsFromRepo(self):
        artifact_id = 719509139
        artifacts = self.repo.get_artifacts()
        for item in artifacts:
            if item.id == artifact_id:
                artifact = item
                break
        else:
            assert False, f"No artifact {artifact_id} is found"

        self.assertEqual(
            repr(artifact),
            f'Artifact(name="build-zip", id={artifact_id})',
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
