# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import Issue
import NamedUser

class IssueEvent( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )
        self.__completed = completion != LazyCompletion
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
            assert attribute in [ "actor", "commit_id", "created_at", "event", "id", "issue", "url", ], attribute
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "actor" in attributes and attributes[ "actor" ] is not None:
            assert isinstance( attributes[ "actor" ], dict )
            self.__actor = NamedUser.NamedUser( self.__requester, attributes[ "actor" ], completion = LazyCompletion )
        if "commit_id" in attributes and attributes[ "commit_id" ] is not None:
            assert isinstance( attributes[ "commit_id" ], ( str, unicode ) )
            self.__commit_id = attributes[ "commit_id" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None:
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) )
            self.__created_at = attributes[ "created_at" ]
        if "event" in attributes and attributes[ "event" ] is not None:
            assert isinstance( attributes[ "event" ], ( str, unicode ) )
            self.__event = attributes[ "event" ]
        if "id" in attributes and attributes[ "id" ] is not None:
            assert isinstance( attributes[ "id" ], int )
            self.__id = attributes[ "id" ]
        if "issue" in attributes and attributes[ "issue" ] is not None:
            assert isinstance( attributes[ "issue" ], dict )
            self.__issue = Issue.Issue( self.__requester, attributes[ "issue" ], completion = LazyCompletion )
        if "url" in attributes and attributes[ "url" ] is not None:
            assert isinstance( attributes[ "url" ], ( str, unicode ) )
            self.__url = attributes[ "url" ]
