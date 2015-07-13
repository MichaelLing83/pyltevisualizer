# 6.6 Physical broadcast channel

# 6.6.4 Mapping to resource elements
def pbch_n_s_l():
    return 1, range(4)
def pbch_k_list(N_DL_RB, N_RB_sc):
    return range(int(N_DL_RB * N_RB_sc / 2) - 36 + 0, int(N_DL_RB * N_RB_sc / 2) - 36 + 71 + 1)