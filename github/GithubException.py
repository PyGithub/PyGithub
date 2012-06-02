class GithubException( Exception ):
    def __init__( self, status, data ):
        Exception.__init__( self )
        self.status = status
        self.data = data

    def __str__( self ):
        return str( self.status ) + " " + str( self.data )
