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
        self.__completeIfNeeded( self.__active )
        return self.__active

    @property
    def config( self ):
        self.__completeIfNeeded( self.__config )
        return self.__config

    @property
    def created_at( self ):
        self.__completeIfNeeded( self.__created_at )
        return self.__created_at

    @property
    def events( self ):
        self.__completeIfNeeded( self.__events )
        return self.__events

    @property
    def id( self ):
        self.__completeIfNeeded( self.__id )
        return self.__id

    @property
    def last_response( self ):
        self.__completeIfNeeded( self.__last_response )
        return self.__last_response

    @property
    def name( self ):
        self.__completeIfNeeded( self.__name )
        return self.__name

    @property
    def updated_at( self ):
        self.__completeIfNeeded( self.__updated_at )
        return self.__updated_at

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
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

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
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
        post_parameters = {
            "name": name,
            "config": config,
        }
        if events is not None:
            post_parameters[ "events" ] = events
        if add_events is not None:
            post_parameters[ "add_events" ] = add_events
        if remove_events is not None:
            post_parameters[ "remove_events" ] = remove_events
        if active is not None:
            post_parameters[ "active" ] = active
        result = self.__github._dataRequest(
            "PATCH",
            "https://api.github.com/user",
            None,
            post_parameters
        )
        self.__useAttributes( result )

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
