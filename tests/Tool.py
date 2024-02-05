from . import Framework


class Tool(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.tool = self.g.get_user().get_repo("PyGithub").get_code_scanning_analyses()[0].tool

    def testAttributes(self):
        self.assertIn("CodeQL", self.tool.name)
        self.assertEqual(None, self.tool.guid)
        self.assertIn("2.4.0", self.tool.version)
