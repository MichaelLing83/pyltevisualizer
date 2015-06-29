from .Matrix import Matrix
from .Enums import CP_TYPE, DUPLEX_MODE, BW, DELTA_F
from ..c6 import calc_N_DL_symb

class L1Config:
    def __init__(self):
        self.ul_cyclicPrefixLength = CP_TYPE.NORMAL
        self.dl_cyclicPrefixLength = CP_TYPE.NORMAL
        self.duplexMode = DUPLEX_MODE.TDD
        self.dl_bandwidth = BW.N6
        self.ul_bandwidth = BW.N6
        self.delta_f = DELTA_F.KHZ_15

class Frame(Matrix):
    def __init__(self, l1_config):
        assert isinstance(l1_config, L1Config), "must be L1Config"
        self.l1_config = l1_config
        if self.l1_config.duplexMode == DUPLEX_MODE.TDD:
            assert self.l1_config.dl_bandwidth == self.l1_config.ul_bandwidth, "TDD must have the same bandwidth for DL and UL!"
            __size_y = BW.toReNumber(self.l1_config.dl_bandwidth, self.l1_config.dl_cyclicPrefixLength, self.l1_config.delta_f)
            __size_x = calc_N_DL_symb(self.l1_config.dl_cyclicPrefixLength, self.l1_config.delta_f)
        else:
            assert False, "FDD is not supported yet!"
        super().__init__(__size_x, __size_y, int)