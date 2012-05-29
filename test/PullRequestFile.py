import Framework

class PullRequestFile( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.file = self.g.get_user().get_repo( "PyGithub" ).get_pull( 31 ).get_files()[ 0 ]

    def testAttributes( self ):
        self.assertEqual( self.file.additions, 1 )
        self.assertEqual( self.file.blob_url, "https://github.com/jacquev6/PyGithub/blob/8a4f306d4b223682dd19410d4a9150636ebe4206/codegen/templates/GithubObject.py" )
        self.assertEqual( self.file.changes, 2 )
        self.assertEqual( self.file.deletions, 1 )
        self.assertEqual( self.file.filename, "codegen/templates/GithubObject.py" )
        self.assertEqual( self.file.patch, '@@ -70,7 +70,7 @@ def __useAttributes( self, attributes ):\n \n         # @toto No need to check if attribute is in attributes when attribute is mandatory\n {% for attribute in class.attributes|dictsort:"name" %}\n-        if "{{ attribute.name }}" in attributes and attributes[ "{{ attribute.name }}" ] is not None:\n+        if "{{ attribute.name }}" in attributes and attributes[ "{{ attribute.name }}" ] is not None: # pragma no branch\n \n {% if attribute.type.cardinality == "scalar" %}\n {% if attribute.type.simple %}' )
        self.assertEqual( self.file.raw_url, "https://github.com/jacquev6/PyGithub/raw/8a4f306d4b223682dd19410d4a9150636ebe4206/codegen/templates/GithubObject.py" )
        self.assertEqual( self.file.sha, "8a4f306d4b223682dd19410d4a9150636ebe4206" )
        self.assertEqual( self.file.status, "modified" )
