import httplib
import json
import base64

from GithubObjects import *

class UnknownGithubObject( Exception ):
    pass

class Github:
    def __init__( self, login, password ):
        self.__login = login
        self.__password = password

    def _dataRequest( self, verb, url, parameters, data ):
        status, headers, data = self.__rawRequest( verb, url, parameters, data )
        if 200 <= status < 300:
            return data
        else:
            raise UnknownGithubObject()

    def _statusRequest( self, verb, url, parameters, data ):
        status, headers, data = self.__rawRequest( verb, url, parameters, data )
        return status

    def __rawRequest( self, verb, url, parameters, input ):
        assert verb in [ "HEAD", "GET", "POST", "PATCH", "PUT", "DELETE" ]

        b64_userpass = base64.b64encode( '%s:%s' % ( self.__login, self.__password ) )
        b64_userpass = b64_userpass.replace( '\n', '' )

        input = json.dumps( input )

        cnx = httplib.HTTPSConnection( "api.github.com", strict = True )
        cnx.request( verb, url, input, { "Authorization" : "Basic " + b64_userpass } )
        response = cnx.getresponse()

        status = response.status
        headers = dict( response.getheaders() )
        output = response.read()
        if len( output ) == 0:
            output = None
        else:
            output = json.loads( output )
        cnx.close()

        # print verb, url, input, "==>", status, str( headers )[ :30 ], str( output )[ :30 ]
        return status, headers, output

    def get_user( self, login = None ):
        if login is None:
            return AuthenticatedUser( self, {}, lazy = True )
        else:
            return NamedUser( self, { "login": login }, lazy = False )

    def get_organization( self, login ):
        return Organization( self, { "login": login }, lazy = False )
