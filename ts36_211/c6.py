from .core.Enums import CP_TYPE, DELTA_F
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

def calc_N_DL_symb(cyclic_prefix, delta_f):
    if cyclic_prefix == CP_TYPE.NORMAL:
        assert delta_f == DELTA_F.KHZ_15, "Illegal configuration!"
        return 7
    else:
        if delta_f == DELTA_F.KHZ_15:
            return 6
        else:
            return 3