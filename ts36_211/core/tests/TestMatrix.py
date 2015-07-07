import unittest
from ..Matrix import Matrix, Column
from random import randint

_CLASS = int
_X_SIZE, _Y_SIZE = 100, 90

class TestMatrix(unittest.TestCase):
    def test_create(self):
        # 100 elements for x-axis, and 90 for y-axis
        matrix = Matrix(_X_SIZE, _Y_SIZE, _CLASS)

        assert matrix._sizes() == (_X_SIZE, _Y_SIZE)
        assert matrix._size_x() == _X_SIZE
        assert matrix._size_y() == _Y_SIZE
    def test_column_indexing(self):
        # 100 elements for x-axis, and 90 for y-axis
        matrix = Matrix(_X_SIZE, _Y_SIZE, _CLASS)

        assert isinstance(matrix[randint(0,_X_SIZE)], Column)
        # make sure minus index also works
        for i in range(_X_SIZE):
            tmp_column = matrix[i]
            assert matrix[i - _X_SIZE] == tmp_column
    def test_cell_indexing(self):
        # 100 elements for x-axis, and 90 for y-axis
        matrix = Matrix(_X_SIZE, _Y_SIZE, _CLASS)
        for i in range(_X_SIZE):
            for j in range(_Y_SIZE):
                matrix[i][j] = i * _Y_SIZE + j
                assert matrix[i][j] == matrix[(i, j)] == i * _Y_SIZE + j

        assert isinstance(matrix[randint(0, _X_SIZE)][randint(0, _Y_SIZE)],
                          _CLASS)
    def test_column_slicing(self):
        # 100 elements for x-axis, and 90 for y-axis
        matrix = Matrix(_X_SIZE, _Y_SIZE, _CLASS)
        for i in range(_X_SIZE):
            for j in range(_Y_SIZE):
                matrix[i][j] = i * _Y_SIZE + j

        # slicing to get all -> the same matrix instance
        assert isinstance(matrix[:], Matrix)
        assert matrix[:] is matrix
        assert matrix[:]._Matrix__data is matrix._Matrix__data
        assert matrix[0:] is matrix
        assert matrix[0:]._Matrix__data is matrix._Matrix__data
        assert matrix[:_X_SIZE] is matrix
        assert matrix[:_X_SIZE]._Matrix__data is matrix._Matrix__data
        assert matrix[(-1 * _X_SIZE):] is matrix
        assert matrix[(-1 * _X_SIZE):]._Matrix__data is matrix._Matrix__data

        # slicing to get one Column
        assert isinstance(matrix[0], Column)
        assert matrix[0]._Column__matrix._Matrix__data is matrix._Matrix__data

        # slicing to get multiple adjacent columns
        assert isinstance(matrix[:3], Matrix)
        assert matrix[:3]._sizes() == (3, _Y_SIZE)
        assert matrix[:3]._Matrix__data is matrix._Matrix__data
        assert matrix[-3:]._sizes() == (3, _Y_SIZE)
        assert matrix[-3:]._Matrix__data is matrix._Matrix__data
        assert matrix[3:5]._sizes() == (2, _Y_SIZE)
        assert matrix[3:5]._Matrix__data is matrix._Matrix__data

    def test_count(self):
        # 100 elements for x-axis, and 90 for y-axis
        matrix = Matrix(_X_SIZE, _Y_SIZE, _CLASS)
        for i in range(_X_SIZE):
            for j in range(_Y_SIZE):
                matrix[i][j] = i * _Y_SIZE + j
        def xxx(value):
            if value >= 10:
                return True
            else:
                return False
        assert matrix.count(xxx) == _X_SIZE * _Y_SIZE - 10

