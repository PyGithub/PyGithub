import httplib
import json
import base64

class UnknownGithubObject( Exception ):
    pass

class Requester:
    def __init__( self, login, password ):
        self.__login = login
        self.__password = password

    def dataRequest( self, verb, url, parameters, input ):
        status, headers, output = self.__rawRequest( verb, url, parameters, input )
        if 200 <= status < 300:
            page = 2
            while "link" in headers and "next" in headers[ "link" ]:
                if parameters is None:
                    parameters = dict()
                parameters[ "page" ] = page
                newStatus, newHeaders, newOutput = self.__rawRequest( verb, url, parameters, input )
                if 200 <= newStatus < 300:
                    headers = newHeaders
                    page += 1
                    output += newOutput
                else:
                    raise UnknownGithubObject()
            return output
        else:
            raise UnknownGithubObject()

    def statusRequest( self, verb, url, parameters, input ):
        status, headers, output = self.__rawRequest( verb, url, parameters, input )
        return status

    def __rawRequest( self, verb, url, parameters, input ):
        assert verb in [ "HEAD", "GET", "POST", "PATCH", "PUT", "DELETE" ]

        b64_userpass = base64.b64encode( '%s:%s' % ( self.__login, self.__password ) )
        b64_userpass = b64_userpass.replace( '\n', '' )

        if parameters is not None and len( parameters ) != 0:
            url += "?" + "&".join( str( key ) + "=" + str( value ) for key, value in parameters.iteritems() )

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
