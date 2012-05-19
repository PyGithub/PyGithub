# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import GitObject

class GitRef( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def object( self ):
        return self.__object

    @property
    def ref( self ):
        return self.__ref

    @property
    def url( self ):
        return self.__url

    def delete( self ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ),
            None,
            None
        )

    def edit( self, sha, force = DefaultValueForOptionalParameters ):
        post_parameters = {
            "sha": sha,
        }
        if force is not DefaultValueForOptionalParameters:
            post_parameters[ "force" ] = force
        status, headers, data = self.__requester.request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self.__useAttributes( data )

    def __initAttributes( self ):
        self.__object = None
        self.__ref = None
        self.__url = None

    def __useAttributes( self, attributes ):
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "object", "ref", "url", ], attribute
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "object" in attributes and attributes[ "object" ] is not None:
            assert isinstance( attributes[ "object" ], dict )
            self.__object = GitObject.GitObject( self.__requester, attributes[ "object" ], completion = LazyCompletion )
        if "ref" in attributes and attributes[ "ref" ] is not None:
            assert isinstance( attributes[ "ref" ], ( str, unicode ) )
            self.__ref = attributes[ "ref" ]
        if "url" in attributes and attributes[ "url" ] is not None:
            assert isinstance( attributes[ "url" ], ( str, unicode ) )
            self.__url = attributes[ "url" ]
