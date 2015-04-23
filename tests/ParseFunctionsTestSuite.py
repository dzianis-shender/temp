__author__ = 'Dzianis_Shender'

import unittest


class ParseFunctionsTestSuite(unittest.TestSuite):

    def suite(self):
        """suite method for all test cases"""

        suite = unittest.TestSuite()

        # put all test case classes here

        unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':

    ParseFunctionsTestSuite().suite()
