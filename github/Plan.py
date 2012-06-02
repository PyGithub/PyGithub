# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class Plan( GithubObject.BasicGithubObject ):
    @property
    def collaborators( self ):
        return self._NoneIfNotSet( self._collaborators )

    @property
    def name( self ):
        return self._NoneIfNotSet( self._name )

    @property
    def private_repos( self ):
        return self._NoneIfNotSet( self._private_repos )

    @property
    def space( self ):
        return self._NoneIfNotSet( self._space )

    def _initAttributes( self ):
        self._collaborators = GithubObject.NotSet
        self._name = GithubObject.NotSet
        self._private_repos = GithubObject.NotSet
        self._space = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "collaborators" in attributes: # pragma no branch
            assert attributes[ "collaborators" ] is None or isinstance( attributes[ "collaborators" ], int ), attributes[ "collaborators" ]
            self._collaborators = attributes[ "collaborators" ]
        if "name" in attributes: # pragma no branch
            assert attributes[ "name" ] is None or isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
        if "private_repos" in attributes: # pragma no branch
            assert attributes[ "private_repos" ] is None or isinstance( attributes[ "private_repos" ], int ), attributes[ "private_repos" ]
            self._private_repos = attributes[ "private_repos" ]
        if "space" in attributes: # pragma no branch
            assert attributes[ "space" ] is None or isinstance( attributes[ "space" ], int ), attributes[ "space" ]
            self._space = attributes[ "space" ]
