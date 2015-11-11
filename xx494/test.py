'''
Created on Nov 10, 2015

@author: Xu Xu
'''
import unittest
import numpy as np
from Investment import investment

class Test(unittest.TestCase):


    def setUp(self):
        pass

    def test_investment_value(self):
        test_value = investment()
        self.assertEqual(text_value.investment_value, 1000)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()