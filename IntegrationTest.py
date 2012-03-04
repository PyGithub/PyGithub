#!/bin/env python

import re
import time
import sys
import httplib
import base64

from github import Github

class RecordReplayException( Exception ):
    pass

class RecordingHttpsConnection:
    class HttpResponse( object ):
        def __init__( self, file, res ):
            self.status = res.status
            self.__headers = res.getheaders()
            self.__output = res.read()
            file.write( str( self.status ) + "\n" )
            file.write( str( self.__headers ) + "\n" )
            file.write( str( self.__output ) + "\n" )

        def getheaders( self ):
            return self.__headers

        def read( self ):
            return self.__output

    __realHttpsConnection = httplib.HTTPSConnection

    def __init__( self, file, *args, **kwds ):
        self.__file = file
        self.__cnx = self.__realHttpsConnection( *args, **kwds )

    def request( self, verb, url, input, headers ):
        print verb, url
        self.__cnx.request( verb, url, input, headers )
        del headers[ "Authorization" ] # Do not let sensitive info in git :-p
        self.__file.write( verb + " " + url + " " + str( headers ) + " " + input + "\n" )

    def getresponse( self ):
        return RecordingHttpsConnection.HttpResponse( self.__file, self.__cnx.getresponse() )

    def close( self ):
        self.__file.write( "\n" )
        return self.__cnx.close()

class ReplayingHttpsConnection:
    class HttpResponse( object ):
        def __init__( self, file ):
            self.status = int( file.readline().strip() )
            self.__headers = eval( file.readline().strip() )
            self.__output = file.readline().strip()

        def getheaders( self ):
            return self.__headers

        def read( self ):
            return self.__output

    def __init__( self, file ):
        self.__file = file

    def request( self, verb, url, input, headers ):
        del headers[ "Authorization" ]
        if( self.__file.readline().strip() != verb + " " + url + " " + str( headers ) + " " + input ):
            raise RecordReplayException( "This test has been changed since last record. Please re-run this script with argument '--record'" )

    def getresponse( self ):
        return ReplayingHttpsConnection.HttpResponse( self.__file )

    def close( self ):
        self.__file.readline()

