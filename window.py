from tkinter import Tk, BOTH, Canvas
from drawing import Point, Line

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.named_title = "I'm a maze Solver"
        
        self.__root = Tk()
        self.__root.title(self.named_title)
        self.__canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.__canvas.pack()

        self.__window_running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        # Updates the Canvas Window
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        # While window running is true, it will continue to redraw
        self.__window_running = True

        while self.__window_running:
            self.redraw()
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
        
    def close(self):
        self.__window_running = False


        