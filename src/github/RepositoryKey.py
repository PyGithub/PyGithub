# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters

class RepositoryKey( GithubObject.GithubObject ):
    def __init__( self, requester, attributes, completed, repoUrl ):
        GithubObject.GithubObject.__init__( self, requester, attributes, completed )
        self.__repoUrl = repoUrl

    @property
    def __customUrl( self ):
        return self.__repoUrl + "/keys/" + str( self.id )

    @property
    def id( self ):
        return self._id

    @property
    def key( self ):
        return self._key

    @property
    def title( self ):
        return self._title

    @property
    def url( self ):
        return self._url

    @property
    def verified( self ):
        return self._verified

    def delete( self ):
        status, headers, data = self._request(
            "DELETE",
            self.__customUrl,
            None,
            None
        )
        self._checkStatus( status, data )

    def edit( self, title = DefaultValueForOptionalParameters, key = DefaultValueForOptionalParameters ):
        if title is not DefaultValueForOptionalParameters:
            assert isinstance( title, ( str, unicode ) ), title
        if key is not DefaultValueForOptionalParameters:
            assert isinstance( key, ( str, unicode ) ), key
        post_parameters = dict()
        if title is not DefaultValueForOptionalParameters:
            post_parameters[ "title" ] = title
        if key is not DefaultValueForOptionalParameters:
            post_parameters[ "key" ] = key
        status, headers, data = self._request(
            "PATCH",
            self.__customUrl,
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        self._useAttributes( data )

    def _initAttributes( self ):
        self._id = None
        self._key = None
        self._title = None
        self._url = None
        self._verified = None

    def _useAttributes( self, attributes ):
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "key" in attributes and attributes[ "key" ] is not None: # pragma no branch
            assert isinstance( attributes[ "key" ], ( str, unicode ) ), attributes[ "key" ]
            self._key = attributes[ "key" ]
        if "title" in attributes and attributes[ "title" ] is not None: # pragma no branch
            assert isinstance( attributes[ "title" ], ( str, unicode ) ), attributes[ "title" ]
            self._title = attributes[ "title" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
        if "verified" in attributes and attributes[ "verified" ] is not None: # pragma no branch
            assert isinstance( attributes[ "verified" ], bool ), attributes[ "verified" ]
            self._verified = attributes[ "verified" ]
