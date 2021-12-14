def day1(lines):
    count = 0
    prev = lines[0]
    for line in lines:
        if int(prev) < int(line):
            count += 1
        prev = line
    return count

def day1_pt2(lines):
    new_lines = []
    for i in range(0, len(lines)-2):
        new_lines.append(int(lines[i])+int(lines[i+1])+int(lines[i+2]))
    return day1(new_lines)
    
with open ("numbers.txt", 'r') as f:
    lines = f.readlines()

print(day1(lines))
print(day1_pt2(lines))

