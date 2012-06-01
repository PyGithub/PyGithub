import GithubObject

class InputGitTreeElement:
    def __init__( self, path, mode, type, content = GithubObject.NotSet, sha = GithubObject.NotSet ):
        self.__path = path
        self.__mode = mode
        self.__type = type
        self.__content = content
        self.__sha = sha

    def _identity( self ):
        identity = {
            "path": self.__path,
            "mode": self.__mode,
            "type": self.__type,
        }
        if self.__sha is not GithubObject.NotSet:
            identity[ "sha" ] = self.__sha
        if self.__content is not GithubObject.NotSet:
            identity[ "content" ] = self.__content
        return identity
