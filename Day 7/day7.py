with open("input.txt", 'r') as f:
    crabs = list(map(int, f.read().splitlines()[0].split(",")))
    

print(crabs)

def sumTo(x):
    return sum(range(1,x+1))

def sum_distance(inpList, point):
    sum = 0
    for num in inpList:
        sum += sumTo(abs(point - num))
    return sum

def findMinPoint(inpList):
    distances = []
    for i in range(min(inpList), max(inpList)):
        distances.append(sum_distance(inpList, i))
    return min(distances)

print(findMinPoint(crabs))



