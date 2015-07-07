from .core.Enums import CP_TYPE, DELTA_F, BW, RE_TYPE
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
    if p in (0, 1):
        return (0, N_DL_symb - 3)
    elif p in (2, 3):
        return (1,)

def csrs(slot, bw, n_s, p, N_cell_ID):
    '''
    slot: Matrix representation of the slot
    bw: DL bandwidth
    n_s: slot index in one frame
    p: antenna port index
    '''
    N_DL_RB = BW.toRbNumber(bw)
    re = RE_TYPE.__getattr__('CSRS_PORT{}'.format(p))
    v_shift = csrs_v_shift(N_cell_ID)
    for m in range(2 * N_DL_RB):
        for l in csrs_l(slot._size_x(), p):
            v = csrs_v(p, n_s, l)
            k = 6 * m + (v + v_shift) % 6
            slot[l][k] = Re(re)
