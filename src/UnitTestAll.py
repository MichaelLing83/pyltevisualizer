'''
Created on 23 dec 2013

@author: Michael Duo Ling
'''
import unittest
import TestEnums

def testAll():
    suite = unittest.TestSuite();
    suite.addTest(TestEnums.Test)
    return suite

if __name__ == "__main__":
    testAll().run(True)
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()