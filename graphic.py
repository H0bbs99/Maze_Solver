from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(   self, width, height):
        self.width = width
        self.height = height
        
        
        self.__root = Tk()
        self.__root.title("Maze Solver Boot.dev")
        self.__canvas = Canvas(self.__root, bg="white", width=self.width, height=self.height)
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

    @property
    def canvas(self):
        return self.__canvas




class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color):
        
        canvas.create_line(self.point_a.x,self.point_a.y, self.point_b.x, self.point_b.y, fill=fill_color, width=2)