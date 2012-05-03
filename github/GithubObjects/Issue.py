# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import IssueComment
import IssueEvent
import NamedUser
import Milestone
import Label

class Issue( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def assignee( self ):
        self.__completeIfNeeded( self.__assignee )
        return self.__assignee

    @property
    def body( self ):
        self.__completeIfNeeded( self.__body )
        return self.__body

    @property
    def closed_at( self ):
        self.__completeIfNeeded( self.__closed_at )
        return self.__closed_at

    @property
    def closed_by( self ):
        self.__completeIfNeeded( self.__closed_by )
        return self.__closed_by

    @property
    def comments( self ):
        self.__completeIfNeeded( self.__comments )
        return self.__comments

    @property
    def created_at( self ):
        self.__completeIfNeeded( self.__created_at )
        return self.__created_at

    @property
    def html_url( self ):
        self.__completeIfNeeded( self.__html_url )
        return self.__html_url

    @property
    def id( self ):
        self.__completeIfNeeded( self.__id )
        return self.__id

    @property
    def labels( self ):
        self.__completeIfNeeded( self.__labels )
        return self.__labels

    @property
    def milestone( self ):
        self.__completeIfNeeded( self.__milestone )
        return self.__milestone

    @property
    def number( self ):
        self.__completeIfNeeded( self.__number )
        return self.__number

    @property
    def pull_request( self ):
        self.__completeIfNeeded( self.__pull_request )
        return self.__pull_request

    @property
    def state( self ):
        self.__completeIfNeeded( self.__state )
        return self.__state

    @property
    def title( self ):
        self.__completeIfNeeded( self.__title )
        return self.__title

    @property
    def updated_at( self ):
        self.__completeIfNeeded( self.__updated_at )
        return self.__updated_at

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    @property
    def user( self ):
        self.__completeIfNeeded( self.__user )
        return self.__user

    def __initAttributes( self ):
        self.__assignee = None
        self.__body = None
        self.__closed_at = None
        self.__closed_by = None
        self.__comments = None
        self.__created_at = None
        self.__html_url = None
        self.__id = None
        self.__labels = None
        self.__milestone = None
        self.__number = None
        self.__pull_request = None
        self.__state = None
        self.__title = None
        self.__updated_at = None
        self.__url = None
        self.__user = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete()
        self.__completed = True

    # @todo Do not generate __complete if type has no url attribute
    def __complete( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url,
            None,
            None
        )
        self.__useAttributes( result )

    def add_to_labels( self, *labels ):
        pass

    def create_comment( self, body ):
        pass

    def delete_labels( self ):
        pass

    def edit( self, title = None, body = None, assignee = None, state = None, milestone = None, labels = None ):
        pass

    def get_comment( self, id ):
        pass

    def get_comments( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/comments",
            None,
            None
        )
        return [
            IssueComment.IssueComment( self.__github, element, lazy = True )
            for element in result
        ]

    def get_events( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/events",
            None,
            None
        )
        return [
            IssueEvent.IssueEvent( self.__github, element, lazy = True )
            for element in result
        ]

    def get_labels( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/labels",
            None,
            None
        )
        return [
            Label.Label( self.__github, element, lazy = True )
            for element in result
        ]

    def remove_from_labels( self, label ):
        pass

    def set_labels( self, *labels ):
        pass

    def __useAttributes( self, attributes ):
        if "assignee" in attributes:
            self.__assignee = attributes[ "assignee" ]
        if "body" in attributes:
            self.__body = attributes[ "body" ]
        if "closed_at" in attributes:
            self.__closed_at = attributes[ "closed_at" ]
        if "closed_by" in attributes:
            self.__closed_by = attributes[ "closed_by" ]
        if "comments" in attributes:
            self.__comments = attributes[ "comments" ]
        if "created_at" in attributes:
            self.__created_at = attributes[ "created_at" ]
        if "html_url" in attributes:
            self.__html_url = attributes[ "html_url" ]
        if "id" in attributes:
            self.__id = attributes[ "id" ]
        if "labels" in attributes:
            self.__labels = attributes[ "labels" ]
        if "milestone" in attributes:
            self.__milestone = attributes[ "milestone" ]
        if "number" in attributes:
            self.__number = attributes[ "number" ]
        if "pull_request" in attributes:
            self.__pull_request = attributes[ "pull_request" ]
        if "state" in attributes:
            self.__state = attributes[ "state" ]
        if "title" in attributes:
            self.__title = attributes[ "title" ]
        if "updated_at" in attributes:
            self.__updated_at = attributes[ "updated_at" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
        if "user" in attributes:
            self.__user = attributes[ "user" ]
