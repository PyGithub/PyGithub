# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *

class PullRequestFile( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def additions( self ):
        return self.__additions

    @property
    def blob_url( self ):
        return self.__blob_url

    @property
    def changes( self ):
        return self.__changes

    @property
    def deletions( self ):
        return self.__deletions

    @property
    def filename( self ):
        return self.__filename

    @property
    def patch( self ):
        return self.__patch

    @property
    def raw_url( self ):
        return self.__raw_url

    @property
    def sha( self ):
        return self.__sha

    @property
    def status( self ):
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

    def __useAttributes( self, attributes ):
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "additions", "blob_url", "changes", "deletions", "filename", "patch", "raw_url", "sha", "status", ], attribute
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "additions" in attributes and attributes[ "additions" ] is not None: # pragma no branch
            self.__additions = attributes[ "additions" ]
        if "blob_url" in attributes and attributes[ "blob_url" ] is not None: # pragma no branch
            self.__blob_url = attributes[ "blob_url" ]
        if "changes" in attributes and attributes[ "changes" ] is not None: # pragma no branch
            self.__changes = attributes[ "changes" ]
        if "deletions" in attributes and attributes[ "deletions" ] is not None: # pragma no branch
            self.__deletions = attributes[ "deletions" ]
        if "filename" in attributes and attributes[ "filename" ] is not None: # pragma no branch
            self.__filename = attributes[ "filename" ]
        if "patch" in attributes and attributes[ "patch" ] is not None: # pragma no branch
            self.__patch = attributes[ "patch" ]
        if "raw_url" in attributes and attributes[ "raw_url" ] is not None: # pragma no branch
            self.__raw_url = attributes[ "raw_url" ]
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            self.__sha = attributes[ "sha" ]
        if "status" in attributes and attributes[ "status" ] is not None: # pragma no branch
            self.__status = attributes[ "status" ]
