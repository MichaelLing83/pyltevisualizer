'''
Created on 27 dec 2013

@author: Michael Duo Ling
'''

from Enums import RE_TYPE, BW, CP_TYPE, DELTA_F

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, p):
        if type(p) == tuple:
            x,y = p
            return Point(self.x+x,self.y+y)
        else:
            return Point(self.x+p.x,self.y+p.y)
    
    def __sub__(self, p):
        return Point(self.x-p.x,self.y-p.y)

    def __str__(self):
        return "%s, %s" % (self.x,self.y)
    
    def toTuple(self):
        return (self.x, self.y)

Size = Point

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
        super(ReTypeSubframe, self).__init__(BW.toReNumber(bw, cpType, delta_f), 2 * ReTypeSubframe.calcOfdmSymbolNumPerSlot(cpType, delta_f))
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