with open('day5input.txt', 'r') as file:
    data = [line.rstrip() for line in file]
    
# part a
import re

rules = dict()

for rule in data[:data.index('')]:
    a,b = re.findall(r'\d+', rule)
    if a in rules:
        rules[a].add(b)
    else:
        rules[a] = {b}

updates = [line.split(',') for line in data[data.index('')+1:]]

def isCorrect(update):
    for i,n in enumerate(update):
        if i > 0 and n in rules:
            if any(m in rules[n] for m in update[:i]):
                return False
            
    return True

ans = 0

for update in updates:
    if isCorrect(update):
        mid = len(update) // 2
        ans = ans + int(update[mid])

print(ans)

# part 2
from functools import cmp_to_key

def compare(a,b):
    if a in rules and b in rules[a]:
        return -1

    if b in rules and a in rules[b]:
        return 1

    return 0

ans2 = 0

for update in updates:
    if not isCorrect(update):
        mid = len(update) // 2
        correct_updated = sorted(update, key = cmp_to_key(compare))
        ans2 = ans2 + int(correct_updated[mid])
        
print(ans2)