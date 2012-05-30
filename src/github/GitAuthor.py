# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class GitAuthor( GithubObject.GithubObject ):
    @property
    def date( self ):
        return self._date

    @property
    def email( self ):
        return self._email

    @property
    def name( self ):
        return self._name

    def _initAttributes( self ):
        self._date = None
        self._email = None
        self._name = None

    def _useAttributes( self, attributes ):
        if "date" in attributes and attributes[ "date" ] is not None: # pragma no branch
            assert isinstance( attributes[ "date" ], ( str, unicode ) ), attributes[ "date" ]
            self._date = attributes[ "date" ]
        if "email" in attributes and attributes[ "email" ] is not None: # pragma no branch
            assert isinstance( attributes[ "email" ], ( str, unicode ) ), attributes[ "email" ]
            self._email = attributes[ "email" ]
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
