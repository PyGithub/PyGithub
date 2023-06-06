import github

from . import Framework

REPO_NAME = "PyGithub/PyGithub"


class PoolSize(Framework.TestCase):
    def setUp(self):
        Framework.setPoolSize(20)
        super().setUp()

    def testReturnsRepoAfterSettingPoolSize(self):
        repository = self.g.get_repo(REPO_NAME)
        self.assertIsInstance(repository, github.Repository.Repository)
        self.assertEqual(repository.full_name, REPO_NAME)

    def testReturnsRepoAfterSettingPoolSizeHttp(self):
        g = github.Github(
            auth=self.login,
            base_url="http://my.enterprise.com",
            pool_size=20,
        )
        repository = g.get_repo(REPO_NAME)
        self.assertIsInstance(repository, github.Repository.Repository)
        self.assertEqual(repository.full_name, REPO_NAME)
