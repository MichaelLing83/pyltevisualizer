import unittest
from nose.tools import eq_
from ..c4 import DwPTS, UpPTS, GP, T_slot, T_s, symbol_nr_DwPTS
from ..core.Enums import SPECIAL_SUBFRAME_PATTERNS, CP_TYPE, DELTA_F

class TestC4(unittest.TestCase):
    def test_special_subframe(self):
        dl_cp = CP_TYPE.NORMAL
        for ssp in SPECIAL_SUBFRAME_PATTERNS.all():
            for ul_cp in CP_TYPE.all():
                eq_(int(T_slot/T_s) * 2, DwPTS(ssp, dl_cp) + GP(ssp, dl_cp, ul_cp) + UpPTS(ssp, dl_cp, ul_cp))
        dl_cp = CP_TYPE.EXTENDED
        for ssp in SPECIAL_SUBFRAME_PATTERNS.all()[:7]:
            for ul_cp in CP_TYPE.all():
                eq_(int(T_slot/T_s) * 2, DwPTS(ssp, dl_cp) + GP(ssp, dl_cp, ul_cp) + UpPTS(ssp, dl_cp, ul_cp))
    def test_DwPTS(self):
        delta_f = DELTA_F.KHZ_15
        dl_cp = CP_TYPE.NORMAL
        for ssp in SPECIAL_SUBFRAME_PATTERNS.all():
            eq_(symbol_nr_DwPTS(ssp, dl_cp, delta_f), (3,9,10,11,12,3,9,10,11)[ssp-SPECIAL_SUBFRAME_PATTERNS.SSP0])
        dl_cp = CP_TYPE.EXTENDED
        for ssp in SPECIAL_SUBFRAME_PATTERNS.all()[:7]:
            eq_(symbol_nr_DwPTS(ssp, dl_cp, delta_f), (3,8,9,10,3,8,9)[ssp-SPECIAL_SUBFRAME_PATTERNS.SSP0])