with open('day16input.txt', 'r') as file:
    room = file.read().splitlines()
    
# initialize    

N = len(room)
M = len(room[0])
scores = dict()
previous = dict()

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

# Dijkstra

from heapq import heappop, heappush

d = [(0,1),(1,0),(0,-1),(-1,0)] # directions
Q = [(0, S, 0)] # priority queue

while Q:
    s, (i,j), k = heappop(Q) # score, (i,j), and direction index
    
    for n in range(4):
        r = i + d[n][0]
        c = j + d[n][1]
        
        if ((r,c),n) not in scores:
            continue
        
        if n == k:
            ds = 1
        elif abs(n - k) == 1 or abs(n - k) == 3:
            ds = 1001
        else:
            continue
        
        if s + ds < scores[((r,c),n)]:
            scores[((r,c),n)] = s + ds
            previous[((r,c),n)] = {((i,j),k)}
            heappush(Q, (s + ds, (r,c), n))
        elif s + ds == scores[((r,c),n)]:
            scores[((r,c),n)] = s + ds
            previous[((r,c),n)].add(((i,j),k))
            heappush(Q, (s + ds, (r,c), n))
        
# part 1
m = min(scores[(E,k)] for k in range(4))
print(m)

# part 2
queue = [(E,k) for k in range(4) if scores[(E,k)] == m]
squares = set()

while queue:
    square, direction = queue.pop(0)
    squares.add(square)
    
    if (square, direction) == (S,0):
        break
    
    queue.extend(previous[(square, direction)])
    
print(len(squares))
