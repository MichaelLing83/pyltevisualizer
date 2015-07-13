import unittest
from ...core.Enums import SPECIAL_SUBFRAME_PATTERNS, CP_TYPE, DELTA_F, DUPLEX_MODE, SUBFRAME_ASSIGNMENT, BW, RE_TYPE
from ...core.Frame import Frame
from ...core.Re import Re
from ...L1Config import L1Config
import logging

logging.basicConfig(level=logging.DEBUG)

class TestS7(unittest.TestCase):
    '''
    Test PCFICH
    '''
    def test_pcfich(self):
        c = L1Config()
        c.ul_cyclicPrefixLength = CP_TYPE.NORMAL
        c.dl_cyclicPrefixLength = CP_TYPE.NORMAL
        c.duplexMode = DUPLEX_MODE.TDD
        c.subframe_assignment = SUBFRAME_ASSIGNMENT.SA1
        c.specialSubframePatterns = SPECIAL_SUBFRAME_PATTERNS.SSP7
        c.dl_bandwidth = BW.N6
        c.ul_bandwidth = BW.N6
        c.delta_f = DELTA_F.KHZ_15
        frame = Frame(c)
        l = 0
        for n_s in (0, 2, 8, 10, 12, 18):
            for k in (1,2,4,5, 23,22,20,19, 37,38,40,41, 59,58,56,55):
                assert frame[l][k] == Re(RE_TYPE.PCFICH)
