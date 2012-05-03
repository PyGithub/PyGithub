# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class Organization( object ):
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
    def billing_email( self ):
        if self.__billing_email is None:
            self.__completeIfNeeded()
        return self.__billing_email

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

    def __completeIfNeeded( self ):
        if not self.__completed:
            self.__complete()
        self.__completed = True

    def __complete( self ):
        pass

    def add_to_public_members( self, public_member ):
        pass

    def create_fork( self, repo ):
        pass

    def create_repo( self, name, description = None, homepage = None, private = None, has_issues = None, has_wiki = None, has_downloads = None, team_id = None ):
        pass

    def create_team( self, name, repo_names = None, permission = None ):
        pass

    def edit( self, billing_email = None, blog = None, company = None, email = None, location = None, name = None ):
        pass

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

    def get_members( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/members",
            None,
            None
        )
        return [
            NamedUser.NamedUser( self.__github, element, lazy = True )
            for element in result
        ]

    def get_public_members( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/public_members",
            None,
            None
        )
        return [
            NamedUser.NamedUser( self.__github, element, lazy = True )
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

    def get_teams( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/teams",
            None,
            None
        )
        return [
            Team.Team( self.__github, element, lazy = True )
            for element in result
        ]

    def has_in_members( self, member ):
        pass

    def has_in_public_members( self, public_member ):
        pass

    def remove_from_members( self, member ):
        pass

    def remove_from_public_members( self, public_member ):
        pass

    def __useAttributes( self, attributes ):
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
