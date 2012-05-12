class PaginatedList:
    def __init__( self, contentClass, requester, headers, data ):
        self.__requester = requester
        self.__contentClass = contentClass
        self.__pages = 0
        self.__fromData( headers, data )

    def __iter__( self ):
        goOn = True
        while goOn:
            goOn = False
            for element in self.__list:
                yield element
            if self.__nextUrl is not None:
                goOn = True
                status, headers, data = self.__requester.request( "GET", self.__nextUrl, None, None )
                self.__fromData( headers, data )

    def __getitem__( self, index ):
        return self.__list[ index ]

    def __fromData( self, headers, data ):
        links = self.__parseLinkHeader( headers )
        if len( data ) > 0 and "next" in links and self.__pages < 9:
            self.__pages += 1
            self.__nextUrl = links[ "next" ]
        else:
            self.__nextUrl = None

        self.__list = [
            self.__contentClass( self.__requester, element, lazy = True )
            for element in data
        ]

    def __parseLinkHeader( self, headers ):
        links = {}
        if "link" in headers:
            linkHeaders = headers[ "link" ].split( "," )
            for linkHeader in linkHeaders:
                ( url, rel ) = linkHeader.split( "; " )
                url = url[ 1 : -1 ]
                rel = rel[ 5 : -1 ]
                links[ rel ] = url
        return links
