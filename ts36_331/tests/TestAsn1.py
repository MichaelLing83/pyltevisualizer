import unittest
from nose.tools import eq_
from ..asn1 import *

class TestAsn1(unittest.TestCase):
    def test_mib(self):
        eq_(len(dl_Bandwidth), 3)
        eq_(dl_Bandwidth.n6, 0)
        eq_(dl_Bandwidth.n15, 1)
        eq_(dl_Bandwidth.n25, 2)
        eq_(dl_Bandwidth.n50, 3)
        eq_(dl_Bandwidth.n75, 4)
        eq_(dl_Bandwidth.n100, 5)
        eq_(dl_Bandwidth.code('n15'), Bits(int=1, length=3))
        eq_(dl_Bandwidth.code('n6'), Bits(int=0, length=3))
        eq_(dl_Bandwidth.code('n25'), Bits(int=2, length=3))
        eq_(dl_Bandwidth.code('n50'), Bits(int=3, length=3))
        eq_(dl_Bandwidth.code('n75'), Bits(uint=4, length=3))
        eq_(dl_Bandwidth.code('n100'), Bits(uint=5, length=3))