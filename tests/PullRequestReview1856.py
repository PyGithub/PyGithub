import datetime

from . import Framework


class PullRequestReviewIssue(Framework.TestCase):
    def setUp(self):
        super().setUp()
        pumpkin_repo = self.g.get_repo("CS481-Team-Pumpkin/PyGithub", lazy=True)
        self.pumpkin_pull = pumpkin_repo.get_pull(3)
        self.pullreview = self.pumpkin_pull.get_review(631417478)

    def testDelete(self):
        before = self.pumpkin_pull.get_reviews()
        self.pullreview.delete()
        after = self.pumpkin_pull.get_reviews()
        self.assertNotEqual(list(before), list(after))