class SimpleScalarAttributes:
    def __init__( self, *attributes ):
        self.__attributes = attributes

def GithubObject( *attributes ):
    class GithubObject:
        def __init__( self, github, attributes, lazy ):
            pass

    return GithubObject
