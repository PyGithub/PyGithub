# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class PullRequestComment( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def body( self ):
        if self.__body is None:
            self.__completeIfNeeded()
        return self.__body

    @property
    def commit_id( self ):
        if self.__commit_id is None:
            self.__completeIfNeeded()
        return self.__commit_id

    @property
    def created_at( self ):
        if self.__created_at is None:
            self.__completeIfNeeded()
        return self.__created_at

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
    def line( self ):
        if self.__line is None:
            self.__completeIfNeeded()
        return self.__line

    @property
    def path( self ):
        if self.__path is None:
            self.__completeIfNeeded()
        return self.__path

    @property
    def position( self ):
        if self.__position is None:
            self.__completeIfNeeded()
        return self.__position

    @property
    def updated_at( self ):
        if self.__updated_at is None:
            self.__completeIfNeeded()
        return self.__updated_at

    @property
    def url( self ):
        if self.__url is None:
            self.__completeIfNeeded()
        return self.__url

    @property
    def user( self ):
        if self.__user is None:
            self.__completeIfNeeded()
        return self.__user

    def __initAttributes( self ):
        self.__body = None
        self.__commit_id = None
        self.__created_at = None
        self.__html_url = None
        self.__id = None
        self.__line = None
        self.__path = None
        self.__position = None
        self.__updated_at = None
        self.__url = None
        self.__user = None

    def __completeIfNeeded( self ):
        if not self.__completed:
            self.__complete()
        self.__completed = True

    def __complete( self ):
        pass

    def delete( self ):
        pass

    def edit( self, body ):
        pass

    def __useAttributes( self, attributes ):
        if "body" in attributes:
            self.__body = attributes[ "body" ]
        if "commit_id" in attributes:
            self.__commit_id = attributes[ "commit_id" ]
        if "created_at" in attributes:
            self.__created_at = attributes[ "created_at" ]
        if "html_url" in attributes:
            self.__html_url = attributes[ "html_url" ]
        if "id" in attributes:
            self.__id = attributes[ "id" ]
        if "line" in attributes:
            self.__line = attributes[ "line" ]
        if "path" in attributes:
            self.__path = attributes[ "path" ]
        if "position" in attributes:
            self.__position = attributes[ "position" ]
        if "updated_at" in attributes:
            self.__updated_at = attributes[ "updated_at" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
        if "user" in attributes:
            self.__user = attributes[ "user" ]
