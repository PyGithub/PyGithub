from Requester import Requester
import GithubObjects.AuthenticatedUser
import GithubObjects.NamedUser
import GithubObjects.Organization
import GithubObjects.Gist

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
            attributes = {
                "url": "https://api.github.com/user",
                # "login": self.__login # @todo ?
            }
            return GithubObjects.AuthenticatedUser.AuthenticatedUser( self, attributes, lazy = True )
        else:
            attributes = {
                "url": "https://api.github.com/users/" + login,
                "login": login,
            }
            return GithubObjects.NamedUser.NamedUser( self, attributes, lazy = False )

    def get_organization( self, login ):
        attributes = {
                "url": "https://api.github.com/orgs/" + login,
                "login": login,
        }
        return GithubObjects.Organization.Organization( self, attributes, lazy = False )

    def get_gist( self, id ):
        return GithubObjects.Gist.Gist( self, { "id": id }, lazy = False )

    def get_gists( self ):
        return [
            GithubObjects.Gist.Gist( self, attributes, lazy = True )
            for attributes
            in self._dataRequest( "GET", "/gists/public", None, None )
        ]

    def _printDebug( self, *args ):
        if self.__debugFile is not None:
            self.__debugFile.write( " ".join( str( arg ) for arg in args ) + "\n" )
