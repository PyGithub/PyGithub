import GithubException

class BasicGithubObject( object ):
    def __init__( self, requester, attributes, completed ): ### 'completed' may be removed if I find a way
        self._requester = requester
        self._initAttributes()
        self._useAttributes( attributes )

    def _request( self, verb, url, parameters, input ):
        return self._requester.request( verb, url, parameters, input )

    def _parentUrl( self, url ):
        return "/".join( url.split( "/" )[ : -1 ] )

    def _checkStatus( self, status, data ):
        if status >= 400: # pragma no branch
            raise GithubException.GithubException( status, data ) # pragma no cover

class GithubObject( BasicGithubObject ):
    def __init__( self, requester, attributes, completed ):
        BasicGithubObject.__init__( self, requester, attributes, completed )
        self.__completed = completed

    def _completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete() # pragma: no cover

    def __complete( self ): # pragma: no cover
        status, headers, data = self._request(
            "GET",
            self._url,
            None,
            None
        )
        self._useAttributes( data )
        self._completed = True
