import unittest
from ..Frame import Frame, L1Config
from ..Plotter import Plotter

class TestMatrix(unittest.TestCase):
    def test_create(self):
        frame = Frame(L1Config())
        plotter = Plotter(frame)
        plotter.plot("test_temporary_plot_frame_blank.png")