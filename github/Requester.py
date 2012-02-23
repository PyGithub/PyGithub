import httplib
import json
import base64
import urllib

class UnknownGithubObject( Exception ):
    pass

class Requester:
    def __init__( self, login, password ):
        self.__authorizationHeader = "Basic " + base64.b64encode( login + ":" + password ).replace( '\n', '' )

    def dataRequest( self, verb, url, parameters, input ):
        if parameters is None:
            parameters = dict()

        headers, output = self.__statusCheckedRequest( verb, url, parameters, input )

        page = 2
        while "link" in headers and "next" in headers[ "link" ]:
            parameters[ "page" ] = page
            headers, newOutput = self.__statusCheckedRequest( verb, url, parameters, input )
            output += newOutput
            page += 1

        return output

    def __statusCheckedRequest( self, verb, url, parameters, input ):
        status, headers, output = self.__rawRequest( verb, url, parameters, input )
        if status < 200 or status >= 300:
            ### @todo Be specific (403 is not the same thing as 404!)
            raise UnknownGithubObject()
        return headers, output

    def statusRequest( self, verb, url, parameters, input ):
        status, headers, output = self.__rawRequest( verb, url, parameters, input )
        return status

    def __rawRequest( self, verb, url, parameters, input ):
        assert verb in [ "HEAD", "GET", "POST", "PATCH", "PUT", "DELETE" ]

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
        output = self.__strucutredFromJson( response.read() )

        cnx.close()

        # print verb, url, input, "==>", status, str( headers )[ :30 ], str( output )[ :30 ]
        return status, headers, output

    def __completeUrl( self, url, parameters ):
        if parameters is None or len( parameters ) == 0:
            return url
        else:
            return url + "?" + urllib.urlencode( parameters )

    def __strucutredFromJson( self, data ):
        if len( data ) == 0:
            return None
        else:
            return json.loads( data )
