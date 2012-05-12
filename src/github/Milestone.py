# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import NamedUser
import Label

class Milestone( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__completed = completion != LazyCompletion
        self.__initAttributes()
        self.__useAttributes( attributes )
        if completion == ImmediateCompletion:
            self.__complete()

    @property
    def closed_issues( self ):
        self.__completeIfNeeded( self.__closed_issues )
        return self.__closed_issues

    @property
    def created_at( self ):
        self.__completeIfNeeded( self.__created_at )
        return self.__created_at

    @property
    def creator( self ):
        self.__completeIfNeeded( self.__creator )
        return self.__creator

    @property
    def description( self ):
        self.__completeIfNeeded( self.__description )
        return self.__description

    @property
    def due_on( self ):
        self.__completeIfNeeded( self.__due_on )
        return self.__due_on

    @property
    def number( self ):
        self.__completeIfNeeded( self.__number )
        return self.__number

    @property
    def open_issues( self ):
        self.__completeIfNeeded( self.__open_issues )
        return self.__open_issues

    @property
    def state( self ):
        self.__completeIfNeeded( self.__state )
        return self.__state

    @property
    def title( self ):
        self.__completeIfNeeded( self.__title )
        return self.__title

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def delete( self ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ),
            None,
            None
        )

    def edit( self, title, state = DefaultValueForOptionalParameters, description = DefaultValueForOptionalParameters, due_on = DefaultValueForOptionalParameters ):
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
        self.__number = None
        self.__open_issues = None
        self.__state = None
        self.__title = None
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
            assert attribute in [ "closed_issues", "created_at", "creator", "description", "due_on", "number", "open_issues", "state", "title", "url", ]
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "closed_issues" in attributes and attributes[ "closed_issues" ] is not None:
            self.__closed_issues = attributes[ "closed_issues" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None:
            self.__created_at = attributes[ "created_at" ]
        if "creator" in attributes and attributes[ "creator" ] is not None:
            assert isinstance( attributes[ "creator" ], dict )
            self.__creator = NamedUser.NamedUser( self.__requester, attributes[ "creator" ], completion = LazyCompletion )
        if "description" in attributes and attributes[ "description" ] is not None:
            self.__description = attributes[ "description" ]
        if "due_on" in attributes and attributes[ "due_on" ] is not None:
            self.__due_on = attributes[ "due_on" ]
        if "number" in attributes and attributes[ "number" ] is not None:
            self.__number = attributes[ "number" ]
        if "open_issues" in attributes and attributes[ "open_issues" ] is not None:
            self.__open_issues = attributes[ "open_issues" ]
        if "state" in attributes and attributes[ "state" ] is not None:
            self.__state = attributes[ "state" ]
        if "title" in attributes and attributes[ "title" ] is not None:
            self.__title = attributes[ "title" ]
        if "url" in attributes and attributes[ "url" ] is not None:
            self.__url = attributes[ "url" ]
