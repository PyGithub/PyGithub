# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
##########
import GitObject

class GitRef( GithubObject.GithubObject ):
    @property
    def object( self ):
        self._completeIfNotSet( self._object )
        return self._NoneIfNotSet( self._object )

    @property
    def ref( self ):
        self._completeIfNotSet( self._ref )
        return self._NoneIfNotSet( self._ref )

    @property
    def url( self ):
        self._completeIfNotSet( self._url )
        return self._NoneIfNotSet( self._url )

    def delete( self ):
        headers, data = self._requester.requestAndCheck(
            "DELETE",
            self.url,
            None,
            None
        )

    def edit( self, sha, force = GithubObject.NotSet ):
        assert isinstance( sha, ( str, unicode ) ), sha
        assert force is GithubObject.NotSet or isinstance( force, bool ), force
        post_parameters = {
            "sha": sha,
        }
        if force is not GithubObject.NotSet:
            post_parameters[ "force" ] = force
        headers, data = self._requester.requestAndCheck(
            "PATCH",
            self.url,
            None,
            post_parameters
        )
        self._useAttributes( data )

    def _initAttributes( self ):
        self._object = GithubObject.NotSet
        self._ref = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "object" in attributes: # pragma no branch
            assert attributes[ "object" ] is None or isinstance( attributes[ "object" ], dict ), attributes[ "object" ]
            self._object = None if attributes[ "object" ] is None else GitObject.GitObject( self._requester, attributes[ "object" ], completed = False )
        if "ref" in attributes: # pragma no branch
            assert attributes[ "ref" ] is None or isinstance( attributes[ "ref" ], ( str, unicode ) ), attributes[ "ref" ]
            self._ref = attributes[ "ref" ]
        if "url" in attributes: # pragma no branch
            assert attributes[ "url" ] is None or isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
