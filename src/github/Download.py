# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *

class Download( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__completed = completion != LazyCompletion
        self.__initAttributes()
        self.__useAttributes( attributes )
        if completion == ImmediateCompletion:
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

    def delete( self ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ),
            None,
            None
        )

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
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "accesskeyid", "acl", "bucket", "content_type", "created_at", "description", "download_count", "expirationdate", "html_url", "id", "mime_type", "name", "path", "policy", "prefix", "redirect", "s3_url", "signature", "size", "url", ], attribute
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "accesskeyid" in attributes and attributes[ "accesskeyid" ] is not None:
            self.__accesskeyid = attributes[ "accesskeyid" ]
        if "acl" in attributes and attributes[ "acl" ] is not None:
            self.__acl = attributes[ "acl" ]
        if "bucket" in attributes and attributes[ "bucket" ] is not None:
            self.__bucket = attributes[ "bucket" ]
        if "content_type" in attributes and attributes[ "content_type" ] is not None:
            self.__content_type = attributes[ "content_type" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None:
            self.__created_at = attributes[ "created_at" ]
        if "description" in attributes and attributes[ "description" ] is not None:
            self.__description = attributes[ "description" ]
        if "download_count" in attributes and attributes[ "download_count" ] is not None:
            self.__download_count = attributes[ "download_count" ]
        if "expirationdate" in attributes and attributes[ "expirationdate" ] is not None:
            self.__expirationdate = attributes[ "expirationdate" ]
        if "html_url" in attributes and attributes[ "html_url" ] is not None:
            self.__html_url = attributes[ "html_url" ]
        if "id" in attributes and attributes[ "id" ] is not None:
            self.__id = attributes[ "id" ]
        if "mime_type" in attributes and attributes[ "mime_type" ] is not None:
            self.__mime_type = attributes[ "mime_type" ]
        if "name" in attributes and attributes[ "name" ] is not None:
            self.__name = attributes[ "name" ]
        if "path" in attributes and attributes[ "path" ] is not None:
            self.__path = attributes[ "path" ]
        if "policy" in attributes and attributes[ "policy" ] is not None:
            self.__policy = attributes[ "policy" ]
        if "prefix" in attributes and attributes[ "prefix" ] is not None:
            self.__prefix = attributes[ "prefix" ]
        if "redirect" in attributes and attributes[ "redirect" ] is not None:
            self.__redirect = attributes[ "redirect" ]
        if "s3_url" in attributes and attributes[ "s3_url" ] is not None:
            self.__s3_url = attributes[ "s3_url" ]
        if "signature" in attributes and attributes[ "signature" ] is not None:
            self.__signature = attributes[ "signature" ]
        if "size" in attributes and attributes[ "size" ] is not None:
            self.__size = attributes[ "size" ]
        if "url" in attributes and attributes[ "url" ] is not None:
            self.__url = attributes[ "url" ]
