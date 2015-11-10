import unittest
from nose.tools import eq_
from ..asn1 import ENUMERATED, BIT_STRING, SEQUENCE, Dl_Bandwidth, Phich_Duration, Phich_Resource, PHICH_Config, SystemFrameNumber, MasterInformationBlock
from ...misc.bitstring.bitstring import Bits

class TestAsn1(unittest.TestCase):
    def test_ENUMERATED(self):
        E = ENUMERATED('Enum', 'zero', 'one', 'two', 'three', 'four')
        eq_(E.__name__, 'Enum')
        eq_(E.length, 3)
        e = E()
        eq_(e.code(), Bits(uint=0, length=3))
        eq_(E.decode(e.code()), e)
        e.set(E.three)
        eq_(e.code(), Bits(uint=3, length=3))

    def test_BIT_STRING(self):
        BS = BIT_STRING('BitString', 9)
        bs = BS()
        bs.set(Bits(uint=11, length=9))
        eq_(bs.code(), Bits(uint=11, length=9))
        bs.set(11)
        eq_(bs.code(), Bits(uint=11, length=9))
        eq_(BS.decode(bs.code()), bs)
        bs.set(b'a')
        eq_(bs.code(), Bits(bin='0b001100001'))

    def test_SEQUENCE(self):
        A = ENUMERATED('A', 'zero', 'one', 'two', 'three')
        B = BIT_STRING('B', 6)
        Seq = SEQUENCE('SEQ', A(), B())
        s = Seq()
        s.A.set(A.three)
        s.B.set(0b010101)
        eq_(s.code(), Bits(bin='0b11010101'))
        eq_(Seq.decode(s.code()), s)

    def test_Dl_Bandwidth(self):
        eq_(Dl_Bandwidth.length, 3)
        eq_(Dl_Bandwidth.n6, 0)
        eq_(Dl_Bandwidth.n15, 1)
        eq_(Dl_Bandwidth.n25, 2)
        eq_(Dl_Bandwidth.n50, 3)
        eq_(Dl_Bandwidth.n75, 4)
        eq_(Dl_Bandwidth.n100, 5)

        eq_(Dl_Bandwidth(Dl_Bandwidth.n6).code(), Bits(int=0, length=3))
        eq_(Dl_Bandwidth(Dl_Bandwidth.n15).code(), Bits(int=1, length=3))
        eq_(Dl_Bandwidth(Dl_Bandwidth.n25).code(), Bits(int=2, length=3))
        eq_(Dl_Bandwidth(Dl_Bandwidth.n50).code(), Bits(int=3, length=3))
        eq_(Dl_Bandwidth(Dl_Bandwidth.n75).code(), Bits(uint=4, length=3))
        eq_(Dl_Bandwidth(Dl_Bandwidth.n100).code(), Bits(uint=5, length=3))

    def test_Phich_Duration(self):
        eq_(Phich_Duration.length, 1)
        eq_(Phich_Duration.normal, 0)
        eq_(Phich_Duration.extended, 1)

        eq_(Phich_Duration(Phich_Duration.normal).code(), Bits(bin='0b0'))
        eq_(Phich_Duration(Phich_Duration.extended).code(), Bits(bin='0b1'))

    def test_Phich_Resource(self):
        eq_(Phich_Resource.length, 2)
        eq_(Phich_Resource.oneSixth, 0)
        eq_(Phich_Resource.half, 1)
        eq_(Phich_Resource.one, 2)
        eq_(Phich_Resource.two, 3)

        eq_(Phich_Resource(Phich_Resource.oneSixth).code(), Bits(bin='0b00'))
        eq_(Phich_Resource(Phich_Resource.half).code(), Bits(bin='0b01'))
        eq_(Phich_Resource(Phich_Resource.one).code(), Bits(bin='0b10'))
        eq_(Phich_Resource(Phich_Resource.two).code(), Bits(bin='0b11'))

    def test_PHICH_Config(self):
        eq_(PHICH_Config.length, 3)

        p = PHICH_Config()
        p.Phich_Duration.set(Phich_Duration.extended)
        p.Phich_Resource.set(Phich_Resource.one)
        eq_(p.code(), Bits(bin='0b110'))

    def test_SystemFrameNumber(self):
        eq_(SystemFrameNumber.length, 8)

        s = SystemFrameNumber()
        s.set(Bits(bin='0b01010101'))
        eq_(s.code(), Bits(bin='0b01010101'))

    def test_MasterInformationBlock(self):
        eq_(MasterInformationBlock.length, 24)
        mib = MasterInformationBlock()
        mib.PHICH_Config.Phich_Duration.set(Phich_Duration.extended)
        mib.PHICH_Config.Phich_Resource.set(Phich_Resource.half)
        mib.Dl_Bandwidth.set(Dl_Bandwidth.n25)
        mib.SystemFrameNumber.set(0xef)
        eq_(mib.code(), Bits(bin='0b010101111011110000000000'))



