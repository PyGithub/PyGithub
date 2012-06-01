class InputGitAuthor( object ):
    def __init__( self, name, email, date ):
        self.__name = name
        self.__email = email
        self.__date = date

    @property
    def _identity( self ):
        return {
            "name": self.__name,
            "email": self.__email,
            "date": self.__date,
        }
