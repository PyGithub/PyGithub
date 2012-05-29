# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import NamedUser
import Label

class Milestone( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def closed_issues( self ):
        return self.__closed_issues

    @property
    def created_at( self ):
        return self.__created_at

    @property
    def creator( self ):
        return self.__creator

    @property
    def description( self ):
        return self.__description

    @property
    def due_on( self ):
        return self.__due_on

    @property
    def id( self ):
        return self.__id

    @property
    def number( self ):
        return self.__number

    @property
    def open_issues( self ):
        return self.__open_issues

    @property
    def state( self ):
        return self.__state

    @property
    def title( self ):
        return self.__title

    @property
    def url( self ):
        return self.__url

    def delete( self ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ),
            None,
            None
        )

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
        status, headers, data = self.__requester.request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self.__useAttributes( data )

    def get_labels( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/labels",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Label.Label,
            self.__requester,
            headers,
            data
        )

    def __initAttributes( self ):
        self.__closed_issues = None
        self.__created_at = None
        self.__creator = None
        self.__description = None
        self.__due_on = None
        self.__id = None
        self.__number = None
        self.__open_issues = None
        self.__state = None
        self.__title = None
        self.__url = None

    def __useAttributes( self, attributes ):
        if "closed_issues" in attributes and attributes[ "closed_issues" ] is not None: # pragma no branch
            assert isinstance( attributes[ "closed_issues" ], int ), attributes[ "closed_issues" ]
            self.__closed_issues = attributes[ "closed_issues" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self.__created_at = attributes[ "created_at" ]
        if "creator" in attributes and attributes[ "creator" ] is not None: # pragma no branch
            assert isinstance( attributes[ "creator" ], dict ), attributes[ "creator" ]
            self.__creator = NamedUser.NamedUser( self.__requester, attributes[ "creator" ], completion = LazyCompletion )
        if "description" in attributes and attributes[ "description" ] is not None: # pragma no branch
            assert isinstance( attributes[ "description" ], ( str, unicode ) ), attributes[ "description" ]
            self.__description = attributes[ "description" ]
        if "due_on" in attributes and attributes[ "due_on" ] is not None: # pragma no branch
            assert isinstance( attributes[ "due_on" ], ( str, unicode ) ), attributes[ "due_on" ]
            self.__due_on = attributes[ "due_on" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self.__id = attributes[ "id" ]
        if "number" in attributes and attributes[ "number" ] is not None: # pragma no branch
            assert isinstance( attributes[ "number" ], int ), attributes[ "number" ]
            self.__number = attributes[ "number" ]
        if "open_issues" in attributes and attributes[ "open_issues" ] is not None: # pragma no branch
            assert isinstance( attributes[ "open_issues" ], int ), attributes[ "open_issues" ]
            self.__open_issues = attributes[ "open_issues" ]
        if "state" in attributes and attributes[ "state" ] is not None: # pragma no branch
            assert isinstance( attributes[ "state" ], ( str, unicode ) ), attributes[ "state" ]
            self.__state = attributes[ "state" ]
        if "title" in attributes and attributes[ "title" ] is not None: # pragma no branch
            assert isinstance( attributes[ "title" ], ( str, unicode ) ), attributes[ "title" ]
            self.__title = attributes[ "title" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self.__url = attributes[ "url" ]
