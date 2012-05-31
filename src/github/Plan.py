# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class Plan( GithubObject.BasicGithubObject ):
    @property
    def collaborators( self ):
        return self._collaborators

    @property
    def name( self ):
        return self._name

    @property
    def private_repos( self ):
        return self._private_repos

    @property
    def space( self ):
        return self._space

    def _initAttributes( self ):
        self._collaborators = None
        self._name = None
        self._private_repos = None
        self._space = None

    def _useAttributes( self, attributes ):
        if "collaborators" in attributes and attributes[ "collaborators" ] is not None: # pragma no branch
            assert isinstance( attributes[ "collaborators" ], int ), attributes[ "collaborators" ]
            self._collaborators = attributes[ "collaborators" ]
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
        if "private_repos" in attributes and attributes[ "private_repos" ] is not None: # pragma no branch
            assert isinstance( attributes[ "private_repos" ], int ), attributes[ "private_repos" ]
            self._private_repos = attributes[ "private_repos" ]
        if "space" in attributes and attributes[ "space" ] is not None: # pragma no branch
            assert isinstance( attributes[ "space" ], int ), attributes[ "space" ]
            self._space = attributes[ "space" ]
