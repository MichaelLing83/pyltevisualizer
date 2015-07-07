import unittest
from ..Re import Re
from ..Enums import RE_TYPE

class TestRe(unittest.TestCase):
    def test_create_default(self):
        re = Re()
        assert re == RE_TYPE.AVAILABLE, "default value should be RE_TYPE.AVAILABLE"
    def test_create_non_default(self):
        for re_type in RE_TYPE.all():
            re = Re(re_type)
            assert re == re_type