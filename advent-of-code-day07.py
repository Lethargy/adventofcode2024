with open('day07input.txt', 'r') as file:
    data = file.read().splitlines()
    
import re

input = [[int(x) for x in re.findall(r'\d+',line)] for line in data]

# part 1

def couldBeTrue(line: list[int]) -> bool:
    stack = [(line[1],1)]
    
    while stack:
        n,i = stack.pop()

        if i == len(line) - 1:
            if n == line[0]:
                return True
            continue

        if n > line[0]:
            continue

        stack.append((n * line[i+1], i+1))
        stack.append((n + line[i+1], i+1))

    return False

print(sum(line[0] for line in input if couldBeTrue(line)))

# part 2

def couldBeTrue2(line: list[int]) -> bool:
    target = line[0]
    stack = [(line[1],1)]
    
    while stack:
        n,i = stack.pop()

        if i == len(line) - 1:
            if n == target:
                return True
            continue

        if n > target:
            continue

        stack.append((n * line[i+1], i+1))
        stack.append((n + line[i+1], i+1))
        stack.append((int(str(n) + str(line[i+1])), i+1))

    return False

print(sum(line[0] for line in input if couldBeTrue2(line)))
