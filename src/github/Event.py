# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
##########
import Organization
import Repository
import NamedUser

class Event( GithubObject.BasicGithubObject ):
    @property
    def actor( self ):
        return self._actor

    @property
    def created_at( self ):
        return self._created_at

    @property
    def id( self ):
        return self._id

    @property
    def org( self ):
        return self._org

    @property
    def payload( self ):
        return self._payload

    @property
    def public( self ):
        return self._public

    @property
    def repo( self ):
        return self._repo

    @property
    def type( self ):
        return self._type

    def _initAttributes( self ):
        self._actor = None
        self._created_at = None
        self._id = None
        self._org = None
        self._payload = None
        self._public = None
        self._repo = None
        self._type = None

    def _useAttributes( self, attributes ):
        if "actor" in attributes and attributes[ "actor" ] is not None: # pragma no branch
            assert isinstance( attributes[ "actor" ], dict ), attributes[ "actor" ]
            self._actor = NamedUser.NamedUser( self._requester, attributes[ "actor" ], completed = False )
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self._created_at = attributes[ "created_at" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], ( str, unicode ) ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "org" in attributes and attributes[ "org" ] is not None: # pragma no branch
            assert isinstance( attributes[ "org" ], dict ), attributes[ "org" ]
            self._org = Organization.Organization( self._requester, attributes[ "org" ], completed = False )
        if "payload" in attributes and attributes[ "payload" ] is not None: # pragma no branch
            self._payload = attributes[ "payload" ]
        if "public" in attributes and attributes[ "public" ] is not None: # pragma no branch
            assert isinstance( attributes[ "public" ], bool ), attributes[ "public" ]
            self._public = attributes[ "public" ]
        if "repo" in attributes and attributes[ "repo" ] is not None: # pragma no branch
            assert isinstance( attributes[ "repo" ], dict ), attributes[ "repo" ]
            self._repo = Repository.Repository( self._requester, attributes[ "repo" ], completed = False )
        if "type" in attributes and attributes[ "type" ] is not None: # pragma no branch
            assert isinstance( attributes[ "type" ], ( str, unicode ) ), attributes[ "type" ]
            self._type = attributes[ "type" ]
