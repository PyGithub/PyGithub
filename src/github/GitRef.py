# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters
##########
import GitObject

class GitRef( GithubObject.GithubObject ):
    @property
    def object( self ):
        return self._object

    @property
    def ref( self ):
        return self._ref

    @property
    def url( self ):
        return self._url

    def delete( self ):
        status, headers, data = self._request(
            "DELETE",
            str( self.url ),
            None,
            None
        )
        self._checkStatus( status, data )

    def edit( self, sha, force = DefaultValueForOptionalParameters ):
        assert isinstance( sha, ( str, unicode ) ), sha
        if force is not DefaultValueForOptionalParameters:
            assert isinstance( force, bool ), force
        post_parameters = {
            "sha": sha,
        }
        if force is not DefaultValueForOptionalParameters:
            post_parameters[ "force" ] = force
        status, headers, data = self._request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        self._useAttributes( data )

    def _initAttributes( self ):
        self._object = None
        self._ref = None
        self._url = None

    def _useAttributes( self, attributes ):
        if "object" in attributes and attributes[ "object" ] is not None: # pragma no branch
            assert isinstance( attributes[ "object" ], dict ), attributes[ "object" ]
            self._object = GitObject.GitObject( self._requester, attributes[ "object" ], completed = False )
        if "ref" in attributes and attributes[ "ref" ] is not None: # pragma no branch
            assert isinstance( attributes[ "ref" ], ( str, unicode ) ), attributes[ "ref" ]
            self._ref = attributes[ "ref" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
