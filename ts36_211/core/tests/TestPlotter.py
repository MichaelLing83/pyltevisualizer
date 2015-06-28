import unittest
from ..Plotter import Plotter
from ..Matrix import Matrix
from random import random

class TestPlotter(unittest.TestCase):
    def test_plot_to_pic(self):
        X, Y = 10, 20
        matrix = Matrix(X, Y, float)
        for i in range(X):
            for j in range(Y):
                matrix[i][j] = random()
        plotter = Plotter(matrix)
        plotter.plot("test_temporary_plot.png")
    def test_plot_orientation(self):
        X, Y = 20, 4
        matrix = Matrix(X, Y, float)
        for i in range(X):
            matrix[i][0] = -1 + 0.1 * i
        plotter = Plotter(matrix)
        plotter.plot("test_temporary_plot_orientation.png")
