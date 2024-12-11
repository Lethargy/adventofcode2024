# import data

grid = []
with open('day04input.txt', 'r') as file:
    for line in file:
        grid.append(line.rstrip())
        
# part 1

def match(i: int, j: int, k: int, d: str) -> None:
    if i < 0 or j < 0 or i == n or j == n:
        return None

    if grid[i][j] != word[k]:
        return None
        
    if k == len(word) - 1:
        global ans
        ans = ans + 1
        return None

    i1 = i
    j1 = j
    if 'n' in d:
        i1 = i1 - 1
    if 's' in d:
        i1 = i1 + 1
    if 'e' in d:
        j1 = j1 + 1
    if 'w' in d:
        j1 = j1 - 1

    match(i1,j1,k+1,d)
    
    
n = len(grid[0])
m = len(grid)

directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
word = 'XMAS'
ans = 0

for i,row in enumerate(grid):
    for j,ch in enumerate(row):
        if ch == 'X':
            for d in directions:
                match(i,j,0,d)

print(ans)

# part 2

ans2 = 0

for i in range(1,n-1):
    for j in range(1,m-1):
        if grid[i][j] == 'A':
            ul = grid[i-1][j-1]
            ur = grid[i-1][j+1]
            ll = grid[i+1][j-1]
            lr = grid[i+1][j+1]

            if {ul,lr} == {'M','S'} and {ur,ll} == {'M','S'}:
                ans2 = ans2 + 1

print(ans2)
