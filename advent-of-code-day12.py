with open('day12input.txt', 'r') as file:
    grid = file.read().splitlines()
    
N = len(grid); M = len(grid[0])

def findRegion(i,j):
    queue = {(i,j)}
    explored = set()

    while queue:
        r,c = queue.pop()
        explored.add((r,c))

        for nr,nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
            if not (0 <= nr <= N-1 and 0 <= nc <= M-1):
                continue

            if grid[nr][nc] != grid[r][c]:
                continue

            if (nr,nc) not in explored and (nr,nc) not in queue:
                queue.add((nr,nc))

    return explored

regions = []
explored = set()

for i in range(N):
    for j in range(M):
        if (i,j) not in explored:
            regions.append(findRegion(i,j))
            explored.update(regions[-1])
            
            
# part 1
def countFences(i,j):
    n = grid[i-1][j] if i>0 else None
    s = grid[i+1][j] if i+1<N else None
    e = grid[i][j+1] if j+1<N else None
    w = grid[i][j-1] if j>0 else None
        
    return sum(grid[i][j] != d for d in [n,s,e,w])

print(sum(sum(countFences(r,c) for r,c in region) * len(region)
          for region in regions))

# part 2
def countVertices(i,j):
    n = grid[i-1][j] if i>0 else None
    s = grid[i+1][j] if i+1<N else None
    e = grid[i][j+1] if j+1<N else None
    w = grid[i][j-1] if j>0 else None
    nw = grid[i-1][j-1] if i>0 and j>0 else None
    ne = grid[i-1][j+1] if i>0 and j+1<N else None
    sw = grid[i+1][j-1] if i+1<N and j>0 else None
    se = grid[i+1][j+1] if i+1<N and j+1<N else None
            
    ans = 0
    if grid[i][j] not in {n,w} or (n == w != nw):
        ans = ans + 1
    if grid[i][j] not in {n,e} or (n == e != ne):
        ans = ans + 1
    if grid[i][j] not in {s,e} or (s == e != se):
        ans = ans + 1
    if grid[i][j] not in {s,w} or (s == w != sw):
        ans = ans + 1

    return ans

print(sum(sum(countVertices(i,j) for (i,j) in region) * len(region)
          for region in regions))
