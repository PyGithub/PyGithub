# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *

class Hook( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def active( self ):
        return self.__active

    @property
    def config( self ):
        return self.__config

    @property
    def created_at( self ):
        return self.__created_at

    @property
    def events( self ):
        return self.__events

    @property
    def id( self ):
        return self.__id

    @property
    def last_response( self ):
        return self.__last_response

    @property
    def name( self ):
        return self.__name

    @property
    def updated_at( self ):
        return self.__updated_at

    @property
    def url( self ):
        return self.__url

    def delete( self ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ),
            None,
            None
        )

    def edit( self, name, config, events = DefaultValueForOptionalParameters, add_events = DefaultValueForOptionalParameters, remove_events = DefaultValueForOptionalParameters, active = DefaultValueForOptionalParameters ):
        post_parameters = {
            "name": name,
            "config": config,
        }
        if events is not DefaultValueForOptionalParameters:
            post_parameters[ "events" ] = events
        if add_events is not DefaultValueForOptionalParameters:
            post_parameters[ "add_events" ] = add_events
        if remove_events is not DefaultValueForOptionalParameters:
            post_parameters[ "remove_events" ] = remove_events
        if active is not DefaultValueForOptionalParameters:
            post_parameters[ "active" ] = active
        status, headers, data = self.__requester.request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self.__useAttributes( data )

    def test( self ):
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/test",
            None,
            None
        )

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

    def __useAttributes( self, attributes ):
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "active", "config", "created_at", "events", "id", "last_response", "name", "updated_at", "url", ], attribute
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "active" in attributes and attributes[ "active" ] is not None:
            self.__active = attributes[ "active" ]
        if "config" in attributes and attributes[ "config" ] is not None:
            self.__config = attributes[ "config" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None:
            self.__created_at = attributes[ "created_at" ]
        if "events" in attributes and attributes[ "events" ] is not None:
            self.__events = attributes[ "events" ]
        if "id" in attributes and attributes[ "id" ] is not None:
            self.__id = attributes[ "id" ]
        if "last_response" in attributes and attributes[ "last_response" ] is not None:
            self.__last_response = attributes[ "last_response" ]
        if "name" in attributes and attributes[ "name" ] is not None:
            self.__name = attributes[ "name" ]
        if "updated_at" in attributes and attributes[ "updated_at" ] is not None:
            self.__updated_at = attributes[ "updated_at" ]
        if "url" in attributes and attributes[ "url" ] is not None:
            self.__url = attributes[ "url" ]
