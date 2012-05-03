# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class PullRequestFile( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def additions( self ):
        self.__completeIfNeeded( self.__additions )
        return self.__additions

    @property
    def blob_url( self ):
        self.__completeIfNeeded( self.__blob_url )
        return self.__blob_url

    @property
    def changes( self ):
        self.__completeIfNeeded( self.__changes )
        return self.__changes

    @property
    def deletions( self ):
        self.__completeIfNeeded( self.__deletions )
        return self.__deletions

    @property
    def filename( self ):
        self.__completeIfNeeded( self.__filename )
        return self.__filename

    @property
    def patch( self ):
        self.__completeIfNeeded( self.__patch )
        return self.__patch

    @property
    def raw_url( self ):
        self.__completeIfNeeded( self.__raw_url )
        return self.__raw_url

    @property
    def sha( self ):
        self.__completeIfNeeded( self.__sha )
        return self.__sha

    @property
    def status( self ):
        self.__completeIfNeeded( self.__status )
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
