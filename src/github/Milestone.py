# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
import PaginatedList
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters
##########
import NamedUser
import Label

class Milestone( GithubObject.GithubObject ):
    @property
    def closed_issues( self ):
        return self._closed_issues

    @property
    def created_at( self ):
        return self._created_at

    @property
    def creator( self ):
        return self._creator

    @property
    def description( self ):
        return self._description

    @property
    def due_on( self ):
        return self._due_on

    @property
    def id( self ):
        return self._id

    @property
    def number( self ):
        return self._number

    @property
    def open_issues( self ):
        return self._open_issues

    @property
    def state( self ):
        return self._state

    @property
    def title( self ):
        return self._title

    @property
    def url( self ):
        return self._url

    def delete( self ):
        status, headers, data = self._request(
            "DELETE",
            str( self.url ),
            None,
            None
        )
        self._checkStatus( status, data )

    def edit( self, title, state = DefaultValueForOptionalParameters, description = DefaultValueForOptionalParameters, due_on = DefaultValueForOptionalParameters ):
        assert isinstance( title, ( str, unicode ) ), title
        if state is not DefaultValueForOptionalParameters:
            assert isinstance( state, ( str, unicode ) ), state
        if description is not DefaultValueForOptionalParameters:
            assert isinstance( description, ( str, unicode ) ), description
        if due_on is not DefaultValueForOptionalParameters:
            assert isinstance( due_on, ( str, unicode ) ), due_on
        post_parameters = {
            "title": title,
        }
        if state is not DefaultValueForOptionalParameters:
            post_parameters[ "state" ] = state
        if description is not DefaultValueForOptionalParameters:
            post_parameters[ "description" ] = description
        if due_on is not DefaultValueForOptionalParameters:
            post_parameters[ "due_on" ] = due_on
        status, headers, data = self._request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        self._useAttributes( data )

    def get_labels( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/labels",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            Label.Label,
            self._requester,
            headers,
            data
        )

    def _initAttributes( self ):
        self._closed_issues = None
        self._created_at = None
        self._creator = None
        self._description = None
        self._due_on = None
        self._id = None
        self._number = None
        self._open_issues = None
        self._state = None
        self._title = None
        self._url = None

    def _useAttributes( self, attributes ):
        if "closed_issues" in attributes and attributes[ "closed_issues" ] is not None: # pragma no branch
            assert isinstance( attributes[ "closed_issues" ], int ), attributes[ "closed_issues" ]
            self._closed_issues = attributes[ "closed_issues" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self._created_at = attributes[ "created_at" ]
        if "creator" in attributes and attributes[ "creator" ] is not None: # pragma no branch
            assert isinstance( attributes[ "creator" ], dict ), attributes[ "creator" ]
            self._creator = NamedUser.NamedUser( self._requester, attributes[ "creator" ], completed = False )
        if "description" in attributes and attributes[ "description" ] is not None: # pragma no branch
            assert isinstance( attributes[ "description" ], ( str, unicode ) ), attributes[ "description" ]
            self._description = attributes[ "description" ]
        if "due_on" in attributes and attributes[ "due_on" ] is not None: # pragma no branch
            assert isinstance( attributes[ "due_on" ], ( str, unicode ) ), attributes[ "due_on" ]
            self._due_on = attributes[ "due_on" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "number" in attributes and attributes[ "number" ] is not None: # pragma no branch
            assert isinstance( attributes[ "number" ], int ), attributes[ "number" ]
            self._number = attributes[ "number" ]
        if "open_issues" in attributes and attributes[ "open_issues" ] is not None: # pragma no branch
            assert isinstance( attributes[ "open_issues" ], int ), attributes[ "open_issues" ]
            self._open_issues = attributes[ "open_issues" ]
        if "state" in attributes and attributes[ "state" ] is not None: # pragma no branch
            assert isinstance( attributes[ "state" ], ( str, unicode ) ), attributes[ "state" ]
            self._state = attributes[ "state" ]
        if "title" in attributes and attributes[ "title" ] is not None: # pragma no branch
            assert isinstance( attributes[ "title" ], ( str, unicode ) ), attributes[ "title" ]
            self._title = attributes[ "title" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
