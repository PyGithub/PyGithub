from . import Framework


class PullRequestReview1856(Framework.TestCase):
    def setUp(self):
        super().setUp()
        pumpkin_repo = self.g.get_repo("CS481-Team-Pumpkin/PyGithub", lazy=True)
        self.pumpkin_pull = pumpkin_repo.get_pull(4)
        self.pullreview = self.pumpkin_pull.get_review(631460061)

    def testDelete(self):
        self.pullreview.delete()
        reviews = self.pumpkin_pull.get_reviews()
        self.assertEqual(list(reviews), [])
