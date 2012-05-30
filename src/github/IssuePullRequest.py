# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *

class IssuePullRequest( object ):
    def __init__( self, requester, attributes, completed ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def diff_url( self ):
        return self.__diff_url

    @property
    def html_url( self ):
        return self.__html_url

    @property
    def patch_url( self ):
        return self.__patch_url

    def __initAttributes( self ):
        self.__diff_url = None
        self.__html_url = None
        self.__patch_url = None

    def __useAttributes( self, attributes ):
        if "diff_url" in attributes and attributes[ "diff_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "diff_url" ], ( str, unicode ) ), attributes[ "diff_url" ]
            self.__diff_url = attributes[ "diff_url" ]
        if "html_url" in attributes and attributes[ "html_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "html_url" ], ( str, unicode ) ), attributes[ "html_url" ]
            self.__html_url = attributes[ "html_url" ]
        if "patch_url" in attributes and attributes[ "patch_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "patch_url" ], ( str, unicode ) ), attributes[ "patch_url" ]
            self.__patch_url = attributes[ "patch_url" ]
