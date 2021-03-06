from .core.Enums import ENUM, SF_TYPE, SUBFRAME_ASSIGNMENT, SPECIAL_SUBFRAME_PATTERNS, CP_TYPE, DELTA_F
from .c5 import cyclic_prefix_in_Ts as ul_cp_in_Ts
from .c5 import N as N_ul
from .c5 import N_UL_symb
from .c6 import N_DL_symb
from .c6 import N as N_dl
from .c6 import cyclic_prefix_in_Ts as dl_cp_in_Ts
import logging

T_f = 10 / 1000         # one frame in seconds
T_s = T_f / 307200      # basic time unit in seconds
T_slot = 15360 * T_s    # one slot in seconds
SLOT_INDICE = range(20)
SUBFRAME_INDICE = range(10)

# 4.2 Frame structure type 2

# Table 4.2-1: Configuration of special subframe (lengths of DwPTS/UpPTS).
def DwPTS(ssp, dl_cp):
    assert ssp in SPECIAL_SUBFRAME_PATTERNS.all()
    assert dl_cp in CP_TYPE.all()
    if dl_cp == CP_TYPE.NORMAL:
        return (6592, 19760, 21952, 24144, 26336, 6592, 19760, 21952, 24144)[ssp - SPECIAL_SUBFRAME_PATTERNS.SSP0]
    else:
        assert SPECIAL_SUBFRAME_PATTERNS.SSP0 <= ssp <= SPECIAL_SUBFRAME_PATTERNS.SSP6
        return (7680, 20480, 23040, 25600, 7680, 20480, 23040)[ssp - SPECIAL_SUBFRAME_PATTERNS.SSP0]

def symbol_nr_DwPTS(ssp, dl_cp, delta_f):
    len_ts = DwPTS(ssp, dl_cp)
    l, count = 0, 0
    while len_ts > 0:
        len_ts -= dl_cp_in_Ts(dl_cp, delta_f, l) + N_dl(delta_f)
        l = (l + 1) % N_DL_symb(dl_cp, delta_f)
        count += 1
    assert len_ts == 0
    return count

def UpPTS(ssp, dl_cp, ul_cp):
    assert ssp in SPECIAL_SUBFRAME_PATTERNS.all()
    assert dl_cp in CP_TYPE.all()
    assert ul_cp in CP_TYPE.all()
    if dl_cp == CP_TYPE.NORMAL:
        if ul_cp == CP_TYPE.NORMAL:
            return (2192, 2192, 2192, 2192, 2192, 4384, 4384, 4384, 4384)[ssp - SPECIAL_SUBFRAME_PATTERNS.SSP0]
        else:
            return (2560, 2560, 2560, 2560, 2560, 5120, 5120, 5120, 5120)[ssp - SPECIAL_SUBFRAME_PATTERNS.SSP0]
    else:
        assert SPECIAL_SUBFRAME_PATTERNS.SSP0 <= ssp <= SPECIAL_SUBFRAME_PATTERNS.SSP6
        if ul_cp == CP_TYPE.NORMAL:
            return (2192, 2192, 2192, 2192, 4384, 4384, 4384)[ssp - SPECIAL_SUBFRAME_PATTERNS.SSP0]
        else:
            return (2560, 2560, 2560, 2560, 5120, 5120, 5120)[ssp - SPECIAL_SUBFRAME_PATTERNS.SSP0]

def symbol_nr_UpPTS(ssp, dl_cp, ul_cp):
    len_ts = UpPTS(ssp, dl_cp, ul_cp)
    # for UpPTS we should calculate from the last symbol
    l, count = N_UL_symb(ul_cp) - 1, 0
    while len_ts > 0:
        len_ts -= ul_cp_in_Ts(ul_cp, l) + N_ul()
        l = (l - 1) % N_UL_symb(ul_cp)
        count += 1
    assert len_ts == 0
    return count

def GP(ssp, dl_cp, ul_cp):
    return int(T_slot/T_s) * 2 - DwPTS(ssp, dl_cp) - UpPTS(ssp, dl_cp, ul_cp)

def symbol_nr_GP(ssp, dl_cp, ul_cp, delta_f):
    logging.debug("ssp={}, dl_cp={}, ul_cp={}, delta_f={}".format(ENUM.to_s(ssp), ENUM.to_s(dl_cp), ENUM.to_s(ul_cp), ENUM.to_s(delta_f)))
    len_ts = GP(ssp, dl_cp, ul_cp)
    logging.debug("len_ts={}".format(len_ts))
    uppts = symbol_nr_UpPTS(ssp, dl_cp, ul_cp)
    in_ul = True
    # count from the last symbol
    l, count = N_UL_symb(ul_cp) - uppts - 1, 0
    while len_ts > 0:
        logging.debug("len_ts={}, l={}".format(len_ts, l))
        if l < 0:
            l = symbol_nr_DwPTS(ssp, dl_cp, delta_f) - 1
            in_ul = False
        if in_ul:
            len_ts -= ul_cp_in_Ts(ul_cp, l) + N_ul()
        else:
            len_ts -= dl_cp_in_Ts(dl_cp, delta_f, l) + N_dl(delta_f)
        l -= 1
        count += 1
    assert len_ts == 0
    logging.debug("count={}".format(count))
    return count

# Table 4.2-2: Uplink-downlink configurations.
def subframe_assignment(sfa):
    assert sfa in SUBFRAME_ASSIGNMENT.all(), "{} is not a valid subframe assignment".format(sfa)
    D, U, S = SF_TYPE.D, SF_TYPE.U, SF_TYPE.S
    return ( (D,S,U,U,U, D,S,U,U,U),
             (D,S,U,U,D, D,S,U,U,D),
             (D,S,U,D,D, D,S,U,D,D),
             (D,S,U,U,U, D,D,D,D,D),
             (D,S,U,U,D, D,D,D,D,D),
             (D,S,U,D,D, D,D,D,D,D),
             (D,S,U,U,U, D,S,U,U,D)
        )[sfa - SUBFRAME_ASSIGNMENT.SA0]