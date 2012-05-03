# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class Event( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def actor( self ):
        if self.__actor is None:
            self.__completeIfNeeded()
        return self.__actor

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
    def event( self ):
        if self.__event is None:
            self.__completeIfNeeded()
        return self.__event

    @property
    def id( self ):
        if self.__id is None:
            self.__completeIfNeeded()
        return self.__id

    @property
    def issue( self ):
        if self.__issue is None:
            self.__completeIfNeeded()
        return self.__issue

    @property
    def org( self ):
        if self.__org is None:
            self.__completeIfNeeded()
        return self.__org

    @property
    def payload( self ):
        if self.__payload is None:
            self.__completeIfNeeded()
        return self.__payload

    @property
    def public( self ):
        if self.__public is None:
            self.__completeIfNeeded()
        return self.__public

    @property
    def repo( self ):
        if self.__repo is None:
            self.__completeIfNeeded()
        return self.__repo

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
        self.__actor = None
        self.__commit_id = None
        self.__created_at = None
        self.__event = None
        self.__id = None
        self.__issue = None
        self.__org = None
        self.__payload = None
        self.__public = None
        self.__repo = None
        self.__type = None
        self.__url = None

    def __completeIfNeeded( self ):
        if not self.__completed:
            self.__complete()
        self.__completed = True

    def __complete( self ):
        pass

    def __useAttributes( self, attributes ):
        if "actor" in attributes:
            self.__actor = attributes[ "actor" ]
        if "commit_id" in attributes:
            self.__commit_id = attributes[ "commit_id" ]
        if "created_at" in attributes:
            self.__created_at = attributes[ "created_at" ]
        if "event" in attributes:
            self.__event = attributes[ "event" ]
        if "id" in attributes:
            self.__id = attributes[ "id" ]
        if "issue" in attributes:
            self.__issue = attributes[ "issue" ]
        if "org" in attributes:
            self.__org = attributes[ "org" ]
        if "payload" in attributes:
            self.__payload = attributes[ "payload" ]
        if "public" in attributes:
            self.__public = attributes[ "public" ]
        if "repo" in attributes:
            self.__repo = attributes[ "repo" ]
        if "type" in attributes:
            self.__type = attributes[ "type" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
