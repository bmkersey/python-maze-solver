from Line import Line
from Point import Point

class Cell:
  def __init__(self, win=None):
    self.x1 = None
    self.y1 = None
    self.x2 = None
    self.y2 = None
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self.win = win
    self.visited = False

  def draw(self, x1, y1, x2, y2, fill_color="black", background_color="#d9d9d9"):
    if self.win:
      self._x1 = x1
      self._x2 = x2
      self._y1 = y1
      self._y2 = y2
      
      if self.has_left_wall:
        self.win.draw_line(Line(Point(x1, y1), Point(x1, y2)), fill_color)
      else:
        self.win.draw_line(Line(Point(x1, y1), Point(x1, y2)), background_color)
      if self.has_right_wall:
        self.win.draw_line(Line(Point(x2, y1), Point(x2, y2)), fill_color)
      else:
        self.win.draw_line(Line(Point(x2, y1), Point(x2, y2)), background_color)
      if self.has_top_wall:
        self.win.draw_line(Line(Point(x1, y1), Point(x2, y1)), fill_color)
      else:
        self.win.draw_line(Line(Point(x1, y1), Point(x2, y1)), background_color)
      if self.has_bottom_wall:
        self.win.draw_line(Line(Point(x1, y2), Point(x2, y2)), fill_color)
      else:
        self.win.draw_line(Line(Point(x1, y2), Point(x2, y2)), background_color)

  def draw_move(self, to_cell, undo=False):
    half_length = abs(self._x2 - self._x1) // 2
    x_center = half_length + self._x1
    y_center = half_length + self._y1

    half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
    x_center2 = half_length2 + to_cell._x1
    y_center2 = half_length2 + to_cell._y1

    fill_color = "green"
    if undo:
      fill_color = "red"

    line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
    self.win.draw_line(line, fill_color)
