'''
Created on 23 dec 2013

@author: Michael Duo Ling
'''
import unittest
from Enums import *


class Test(unittest.TestCase):


    def testBW(self):
        self.assertEqual(BW.toRbNumber(BW.N100), 100)
        self.assertEqual(BW.toRbNumber(BW.N15), 15)
        self.assertEqual(BW.toRbNumber(BW.N25), 25)
        self.assertEqual(BW.toRbNumber(BW.N6), 6)
        self.assertEqual(BW.calc__N_RB_sc(CP_TYPE.NORMAL, DELTA_F.KHZ_15), 12)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()