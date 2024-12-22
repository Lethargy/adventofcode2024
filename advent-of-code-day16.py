with open('day16input.txt', 'r') as file:
    room = file.read().splitlines()
    
# part 1
N = len(room)
M = len(room[0])
scores = {}

for i in range(N):
    for j in range(M):
        if room[i][j] == '#':
            continue
        
        for k in range(4):
            scores[((i,j),k)] = float('inf')
            
        if room[i][j] == 'S':
            S = (i,j)

        if room[i][j] == 'E':
            E = (i,j)
            
scores[(S,0)] = 0

from heapq import heappop, heappush

d = [(0,1),(1,0),(0,-1),(-1,0)] # directions
Q = [(0, S, 0)] # priority queue: score, (i,j), and direction index

while Q:
    s, (i,j), k = heappop(Q)

    for n in range(4):
        r = i + d[n][0]
        c = j + d[n][1]
        
        if ((r,c),n) not in scores:
            continue
        
        if n == k:
            ds = 1
        elif abs(n - k) == 1 or abs(n - k) == 3:
            ds = 1001
        
        if s + ds <= scores[((r,c),n)]:
            scores[((r,c),n)] = s + ds
            heappush(Q, (s + ds,(r,c),n))
        
print(min(scores[(E,k)] for k in range(4)))

# part 2

m = min(scores[(E,k)] for k in range(4)) # answer from part 1
Q = [(0, S, {S}, 0)] # priority queue: score, (i,j), path, and direction index
squares = set()

while Q:
    s, (i,j), p, k = heappop(Q) # score, (i,j), and direction index
    
    if (i,j) == E and s == m:
        squares.update(p)
        continue
    
    for n in range(4):
        r = i + d[n][0]
        c = j + d[n][1]
        
        if ((r,c),n) not in scores:
            continue
        
        if n == k:
            ds = 1
        elif abs(n - k) == 1 or abs(n - k) == 3:
            ds = 1001
        
        if s + ds <= scores[((r,c),n)]:
            scores[((r,c),n)] = s + ds
            heappush(Q, (s + ds,(r,c),p|{(r,c)},n))
        
print(len(squares))
