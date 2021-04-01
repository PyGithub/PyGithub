import datetime

from . import Framework


class PullRequestReviewIssue(Framework.TestCase):
    def setUp(self):
        super().setUp()
        pumpkin_repo = self.g.get_repo("CS481-Team-Pumpkin/PyGithub", lazy=True)
        self.pumpkin_pull = pumpkin_repo.get_pull(1)
        self.pullreview = self.pumpkin_pull.get_review(626417408)

    def testDelete(self):
        self.pullreview.delete()
        pr = self.pumpkin_pull.get_review(626417408)
        self.assertEqual(pr.state, "CHANGES_REQUESTED")