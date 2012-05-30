# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import Gist
import Repository
import NamedUser
import Plan
import Organization
import UserKey
import Issue
import Event
import Authorization

class AuthenticatedUser( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )
        self.__completed = completion != LazyCompletion
        if completion == ImmediateCompletion:
            self.__complete() # pragma: no cover

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

    def add_to_emails( self, *emails ):
        assert all( isinstance( email, ( str, unicode ) ) for email in emails ), emails
        post_parameters = emails
        status, headers, data = self.__requester.request(
            "POST",
            "https://api.github.com/user" + "/emails",
            None,
            post_parameters
        )

    def add_to_following( self, following ):
        assert isinstance( following, NamedUser.NamedUser ), following
        status, headers, data = self.__requester.request(
            "PUT",
            "https://api.github.com/user" + "/following" + "/" + str( following._identity ),
            None,
            None
        )

    def add_to_watched( self, watched ):
        assert isinstance( watched, Repository.Repository ), watched
        status, headers, data = self.__requester.request(
            "PUT",
            "https://api.github.com/user" + "/watched" + "/" + str( watched._identity ),
            None,
            None
        )

    def create_authorization( self, scopes = DefaultValueForOptionalParameters, note = DefaultValueForOptionalParameters, note_url = DefaultValueForOptionalParameters ):
        if scopes is not DefaultValueForOptionalParameters:
            assert all( isinstance( element, ( str, unicode ) ) for element in scopes ), scopes
        if note is not DefaultValueForOptionalParameters:
            assert isinstance( note, ( str, unicode ) ), note
        if note_url is not DefaultValueForOptionalParameters:
            assert isinstance( note_url, ( str, unicode ) ), note_url
        post_parameters = dict()
        if scopes is not DefaultValueForOptionalParameters:
            post_parameters[ "scopes" ] = scopes
        if note is not DefaultValueForOptionalParameters:
            post_parameters[ "note" ] = note
        if note_url is not DefaultValueForOptionalParameters:
            post_parameters[ "note_url" ] = note_url
        status, headers, data = self.__requester.request(
            "POST",
            "https://api.github.com/authorizations",
            None,
            post_parameters
        )
        return Authorization.Authorization( self.__requester, data, completion = NoCompletion )

    def create_fork( self, repo ):
        assert isinstance( repo, Repository.Repository ), repo
        status, headers, data = self.__requester.request(
            "POST",
            "https://api.github.com/repos/" + str( repo.owner.login ) + "/" + str( repo.name ) + "/forks",
            None,
            None
        )
        return Repository.Repository( self.__requester, data, completion = NoCompletion )

    def create_gist( self, public, files, description = DefaultValueForOptionalParameters ):
        assert isinstance( public, bool ), public
        if description is not DefaultValueForOptionalParameters:
            assert isinstance( description, ( str, unicode ) ), description
        post_parameters = {
            "public": public,
            "files": files,
        }
        if description is not DefaultValueForOptionalParameters:
            post_parameters[ "description" ] = description
        status, headers, data = self.__requester.request(
            "POST",
            "https://api.github.com/gists",
            None,
            post_parameters
        )
        return Gist.Gist( self.__requester, data, completion = NoCompletion )

    def create_key( self, title, key ):
        assert isinstance( title, ( str, unicode ) ), title
        assert isinstance( key, ( str, unicode ) ), key
        post_parameters = {
            "title": title,
            "key": key,
        }
        status, headers, data = self.__requester.request(
            "POST",
            "https://api.github.com/user/keys",
            None,
            post_parameters
        )
        if self.__requester.isFailureStatus( status ):
            raise GithubException( status, data )
        return UserKey.UserKey( self.__requester, data, completion = NoCompletion )

    def create_repo( self, name, description = DefaultValueForOptionalParameters, homepage = DefaultValueForOptionalParameters, private = DefaultValueForOptionalParameters, has_issues = DefaultValueForOptionalParameters, has_wiki = DefaultValueForOptionalParameters, has_downloads = DefaultValueForOptionalParameters ):
        assert isinstance( name, ( str, unicode ) ), name
        if description is not DefaultValueForOptionalParameters:
            assert isinstance( description, ( str, unicode ) ), description
        if homepage is not DefaultValueForOptionalParameters:
            assert isinstance( homepage, ( str, unicode ) ), homepage
        if private is not DefaultValueForOptionalParameters:
            assert isinstance( private, bool ), private
        if has_issues is not DefaultValueForOptionalParameters:
            assert isinstance( has_issues, bool ), has_issues
        if has_wiki is not DefaultValueForOptionalParameters:
            assert isinstance( has_wiki, bool ), has_wiki
        if has_downloads is not DefaultValueForOptionalParameters:
            assert isinstance( has_downloads, bool ), has_downloads
        post_parameters = {
            "name": name,
        }
        if description is not DefaultValueForOptionalParameters:
            post_parameters[ "description" ] = description
        if homepage is not DefaultValueForOptionalParameters:
            post_parameters[ "homepage" ] = homepage
        if private is not DefaultValueForOptionalParameters:
            post_parameters[ "private" ] = private
        if has_issues is not DefaultValueForOptionalParameters:
            post_parameters[ "has_issues" ] = has_issues
        if has_wiki is not DefaultValueForOptionalParameters:
            post_parameters[ "has_wiki" ] = has_wiki
        if has_downloads is not DefaultValueForOptionalParameters:
            post_parameters[ "has_downloads" ] = has_downloads
        status, headers, data = self.__requester.request(
            "POST",
            "https://api.github.com/user" + "/repos",
            None,
            post_parameters
        )
        return Repository.Repository( self.__requester, data, completion = NoCompletion )

    def edit( self, name = DefaultValueForOptionalParameters, email = DefaultValueForOptionalParameters, blog = DefaultValueForOptionalParameters, company = DefaultValueForOptionalParameters, location = DefaultValueForOptionalParameters, hireable = DefaultValueForOptionalParameters, bio = DefaultValueForOptionalParameters ):
        if name is not DefaultValueForOptionalParameters:
            assert isinstance( name, ( str, unicode ) ), name
        if email is not DefaultValueForOptionalParameters:
            assert isinstance( email, ( str, unicode ) ), email
        if blog is not DefaultValueForOptionalParameters:
            assert isinstance( blog, ( str, unicode ) ), blog
        if company is not DefaultValueForOptionalParameters:
            assert isinstance( company, ( str, unicode ) ), company
        if location is not DefaultValueForOptionalParameters:
            assert isinstance( location, ( str, unicode ) ), location
        if hireable is not DefaultValueForOptionalParameters:
            assert isinstance( hireable, bool ), hireable
        if bio is not DefaultValueForOptionalParameters:
            assert isinstance( bio, ( str, unicode ) ), bio
        post_parameters = dict()
        if name is not DefaultValueForOptionalParameters:
            post_parameters[ "name" ] = name
        if email is not DefaultValueForOptionalParameters:
            post_parameters[ "email" ] = email
        if blog is not DefaultValueForOptionalParameters:
            post_parameters[ "blog" ] = blog
        if company is not DefaultValueForOptionalParameters:
            post_parameters[ "company" ] = company
        if location is not DefaultValueForOptionalParameters:
            post_parameters[ "location" ] = location
        if hireable is not DefaultValueForOptionalParameters:
            post_parameters[ "hireable" ] = hireable
        if bio is not DefaultValueForOptionalParameters:
            post_parameters[ "bio" ] = bio
        status, headers, data = self.__requester.request(
            "PATCH",
            "https://api.github.com/user",
            None,
            post_parameters
        )
        self.__useAttributes( data )

    def get_authorization( self, id ):
        assert isinstance( id, int ), id
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/authorizations" + "/" + str( id ),
            None,
            None
        )
        return Authorization.Authorization( self.__requester, data, completion = NoCompletion )

    def get_authorizations( self ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/authorizations",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Authorization.Authorization,
            self.__requester,
            headers,
            data
        )

    def get_emails( self ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/user" + "/emails",
            None,
            None
        )
        return data

    def get_events( self ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/events",
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
            "https://api.github.com/user" + "/followers",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self.__requester,
            headers,
            data
        )

    def get_following( self ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/user" + "/following",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self.__requester,
            headers,
            data
        )

    def get_gists( self ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/gists",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Gist.Gist,
            self.__requester,
            headers,
            data
        )

    def get_issues( self ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/issues",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Issue.Issue,
            self.__requester,
            headers,
            data
        )

    def get_key( self, id ):
        assert isinstance( id, int ), id
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/user/keys" + "/" + str( id ),
            None,
            None
        )
        return UserKey.UserKey( self.__requester, data, completion = NoCompletion )

    def get_keys( self ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/user/keys",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            UserKey.UserKey,
            self.__requester,
            headers,
            data
        )

    def get_organization_events( self, org ):
        assert isinstance( org, Organization.Organization ), org
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/users/" + str( self.login ) + "/events/orgs/" + str( org.login ),
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Event.Event,
            self.__requester,
            headers,
            data
        )

    def get_orgs( self ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/user" + "/orgs",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Organization.Organization,
            self.__requester,
            headers,
            data
        )

    def get_repo( self, name ):
        assert isinstance( name, ( str, unicode ) ), name
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/repos/" + str( self.login ) + "/" + str( name ),
            None,
            None
        )
        return Repository.Repository( self.__requester, data, completion = NoCompletion )

    def get_repos( self, type = DefaultValueForOptionalParameters, sort = DefaultValueForOptionalParameters, direction = DefaultValueForOptionalParameters ):
        if type is not DefaultValueForOptionalParameters:
            assert isinstance( type, ( str, unicode ) ), type
        if sort is not DefaultValueForOptionalParameters:
            assert isinstance( sort, ( str, unicode ) ), sort
        if direction is not DefaultValueForOptionalParameters:
            assert isinstance( direction, ( str, unicode ) ), direction
        url_parameters = dict()
        if type is not DefaultValueForOptionalParameters:
            url_parameters[ "type" ] = type
        if sort is not DefaultValueForOptionalParameters:
            url_parameters[ "sort" ] = sort
        if direction is not DefaultValueForOptionalParameters:
            url_parameters[ "direction" ] = direction
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/user" + "/repos",
            url_parameters,
            None
        )
        return PaginatedList.PaginatedList(
            Repository.Repository,
            self.__requester,
            headers,
            data
        )

    def get_starred_gists( self ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/gists/starred",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Gist.Gist,
            self.__requester,
            headers,
            data
        )

    def get_watched( self ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/user" + "/watched",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Repository.Repository,
            self.__requester,
            headers,
            data
        )

    def has_in_following( self, following ):
        assert isinstance( following, NamedUser.NamedUser ), following
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/user" + "/following" + "/" + str( following._identity ),
            None,
            None
        )
        return status == 204

    def has_in_watched( self, watched ):
        assert isinstance( watched, Repository.Repository ), watched
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/user" + "/watched" + "/" + str( watched._identity ),
            None,
            None
        )
        return status == 204

    def remove_from_emails( self, *emails ):
        assert all( isinstance( email, ( str, unicode ) ) for email in emails ), emails
        post_parameters = emails
        status, headers, data = self.__requester.request(
            "DELETE",
            "https://api.github.com/user" + "/emails",
            None,
            post_parameters
        )

    def remove_from_following( self, following ):
        assert isinstance( following, NamedUser.NamedUser ), following
        status, headers, data = self.__requester.request(
            "DELETE",
            "https://api.github.com/user" + "/following" + "/" + str( following._identity ),
            None,
            None
        )

    def remove_from_watched( self, watched ):
        assert isinstance( watched, Repository.Repository ), watched
        status, headers, data = self.__requester.request(
            "DELETE",
            "https://api.github.com/user" + "/watched" + "/" + str( watched._identity ),
            None,
            None
        )

    def __initAttributes( self ):
        self.__avatar_url = None
        self.__bio = None
        self.__blog = None
        self.__collaborators = None
        self.__company = None
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
            self.__complete() # pragma: no cover

    def __complete( self ): # pragma: no cover
        status, headers, data = self.__requester.request(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( data )
        self.__completed = True

    def __useAttributes( self, attributes ):
        if "avatar_url" in attributes and attributes[ "avatar_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "avatar_url" ], ( str, unicode ) ), attributes[ "avatar_url" ]
            self.__avatar_url = attributes[ "avatar_url" ]
        if "bio" in attributes and attributes[ "bio" ] is not None: # pragma no branch
            assert isinstance( attributes[ "bio" ], ( str, unicode ) ), attributes[ "bio" ]
            self.__bio = attributes[ "bio" ]
        if "blog" in attributes and attributes[ "blog" ] is not None: # pragma no branch
            assert isinstance( attributes[ "blog" ], ( str, unicode ) ), attributes[ "blog" ]
            self.__blog = attributes[ "blog" ]
        if "collaborators" in attributes and attributes[ "collaborators" ] is not None: # pragma no branch
            assert isinstance( attributes[ "collaborators" ], int ), attributes[ "collaborators" ]
            self.__collaborators = attributes[ "collaborators" ]
        if "company" in attributes and attributes[ "company" ] is not None: # pragma no branch
            assert isinstance( attributes[ "company" ], ( str, unicode ) ), attributes[ "company" ]
            self.__company = attributes[ "company" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self.__created_at = attributes[ "created_at" ]
        if "disk_usage" in attributes and attributes[ "disk_usage" ] is not None: # pragma no branch
            assert isinstance( attributes[ "disk_usage" ], int ), attributes[ "disk_usage" ]
            self.__disk_usage = attributes[ "disk_usage" ]
        if "email" in attributes and attributes[ "email" ] is not None: # pragma no branch
            assert isinstance( attributes[ "email" ], ( str, unicode ) ), attributes[ "email" ]
            self.__email = attributes[ "email" ]
        if "followers" in attributes and attributes[ "followers" ] is not None: # pragma no branch
            assert isinstance( attributes[ "followers" ], int ), attributes[ "followers" ]
            self.__followers = attributes[ "followers" ]
        if "following" in attributes and attributes[ "following" ] is not None: # pragma no branch
            assert isinstance( attributes[ "following" ], int ), attributes[ "following" ]
            self.__following = attributes[ "following" ]
        if "gravatar_id" in attributes and attributes[ "gravatar_id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "gravatar_id" ], ( str, unicode ) ), attributes[ "gravatar_id" ]
            self.__gravatar_id = attributes[ "gravatar_id" ]
        if "hireable" in attributes and attributes[ "hireable" ] is not None: # pragma no branch
            assert isinstance( attributes[ "hireable" ], bool ), attributes[ "hireable" ]
            self.__hireable = attributes[ "hireable" ]
        if "html_url" in attributes and attributes[ "html_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "html_url" ], ( str, unicode ) ), attributes[ "html_url" ]
            self.__html_url = attributes[ "html_url" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self.__id = attributes[ "id" ]
        if "location" in attributes and attributes[ "location" ] is not None: # pragma no branch
            assert isinstance( attributes[ "location" ], ( str, unicode ) ), attributes[ "location" ]
            self.__location = attributes[ "location" ]
        if "login" in attributes and attributes[ "login" ] is not None: # pragma no branch
            assert isinstance( attributes[ "login" ], ( str, unicode ) ), attributes[ "login" ]
            self.__login = attributes[ "login" ]
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self.__name = attributes[ "name" ]
        if "owned_private_repos" in attributes and attributes[ "owned_private_repos" ] is not None: # pragma no branch
            assert isinstance( attributes[ "owned_private_repos" ], int ), attributes[ "owned_private_repos" ]
            self.__owned_private_repos = attributes[ "owned_private_repos" ]
        if "plan" in attributes and attributes[ "plan" ] is not None: # pragma no branch
            assert isinstance( attributes[ "plan" ], dict ), attributes[ "plan" ]
            self.__plan = Plan.Plan( self.__requester, attributes[ "plan" ], completion = LazyCompletion )
        if "private_gists" in attributes and attributes[ "private_gists" ] is not None: # pragma no branch
            assert isinstance( attributes[ "private_gists" ], int ), attributes[ "private_gists" ]
            self.__private_gists = attributes[ "private_gists" ]
        if "public_gists" in attributes and attributes[ "public_gists" ] is not None: # pragma no branch
            assert isinstance( attributes[ "public_gists" ], int ), attributes[ "public_gists" ]
            self.__public_gists = attributes[ "public_gists" ]
        if "public_repos" in attributes and attributes[ "public_repos" ] is not None: # pragma no branch
            assert isinstance( attributes[ "public_repos" ], int ), attributes[ "public_repos" ]
            self.__public_repos = attributes[ "public_repos" ]
        if "total_private_repos" in attributes and attributes[ "total_private_repos" ] is not None: # pragma no branch
            assert isinstance( attributes[ "total_private_repos" ], int ), attributes[ "total_private_repos" ]
            self.__total_private_repos = attributes[ "total_private_repos" ]
        if "type" in attributes and attributes[ "type" ] is not None: # pragma no branch
            assert isinstance( attributes[ "type" ], ( str, unicode ) ), attributes[ "type" ]
            self.__type = attributes[ "type" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self.__url = attributes[ "url" ]
