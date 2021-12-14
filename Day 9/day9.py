import numpy

class Cave:

    def __init__(self, inp):
        self.cave = []
        self.basins = []
        for line in inp:
            self.cave.append([int(char) for char in line])
        self.padded = numpy.pad(self.cave, (1,), 'constant', constant_values=10)
        self.basin_cave = numpy.pad(self.cave, (1,), 'constant', constant_values=9)
        self.explored = []

    def getCave(self):
        return self.cave

    def get(self, i, j):
        return self.cave[i][j]

    def is_local_minima(self, i ,j):
        val = self.cave[i][j]
        i += 1
        j += 1
        return (val < self.padded[i+1][j] and val < self.padded[i-1][j] and val < self.padded[i][j+1] and val < self.padded[i][j-1])

    def get_local_minima(self):
        mins = []
        for i in range(0, len(self.cave)):
            for j in range(0, len(self.cave[i])):
                if self.is_local_minima(i,j):
                    mins.append((i,j))
        return mins

    def getNines(self):
        nines = []
        for i in range(0, len(self.cave)):
            for j in range(0, len(self.cave[i])):
                if self.cave[i][j] == 9:
                    nines.append((i,j))
        return nines

    def getBasin(self, pos):
        i = pos[0]
        j = pos[1]
        if pos in self.explored:
            return []
        self.explored.append(pos)
        if self.basin_cave[i][j] == 9:
            return []
        return [pos] + self.getBasin([i+1,j]) + self.getBasin([i-1,j]) + self.getBasin([i,j+1]) + self.getBasin([i,j-1])
        
def prod(xs):
    out = 1
    for x in xs:
        out = out * x
    return out
    

with open("input.txt", 'r') as f:
    lines = f.read().splitlines()

cave = Cave(lines)

mins = cave.get_local_minima()
print(sum(list(map(lambda a : cave.get(a[0],a[1])+1,mins))))

basins = []
for min in mins:
    i = min[0]+1
    j = min[1]+1
    basins.append(cave.getBasin([i,j]))

sizes = list(map(len,basins))
sizes.sort()


print(prod(sizes[-3:]))