# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
import NamedUser
import GitCommit
import CommitComment
# This allows None as a valid value for an optional parameter

class DefaultValueForOptionalParametersType:
    pass
DefaultValueForOptionalParameters = DefaultValueForOptionalParametersType()

class Commit( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def author( self ):
        self.__completeIfNeeded( self.__author )
        return self.__author

    @property
    def commit( self ):
        self.__completeIfNeeded( self.__commit )
        return self.__commit

    @property
    def committer( self ):
        self.__completeIfNeeded( self.__committer )
        return self.__committer

    @property
    def files( self ):
        self.__completeIfNeeded( self.__files )
        return self.__files

    @property
    def parents( self ):
        self.__completeIfNeeded( self.__parents )
        return self.__parents

    @property
    def sha( self ):
        self.__completeIfNeeded( self.__sha )
        return self.__sha

    @property
    def stats( self ):
        self.__completeIfNeeded( self.__stats )
        return self.__stats

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def create_comment( self, body, commit_id = DefaultValueForOptionalParameters, line = DefaultValueForOptionalParameters, path = DefaultValueForOptionalParameters, position = DefaultValueForOptionalParameters ):
        post_parameters = {
            "body": body,
        }
        if commit_id is not DefaultValueForOptionalParameters:
            post_parameters[ "commit_id" ] = commit_id
        if line is not DefaultValueForOptionalParameters:
            post_parameters[ "line" ] = line
        if path is not DefaultValueForOptionalParameters:
            post_parameters[ "path" ] = path
        if position is not DefaultValueForOptionalParameters:
            post_parameters[ "position" ] = position
        status, headers, data = self.__requester.request(
            "POST",
            str( self.url ) + "/comments",
            None,
            post_parameters
        )
        return CommitComment.CommitComment( self.__requester, data, lazy = True )

    def get_comments( self ):
        status, headers, data = self.__requester.request(
            "GET",
            str( self.url ) + "/comments",
            None,
            None
        )
        return PaginatedList.PaginatedList(
            CommitComment.CommitComment,
            self.__requester,
            headers,
            data
        )

    def __initAttributes( self ):
        self.__author = None
        self.__commit = None
        self.__committer = None
        self.__files = None
        self.__parents = None
        self.__sha = None
        self.__stats = None
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
        if "author" in attributes:
            self.__author = NamedUser.NamedUser( self.__requester, attributes[ "author" ], lazy = True )
        if "commit" in attributes:
            self.__commit = GitCommit.GitCommit( self.__requester, attributes[ "commit" ], lazy = True )
        if "committer" in attributes:
            self.__committer = NamedUser.NamedUser( self.__requester, attributes[ "committer" ], lazy = True )
        if "files" in attributes:
            self.__files = attributes[ "files" ]
        if "parents" in attributes:
            self.__parents = attributes[ "parents" ]
        if "sha" in attributes:
            self.__sha = attributes[ "sha" ]
        if "stats" in attributes:
            self.__stats = attributes[ "stats" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
