with open("input.txt", 'r') as f:
    lines = f.read().splitlines()


def isCorrupted(line):
    stack = []
    for char in line:
        if char == "(" or char == "<" or char == "[" or char == "{":
            stack.append(char)
        elif stack == []:
            return True
        elif char == ")":
            if stack.pop() != "(":
                return True
        elif char == "]":
            if stack.pop() != "[":
                return True
        elif char == ">":
            if stack.pop() != "<":
                return True
        elif char == "}":
            if stack.pop() != "{":
                return True
    return False

def getCorrupted(line):
    stack = []
    for char in line:
        if char == "(" or char == "<" or char == "[" or char == "{":
            stack.append(char)
        elif stack == []:
            return char
        elif char == ")":
            if stack.pop() != "(":
                return char
        elif char == "]":
            if stack.pop() != "[":
                return char
        elif char == ">":
            if stack.pop() != "<":
                return char
        elif char == "}":
            if stack.pop() != "{":
                return char
    return " "

def finish(line):
    stack = []
    tot = 0
    finishValues = dict([("(",1), ("[",2), ("{", 3), ("<", 4)])
    for char in line:
        if char == "(" or char == "<" or char == "[" or char == "{":
            stack.append(char)
        elif char == ")" or char == ">" or char == "]" or char == "}":
            stack.pop()
    while stack:
        tot = (tot*5) + finishValues[stack.pop()]
    return tot
        



def pt1(lines):
    corrValues = dict([(")",3), ("]",57), ("}", 1197), (">", 25137), (" ", 0)])
    tot = 0
    for line in lines:
        tot += corrValues[getCorrupted(line)]
    print(tot)


def pt2(lines):
    incomplete = list(filter((lambda a : not isCorrupted(a)), lines))
    finishVals = list(map(finish,incomplete))
    finishVals.sort()
    print(finishVals[len(finishVals) // 2])

pt2(lines)