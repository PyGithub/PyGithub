# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import NamedUser
import Label

class Milestone( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
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
        pass

    def edit( self, title, state = None, description = None, due_on = None ):
        post_parameters = {
            "title": title,
        }
        if state is not None:
            post_parameters[ "state" ] = state
        if description is not None:
            post_parameters[ "description" ] = description
        if due_on is not None:
            post_parameters[ "due_on" ] = due_on
        status, headers, data = self.__requester.request(
            "PATCH",
            "https://api.github.com/user",
            None,
            post_parameters
        )
        self.__useAttributes( data )

    def get_labels( self ):
        status, headers, data = self.__requester.request(
            "GET",
            self.url + "/labels",
            None,
            None
        )
        return [
            Label.Label( self.__requester, element, lazy = True )
            for element in data
        ]

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

    # @todo Do not generate __complete if type has no url attribute
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
         #@todo No need to check if attribute is in attributes when attribute is mandatory
        if "closed_issues" in attributes:
            self.__closed_issues = attributes[ "closed_issues" ]
        if "created_at" in attributes:
            self.__created_at = attributes[ "created_at" ]
        if "creator" in attributes:
            self.__creator = NamedUser.NamedUser( self.__requester, attributes[ "creator" ], lazy = True )
        if "description" in attributes:
            self.__description = attributes[ "description" ]
        if "due_on" in attributes:
            self.__due_on = attributes[ "due_on" ]
        if "number" in attributes:
            self.__number = attributes[ "number" ]
        if "open_issues" in attributes:
            self.__open_issues = attributes[ "open_issues" ]
        if "state" in attributes:
            self.__state = attributes[ "state" ]
        if "title" in attributes:
            self.__title = attributes[ "title" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
