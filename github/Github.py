from Requester import Requester
import AuthenticatedUser
import NamedUser
import Organization
import Gist
import PaginatedList

class Github( object ):
    def __init__( self, login_or_token = None, password = None ):
        self.__requester = Requester( login_or_token, password )

    @property
    def rate_limiting( self ):
        return self.__requester.rate_limiting

    def get_user( self, login = None ):
        if login is None:
            return AuthenticatedUser.AuthenticatedUser( self.__requester, { "url": "https://api.github.com/user" }, completed = False )
        else:
            headers, data = self.__requester.requestAndCheck(
                "GET",
                "https://api.github.com/users/" + login,
                None,
                None
            )
            return NamedUser.NamedUser( self.__requester, data, completed = True )

    def get_organization( self, login ):
        headers, data = self.__requester.requestAndCheck(
            "GET",
            "https://api.github.com/orgs/" + login,
            None,
            None
        )
        return Organization.Organization( self.__requester, data, completed = True )

    def get_gist( self, id ):
        headers, data = self.__requester.requestAndCheck(
            "GET",
            "https://api.github.com/gists/" + str( id ),
            None,
            None
        )
        return Gist.Gist( self.__requester, data, completed = True )

    def get_gists( self ):
        headers, data = self.__requester.requestAndCheck( "GET", "https://api.github.com/gists/public", None, None )
        return PaginatedList.PaginatedList(
            Gist.Gist,
            self.__requester,
            headers,
            data
        )
