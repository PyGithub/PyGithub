# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import Gist
import Repository
import NamedUser
import Plan
import Organization
import Event

class NamedUser( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__completed = completion != LazyCompletion
        self.__initAttributes()
        self.__useAttributes( attributes )
        if completion == ImmediateCompletion:
            self.__complete()

    @property
    def avatar_url( self ):
        self.__completeIfNeeded( self.__avatar_url )
        return self.__avatar_url

    @property
    def bio( self ):
        self.__completeIfNeeded( self.__bio )
        return self.__bio

    @property
    def blog( self ):
        self.__completeIfNeeded( self.__blog )
        return self.__blog

    @property
    def collaborators( self ):
        self.__completeIfNeeded( self.__collaborators )
        return self.__collaborators

    @property
    def company( self ):
        self.__completeIfNeeded( self.__company )
        return self.__company

    @property
    def contributions( self ):
        self.__completeIfNeeded( self.__contributions )
        return self.__contributions

    @property
    def created_at( self ):
        self.__completeIfNeeded( self.__created_at )
        return self.__created_at

    @property
    def disk_usage( self ):
        self.__completeIfNeeded( self.__disk_usage )
        return self.__disk_usage

    @property
    def email( self ):
        self.__completeIfNeeded( self.__email )
        return self.__email

    @property
    def followers( self ):
        self.__completeIfNeeded( self.__followers )
        return self.__followers

    @property
    def following( self ):
        self.__completeIfNeeded( self.__following )
        return self.__following

    @property
    def gravatar_id( self ):
        self.__completeIfNeeded( self.__gravatar_id )
        return self.__gravatar_id

    @property
    def hireable( self ):
        self.__completeIfNeeded( self.__hireable )
        return self.__hireable

    @property
    def html_url( self ):
        self.__completeIfNeeded( self.__html_url )
        return self.__html_url

    @property
    def id( self ):
        self.__completeIfNeeded( self.__id )
        return self.__id

    @property
    def location( self ):
        self.__completeIfNeeded( self.__location )
        return self.__location

    @property
    def login( self ):
        self.__completeIfNeeded( self.__login )
        return self.__login

    @property
    def name( self ):
        self.__completeIfNeeded( self.__name )
        return self.__name

    @property
    def owned_private_repos( self ):
        self.__completeIfNeeded( self.__owned_private_repos )
        return self.__owned_private_repos

    @property
    def plan( self ):
        self.__completeIfNeeded( self.__plan )
        return self.__plan

    @property
    def private_gists( self ):
        self.__completeIfNeeded( self.__private_gists )
        return self.__private_gists

    @property
    def public_gists( self ):
        self.__completeIfNeeded( self.__public_gists )
        return self.__public_gists

    @property
    def public_repos( self ):
        self.__completeIfNeeded( self.__public_repos )
        return self.__public_repos

    @property
    def total_private_repos( self ):
        self.__completeIfNeeded( self.__total_private_repos )
        return self.__total_private_repos

    @property
    def type( self ):
        self.__completeIfNeeded( self.__type )
        return self.__type

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def create_gist( self, public, files, description = DefaultValueForOptionalParameters ):
        post_parameters = {
            "public": public,
            "files": files,
        }
        if description is not DefaultValueForOptionalParameters:
            post_parameters[ "description" ] = description
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/gists",
            None,
            post_parameters
        )
        return Gist.Gist( self.__requester, data, completion = NoCompletion )

    def get_events( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/events",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Event.Event,
            self.__requester,
            headers,
            data
        )

    def get_followers( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/followers",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            NamedUser,
            self.__requester,
            headers,
            data
        )

    def get_following( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/following",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            NamedUser,
            self.__requester,
            headers,
            data
        )

    def get_gists( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/gists",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Gist.Gist,
            self.__requester,
            headers,
            data
        )

    def get_orgs( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/orgs",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Organization.Organization,
            self.__requester,
            headers,
            data
        )

    def get_public_events( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/events/public",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Event.Event,
            self.__requester,
            headers,
            data
        )

    def get_public_received_events( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/received_events/public",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Event.Event,
            self.__requester,
            headers,
            data
        )

    def get_received_events( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/received_events",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Event.Event,
            self.__requester,
            headers,
            data
        )

    def get_repo( self, name ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/repos/" + str( self.login ) + "/" + str( name ),
            None,
            None
        )
        return Repository.Repository( self.__requester, data, completion = NoCompletion )

    def get_repos( self, type = DefaultValueForOptionalParameters ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/repos",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Repository.Repository,
            self.__requester,
            headers,
            data
        )

    def get_watched( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/watched",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Repository.Repository,
            self.__requester,
            headers,
            data
        )

    # @todo Remove '_identity' from the normalized json description
    @property
    def _identity( self ):
        return str( self.login )

    def __initAttributes( self ):
        self.__avatar_url = None
        self.__bio = None
        self.__blog = None
        self.__collaborators = None
        self.__company = None
        self.__contributions = None
        self.__created_at = None
        self.__disk_usage = None
        self.__email = None
        self.__followers = None
        self.__following = None
        self.__gravatar_id = None
        self.__hireable = None
        self.__html_url = None
        self.__id = None
        self.__location = None
        self.__login = None
        self.__name = None
        self.__owned_private_repos = None
        self.__plan = None
        self.__private_gists = None
        self.__public_gists = None
        self.__public_repos = None
        self.__total_private_repos = None
        self.__type = None
        self.__url = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete()

    def __complete( self ):
        status, headers, data = self.__requester.request(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( data )
        self.__completed = True

    def __useAttributes( self, attributes ):
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "avatar_url", "bio", "blog", "collaborators", "company", "contributions", "created_at", "disk_usage", "email", "followers", "following", "gravatar_id", "hireable", "html_url", "id", "location", "login", "name", "owned_private_repos", "plan", "private_gists", "public_gists", "public_repos", "total_private_repos", "type", "url", ], attribute
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "avatar_url" in attributes and attributes[ "avatar_url" ] is not None:
            assert isinstance( attributes[ "avatar_url" ], ( str, unicode ) )
            self.__avatar_url = attributes[ "avatar_url" ]
        if "bio" in attributes and attributes[ "bio" ] is not None:
            assert isinstance( attributes[ "bio" ], ( str, unicode ) )
            self.__bio = attributes[ "bio" ]
        if "blog" in attributes and attributes[ "blog" ] is not None:
            assert isinstance( attributes[ "blog" ], ( str, unicode ) )
            self.__blog = attributes[ "blog" ]
        if "collaborators" in attributes and attributes[ "collaborators" ] is not None:
            assert isinstance( attributes[ "collaborators" ], int )
            self.__collaborators = attributes[ "collaborators" ]
        if "company" in attributes and attributes[ "company" ] is not None:
            assert isinstance( attributes[ "company" ], ( str, unicode ) )
            self.__company = attributes[ "company" ]
        if "contributions" in attributes and attributes[ "contributions" ] is not None:
            assert isinstance( attributes[ "contributions" ], int )
            self.__contributions = attributes[ "contributions" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None:
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) )
            self.__created_at = attributes[ "created_at" ]
        if "disk_usage" in attributes and attributes[ "disk_usage" ] is not None:
            assert isinstance( attributes[ "disk_usage" ], int )
            self.__disk_usage = attributes[ "disk_usage" ]
        if "email" in attributes and attributes[ "email" ] is not None:
            assert isinstance( attributes[ "email" ], ( str, unicode ) )
            self.__email = attributes[ "email" ]
        if "followers" in attributes and attributes[ "followers" ] is not None:
            assert isinstance( attributes[ "followers" ], int )
            self.__followers = attributes[ "followers" ]
        if "following" in attributes and attributes[ "following" ] is not None:
            assert isinstance( attributes[ "following" ], int )
            self.__following = attributes[ "following" ]
        if "gravatar_id" in attributes and attributes[ "gravatar_id" ] is not None:
            assert isinstance( attributes[ "gravatar_id" ], ( str, unicode ) )
            self.__gravatar_id = attributes[ "gravatar_id" ]
        if "hireable" in attributes and attributes[ "hireable" ] is not None:
            assert isinstance( attributes[ "hireable" ], bool )
            self.__hireable = attributes[ "hireable" ]
        if "html_url" in attributes and attributes[ "html_url" ] is not None:
            assert isinstance( attributes[ "html_url" ], ( str, unicode ) )
            self.__html_url = attributes[ "html_url" ]
        if "id" in attributes and attributes[ "id" ] is not None:
            assert isinstance( attributes[ "id" ], int )
            self.__id = attributes[ "id" ]
        if "location" in attributes and attributes[ "location" ] is not None:
            assert isinstance( attributes[ "location" ], ( str, unicode ) )
            self.__location = attributes[ "location" ]
        if "login" in attributes and attributes[ "login" ] is not None:
            assert isinstance( attributes[ "login" ], ( str, unicode ) )
            self.__login = attributes[ "login" ]
        if "name" in attributes and attributes[ "name" ] is not None:
            assert isinstance( attributes[ "name" ], ( str, unicode ) )
            self.__name = attributes[ "name" ]
        if "owned_private_repos" in attributes and attributes[ "owned_private_repos" ] is not None:
            assert isinstance( attributes[ "owned_private_repos" ], int )
            self.__owned_private_repos = attributes[ "owned_private_repos" ]
        if "plan" in attributes and attributes[ "plan" ] is not None:
            assert isinstance( attributes[ "plan" ], dict )
            self.__plan = Plan.Plan( self.__requester, attributes[ "plan" ], completion = LazyCompletion )
        if "private_gists" in attributes and attributes[ "private_gists" ] is not None:
            assert isinstance( attributes[ "private_gists" ], int )
            self.__private_gists = attributes[ "private_gists" ]
        if "public_gists" in attributes and attributes[ "public_gists" ] is not None:
            assert isinstance( attributes[ "public_gists" ], int )
            self.__public_gists = attributes[ "public_gists" ]
        if "public_repos" in attributes and attributes[ "public_repos" ] is not None:
            assert isinstance( attributes[ "public_repos" ], int )
            self.__public_repos = attributes[ "public_repos" ]
        if "total_private_repos" in attributes and attributes[ "total_private_repos" ] is not None:
            assert isinstance( attributes[ "total_private_repos" ], int )
            self.__total_private_repos = attributes[ "total_private_repos" ]
        if "type" in attributes and attributes[ "type" ] is not None:
            assert isinstance( attributes[ "type" ], ( str, unicode ) )
            self.__type = attributes[ "type" ]
        if "url" in attributes and attributes[ "url" ] is not None:
            assert isinstance( attributes[ "url" ], ( str, unicode ) )
            self.__url = attributes[ "url" ]
