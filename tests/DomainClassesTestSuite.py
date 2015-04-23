__author__ = 'Dzianis_Shender'

import unittest

from core.domain.ErrorDetails import ErrorDetails


class ErrorDetailsTestCase(unittest.TestCase):

    def test_test_getters_and_setters(self):
        errorDetails = ErrorDetails()
        errorDetails.permutationName = '__permutationName__'
        errorDetails.error = '__error__'
        errorDetails.serverTime = '__serverTime__'
        self.assertEqual(errorDetails.permutationName, '__permutationName__')
        self.assertEqual(errorDetails.error, '__error__')
        self.assertEqual(errorDetails.serverTime, '__serverTime__')
        del errorDetails.error
        self.assertEqual(errorDetails.error, None)
        del errorDetails.permutationName
        self.assertEqual(errorDetails.permutationName, None)
        del errorDetails.serverTime
        self.assertEqual(errorDetails.serverTime, None)

    def test_parse_text(self):
        errorDetails = ErrorDetails()


class DomainClassesTestSuite(unittest.TestSuite):

    def suite(self):
        """suite method for all test cases"""

        suite = unittest.TestSuite()

        # put all test case classes here
        suite.addTest(ErrorDetailsTestCase)

        unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':

    DomainClassesTestSuite().suite()
