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
        dl_cp, delta_f = CP_TYPE.NORMAL, DELTA_F.KHZ_15
        for ssp in SPECIAL_SUBFRAME_PATTERNS.all():
            symbol_nr_DwPTS(ssp, dl_cp, delta_f)
        dl_cp = CP_TYPE.EXTENDED
        for delta_f in DELTA_F.all():
            for ssp in SPECIAL_SUBFRAME_PATTERNS.all()[:7]:
                symbol_nr_DwPTS(ssp, dl_cp, delta_f)