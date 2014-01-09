'''
Created on 23 dec 2013

@author: Michael Duo Ling
'''
from Enums import *
import PhyChannels
from ToolClasses import Point, Size
from SubframeConfig import SubframeConfig

############ Start of Global LTE Configuration #############
class __GlobalConfig__:
    DuplexMode = DUPLEX_MODE.FDD
    DownlinkBandwidth = BW.N6
    UplinkBandwidth = BW.N6
    UlCyclicPrefixLength = CP_TYPE.NORMAL
    DlCyclicPrefixLength = CP_TYPE.NORMAL
    SubframeAssignment = SUBFRAME_ASSIGNMENT.SA1
    SpecialSubframePatterns = SPECIAL_SUBFRAME_PATTERNS.SSP5
    DeltaF = DELTA_F.KHZ_15
    CellId = 10
    AntennaPortsCount = ANTENNA_PORTS_COUNT.AN4
    PhichDuration = PHICH_DURATION.NORMAL
    PhichResource = PHICH_RESOURCE.HALF
    CFI = 2
    PuschHoppingOffset = PUSCH_HOPPING_OFFSET.OFFSET_8
    PrachFreqOffset = PRACH_FREQ_OFFSET.OFFSET_2
    PrachConfigIndex = PRACH_CONFIG_INDEX.INDEX_0
GlobalConfig = __GlobalConfig__()
############ End of Global LTE Configuration #############

############ Start of per Subframe LTE Configuration #############
subframeConfigs = list()
for longSfn in range(100, 101):
    subframeConfigs.append(SubframeConfig(longSfn, SF_TYPE.D, GlobalConfig.CFI, GlobalConfig))
    subframeConfigs.append(SubframeConfig(longSfn, SF_TYPE.U, GlobalConfig.CFI, GlobalConfig))
############ End of per Subframe LTE Configuration #############

############ Start of Drawing Configuration #############
class DrawingConfig:
    RE_SIZE = Size(7, 7)    # size for one RE (resource element), in pixel
    frame_interval  =  10    #blank width between two frames, in pixel
    draw_offset = Point(15, 15)   # offset for the whole lattice
    subframe_gap = Size(2, 0)        # a small gap between adjacent subframes
    gap_ul_dl_for_fdd = 20
    image_margin = Size( 30, 70)
    # all color parameters are listed below. each color setting is represented by (r,g,b,a), i.e. (red, green, blue, alpha)
    color_text = (0, 0, 0, 255)
    # line color within one RB
    color_line_RE = (0, 0, 0, 64)
    color_line_DL_RE = (0, 0, 160, 64)
    color_line_UL_RE = (0, 160, 0, 64)
    color_line_S_RE = (160, 0, 0, 0)
    # RB color type 1 (grey, for showing different RBs)
    color_brush1_RB = (192, 192, 192, 64)
    # RB color type 2
    color_brush2_RB = (255, 255, 255, 64)
    # default color for all REs
    color_brush_RE = (255, 255, 255, 0)
    # default color for all REs in Special subframe
    color_brush_S_RE = (255, 255, 255, 0)
    
    ###########################################################
    # all color settings for all channels
    ###########################################################
    color_brush_PBCH = (0, 255, 0, 255)
    color_brush_PSS = (0, 0, 255, 255)
    color_brush_SSS = (255, 128, 128, 255)
    color_brush_CSRS_AP0 = (255, 0, 0, 255)
    color_brush_CSRS_AP1 = (255, 0, 0, 255)
    color_brush_CSRS_AP2 = (255, 0, 0, 255)
    color_brush_CSRS_AP3 = (255, 0, 0, 255)
    color_brush_CSRS_AP4 = (255, 0, 0, 255)
    color_brush_CSRS_AP5 = (255, 0, 0, 255)
    color_brush_CSRS_AP6 = (255, 0, 0, 255)
    color_brush_CSRS_AP7 = (255, 0, 0, 255)
    color_brush_CSRS = (255, 0, 0, 255)
    color_brush_PCFICH = (128, 255, 128, 255)
    color_brush_PHICH = (0, 0, 0, 255)
    color_brush_PDCCH = (0, 128, 255, 255)
    color_brush_PRACH = (128, 0, 255, 128)
############ End of Drawing Configuration #############

############ !!DO NOT CHANGE ANY CODE AFTER THIS COMMENT!! #############
if (GlobalConfig.CellId<0 or GlobalConfig.CellId>3*135+2):
    raise Exception("CellId={0} is invalid!".format(GlobalConfig.CellId))
GlobalConfig.N_ID_1 = GlobalConfig.CellId // 3
GlobalConfig.N_ID_2 = GlobalConfig.CellId % 3
GlobalConfig.N_RB_sc = BW.calc__N_RB_sc(GlobalConfig.DlCyclicPrefixLength, GlobalConfig.DeltaF)
GlobalConfig.N_DL_RB = BW.toRbNumber(GlobalConfig.DownlinkBandwidth)
GlobalConfig.N_DL_symb = PhyChannels.Downlink.calc_N_DL_symb(GlobalConfig.DlCyclicPrefixLength, GlobalConfig.DeltaF)
GlobalConfig.N_UL_RB = BW.toRbNumber(GlobalConfig.UplinkBandwidth)

project_version = '2.0.0'
project_name = 'pyLTEVisualizer'
project_owner = "Author: Michael Duo Ling, Email: duo.ling.cn@gmail.com"
project_weblink = "http://code.google.com/p/pyltevisualizer/"

if __name__ == '__main__':
    pass