from . import Framework


class CodeScanAnalysis(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_user().get_repo("PyGithub")

    def testAttributes(self):
        analysis = self.repo.get_code_scanning_analyses()[0]

        self.assertIn("refs/heads/main", analysis.ref)
        self.assertIn("d99612c3e1f2970085cfbaeadf8f010ef69bad83", analysis.commit_sha)
        self.assertIn(".github/workflows/codeql-analysis.yml:analyze", analysis.analysis_key)
        self.assertIn('{"language":"python"}', analysis.environment)
        self.assertIn("", analysis.error)
        self.assertIn(
            ".github/workflows/codeql-analysis.yml:analyze/language:python",
            analysis.category,
        )
        self.assertIn("2020-08-27T15:05:21Z", analysis.created_at)
        self.assertEqual(17, analysis.results_count)
        self.assertEqual(49, analysis.rules_count)
        self.assertEqual(201, analysis.id)
        self.assertIn(
            "https://api.github.com/repos/octocat/hello-world/code-scanning/analyses/201",
            analysis.url,
        )
        self.assertIn("6c81cd8e-b078-4ac3-a3be-1dad7dbd0b53", analysis.sarif_id)
        self.assertEqual(True, analysis.deletable)
        self.assertIn("", analysis.warning)
