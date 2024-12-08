with open('day07input.txt', 'r') as file:
    data = [line.rstrip() for line in file]
    
import re

input = [[int(x) for x in re.findall(r'\d+',line)] for line in data]

# part 1

def recursive_backtrack(n,i,line):
    if i == len(line) - 1:
        if n == line[0]:
            return True
        else:
            return False

    if n > line[0]:
        return False

    mul = recursive_backtrack(n * line[i+1], i+1, line)
    add = recursive_backtrack(n + line[i+1], i+1, line)
    
    return mul or add

def couldBeTrue(line):
    return recursive_backtrack(line[1], 1, line)

print(sum(line[0] for line in input if couldBeTrue(line)))

# part 2

def recursive_backtrack2(n,i,line):
    if i == len(line) - 1:
        if n == line[0]:
            return True
        else:
            return False

    if n > line[0]:
        return False

    mul = recursive_backtrack2(n * line[i+1], i+1, line)
    add = recursive_backtrack2(n + line[i+1], i+1, line)
    con = recursive_backtrack2(int(str(n) + str(line[i+1])), i+1, line)
    return mul or add or con

def couldBeTrue2(line):
    return recursive_backtrack2(line[1], 1, line)

print(sum(line[0] for line in input if couldBeTrue2(line)))
