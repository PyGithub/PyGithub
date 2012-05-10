import httplib
import json
import base64
import urllib

class UnknownGithubObject( Exception ):
    pass

class Requester:
    def __init__( self, login, password ):
        self.__authorizationHeader = "Basic " + base64.b64encode( login + ":" + password ).replace( '\n', '' )

    def request( self, verb, url, parameters, input ):
        assert verb in [ "HEAD", "GET", "POST", "PATCH", "PUT", "DELETE" ]
        assert url.startswith( "https://api.github.com" )
        url = url[ len( "https://api.github.com" ) : ]

        cnx = httplib.HTTPSConnection( "api.github.com", strict = True )
        cnx.request(
            verb,
            self.__completeUrl( url, parameters ),
            json.dumps( input ),
            { "Authorization" : self.__authorizationHeader }
        )
        response = cnx.getresponse()

        status = response.status
        headers = dict( response.getheaders() )
        output = self.__structuredFromJson( response.read() )

        cnx.close()

        # print verb, url, parameters, input, "==>", status, str( headers )[ :30 ], str( output )[ :30 ]
        return status, headers, output

    def __completeUrl( self, url, parameters ):
        if parameters is None or len( parameters ) == 0:
            return url
        else:
            return url + "?" + urllib.urlencode( parameters )

    def __structuredFromJson( self, data ):
        if len( data ) == 0:
            return None
        else:
            return json.loads( data )
