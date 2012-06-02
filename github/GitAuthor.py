# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class GitAuthor( GithubObject.BasicGithubObject ):
    @property
    def date( self ):
        return self._NoneIfNotSet( self._date )

    @property
    def email( self ):
        return self._NoneIfNotSet( self._email )

    @property
    def name( self ):
        return self._NoneIfNotSet( self._name )

    def _initAttributes( self ):
        self._date = GithubObject.NotSet
        self._email = GithubObject.NotSet
        self._name = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "date" in attributes: # pragma no branch
            assert attributes[ "date" ] is None or isinstance( attributes[ "date" ], ( str, unicode ) ), attributes[ "date" ]
            self._date = attributes[ "date" ]
        if "email" in attributes: # pragma no branch
            assert attributes[ "email" ] is None or isinstance( attributes[ "email" ], ( str, unicode ) ), attributes[ "email" ]
            self._email = attributes[ "email" ]
        if "name" in attributes: # pragma no branch
            assert attributes[ "name" ] is None or isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
