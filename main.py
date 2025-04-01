from Window import Window
from Point import Point
from Line import Line
from Cell import Cell

win = Window(800,600)
cell = Cell(Point(20,20),Point(40,40), win)
cell2 = Cell(Point(40,20),Point(60,40), win)
cell.draw_move(cell2)
cell.draw()
cell2.draw()
win.wait_for_close()