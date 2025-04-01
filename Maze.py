from Point import Point
from Cell import Cell
import time

class Maze:
  def __init__(self, starting_point, num_rows, num_cols, cell_size_x, cell_size_y, win):
    self.x1 = starting_point.x
    self.y1 = starting_point.y
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.cell_size_x = cell_size_x
    self.cell_size_y = cell_size_y
    self.win = win
    self._create_cells()

  def _create_cells(self):
    self._cells = []
    for i in range(self.num_cols):
      col = []
      for j in range(self.num_rows):
        col.append(None)
      self._cells.append(col)
    
    for i in range(self.num_cols):
      for j in range(self.num_rows):
        self._draw_cell(i,j)
  
  def _draw_cell(self, i, j):
    x1 = self.x1 + i * self.cell_size_x
    y1 = self.y1 + j * self.cell_size_y
    x2 = x1 + self.cell_size_x
    y2 = y1 + self.cell_size_y

    top_point = Point(x1, y1)
    bottom_point = Point(x2, y2)
    self._cells[i][j] = Cell(top_point, bottom_point, self.win)
    self._cells[i][j].draw()

    self._animate()

  def _animate(self):
    self.win.redraw()
    time.sleep(0.05)