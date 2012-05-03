# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import NamedUser
import GitCommit
import CommitComment

class Commit( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
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
        result = self.__github._dataRequest(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( result )
        self.__completed = True

    def create_comment( self, body, commit_id = None, line = None, path = None, position = None ):
        pass

    def get_comments( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/comments",
            None,
            None
        )
        return [
            CommitComment.CommitComment( self.__github, element, lazy = True )
            for element in result
        ]

    def __useAttributes( self, attributes ):
        if "author" in attributes:
            self.__author = attributes[ "author" ]
        if "commit" in attributes:
            self.__commit = attributes[ "commit" ]
        if "committer" in attributes:
            self.__committer = attributes[ "committer" ]
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
