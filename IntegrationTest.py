#!/bin/env python

import sys
import httplib

from github import Github

class RecordingHttpResponse( object ):
    def __init__( self, res ):
        self.__res = res

    @property
    def status( self ):
        return self.__res.status

    def getheaders( self ):
        return self.__res.getheaders()

    def read( self ):
        return self.__res.read()

class RecordingHttpsConnection:
    __realHttpsConnection = httplib.HTTPSConnection

    def __init__( self, host, strict ):
        self.__cnx = self.__realHttpsConnection( host, strict = strict )

    def request( *args, **kwds ):
        return self.__cnx.request( *args, **kwds )

    def getresponse( self ):
        return RecordingHttpResponse( self.__cnx.getresponse() )

    def close( self ):
        return self.__cnx.close()

class IntegrationTest:
    def main( self ):
        if len( sys.argv ) == 2 and sys.argv[ 1 ] == "--record":
            print "Record mode: I'm really going to do requests to github.com. Please type 'yes' and return"
            confirm = sys.stdin.readline().strip()
            if confirm != "yes":
                exit( 1 )
            self.record()
        else:
            self.replay()

        exit()

    def record( self ):
        g = self.prepareRecord()
        self.playScenario( g )

    def replay( self ):
        g = self.prepareReplay()
        self.playScenario( g )

    def prepareRecord( self ):
        try:
            import GithubCredentials
            g = Github( GithubCredentials.login, GithubCredentials.password )
            httplib.HTTPSConnection = RecordingHttpsConnection
            return g
        except ImportError:
            print "Please create a 'GithubCredentials.py' file containing:"
            print "login = '<your github login>'"
            print "password = '<your github password>'"
            exit( 1 )

    def playScenario( self, g ):
        print g.get_user().name

    def dumpUser( u ):
        print u.login, "(", u.name, ")"
        print "  Repos:"
        for r in u.get_repos():
            print "   ", r.name,
            if r.fork:
                print "<-", r.parent.owner.login + "/" + r.parent.name,
                print "<-", r.source.owner.login + "/" + r.source.name,
            print
        print "  Watched:", ", ".join( r.name for r in u.get_watched() )
        print "  Organizations:", ", ".join( o.login for o in u.get_orgs() )
        print "  Following:", ", ".join( f.login for f in u.get_following() )
        print "  Followers:", ", ".join( f.login for f in u.get_followers() )
        print

    def dumpOrganization( o ):
        print o.login, "(", o.name, ")"
        print "  Members:", ", ".join( u.login for u in o.get_members() )
        print "  Repos:", ", ".join( r.name for r in o.get_repos() )
        print

    def dumpRepository( r ):
        print r.owner.login + "/" + r.name
        print "  Collaborators:", ", ".join( u.login for u in r.get_collaborators() )
        print "  Contributors:", ", ".join( u.login for u in r.get_contributors() )
        print "  Watchers:", ", ".join( u.login for u in r.get_watchers() )
        print "  Forks:", ", ".join( f.owner.login + "/" + f.name for f in r.get_forks() )
        print

IntegrationTest().main()

g = Github( GithubCredentials.login, GithubCredentials.password )

# Reads
# =====
u = g.get_user()
# o = g.get_organization( "<some organization you are admin of>" )
jacquev6 = g.get_user( "jacquev6" )
PyGithub = jacquev6.get_repo( "PyGithub" )

dumpUser( u )
dumpUser( jacquev6 )
dumpOrganization( g.get_organization( "github" ) )
dumpRepository( PyGithub )

# Writes (to user)
# ================
# u.edit( bio = u.bio + "(Edited by PyGithub)" )

# u.remove_from_following( jacquev6 )
# u.add_to_following( jacquev6 )

# u.remove_from_watched( PyGithub )
# u.add_to_watched( PyGithub )

# dumpRepository( u.create_repo( name = "TestGithubApi", description = "Created by a Python script!", has_wiki = False ) )
# dumpRepository( u.create_fork( PyGithub ) )


# Writes (to organization)
# ========================
# o.edit( location = "Paris, France" )

# dumpRepository( o.create_repo( name = "TestGithubApi", description = "Created by a Python script!", has_wiki = False ) )
# dumpRepository( o.create_fork( PyGithub ) )
