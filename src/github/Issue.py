# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
import PaginatedList
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters
##########
import Repository
import IssueEvent
import Label
import NamedUser
import Milestone
import IssueComment
import IssuePullRequest

class Issue( GithubObject.GithubObject ):
    @property
    def assignee( self ):
        self._completeIfNeeded( self._assignee )
        return self._assignee

    @property
    def body( self ):
        self._completeIfNeeded( self._body )
        return self._body

    @property
    def closed_at( self ):
        self._completeIfNeeded( self._closed_at )
        return self._closed_at

    @property
    def closed_by( self ):
        self._completeIfNeeded( self._closed_by )
        return self._closed_by

    @property
    def comments( self ):
        self._completeIfNeeded( self._comments )
        return self._comments

    @property
    def created_at( self ):
        self._completeIfNeeded( self._created_at )
        return self._created_at

    @property
    def html_url( self ):
        self._completeIfNeeded( self._html_url )
        return self._html_url

    @property
    def id( self ):
        self._completeIfNeeded( self._id )
        return self._id

    @property
    def labels( self ):
        self._completeIfNeeded( self._labels )
        return self._labels

    @property
    def milestone( self ):
        self._completeIfNeeded( self._milestone )
        return self._milestone

    @property
    def number( self ):
        self._completeIfNeeded( self._number )
        return self._number

    @property
    def pull_request( self ):
        self._completeIfNeeded( self._pull_request )
        return self._pull_request

    @property
    def repository( self ):
        self._completeIfNeeded( self._repository )
        return self._repository

    @property
    def state( self ):
        self._completeIfNeeded( self._state )
        return self._state

    @property
    def title( self ):
        self._completeIfNeeded( self._title )
        return self._title

    @property
    def updated_at( self ):
        self._completeIfNeeded( self._updated_at )
        return self._updated_at

    @property
    def url( self ):
        self._completeIfNeeded( self._url )
        return self._url

    @property
    def user( self ):
        self._completeIfNeeded( self._user )
        return self._user

    def add_to_labels( self, *labels ):
        assert all( isinstance( label, Label.Label ) for label in labels ), labels
        post_parameters = [ label._identity for label in labels ]
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/labels",
            None,
            post_parameters
        )
        self._checkStatus( status, data )

    def create_comment( self, body ):
        assert isinstance( body, ( str, unicode ) ), body
        post_parameters = {
            "body": body,
        }
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/comments",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return IssueComment.IssueComment( self._requester, data, completed = True )

    def delete_labels( self ):
        status, headers, data = self._request(
            "DELETE",
            str( self.url ) + "/labels",
            None,
            None
        )
        self._checkStatus( status, data )

    def edit( self, title = DefaultValueForOptionalParameters, body = DefaultValueForOptionalParameters, assignee = DefaultValueForOptionalParameters, state = DefaultValueForOptionalParameters, milestone = DefaultValueForOptionalParameters, labels = DefaultValueForOptionalParameters ):
        if title is not DefaultValueForOptionalParameters:
            assert isinstance( title, ( str, unicode ) ), title
        if body is not DefaultValueForOptionalParameters:
            assert isinstance( body, ( str, unicode ) ), body
        if assignee is not DefaultValueForOptionalParameters:
            assert isinstance( assignee, ( str, unicode ) ), assignee
        if state is not DefaultValueForOptionalParameters:
            assert isinstance( state, ( str, unicode ) ), state
        if milestone is not DefaultValueForOptionalParameters:
            assert isinstance( milestone, int ), milestone
        if labels is not DefaultValueForOptionalParameters:
            assert all( isinstance( element, ( str, unicode ) ) for element in labels ), labels
        post_parameters = dict()
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
        status, headers, data = self._request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        self._useAttributes( data )

    def get_comment( self, id ):
        assert isinstance( id, int ), id
        status, headers, data = self._request(
            "GET",
            self._parentUrl( str( self.url ) ) + "/comments/" + str( id ),
            None,
            None
        )
        self._checkStatus( status, data )
        return IssueComment.IssueComment( self._requester, data, completed = True )

    def get_comments( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/comments",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            IssueComment.IssueComment,
            self._requester,
            headers,
            data
        )

    def get_events( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/events",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            IssueEvent.IssueEvent,
            self._requester,
            headers,
            data
        )

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

    def remove_from_labels( self, label ):
        assert isinstance( label, Label.Label ), label
        status, headers, data = self._request(
            "DELETE",
            str( self.url ) + "/labels/" + str( label._identity ),
            None,
            None
        )
        self._checkStatus( status, data )

    def set_labels( self, *labels ):
        assert all( isinstance( label, Label.Label ) for label in labels ), labels
        post_parameters = [ label._identity for label in labels ]
        status, headers, data = self._request(
            "PUT",
            str( self.url ) + "/labels",
            None,
            post_parameters
        )
        self._checkStatus( status, data )

    def _initAttributes( self ):
        self._assignee = None
        self._body = None
        self._closed_at = None
        self._closed_by = None
        self._comments = None
        self._created_at = None
        self._html_url = None
        self._id = None
        self._labels = None
        self._milestone = None
        self._number = None
        self._pull_request = None
        self._repository = None
        self._state = None
        self._title = None
        self._updated_at = None
        self._url = None
        self._user = None

    def _useAttributes( self, attributes ):
        if "assignee" in attributes and attributes[ "assignee" ] is not None: # pragma no branch
            assert isinstance( attributes[ "assignee" ], dict ), attributes[ "assignee" ]
            self._assignee = NamedUser.NamedUser( self._requester, attributes[ "assignee" ], completed = False )
        if "body" in attributes and attributes[ "body" ] is not None: # pragma no branch
            assert isinstance( attributes[ "body" ], ( str, unicode ) ), attributes[ "body" ]
            self._body = attributes[ "body" ]
        if "closed_at" in attributes and attributes[ "closed_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "closed_at" ], ( str, unicode ) ), attributes[ "closed_at" ]
            self._closed_at = attributes[ "closed_at" ]
        if "closed_by" in attributes and attributes[ "closed_by" ] is not None: # pragma no branch
            assert isinstance( attributes[ "closed_by" ], dict ), attributes[ "closed_by" ]
            self._closed_by = NamedUser.NamedUser( self._requester, attributes[ "closed_by" ], completed = False )
        if "comments" in attributes and attributes[ "comments" ] is not None: # pragma no branch
            assert isinstance( attributes[ "comments" ], int ), attributes[ "comments" ]
            self._comments = attributes[ "comments" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self._created_at = attributes[ "created_at" ]
        if "html_url" in attributes and attributes[ "html_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "html_url" ], ( str, unicode ) ), attributes[ "html_url" ]
            self._html_url = attributes[ "html_url" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "labels" in attributes and attributes[ "labels" ] is not None: # pragma no branch
            assert all( isinstance( element, dict ) for element in attributes[ "labels" ] ), attributes[ "labels" ]
            self._labels = [
                Label.Label( self._requester, element, completed = False )
                for element in attributes[ "labels" ]
            ]
        if "milestone" in attributes and attributes[ "milestone" ] is not None: # pragma no branch
            assert isinstance( attributes[ "milestone" ], dict ), attributes[ "milestone" ]
            self._milestone = Milestone.Milestone( self._requester, attributes[ "milestone" ], completed = False )
        if "number" in attributes and attributes[ "number" ] is not None: # pragma no branch
            assert isinstance( attributes[ "number" ], int ), attributes[ "number" ]
            self._number = attributes[ "number" ]
        if "pull_request" in attributes and attributes[ "pull_request" ] is not None: # pragma no branch
            assert isinstance( attributes[ "pull_request" ], dict ), attributes[ "pull_request" ]
            self._pull_request = IssuePullRequest.IssuePullRequest( self._requester, attributes[ "pull_request" ], completed = False )
        if "repository" in attributes and attributes[ "repository" ] is not None: # pragma no branch
            assert isinstance( attributes[ "repository" ], dict ), attributes[ "repository" ]
            self._repository = Repository.Repository( self._requester, attributes[ "repository" ], completed = False )
        if "state" in attributes and attributes[ "state" ] is not None: # pragma no branch
            assert isinstance( attributes[ "state" ], ( str, unicode ) ), attributes[ "state" ]
            self._state = attributes[ "state" ]
        if "title" in attributes and attributes[ "title" ] is not None: # pragma no branch
            assert isinstance( attributes[ "title" ], ( str, unicode ) ), attributes[ "title" ]
            self._title = attributes[ "title" ]
        if "updated_at" in attributes and attributes[ "updated_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "updated_at" ], ( str, unicode ) ), attributes[ "updated_at" ]
            self._updated_at = attributes[ "updated_at" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
        if "user" in attributes and attributes[ "user" ] is not None: # pragma no branch
            assert isinstance( attributes[ "user" ], dict ), attributes[ "user" ]
            self._user = NamedUser.NamedUser( self._requester, attributes[ "user" ], completed = False )
