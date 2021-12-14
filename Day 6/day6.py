from collections import deque

class Ocean:
    def __init__(self, initList):
        self.ocean = dict(zip([-1,0,1,2,3,4,5,6,7,8],[0,0,0,0,0,0,0,0,0,0]))
        for num in initList.split(","):
            self.ocean[int(num)] += 1

    def passday(self):
        values_deque = deque(self.ocean.values())
        values_deque.rotate(-1)
        self.ocean = dict(zip(self.ocean.keys(), values_deque))
        self.ocean[6] += self.ocean[-1]
        self.ocean[8] += self.ocean[-1]
        self.ocean[-1] = 0

    def get_total(self):
        return sum(self.ocean.values())

with open("input.txt", 'r') as f:
    lines = f.read().splitlines()

ocean = Ocean(lines[0])

for day in range(0, 256):
    ocean.passday()

print(ocean.get_total())


