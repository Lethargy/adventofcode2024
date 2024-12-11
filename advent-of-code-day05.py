with open('day05input.txt', 'r') as file:
    data = [line.rstrip() for line in file]
    
# part 1
import re
greaterThan = dict()

for pair in data[:data.index('')]:
    a,b = re.findall(r'\d+', pair)
    if a in greaterThan:
        greaterThan[a].add(b)
    else:
        greaterThan[a] = {b}

updates = [line.split(',') for line in data[data.index('')+1:]]

def isCorrect(update: list[str]) -> bool:
    for i,n in enumerate(update):
        if i > 0 and n in greaterThan:
            if any(m in greaterThan[n] for m in update[:i]):
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

def compare(a: str, b: str) -> int:
    if a in greaterThan and b in greaterThan[a]:
        return -1

    if b in greaterThan and a in greaterThan[b]:
        return 1

    return 0

ans2 = 0
for update in updates:
    if not isCorrect(update):
        mid = len(update) // 2
        correct_updated = sorted(update, key = cmp_to_key(compare))
        ans2 = ans2 + int(correct_updated[mid])
        
print(ans2)
