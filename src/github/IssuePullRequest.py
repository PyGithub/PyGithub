# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class IssuePullRequest( GithubObject.GithubObject ):
    @property
    def diff_url( self ):
        return self._diff_url

    @property
    def html_url( self ):
        return self._html_url

    @property
    def patch_url( self ):
        return self._patch_url

    def _initAttributes( self ):
        self._diff_url = None
        self._html_url = None
        self._patch_url = None

    def _useAttributes( self, attributes ):
        if "diff_url" in attributes and attributes[ "diff_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "diff_url" ], ( str, unicode ) ), attributes[ "diff_url" ]
            self._diff_url = attributes[ "diff_url" ]
        if "html_url" in attributes and attributes[ "html_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "html_url" ], ( str, unicode ) ), attributes[ "html_url" ]
            self._html_url = attributes[ "html_url" ]
        if "patch_url" in attributes and attributes[ "patch_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "patch_url" ], ( str, unicode ) ), attributes[ "patch_url" ]
            self._patch_url = attributes[ "patch_url" ]
