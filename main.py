from Window import Window
from Point import Point
from Line import Line
from Cell import Cell
from Maze import Maze

win = Window(800,600)
starting_point = Point(100,100)
maze = Maze(starting_point,10,10,20,20,win)
win.wait_for_close()