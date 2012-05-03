# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class Hook( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def active( self ):
        if self.__active is None:
            self.__completeIfNeeded()
        return self.__active

    @property
    def config( self ):
        if self.__config is None:
            self.__completeIfNeeded()
        return self.__config

    @property
    def created_at( self ):
        if self.__created_at is None:
            self.__completeIfNeeded()
        return self.__created_at

    @property
    def events( self ):
        if self.__events is None:
            self.__completeIfNeeded()
        return self.__events

    @property
    def id( self ):
        if self.__id is None:
            self.__completeIfNeeded()
        return self.__id

    @property
    def last_response( self ):
        if self.__last_response is None:
            self.__completeIfNeeded()
        return self.__last_response

    @property
    def name( self ):
        if self.__name is None:
            self.__completeIfNeeded()
        return self.__name

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

    def __initAttributes( self ):
        self.__active = None
        self.__config = None
        self.__created_at = None
        self.__events = None
        self.__id = None
        self.__last_response = None
        self.__name = None
        self.__updated_at = None
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

    def delete( self ):
        pass

    def edit( self, name, config, events = None, add_events = None, remove_events = None, active = None ):
        pass

    def test( self ):
        pass

    def __useAttributes( self, attributes ):
        if "active" in attributes:
            self.__active = attributes[ "active" ]
        if "config" in attributes:
            self.__config = attributes[ "config" ]
        if "created_at" in attributes:
            self.__created_at = attributes[ "created_at" ]
        if "events" in attributes:
            self.__events = attributes[ "events" ]
        if "id" in attributes:
            self.__id = attributes[ "id" ]
        if "last_response" in attributes:
            self.__last_response = attributes[ "last_response" ]
        if "name" in attributes:
            self.__name = attributes[ "name" ]
        if "updated_at" in attributes:
            self.__updated_at = attributes[ "updated_at" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
