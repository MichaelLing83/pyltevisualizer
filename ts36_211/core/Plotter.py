from .Matrix import Matrix
import matplotlib
matplotlib.use('Agg')   # for PNG, avoid using a window so it works on pure cmd
from numpy import zeros
import matplotlib.pyplot as plt



class Plotter:
    def __init__(self, matrix, dpi=160):
        assert isinstance(matrix, Matrix)
        self._matrix = matrix
        self.dpi = dpi
    def plot(self, fname):
        assert isinstance(fname, str), "{} is not a string, but {}".format(fname, type(fname))
        C = zeros( (self._matrix._size_y(), self._matrix._size_x()) )
        for j in range(self._matrix._size_y()):
            for i in range(self._matrix._size_x()):
                C[j][i] = self._matrix[i][j]
        plt.pcolormesh(C, cmap=plt.get_cmap("RdBu"))
        plt.savefig(fname, dpi=self.dpi)