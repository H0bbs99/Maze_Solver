from tkinter import Tk
from window import *

class Point():
    def __init__(self):
        self.xcoord = 0
        self.ycoord = 0

class Line():
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(canvas, fill_color):
        
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)