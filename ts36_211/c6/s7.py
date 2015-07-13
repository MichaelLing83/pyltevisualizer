from ..core.Enums import BW, DUPLEX_MODE, SF_TYPE, ENUM
from ..c4 import subframe_assignment
from .s2 import reg_index, reg_without_csrs
from math import floor
import logging

# 6.7 Physical control format indicator channel

# 6.7.4 Mapping to resource elements
def pcfich_n_s_l_list(duplex_mode, sfa):
    '''
    return: list of n_s, l
    '''
    if duplex_mode == DUPLEX_MODE.TDD:
        n_s_list = list()
        sfa_l = subframe_assignment(sfa)
        for slot_index in range(0, 20, 2):
            if sfa_l[int(slot_index/2)] in (SF_TYPE.D, SF_TYPE.S):
                n_s_list.append(slot_index)
        l = 0
    else:
        assert False, "FDD is not supported yet"
    logging.getLogger(__name__).debug("pcfich_n_s_l_list({}, {})={},{}".format(ENUM.to_s(duplex_mode), ENUM.to_s(sfa), n_s_list, l))
    return n_s_list, l
def pcfich_reg_k(pcfich_index, N_RB_sc, N_cell_ID, N_DL_RB):
    '''
    Return one subcarrier index k representing one REG for PCFICH quadruplet index pcfich_index
    '''
    k_ = int(N_RB_sc/2 * (N_cell_ID % (2*N_DL_RB)))
    k = k_ + int(floor(pcfich_index * N_DL_RB / 2) * N_RB_sc / 2)
    logging.getLogger(__name__).debug("pcfich_reg_k({},{},{},{})={}".format(pcfich_index, N_RB_sc, N_cell_ID, N_DL_RB,k))
    return k
def pcfich_reg(pcfich_index, n_s, l, N_DL_symb, N_RB_sc, N_cell_ID, bw, antenna_ports_count, dl_cp):
    '''
    Return a list of k.
    '''
    logging.getLogger(__name__).debug("pcfich_reg({},{},{},{},{},{},{},{},{})".format(pcfich_index, n_s, l, N_DL_symb, N_RB_sc, N_cell_ID, ENUM.to_s(bw), ENUM.to_s(antenna_ports_count), ENUM.to_s(dl_cp)))
    N_DL_RB = BW.toRbNumber(bw)
    k = pcfich_reg_k(pcfich_index, N_RB_sc, N_cell_ID, N_DL_RB)
    rb_index, index = reg_index(l, k, N_RB_sc, antenna_ports_count, dl_cp)
    logging.getLogger(__name__).debug("rb_index, index = {}, {}".format(rb_index, index))
    reg = reg_without_csrs(N_cell_ID, bw, rb_index, n_s, l, index, N_DL_symb, N_RB_sc, antenna_ports_count, dl_cp)
    logging.getLogger(__name__).debug("reg = {}".format(reg))
    reg = [k_+rb_index*N_RB_sc for k_ in reg]
    logging.getLogger(__name__).debug("reg = {}".format(reg))
    return reg