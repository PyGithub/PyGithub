# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class Download( GithubObject.CompletableGithubObject ):
    @property
    def accesskeyid( self ):
        self._completeIfNeeded( self._accesskeyid )
        return self._accesskeyid

    @property
    def acl( self ):
        self._completeIfNeeded( self._acl )
        return self._acl

    @property
    def bucket( self ):
        self._completeIfNeeded( self._bucket )
        return self._bucket

    @property
    def content_type( self ):
        self._completeIfNeeded( self._content_type )
        return self._content_type

    @property
    def created_at( self ):
        self._completeIfNeeded( self._created_at )
        return self._created_at

    @property
    def description( self ):
        self._completeIfNeeded( self._description )
        return self._description

    @property
    def download_count( self ):
        self._completeIfNeeded( self._download_count )
        return self._download_count

    @property
    def expirationdate( self ):
        self._completeIfNeeded( self._expirationdate )
        return self._expirationdate

    @property
    def html_url( self ):
        self._completeIfNeeded( self._html_url )
        return self._html_url

    @property
    def id( self ):
        self._completeIfNeeded( self._id )
        return self._id

    @property
    def mime_type( self ):
        self._completeIfNeeded( self._mime_type )
        return self._mime_type

    @property
    def name( self ):
        self._completeIfNeeded( self._name )
        return self._name

    @property
    def path( self ):
        self._completeIfNeeded( self._path )
        return self._path

    @property
    def policy( self ):
        self._completeIfNeeded( self._policy )
        return self._policy

    @property
    def prefix( self ):
        self._completeIfNeeded( self._prefix )
        return self._prefix

    @property
    def redirect( self ):
        self._completeIfNeeded( self._redirect )
        return self._redirect

    @property
    def s3_url( self ):
        self._completeIfNeeded( self._s3_url )
        return self._s3_url

    @property
    def signature( self ):
        self._completeIfNeeded( self._signature )
        return self._signature

    @property
    def size( self ):
        self._completeIfNeeded( self._size )
        return self._size

    @property
    def url( self ):
        self._completeIfNeeded( self._url )
        return self._url

    def delete( self ):
        status, headers, data = self._request(
            "DELETE",
            str( self.url ),
            None,
            None
        )
        self._checkStatus( status, data )

    def _initAttributes( self ):
        self._accesskeyid = None
        self._acl = None
        self._bucket = None
        self._content_type = None
        self._created_at = None
        self._description = None
        self._download_count = None
        self._expirationdate = None
        self._html_url = None
        self._id = None
        self._mime_type = None
        self._name = None
        self._path = None
        self._policy = None
        self._prefix = None
        self._redirect = None
        self._s3_url = None
        self._signature = None
        self._size = None
        self._url = None

    def _useAttributes( self, attributes ):
        if "accesskeyid" in attributes and attributes[ "accesskeyid" ] is not None: # pragma no branch
            assert isinstance( attributes[ "accesskeyid" ], ( str, unicode ) ), attributes[ "accesskeyid" ]
            self._accesskeyid = attributes[ "accesskeyid" ]
        if "acl" in attributes and attributes[ "acl" ] is not None: # pragma no branch
            assert isinstance( attributes[ "acl" ], ( str, unicode ) ), attributes[ "acl" ]
            self._acl = attributes[ "acl" ]
        if "bucket" in attributes and attributes[ "bucket" ] is not None: # pragma no branch
            assert isinstance( attributes[ "bucket" ], ( str, unicode ) ), attributes[ "bucket" ]
            self._bucket = attributes[ "bucket" ]
        if "content_type" in attributes and attributes[ "content_type" ] is not None: # pragma no branch
            assert isinstance( attributes[ "content_type" ], ( str, unicode ) ), attributes[ "content_type" ]
            self._content_type = attributes[ "content_type" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self._created_at = attributes[ "created_at" ]
        if "description" in attributes and attributes[ "description" ] is not None: # pragma no branch
            assert isinstance( attributes[ "description" ], ( str, unicode ) ), attributes[ "description" ]
            self._description = attributes[ "description" ]
        if "download_count" in attributes and attributes[ "download_count" ] is not None: # pragma no branch
            assert isinstance( attributes[ "download_count" ], int ), attributes[ "download_count" ]
            self._download_count = attributes[ "download_count" ]
        if "expirationdate" in attributes and attributes[ "expirationdate" ] is not None: # pragma no branch
            assert isinstance( attributes[ "expirationdate" ], ( str, unicode ) ), attributes[ "expirationdate" ]
            self._expirationdate = attributes[ "expirationdate" ]
        if "html_url" in attributes and attributes[ "html_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "html_url" ], ( str, unicode ) ), attributes[ "html_url" ]
            self._html_url = attributes[ "html_url" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "mime_type" in attributes and attributes[ "mime_type" ] is not None: # pragma no branch
            assert isinstance( attributes[ "mime_type" ], ( str, unicode ) ), attributes[ "mime_type" ]
            self._mime_type = attributes[ "mime_type" ]
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
        if "path" in attributes and attributes[ "path" ] is not None: # pragma no branch
            assert isinstance( attributes[ "path" ], ( str, unicode ) ), attributes[ "path" ]
            self._path = attributes[ "path" ]
        if "policy" in attributes and attributes[ "policy" ] is not None: # pragma no branch
            assert isinstance( attributes[ "policy" ], ( str, unicode ) ), attributes[ "policy" ]
            self._policy = attributes[ "policy" ]
        if "prefix" in attributes and attributes[ "prefix" ] is not None: # pragma no branch
            assert isinstance( attributes[ "prefix" ], ( str, unicode ) ), attributes[ "prefix" ]
            self._prefix = attributes[ "prefix" ]
        if "redirect" in attributes and attributes[ "redirect" ] is not None: # pragma no branch
            assert isinstance( attributes[ "redirect" ], bool ), attributes[ "redirect" ]
            self._redirect = attributes[ "redirect" ]
        if "s3_url" in attributes and attributes[ "s3_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "s3_url" ], ( str, unicode ) ), attributes[ "s3_url" ]
            self._s3_url = attributes[ "s3_url" ]
        if "signature" in attributes and attributes[ "signature" ] is not None: # pragma no branch
            assert isinstance( attributes[ "signature" ], ( str, unicode ) ), attributes[ "signature" ]
            self._signature = attributes[ "signature" ]
        if "size" in attributes and attributes[ "size" ] is not None: # pragma no branch
            assert isinstance( attributes[ "size" ], int ), attributes[ "size" ]
            self._size = attributes[ "size" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
