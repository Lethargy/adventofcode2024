# import and process

with open('day08input.txt', 'r') as file:
    city = [line.rstrip() for line in file]
    
N = len(city)
M = len(city[0])

d = {}

for i in range(N):
    for j in range(M):
        if city[i][j] == '.':
            continue

        if city[i][j] not in d:
            d[city[i][j]] = {(i,j)}
        else:
            d[city[i][j]].add((i,j))
            
# part 1

antinodes = set()

for k in d:
    for (x0,y0) in d[k]:
        for (x1,y1) in d[k] - {(x0,y0)}:
                
            x2 = x1 + (x1 - x0)
            y2 = y1 + (y1 - y0)

            if 0 <= x2 <= N-1 and 0 <= y2 <= N-1:
                antinodes.add((x2,y2))

print(len(antinodes))

# part 2

antinodes2 = set()

for k in d:
    for (x0,y0) in d[k]:
        for (x1,y1) in d[k] - {(x0,y0)}:
            dx = x1 - x0
            dy = y1 - y0

            x2 = x0; y2 = y0;
            while 0 <= x2 <= N-1 and 0 <= y2 <= N-1:
                antinodes2.add((x2,y2))
                x2 = x2 + dx
                y2 = y2 + dy

print(len(antinodes2))
