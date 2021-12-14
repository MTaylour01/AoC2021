class Map:
    def __init__(self, size):
        self.size = size
        self.board = []
        for i in range(0, size):
            row = []
            for j in range(0,size):
                row.append(".")
            self.board.append(row)

    def add_line(self, line):
        if line.get_start().getx() == line.get_end().getx():
            for j in line.spany():
                self.increment(line.get_start().getx(), j)
        elif line.get_start().gety() == line.get_end().gety():
            for i in line.spanx():
                self.increment(i, line.get_start().gety())
        else:
            for point in zip(line.spanx(), line.spany()):
                self.increment(point[0], point[1])


    def getboard(self):
        return self.board

    def increment(self, x, y):
        if self.board[x][y] == ".":
            self.board[x][y] = "1"
        else:
            self.board[x][y] = str(int(self.board[x][y]) + 1)

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getx(self):
        return self.x
    
    def gety(self):
        return self.y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def get_start(self):
        return self.start
    
    def get_end(self):
        return self.end

    def spanx(self):
        if self.start.getx() > self.end.getx():
            return range(self.start.getx(), self.end.getx()-1, -1)
        else:
            return range(self.start.getx(), self.end.getx()+1)

    def spany(self):
        if self.start.gety() > self.end.gety():
            return range(self.start.gety(), self.end.gety()-1, -1)
        else:
            return range(self.start.gety(), self.end.gety()+1)
                   
     


with open("input.txt", 'r') as f:
    lines = f.read().splitlines()

map = Map(1000)
for line in lines:
    coords = line.split(" -> ")
    startCoord = Coord(int(coords[0].split(",")[1]), int(coords[0].split(",")[0]))
    endCoord = Coord(int(coords[1].split(",")[1]), int(coords[1].split(",")[0]))
    newline = Line(startCoord, endCoord)
    map.add_line(newline)

count = 0
myBoard = map.getboard()
for row in myBoard:
    for num in row:
        if num == "." or num == "1":
            pass
        else:
            count += 1
print(count)
