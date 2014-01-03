'''
Created on 2 jan 2014

Representing specification 36.211

@author: Michael Duo Ling
'''
from Enums import CP_TYPE, DELTA_F

class Downlink:
    # 6.2.3
    @staticmethod
    def calc_N_DL_symb(dlCpType, deltaF):
        if (dlCpType == CP_TYPE.NORMAL):
            return 7
        elif (dlCpType == CP_TYPE.EXTENDED):
            if (deltaF == DELTA_F.KHZ_15):
                return 6
            elif (deltaF == DELTA_F.KHZ_7_5):
                return 3
        raise Exception("Invalid configuration for dlCpType=={0}, deltaF={1}".format(dlCpType, deltaF))