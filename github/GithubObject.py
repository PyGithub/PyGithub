import GithubException

class _NotSetType:
    pass
NotSet = _NotSetType()

class BasicGithubObject( object ):
    def __init__( self, requester, attributes, completed ): ### 'completed' may be removed if I find a way
        self._requester = requester
        self._initAttributes()
        self._useAttributes( attributes )

    @staticmethod
    def _parentUrl( url ):
        return "/".join( url.split( "/" )[ : -1 ] )

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
        headers, data = self._requester.requestAndCheck(
            "GET",
            self._url,
            None,
            None
        )
        self._useAttributes( data )
        self._completed = True
