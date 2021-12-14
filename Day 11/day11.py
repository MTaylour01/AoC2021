class Octopus:
    def __init__(self, initEnergy, x, y, grid):
        self.energy = initEnergy
        self.flashedThisTurn = False
        self.grid = grid
        self.x = x
        self.y = y
    
    def increaseEnergy(self):
        self.energy += 1
        if self.energy > 9 and not self.flashedThisTurn:
            self.flashedThisTurn = True
            self.grid.addToFlash(self.x, self.y)

    def endStep(self):
        self.flashedThisTurn = False
        if self.energy > 9:
            self.energy = 0

    def getVal(self):
        return self.energy

class Grid:
    def __init__(self, lines):
        self.grid = []
        self.toFlash = []
        self.totFlashes = 0
        splitlines = list(map((lambda a : list(a)),lines))
        for i in range(0, len(splitlines)):
            row = []
            for j in range(0, len(splitlines[i])):
                row.append(Octopus(int(splitlines[i][j]), i, j, self))
            self.grid.append(row)

    def step(self):
        for row in self.grid:
            for octopus in row:
                octopus.increaseEnergy()
        while self.toFlash:
            octToFlash = self.toFlash.pop()
            self.flashed(octToFlash[0], octToFlash[1])
        for row in self.grid:
            for octopus in row:
                octopus.endStep()
    
    def addToFlash(self, x, y):
        self.toFlash.append([x,y])

    def flashed(self, x, y):
        self.totFlashes += 1
        #print("(" + str(x) + "," + str(y) + ") flashed")
        for i in range(-1,2):
            for j in range(-1,2):
                if inbounds(self.grid, x+i, y+j):
                    self.grid[x+i][y+j].increaseEnergy()

    def getFlashes(self):
        return self.totFlashes

    def getGrid(self):
        out = []
        for row in self.grid:
            outrow = []
            for oct in row:
                outrow.append(oct.getVal())
            out.append(outrow)
        return out

with open("input.txt", 'r') as f:
    lines = f.read().splitlines()

def pt1(lines):
    grid = Grid(lines)
    for i in range(0,100):
        grid.step()
    print(grid.getFlashes())
    for row in grid.getGrid():
        print(row)

def inbounds(grid, x, y):
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x])

pt1(lines)

def pt2(lines):
    grid = Grid(lines)
    step = 0
    while True:
        grid.step()
        step += 1
        isSynced = True
        for row in grid.getGrid():
            for val in row:
                if val != 0:
                    isSynced = False
        if isSynced:
            return step

print(pt2(lines))