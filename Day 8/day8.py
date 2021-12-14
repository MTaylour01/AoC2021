with open("input.txt", 'r') as f:
    lines = f.read().splitlines()

def subset(xs, ys):
    for x in xs:
        if not x in ys:
            return False
    return True

def rem(str1, str2):
    out = ""
    for char in str1:
        if not char in str2:
            out += char
    return out

def sort_string(str):
    sorted_chars = sorted(str)
    sorted_str = "".join(sorted_chars)
    return sorted_str

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def get_key(val, myDict):
    for key, value in myDict.items():
        if val == value[0]:
            return key

def getOutput(line):
    numbers = dict(zip(list(range(0,10)), [[] for i in range(0,10)]))
    sections = dict(zip(list(char_range('a','g')),[""]*8))
    for num in line.split("|")[0].split(" "):
        num = sort_string(num)
        if len(num) == 2:
            numbers[1] = [num]
        elif len(num) == 3:
            numbers[7] = [num]
        elif len(num) == 4:
            numbers[4] = [num]
        elif len(num) == 7:
            numbers [8] = [num]
        elif len(num) == 5:
            numbers[2].append(num)
            numbers[3].append(num)
            numbers[5].append(num)
        elif len(num) == 6:
            numbers[0].append(num)
            numbers[6].append(num)
            numbers[9].append(num)
    print(numbers[4])
    print(numbers[9])
    numbers[9] = list(filter(lambda a: subset(numbers[4][0], a), numbers[9]))
    numbers[0] = list(filter((lambda a : not subset(rem(numbers[9][0], numbers[7][0]), a)), numbers[0]))
    numbers[6].remove(numbers[9][0])
    numbers[6].remove(numbers[0][0])
    sections['a'] = rem(numbers[7][0], numbers[1][0])
    sections['c'] = rem(numbers[8][0], numbers[6][0])
    sections['d'] = rem(numbers[8][0], numbers[0][0])
    sections['e'] = rem(numbers[8][0], numbers[9][0])
    sections['g'] = rem(rem(numbers[9][0], numbers[4][0]), sections['a'])
    numbers[2] = [sort_string(sections['a'] + sections['c'] + sections['d'] + sections['e'] + sections['g'])]
    print(numbers[7][0])
    print(numbers[3])
    print(numbers[2][0])
    numbers[3].remove(numbers[2][0])
    numbers[5].remove(numbers[2][0])
    numbers[3] = list(filter((lambda a : sections['c'] in a), numbers[3]))
    numbers[5].remove(numbers[3][0])
    sections['f'] = rem(numbers[1][0], sections['c'])
    sections['b'] = rem(numbers[8][0], sections['a'] + sections['c'] + sections['d'] + sections['e'] + sections['f'] + sections['g'])
        
    outNum = ""
    for digit in line.split("|")[1].split():
        sortedDigit = sort_string(digit)
        outNum = outNum + str(get_key(sortedDigit, numbers))
    return outNum

def pt2():
    finalSum = 0
    for line in lines:
        finalSum += int(getOutput(line))
        print(finalSum)
    return finalSum

        
print(pt2())