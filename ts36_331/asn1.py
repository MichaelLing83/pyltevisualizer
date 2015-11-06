
#from pyltevisualizer.misc import bitstring
from ..misc.bitstring.bitstring import Bits
from math import ceil, log2

class ENUMERATED:
    def __init__(self, *args):
        assert len(args) > 0
        self.value = 0
        self.length = ceil(log2(len(args)))
        value = 0
        for attribute in args:
            self.__setattr__(attribute, value)
            value += 1
    def __len__(self):
        return self.length
    def code(self, v):
        if isinstance(v, str):
            assert v in self.__dict__.keys()
            return Bits(uint=self.__getattribute__(v), length=self.length)
        elif isinstance(v, int):
            assert v in self.__dict__.values()
            return Bits(uint=v, length=self.length)

dl_Bandwidth = ENUMERATED('n6', 'n15', 'n25', 'n50', 'n75', 'n100')