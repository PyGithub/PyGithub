from Requester import Requester
import GithubObjects.AuthenticatedUser
import GithubObjects.NamedUser
import GithubObjects.Organization
import GithubObjects.Gist

class Github:
    def __init__( self, login, password ):
        self.__requester = Requester( login, password )

    def get_user( self, login = None ):
        if login is None:
            attributes = {
                "url": "https://api.github.com/user", # @todo Erf, this url is replaced by /users/login when __complete is called...
                # "login": self.__login # @todo ?
            }
            return GithubObjects.AuthenticatedUser.AuthenticatedUser( self.__requester, attributes, lazy = True )
        else:
            attributes = {
                "url": "https://api.github.com/users/" + login,
                "login": login,
            }
            return GithubObjects.NamedUser.NamedUser( self.__requester, attributes, lazy = False )

    def get_organization( self, login ):
        attributes = {
                "url": "https://api.github.com/orgs/" + login,
                "login": login,
        }
        return GithubObjects.Organization.Organization( self.__requester, attributes, lazy = False )

    def get_gist( self, id ):
        return GithubObjects.Gist.Gist( self.__requester, { "id": id }, lazy = False )

    def get_gists( self ):
        status, headers, data = self.__requester.request( "GET", "/gists/public", None, None )
        return [
            GithubObjects.Gist.Gist( self.__requester, attributes, lazy = True )
            for attributes
            in data
        ]