class IntegrationTest:
    cobayeUser = "Lyloa"
    cobayeOrganization = "BeaverSoftware"

    def main( self, argv ):
        record = False
        if len( argv ) >= 1:
            if argv[ 0 ] == "--record":
                argv = argv[ 1: ]
                record = True
            elif argv[ 0 ] == "--list":
                print "List of available tests:"
                print "\n".join( self.listTests() )
                return

        if record:
            print "Record mode: this script is really going to do requests to github.com"
        else:
            print "Replay mode: this script will used requests to and replies from github.com recorded in previous runs in record mode"

        if len( argv ) == 0:
            tests = self.listTests()
        else:
            tests = argv
        self.runTests( tests, record )

        if self.succeeded:
            self.analyseCoverage()

    def prepareRecord( self, test ):
        self.avoidError500FromGithub = lambda: time.sleep( 1 )
        try:
            import GithubCredentials
            self.g = Github( GithubCredentials.login, GithubCredentials.password )
            self.__file = open( self.__fileName( test ), "w" )
            httplib.HTTPSConnection = lambda *args, **kwds: RecordingHttpsConnection( self.__file, *args, **kwds )
        except ImportError:
            raise RecordReplayException( textwrap.dedent( """\
                Please create a 'GithubCredentials.py' file containing:"
                login = '<your github login>'"
                password = '<your github password>'""" ) )

    def prepareReplay( self, test ):
        self.avoidError500FromGithub = lambda: 0
        try:
            self.__file = None
            self.__file = open( self.__fileName( test ) )
            httplib.HTTPSConnection = lambda *args, **kwds: ReplayingHttpsConnection( self.__file )
            self.g = Github( "login", "password" )
        except IOError:
            raise RecordReplayException( "This test has never been recorded. Please re-run this script with argument '--record'" )

    def __fileName( self, test ):
        return "ReplayDataForIntegrationTest." + test + ".txt"

    def listTests( self ):
        return [ f[ 4: ] for f in dir( self ) if f.startswith( "test" ) ]

    def runTests( self, tests, record ):
        self.succeeded = True
        for test in tests:
            print
            print test
            print "=" * len( test )
            try:
                if record:
                    self.prepareRecord( test )
                else:
                    self.prepareReplay( test )
                getattr( self, "test" + test )()
                if not record:
                    if self.__file.readline():
                        raise RecordReplayException( "This test has been changed since last record. Please re-run this script with argument '--record'" )
            except RecordReplayException, e:
                print "*" * len( str( e ) )
                print e
                print "*" * len( str( e ) )
                self.succeeded = False
            finally:
                if self.__file is not None:
                    self.__file.close()

    def analyseCoverage( self ):
        coveredUrls = dict()
        for test in self.listTests():
            with open( self.__fileName( test ) ) as file:
                requests = [ line.strip() for line in file.readlines() ][ 0 : : 5 ]
                for request in requests:
                    verb, url = request.split( " " )[ 0 : 2 ]
                    if url not in coveredUrls:
                        coveredUrls[ url ] = set()
                    coveredUrls[ url ].add( verb )

        uncoveredMethods = set()
        with open( "ReferenceOfApis.md" ) as file:
            for line in file.readlines():
                line = line.strip()
                if line.startswith( "API" ):
                    currentApi = line[ 5 : -1 ]
                    apiRegex = re.sub( ":\w+", "\w+", currentApi )
                if line.startswith( "* " ) and line.endswith( "`" ):
                    verb = line[ 2 : line.find( ":" ) ]
                    for url, verbs in coveredUrls.iteritems():
                        if re.match( apiRegex, url ) and verb in verbs:
                            break
                    else:
                        uncoveredMethods.add( line[ line.find( "`" ) + 1 : -1 ] )

        if len( uncoveredMethods ) != 0:
            print
            print "Not covered (" + str( len( uncoveredMethods ) ) + "):"
            print "\n".join( sorted( uncoveredMethods ) )

    def testColaborators( self ):
        r = self.g.get_user().get_repo( "TestPyGithub" )
        cobaye = self.g.get_user( self.cobayeUser )
        self.printList( "Collaborators", r.get_collaborators(), lambda m: m.login )
        r.add_to_collaborators( cobaye )
        assert r.has_in_collaborators( cobaye )
        self.printList( "Collaborators", r.get_collaborators(), lambda m: m.login )
        r.remove_from_collaborators( cobaye )
        assert not r.has_in_collaborators( cobaye )
        self.printList( "Collaborators", r.get_collaborators(), lambda m: m.login )

    def testCommentCommit( self ):
        r = self.g.get_user().get_repo( "TestPyGithub" )
        c = r.get_commits()[ 0 ]
        self.printList( "Comments", c.get_comments(), lambda c: c.body )
        com1 = c.create_comment( "Comment created by PyGithub" )
        self.printList( "Comments", c.get_comments(), lambda c: c.body )
        com2 = c.create_comment( "Comment also created by PyGithub", path = "ReadMe.md", line = 1 )
        self.printList( "Comments", c.get_comments(), lambda c: c.body )
        com2.delete()
        com1.edit( body = "Comment edited by PyGithub" )
        self.printList( "Comments", c.get_comments(), lambda c: c.body )

    def testCreateForkForOrganization( self ):
        o = self.g.get_organization( self.cobayeOrganization )
        r = self.g.get_user().get_repo( "TestPyGithub" )
        rf = o.create_fork( r )
        print r.owner.login + "/" + r.name, "->", rf.owner.login + "/" + rf.name

    def testCreateRepoForOrganization( self ):
        o = self.g.get_organization( self.cobayeOrganization )
        self.printList( "Repos", o.get_repos(), lambda r: r.name )
        r = o.create_repo( "CreatedByPyGithub", has_wiki = False )
        self.printList( "Repos", o.get_repos(), lambda r: r.name )

    def testCreateRepoForUser( self ):
        u = self.g.get_user()
        self.printList( "Repos", u.get_repos(), lambda r: r.name )
        r = u.create_repo( "CreatedByPyGithub", has_wiki = False )
        self.printList( "Repos", u.get_repos(), lambda r: r.name )

    def testEditAuthenticatedUser( self ):
        u = self.g.get_user()
        originalName = u.name
        print u.name
        u.edit( name = u.name + " (edited by PyGithub)" )
        print u.name
        u.edit( name = originalName )
        print u.name

    def testEditOrganization( self ):
        o = self.g.get_organization( self.cobayeOrganization )
        originalName = o.name
        print o.name
        o.edit( name = str( o.name ) + " (edited by PyGithub)" )
        print o.name
        o.edit( name = originalName )
        print o.name

    def testEditOrganizationTeamAndMembers( self ):
        o = self.g.get_organization( self.cobayeOrganization )
        r = o.get_repo( "TestPyGithub" )

        self.printList( "Teams", o.get_teams(), lambda t: t.name )
        t = o.create_team( "PyGithubTesters" )
        t.edit( "PyGithubTesters", permission = "push" )
        self.printList( "Teams", o.get_teams(), lambda t: t.name )

        u = self.g.get_user( self.cobayeUser )

        self.printList( "Team members", t.get_members(), lambda m: m.login )
        self.printList( "Team repos", t.get_repos(), lambda r: r.name )
        assert not t.has_in_repos( r )
        assert not t.has_in_members( u )
        t.add_to_members( u )
        t.add_to_repos( r )
        assert t.has_in_repos( r )
        assert t.has_in_members( u )
        self.printList( "Team members", t.get_members(), lambda m: m.login )
        self.printList( "Team repos", t.get_repos(), lambda r: r.name )

        self.printList( "Public members", o.get_public_members(), lambda m: m.login )
        o.add_to_public_members( u )
        assert o.has_in_public_members( u )
        self.printList( "Public members", o.get_public_members(), lambda m: m.login )
        o.remove_from_public_members( u )
        assert not o.has_in_public_members( u )
        self.printList( "Public members", o.get_public_members(), lambda m: m.login )

        self.printList( "Members", o.get_members(), lambda m: m.login )
        assert o.has_in_members( u )
        o.remove_from_members( u )
        assert not o.has_in_members( u )
        self.printList( "Members", o.get_members(), lambda m: m.login )

        self.printList( "Team members", t.get_members(), lambda m: m.login )
        self.printList( "Team repos", t.get_repos(), lambda r: r.name )
        t.remove_from_members( u )
        t.remove_from_repos( r )
        assert not t.has_in_repos( r )
        assert not t.has_in_members( u )
        self.printList( "Team members", t.get_members(), lambda m: m.login )
        self.printList( "Team repos", t.get_repos(), lambda r: r.name )

        t.delete()
        self.printList( "Teams", o.get_teams(), lambda t: t.name )

    def testFollow( self ):
        cobaye = self.g.get_user( self.cobayeUser )
        u = self.g.get_user()
        u.remove_from_following( cobaye )
        assert not u.has_in_following( cobaye )
        u.add_to_following( cobaye )
        assert u.has_in_following( cobaye )
        self.printList( "Following", u.get_following(), lambda f: f.login )
        self.printList( "Followers", u.get_followers(), lambda f: f.login )

    def testGists( self ):
        u = self.g.get_user()
        self.printList( "Gists", u.get_gists(), lambda g: g.description )
        g = u.create_gist( public = True, description = "Gist created by PyGithub", files = { "foo.bar": { "content": "This gist was created by PyGithub" } } )
        self.printList( "Gists", u.get_gists(), lambda g: g.description )
        g.edit( description = "Gist edited by PyGithub" )
        self.printList( "Gists", u.get_gists(), lambda g: g.description )

        self.printList( "Starred gists", u.get_starred_gists(), lambda g: g.description )
        g.set_starred()
        assert g.is_starred()
        self.printList( "Starred gists", u.get_starred_gists(), lambda g: g.description )
        g.reset_starred()
        self.printList( "Starred gists", u.get_starred_gists(), lambda g: g.description )

        self.printList( "Gist comments", g.get_comments(), lambda c: c.body )
        c = g.create_comment( "Comment created by PyGithub" )
        self.printList( "Gist comments", g.get_comments(), lambda c: c.body )
        c.edit( "Comment edited by PyGithub" )
        self.printList( "Gist comments", g.get_comments(), lambda c: c.body )
        sameComment = g.get_comment( c.id )
        c.delete()
        self.printList( "Gist comments", g.get_comments(), lambda c: c.body )

        otherGist = self.g.get_gist( 1965703 ).create_fork() # Origin gist picked up randomly
        self.printList( "Gists", u.get_gists(), lambda g: g.description or "None" )
        otherGist.delete()
        self.printList( "Gists", u.get_gists(), lambda g: g.description )

        g.delete()
        self.printList( "Gists", u.get_gists(), lambda g: g.description )

    def testGitObjects( self ):
        o = self.g.get_organization( self.cobayeOrganization )
        r = o.get_repo( "TestPyGithub" )

        masterRef = r.get_git_ref( "refs/heads/master" )
        masterCommit = r.get_git_commit( masterRef.object[ "sha" ] )
        masterTree = r.get_git_tree( masterCommit.tree.sha )
        readmeBlob = None
        for element in masterTree.tree:
            if element[ "path" ] == "ReadMe.md":
                readmeBlob = r.get_git_blob( element[ "sha" ] )
                break

        blob = r.create_git_blob( "This blob was created by PyGithub", encoding = "latin1" )
        tree = r.create_git_tree( [ { "path": "foo.bar", "mode": "100644", "type": "blob", "sha": blob.sha }, { "path": "ReadMe.md", "mode": "100644", "type": "blob", "sha": readmeBlob.sha } ] )
        commit = r.create_git_commit( "This commit was created by PyGithub", tree.sha, [ masterCommit.sha ] )
        r.create_git_ref( "refs/heads/previous_master", masterRef.object[ "sha" ] )
        masterRef.edit( commit.sha )

        tag = r.create_git_tag( "tagCreatedByPyGithub", "This tag was created by PyGithub", commit.sha, "commit" )
        r.create_git_ref( "refs/tags/tagCreatedByPyGithub", tag.sha )
        reTag = r.get_git_tag( tag.sha )

    def testIssuesAndMilestones( self ):
        u = self.g.get_user()
        r = u.get_repo( "TestPyGithub" )

        self.printList( "Issues", r.get_issues(), lambda i: i.title )
        i = r.create_issue( "Issue created by PyGithub" )
        self.printList( "Issues", r.get_issues(), lambda i: i.title )
        i.edit( body = "Issue edited by PyGithub" )

        self.printList( "Comments on issue", i.get_comments(), lambda c: c.body )
        c = i.create_comment( "Comment created by PyGithub" )
        self.printList( "Comments on issue", i.get_comments(), lambda c: c.body )
        c.edit( "Comment edited by PyGithub" )
        sameComment = i.get_comment( c.id )
        self.printList( "Comments on issue", i.get_comments(), lambda c: c.body )
        c.delete()
        self.printList( "Comments on issue", i.get_comments(), lambda c: c.body )

        self.printList( "Milestones", r.get_milestones(), lambda m: m.title )
        m = r.create_milestone( "Milestone created by PyGithub" )
        self.printList( "Milestones", r.get_milestones(), lambda m: m.title )
        m.edit( title = "Milestone edited by PyGithub" )
        self.printList( "Milestones", r.get_milestones(), lambda m: m.title )

        self.printList( "Issues of milestone", r.get_issues( milestone = m.number ), lambda i: i.title )
        i.edit( milestone = m.number )
        self.printList( "Issues of milestone", r.get_issues( milestone = m.number ), lambda i: i.title )

        self.printList( "Repository labels", r.get_labels(), lambda l: l.name )
        labelD = r.create_label( "D", "FF0000" )
        self.printList( "Repository labels", r.get_labels(), lambda l: l.name )
        ### @todo Uncomment after fixing bug about BaseUrl depending on editable attribute
        # labelD.edit( "Dada", "00FF00" )
        # self.printList( "Repository labels", r.get_labels(), lambda l: l.name )
        labelD.delete()
        self.printList( "Repository labels", r.get_labels(), lambda l: l.name )

        labelA = r.get_label( "bug" )
        labelB = r.get_label( "duplicate" )
        labelC = r.get_label( "invalid" )

        self.printList( "Labels", i.get_labels(), lambda l: l.name )
        i.set_labels( labelA, labelB )
        self.printList( "Labels", i.get_labels(), lambda l: l.name )
        i.remove_from_labels( labelB )
        self.printList( "Labels", i.get_labels(), lambda l: l.name )
        i.delete_labels()
        self.printList( "Labels", i.get_labels(), lambda l: l.name )
        i.add_to_labels( labelB, labelC )
        self.printList( "Labels", i.get_labels(), lambda l: l.name )

        self.printList( "Milestone labels", r.get_milestone( m.number ).get_labels(), lambda l: l.name )

        m.delete()
        self.printList( "Milestones", r.get_milestones(), lambda m: m.title )

    def testKeys( self ):
        u = self.g.get_user()
        self.printList( "Keys", u.get_keys(), lambda k: k.title )
        k = u.create_key( u.login + "@PyGithub", "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAvborozfBBn2a+JETqPekTWZ1tmYjpfH9wTKFPLjIXQmxXjNye6HVgvi+iMI436RdoLsPEFDe3cjrQ6CJa7KzhRJKNTPh5EZbKI13CXfMGr7V1i3tOokXBFSRQKnDx2dj2hnswqxGUk2jXpgC/KA1q71yqnL45CBlWr50eDpwUIEPnmqSrPpRV/0ZGwIlh4o7+6HwPUF9aBhWj945WSkjZubR4UFWlDZl7ROafpkJHs2cQzaxtmBOZnu6dzmfyro0zJsvhZKD2K6d9eKgpDeKaw5rWr6FeOZPd4xyDaV1gctG0YEui8uuSPKhpcykgREUAFf+vmOKt+yXnOoq8P4vIQ==" )
        self.printList( "Keys", u.get_keys(), lambda k: k.title )
        k.edit( title = u.login + "@PyGithub2" )
        k = u.get_key( k.id )
        self.printList( "Keys", u.get_keys(), lambda k: k.title )
        k.delete()
        self.printList( "Keys", u.get_keys(), lambda k: k.title )

    def testNamedUserDetails( self ):
        u = self.g.get_user( "jacquev6" )
        print u.login, "(" + u.name + ") is from", u.location
        self.printList( "Repos", u.get_repos(), lambda r: r.name )
        self.printList( "Followers", u.get_followers(), lambda m: m.login )
        self.printList( "Following", u.get_following(), lambda m: m.login )
        self.printList( "Watched", u.get_watched(), lambda r: r.owner.login + "/" + r.name )
        self.printList( "Organizations", u.get_orgs(), lambda o: o.login )
        self.printList( "Gists", u.get_gists(), lambda g: g.description )

    def testOrganizationDetails( self ):
        o = self.g.get_organization( "github" )
        print o.login, "(" + o.name + ") is in", o.location

    def testPullRequest( self ):
        r = self.g.get_user().get_repo( "TestPyGithub" )
        self.printList( "Pull requests", r.get_pulls(), lambda p: p.title )
        p1 = r.create_pull( "Pull request created by PyGithub", "", "master", "BeaverSoftware:master" )
        self.printList( "Pull requests", r.get_pulls(), lambda p: p.title )
        p1.edit( state = "closed" )
        self.printList( "Pull requests", r.get_pulls(), lambda p: p.title )
        p2 = r.create_pull( "Pull request also created by PyGithub", "", "master", "BeaverSoftware:master" )
        self.printList( "Pull requests", r.get_pulls(), lambda p: p.title )
        self.printList( "Files", p2.get_files(), lambda f: f.filename )
        self.printList( "Commits", p2.get_commits(), lambda c: c.commit.message )
        self.printList( "Comments", p2.get_comments(), lambda c: c.body )
        com = p2.create_comment( "Comment created by PyGithub", "e4e84560cb5e87f3c0e9f710dae1ddab0eef487b", "foo.bar", 1 )
        self.printList( "Comments", p2.get_comments(), lambda c: c.body )
        com.edit( body = "Comment edited by PyGithub" )
        self.printList( "Comments", p2.get_comments(), lambda c: c.body )
        sameCom = p2.get_comment( com.id )
        sameCom.delete()
        self.printList( "Comments", p2.get_comments(), lambda c: c.body )
        p2.edit( state = "closed" )
        self.printList( "Pull requests", r.get_pulls(), lambda p: p.title )

    def testRepositoryKeys( self ):
        r = self.g.get_user().get_repo( "TestPyGithub" )
        self.printList( "Keys", r.get_keys(), lambda k: k.title )
        k = r.create_key( "Key created by PyGithub", "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAvborozfBBn2a+JETqPekTWZ1tmYjpfH9wTKFPLjIXQmxXjNye6HVgvi+iMI436RdoLsPEFDe3cjrQ6CJa7KzhRJKNTPh5EZbKI13CXfMGr7V1i3tOokXBFSRQKnDx2dj2hnswqxGUk2jXpgC/KA1q71yqnL45CBlWr50eDpwUIEPnmqSrPpRV/0ZGwIlh4o7+6HwPUF9aBhWj945WSkjZubR4UFWlDZl7ROafpkJHs2cQzaxtmBOZnu6dzmfyro0zJsvhZKD2K6d9eKgpDeKaw5rWr6FeOZPd4xyDaV1gctG0YEui8uuSPKhpcykgREUAFf+vmOKt+yXnOoq8P4vIQ==" )
        self.printList( "Keys", r.get_keys(), lambda k: k.title )
        k.edit( "Key edited by PyGithub", "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAvborozfBBn2a+JETqPekTWZ1tmYjpfH9wTKFPLjIXQmxXjNye6HVgvi+iMI436RdoLsPEFDe3cjrQ6CJa7KzhRJKNTPh5EZbKI13CXfMGr7V1i3tOokXBFSRQKnDx2dj2hnswqxGUk2jXpgC/KA1q71yqnL45CBlWr50eDpwUIEPnmqSrPpRV/0ZGwIlh4o7+6HwPUF9aBhWj945WSkjZubR4UFWlDZl7ROafpkJHs2cQzaxtmBOZnu6dzmfyro0zJsvhZKD2K6d9eKgpDeKaw5rWr6FeOZPd4xyDaV1gctG0YEui8uuSPKhpcykgREUAFf+vmOKt+yXnOoq8P4vIQ==" )
        self.printList( "Keys", r.get_keys(), lambda k: k.title )
        sameKey = r.get_key( k.id )
        sameKey.delete()
        self.printList( "Keys", r.get_keys(), lambda k: k.title )

    def testWatch( self ):
        r = self.g.get_user( "jacquev6" ).get_repo( "PyGithub" )
        u = self.g.get_user()
        u.remove_from_watched( r )
        assert not u.has_in_watched( r )
        u.add_to_watched( r )
        assert u.has_in_watched( r )
        self.printList( "Watched", u.get_watched(), lambda r: r.name )

    def testEmails( self ):
        u = self.g.get_user()
        self.printList( "Emails", u.get_emails() )
        u.add_to_emails( "ab@xxx.com", "cd@xxx.com" )
        self.printList( "Emails", u.get_emails() )
        u.remove_from_emails( "ab@xxx.com", "cd@xxx.com" )
        self.printList( "Emails", u.get_emails() )

    def printList( self, title, iterable, f = lambda x: x ):
        print title + ":", ", ".join( f( x ) for x in iterable[ :10 ] ), "..." if len( iterable ) > 10 else ""

IntegrationTest().main( sys.argv[ 1: ] )
