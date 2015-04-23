#------------------------------------------------------------------------------
# Class:  ErrorDetails
#
# Description:
#    Domain class for error details RWI report paragraph
# 
#------------------------------------------------------------------------------

class ErrorDetails (object):

    def __init__(self):
        self._permutationName = None
        self._error = None
        self._serverTime = None

    @property
    def permutationName(self):
        return self._permutationName

    @permutationName.setter
    def permutationName(self, value):
        self._permutationName = value

    @permutationName.deleter
    def permutationName(self):
        self._permutationName = None

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, value):
        self._error = value

    @error.deleter
    def error(self):
        self._error = None

    @property
    def serverTime(self):
        return self._serverTime

    @serverTime.setter
    def serverTime(self, value):
        self._serverTime = value

    @serverTime.deleter
    def serverTime(self):
        self._serverTime = None

