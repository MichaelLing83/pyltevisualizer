from .core.Enums import CP_TYPE, DELTA_F, BW, RE_TYPE, SF_TYPE, DUPLEX_MODE
from .core.Re import Re

# 6.2.3 Resource blocks
def calc_N_RB_sc(cyclic_prefix, delta_f):
    if cyclic_prefix == CP_TYPE.NORMAL:
        assert delta_f == DELTA_F.KHZ_15, "Illegal configuration!"
        return 12
    else:
        if delta_f == DELTA_F.KHZ_15:
            return 12
        else:
            return 24

def N_DL_symb(cyclic_prefix, delta_f):
    if cyclic_prefix == CP_TYPE.NORMAL:
        assert delta_f == DELTA_F.KHZ_15, "Illegal configuration!"
        return 7
    else:
        if delta_f == DELTA_F.KHZ_15:
            return 6
        else:
            return 3

# 6.6 Physical broadcast channel

# 6.6.4 Mapping to resource elements
def pbch_n_s_l():
    return 1, range(4)
def pbch_k_list(N_DL_RB, N_RB_sc):
    return range(int(N_DL_RB * N_RB_sc / 2) - 36 + 0, int(N_DL_RB * N_RB_sc / 2) - 36 + 71 + 1)

# 6.12 OFDM baseband signal generation
# number of Ts for one OFDM symbol without CP
def N(delta_f):
    assert delta_f in DELTA_F.all()
    if delta_f == DELTA_F.KHZ_15:
        return 2048
    else:
        return 4096

#   Table 6.12-1: OFDM parameters
def cyclic_prefix_in_Ts(cyclic_prefix, delta_f, l):
    '''
    l: index of symbol in the slot
    '''
    assert cyclic_prefix in CP_TYPE.all()
    assert delta_f in DELTA_F.all()
    if cyclic_prefix == CP_TYPE.NORMAL:
        assert 0 <= l <= 6
        if delta_f == DELTA_F.KHZ_15:
            if l == 0:
                return 160
            else:
                return 144
    else:
        # extended CP
        if delta_f == DELTA_F.KHZ_15:
            assert 0 <= l <= 5
            return 512
        else:
            assert 0 <= l <= 2
            return 1024

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

def is_csrs_reserved(l, k, bw, n_s, N_cell_ID, N_DL_symb):
    return is_csrs_ap(l, k , bw, n_s, N_cell_ID, N_DL_symb, 0) or \
        is_csrs_ap(l, k , bw, n_s, N_cell_ID, N_DL_symb, 1) or \
        is_csrs_ap(l, k , bw, n_s, N_cell_ID, N_DL_symb, 2) or \
        is_csrs_ap(l, k , bw, n_s, N_cell_ID, N_DL_symb, 3)

# 6.11 Synchronization signals

# 6.11.1 Primary synchronization signal

# 6.11.1.2 Mapping to resource elements
def pss_n_s_l(duplex_mode, N_DL_symb):
    '''
    Calc pss resource in time domain

    return: list of n_s, l
    '''
    assert duplex_mode in DUPLEX_MODE.all()
    if duplex_mode == DUPLEX_MODE.FDD:
        n_s_list = (0, 10)
        l = N_DL_symb - 1
    else:
        n_s_list = (1*2-1, 6*2-1)
        l = 2
    return n_s_list, l

def pss_k_list(N_DL_RB, N_RB_sc):
    return range(int(-31 + N_DL_RB * N_RB_sc / 2), int(61 - 31 + N_DL_RB * N_RB_sc / 2) + 1)

def pss_k_reserved_list(N_DL_RB, N_RB_sc):
    k_reserved_list = list()
    for n in range(-5, 0):
        k_reserved_list.append(int(n -31 + N_DL_RB * N_RB_sc / 2))
    for n in range(62, 67):
        k_reserved_list.append(int(n -31 + N_DL_RB * N_RB_sc / 2))
    return k_reserved_list

# 6.11.2 Secondary synchronization signal

# 6.11.2.2 Mapping to resource elements
def sss_n_s_l(duplex_mode, N_DL_symb):
    '''
    Calc SSS resource in time domain

    return: list of n_s, l
    '''
    assert duplex_mode in DUPLEX_MODE.all()
    if duplex_mode == DUPLEX_MODE.FDD:
        n_s_list = (0, 10)
        l = N_DL_symb - 2
    else:
        n_s_list = (1, 11)
        l = N_DL_symb - 1
    return n_s_list, l

def sss_k_list(N_DL_RB, N_RB_sc):
    return range(int(-31 + N_DL_RB * N_RB_sc / 2), int(61 - 31 + N_DL_RB * N_RB_sc / 2) + 1)

def sss_k_reserved_list(N_DL_RB, N_RB_sc):
    k_reserved_list = list()
    for n in range(-5, 0):
        k_reserved_list.append(int(n -31 + N_DL_RB * N_RB_sc / 2))
    for n in range(62, 67):
        k_reserved_list.append(int(n -31 + N_DL_RB * N_RB_sc / 2))
    return k_reserved_list

