# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
##########
import GitAuthor
import GitObject

class GitTag( GithubObject.GithubObject ):
    @property
    def message( self ):
        self._completeIfNeeded( self._message )
        return self._message

    @property
    def object( self ):
        self._completeIfNeeded( self._object )
        return self._object

    @property
    def sha( self ):
        self._completeIfNeeded( self._sha )
        return self._sha

    @property
    def tag( self ):
        self._completeIfNeeded( self._tag )
        return self._tag

    @property
    def tagger( self ):
        self._completeIfNeeded( self._tagger )
        return self._tagger

    @property
    def url( self ):
        self._completeIfNeeded( self._url )
        return self._url

    def _initAttributes( self ):
        self._message = None
        self._object = None
        self._sha = None
        self._tag = None
        self._tagger = None
        self._url = None

    def _useAttributes( self, attributes ):
        if "message" in attributes and attributes[ "message" ] is not None: # pragma no branch
            assert isinstance( attributes[ "message" ], ( str, unicode ) ), attributes[ "message" ]
            self._message = attributes[ "message" ]
        if "object" in attributes and attributes[ "object" ] is not None: # pragma no branch
            assert isinstance( attributes[ "object" ], dict ), attributes[ "object" ]
            self._object = GitObject.GitObject( self._requester, attributes[ "object" ], completed = False )
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self._sha = attributes[ "sha" ]
        if "tag" in attributes and attributes[ "tag" ] is not None: # pragma no branch
            assert isinstance( attributes[ "tag" ], ( str, unicode ) ), attributes[ "tag" ]
            self._tag = attributes[ "tag" ]
        if "tagger" in attributes and attributes[ "tagger" ] is not None: # pragma no branch
            assert isinstance( attributes[ "tagger" ], dict ), attributes[ "tagger" ]
            self._tagger = GitAuthor.GitAuthor( self._requester, attributes[ "tagger" ], completed = False )
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
