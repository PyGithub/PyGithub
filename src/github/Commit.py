# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
import PaginatedList
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters
##########
import CommitFile
import NamedUser
import GitCommit
import CommitStats
import Commit
import CommitComment

class Commit( GithubObject.CompletableGithubObject ):
    @property
    def author( self ):
        self._completeIfNeeded( self._author )
        return self._author

    @property
    def commit( self ):
        self._completeIfNeeded( self._commit )
        return self._commit

    @property
    def committer( self ):
        self._completeIfNeeded( self._committer )
        return self._committer

    @property
    def files( self ):
        self._completeIfNeeded( self._files )
        return self._files

    @property
    def parents( self ):
        self._completeIfNeeded( self._parents )
        return self._parents

    @property
    def sha( self ):
        self._completeIfNeeded( self._sha )
        return self._sha

    @property
    def stats( self ):
        self._completeIfNeeded( self._stats )
        return self._stats

    @property
    def url( self ):
        self._completeIfNeeded( self._url )
        return self._url

    def create_comment( self, body, line = DefaultValueForOptionalParameters, path = DefaultValueForOptionalParameters, position = DefaultValueForOptionalParameters ):
        assert isinstance( body, ( str, unicode ) ), body
        if line is not DefaultValueForOptionalParameters:
            assert isinstance( line, int ), line
        if path is not DefaultValueForOptionalParameters:
            assert isinstance( path, ( str, unicode ) ), path
        if position is not DefaultValueForOptionalParameters:
            assert isinstance( position, int ), position
        post_parameters = {
            "body": body,
        }
        if line is not DefaultValueForOptionalParameters:
            post_parameters[ "line" ] = line
        if path is not DefaultValueForOptionalParameters:
            post_parameters[ "path" ] = path
        if position is not DefaultValueForOptionalParameters:
            post_parameters[ "position" ] = position
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/comments",
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        return CommitComment.CommitComment( self._requester, data, completed = True )

    def get_comments( self ):
        status, headers, data = self._request(
            "GET",
            str( self.url ) + "/comments",
            None,
            None
        )
        self._checkStatus( status, data )
        return PaginatedList.PaginatedList(
            CommitComment.CommitComment,
            self._requester,
            headers,
            data
        )

    def _initAttributes( self ):
        self._author = None
        self._commit = None
        self._committer = None
        self._files = None
        self._parents = None
        self._sha = None
        self._stats = None
        self._url = None

    def _useAttributes( self, attributes ):
        if "author" in attributes and attributes[ "author" ] is not None: # pragma no branch
            assert isinstance( attributes[ "author" ], dict ), attributes[ "author" ]
            self._author = NamedUser.NamedUser( self._requester, attributes[ "author" ], completed = False )
        if "commit" in attributes and attributes[ "commit" ] is not None: # pragma no branch
            assert isinstance( attributes[ "commit" ], dict ), attributes[ "commit" ]
            self._commit = GitCommit.GitCommit( self._requester, attributes[ "commit" ], completed = False )
        if "committer" in attributes and attributes[ "committer" ] is not None: # pragma no branch
            assert isinstance( attributes[ "committer" ], dict ), attributes[ "committer" ]
            self._committer = NamedUser.NamedUser( self._requester, attributes[ "committer" ], completed = False )
        if "files" in attributes and attributes[ "files" ] is not None: # pragma no branch
            assert all( isinstance( element, dict ) for element in attributes[ "files" ] ), attributes[ "files" ]
            self._files = [
                CommitFile.CommitFile( self._requester, element, completed = False )
                for element in attributes[ "files" ]
            ]
        if "parents" in attributes and attributes[ "parents" ] is not None: # pragma no branch
            assert all( isinstance( element, dict ) for element in attributes[ "parents" ] ), attributes[ "parents" ]
            self._parents = [
                Commit( self._requester, element, completed = False )
                for element in attributes[ "parents" ]
            ]
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self._sha = attributes[ "sha" ]
        if "stats" in attributes and attributes[ "stats" ] is not None: # pragma no branch
            assert isinstance( attributes[ "stats" ], dict ), attributes[ "stats" ]
            self._stats = CommitStats.CommitStats( self._requester, attributes[ "stats" ], completed = False )
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
