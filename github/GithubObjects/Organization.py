# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import Team
import Event
import Repository
import NamedUser

class Organization( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def avatar_url( self ):
        self.__completeIfNeeded( self.__avatar_url )
        return self.__avatar_url

    @property
    def billing_email( self ):
        self.__completeIfNeeded( self.__billing_email )
        return self.__billing_email

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

    def add_to_public_members( self, public_member ):
        status, headers, data = self.__requester.request(
            "PUT",
            str( self.url ) + "/public_members/" + str( public_member.login ),
            None,
            None
        )

    def create_fork( self, repo ):
        status, headers, data = self.__requester.request(
            "POST",
            "https://api.github.com/repos/" + str( repo.owner.login ) + "/" + str( repo.name ) + "/forks",
            None,
            None
        )
        return Repository.Repository( self.__requester, data, lazy = True )

    def create_repo( self, name, description = None, homepage = None, private = None, has_issues = None, has_wiki = None, has_downloads = None, team_id = None ):
        post_parameters = {
            "name": name,
        }
        if description is not None:
            post_parameters[ "description" ] = description
        if homepage is not None:
            post_parameters[ "homepage" ] = homepage
        if private is not None:
            post_parameters[ "private" ] = private
        if has_issues is not None:
            post_parameters[ "has_issues" ] = has_issues
        if has_wiki is not None:
            post_parameters[ "has_wiki" ] = has_wiki
        if has_downloads is not None:
            post_parameters[ "has_downloads" ] = has_downloads
        if team_id is not None:
            post_parameters[ "team_id" ] = team_id
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/repos",
            None,
            post_parameters
        )
        return Repository.Repository( self.__requester, data, lazy = True )

    def create_team( self, name, repo_names = None, permission = None ):
        post_parameters = {
            "name": name,
        }
        if repo_names is not None:
            post_parameters[ "repo_names" ] = repo_names
        if permission is not None:
            post_parameters[ "permission" ] = permission
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/teams",
            None,
            post_parameters
        )
        return Team.Team( self.__requester, data, lazy = True )

    def edit( self, billing_email = None, blog = None, company = None, email = None, location = None, name = None ):
        post_parameters = {
        }
        if billing_email is not None:
            post_parameters[ "billing_email" ] = billing_email
        if blog is not None:
            post_parameters[ "blog" ] = blog
        if company is not None:
            post_parameters[ "company" ] = company
        if email is not None:
            post_parameters[ "email" ] = email
        if location is not None:
            post_parameters[ "location" ] = location
        if name is not None:
            post_parameters[ "name" ] = name
        status, headers, data = self.__requester.request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self.__useAttributes( data )

    def get_events( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/events",
            None,
            None
        )
        return [
            Event.Event( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_members( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/members",
            None,
            None
        )
        return [
            NamedUser.NamedUser( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_public_members( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/public_members",
            None,
            None
        )
        return [
            NamedUser.NamedUser( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_repo( self, name ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/repos/" + str( self.login ) + "/" + str( name ),
            None,
            None
        )
        return Repository.Repository( self.__requester, data, lazy = True )

    def get_repos( self, type = None ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/repos",
            None,
            None
        )
        return [
            Repository.Repository( self.__requester, element, lazy = True )
            for element in data
        ]

    def get_teams( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/teams",
            None,
            None
        )
        return [
            Team.Team( self.__requester, element, lazy = True )
            for element in data
        ]

    def has_in_members( self, member ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/members/" + str( member.login ),
            None,
            None
        )
        return status == 204

    def has_in_public_members( self, public_member ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/public_members/" + str( public_member.login ),
            None,
            None
        )
        return status == 204

    def remove_from_members( self, member ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ) + "/members/" + str( member.login ),
            None,
            None
        )

    def remove_from_public_members( self, public_member ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ) + "/public_members/" + str( public_member.login ),
            None,
            None
        )

    def __initAttributes( self ):
        self.__avatar_url = None
        self.__billing_email = None
        self.__blog = None
        self.__collaborators = None
        self.__company = None
        self.__created_at = None
        self.__disk_usage = None
        self.__email = None
        self.__followers = None
        self.__following = None
        self.__gravatar_id = None
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

    # @todo Do not generate __complete if type has no url attribute
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
         #@todo No need to check if attribute is in attributes when attribute is mandatory
        if "avatar_url" in attributes:
            self.__avatar_url = attributes[ "avatar_url" ]
        if "billing_email" in attributes:
            self.__billing_email = attributes[ "billing_email" ]
        if "blog" in attributes:
            self.__blog = attributes[ "blog" ]
        if "collaborators" in attributes:
            self.__collaborators = attributes[ "collaborators" ]
        if "company" in attributes:
            self.__company = attributes[ "company" ]
        if "created_at" in attributes:
            self.__created_at = attributes[ "created_at" ]
        if "disk_usage" in attributes:
            self.__disk_usage = attributes[ "disk_usage" ]
        if "email" in attributes:
            self.__email = attributes[ "email" ]
        if "followers" in attributes:
            self.__followers = attributes[ "followers" ]
        if "following" in attributes:
            self.__following = attributes[ "following" ]
        if "gravatar_id" in attributes:
            self.__gravatar_id = attributes[ "gravatar_id" ]
        if "html_url" in attributes:
            self.__html_url = attributes[ "html_url" ]
        if "id" in attributes:
            self.__id = attributes[ "id" ]
        if "location" in attributes:
            self.__location = attributes[ "location" ]
        if "login" in attributes:
            self.__login = attributes[ "login" ]
        if "name" in attributes:
            self.__name = attributes[ "name" ]
        if "owned_private_repos" in attributes:
            self.__owned_private_repos = attributes[ "owned_private_repos" ]
        if "plan" in attributes:
            self.__plan = attributes[ "plan" ]
        if "private_gists" in attributes:
            self.__private_gists = attributes[ "private_gists" ]
        if "public_gists" in attributes:
            self.__public_gists = attributes[ "public_gists" ]
        if "public_repos" in attributes:
            self.__public_repos = attributes[ "public_repos" ]
        if "total_private_repos" in attributes:
            self.__total_private_repos = attributes[ "total_private_repos" ]
        if "type" in attributes:
            self.__type = attributes[ "type" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
