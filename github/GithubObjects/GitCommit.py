# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GitTree

class GitCommit( object ):
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
    def committer( self ):
        if self.__committer is None:
            self.__completeIfNeeded()
        return self.__committer

    @property
    def message( self ):
        if self.__message is None:
            self.__completeIfNeeded()
        return self.__message

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
    def tree( self ):
        if self.__tree is None:
            self.__completeIfNeeded()
        return self.__tree

    @property
    def url( self ):
        if self.__url is None:
            self.__completeIfNeeded()
        return self.__url

    def __initAttributes( self ):
        self.__author = None
        self.__committer = None
        self.__message = None
        self.__parents = None
        self.__sha = None
        self.__tree = None
        self.__url = None

    def __completeIfNeeded( self ):
        if not self.__completed:
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

    def __useAttributes( self, attributes ):
        if "author" in attributes:
            self.__author = attributes[ "author" ]
        if "committer" in attributes:
            self.__committer = attributes[ "committer" ]
        if "message" in attributes:
            self.__message = attributes[ "message" ]
        if "parents" in attributes:
            self.__parents = attributes[ "parents" ]
        if "sha" in attributes:
            self.__sha = attributes[ "sha" ]
        if "tree" in attributes:
            self.__tree = attributes[ "tree" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
