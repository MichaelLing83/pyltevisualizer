from ..core.Enums import DUPLEX_MODE

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