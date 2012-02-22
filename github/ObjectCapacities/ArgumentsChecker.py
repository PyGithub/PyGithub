import itertools

class ArgumentsChecker:
    def __init__( self, mandatoryParameters, optionalParameters ):
        self.__mandatoryParameters = mandatoryParameters
        self.__optionalParameters = optionalParameters

    def check( self, args, kwds ):
        data = dict( kwds )
        for arg, argumentName in itertools.izip( args, itertools.chain( self.__mandatoryParameters, self.__optionalParameters ) ):
            if argumentName in kwds:
                raise TypeError()
            else:
                data[ argumentName ] = arg
        for argumentName in data:
            if argumentName not in itertools.chain( self.__mandatoryParameters, self.__optionalParameters ):
                raise TypeError()
        for argumentName in self.__mandatoryParameters:
            if argumentName not in data:
                raise TypeError()
        return data
