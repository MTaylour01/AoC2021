with open("input.txt", 'r') as f:
    lines = f.read().splitlines()

class Cave:

    def __init__(self, name):
        self.paths = []
        self.name = name
        self.isSmall = str.islower(self.name)
        self.traversed = False
    
    def addPath(self, cave):
        if cave not in self.paths:
            self.paths.append(cave)
            cave.addPath(self)
    
    def isSmall(self):
        return self.isSmall
    
    def getName(self):
        return self.name
    
    def isTraversable(self):
        return (not self.traversed) or (not self.isSmall)
    
    def traverse(self):
        self.traversed = True

    def getPaths(self):
        return self.paths

def traverse(cave):
    if not cave.isTraversable():
        return []
    if cave.getName() == "end":
        return [cave]
    cave.traverse()
    output = []
    for path in cave.getPaths():
        output.append([cave] + traverse(path))
    return output


def pt1(lines):
    caves = []
    for line in lines:
        startcavename = line.split("-")[0]
        endcavename = line.split("-")[1]
        startCave = Cave(startcavename)
        endCave = Cave(endcavename)
        for cave in caves:
            if startcavename == cave.getName():
                startCave = cave
            if endcavename == cave.getName():
                endCave = cave
        startCave.addPath(endCave)
        if startCave not in caves:
            caves.append(startCave)
        if endCave not in caves:
            caves.append(endCave)
    return traverse(caves[0])

paths = pt1(lines)
for path in paths:
    for cave in path:
        print(cave.getName())