import unittest
from nose.tools import eq_
from ..c6 import csrs_v
from ..core.Enums import SPECIAL_SUBFRAME_PATTERNS, CP_TYPE, DELTA_F, DUPLEX_MODE, SUBFRAME_ASSIGNMENT, BW, RE_TYPE
from ..core.Frame import Frame
from ..core.Plotter import Plotter
from ..core.Re import Re
from ..L1Config import L1Config
import logging

logging.basicConfig(level=logging.DEBUG)

class TestC6(unittest.TestCase):
    def test_csrs_v(self):
        p, l = 0, 0
        for n_s in range(20):
            eq_(0, csrs_v(p, n_s, l))
        p = 0
        for l in range(1, 7):
            for n_s in range(20):
                eq_(3, csrs_v(p, n_s, l))
        p, l = 1, 0
        for n_s in range(20):
            eq_(3, csrs_v(p, n_s, l))
        p = 1
        for l in range(1, 7):
            for n_s in range(20):
                eq_(0, csrs_v(p, n_s, l))
        p = 2
        for l in range(7):
            for n_s in range(20):
                eq_(3 * (n_s%2), csrs_v(p, n_s, l))
        p = 3
        for l in range(7):
            for n_s in range(20):
                eq_(3 + 3 * (n_s%2), csrs_v(p, n_s, l))
    def test_csrs(self):
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
        eq_(frame._size_x(), 140)
        eq_(frame._size_y(), 72)
        for x in range(frame._size_x()):
            for y in range(frame._size_y()):
                frame[x][y] = Re((x * y + x) % len(RE_TYPE))
        plotter = Plotter(frame)
        plotter.plot("test_temporary_plot_frame_blank.png")
