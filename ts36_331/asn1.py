
#from pyltevisualizer.misc import bitstring
from ..misc.bitstring.bitstring import Bits
from math import ceil, log2

def ENUMERATED(name, *choices):
    assert isinstance(name, str)
    assert len(choices) > 0
    for c in choices:
        assert isinstance(c, str)
    d = dict()
    for i in range(len(choices)):
        d[choices[i]] = i
    d['length'] = ceil(log2(len(choices)))
    def init(self, isRequired, value=0):
        self.isRequired = isRequired
        self.value = 0
        self.set(value)
    d['__init__'] = init
    def __len(self):
        return self.__class__.length
    d['__len__'] = __len
    def set(self, value):
        assert 0 <= value < 2**self.length
        self.value = value
    d['set'] = set
    def code(self):
        return Bits(uint=self.value, length=self.length)
    d['code'] = code
    return type(name, (object,), d)

def BIT_STRING(name, length):
    assert isinstance(name, str)
    assert length > 0
    d = dict()
    d['length'] = length
    def init(self, isRequired, bits):
        self.isRequired = isRequired
        if isinstance(bits, int):
            assert 0 <= bits < 2**self.length
        elif isinstance(bits, Bits):
            assert bits.length == self.length
        elif isinstance(bits, str):
            bits = Bits(bytes=bits.encode('ascii'), length=self.length)
        elif isinstance(bits, bytes):
            assert len(bits) < self.length
            bits = Bits(bytes=bits, length=self.length)
        self.bits = bits
'''
class BIT_STRING:
    def __init__(self, length):
        assert isinstance(length, int) and length > 0
        self.length = length
        self.value = 0
    def __len__(self):
        return self.length
    def code(self, v):
        assert isinstance(v, int) and v >= 0 and v < 2**self.length
        return Bits(uint=v, length=self.length)

class SEQUENCE:
    def __init__(self, *args):
        assert len(args) > 0
        self.values = list()
        for attribute in args:
            assert isinstance(attribute, Bits)
                or isinstance(attribute, ENUMERATED)
                or isinstance(attribute, BIT_STRING)
                or isinstance(attribute, SEQUENCE)
            self.values.append(attribute)
    def __len__(self):
        length = 0
        for v in self.values:
            length += len(v)
        return length
    def code(self):
'''


dl_Bandwidth = ENUMERATED('n6', 'n15', 'n25', 'n50', 'n75', 'n100')