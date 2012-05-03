# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class IssueEvent( object ):
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
        if "url" in attributes:
            self.__url = attributes[ "url" ]
