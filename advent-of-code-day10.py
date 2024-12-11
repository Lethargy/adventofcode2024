with open('day10input.txt', 'r') as file:
    grid = [line.rstrip() for line in file]

N = len(grid)
M = len(grid[0])

# part 1
def score(i,j):
    stack = [[(i,j)]]
    ans = 0
    peaks = []
    
    while stack:
        path = stack.pop()
        r,c = path[-1]

        if grid[r][c] == '9':
            if (r,c) not in peaks:
                ans = ans + 1
                peaks.append((r,c))
            continue

        for (nr,nc) in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
            if not ((0 <= nr <= N-1) and (0 <= nc <= N-1)):
                continue
            if int(grid[nr][nc]) == int(grid[r][c]) + 1:
                stack.append(path + [(nr,nc)])
                
    return ans

print(sum(score(i,j) for i in range(N) for j in range(M) if grid[i][j] == '0'))

# part 2
def rating(i,j):
    stack = [[(i,j)]] # path and height
    ans = 0
    
    while stack:
        path = stack.pop()
        r,c = path[-1]

        if grid[r][c] == '9':
            ans = ans + 1
            continue

        for (nr,nc) in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
            if not ((0 <= nr <= N-1) and (0 <= nc <= N-1)):
                continue
            if int(grid[nr][nc]) == int(grid[r][c]) + 1:
                stack.append(path + [(nr,nc)])
                
    return ans

print(sum(rating(i,j) for i in range(N) for j in range(M) if grid[i][j] == '0'))