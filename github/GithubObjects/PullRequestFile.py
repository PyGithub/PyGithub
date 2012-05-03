# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class PullRequestFile( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def additions( self ):
        if self.__additions is None:
            self.__completeIfNeeded()
        return self.__additions

    @property
    def blob_url( self ):
        if self.__blob_url is None:
            self.__completeIfNeeded()
        return self.__blob_url

    @property
    def changes( self ):
        if self.__changes is None:
            self.__completeIfNeeded()
        return self.__changes

    @property
    def deletions( self ):
        if self.__deletions is None:
            self.__completeIfNeeded()
        return self.__deletions

    @property
    def filename( self ):
        if self.__filename is None:
            self.__completeIfNeeded()
        return self.__filename

    @property
    def patch( self ):
        if self.__patch is None:
            self.__completeIfNeeded()
        return self.__patch

    @property
    def raw_url( self ):
        if self.__raw_url is None:
            self.__completeIfNeeded()
        return self.__raw_url

    @property
    def sha( self ):
        if self.__sha is None:
            self.__completeIfNeeded()
        return self.__sha

    @property
    def status( self ):
        if self.__status is None:
            self.__completeIfNeeded()
        return self.__status

    def __initAttributes( self ):
        self.__additions = None
        self.__blob_url = None
        self.__changes = None
        self.__deletions = None
        self.__filename = None
        self.__patch = None
        self.__raw_url = None
        self.__sha = None
        self.__status = None

    def __completeIfNeeded( self ):
        if not self.__completed:
            self.__complete()
        self.__completed = True

    def __complete( self ):
        pass

    def __useAttributes( self, attributes ):
        if "additions" in attributes:
            self.__additions = attributes[ "additions" ]
        if "blob_url" in attributes:
            self.__blob_url = attributes[ "blob_url" ]
        if "changes" in attributes:
            self.__changes = attributes[ "changes" ]
        if "deletions" in attributes:
            self.__deletions = attributes[ "deletions" ]
        if "filename" in attributes:
            self.__filename = attributes[ "filename" ]
        if "patch" in attributes:
            self.__patch = attributes[ "patch" ]
        if "raw_url" in attributes:
            self.__raw_url = attributes[ "raw_url" ]
        if "sha" in attributes:
            self.__sha = attributes[ "sha" ]
        if "status" in attributes:
            self.__status = attributes[ "status" ]
