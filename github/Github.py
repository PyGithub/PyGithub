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

    def _rawRequest( self, verb, url, data = None ):
        assert( verb in [ "HEAD", "GET", "POST", "PATCH", "PUT", "DELETE" ] )

        # print verb, url, data

        req = Github._Request( verb, "https://api.github.com" + url, json.dumps( data ) )
        b64_userpass = base64.b64encode( '%s:%s' % ( self.__login, self.__password ) )
        b64_userpass = b64_userpass.replace( '\n', '' )
        req.add_header(
            "Authorization", "Basic %s" % b64_userpass
        )

        return json.load( urllib2.urlopen( req ) )

    def get_user( self, login = None ):
        if login is None:
            return AuthenticatedUser( self, {}, lazy = True )
        else:
            return NamedUser( self, { "login": login }, lazy = False )

    def get_organization( self, login ):
        return Organization( self, { "login": login }, lazy = False )
