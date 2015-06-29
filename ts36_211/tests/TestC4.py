import unittest
from nose.tools import eq_
from ..c4 import DwPTS, UpPTS, GP, T_slot, T_s
from ..core.Enums import SPECIAL_SUBFRAME_PATTERNS, CP_TYPE

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