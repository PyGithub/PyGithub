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
        self._completeIfNeeded( self._author )
        return self._author

    @property
    def committer( self ):
        self._completeIfNeeded( self._committer )
        return self._committer

    @property
    def message( self ):
        self._completeIfNeeded( self._message )
        return self._message

    @property
    def parents( self ):
        self._completeIfNeeded( self._parents )
        return self._parents

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
        self._author = None
        self._committer = None
        self._message = None
        self._parents = None
        self._sha = None
        self._tree = None
        self._url = None

    def _useAttributes( self, attributes ):
        if "author" in attributes and attributes[ "author" ] is not None: # pragma no branch
            assert isinstance( attributes[ "author" ], dict ), attributes[ "author" ]
            self._author = GitAuthor.GitAuthor( self._requester, attributes[ "author" ], completed = False )
        if "committer" in attributes and attributes[ "committer" ] is not None: # pragma no branch
            assert isinstance( attributes[ "committer" ], dict ), attributes[ "committer" ]
            self._committer = GitAuthor.GitAuthor( self._requester, attributes[ "committer" ], completed = False )
        if "message" in attributes and attributes[ "message" ] is not None: # pragma no branch
            assert isinstance( attributes[ "message" ], ( str, unicode ) ), attributes[ "message" ]
            self._message = attributes[ "message" ]
        if "parents" in attributes and attributes[ "parents" ] is not None: # pragma no branch
            assert all( isinstance( element, dict ) for element in attributes[ "parents" ] ), attributes[ "parents" ]
            self._parents = [
                GitCommit( self._requester, element, completed = False )
                for element in attributes[ "parents" ]
            ]
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self._sha = attributes[ "sha" ]
        if "tree" in attributes and attributes[ "tree" ] is not None: # pragma no branch
            assert isinstance( attributes[ "tree" ], dict ), attributes[ "tree" ]
            self._tree = GitTree.GitTree( self._requester, attributes[ "tree" ], completed = False )
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
