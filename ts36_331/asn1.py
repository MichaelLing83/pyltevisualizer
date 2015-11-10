
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
    def init(self, value=0):
        self.value = 0
        self.set(value)
    d['__init__'] = init
    def __len(self):
        return self.__class__.length
    d['__len__'] = __len
    def eq(self, enum):
        return self.value == enum.value
    d['__eq__'] = eq
    def set(self, value):
        if isinstance(value, int):
            assert 0 <= value < 2**self.length
            self.value = value
        elif isinstance(value, Bits):
            assert value.length == self.length
            self.value = value.uint
        return self
    d['set'] = set
    def code(self):
        return Bits(uint=self.value, length=self.length)
    d['code'] = code
    @classmethod
    def decode(cls, bits):
        assert isinstance(bits, Bits)
        return cls().set(bits)
    d['decode'] = decode
    return type(name, (object,), d)

def BIT_STRING(name, length):
    assert isinstance(name, str)
    assert length > 0
    d = dict()
    d['length'] = length
    def init(self, bits=0):
        self.set(bits)
    d['__init__'] = init
    def _len(self):
        return self.__class__.length
    d['__len__'] = _len
    def eq(self, bitstring):
        return self.bits == bitstring.bits
    d['__eq__'] = eq
    def set(self, bits):
        if isinstance(bits, int):
            assert 0 <= bits < 2**self.length
            bits = Bits(uint=bits, length=self.length)
        elif isinstance(bits, Bits):
            assert bits.length == self.length
        elif isinstance(bits, str):
            bits = Bits(bytes=bits.encode('ascii'), length=self.length)
        elif isinstance(bits, bytes):
            assert 8 * len(bits) <= self.length
            if 8 * len(bits) < self.length:
                bits = b'0' * ceil((self.length - 8*len(bits))/8) +  bits
            bits = Bits(bytes=bits, length=self.length, offset=len(bits)*8-self.length)
        self.bits = bits
        return self
    d['set'] = set
    def code(self):
        return self.bits
    d['code'] = code
    @classmethod
    def decode(cls, bits):
        assert isinstance(bits, Bits)
        return cls().set(bits)
    d['decode'] = decode
    return type(name, (object,), d)

def SEQUENCE(name, *members):
    assert len(members) > 0
    for member in members:
        assert not isinstance(member, type) # should not be a class
    d = dict()
    l = list()
    length = 0
    for member in members:
        d[str(member.__class__).split('.')[-1][:-2]] = member
        l.append(member)
        length += len(member)
    d['length'] = length
    d['members'] = l
    def code(self):
        bits = self.members[0].code()
        for member in self.members[1:]:
            bits += member.code()
        return bits
    d['code'] = code
    def _len(self):
        return self.__class__.length
    d['__len__'] = _len
    def eq(self, seq):
        result = True
        for i in range(len(self.members)):
            result = result and self.members[i] == seq.members[i]
            if not result: break
        return result
    d['__eq__'] = eq
    @classmethod
    def decode(cls, bits):
        assert isinstance(bits, Bits)
        seq = cls()
        index = 0
        for member in seq.members:
            member.set(bits[index:index+member.length])
            index += member.length
        return seq
    d['decode'] = decode
    return type(name, (object,), d)


Dl_Bandwidth = ENUMERATED('Dl_Bandwidth', 'n6', 'n15', 'n25', 'n50', 'n75', 'n100')
Phich_Duration = ENUMERATED('Phich_Duration', 'normal', 'extended')
Phich_Resource = ENUMERATED('Phich_Resource', 'oneSixth', 'half', 'one', 'two')
PHICH_Config = SEQUENCE('PHICH_Config', Phich_Duration(), Phich_Resource())
SystemFrameNumber = BIT_STRING('SystemFrameNumber', 8)
MasterInformationBlock = SEQUENCE('MasterInformationBlock', Dl_Bandwidth(), PHICH_Config(), SystemFrameNumber(), BIT_STRING('Spare', 10)())







