# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import httplib
import base64
import urllib
import urlparse

try:
    import json
except ImportError: #pragma no cover: only for Python 2.5
    import simplejson as json #pragma no cover

import GithubException

class Requester:
    def __init__( self, login_or_token, password, base_url, timeout=10 ):
        if password is not None:
            login = login_or_token
            self.__authorizationHeader = "Basic " + base64.b64encode( login + ":" + password ).replace( '\n', '' )
        elif login_or_token is not None:
            token = login_or_token
            self.__authorizationHeader = "token " + token
        else:
            self.__authorizationHeader = None

        self.__base_url = base_url
        o = urlparse.urlparse( base_url )
        self.__hostname = o.hostname
        self.__port = o.port
        self.__prefix = o.path
        self.__timeout = timeout
        if o.scheme == "https":
            self.__connection_class = httplib.HTTPSConnection
        elif o.scheme == "http":
            self.__connection_class = httplib.HTTPConnection
        else:
            assert( False ) #pragma no cover
        self.rate_limiting = ( 5000, 5000 )

    def requestAndCheck( self, verb, url, parameters, input ):
        status, headers, output = self.requestRaw( verb, url, parameters, input )
        output = self.__structuredFromJson( output )
        if status >= 400:
            raise GithubException.GithubException( status, output )
        return headers, output

    def requestRaw( self, verb, url, parameters, input ):
        assert verb in [ "HEAD", "GET", "POST", "PATCH", "PUT", "DELETE" ]
        
        #URLs generated locally will be relative to __base_url
        #URLs returned from the server will start with __base_url
        if url.startswith( self.__base_url ):
            url = url[ len(self.__base_url): ]
        elif url.startswith( "/" ):
            url = url
        else:
            assert( False ) #pragma no cover
        
        headers = dict()
        if self.__authorizationHeader is not None:
            headers[ "Authorization" ] = self.__authorizationHeader

        cnx = self.__connection_class( host = self.__hostname, port = self.__port, strict = True, timeout = self.__timeout)
        cnx.request(
            verb,
            self.__completeUrl( url, parameters ),
            json.dumps( input ),
            headers
        )
        response = cnx.getresponse()

        status = response.status
        headers = dict( response.getheaders() )
        output = response.read()

        cnx.close()

        if "x-ratelimit-remaining" in headers and "x-ratelimit-limit" in headers:
            self.rate_limiting = ( int( headers[ "x-ratelimit-remaining" ] ), int( headers[ "x-ratelimit-limit" ] ) )

        # print verb, url, parameters, input, "==>", status, str( headers )[ :30 ], str( output )[ :30 ]
        return status, headers, output

    def __completeUrl( self, url, parameters ):
        if parameters is None or len( parameters ) == 0:
            return self.__prefix + url
        else:
            return self.__prefix + url + "?" + urllib.urlencode( parameters )

    def __structuredFromJson( self, data ):
        if len( data ) == 0:
            return None
        else:
            return json.loads( data )
