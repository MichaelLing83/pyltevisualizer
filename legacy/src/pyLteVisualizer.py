'''
Created on 20 dec 2013

@author: Michael Duo Ling

Terminology:
    1. longSf: long subframe number, which is systemFrameNumber * 10 + subframeNumber
'''


import Config
from Enums import *
from ImageDrawing import ImageDrawer
from ToolClasses import ReTypeSubframe

reTypeSubframeList = list()
for s in Config.subframeConfigs:
    reTypeSubframeList.append(ReTypeSubframe(Config.GlobalConfig.DownlinkBandwidth, Config.GlobalConfig.DlCyclicPrefixLength, Config.GlobalConfig.DeltaF, s.subframeType, s.longSfn, s.numberOfPdcchSymbols()))
imageDrawer = ImageDrawer(Config.GlobalConfig.DuplexMode, reTypeSubframeList)
    

if __name__ == '__main__':
    print("%s, %s" % (1, 'abc'))