# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
##########
import GitAuthor
import GitCommit
import GitTree

class GitCommit( GithubObject.GithubObject ):
    @property
    def author( self ):
        self._completeIfNotSet( self._author )
        return self._NoneIfNotSet( self._author )

    @property
    def committer( self ):
        self._completeIfNotSet( self._committer )
        return self._NoneIfNotSet( self._committer )

    @property
    def message( self ):
        self._completeIfNotSet( self._message )
        return self._NoneIfNotSet( self._message )

    @property
    def parents( self ):
        self._completeIfNotSet( self._parents )
        return self._NoneIfNotSet( self._parents )

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

    def _initAttributes( self ):
        self._author = GithubObject.NotSet
        self._committer = GithubObject.NotSet
        self._message = GithubObject.NotSet
        self._parents = GithubObject.NotSet
        self._sha = GithubObject.NotSet
        self._tree = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "author" in attributes: # pragma no branch
            assert attributes[ "author" ] is None or isinstance( attributes[ "author" ], dict ), attributes[ "author" ]
            self._author = None if attributes[ "author" ] is None else GitAuthor.GitAuthor( self._requester, attributes[ "author" ], completed = False )
        if "committer" in attributes: # pragma no branch
            assert attributes[ "committer" ] is None or isinstance( attributes[ "committer" ], dict ), attributes[ "committer" ]
            self._committer = None if attributes[ "committer" ] is None else GitAuthor.GitAuthor( self._requester, attributes[ "committer" ], completed = False )
        if "message" in attributes: # pragma no branch
            assert attributes[ "message" ] is None or isinstance( attributes[ "message" ], ( str, unicode ) ), attributes[ "message" ]
            self._message = attributes[ "message" ]
        if "parents" in attributes: # pragma no branch
            assert all( isinstance( element, dict ) for element in attributes[ "parents" ] ), attributes[ "parents" ]
            self._parents = [
                GitCommit( self._requester, element, completed = False )
                for element in attributes[ "parents" ]
            ]
        if "sha" in attributes: # pragma no branch
            assert attributes[ "sha" ] is None or isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self._sha = attributes[ "sha" ]
        if "tree" in attributes: # pragma no branch
            assert attributes[ "tree" ] is None or isinstance( attributes[ "tree" ], dict ), attributes[ "tree" ]
            self._tree = None if attributes[ "tree" ] is None else GitTree.GitTree( self._requester, attributes[ "tree" ], completed = False )
        if "url" in attributes: # pragma no branch
            assert attributes[ "url" ] is None or isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
