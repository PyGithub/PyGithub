# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class Commit( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def author( self ):
        if self.__author is None:
            self.__completeIfNeeded()
        return self.__author

    @property
    def commit( self ):
        if self.__commit is None:
            self.__completeIfNeeded()
        return self.__commit

    @property
    def committer( self ):
        if self.__committer is None:
            self.__completeIfNeeded()
        return self.__committer

    @property
    def files( self ):
        if self.__files is None:
            self.__completeIfNeeded()
        return self.__files

    @property
    def parents( self ):
        if self.__parents is None:
            self.__completeIfNeeded()
        return self.__parents

    @property
    def sha( self ):
        if self.__sha is None:
            self.__completeIfNeeded()
        return self.__sha

    @property
    def stats( self ):
        if self.__stats is None:
            self.__completeIfNeeded()
        return self.__stats

    @property
    def url( self ):
        if self.__url is None:
            self.__completeIfNeeded()
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

    def __completeIfNeeded( self ):
        if not self.__completed:
            self.__complete()
        self.__completed = True

    def __complete( self ):
        pass

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
