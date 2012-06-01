class InputFileContent:
    def __init__( self, content ):
        self.__content = content

    def _identity( self ):
        return {
            "content": self.__content,
        }
