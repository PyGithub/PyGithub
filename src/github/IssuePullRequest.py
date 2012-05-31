# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class IssuePullRequest( GithubObject.BasicGithubObject ):
    @property
    def diff_url( self ):
        return self._NoneIfNotSet( self._diff_url )

    @property
    def html_url( self ):
        return self._NoneIfNotSet( self._html_url )

    @property
    def patch_url( self ):
        return self._NoneIfNotSet( self._patch_url )

    def _initAttributes( self ):
        self._diff_url = GithubObject.NotSet
        self._html_url = GithubObject.NotSet
        self._patch_url = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "diff_url" in attributes: # pragma no branch
            assert attributes[ "diff_url" ] is None or isinstance( attributes[ "diff_url" ], ( str, unicode ) ), attributes[ "diff_url" ]
            self._diff_url = attributes[ "diff_url" ]
        if "html_url" in attributes: # pragma no branch
            assert attributes[ "html_url" ] is None or isinstance( attributes[ "html_url" ], ( str, unicode ) ), attributes[ "html_url" ]
            self._html_url = attributes[ "html_url" ]
        if "patch_url" in attributes: # pragma no branch
            assert attributes[ "patch_url" ] is None or isinstance( attributes[ "patch_url" ], ( str, unicode ) ), attributes[ "patch_url" ]
            self._patch_url = attributes[ "patch_url" ]
