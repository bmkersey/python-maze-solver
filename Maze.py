from Point import Point
from Cell import Cell
import time
import random

class Maze:
  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
    self._cells = []
    self.x1 = x1
    self.y1 = y1
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.cell_size_x = cell_size_x
    self.cell_size_y = cell_size_y
    self.win = win
    if seed is not None:
      self.seed = random.seed(seed)
    self._create_cells()
    self._break_entrance_and_exit()
    self._break_walls_r(0,0)
    self._reset_cells_visited()
    self.solve()

  def _create_cells(self):
    for i in range(self.num_cols):
      col = []
      for j in range(self.num_rows):
        col.append(Cell(self.win))
      self._cells.append(col)
    
    for i in range(self.num_cols):
      for j in range(self.num_rows):
        self._draw_cell(i,j)
  
  def _draw_cell(self, i, j):
    if self.win is None:
      return
    x1 = self.x1 + i * self.cell_size_x
    y1 = self.y1 + j * self.cell_size_y
    x2 = x1 + self.cell_size_x
    y2 = y1 + self.cell_size_y
    
    self._cells[i][j].draw(x1, y1, x2, y2)

    self._animate()

  def _animate(self):
    if self.win is None:
      return
    if self.win:
      self.win.redraw()
      time.sleep(0.1)

  def _break_entrance_and_exit(self):
    self._cells[0][0].has_top_wall = False
    self._draw_cell(0,0)
    self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
    self._draw_cell(self.num_cols - 1, self.num_rows - 1)

  def _break_walls_r(self, i, j):
    self._cells[i][j].visited = True
    
    while True:
      possible_directions = []
      if j > 0 and not self._cells[i][j-1].visited:
        possible_directions.append((i, j - 1))
      if i < self.num_cols - 1 and not self._cells[i+1][j].visited:
        possible_directions.append((i + 1, j))
      if j < self.num_rows - 1 and not self._cells[i][j+1].visited:
        possible_directions.append((i, j + 1))
      if i > 0 and not self._cells[i-1][j].visited:
        possible_directions.append((i - 1, j))
      if len(possible_directions) == 0:
        self._draw_cell(i, j)
        return

      next_cell_inx = random.randrange(len(possible_directions))
      next_index = possible_directions[next_cell_inx]

      if next_index[0] == i + 1:
        self._cells[i][j].has_right_wall = False
        self._cells[i + 1][j].has_left_wall = False
      if next_index[0] == i - 1:
        self._cells[i][j].has_left_wall = False
        self._cells[i - 1][j].has_right_wall = False
      if next_index[1] == j + 1:
        self._cells[i][j].has_bottom_wall = False
        self._cells[i][j + 1].has_top_wall = False
      if next_index[1] == j - 1:
        self._cells[i][j].has_top_wall = False
        self._cells[i][j - 1].has_bottom_wall = False

      self._break_walls_r(next_index[0], next_index[1])

  def _reset_cells_visited(self):
    for col in self._cells:
      for cell in col:
        cell.visited = False

  def solve(self):
    result = self._solve_r(0,0)
    if result == False:
      return False
    return True
  
  def _solve_r(self, i, j):
    self._animate()
    self._cells[i][j].visited = True
    possible_directions = [(0, 1, "has_bottom_wall"), (1, 0, "has_right_wall"), (0, -1, "has_top_wall"), (-1, 0, "has_left_wall")]
    if i == self.num_cols -1 and j == self.num_rows -1:
      return True
    for di, dj, wall_property in possible_directions:
      new_i = i + di
      new_j = j + dj
      if 0 <= new_i < self.num_cols and 0 <= new_j < self.num_rows:  
        cell = self._cells[i][j]
        new_cell = self._cells[new_i][new_j]
        if not getattr(cell, wall_property) and new_cell.visited == False:
          cell.draw_move(new_cell)
          result = self._solve_r(new_i, new_j)
          if result:
            return True
          cell.draw_move(new_cell, undo=True)
          new_cell.visited = False
    return False

    