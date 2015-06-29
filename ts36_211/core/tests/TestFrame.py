import unittest
from ..Frame import Frame, L1Config

class TestMatrix(unittest.TestCase):
    def test_create(self):
        frame = Frame(L1Config())