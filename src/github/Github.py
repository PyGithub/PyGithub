from Requester import Requester
import AuthenticatedUser
import NamedUser
import Organization
import Gist
import PaginatedList
from GithubObject import LazyCompletion, ImmediateCompletion

class Github( object ):
    def __init__( self, login_or_token = None, password = None ):
        self.__requester = Requester( login_or_token, password )

    @property
    def rate_limiting( self ):
        return self.__requester.rate_limiting

    def get_user( self, login = None ):
        if login is None:
            attributes = {
                "url": "https://api.github.com/user", # @todo Erf, this url is replaced by /users/login when __complete is called...
                # "login": self.__login # @todo ?
            }
            return AuthenticatedUser.AuthenticatedUser( self.__requester, attributes, completion = LazyCompletion )
        else:
            attributes = {
                "url": "https://api.github.com/users/" + login,
                "login": login,
            }
            return NamedUser.NamedUser( self.__requester, attributes, completion = ImmediateCompletion )

    def get_organization( self, login ):
        attributes = {
                "url": "https://api.github.com/orgs/" + login,
                "login": login,
        }
        return Organization.Organization( self.__requester, attributes, completion = ImmediateCompletion )

    def get_gist( self, id ):
        attributes = {
                "url": "https://api.github.com/gists/" + str( id ),
                "id": id,
        }
        return Gist.Gist( self.__requester, attributes, completion = ImmediateCompletion )

    def get_gists( self ):
        status, headers, data = self.__requester.request( "GET", "https://api.github.com/gists/public", None )
        return PaginatedList.PaginatedList(
            Gist.Gist,
            self.__requester,
            headers,
            data
        )
