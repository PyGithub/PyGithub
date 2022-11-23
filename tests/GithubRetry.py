import github

from . import Framework

REPO_NAME = "PyGithub/PyGithub"


class GithubRetry(Framework.TestCase):
    def handleResponse(self, response):
        github.Requester.Requester.__connection.handle_response(response)

    def setUp(self):
        self.setPerPage(10)
        retry = github.GithubRetry()
        Framework.RecordingConnection.injectExtraResponseHandler(retry.injectResponseHandler)
        self.enableRetry(retry)
        super().setUp()

    def testPrimaryRateLimitHandling(self):
        issues = self.g.search_issues("is:issue rate limit")
        with self.assertRaises(github.RateLimitExceededException):
            self.assertEqual(1, len([issue for issue in issues]))

    def testSecondaryRateLimitHandling(self):
        issues = self.g.search_issues("is:issue rate limit")
        with self.assertRaises(github.RateLimitExceededException):
            self.assertEqual(1, len([issue for issue in issues]))

    def testSecondaryRateLimitHandling1(self):
        issues = self.g.search_issues("is:issue rate limit")
        with self.assertRaises(github.RateLimitExceededException):
            self.assertEqual(1, len([issue for issue in issues]))
