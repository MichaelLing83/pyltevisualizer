'''
Created on 20 dec 2013

@author: linggduo

Terminology:
    1. longSf: long subframe number, which is systemFrameNumber * 10 + subframeNumber
'''
project_version = '2.0.0'
project_name = 'pyLTEVisualizer'
project_owner = "Author: Michael Duo Ling, Email: duo.ling.cn@gmail.com"
project_weblink = "http://code.google.com/p/pyltevisualizer/"

ENUM_MAX = 0

class RE_TYPE:
    '''
    Resource Element Type: used to mark each RE which PHY signal/channel is using this one.
    '''
    global ENUM_MAX
    size = 9
    AVAILABLE, CSRS_PORT0, CSRS_PORT1, CSRS_PORT2, CSRS_PORT3, CSRS_PORT4, CSRS_PORT5, CSRS_PORT6, CSRS_PORT7 = range(ENUM_MAX, ENUM_MAX+size)
    ENUM_MAX += size

class SF_TYPE:
    '''
    enum class for subframe type
    '''
    global ENUM_MAX
    size = 3
    D, U, S = range(ENUM_MAX, ENUM_MAX+size)
    ENUM_MAX += size

class CP_TYPE:
    '''
    Cyclic Prefix Type
    '''
    global ENUM_MAX
    size = 2
    NORMAL, EXTENDED = range(ENUM_MAX, ENUM_MAX+size)
    ENUM_MAX += size

class DELTA_F:
    global ENUM_MAX
    size = 2
    KHZ_7_5, KHZ_15 = range(ENUM_MAX, ENUM_MAX+size)
    ENUM_MAX += size

class BW:
    '''
    Up-link or down-link BandWidth
    '''
    global ENUM_MAX
    size = 6
    N6, N15, N25, N50, N75, N100 = range(ENUM_MAX, ENUM_MAX+size)
    ENUM_MAX += size
    @staticmethod
    def toReNumber(bw, cpType, delta_f):
        '''
        Calculate number of sub-carriers for the whole bandwidth.
        '''
        return BW.toRbNumber(bw) * BW.calc__N_RB_sc(cpType, delta_f)
    @staticmethod
    def toRbNumber(bw):
        '''
        Calculate number of Resource Blocks from given band-width.
        '''
        return (6,15,25,50,75,100)[bw-BW.N6]
    @staticmethod
    def calc__N_RB_sc(cpType, delta_f):
        '''
        Calculate number of sub-carriers for one Resource Block, according to table 6.2.3-1 in 36.211.
        '''
        if delta_f == DELTA_F.KHZ_15:
            return 12
        elif delta_f == DELTA_F.KHZ_7_5:
            return 24
        raise Exception("Unknown delta_f={0}".format(delta_f))

class ReTypeMatrix:
    '''
    Represents a matrix of Resource Elements. It's fast to grab any column of this matrix, but not rows.
    '''
    def __init__(self, rowDimension, columnDimension):
        self.rowDimension = rowDimension
        self.columnDimension = columnDimension
        self.m = [[RE_TYPE.AVAILABLE for j in range(self.rowDimension)] for i in range(self.columnDimension)]
    def getColumn(self, columnIndex):
        return self.m[columnIndex]

class ReTypeSubframe(ReTypeMatrix):
    '''
    Represents a subframe.
    '''
    def __init__(self, bw, cpType, delta_f, sfType, longSf, numOfPdcchSymbols):
        self.bw = bw
        self.cpType = cpType
        self.numOfPdcchSymbols = numOfPdcchSymbols
        self.sfType = sfType
        self.longSf = longSf
        super.__init(self, BW.toReNumber(bw, cpType, delta_f), 2*ReTypeSubframe.calcOfdmSymbolNumPerSlot(cpType, delta_f))
    @staticmethod
    def calcOfdmSymbolNumPerSlot(cpType, delta_f):
        '''
        Calculate number of OFDM symbols per slot.
        '''
        if cpType==CP_TYPE.NORMAL:
            return 7
        elif cpType==CP_TYPE.EXTENDED:
            if delta_f==DELTA_F.KHZ_15:
                return 6
            elif delta_f==DELTA_F.KHZ_7_5:
                return 3
        raise Exception("Unknown combination: cpType={0}, delta_f={1}".format(cpType, delta_f))

if __name__ == '__main__':
    pass