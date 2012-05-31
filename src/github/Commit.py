# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
import PaginatedList
##########
import CommitFile
import NamedUser
import GitCommit
import CommitStats
import Commit
import CommitComment

class Commit( GithubObject.GithubObject ):
    @property
    def author( self ):
        self._completeIfNotSet( self._author )
        return self._NoneIfNotSet( self._author )

    @property
    def commit( self ):
        self._completeIfNotSet( self._commit )
        return self._NoneIfNotSet( self._commit )

    @property
    def committer( self ):
        self._completeIfNotSet( self._committer )
        return self._NoneIfNotSet( self._committer )

    @property
    def files( self ):
        self._completeIfNotSet( self._files )
        return self._NoneIfNotSet( self._files )

    @property
    def parents( self ):
        self._completeIfNotSet( self._parents )
        return self._NoneIfNotSet( self._parents )

    @property
    def sha( self ):
        self._completeIfNotSet( self._sha )
        return self._NoneIfNotSet( self._sha )

    @property
    def stats( self ):
        self._completeIfNotSet( self._stats )
        return self._NoneIfNotSet( self._stats )

    @property
    def url( self ):
        self._completeIfNotSet( self._url )
        return self._NoneIfNotSet( self._url )

    def create_comment( self, body, line = GithubObject.NotSet, path = GithubObject.NotSet, position = GithubObject.NotSet ):
        assert isinstance( body, ( str, unicode ) ), body
        if line is not GithubObject.NotSet:
            assert isinstance( line, int ), line
        if path is not GithubObject.NotSet:
            assert isinstance( path, ( str, unicode ) ), path
        if position is not GithubObject.NotSet:
            assert isinstance( position, int ), position
        post_parameters = {
            "body": body,
        }
        if line is not GithubObject.NotSet:
            post_parameters[ "line" ] = line
        if path is not GithubObject.NotSet:
            post_parameters[ "path" ] = path
        if position is not GithubObject.NotSet:
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
        self._author = GithubObject.NotSet
        self._commit = GithubObject.NotSet
        self._committer = GithubObject.NotSet
        self._files = GithubObject.NotSet
        self._parents = GithubObject.NotSet
        self._sha = GithubObject.NotSet
        self._stats = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "author" in attributes: # pragma no branch
            assert attributes[ "author" ] is None or isinstance( attributes[ "author" ], dict ), attributes[ "author" ]
            self._author = None if attributes[ "author" ] is None else NamedUser.NamedUser( self._requester, attributes[ "author" ], completed = False )
        if "commit" in attributes: # pragma no branch
            assert attributes[ "commit" ] is None or isinstance( attributes[ "commit" ], dict ), attributes[ "commit" ]
            self._commit = None if attributes[ "commit" ] is None else GitCommit.GitCommit( self._requester, attributes[ "commit" ], completed = False )
        if "committer" in attributes: # pragma no branch
            assert attributes[ "committer" ] is None or isinstance( attributes[ "committer" ], dict ), attributes[ "committer" ]
            self._committer = None if attributes[ "committer" ] is None else NamedUser.NamedUser( self._requester, attributes[ "committer" ], completed = False )
        if "files" in attributes: # pragma no branch
            assert all( isinstance( element, dict ) for element in attributes[ "files" ] ), attributes[ "files" ]
            self._files = [
                CommitFile.CommitFile( self._requester, element, completed = False )
                for element in attributes[ "files" ]
            ]
        if "parents" in attributes: # pragma no branch
            assert all( isinstance( element, dict ) for element in attributes[ "parents" ] ), attributes[ "parents" ]
            self._parents = [
                Commit( self._requester, element, completed = False )
                for element in attributes[ "parents" ]
            ]
        if "sha" in attributes: # pragma no branch
            assert attributes[ "sha" ] is None or isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self._sha = attributes[ "sha" ]
        if "stats" in attributes: # pragma no branch
            assert attributes[ "stats" ] is None or isinstance( attributes[ "stats" ], dict ), attributes[ "stats" ]
            self._stats = None if attributes[ "stats" ] is None else CommitStats.CommitStats( self._requester, attributes[ "stats" ], completed = False )
        if "url" in attributes: # pragma no branch
            assert attributes[ "url" ] is None or isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
