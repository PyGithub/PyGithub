import urllib2
import json
import base64

from GithubObjects import *

class Github:
    def __init__( self, login, password ):
        self.__login = login
        self.__password = password

    class _Request( urllib2.Request ):
        def __init__( self, verb, url, data ):
            urllib2.Request.__init__( self, url, data )
            self.__verb = verb

        def get_method( self ):
            return self.__verb

    def _dataRequest( self, verb, url, data = None ):
        return json.load( self.__rawRequest( verb, url, json.dumps( data ) ) )

    def _statusRequest( self, verb, url, data = None ):
        try:
            print verb, url, data
            self.__rawRequest( verb, url, json.dumps( data ) )
            print "Got HTTP status 200"
            return 200
        except urllib2.HTTPError as e:
            print "Got HTTP status", e.code
            return e.code

    def __rawRequest( self, verb, url, data ):
        assert( verb in [ "HEAD", "GET", "POST", "PATCH", "PUT", "DELETE" ] )

        # print verb, url, data

        req = Github._Request( verb, "https://api.github.com" + url, data )
        b64_userpass = base64.b64encode( '%s:%s' % ( self.__login, self.__password ) )
        b64_userpass = b64_userpass.replace( '\n', '' )
        req.add_header(
            "Authorization", "Basic %s" % b64_userpass
        )

        return urllib2.urlopen( req )

    def get_user( self, login = None ):
        if login is None:
            return AuthenticatedUser( self, {}, lazy = True )
        else:
            return NamedUser( self, { "login": login }, lazy = False )

    def get_organization( self, login ):
        return Organization( self, { "login": login }, lazy = False )
