import unittest
from ..Frame import Frame, L1Config
from ..Enums import ENUM, CP_TYPE, DUPLEX_MODE, BW, DELTA_F, SUBFRAME_ASSIGNMENT, SPECIAL_SUBFRAME_PATTERNS, RE_TYPE, SF_TYPE
from ..Plotter import Plotter
from ..Re import Re
from nose.tools import eq_
import logging

logging.basicConfig(level=logging.DEBUG)

class TestFrame(unittest.TestCase):
    def test_create_and_plot(self):
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
        plotter = Plotter(frame)
        plotter.plot("test_temporary_plot_frame_blank.png")
        assert frame[:]._Matrix__data is frame._Matrix__data
        assert frame[1:2]._Matrix__data is frame._Matrix__data
        eq_(frame._size_x(), 14*10)
        eq_(frame._size_y(), 72)
        # GP
        assert frame.count(lambda x: x == RE_TYPE.GP) == 72 * 2 *2
        for x in range(14+10, 14+10+2):
            for y in range(72):
                assert frame[x][y] == RE_TYPE.GP
        for x in range(14*5+14+10, 14*5+14+10+2):
            for y in range(72):
                assert frame[x][y] == RE_TYPE.GP
        # DwPTS
        assert frame.count(lambda x: x == RE_TYPE.DWPTS) == 72 * 10 *2
        for x in range(14, 14+10):
            for y in range(72):
                assert frame[x][y] == RE_TYPE.DWPTS
        for x in range(14*5+14, 14*5+14+10):
            for y in range(72):
                assert frame[x][y] == RE_TYPE.DWPTS
        # UpPTS
        assert frame.count(lambda x: x == RE_TYPE.UPPTS) == 72 * 2 *2
        for x in range(14+10+2, 14+10+2+2):
            for y in range(72):
                assert frame[x][y] == RE_TYPE.UPPTS
        for x in range(14*5+14+10+2, 14*5+14+10+2+2):
            for y in range(72):
                assert frame[x][y] == RE_TYPE.UPPTS
    def test_slot(self):
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
        for i in (0, 4, 5, 9):
            for j in (2*i, 2*i+1):
                slot = frame.slot(j)
                assert slot.sf_type == SF_TYPE.D
                assert slot._size_x() == 7
        for i in (1, 6):
            for j in (2*i, 2*i+1):
                slot = frame.slot(j)
                assert slot.sf_type == SF_TYPE.S
                assert slot._size_x() == 7
        for i in (2, 3, 7, 8):
            for j in (2*i, 2*i+1):
                eq_(frame.slot(j).sf_type, SF_TYPE.U)
        assert frame.nr_of_GP() == 2
        assert frame.nr_of_DwPTS() == 2
        for i in range(2):
            dwpts = frame.slot_DwPTS(i)
            #assert dwpts._size_x() == 10
        assert frame.nr_of_UpPTS() == 2
