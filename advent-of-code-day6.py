with open('day6input.txt', 'r') as file:
    room = [line.rstrip() for line in file]
    
# part 1

n = len(room)
m = len(room[0])

def next_step(i,j,d):
    if d == '^':
        return i-1,j
    if d == '>':
        return i,j+1
    if d == 'v':
        return i+1,j
    if d == '<':
        return i,j-1

for r,row in enumerate(room):
    if '^' in row:
        i00 = r
        j00 = row.index('^')
        
directions = ['^','>','v','<']

k = 0
d = directions[k % 4]
visited = {(i00,j00)}
i1,j1 = next_step(i00,j00,d)

while (0 <= i1 <= n-1) and (0 <= j1 <= m-1):
    if room[i1][j1] != '#':
        visited.add((i1,j1))
        i0,j0 = i1,j1
    else:
        k = k + 1
        d = directions[k % 4]

    i1,j1 = next_step(i0,j0,d)

print(len(visited))

# part 2

def isLoop(i_obs,j_obs):
    i0 = i00; j0 = j00; d = '^'; k = 0
    visited  = {(i0,j0,d)}
    i1,j1 = next_step(i0,j0,d)
    
    while (0 <= i1 <= n-1) and (0 <= j1 <= n-1):
        if room[i1][j1] == '#' or (i1,j1) == (i_obs,j_obs):
            k = k + 1
            d = directions[k % 4]
        else:
            if (i1,j1,d) in visited:
                return 1

            visited.add((i1,j1,d))
            i0,j0 = i1,j1

        i1,j1 = next_step(i0,j0,d)
        
    return 0

print(sum(isLoop(a,b) for (a,b) in visited - {(i00,j00)}))
