'''
Created on 23 dec 2013

@author: linggduo
'''
from Enums import SF_TYPE, CFI
from Config import GlobalConfig
class SubframeConfig:
    '''
    Configuration for one subframe
    '''
    def __init__(self, longSfn=0, subframeType=SF_TYPE.D, cfi=GlobalConfig.CFI):
        '''
        Constructor
        '''
        self.longSfn = longSfn
        self.subframeType = subframeType
        self.cfi = cfi
        