
import Framework


class SourceImport(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.user = self.g.get_user("brix4dayz")
        self.repo = self.user.get_repo("source-import-test")
        self.source_import = self.repo.get_source_import()

    def testAttributes(self):
        self.assertEqual(self.source_import.authors_count, 1)
        self.assertEqual(self.source_import.authors_url, "https://api.github.com/repos/brix4dayz/source-import-test/import/authors")
        self.assertEqual(self.source_import.has_large_files, False)
        self.assertEqual(self.source_import.html_url, "https://github.com/brix4dayz/source-import-test/import")
        self.assertEqual(self.source_import.large_files_count, 0)
        self.assertEqual(self.source_import.large_files_size, 0)
        self.assertEqual(self.source_import.repository_url, "https://api.github.com/repos/brix4dayz/source-import-test")
        self.assertEqual(self.source_import.status, "complete")
        self.assertEqual(self.source_import.status_text, "Done")
        self.assertEqual(self.source_import.url, "https://api.github.com/repos/brix4dayz/source-import-test/import")
        self.assertEqual(self.source_import.use_lfs, "undecided")
        self.assertEqual(self.source_import.vcs, "mercurial")
        self.assertEqual(self.source_import.vcs_url, "https://bitbucket.org/hfuss/source-import-test")

        self.assertEqual(self.source_import.__repr__(),
                         'SourceImport(vcs_url="https://bitbucket.org/hfuss/source-import-test", url="https://api.github.com/repos/brix4dayz/source-import-test/import", status="complete", repository_url="https://api.github.com/repos/brix4dayz/source-import-test")')
