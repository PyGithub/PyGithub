# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
##########
import GitTreeElement

class GitTree( GithubObject.GithubObject ):
    @property
    def sha( self ):
        self._completeIfNeeded( self._sha )
        return self._sha

    @property
    def tree( self ):
        self._completeIfNeeded( self._tree )
        return self._tree

    @property
    def url( self ):
        self._completeIfNeeded( self._url )
        return self._url

    def _initAttributes( self ):
        self._sha = None
        self._tree = None
        self._url = None

    def _useAttributes( self, attributes ):
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self._sha = attributes[ "sha" ]
        if "tree" in attributes and attributes[ "tree" ] is not None: # pragma no branch
            assert all( isinstance( element, dict ) for element in attributes[ "tree" ] ), attributes[ "tree" ]
            self._tree = [
                GitTreeElement.GitTreeElement( self._requester, element, completed = False )
                for element in attributes[ "tree" ]
            ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
