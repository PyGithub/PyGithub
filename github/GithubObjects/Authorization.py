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
        if self.__app is None:
            self.__completeIfNeeded()
        return self.__app

    @property
    def created_at( self ):
        if self.__created_at is None:
            self.__completeIfNeeded()
        return self.__created_at

    @property
    def id( self ):
        if self.__id is None:
            self.__completeIfNeeded()
        return self.__id

    @property
    def note( self ):
        if self.__note is None:
            self.__completeIfNeeded()
        return self.__note

    @property
    def note_url( self ):
        if self.__note_url is None:
            self.__completeIfNeeded()
        return self.__note_url

    @property
    def scopes( self ):
        if self.__scopes is None:
            self.__completeIfNeeded()
        return self.__scopes

    @property
    def token( self ):
        if self.__token is None:
            self.__completeIfNeeded()
        return self.__token

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
        self.__app = None
        self.__created_at = None
        self.__id = None
        self.__note = None
        self.__note_url = None
        self.__scopes = None
        self.__token = None
        self.__updated_at = None
        self.__url = None

    def __completeIfNeeded( self ):
        if not self.__completed:
            self.__complete()
        self.__completed = True

    def __complete( self ):
        pass

    def delete( self ):
        pass

    def edit( self, scopes = None, add_scopes = None, remove_scopes = None, note = None, note_url = None ):
        pass

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
