# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class Authorization( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

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

    def edit( self, scopes = None, add_scopes = None, remove_scopes = None, note = None, note_url = None ):
        post_parameters = {
        }
        if scopes is not None:
            post_parameters[ "scopes" ] = scopes
        if add_scopes is not None:
            post_parameters[ "add_scopes" ] = add_scopes
        if remove_scopes is not None:
            post_parameters[ "remove_scopes" ] = remove_scopes
        if note is not None:
            post_parameters[ "note" ] = note
        if note_url is not None:
            post_parameters[ "note_url" ] = note_url
        result = self.__github._dataRequest(
            "PATCH",
            "https://api.github.com/user",
            None,
            post_parameters
        )
        self.__useAttributes( result )

    def __useAttributes( self, attributes ):
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
