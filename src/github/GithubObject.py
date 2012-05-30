# This allows None as a valid value for an optional parameter
class DefaultValueForOptionalParametersType:
    pass
DefaultValueForOptionalParameters = DefaultValueForOptionalParametersType()

LazyCompletion = 0
ImmediateCompletion = 1
NoCompletion = 2

class GithubException( Exception ):
    def __init__( self, status, data ):
        Exception.__init__( self )
        self.status = status
        self.data = data
