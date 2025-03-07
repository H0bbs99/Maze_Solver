from graphic import Line, Point

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell size_y, win)
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        for i in range(num_rows):
            row = []
            for j in range(num_cols):
                cell = Cell(win)
                row.append(cell)
            self._cells.append(row)
        
        self._create_cells
    
    def _create_cells(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                x1 = self._x1 + j * self._cell_size_x
                y1 = self._y1 + i * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                self._cells[i][j].draw(x1, y1, x2, y2)

        for i in range(self