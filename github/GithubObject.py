import GithubException

class _NotSetType:
    pass
NotSet = _NotSetType()

class BasicGithubObject( object ):
    def __init__( self, requester, attributes, completed ): ### 'completed' may be removed if I find a way
        self._requester = requester
        self._initAttributes()
        self._useAttributes( attributes )

    def _request( self, verb, url, parameters, input ):
        return self._requester.request( verb, url, parameters, input )

    @staticmethod
    def _parentUrl( url ):
        return "/".join( url.split( "/" )[ : -1 ] )

    @staticmethod
    def _checkStatus( status, data ):
        if status >= 400:
            raise GithubException.GithubException( status, data )

    @staticmethod
    def _NoneIfNotSet( value ):
        if value is NotSet:
            return None
        else:
            return value

class GithubObject( BasicGithubObject ):
    def __init__( self, requester, attributes, completed ):
        BasicGithubObject.__init__( self, requester, attributes, completed )
        self.__completed = completed

    def _completeIfNotSet( self, value ):
        if not self.__completed and value is NotSet:
            self.__complete()

    def __complete( self ):
        status, headers, data = self._request(
            "GET",
            self._url,
            None,
            None
        )
        self._checkStatus( status, data )
        self._useAttributes( data )
        self._completed = True
