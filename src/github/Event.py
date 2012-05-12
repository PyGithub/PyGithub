# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import Organization
import Repository
import NamedUser

class Event( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__completed = completion != LazyCompletion
        self.__initAttributes()
        self.__useAttributes( attributes )
        if completion == ImmediateCompletion:
            self.__complete()

    @property
    def actor( self ):
        self.__completeIfNeeded( self.__actor )
        return self.__actor

    @property
    def commit_id( self ):
        self.__completeIfNeeded( self.__commit_id )
        return self.__commit_id

    @property
    def created_at( self ):
        self.__completeIfNeeded( self.__created_at )
        return self.__created_at

    @property
    def event( self ):
        self.__completeIfNeeded( self.__event )
        return self.__event

    @property
    def id( self ):
        self.__completeIfNeeded( self.__id )
        return self.__id

    @property
    def issue( self ):
        self.__completeIfNeeded( self.__issue )
        return self.__issue

    @property
    def org( self ):
        self.__completeIfNeeded( self.__org )
        return self.__org

    @property
    def payload( self ):
        self.__completeIfNeeded( self.__payload )
        return self.__payload

    @property
    def public( self ):
        self.__completeIfNeeded( self.__public )
        return self.__public

    @property
    def repo( self ):
        self.__completeIfNeeded( self.__repo )
        return self.__repo

    @property
    def type( self ):
        self.__completeIfNeeded( self.__type )
        return self.__type

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def __initAttributes( self ):
        self.__actor = None
        self.__commit_id = None
        self.__created_at = None
        self.__event = None
        self.__id = None
        self.__issue = None
        self.__org = None
        self.__payload = None
        self.__public = None
        self.__repo = None
        self.__type = None
        self.__url = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete()

    def __complete( self ):
        status, headers, data = self.__requester.request(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( data )
        self.__completed = True

    def __useAttributes( self, attributes ):
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "actor", "commit_id", "created_at", "event", "id", "issue", "org", "payload", "public", "repo", "type", "url", ], attribute
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "actor" in attributes and attributes[ "actor" ] is not None:
            assert isinstance( attributes[ "actor" ], dict )
            self.__actor = NamedUser.NamedUser( self.__requester, attributes[ "actor" ], completion = LazyCompletion )
        if "commit_id" in attributes and attributes[ "commit_id" ] is not None:
            self.__commit_id = attributes[ "commit_id" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None:
            self.__created_at = attributes[ "created_at" ]
        if "event" in attributes and attributes[ "event" ] is not None:
            self.__event = attributes[ "event" ]
        if "id" in attributes and attributes[ "id" ] is not None:
            self.__id = attributes[ "id" ]
        if "issue" in attributes and attributes[ "issue" ] is not None:
            self.__issue = attributes[ "issue" ]
        if "org" in attributes and attributes[ "org" ] is not None:
            assert isinstance( attributes[ "org" ], dict )
            self.__org = Organization.Organization( self.__requester, attributes[ "org" ], completion = LazyCompletion )
        if "payload" in attributes and attributes[ "payload" ] is not None:
            self.__payload = attributes[ "payload" ]
        if "public" in attributes and attributes[ "public" ] is not None:
            self.__public = attributes[ "public" ]
        if "repo" in attributes and attributes[ "repo" ] is not None:
            assert isinstance( attributes[ "repo" ], dict )
            self.__repo = Repository.Repository( self.__requester, attributes[ "repo" ], completion = LazyCompletion )
        if "type" in attributes and attributes[ "type" ] is not None:
            self.__type = attributes[ "type" ]
        if "url" in attributes and attributes[ "url" ] is not None:
            self.__url = attributes[ "url" ]
