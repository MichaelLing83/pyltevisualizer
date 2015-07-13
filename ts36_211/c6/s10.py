from ..core.Enums import BW, RE_TYPE, ANTENNA_PORTS_COUNT
from ..core.Re import Re

# 6.10 Reference signals

# 6.10.1 Cell-specific reference signals

# 6.10.1.2 Mapping to resource elements

def csrs_v(p, n_s, l):
    '''
    p: antenna port
    n_s: slot index within one frame
    l: symbol index in one slot
    '''
    assert 0 <= p <= 3
    if p == 0:
        if l == 0:
            return 0
        else:
            return 3
    elif p == 1:
        if l == 0:
            return 3
        else:
            return 0
    elif p == 2:
        return 3 * (n_s % 2)
    elif p == 3:
        return 3 + 3 * (n_s % 2)

def csrs_v_shift(N_cell_ID):
    return N_cell_ID % 6

def csrs_l(N_DL_symb, p):
    '''
    N_DL_symb: number of DL symbols in one slot
    p: antenna port index
    '''
    assert 0 <= p <= 3
    symbol_indice = ()
    if p in (0, 1):
        symbol_indice = (0, N_DL_symb - 3)
    elif p in (2, 3):
        symbol_indice = (1,)
    # filter out illegal symbol indice due to DwPTS
    return [x for x in symbol_indice if 0 <= x < N_DL_symb]

def csrs_ap(slot, bw, n_s, p, N_cell_ID):
    '''
    Mark CSRS for one given Antenna Port.

    slot: Matrix representation of the slot
    sf_type: subframe type for given slot
    bw: DL bandwidth
    n_s: slot index in one frame
    p: antenna port index
    '''
    N_DL_RB = BW.toRbNumber(bw)
    re = RE_TYPE.__getattribute__('CSRS_PORT{}'.format(p))
    v_shift = csrs_v_shift(N_cell_ID)
    for m in range(2 * N_DL_RB):
        for l in csrs_l(slot._size_x(), p):
            v = csrs_v(p, n_s, l)
            k = 6 * m + (v + v_shift) % 6
            slot[l][k] = Re(re)

def is_csrs_ap(l, k , bw, n_s, N_cell_ID, N_DL_symb, p):
    N_DL_RB = BW.toRbNumber(bw)
    v_shift = csrs_v_shift(N_cell_ID)
    v = csrs_v(p, n_s, l)
    l_list = csrs_l(N_DL_symb, p)
    if l in l_list:
        if (k - (v + v_shift) % 6) % 6 == 0 and 0 <= int((k - (v + v_shift) % 6) / 6)  <= 2 * N_DL_RB - 1:
            return True
    return False

def is_csrs(l, k , bw, n_s, N_cell_ID, N_DL_symb, antenna_ports_count):
    for p in range(ANTENNA_PORTS_COUNT.to_int(antenna_ports_count)):
        if is_csrs_ap(l, k , bw, n_s, N_cell_ID, N_DL_symb, p):
            return True
    return False

def is_csrs_reserved(l, k, bw, n_s, N_cell_ID, N_DL_symb):
    return is_csrs_ap(l, k , bw, n_s, N_cell_ID, N_DL_symb, 0) or \
        is_csrs_ap(l, k , bw, n_s, N_cell_ID, N_DL_symb, 1) or \
        is_csrs_ap(l, k , bw, n_s, N_cell_ID, N_DL_symb, 2) or \
        is_csrs_ap(l, k , bw, n_s, N_cell_ID, N_DL_symb, 3)