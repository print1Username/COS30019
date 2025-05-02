import tkinter as tk


class Window:
    def __init__(self, width, height, title, size):
        self.width = width
        self.height = height
        self.title = title
        self.row = size[0]
        self.column = size[1]
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

    def CreateWindow(self):
        self.root.title(self.title)
        self.root.iconbitmap('image/icon.ico')
        self.root.geometry(str(self.width) + 'x' + str(self.height))

    def CalculateLength(self):
        if ((self.width - 100) / self.row) < ((self.height - 100) / self.column):
            size = (self.width - 100) / self.row
            start_x = 50
            start_y = (self.height - size * self.column) / 2
        else:
            size = (self.height - 100) / self.column
            start_x = (self.width - size * self.row) / 2
            start_y = 50
        return start_x, start_y, size

    def MakeSquare(self, w, h, fill, width, outline):
        if self.row >= w and self.column >= h:
            x, y, s = self.CalculateLength()
            self.canvas.create_rectangle(x + w * s, y + h * s, x + w * s + s, y + h * s + s, fill=fill, outline=outline, width=width)

    def CreateMaze(self):
        for i in range(self.row):
            for j in range(self.column):
                self.MakeSquare(i,j,'',3,'black')

    def CreateStart(self,start):
        for i in range(self.row):
            for j in range(self.column):
                if i == start[0] and j == start[1]:
                    self.MakeSquare(i,j,'red',3,'black')

    def CreateEnd(self,end):
        for e in end:
            for i in range(self.row):
                for j in range(self.column):
                    if int(e[0]) == i and int(e[1]) == j:
                        self.MakeSquare(i, j, 'lime', 3, 'black')

    def CreateWall(self,wall):
        for w in wall:
            for i in range(self.row):
                for j in range(self.column):
                    if (i >= w[0]) and (i < w[0] + w[2]) and (j >= w[1]) and (j < w[1] + w[3]):
                        self.MakeSquare(i,j,'gray',3,'black')

    def CreateSteps(self,move):
            for s in move:
                for i in range(self.row):
                    for j in range(self.column):
                        if s[0] == i and s[1] == j:
                            self.MakeSquare(i, j, 'yellow', 3, 'black')

    def LoopWindow(self):
        self.root.mainloop()