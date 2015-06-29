from .core.Enums import CP_TYPE

# 5.6 SC-FDMA baseband signal generation

#   symbol length in Ts without CP
def N():
    # in UL delta_f is alway 15 kHz
    return 2048

#   Table 5.6-1: SC-FDMA parameters
def cyclic_prefix_in_Ts(cyclic_prefix, l):
    '''
    l: index of symbol in the slot
    '''
    assert cyclic_prefix in CP_TYPE.all()
    if cyclic_prefix == CP_TYPE.NORMAL:
        assert 0 <= l <= 6
        if l == 0:
            return 160
        else:
            return 144
    else:
        # extended CP
        assert 0 <= l <= 5
        return 512