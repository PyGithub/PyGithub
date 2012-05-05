# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
# This allows None as a valid value for an optional parameter

class DefaultValueForOptionalParametersType:
    pass
DefaultValueForOptionalParameters = DefaultValueForOptionalParametersType()

class Authorization( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def app( self ):
        self.__completeIfNeeded( self.__app )
        return self.__app

    @property
    def created_at( self ):
        self.__completeIfNeeded( self.__created_at )
        return self.__created_at

    @property
    def id( self ):
        self.__completeIfNeeded( self.__id )
        return self.__id

    @property
    def note( self ):
        self.__completeIfNeeded( self.__note )
        return self.__note

    @property
    def note_url( self ):
        self.__completeIfNeeded( self.__note_url )
        return self.__note_url

    @property
    def scopes( self ):
        self.__completeIfNeeded( self.__scopes )
        return self.__scopes

    @property
    def token( self ):
        self.__completeIfNeeded( self.__token )
        return self.__token

    @property
    def updated_at( self ):
        self.__completeIfNeeded( self.__updated_at )
        return self.__updated_at

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def delete( self ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ),
            None,
            None
        )

    def edit( self, scopes = DefaultValueForOptionalParameters, add_scopes = DefaultValueForOptionalParameters, remove_scopes = DefaultValueForOptionalParameters, note = DefaultValueForOptionalParameters, note_url = DefaultValueForOptionalParameters ):
        post_parameters = {
        }
        if scopes is not DefaultValueForOptionalParameters:
            post_parameters[ "scopes" ] = scopes
        if add_scopes is not DefaultValueForOptionalParameters:
            post_parameters[ "add_scopes" ] = add_scopes
        if remove_scopes is not DefaultValueForOptionalParameters:
            post_parameters[ "remove_scopes" ] = remove_scopes
        if note is not DefaultValueForOptionalParameters:
            post_parameters[ "note" ] = note
        if note_url is not DefaultValueForOptionalParameters:
            post_parameters[ "note_url" ] = note_url
        status, headers, data = self.__requester.request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self.__useAttributes( data )

    def __initAttributes( self ):
        self.__app = None
        self.__created_at = None
        self.__id = None
        self.__note = None
        self.__note_url = None
        self.__scopes = None
        self.__token = None
        self.__updated_at = None
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
        if "app" in attributes:
            self.__app = attributes[ "app" ]
        if "created_at" in attributes:
            self.__created_at = attributes[ "created_at" ]
        if "id" in attributes:
            self.__id = attributes[ "id" ]
        if "note" in attributes:
            self.__note = attributes[ "note" ]
        if "note_url" in attributes:
            self.__note_url = attributes[ "note_url" ]
        if "scopes" in attributes:
            self.__scopes = attributes[ "scopes" ]
        if "token" in attributes:
            self.__token = attributes[ "token" ]
        if "updated_at" in attributes:
            self.__updated_at = attributes[ "updated_at" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
