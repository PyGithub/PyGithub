class InputFileContent( object ):
    def __init__( self, content ):
        self.__content = content

    @property
    def _identity( self ):
        return {
            "content": self.__content,
        }
