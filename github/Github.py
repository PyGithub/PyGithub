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
            status, headers, data = self.__requester.request(
                "GET",
                "https://api.github.com/users/" + login,
                None,
                None
            )
            NamedUser.NamedUser._checkStatus( status, data )
            return NamedUser.NamedUser( self.__requester, data, completed = True )

    def get_organization( self, login ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/orgs/" + login,
            None,
            None
        )
        Organization.Organization._checkStatus( status, data )
        return Organization.Organization( self.__requester, data, completed = True )

    def get_gist( self, id ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/gists/" + str( id ),
            None,
            None
        )
        Gist.Gist._checkStatus( status, data )
        return Gist.Gist( self.__requester, data, completed = True )

    def get_gists( self ):
        status, headers, data = self.__requester.request( "GET", "https://api.github.com/gists/public", None, None )
        Gist.Gist._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Gist.Gist,
            self.__requester,
            headers,
            data
        )
