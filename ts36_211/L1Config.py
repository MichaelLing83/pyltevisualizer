from .core.Enums import CP_TYPE, DUPLEX_MODE, BW, DELTA_F, SUBFRAME_ASSIGNMENT, SPECIAL_SUBFRAME_PATTERNS, ANTENNA_PORTS_COUNT, PHICH_DURATION, PHICH_RESOURCE, CFI

class SubframeConfig:
    def __init__(self):
        # default per subframe config
        self.cfi = CFI.CFI_2
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
        self.phichDuration = PHICH_DURATION.NORMAL
        self.phichResource = PHICH_RESOURCE.HALF
        self.subframeConfigs = dict()
    def subframeConfig(self, sfn):
        if not self.subframeConfigs.has_key(sfn):
            self.subframeConfigs[sfn] = SubframeConfig()
        return self.subframeConfigs[sfn]