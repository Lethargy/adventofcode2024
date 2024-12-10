data = ''
with open('day09input.txt', 'r') as file:
    for line in file:
        data = data + line
        
# part 1
# credit to Riley Thomp (https://github.com/rileythomp/adventofcode/blob/master/2024/9/main.py)

from collections import deque

disk = []; fileIndices = deque([]); freeIndices = deque([]); s = 0
for i,c in enumerate(data):
    if i % 2 == 0:
        disk.extend(i//2 for _ in range(int(c)))
        fileIndices.extend(j for j in range(s,s+int(c)))
    else:
        disk.extend(None for _ in range(int(c)))
        freeIndices.extend(j for j in range(s,s+int(c)))
    s = s + int(c)

while freeIndices[0] < fileIndices[-1]:
    i = freeIndices.popleft()
    j = fileIndices.pop()
    disk[i], disk[j] = disk[j], disk[i]

print(sum(i * d for i,d in enumerate(disk) if d is not None))

# part 2

s = 0; blocks = []; gaps = []

for i,c in enumerate(data):
    if i % 2 == 0:
        blocks.append([s,int(c)])
    else:
        gaps.append([s,int(c)])
    s = s + int(c)
    
for i in reversed(range(len(blocks))):
    b = blocks[i]
    for j,g in enumerate(gaps):
        if g[1] >= b[1] and g[0] < b[0]:
            blocks[i], gaps[j] = [g[0], b[1]], [g[0]+b[1], g[-1]-b[1]]
            break

ans = 0
for i,(s,l) in enumerate(blocks):
    for k in range(s,s+l):
        ans = ans + k * i

print(ans)
