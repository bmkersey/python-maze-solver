from Window import Window
from Point import Point
from Line import Line

win = Window(800,600)
start_point = Point(20,20)
end_point = Point(600,20)
full_line = Line(start_point, end_point)
win.draw_line(full_line, "black")
win.wait_for_close()