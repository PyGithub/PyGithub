# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
import PaginatedList
##########
import Gist
import Repository
import NamedUser
import Plan
import Organization
import UserKey
import Issue
import Event
import Authorization

class AuthenticatedUser( GithubObject.GithubObject ):
    @property
    def avatar_url( self ):
        self._completeIfNotSet( self._avatar_url )
        return self._NoneIfNotSet( self._avatar_url )

    @property
    def bio( self ):
        self._completeIfNotSet( self._bio )
        return self._NoneIfNotSet( self._bio )

    @property
    def blog( self ):
        self._completeIfNotSet( self._blog )
        return self._NoneIfNotSet( self._blog )

    @property
    def collaborators( self ):
        self._completeIfNotSet( self._collaborators )
        return self._NoneIfNotSet( self._collaborators )

    @property
    def company( self ):
        self._completeIfNotSet( self._company )
        return self._NoneIfNotSet( self._company )

    @property
    def created_at( self ):
        self._completeIfNotSet( self._created_at )
        return self._NoneIfNotSet( self._created_at )

    @property
    def disk_usage( self ):
        self._completeIfNotSet( self._disk_usage )
        return self._NoneIfNotSet( self._disk_usage )

    @property
    def email( self ):
        self._completeIfNotSet( self._email )
        return self._NoneIfNotSet( self._email )

    @property
    def followers( self ):
        self._completeIfNotSet( self._followers )
        return self._NoneIfNotSet( self._followers )

    @property
    def following( self ):
        self._completeIfNotSet( self._following )
        return self._NoneIfNotSet( self._following )

    @property
    def gravatar_id( self ):
        self._completeIfNotSet( self._gravatar_id )
        return self._NoneIfNotSet( self._gravatar_id )

    @property
    def hireable( self ):
        self._completeIfNotSet( self._hireable )
        return self._NoneIfNotSet( self._hireable )

    @property
    def html_url( self ):
        self._completeIfNotSet( self._html_url )
        return self._NoneIfNotSet( self._html_url )

    @property
    def id( self ):
        self._completeIfNotSet( self._id )
        return self._NoneIfNotSet( self._id )

    @property
    def location( self ):
        self._completeIfNotSet( self._location )
        return self._NoneIfNotSet( self._location )

    @property
    def login( self ):
        self._completeIfNotSet( self._login )
        return self._NoneIfNotSet( self._login )

    @property
    def name( self ):
        self._completeIfNotSet( self._name )
        return self._NoneIfNotSet( self._name )

    @property
    def owned_private_repos( self ):
        self._completeIfNotSet( self._owned_private_repos )
        return self._NoneIfNotSet( self._owned_private_repos )

    @property
    def plan( self ):
        self._completeIfNotSet( self._plan )
        return self._NoneIfNotSet( self._plan )

    @property
    def private_gists( self ):
        self._completeIfNotSet( self._private_gists )
        return self._NoneIfNotSet( self._private_gists )

    @property
    def public_gists( self ):
        self._completeIfNotSet( self._public_gists )
        return self._NoneIfNotSet( self._public_gists )

    @property
    def public_repos( self ):
        self._completeIfNotSet( self._public_repos )
        return self._NoneIfNotSet( self._public_repos )

    @property
    def total_private_repos( self ):
        self._completeIfNotSet( self._total_private_repos )
        return self._NoneIfNotSet( self._total_private_repos )

    @property
    def type( self ):
        self._completeIfNotSet( self._type )
        return self._NoneIfNotSet( self._type )

    @property
    def url( self ):
        self._completeIfNotSet( self._url )
        return self._NoneIfNotSet( self._url )

    def add_to_emails( self, *emails ):
        assert all( isinstance( email, ( str, unicode ) ) for email in emails ), emails
        post_parameters = emails
        status, headers, data = self._request(
            "POST",
            "https://api.github.com/user/emails",
            None,
            post_parameters
        )
        self._checkStatus( status, data )

    def add_to_following( self, following ):
        assert isinstance( following, NamedUser.NamedUser ), following
        status, headers, data = self._request(
            "PUT",
            "https://api.github.com/user/following/" + str( following._identity ),
            None,
            None
        )
        self._checkStatus( status, data )

    def add_to_watched( self, watched ):
        assert isinstance( watched, Repository.Repository ), watched
        status, headers, data = self._request(
            "PUT",
            "https://api.github.com/user/watched/" + str( watched._identity ),
            None,
            None
        )
        self._checkStatus( status, data )

    def create_authorization( self, scopes = GithubObject.NotSet, note = GithubObject.NotSet, note_url = GithubObject.NotSet ):
        if scopes is not GithubObject.NotSet:
            assert all( isinstance( element, ( str, unicode ) ) for element in scopes ), scopes
        if note is not GithubObject.NotSet:
            assert isinstance( note, ( str, unicode ) ), note
        if note_url is not GithubObject.NotSet:
            assert isinstance( note_url, ( str, unicode ) ), note_url
        post_parameters = dict()
        if scopes is not GithubObject.NotSet:
            post_parameters[ "scopes" ] = scopes
        if note is not GithubObject.NotSet:
            post_parameters[ "note" ] = note
        if note_url is not GithubObject.NotSet:
            post_parameters[ "note_url" ] = note_url
        status, headers, data = self._request(
            "POST",
            "https://api.github.com/authorizations",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return Authorization.Authorization( self._requester, data, completed = True )

    def create_fork( self, repo ):
        assert isinstance( repo, Repository.Repository ), repo
        status, headers, data = self._request(
            "POST",
            "https://api.github.com/repos/" + str( repo.owner.login ) + "/" + str( repo.name ) + "/forks",
            None,
            None
        )
        self._checkStatus( status, data )
        return Repository.Repository( self._requester, data, completed = True )

    def create_gist( self, public, files, description = GithubObject.NotSet ):
        assert isinstance( public, bool ), public
        if description is not GithubObject.NotSet:
            assert isinstance( description, ( str, unicode ) ), description
        post_parameters = {
            "public": public,
            "files": files,
        }
        if description is not GithubObject.NotSet:
            post_parameters[ "description" ] = description
        status, headers, data = self._request(
            "POST",
            "https://api.github.com/gists",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return Gist.Gist( self._requester, data, completed = True )

    def create_key( self, title, key ):
        assert isinstance( title, ( str, unicode ) ), title
        assert isinstance( key, ( str, unicode ) ), key
        post_parameters = {
            "title": title,
            "key": key,
        }
        status, headers, data = self._request(
            "POST",
            "https://api.github.com/user/keys",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return UserKey.UserKey( self._requester, data, completed = True )

    def create_repo( self, name, description = GithubObject.NotSet, homepage = GithubObject.NotSet, private = GithubObject.NotSet, has_issues = GithubObject.NotSet, has_wiki = GithubObject.NotSet, has_downloads = GithubObject.NotSet ):
        assert isinstance( name, ( str, unicode ) ), name
        if description is not GithubObject.NotSet:
            assert isinstance( description, ( str, unicode ) ), description
        if homepage is not GithubObject.NotSet:
            assert isinstance( homepage, ( str, unicode ) ), homepage
        if private is not GithubObject.NotSet:
            assert isinstance( private, bool ), private
        if has_issues is not GithubObject.NotSet:
            assert isinstance( has_issues, bool ), has_issues
        if has_wiki is not GithubObject.NotSet:
            assert isinstance( has_wiki, bool ), has_wiki
        if has_downloads is not GithubObject.NotSet:
            assert isinstance( has_downloads, bool ), has_downloads
        post_parameters = {
            "name": name,
        }
        if description is not GithubObject.NotSet:
            post_parameters[ "description" ] = description
        if homepage is not GithubObject.NotSet:
            post_parameters[ "homepage" ] = homepage
        if private is not GithubObject.NotSet:
            post_parameters[ "private" ] = private
        if has_issues is not GithubObject.NotSet:
            post_parameters[ "has_issues" ] = has_issues
        if has_wiki is not GithubObject.NotSet:
            post_parameters[ "has_wiki" ] = has_wiki
        if has_downloads is not GithubObject.NotSet:
            post_parameters[ "has_downloads" ] = has_downloads
        status, headers, data = self._request(
            "POST",
            "https://api.github.com/user/repos",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return Repository.Repository( self._requester, data, completed = True )

    def edit( self, name = GithubObject.NotSet, email = GithubObject.NotSet, blog = GithubObject.NotSet, company = GithubObject.NotSet, location = GithubObject.NotSet, hireable = GithubObject.NotSet, bio = GithubObject.NotSet ):
        if name is not GithubObject.NotSet:
            assert isinstance( name, ( str, unicode ) ), name
        if email is not GithubObject.NotSet:
            assert isinstance( email, ( str, unicode ) ), email
        if blog is not GithubObject.NotSet:
            assert isinstance( blog, ( str, unicode ) ), blog
        if company is not GithubObject.NotSet:
            assert isinstance( company, ( str, unicode ) ), company
        if location is not GithubObject.NotSet:
            assert isinstance( location, ( str, unicode ) ), location
        if hireable is not GithubObject.NotSet:
            assert isinstance( hireable, bool ), hireable
        if bio is not GithubObject.NotSet:
            assert isinstance( bio, ( str, unicode ) ), bio
        post_parameters = dict()
        if name is not GithubObject.NotSet:
            post_parameters[ "name" ] = name
        if email is not GithubObject.NotSet:
            post_parameters[ "email" ] = email
        if blog is not GithubObject.NotSet:
            post_parameters[ "blog" ] = blog
        if company is not GithubObject.NotSet:
            post_parameters[ "company" ] = company
        if location is not GithubObject.NotSet:
            post_parameters[ "location" ] = location
        if hireable is not GithubObject.NotSet:
            post_parameters[ "hireable" ] = hireable
        if bio is not GithubObject.NotSet:
            post_parameters[ "bio" ] = bio
        status, headers, data = self._request(
            "PATCH",
            "https://api.github.com/user",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        self._useAttributes( data )

    def get_authorization( self, id ):
        assert isinstance( id, int ), id
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/authorizations/" + str( id ),
            None,
            None
        )
        self._checkStatus( status, data )
        return Authorization.Authorization( self._requester, data, completed = True )

    def get_authorizations( self ):
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/authorizations",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Authorization.Authorization,
            self._requester,
            headers,
            data
        )

    def get_emails( self ):
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/user/emails",
            None,
            None
        )
        self._checkStatus( status, data )
        return data

    def get_events( self ):
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/events",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Event.Event,
            self._requester,
            headers,
            data
        )

    def get_followers( self ):
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/user/followers",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self._requester,
            headers,
            data
        )

    def get_following( self ):
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/user/following",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self._requester,
            headers,
            data
        )

    def get_gists( self ):
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/gists",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Gist.Gist,
            self._requester,
            headers,
            data
        )

    def get_issues( self ):
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/issues",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Issue.Issue,
            self._requester,
            headers,
            data
        )

    def get_key( self, id ):
        assert isinstance( id, int ), id
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/user/keys/" + str( id ),
            None,
            None
        )
        self._checkStatus( status, data )
        return UserKey.UserKey( self._requester, data, completed = True )

    def get_keys( self ):
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/user/keys",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            UserKey.UserKey,
            self._requester,
            headers,
            data
        )

    def get_organization_events( self, org ):
        assert isinstance( org, Organization.Organization ), org
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/users/" + str( self.login ) + "/events/orgs/" + str( org.login ),
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Event.Event,
            self._requester,
            headers,
            data
        )

    def get_orgs( self ):
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/user/orgs",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Organization.Organization,
            self._requester,
            headers,
            data
        )

    def get_repo( self, name ):
        assert isinstance( name, ( str, unicode ) ), name
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/repos/" + str( self.login ) + "/" + str( name ),
            None,
            None
        )
        self._checkStatus( status, data )
        return Repository.Repository( self._requester, data, completed = True )

    def get_repos( self, type = GithubObject.NotSet, sort = GithubObject.NotSet, direction = GithubObject.NotSet ):
        if type is not GithubObject.NotSet:
            assert isinstance( type, ( str, unicode ) ), type
        if sort is not GithubObject.NotSet:
            assert isinstance( sort, ( str, unicode ) ), sort
        if direction is not GithubObject.NotSet:
            assert isinstance( direction, ( str, unicode ) ), direction
        url_parameters = dict()
        if type is not GithubObject.NotSet:
            url_parameters[ "type" ] = type
        if sort is not GithubObject.NotSet:
            url_parameters[ "sort" ] = sort
        if direction is not GithubObject.NotSet:
            url_parameters[ "direction" ] = direction
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/user/repos",
            url_parameters,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Repository.Repository,
            self._requester,
            headers,
            data
        )

    def get_starred_gists( self ):
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/gists/starred",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Gist.Gist,
            self._requester,
            headers,
            data
        )

    def get_watched( self ):
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/user/watched",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Repository.Repository,
            self._requester,
            headers,
            data
        )

    def has_in_following( self, following ):
        assert isinstance( following, NamedUser.NamedUser ), following
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/user/following/" + str( following._identity ),
            None,
            None
        )
        return status == 204

    def has_in_watched( self, watched ):
        assert isinstance( watched, Repository.Repository ), watched
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/user/watched/" + str( watched._identity ),
            None,
            None
        )
        return status == 204

    def remove_from_emails( self, *emails ):
        assert all( isinstance( email, ( str, unicode ) ) for email in emails ), emails
        post_parameters = emails
        status, headers, data = self._request(
            "DELETE",
            "https://api.github.com/user/emails",
            None,
            post_parameters
        )
        self._checkStatus( status, data )

    def remove_from_following( self, following ):
        assert isinstance( following, NamedUser.NamedUser ), following
        status, headers, data = self._request(
            "DELETE",
            "https://api.github.com/user/following/" + str( following._identity ),
            None,
            None
        )
        self._checkStatus( status, data )

    def remove_from_watched( self, watched ):
        assert isinstance( watched, Repository.Repository ), watched
        status, headers, data = self._request(
            "DELETE",
            "https://api.github.com/user/watched/" + str( watched._identity ),
            None,
            None
        )
        self._checkStatus( status, data )

    def _initAttributes( self ):
        self._avatar_url = GithubObject.NotSet
        self._bio = GithubObject.NotSet
        self._blog = GithubObject.NotSet
        self._collaborators = GithubObject.NotSet
        self._company = GithubObject.NotSet
        self._created_at = GithubObject.NotSet
        self._disk_usage = GithubObject.NotSet
        self._email = GithubObject.NotSet
        self._followers = GithubObject.NotSet
        self._following = GithubObject.NotSet
        self._gravatar_id = GithubObject.NotSet
        self._hireable = GithubObject.NotSet
        self._html_url = GithubObject.NotSet
        self._id = GithubObject.NotSet
        self._location = GithubObject.NotSet
        self._login = GithubObject.NotSet
        self._name = GithubObject.NotSet
        self._owned_private_repos = GithubObject.NotSet
        self._plan = GithubObject.NotSet
        self._private_gists = GithubObject.NotSet
        self._public_gists = GithubObject.NotSet
        self._public_repos = GithubObject.NotSet
        self._total_private_repos = GithubObject.NotSet
        self._type = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "avatar_url" in attributes: # pragma no branch
            assert attributes[ "avatar_url" ] is None or isinstance( attributes[ "avatar_url" ], ( str, unicode ) ), attributes[ "avatar_url" ]
            self._avatar_url = attributes[ "avatar_url" ]
        if "bio" in attributes: # pragma no branch
            assert attributes[ "bio" ] is None or isinstance( attributes[ "bio" ], ( str, unicode ) ), attributes[ "bio" ]
            self._bio = attributes[ "bio" ]
        if "blog" in attributes: # pragma no branch
            assert attributes[ "blog" ] is None or isinstance( attributes[ "blog" ], ( str, unicode ) ), attributes[ "blog" ]
            self._blog = attributes[ "blog" ]
        if "collaborators" in attributes: # pragma no branch
            assert attributes[ "collaborators" ] is None or isinstance( attributes[ "collaborators" ], int ), attributes[ "collaborators" ]
            self._collaborators = attributes[ "collaborators" ]
        if "company" in attributes: # pragma no branch
            assert attributes[ "company" ] is None or isinstance( attributes[ "company" ], ( str, unicode ) ), attributes[ "company" ]
            self._company = attributes[ "company" ]
        if "created_at" in attributes: # pragma no branch
            assert attributes[ "created_at" ] is None or isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self._created_at = attributes[ "created_at" ]
        if "disk_usage" in attributes: # pragma no branch
            assert attributes[ "disk_usage" ] is None or isinstance( attributes[ "disk_usage" ], int ), attributes[ "disk_usage" ]
            self._disk_usage = attributes[ "disk_usage" ]
        if "email" in attributes: # pragma no branch
            assert attributes[ "email" ] is None or isinstance( attributes[ "email" ], ( str, unicode ) ), attributes[ "email" ]
            self._email = attributes[ "email" ]
        if "followers" in attributes: # pragma no branch
            assert attributes[ "followers" ] is None or isinstance( attributes[ "followers" ], int ), attributes[ "followers" ]
            self._followers = attributes[ "followers" ]
        if "following" in attributes: # pragma no branch
            assert attributes[ "following" ] is None or isinstance( attributes[ "following" ], int ), attributes[ "following" ]
            self._following = attributes[ "following" ]
        if "gravatar_id" in attributes: # pragma no branch
            assert attributes[ "gravatar_id" ] is None or isinstance( attributes[ "gravatar_id" ], ( str, unicode ) ), attributes[ "gravatar_id" ]
            self._gravatar_id = attributes[ "gravatar_id" ]
        if "hireable" in attributes: # pragma no branch
            assert attributes[ "hireable" ] is None or isinstance( attributes[ "hireable" ], bool ), attributes[ "hireable" ]
            self._hireable = attributes[ "hireable" ]
        if "html_url" in attributes: # pragma no branch
            assert attributes[ "html_url" ] is None or isinstance( attributes[ "html_url" ], ( str, unicode ) ), attributes[ "html_url" ]
            self._html_url = attributes[ "html_url" ]
        if "id" in attributes: # pragma no branch
            assert attributes[ "id" ] is None or isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "location" in attributes: # pragma no branch
            assert attributes[ "location" ] is None or isinstance( attributes[ "location" ], ( str, unicode ) ), attributes[ "location" ]
            self._location = attributes[ "location" ]
        if "login" in attributes: # pragma no branch
            assert attributes[ "login" ] is None or isinstance( attributes[ "login" ], ( str, unicode ) ), attributes[ "login" ]
            self._login = attributes[ "login" ]
        if "name" in attributes: # pragma no branch
            assert attributes[ "name" ] is None or isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
        if "owned_private_repos" in attributes: # pragma no branch
            assert attributes[ "owned_private_repos" ] is None or isinstance( attributes[ "owned_private_repos" ], int ), attributes[ "owned_private_repos" ]
            self._owned_private_repos = attributes[ "owned_private_repos" ]
        if "plan" in attributes: # pragma no branch
            assert attributes[ "plan" ] is None or isinstance( attributes[ "plan" ], dict ), attributes[ "plan" ]
            self._plan = None if attributes[ "plan" ] is None else Plan.Plan( self._requester, attributes[ "plan" ], completed = False )
        if "private_gists" in attributes: # pragma no branch
            assert attributes[ "private_gists" ] is None or isinstance( attributes[ "private_gists" ], int ), attributes[ "private_gists" ]
            self._private_gists = attributes[ "private_gists" ]
        if "public_gists" in attributes: # pragma no branch
            assert attributes[ "public_gists" ] is None or isinstance( attributes[ "public_gists" ], int ), attributes[ "public_gists" ]
            self._public_gists = attributes[ "public_gists" ]
        if "public_repos" in attributes: # pragma no branch
            assert attributes[ "public_repos" ] is None or isinstance( attributes[ "public_repos" ], int ), attributes[ "public_repos" ]
            self._public_repos = attributes[ "public_repos" ]
        if "total_private_repos" in attributes: # pragma no branch
            assert attributes[ "total_private_repos" ] is None or isinstance( attributes[ "total_private_repos" ], int ), attributes[ "total_private_repos" ]
            self._total_private_repos = attributes[ "total_private_repos" ]
        if "type" in attributes: # pragma no branch
            assert attributes[ "type" ] is None or isinstance( attributes[ "type" ], ( str, unicode ) ), attributes[ "type" ]
            self._type = attributes[ "type" ]
        if "url" in attributes: # pragma no branch
            assert attributes[ "url" ] is None or isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
