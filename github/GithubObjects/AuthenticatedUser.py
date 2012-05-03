# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import Gist
import Repository
import NamedUser
import Organization
import UserKey
import Issue
import Event
import Authorization

class AuthenticatedUser( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def avatar_url( self ):
        if self.__avatar_url is None:
            self.__completeIfNeeded()
        return self.__avatar_url

    @property
    def bio( self ):
        if self.__bio is None:
            self.__completeIfNeeded()
        return self.__bio

    @property
    def blog( self ):
        if self.__blog is None:
            self.__completeIfNeeded()
        return self.__blog

    @property
    def collaborators( self ):
        if self.__collaborators is None:
            self.__completeIfNeeded()
        return self.__collaborators

    @property
    def company( self ):
        if self.__company is None:
            self.__completeIfNeeded()
        return self.__company

    @property
    def created_at( self ):
        if self.__created_at is None:
            self.__completeIfNeeded()
        return self.__created_at

    @property
    def disk_usage( self ):
        if self.__disk_usage is None:
            self.__completeIfNeeded()
        return self.__disk_usage

    @property
    def email( self ):
        if self.__email is None:
            self.__completeIfNeeded()
        return self.__email

    @property
    def followers( self ):
        if self.__followers is None:
            self.__completeIfNeeded()
        return self.__followers

    @property
    def following( self ):
        if self.__following is None:
            self.__completeIfNeeded()
        return self.__following

    @property
    def gravatar_id( self ):
        if self.__gravatar_id is None:
            self.__completeIfNeeded()
        return self.__gravatar_id

    @property
    def hireable( self ):
        if self.__hireable is None:
            self.__completeIfNeeded()
        return self.__hireable

    @property
    def html_url( self ):
        if self.__html_url is None:
            self.__completeIfNeeded()
        return self.__html_url

    @property
    def id( self ):
        if self.__id is None:
            self.__completeIfNeeded()
        return self.__id

    @property
    def location( self ):
        if self.__location is None:
            self.__completeIfNeeded()
        return self.__location

    @property
    def login( self ):
        if self.__login is None:
            self.__completeIfNeeded()
        return self.__login

    @property
    def name( self ):
        if self.__name is None:
            self.__completeIfNeeded()
        return self.__name

    @property
    def owned_private_repos( self ):
        if self.__owned_private_repos is None:
            self.__completeIfNeeded()
        return self.__owned_private_repos

    @property
    def plan( self ):
        if self.__plan is None:
            self.__completeIfNeeded()
        return self.__plan

    @property
    def private_gists( self ):
        if self.__private_gists is None:
            self.__completeIfNeeded()
        return self.__private_gists

    @property
    def public_gists( self ):
        if self.__public_gists is None:
            self.__completeIfNeeded()
        return self.__public_gists

    @property
    def public_repos( self ):
        if self.__public_repos is None:
            self.__completeIfNeeded()
        return self.__public_repos

    @property
    def total_private_repos( self ):
        if self.__total_private_repos is None:
            self.__completeIfNeeded()
        return self.__total_private_repos

    @property
    def type( self ):
        if self.__type is None:
            self.__completeIfNeeded()
        return self.__type

    @property
    def url( self ):
        if self.__url is None:
            self.__completeIfNeeded()
        return self.__url

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

    def __completeIfNeeded( self ):
        if not self.__completed:
            self.__complete()
        self.__completed = True

    # @todo Do not generate __complete if type has no url attribute
    def __complete( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url,
            None,
            None
        )
        self.__useAttributes( result )

    def add_to_emails( self, *emails ):
        pass

    def add_to_following( self, following ):
        pass

    def add_to_watched( self, watched ):
        pass

    def create_authorization( self, scopes = None, note = None, note_url = None ):
        pass

    def create_fork( self, repo ):
        result = self.__github._dataRequest(
            "POST",
            "/repos/" + repo.owner.login + "/" + repo.name + "/forks",
            None,
            None
        )
        return Repository.Repository( self.__github, result, lazy = True )

    def create_gist( self, public, files, description = None ):
        pass

    def create_key( self, title, key ):
        pass

    def create_repo( self, name, description = None, homepage = None, private = None, has_issues = None, has_wiki = None, has_downloads = None, team_id = None ):
        pass

    def edit( self, name = None, email = None, blog = None, company = None, location = None, hireable = None, bio = None ):
        pass

    def get_authorization( self, id ):
        pass

    def get_authorizations( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/authorizations",
            None,
            None
        )
        return [
            Authorization.Authorization( self.__github, element, lazy = True )
            for element in result
        ]

    def get_emails( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/emails",
            None,
            None
        )
        return [
            string.string( self.__github, element, lazy = True )
            for element in result
        ]

    def get_events( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/events",
            None,
            None
        )
        return [
            Event.Event( self.__github, element, lazy = True )
            for element in result
        ]

    def get_followers( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/followers",
            None,
            None
        )
        return [
            NamedUser.NamedUser( self.__github, element, lazy = True )
            for element in result
        ]

    def get_following( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/following",
            None,
            None
        )
        return [
            NamedUser.NamedUser( self.__github, element, lazy = True )
            for element in result
        ]

    def get_gists( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/gists",
            None,
            None
        )
        return [
            Gist.Gist( self.__github, element, lazy = True )
            for element in result
        ]

    def get_issues( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/issues",
            None,
            None
        )
        return [
            Issue.Issue( self.__github, element, lazy = True )
            for element in result
        ]

    def get_key( self, id ):
        pass

    def get_keys( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/keys",
            None,
            None
        )
        return [
            UserKey.UserKey( self.__github, element, lazy = True )
            for element in result
        ]

    def get_organization_events( self, org ):
        pass

    def get_orgs( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/orgs",
            None,
            None
        )
        return [
            Organization.Organization( self.__github, element, lazy = True )
            for element in result
        ]

    def get_repo( self, name ):
        pass

    def get_repos( self, type = None ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/repos",
            None,
            None
        )
        return [
            Repository.Repository( self.__github, element, lazy = True )
            for element in result
        ]

    def get_starred_gists( self ):
        pass

    def get_watched( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/watched",
            None,
            None
        )
        return [
            Repository.Repository( self.__github, element, lazy = True )
            for element in result
        ]

    def has_in_following( self, following ):
        pass

    def has_in_watched( self, watched ):
        pass

    def remove_from_emails( self, *emails ):
        pass

    def remove_from_following( self, following ):
        pass

    def remove_from_watched( self, watched ):
        pass

    def __useAttributes( self, attributes ):
        if "avatar_url" in attributes:
            self.__avatar_url = attributes[ "avatar_url" ]
        if "bio" in attributes:
            self.__bio = attributes[ "bio" ]
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
        if "hireable" in attributes:
            self.__hireable = attributes[ "hireable" ]
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
