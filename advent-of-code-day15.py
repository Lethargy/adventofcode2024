with open('day15input.txt', 'r') as file:
    input = file.read().splitlines()
    
def nextPos(coordinates,d):
    i,j = coordinates
    if d == '^':
        return (i-1,j)
    if d == '>':
        return (i,j+1)
    if d == '<':
        return (i,j-1)
    if d == 'v':
        return (i+1,j)
    
def findRobot(room):
    N = len(room)
    M = len(room[0])
    for i in range(N):
        for j in range(M):
            if room[i][j] == '@':
                return i,j
            
# part 1
N = input.index('') # dimensions of room
M = len(input[0])

room = [list(line) for line in input[:N]] # create room
movements = ''.join(input[N:])
curr = findRobot(room)

for d in movements:
    stack = [(curr,nextPos(curr,d))]
    while stack:
        (ci,cj),(ni,nj) = stack[-1]
        if room[ni][nj] == '#':
            break
        elif room[ni][nj] == 'O':
            stack.append(((ni,nj), nextPos((ni,nj),d)))
        else:
            stack.pop()
            room[ci][cj], room[ni][nj] = room[ni][nj], room[ci][cj]
            if not stack:
                curr = (ni,nj)

print(sum(100*i+j for i in range(N) for j in range(M) if room[i][j] == 'O'))

# part 2

from collections import deque

# dimensions of room
N = input.index('')
M = 2 * len(input[0])

# create room
room = [[] for _ in range(N)]

for i in range(N):
    for j in range(len(input[0])):
        if input[i][j] == '#':
            room[i].extend(('#','#'))
        elif input[i][j] == '.':
            room[i].extend(('.','.'))
        elif input[i][j] == 'O':
            room[i].extend(('[',']'))
        elif input[i][j] == '@':
            room[i].extend(('@','.'))

movements = ''.join(input[N:])
curr = findRobot(room)

for d in movements:
    if d == '<' or d == '>': # similar to part 1
        stack = [(curr,nextPos(curr,d))]
        while stack:
            (ci,cj),(ni,nj) = stack[-1]
            if room[ni][nj] == '#':
                break
            elif room[ni][nj] == '[' or room[ni][nj] == ']':
                stack.append(((ni,nj), nextPos((ni,nj),d)))
            else:
                stack.pop()
                room[ci][cj], room[ni][nj] = room[ni][nj], room[ci][cj]
                if not stack:
                    curr = (ni,nj)
                    
    if d == '^' or d == 'v': # more complicated; need queue and stack
        queue = deque([(curr,nextPos(curr,d))])
        stack = []
        
        while queue:
            (ci,cj),(ni,nj) = queue.popleft()
            if ((ci,cj), (ni,nj)) not in stack:
                stack.append(((ci,cj), (ni,nj)))
                
            if room[ni][nj] == '#':
                stack = []
                break
            elif room[ni][nj] == '[':
                queue.append(((ni,nj), nextPos((ni,nj),d)))
                shiftRight = ((ni,nj+1), nextPos((ni,nj+1),d))
                if shiftRight not in queue:
                    queue.append(shiftRight)
            elif room[ni][nj] == ']':
                queue.append(((ni,nj), nextPos((ni,nj),d)))
                shiftLeft = ((ni,nj-1), nextPos((ni,nj-1),d))
                if shiftLeft not in queue:
                    queue.append(shiftLeft)
        
        while stack:
            (ci,cj),(ni,nj) = stack.pop()
            room[ci][cj], room[ni][nj] = room[ni][nj], room[ci][cj]
            if not stack:
                curr = (ni,nj)

print(sum(100*min(i,M-2-i)+j for i in range(N) for j in range(M) if room[i][j] == '['))
