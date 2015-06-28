class _Array:
    def __init__(self):
        assert False, "_Array base class should not be instantilized!"
    def _norm_index(self, index, size):
        assert isinstance(index, int)
        assert isinstance(size, int)
        if index < -1 * size or index >= size:
            return size
        else:
            return (index + size) % size
class Column(_Array):
    def __init__(self, matrix, column_index):
        assert 0 <= column_index < matrix._size_x()
        self.__matrix = matrix
        self.__column_index = column_index
    def __getitem__(self, index):
        size_y = self.__matrix._size_y()
        assert -1 * size_y <= index < size_y
        index = (index + size_y) % size_y
        return self.__matrix[(self.__column_index, index)]
    def __setitem__(self, index, value):
        assert isinstance(value, self.__matrix._class)
        size_y = self.__matrix._size_y()
        assert -1 * size_y <= index < size_y
        index = (index + size_y) % size_y
        self.__matrix[(self.__column_index, index)] = value
        return value
    def __eq__(self, column):
        if ( isinstance(column, self.__class__)
            and column.__matrix is self.__matrix
            and column.__column_index == self.__column_index):
            return True
        # TODO: add a branch to compare Columns from different Matrix instances
        else:
            return False

class Row(_Array):
    def __init__(self, matrix, column_index):
        self.__matrix = matrix
        self.__column_index = column_index
    def __getitem__(self, index):
        return self.__matrix._getitem(index, self.__column_index)
    def __eq__(self, row):
        if ( isinstance(row, self.__class__)
            and row.__matrix is self.__matrix
            and row.__column_index == self.__column_index):
            return True
        else:
            return False

class Matrix(_Array):
    '''
    A matrix, column oriented, meaning Matrix[x] gives you its xth column.
    '''
    def __init__(self, size_x, size_y, _class,
                 start_x=None, start_y=None,
                 end_x=None, end_y=None,
                 data=None):
        assert size_x > 0
        assert size_y > 0
        self.__size_x = size_x
        self.__size_y = size_y
        self._class = _class
        if start_x:
            self.__start_x = start_x
        else:
            self.__start_x = 0
        if start_y:
            self.__start_y = start_y
        else:
            self.__start_y = 0
        if end_x:
            self.__end_x = end_x
        else:
            self.__end_x = self.__size_x
        if end_y:
            self.__end_y = end_y
        else:
            self.__end_y = self.__size_y
        if data:
            self.__data = data
        else:
            self.__data = dict()
        self.debug = False
    def _sizes(self):
        return (self._size_x(), self._size_y())
    def shape(self):
        return self._sizes()
    def _size_x(self):
        return self.__end_x - self.__start_x
    def _size_y(self):
        return self.__end_y - self.__start_y
    def __len__(self):
        return self._size_x()
    def __getitem__(self, selection):
        if self.debug:
            print("selection={} of {}".format(selection, type(selection)))
        if isinstance(selection, int):
            # get one column
            return Column(self, (selection + self.__size_x) % self.__size_x)
        elif isinstance(selection, tuple) or isinstance(selection, list):
            # get one cell
            assert len(selection) == 2
            column, row = selection
            assert 0 <= column < self._size_x()
            assert 0 <= row < self._size_y()
            _key = (column, row)
            if _key not in self.__data:
                self.__data[_key] = self._class()
            return self.__data[_key]
        elif isinstance(selection, slice):
            if self.debug:
                print("selection={}:{}".format(selection.start, selection.stop))
            if selection.start:
                start_x = self._norm_index(selection.start, self._size_x())
            else:
                start_x = 0
            if selection.stop:
                end_x = self._norm_index(selection.stop, self._size_x())
            else:
                end_x = self.__size_x
            if self.debug:
                print("start_x={}, end_x={}".format(start_x, end_x))
            if start_x == 0 and end_x == self.__size_x:
                return self
            else:
                return Matrix(self.__size_x, self.__size_y, self._class,
                              start_x, 0, end_x, self.__size_y, self.__data)
    def __setitem__(self, selection, value):
        '''
        Assign value(s) to a cell, a column, a slice of columns, or the whole Matrix.
        '''
        assert isinstance(value, self._class)
        if isinstance(selection, tuple) or isinstance(selection, list):
            assert len(selection) == 2
            column, row = selection
            assert 0 <= column < self._size_x()
            assert 0 <= row < self._size_y()
            self.__data[(column, row)] = value
        return value
    def count(self, func):
        '''
        for each cell in this matrix:
            call func(cell)
        return total count of such function calls that return True
        '''
        num = 0
        for i in range(self._size_x()):
            for j in range(self._size_y()):
                if func(self[i][j]):
                    num += 1
        return num
