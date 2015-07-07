from .Enums import RE_TYPE

class Re(int):
    def __new__(cls, *args, **kw):
        if len(args) == 0:
            return int.__new__(cls, RE_TYPE.AVAILABLE, **kw)
        else:
            assert args[0] in RE_TYPE.all(), "{} is not a valid Re type".format(args[0])
            return int.__new__(cls, *args, **kw)
