# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
##########
import Issue
import NamedUser

class IssueEvent( GithubObject.CompletableGithubObject ):
    @property
    def actor( self ):
        self._completeIfNeeded( self._actor )
        return self._actor

    @property
    def commit_id( self ):
        self._completeIfNeeded( self._commit_id )
        return self._commit_id

    @property
    def created_at( self ):
        self._completeIfNeeded( self._created_at )
        return self._created_at

    @property
    def event( self ):
        self._completeIfNeeded( self._event )
        return self._event

    @property
    def id( self ):
        self._completeIfNeeded( self._id )
        return self._id

    @property
    def issue( self ):
        self._completeIfNeeded( self._issue )
        return self._issue

    @property
    def url( self ):
        self._completeIfNeeded( self._url )
        return self._url

    def _initAttributes( self ):
        self._actor = None
        self._commit_id = None
        self._created_at = None
        self._event = None
        self._id = None
        self._issue = None
        self._url = None

    def _useAttributes( self, attributes ):
        if "actor" in attributes and attributes[ "actor" ] is not None: # pragma no branch
            assert isinstance( attributes[ "actor" ], dict ), attributes[ "actor" ]
            self._actor = NamedUser.NamedUser( self._requester, attributes[ "actor" ], completed = False )
        if "commit_id" in attributes and attributes[ "commit_id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "commit_id" ], ( str, unicode ) ), attributes[ "commit_id" ]
            self._commit_id = attributes[ "commit_id" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self._created_at = attributes[ "created_at" ]
        if "event" in attributes and attributes[ "event" ] is not None: # pragma no branch
            assert isinstance( attributes[ "event" ], ( str, unicode ) ), attributes[ "event" ]
            self._event = attributes[ "event" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "issue" in attributes and attributes[ "issue" ] is not None: # pragma no branch
            assert isinstance( attributes[ "issue" ], dict ), attributes[ "issue" ]
            self._issue = Issue.Issue( self._requester, attributes[ "issue" ], completed = False )
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
