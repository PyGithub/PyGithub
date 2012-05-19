import Framework

class Gist( Framework.TestCase ):
    def testGetAll( self ):
        ids = [ "2729695", "2729656", "2729597", "2729584", "2729569", "2729554", "2729543", "2729537", "2729536", "2729533", "2729525", "2729522", "2729519", "2729515", "2729506", "2729487", "2729484", "2729482", "2729441", "2729432", "2729420", "2729398", "2729372", "2729371", "2729351", "2729346", "2729316", "2729304", "2729296", "2729276", "2729272", "2729265", "2729195", "2729160", "2729143", "2729127", "2729119", "2729113", "2729103", "2729069", "2729059", "2729051", "2729029", "2729027", "2729026", "2729022", "2729002", "2728985", "2728979", "2728964", "2728937", "2728933", "2728884", "2728869", "2728866", "2728855", "2728854", "2728853", "2728846", "2728825", "2728814", "2728813", "2728812", "2728805", "2728802", "2728800", "2728798", "2728797", "2728796", "2728793", "2728758", "2728754", "2728751", "2728748", "2728721", "2728716", "2728715", "2728705", "2728701", "2728699", "2728697", "2728688", "2728683", "2728677", "2728649", "2728640", "2728625", "2728620", "2728615", "2728614", "2728565", "2728564", "2728554", "2728523", "2728519", "2728511", "2728497", "2728496", "2728495", "2728487" ]
        gists = self.g.get_gists()
        i = 0
        for gist in gists:
            self.assertEquals( gist.id, ids[ i ] )
            i += 1
            if i == 100:
                break

    def testAttributes( self ):
        gist = self.g.get_gist( "1942384" )
        self.assertEquals( gist.comments, 0 )
        self.assertEquals( gist.created_at, "2012-02-29T16:47:12Z" )
        self.assertEquals( gist.description, "How to error 500 Github API v3, as requested by Rick (GitHub Staff)" )
        self.assertEquals( gist.files, {u'fail_github.py': {u'raw_url': u'https://gist.github.com/raw/1942384/2fb3aa84e0efa50dc0f4c18b5df5b7b9ab27076b/fail_github.py', u'language': u'Python', u'filename': u'fail_github.py', u'content': u'import httplib\nimport base64\nimport json\n\nlogin = ""\npassword = ""\norgName = ""\nrepoName = "FailGithubApi"\n\ndef doRequest( verb, url, input ):\n    input = json.dumps( input )\n    cnx = httplib.HTTPSConnection( "api.github.com", strict = True )\n    cnx.request( verb, url, input, { "Authorization" : "Basic " + base64.b64encode( login + ":" + password ).replace( \'\\n\', \'\' ) } )\n    response = cnx.getresponse()\n    status = response.status\n    output = response.read()\n    cnx.close()\n    print verb, url, input, "=>", status, output\n    print\n    if status < 200 or status >= 300:\n        exit( 1 )\n    return json.loads( output )\n\n# Create a repo\ndoRequest( "POST", "/user/repos", { "name": repoName } )\n\n# Create a blob, a tree, a commit and the master branch\nb = doRequest(\n    "POST", "/repos/%s/%s/git/blobs" % ( login, repoName ),\n    { "content": "Content of the blob", "encoding": "latin1" }\n)\nt = doRequest(\n    "POST", "/repos/%s/%s/git/trees" % ( login, repoName ),\n    { "tree" : [ { "path": "foo.bar", "type": "blob", "mode": "100644", "sha": b["sha"] } ] }\n)\nc = doRequest(\n    "POST", "/repos/%s/%s/git/commits" % ( login, repoName ),\n    { "parents": [], "message": "Message of the commit", "tree": t["sha"] }\n)\ndoRequest(\n    "POST", "/repos/%s/%s/git/refs" % ( login, repoName ),\n    { "ref": "refs/heads/master", "sha": c["sha"] }\n)\n\n# Fork the repo\ndoRequest( "POST", "/repos/%s/%s/forks?org=%s" % ( login, repoName, orgName ), None )\n\n# Create a new blob => BOOM error 500\ndoRequest(\n    "POST", "/repos/%s/%s/git/blobs" % ( orgName, repoName ),\n    { "content": "Content of the new blob", "encoding": "latin1" }\n)\n', u'type': u'application/python', u'size': 1636}} ) ### @todo
        self.assertEquals( gist.forks, [] )
        self.assertEquals( gist.git_pull_url, "git://gist.github.com/1942384.git" )
        self.assertEquals( gist.git_push_url, "git@gist.github.com:1942384.git" )
        self.assertEquals( len( gist.history ), 1 )
        self.assertEquals( gist.history[ 0 ].change_status.additions, 52 )
        self.assertEquals( gist.history[ 0 ].change_status.deletions, 0 )
        self.assertEquals( gist.history[ 0 ].change_status.total, 52 )
        self.assertEquals( gist.history[ 0 ].committed_at, "2012-02-29T16:47:12Z" )
        self.assertEquals( gist.history[ 0 ].url, "https://api.github.com/gists/1942384/a40de483e42ba33bda308371c0ef8383db73be9e" )
        self.assertEquals( gist.history[ 0 ].user.login, "jacquev6" )
        self.assertEquals( gist.history[ 0 ].version, "a40de483e42ba33bda308371c0ef8383db73be9e" )
        self.assertEquals( gist.html_url, "https://gist.github.com/1942384" )
        self.assertEquals( gist.id, "1942384" )
        self.assertEquals( gist.public, True )
        self.assertEquals( gist.updated_at, "2012-02-29T16:47:12Z" )
        self.assertEquals( gist.url, "https://api.github.com/gists/1942384" )
        self.assertEquals( gist.user.login, "jacquev6" )

    def testCreate( self ):
        gist = self.g.get_user().create_gist( True, { "foobar.txt": { "content": "File created by PyGithub" } }, "Gist created by PyGithub" )
        self.assertEquals( gist.description, "Gist created by PyGithub" )
        self.assertEquals( gist.files, {u'foobar.txt': {u'raw_url': u'https://gist.github.com/raw/2729810/73a1c7f17aa0ad5d7cbb5a8ca033ce47d3d23197/foobar.txt', u'language': u'Text', u'filename': u'foobar.txt', u'content': u'File created by PyGithub', u'type': u'text/plain', u'size': 24}} ) ### @todo

    def testEditWithoutParameters( self ):
        gist = self.g.get_gist( "2729810" )
        gist.edit()
        self.assertEquals( gist.description, "Gist created by PyGithub" )
        self.assertEquals( gist.updated_at, "2012-05-19T07:00:58Z" )

    def testEditWithAllParameters( self ):
        gist = self.g.get_gist( "2729810" )
        gist.edit( "Description edited by PyGithub", { "barbaz.txt": { "content": "File also created by PyGithub" } } )
        self.assertEquals( gist.description, "Description edited by PyGithub" )
        self.assertEquals( gist.updated_at, "2012-05-19T07:06:10Z" )
        self.assertEquals( gist.files, {u'foobar.txt': {u'raw_url': u'https://gist.github.com/raw/2729810/73a1c7f17aa0ad5d7cbb5a8ca033ce47d3d23197/foobar.txt', u'language': u'Text', u'filename': u'foobar.txt', u'content': u'File created by PyGithub', u'type': u'text/plain', u'size': 24}, u'barbaz.txt': {u'raw_url': u'https://gist.github.com/raw/2729810/92be1df4e473d2541c5c166ad145a39d0324de8b/barbaz.txt', u'language': u'Text', u'filename': u'barbaz.txt', u'content': u'File also created by PyGithub', u'type': u'text/plain', u'size': 29}} ) # Notice that the file is added, not replacing ### @todo

    def testCreateComment( self ):
        gist = self.g.get_gist( "2729810" )
        comment = gist.create_comment( "Comment created by PyGithub" )
        self.assertEquals( comment.id, 323629 )

    def testCommentAttributes( self ):
        comment = self.g.get_gist( "2729810" ).get_comment( 323629 )
        self.assertEquals( comment.body, "Comment created by PyGithub" )
        self.assertEquals( comment.created_at, "2012-05-19T07:07:57Z" )
        self.assertEquals( comment.id, 323629 )
        self.assertEquals( comment.updated_at, "2012-05-19T07:07:57Z" )
        self.assertEquals( comment.url, "https://api.github.com/gists/comments/323629" )
        self.assertEquals( comment.user.login, "jacquev6" )

    def testEditComment( self ):
        comment = self.g.get_gist( "2729810" ).get_comment( 323629 )
        comment.edit( "Comment edited by PyGithub" )
        self.assertEquals( comment.body, "Comment edited by PyGithub" )
        self.assertEquals( comment.updated_at, "2012-05-19T07:12:32Z" )

    def testDeleteComment( self ):
        comment = self.g.get_gist( "2729810" ).get_comment( 323629 )
        comment.delete()

    def testGetComments( self ):
        gist = self.g.get_gist( "2729810" )
        for comment in gist.get_comments(): # There is only one comment
            self.assertEquals( comment.id, 323637 )

    def testStarring( self ):
        gist = self.g.get_gist( "2729810" )
        self.assertFalse( gist.is_starred() )
        gist.set_starred()
        self.assertTrue( gist.is_starred() )
        gist.reset_starred()
        self.assertFalse( gist.is_starred() )

    def testFork( self ):
        gist = self.g.get_gist( "2729818" ) # Random gist
        myGist = gist.create_fork()
        self.assertEquals( myGist.id, "2729865" )
        self.assertEquals( myGist.fork_of, None ) # WTF
        sameGist = self.g.get_gist( "2729865" )
        self.assertEquals( sameGist.fork_of.id, "2729818" )

    def testDelete( self ):
        gist = self.g.get_gist( "2729865" )
        gist.delete()
