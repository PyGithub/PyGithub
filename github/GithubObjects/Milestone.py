# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.


class Milestone( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def closed_issues( self ):
        if self.__closed_issues is None:
            self.__completeIfNeeded()
        return self.__closed_issues

    @property
    def created_at( self ):
        if self.__created_at is None:
            self.__completeIfNeeded()
        return self.__created_at

    @property
    def creator( self ):
        if self.__creator is None:
            self.__completeIfNeeded()
        return self.__creator

    @property
    def description( self ):
        if self.__description is None:
            self.__completeIfNeeded()
        return self.__description

    @property
    def due_on( self ):
        if self.__due_on is None:
            self.__completeIfNeeded()
        return self.__due_on

    @property
    def number( self ):
        if self.__number is None:
            self.__completeIfNeeded()
        return self.__number

    @property
    def open_issues( self ):
        if self.__open_issues is None:
            self.__completeIfNeeded()
        return self.__open_issues

    @property
    def state( self ):
        if self.__state is None:
            self.__completeIfNeeded()
        return self.__state

    @property
    def title( self ):
        if self.__title is None:
            self.__completeIfNeeded()
        return self.__title

    @property
    def url( self ):
        if self.__url is None:
            self.__completeIfNeeded()
        return self.__url

    def __initAttributes( self ):
        self.__closed_issues = None
        self.__created_at = None
        self.__creator = None
        self.__description = None
        self.__due_on = None
        self.__number = None
        self.__open_issues = None
        self.__state = None
        self.__title = None
        self.__url = None

    def __completeIfNeeded( self ):
        if not self.__completed:
            self.__complete()
        self.__completed = True

    def __complete( self ):
        pass

    def delete( self ):
        pass

    def edit( self, title, state = None, description = None, due_on = None ):
        pass

    def get_labels( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url + "/labels",
            None,
            None
        )
        return [
            Label.Label( self.__github, element, lazy = True )
            for element in result
        ]

    def __useAttributes( self, attributes ):
        if "closed_issues" in attributes:
            self.__closed_issues = attributes[ "closed_issues" ]
        if "created_at" in attributes:
            self.__created_at = attributes[ "created_at" ]
        if "creator" in attributes:
            self.__creator = attributes[ "creator" ]
        if "description" in attributes:
            self.__description = attributes[ "description" ]
        if "due_on" in attributes:
            self.__due_on = attributes[ "due_on" ]
        if "number" in attributes:
            self.__number = attributes[ "number" ]
        if "open_issues" in attributes:
            self.__open_issues = attributes[ "open_issues" ]
        if "state" in attributes:
            self.__state = attributes[ "state" ]
        if "title" in attributes:
            self.__title = attributes[ "title" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
