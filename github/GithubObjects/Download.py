# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class Download( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def accesskeyid( self ):
        self.__completeIfNeeded( self.__accesskeyid )
        return self.__accesskeyid

    @property
    def acl( self ):
        self.__completeIfNeeded( self.__acl )
        return self.__acl

    @property
    def bucket( self ):
        self.__completeIfNeeded( self.__bucket )
        return self.__bucket

    @property
    def content_type( self ):
        self.__completeIfNeeded( self.__content_type )
        return self.__content_type

    @property
    def created_at( self ):
        self.__completeIfNeeded( self.__created_at )
        return self.__created_at

    @property
    def description( self ):
        self.__completeIfNeeded( self.__description )
        return self.__description

    @property
    def download_count( self ):
        self.__completeIfNeeded( self.__download_count )
        return self.__download_count

    @property
    def expirationdate( self ):
        self.__completeIfNeeded( self.__expirationdate )
        return self.__expirationdate

    @property
    def html_url( self ):
        self.__completeIfNeeded( self.__html_url )
        return self.__html_url

    @property
    def id( self ):
        self.__completeIfNeeded( self.__id )
        return self.__id

    @property
    def mime_type( self ):
        self.__completeIfNeeded( self.__mime_type )
        return self.__mime_type

    @property
    def name( self ):
        self.__completeIfNeeded( self.__name )
        return self.__name

    @property
    def path( self ):
        self.__completeIfNeeded( self.__path )
        return self.__path

    @property
    def policy( self ):
        self.__completeIfNeeded( self.__policy )
        return self.__policy

    @property
    def prefix( self ):
        self.__completeIfNeeded( self.__prefix )
        return self.__prefix

    @property
    def redirect( self ):
        self.__completeIfNeeded( self.__redirect )
        return self.__redirect

    @property
    def s3_url( self ):
        self.__completeIfNeeded( self.__s3_url )
        return self.__s3_url

    @property
    def signature( self ):
        self.__completeIfNeeded( self.__signature )
        return self.__signature

    @property
    def size( self ):
        self.__completeIfNeeded( self.__size )
        return self.__size

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def __initAttributes( self ):
        self.__accesskeyid = None
        self.__acl = None
        self.__bucket = None
        self.__content_type = None
        self.__created_at = None
        self.__description = None
        self.__download_count = None
        self.__expirationdate = None
        self.__html_url = None
        self.__id = None
        self.__mime_type = None
        self.__name = None
        self.__path = None
        self.__policy = None
        self.__prefix = None
        self.__redirect = None
        self.__s3_url = None
        self.__signature = None
        self.__size = None
        self.__url = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete()

    # @todo Do not generate __complete if type has no url attribute
    def __complete( self ):
        result = self.__github._dataRequest(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( result )
        self.__completed = True

    def delete( self ):
        pass

    def __useAttributes( self, attributes ):
        if "accesskeyid" in attributes:
            self.__accesskeyid = attributes[ "accesskeyid" ]
        if "acl" in attributes:
            self.__acl = attributes[ "acl" ]
        if "bucket" in attributes:
            self.__bucket = attributes[ "bucket" ]
        if "content_type" in attributes:
            self.__content_type = attributes[ "content_type" ]
        if "created_at" in attributes:
            self.__created_at = attributes[ "created_at" ]
        if "description" in attributes:
            self.__description = attributes[ "description" ]
        if "download_count" in attributes:
            self.__download_count = attributes[ "download_count" ]
        if "expirationdate" in attributes:
            self.__expirationdate = attributes[ "expirationdate" ]
        if "html_url" in attributes:
            self.__html_url = attributes[ "html_url" ]
        if "id" in attributes:
            self.__id = attributes[ "id" ]
        if "mime_type" in attributes:
            self.__mime_type = attributes[ "mime_type" ]
        if "name" in attributes:
            self.__name = attributes[ "name" ]
        if "path" in attributes:
            self.__path = attributes[ "path" ]
        if "policy" in attributes:
            self.__policy = attributes[ "policy" ]
        if "prefix" in attributes:
            self.__prefix = attributes[ "prefix" ]
        if "redirect" in attributes:
            self.__redirect = attributes[ "redirect" ]
        if "s3_url" in attributes:
            self.__s3_url = attributes[ "s3_url" ]
        if "signature" in attributes:
            self.__signature = attributes[ "signature" ]
        if "size" in attributes:
            self.__size = attributes[ "size" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
