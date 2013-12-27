'''
Created on 23 dec 2013

@author: linggduo
'''
from Enums import SF_TYPE, CFI
class SubframeConfig:
    '''
    Configuration for one subframe
    '''
    def __init__(self, longSfn, subframeType, cfi, globalConfig):
        '''
        config: this should be the module Config
        '''
        self.longSfn = longSfn
        self.subframeType = subframeType
        self.cfi = cfi
        self.globalConfig = globalConfig
    
    def numberOfPdcchSymbols(self):
        if self.subframeType==SF_TYPE.D and self.cfi in (1, 2, 3):
            if self.globalConfig.N_DL_RB>10:
                return self.cfi
            else:
                return self.cfi+1
        raise Exception("Invalid parameters: subframeType={0}, CFI={1}".format(self.subframeType, self.cfi))
        