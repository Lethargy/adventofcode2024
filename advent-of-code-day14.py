with open('day14input.txt', 'r') as file:
    input = file.read().splitlines()

H = 103
W = 101
L = len(input)

# part 1
import re

X = []; Y = []; dX = []; dY = []

for line in input:
    x,y,dx,dy = re.findall(r'-?\d+', line)
    X.append(int(x))
    Y.append(int(y))
    dX.append(int(dx))
    dY.append(int(dy))

for _ in range(100):
    for i in range(L):
        X[i] = (X[i] + dX[i]) % W
        Y[i] = (Y[i] + dY[i]) % H

mx = W // 2
my = H // 2

ne = nw = sw = se = 0
for i in range(L):
    if X[i] < mx and Y[i] < my:
        nw = nw + 1
    if X[i] < mx and Y[i] > my:
        sw = sw + 1
    if X[i] > mx and Y[i] < my:
        ne = ne + 1
    if X[i] > mx and Y[i] > my:
        se = se + 1

print(ne * nw * sw * se)

# part 2
X = []; Y = []; dX = []; dY = []

for line in input:
    x,y,dx,dy = re.findall(r'-?\d+', line)
    X.append(int(x))
    Y.append(int(y))
    dX.append(int(dx))
    dY.append(int(dy))

def biggestCluster(coordinates):
    out = 0
    
    while coordinates:
        nPoints = 0 # number of points in current cluster
        stack = [coordinates.pop()]
        
        while stack:
            x,y = stack.pop()
            nPoints = nPoints + 1

            for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if (nx,ny) in coordinates:
                    stack.append((nx,ny))
                    coordinates.remove((nx,ny))
        
        out = max(out,nPoints)
    return out

C = {(x,y) for x,y in zip(X,Y)}
iteration = 0

while biggestCluster(C) < 100:
    for i in range(L):
        X[i] = (X[i] + dX[i]) % W
        Y[i] = (Y[i] + dY[i]) % H

    C = {(x,y) for x,y in zip(X,Y)}
    iteration = iteration + 1

print(iteration)