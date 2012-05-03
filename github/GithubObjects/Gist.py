# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import NamedUser
import Gist
import GistComment

class Gist( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def comments( self ):
        if self.__comments is None:
            self.__completeIfNeeded()
        return self.__comments

    @property
    def created_at( self ):
        if self.__created_at is None:
            self.__completeIfNeeded()
        return self.__created_at

    @property
    def description( self ):
        if self.__description is None:
            self.__completeIfNeeded()
        return self.__description

    @property
    def files( self ):
        if self.__files is None:
            self.__completeIfNeeded()
        return self.__files

    @property
    def forks( self ):
        if self.__forks is None:
            self.__completeIfNeeded()
        return self.__forks

    @property
    def git_pull_url( self ):
        if self.__git_pull_url is None:
            self.__completeIfNeeded()
        return self.__git_pull_url

    @property
    def git_push_url( self ):
        if self.__git_push_url is None:
            self.__completeIfNeeded()
        return self.__git_push_url

    @property
    def history( self ):
        if self.__history is None:
            self.__completeIfNeeded()
        return self.__history

    @property
    def html_url( self ):
        if self.__html_url is None:
            self.__completeIfNeeded()
        return self.__html_url

    @property
    def id( self ):
        if self.__id is None:
            self.__completeIfNeeded()
        return self.__id

    @property
    def public( self ):
        if self.__public is None:
            self.__completeIfNeeded()
        return self.__public

    @property
    def updated_at( self ):
        if self.__updated_at is None:
            self.__completeIfNeeded()
        return self.__updated_at

    @property
    def url( self ):
        if self.__url is None:
            self.__completeIfNeeded()
        return self.__url

    @property
    def user( self ):
        if self.__user is None:
            self.__completeIfNeeded()
        return self.__user

    def __initAttributes( self ):
        self.__comments = None
        self.__created_at = None
        self.__description = None
        self.__files = None
        self.__forks = None
        self.__git_pull_url = None
        self.__git_push_url = None
        self.__history = None
        self.__html_url = None
        self.__id = None
        self.__public = None
        self.__updated_at = None
        self.__url = None
        self.__user = None

    def __completeIfNeeded( self ):
        if not self.__completed:
            self.__complete()
        self.__completed = True

    def __complete( self ):
        pass

    def create_comment( self, body ):
        pass

    def create_fork( self ):
        pass

    def delete( self ):
        pass

    def edit( self, description = None, files = None ):
        pass

    def get_comment( self, id ):
        pass

    def get_comments( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/comments",
            None,
            None
        )
        return [
            GistComment.GistComment( self.__github, element, lazy = True )
            for element in result
        ]

    def is_starred( self ):
        pass

    def reset_starred( self ):
        pass

    def set_starred( self ):
        pass

    def __useAttributes( self, attributes ):
        if "comments" in attributes:
            self.__comments = attributes[ "comments" ]
        if "created_at" in attributes:
            self.__created_at = attributes[ "created_at" ]
        if "description" in attributes:
            self.__description = attributes[ "description" ]
        if "files" in attributes:
            self.__files = attributes[ "files" ]
        if "forks" in attributes:
            self.__forks = attributes[ "forks" ]
        if "git_pull_url" in attributes:
            self.__git_pull_url = attributes[ "git_pull_url" ]
        if "git_push_url" in attributes:
            self.__git_push_url = attributes[ "git_push_url" ]
        if "history" in attributes:
            self.__history = attributes[ "history" ]
        if "html_url" in attributes:
            self.__html_url = attributes[ "html_url" ]
        if "id" in attributes:
            self.__id = attributes[ "id" ]
        if "public" in attributes:
            self.__public = attributes[ "public" ]
        if "updated_at" in attributes:
            self.__updated_at = attributes[ "updated_at" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
        if "user" in attributes:
            self.__user = attributes[ "user" ]
