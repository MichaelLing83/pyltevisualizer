from .core.Enums import CP_TYPE, DUPLEX_MODE, BW, DELTA_F, SUBFRAME_ASSIGNMENT, SPECIAL_SUBFRAME_PATTERNS, ANTENNA_PORTS_COUNT

class L1Config:
    def __init__(self):
        # default L1 configuration
        self.ul_cyclicPrefixLength = CP_TYPE.NORMAL
        self.dl_cyclicPrefixLength = CP_TYPE.NORMAL
        self.duplexMode = DUPLEX_MODE.TDD
        self.subframe_assignment = SUBFRAME_ASSIGNMENT.SA1
        self.specialSubframePatterns = SPECIAL_SUBFRAME_PATTERNS.SSP7
        self.dl_bandwidth = BW.N6
        self.ul_bandwidth = BW.N6
        self.delta_f = DELTA_F.KHZ_15
        self.antenna_ports_count = ANTENNA_PORTS_COUNT.AN4
        self.PhysCellId = 0 # 0..503