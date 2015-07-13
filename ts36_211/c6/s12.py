from ..core.Enums import CP_TYPE, DELTA_F

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