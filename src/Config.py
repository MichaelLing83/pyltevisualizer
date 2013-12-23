'''
Created on 23 dec 2013

@author: Michael Duo Ling
'''
from Enums import *
from ImageDrawing import Point, Size
from SubframeConfig import SubframeConfig

############ Start of Global LTE Configuration #############
class GlobalConfig:
    DuplexMode = DUPLEX_MODE.FDD
    DownlinkBandwidth = BW.N6
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
############ End of Global LTE Configuration #############

############ Start of per Subframe LTE Configuration #############
subframeConfigs = list()
for longSf in range(100, 102):
    subframeConfigs.append(SubframeConfig(longSf=longSf))
############ End of per Subframe LTE Configuration #############

############ Start of Drawing Configuration #############
class DrawingConfig:
    RE_SIZE = Size(7, 7)    # size for one RE (resource element), in pixel
    frame_num  =  1    #total number of frames that will be drawn
    frame_interval  =  10    #blank width between two frames, in pixel
    draw_offset = Point(15, 15)   # offset for the whole lattice
    
    # all color parameters are listed below. each color setting is represented by (r,g,b,a), i.e. (red, green, blue, alpha)
    color_text = (0, 0, 0, 255)
    
    # line color within one RB
    color_line_RE_r =   0
    color_line_RE_b =   0
    color_line_RE_g  =  0
    color_line_RE_alpha  =  64
    
    color_line_DL_RE_r  =  0
    color_line_DL_RE_b =   0
    color_line_DL_RE_g  =  160
    color_line_DL_RE_alpha  =  64
    
    color_line_UL_RE_r  =  0
    color_line_UL_RE_b  =  160
    color_line_UL_RE_g =   0
    color_line_UL_RE_alpha  =  64
    
    color_line_S_RE_r  =  160
    color_line_S_RE_b  =  0
    color_line_S_RE_g  =  0
    color_line_S_RE_alpha  =  0
    
    # RB color type 1 (grey, for showing different RBs)
    color_brush1_RB_r   = 192
    color_brush1_RB_g  =  192
    color_brush1_RB_b   = 192
    color_brush1_RB_alpha  =  64
    
    # RB color type 2
    color_brush2_RB_r  =  255
    color_brush2_RB_g =   255
    color_brush2_RB_b  =  255
    color_brush2_RB_alpha  =  64
    
    # default color for all REs
    color_brush_RE_r  =  255
    color_brush_RE_g  =  255
    color_brush_RE_b  =  255
    color_brush_RE_alpha  =  0
    
    # default color for all REs in Special subframe
    color_brush_S_RE_r  =  255
    color_brush_S_RE_g  =  255
    color_brush_S_RE_b  =  255
    color_brush_S_RE_alpha  =  0
    
    
    ###########################################################
    # all color settings for all channels
    ###########################################################
    # for PBCH
    color_brush_PBCH_r  =  0
    color_brush_PBCH_g  =  255
    color_brush_PBCH_b  =  0
    color_brush_PBCH_alpha  =  255
    
    # for Primary Synchronization Signal
    color_brush_PSS_r =   0
    color_brush_PSS_g  =  0
    color_brush_PSS_b  =  255
    color_brush_PSS_alpha  =  255
    
    # for Secondary Synchronization Signal
    color_brush_SSS_r  =  255
    color_brush_SSS_g  =  128
    color_brush_SSS_b  =  128
    color_brush_SSS_alpha  =  255
    
    # for Cell Specific Reference Signal of AP (Antenna Port) 0 to 3
    color_brush_CSRS_AP0_r  =  255
    color_brush_CSRS_AP0_g  =  0
    color_brush_CSRS_AP0_b  =  0
    color_brush_CSRS_AP0_alpha  =  255
    color_brush_CSRS_AP1_r  =  255
    color_brush_CSRS_AP1_g  =  0
    color_brush_CSRS_AP1_b  =  0
    color_brush_CSRS_AP1_alpha  =  255
    color_brush_CSRS_AP2_r  =  255
    color_brush_CSRS_AP2_g  =  0
    color_brush_CSRS_AP2_b  =  0
    color_brush_CSRS_AP2_alpha  =  255
    color_brush_CSRS_AP3_r  =  255
    color_brush_CSRS_AP3_g =   0
    color_brush_CSRS_AP3_b  =  0
    color_brush_CSRS_AP3_alpha  =  255
    color_brush_CSRS_r   = 255
    color_brush_CSRS_g =   0
    color_brush_CSRS_b  =  0
    color_brush_CSRS_alpha  =  255
    
    # for Physical Control Format Indicator Channel
    color_brush_PCFICH_r  =  128
    color_brush_PCFICH_g  =  255
    color_brush_PCFICH_b   = 128
    color_brush_PCFICH_alpha  =  255
    
    # for Physical HARQ Indicator Channel
    color_brush_PHICH_r  =  0
    color_brush_PHICH_g  =  0
    color_brush_PHICH_b =   0
    color_brush_PHICH_alpha   = 255
    
    # for Physical Downlink Control Channel
    color_brush_PDCCH_r  =  0
    color_brush_PDCCH_g  =  128
    color_brush_PDCCH_b  =  255
    color_brush_PDCCH_alpha   = 255
    
    # for Physical Random Access Channel
    color_brush_PRACH_r  =  128
    color_brush_PRACH_g  =  0
    color_brush_PRACH_b   = 255
    color_brush_PRACH_alpha  =  128
############ End of Drawing Configuration #############

############ !!DO NOT CHANGE ANY CODE AFTER THIS COMMENT!! #############
if (GlobalConfig.CellId<0 or GlobalConfig.CellId>3*135+2):
    raise Exception("CellId={0} is invalid!".format(GlobalConfig.CellId))
GlobalConfig.N_ID_1 = GlobalConfig.CellId // 3
GlobalConfig.N_ID_2 = GlobalConfig.CellId % 3

project_version = '2.0.0'
project_name = 'pyLTEVisualizer'
project_owner = "Author: Michael Duo Ling, Email: duo.ling.cn@gmail.com"
project_weblink = "http://code.google.com/p/pyltevisualizer/"