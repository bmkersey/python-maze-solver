from Line import Line
from Point import Point

class Cell:
  def __init__(self, top_point, bottom_point, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
    self.x1 = top_point.x
    self.y1 = top_point.y
    self.x2 = bottom_point.x
    self.y2 = bottom_point.y
    self.has_left_wall = has_left_wall
    self.has_right_wall = has_right_wall
    self.has_top_wall = has_top_wall
    self.has_bottom_wall = has_bottom_wall
    self.win = win

  def draw(self, fill_color="black"):
    if self.has_left_wall:
      self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), fill_color)
    if self.has_right_wall:
      self.win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), fill_color)
    if self.has_top_wall:
      self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), fill_color)
    if self.has_bottom_wall:
      self.win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), fill_color)
  
  def draw_move(self, to_cell, undo=False):
    path = Line(Point((self.x1 + self.x2)/2, (self.y1 + self.y2)/2), Point((to_cell.x1 + to_cell.x2)/2, (to_cell.y1 + to_cell.y2)/2))
    if undo == False:
      self.win.draw_line(path, fill_color="red")
    else:
      self.win.draw_line(path, fill_color="gray")