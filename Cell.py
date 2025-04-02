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
    path = Line(Point((self.x1 + self.x2)/2, (self.y1 + self.y2)/2), Point((to_cell.x1 + to_cell.x2)/2, (to_cell.y1 + to_cell.y2)/2))
    if undo == False:
      self.win.draw_line(path, fill_color="red")
    else:
      self.win.draw_line(path, fill_color="gray")