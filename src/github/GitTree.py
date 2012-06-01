# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
##########
import GitTreeElement

class GitTree( GithubObject.GithubObject ):
    @property
    def sha( self ):
        self._completeIfNotSet( self._sha )
        return self._NoneIfNotSet( self._sha )

    @property
    def tree( self ):
        self._completeIfNotSet( self._tree )
        return self._NoneIfNotSet( self._tree )

    @property
    def url( self ):
        self._completeIfNotSet( self._url )
        return self._NoneIfNotSet( self._url )

    @property
    def _identity( self ):
        return self.sha

    def _initAttributes( self ):
        self._sha = GithubObject.NotSet
        self._tree = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "sha" in attributes: # pragma no branch
            assert attributes[ "sha" ] is None or isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self._sha = attributes[ "sha" ]
        if "tree" in attributes: # pragma no branch
            assert attributes[ "tree" ] is None or all( isinstance( element, dict ) for element in attributes[ "tree" ] ), attributes[ "tree" ]
            self._tree = None if attributes[ "tree" ] is None else [
                GitTreeElement.GitTreeElement( self._requester, element, completed = False )
                for element in attributes[ "tree" ]
            ]
        if "url" in attributes: # pragma no branch
            assert attributes[ "url" ] is None or isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
