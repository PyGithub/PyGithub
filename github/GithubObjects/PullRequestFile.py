# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
# This allows None as a valid value for an optional parameter

class DefaultValueForOptionalParametersType:
    pass
DefaultValueForOptionalParameters = DefaultValueForOptionalParametersType()

class PullRequestFile( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
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
        if "additions" in attributes and attributes[ "additions" ] is not None:
            self.__additions = attributes[ "additions" ]
        if "blob_url" in attributes and attributes[ "blob_url" ] is not None:
            self.__blob_url = attributes[ "blob_url" ]
        if "changes" in attributes and attributes[ "changes" ] is not None:
            self.__changes = attributes[ "changes" ]
        if "deletions" in attributes and attributes[ "deletions" ] is not None:
            self.__deletions = attributes[ "deletions" ]
        if "filename" in attributes and attributes[ "filename" ] is not None:
            self.__filename = attributes[ "filename" ]
        if "patch" in attributes and attributes[ "patch" ] is not None:
            self.__patch = attributes[ "patch" ]
        if "raw_url" in attributes and attributes[ "raw_url" ] is not None:
            self.__raw_url = attributes[ "raw_url" ]
        if "sha" in attributes and attributes[ "sha" ] is not None:
            self.__sha = attributes[ "sha" ]
        if "status" in attributes and attributes[ "status" ] is not None:
            self.__status = attributes[ "status" ]
