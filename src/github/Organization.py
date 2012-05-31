# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
import PaginatedList
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters
##########
import Team
import Plan
import Event
import Repository
import NamedUser

class Organization( GithubObject.GithubObject ):
    @property
    def avatar_url( self ):
        self._completeIfNeeded( self._avatar_url )
        return self._avatar_url

    @property
    def billing_email( self ):
        self._completeIfNeeded( self._billing_email )
        return self._billing_email

    @property
    def blog( self ):
        self._completeIfNeeded( self._blog )
        return self._blog

    @property
    def collaborators( self ):
        self._completeIfNeeded( self._collaborators )
        return self._collaborators

    @property
    def company( self ):
        self._completeIfNeeded( self._company )
        return self._company

    @property
    def created_at( self ):
        self._completeIfNeeded( self._created_at )
        return self._created_at

    @property
    def disk_usage( self ):
        self._completeIfNeeded( self._disk_usage )
        return self._disk_usage

    @property
    def email( self ):
        self._completeIfNeeded( self._email )
        return self._email

    @property
    def followers( self ):
        self._completeIfNeeded( self._followers )
        return self._followers

    @property
    def following( self ):
        self._completeIfNeeded( self._following )
        return self._following

    @property
    def gravatar_id( self ):
        self._completeIfNeeded( self._gravatar_id )
        return self._gravatar_id

    @property
    def html_url( self ):
        self._completeIfNeeded( self._html_url )
        return self._html_url

    @property
    def id( self ):
        self._completeIfNeeded( self._id )
        return self._id

    @property
    def location( self ):
        self._completeIfNeeded( self._location )
        return self._location

    @property
    def login( self ):
        self._completeIfNeeded( self._login )
        return self._login

    @property
    def name( self ):
        self._completeIfNeeded( self._name )
        return self._name

    @property
    def owned_private_repos( self ):
        self._completeIfNeeded( self._owned_private_repos )
        return self._owned_private_repos

    @property
    def plan( self ):
        self._completeIfNeeded( self._plan )
        return self._plan

    @property
    def private_gists( self ):
        self._completeIfNeeded( self._private_gists )
        return self._private_gists

    @property
    def public_gists( self ):
        self._completeIfNeeded( self._public_gists )
        return self._public_gists

    @property
    def public_repos( self ):
        self._completeIfNeeded( self._public_repos )
        return self._public_repos

    @property
    def total_private_repos( self ):
        self._completeIfNeeded( self._total_private_repos )
        return self._total_private_repos

    @property
    def type( self ):
        self._completeIfNeeded( self._type )
        return self._type

    @property
    def url( self ):
        self._completeIfNeeded( self._url )
        return self._url

    def add_to_public_members( self, public_member ):
        assert isinstance( public_member, NamedUser.NamedUser ), public_member
        status, headers, data = self._request(
            "PUT",
            str( self.url ) + "/public_members/" + str( public_member._identity ),
            None,
            None
        )
        self._checkStatus( status, data )

    def create_fork( self, repo ):
        assert isinstance( repo, Repository.Repository ), repo
        url_parameters = {
            "org": str( self.login ),
        }
        status, headers, data = self._request(
            "POST",
            "https://api.github.com/repos/" + str( repo.owner.login ) + "/" + str( repo.name ) + "/forks",
            url_parameters,
            None
        )
        self._checkStatus( status, data )
        return Repository.Repository( self._requester, data, completed = True )

    def create_repo( self, name, description = DefaultValueForOptionalParameters, homepage = DefaultValueForOptionalParameters, private = DefaultValueForOptionalParameters, has_issues = DefaultValueForOptionalParameters, has_wiki = DefaultValueForOptionalParameters, has_downloads = DefaultValueForOptionalParameters, team_id = DefaultValueForOptionalParameters ):
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
        if team_id is not DefaultValueForOptionalParameters:
            assert isinstance( team_id, int ), team_id
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
        if team_id is not DefaultValueForOptionalParameters:
            post_parameters[ "team_id" ] = team_id
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/repos",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return Repository.Repository( self._requester, data, completed = True )

    def create_team( self, name, repo_names = DefaultValueForOptionalParameters, permission = DefaultValueForOptionalParameters ):
        assert isinstance( name, ( str, unicode ) ), name
        if repo_names is not DefaultValueForOptionalParameters:
            assert all( isinstance( element, ( str, unicode ) ) for element in repo_names ), repo_names
        if permission is not DefaultValueForOptionalParameters:
            assert isinstance( permission, ( str, unicode ) ), permission
        post_parameters = {
            "name": name,
        }
        if repo_names is not DefaultValueForOptionalParameters:
            post_parameters[ "repo_names" ] = repo_names
        if permission is not DefaultValueForOptionalParameters:
            post_parameters[ "permission" ] = permission
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/teams",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return Team.Team( self._requester, data, completed = True )

    def edit( self, billing_email = DefaultValueForOptionalParameters, blog = DefaultValueForOptionalParameters, company = DefaultValueForOptionalParameters, email = DefaultValueForOptionalParameters, location = DefaultValueForOptionalParameters, name = DefaultValueForOptionalParameters ):
        if billing_email is not DefaultValueForOptionalParameters:
            assert isinstance( billing_email, ( str, unicode ) ), billing_email
        if blog is not DefaultValueForOptionalParameters:
            assert isinstance( blog, ( str, unicode ) ), blog
        if company is not DefaultValueForOptionalParameters:
            assert isinstance( company, ( str, unicode ) ), company
        if email is not DefaultValueForOptionalParameters:
            assert isinstance( email, ( str, unicode ) ), email
        if location is not DefaultValueForOptionalParameters:
            assert isinstance( location, ( str, unicode ) ), location
        if name is not DefaultValueForOptionalParameters:
            assert isinstance( name, ( str, unicode ) ), name
        post_parameters = dict()
        if billing_email is not DefaultValueForOptionalParameters:
            post_parameters[ "billing_email" ] = billing_email
        if blog is not DefaultValueForOptionalParameters:
            post_parameters[ "blog" ] = blog
        if company is not DefaultValueForOptionalParameters:
            post_parameters[ "company" ] = company
        if email is not DefaultValueForOptionalParameters:
            post_parameters[ "email" ] = email
        if location is not DefaultValueForOptionalParameters:
            post_parameters[ "location" ] = location
        if name is not DefaultValueForOptionalParameters:
            post_parameters[ "name" ] = name
        status, headers, data = self._request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        self._useAttributes( data )

    def get_events( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/events",
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

    def get_members( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/members",
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

    def get_public_members( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/public_members",
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

    def get_repos( self, type = DefaultValueForOptionalParameters ):
        if type is not DefaultValueForOptionalParameters:
            assert isinstance( type, ( str, unicode ) ), type
        url_parameters = dict()
        if type is not DefaultValueForOptionalParameters:
            url_parameters[ "type" ] = type
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/repos",
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

    def get_team( self, id ):
        assert isinstance( id, int ), id
        status, headers, data = self._request(
            "GET",
            "https://api.github.com/teams/" + str( id ),
            None,
            None
        )
        self._checkStatus( status, data )
        return Team.Team( self._requester, data, completed = True )

    def get_teams( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/teams",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Team.Team,
            self._requester,
            headers,
            data
        )

    def has_in_members( self, member ):
        assert isinstance( member, NamedUser.NamedUser ), member
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/members/" + str( member._identity ),
            None,
            None
        )
        return status == 204

    def has_in_public_members( self, public_member ):
        assert isinstance( public_member, NamedUser.NamedUser ), public_member
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/public_members/" + str( public_member._identity ),
            None,
            None
        )
        return status == 204

    def remove_from_members( self, member ):
        assert isinstance( member, NamedUser.NamedUser ), member
        status, headers, data = self._request(
            "DELETE",
            str( self.url ) + "/members/" + str( member._identity ),
            None,
            None
        )
        self._checkStatus( status, data )

    def remove_from_public_members( self, public_member ):
        assert isinstance( public_member, NamedUser.NamedUser ), public_member
        status, headers, data = self._request(
            "DELETE",
            str( self.url ) + "/public_members/" + str( public_member._identity ),
            None,
            None
        )
        self._checkStatus( status, data )

    def _initAttributes( self ):
        self._avatar_url = None
        self._billing_email = None
        self._blog = None
        self._collaborators = None
        self._company = None
        self._created_at = None
        self._disk_usage = None
        self._email = None
        self._followers = None
        self._following = None
        self._gravatar_id = None
        self._html_url = None
        self._id = None
        self._location = None
        self._login = None
        self._name = None
        self._owned_private_repos = None
        self._plan = None
        self._private_gists = None
        self._public_gists = None
        self._public_repos = None
        self._total_private_repos = None
        self._type = None
        self._url = None

    def _useAttributes( self, attributes ):
        if "avatar_url" in attributes and attributes[ "avatar_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "avatar_url" ], ( str, unicode ) ), attributes[ "avatar_url" ]
            self._avatar_url = attributes[ "avatar_url" ]
        if "billing_email" in attributes and attributes[ "billing_email" ] is not None: # pragma no branch
            assert isinstance( attributes[ "billing_email" ], ( str, unicode ) ), attributes[ "billing_email" ]
            self._billing_email = attributes[ "billing_email" ]
        if "blog" in attributes and attributes[ "blog" ] is not None: # pragma no branch
            assert isinstance( attributes[ "blog" ], ( str, unicode ) ), attributes[ "blog" ]
            self._blog = attributes[ "blog" ]
        if "collaborators" in attributes and attributes[ "collaborators" ] is not None: # pragma no branch
            assert isinstance( attributes[ "collaborators" ], int ), attributes[ "collaborators" ]
            self._collaborators = attributes[ "collaborators" ]
        if "company" in attributes and attributes[ "company" ] is not None: # pragma no branch
            assert isinstance( attributes[ "company" ], ( str, unicode ) ), attributes[ "company" ]
            self._company = attributes[ "company" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self._created_at = attributes[ "created_at" ]
        if "disk_usage" in attributes and attributes[ "disk_usage" ] is not None: # pragma no branch
            assert isinstance( attributes[ "disk_usage" ], int ), attributes[ "disk_usage" ]
            self._disk_usage = attributes[ "disk_usage" ]
        if "email" in attributes and attributes[ "email" ] is not None: # pragma no branch
            assert isinstance( attributes[ "email" ], ( str, unicode ) ), attributes[ "email" ]
            self._email = attributes[ "email" ]
        if "followers" in attributes and attributes[ "followers" ] is not None: # pragma no branch
            assert isinstance( attributes[ "followers" ], int ), attributes[ "followers" ]
            self._followers = attributes[ "followers" ]
        if "following" in attributes and attributes[ "following" ] is not None: # pragma no branch
            assert isinstance( attributes[ "following" ], int ), attributes[ "following" ]
            self._following = attributes[ "following" ]
        if "gravatar_id" in attributes and attributes[ "gravatar_id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "gravatar_id" ], ( str, unicode ) ), attributes[ "gravatar_id" ]
            self._gravatar_id = attributes[ "gravatar_id" ]
        if "html_url" in attributes and attributes[ "html_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "html_url" ], ( str, unicode ) ), attributes[ "html_url" ]
            self._html_url = attributes[ "html_url" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "location" in attributes and attributes[ "location" ] is not None: # pragma no branch
            assert isinstance( attributes[ "location" ], ( str, unicode ) ), attributes[ "location" ]
            self._location = attributes[ "location" ]
        if "login" in attributes and attributes[ "login" ] is not None: # pragma no branch
            assert isinstance( attributes[ "login" ], ( str, unicode ) ), attributes[ "login" ]
            self._login = attributes[ "login" ]
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
        if "owned_private_repos" in attributes and attributes[ "owned_private_repos" ] is not None: # pragma no branch
            assert isinstance( attributes[ "owned_private_repos" ], int ), attributes[ "owned_private_repos" ]
            self._owned_private_repos = attributes[ "owned_private_repos" ]
        if "plan" in attributes and attributes[ "plan" ] is not None: # pragma no branch
            assert isinstance( attributes[ "plan" ], dict ), attributes[ "plan" ]
            self._plan = Plan.Plan( self._requester, attributes[ "plan" ], completed = False )
        if "private_gists" in attributes and attributes[ "private_gists" ] is not None: # pragma no branch
            assert isinstance( attributes[ "private_gists" ], int ), attributes[ "private_gists" ]
            self._private_gists = attributes[ "private_gists" ]
        if "public_gists" in attributes and attributes[ "public_gists" ] is not None: # pragma no branch
            assert isinstance( attributes[ "public_gists" ], int ), attributes[ "public_gists" ]
            self._public_gists = attributes[ "public_gists" ]
        if "public_repos" in attributes and attributes[ "public_repos" ] is not None: # pragma no branch
            assert isinstance( attributes[ "public_repos" ], int ), attributes[ "public_repos" ]
            self._public_repos = attributes[ "public_repos" ]
        if "total_private_repos" in attributes and attributes[ "total_private_repos" ] is not None: # pragma no branch
            assert isinstance( attributes[ "total_private_repos" ], int ), attributes[ "total_private_repos" ]
            self._total_private_repos = attributes[ "total_private_repos" ]
        if "type" in attributes and attributes[ "type" ] is not None: # pragma no branch
            assert isinstance( attributes[ "type" ], ( str, unicode ) ), attributes[ "type" ]
            self._type = attributes[ "type" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
