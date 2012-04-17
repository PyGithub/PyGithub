from Requester import Requester
from GithubObjects import *

class Github:
    def __init__( self, login, password, debugFile = None ):
        self.__requester = Requester( login, password )
        self.__debugFile = debugFile

    def _dataRequest( self, verb, url, parameters, data ):
        return self.__requester.dataRequest( verb, url, parameters, data )

    def _statusRequest( self, verb, url, parameters, data ):
        return self.__requester.statusRequest( verb, url, parameters, data )

    def get_user( self, login = None ):
        if login is None:
            return AuthenticatedUser( self, {}, lazy = True )
        else:
            return NamedUser( self, { "login": login }, lazy = False )

    def get_organization( self, login ):
        return Organization( self, { "login": login }, lazy = False )

    def get_gist( self, id ):
        return Gist( self, { "id": id }, lazy = False )

    def get_gists( self ):
        return [
            Gist( self, attributes, lazy = True )
            for attributes
            in self._dataRequest( "GET", "/gists/public", None, None )
        ]

    def _printDebug( self, *args ):
        if self.__debugFile is not None:
            self.__debugFile.write( " ".join( str( arg ) for arg in args ) + "\n" )
