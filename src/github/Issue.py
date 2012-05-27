# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import Repository
import IssueEvent
import NamedUser
import Milestone
import IssueComment
import Label

class Issue( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )
        self.__completed = completion != LazyCompletion
        if completion == ImmediateCompletion:
            self.__complete() # pragma: no cover

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
    def repository( self ):
        self.__completeIfNeeded( self.__repository )
        return self.__repository

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

    def add_to_labels( self, *labels ):
        post_parameters = [ label.name for label in labels ]
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/labels",
            None,
            post_parameters
        )

    def create_comment( self, body ):
        post_parameters = {
            "body": body,
        }
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/comments",
            None,
            post_parameters
        )
        return IssueComment.IssueComment( self.__requester, data, completion = NoCompletion )

    def delete_labels( self ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ) + "/labels",
            None,
            None
        )

    def edit( self, title = DefaultValueForOptionalParameters, body = DefaultValueForOptionalParameters, assignee = DefaultValueForOptionalParameters, state = DefaultValueForOptionalParameters, milestone = DefaultValueForOptionalParameters, labels = DefaultValueForOptionalParameters ):
        post_parameters = {
        }
        if title is not DefaultValueForOptionalParameters:
            post_parameters[ "title" ] = title
        if body is not DefaultValueForOptionalParameters:
            post_parameters[ "body" ] = body
        if assignee is not DefaultValueForOptionalParameters:
            post_parameters[ "assignee" ] = assignee
        if state is not DefaultValueForOptionalParameters:
            post_parameters[ "state" ] = state
        if milestone is not DefaultValueForOptionalParameters:
            post_parameters[ "milestone" ] = milestone
        if labels is not DefaultValueForOptionalParameters:
            post_parameters[ "labels" ] = labels
        status, headers, data = self.__requester.request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self.__useAttributes( data )

    def get_comment( self, id ):
        status, headers, data = self.__requester.request(
            "GET",
            "https://api.github.com/repos/jacquev6/PyGithub/issues/comments" + "/" + str( id ), ### @todo
            None,
            None
        )
        return IssueComment.IssueComment( self.__requester, data, completion = NoCompletion )

    def get_comments( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/comments",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            IssueComment.IssueComment,
            self.__requester,
            headers,
            data
        )

    def get_events( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/events",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            IssueEvent.IssueEvent,
            self.__requester,
            headers,
            data
        )

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

    def remove_from_labels( self, label ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ) + "/labels" + "/" + str( label._identity ),
            None,
            None
        )

    def set_labels( self, *labels ):
        post_parameters = [ label.name for label in labels ]
        status, headers, data = self.__requester.request(
            "PUT",
            str( self.url ) + "/labels",
            None,
            post_parameters
        )

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
        self.__repository = None
        self.__state = None
        self.__title = None
        self.__updated_at = None
        self.__url = None
        self.__user = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete() # pragma: no cover

    def __complete( self ): # pragma: no cover
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
            assert attribute in [ "assignee", "body", "closed_at", "closed_by", "comments", "created_at", "html_url", "id", "labels", "milestone", "number", "pull_request", "repository", "state", "title", "updated_at", "url", "user", ], attribute
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "assignee" in attributes and attributes[ "assignee" ] is not None: # pragma no branch
            assert isinstance( attributes[ "assignee" ], dict )
            self.__assignee = NamedUser.NamedUser( self.__requester, attributes[ "assignee" ], completion = LazyCompletion )
        if "body" in attributes and attributes[ "body" ] is not None: # pragma no branch
            assert isinstance( attributes[ "body" ], ( str, unicode ) )
            self.__body = attributes[ "body" ]
        if "closed_at" in attributes and attributes[ "closed_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "closed_at" ], ( str, unicode ) )
            self.__closed_at = attributes[ "closed_at" ]
        if "closed_by" in attributes and attributes[ "closed_by" ] is not None: # pragma no branch
            assert isinstance( attributes[ "closed_by" ], dict )
            self.__closed_by = NamedUser.NamedUser( self.__requester, attributes[ "closed_by" ], completion = LazyCompletion )
        if "comments" in attributes and attributes[ "comments" ] is not None: # pragma no branch
            assert isinstance( attributes[ "comments" ], int )
            self.__comments = attributes[ "comments" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) )
            self.__created_at = attributes[ "created_at" ]
        if "html_url" in attributes and attributes[ "html_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "html_url" ], ( str, unicode ) )
            self.__html_url = attributes[ "html_url" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int )
            self.__id = attributes[ "id" ]
        if "labels" in attributes and attributes[ "labels" ] is not None: # pragma no branch
            assert isinstance( attributes[ "labels" ], list ) and ( len( attributes[ "labels" ] ) == 0 or isinstance( attributes[ "labels" ][ 0 ], dict ) )
            self.__labels = [
                Label.Label( self.__requester, element, completion = LazyCompletion )
                for element in attributes[ "labels" ]
            ]
        if "milestone" in attributes and attributes[ "milestone" ] is not None: # pragma no branch
            assert isinstance( attributes[ "milestone" ], dict )
            self.__milestone = Milestone.Milestone( self.__requester, attributes[ "milestone" ], completion = LazyCompletion )
        if "number" in attributes and attributes[ "number" ] is not None: # pragma no branch
            assert isinstance( attributes[ "number" ], int )
            self.__number = attributes[ "number" ]
        if "pull_request" in attributes and attributes[ "pull_request" ] is not None: # pragma no branch
            self.__pull_request = attributes[ "pull_request" ]
        if "repository" in attributes and attributes[ "repository" ] is not None: # pragma no branch
            assert isinstance( attributes[ "repository" ], dict )
            self.__repository = Repository.Repository( self.__requester, attributes[ "repository" ], completion = LazyCompletion )
        if "state" in attributes and attributes[ "state" ] is not None: # pragma no branch
            assert isinstance( attributes[ "state" ], ( str, unicode ) )
            self.__state = attributes[ "state" ]
        if "title" in attributes and attributes[ "title" ] is not None: # pragma no branch
            assert isinstance( attributes[ "title" ], ( str, unicode ) )
            self.__title = attributes[ "title" ]
        if "updated_at" in attributes and attributes[ "updated_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "updated_at" ], ( str, unicode ) )
            self.__updated_at = attributes[ "updated_at" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) )
            self.__url = attributes[ "url" ]
        if "user" in attributes and attributes[ "user" ] is not None: # pragma no branch
            assert isinstance( attributes[ "user" ], dict )
            self.__user = NamedUser.NamedUser( self.__requester, attributes[ "user" ], completion = LazyCompletion )
