from ..core.Enums import CP_TYPE, DELTA_F, ANTENNA_PORTS_COUNT
from .s10 import is_csrs

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

# 6.2.4 Resource-element groups
def nr_of_reg_in_symb(l, antenna_ports_count, dl_cp):
    assert 0 <= l <= 3
    antenna_ports_count = ANTENNA_PORTS_COUNT.to_int(antenna_ports_count)
    if l == 0:
        return 2
    elif l == 1:
        if antenna_ports_count == 4:
            return 2
        else:
            return 3
    elif l == 2:
        return 3
    elif l == 3:
        if dl_cp == CP_TYPE.NORMAL:
            return 3
        else:
            return 2

def reg_in_rb(rb_index, l, reg_index, N_RB_sc, antenna_ports_count, dl_cp):
    '''
    return a list of k for specified REG in symbol l with reg_index in RB specified by rb_index.

    Note: CSRS occupied RE's are not removed.
    '''
    assert 0 <= l <= 3
    assert 0 <= reg_index < nr_of_reg_in_symb(l, antenna_ports_count, dl_cp)
    antenna_ports_count = ANTENNA_PORTS_COUNT.to_int(antenna_ports_count)
    k_0 = N_RB_sc * rb_index
    if l == 0:
        k = (range(0,6), range(6,12))[reg_index]
    elif l == 1:
        if antenna_ports_count == 4:
            k = (range(0,6), range(6,12))[reg_index]
        else:
            k = (range(0,4), range(4,8), range(8,12))[reg_index]
    elif l == 2:
        k = (range(0,4), range(4,8), range(8,12))[reg_index]
    elif l == 3:
        if dl_cp == CP_TYPE.NORMAL:
            k = (range(0,4), range(4,8), range(8,12))[reg_index]
        else:
            k = (range(0,6), range(6,12))[reg_index]
    return tuple(map(lambda x: x + k_0, k))

def reg(l, reg_index, N_RB_sc, antenna_ports_count, dl_cp):
    reg_nr_per_rb = nr_of_reg_in_symb(l, antenna_ports_count, dl_cp)
    rb_index = int(reg_index / reg_nr_per_rb)
    reg_index = reg_index % reg_nr_per_rb
    return reg_in_rb(rb_index, l, reg_index, N_RB_sc, antenna_ports_count, dl_cp)

def reg_in_rb_without_csrs(N_cell_ID, bw, rb_index, n_s, l, reg_index, N_DL_symb, N_RB_sc, antenna_ports_count, dl_cp):
    '''
    return a list of k for specified REG in symbol l with reg_index in RB specified by rb_index.

    Note: CSRS occupied RE's are removed.
    '''
    k_list = reg_in_rb(rb_index, l, reg_index, N_RB_sc, antenna_ports_count, dl_cp)
    k_list_without_csrs = [k for k in k_list if not is_csrs(l, k , bw, n_s, N_cell_ID, N_DL_symb, antenna_ports_count)]
    return tuple(k_list_without_csrs)

def reg_without_csrs(N_cell_ID, bw, rb_index, n_s, l, reg_index, N_DL_symb, N_RB_sc, antenna_ports_count, dl_cp):
    reg_nr_per_rb = nr_of_reg_in_symb(l, antenna_ports_count, dl_cp)
    rb_index = int(reg_index / reg_nr_per_rb)
    reg_index = reg_index % reg_nr_per_rb
    return reg_in_rb_without_csrs(N_cell_ID, bw, rb_index, n_s, l, reg_index, N_DL_symb, N_RB_sc, antenna_ports_count, dl_cp)

def reg_index(l, k, N_RB_sc, antenna_ports_count, dl_cp):
    rb_index = int(k / N_RB_sc)
    k %= N_RB_sc
    nr = nr_of_reg_in_symb(l, antenna_ports_count, dl_cp)
    if nr == 2:
        index = int(k/6)
    else:
        index = int(k/4)
    return rb_index, index