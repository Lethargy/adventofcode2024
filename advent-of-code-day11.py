with open('day11input.txt', 'r') as file:
    line = next(file)
    initArr = [int(n) for n in line.split()]
    
from math import log10

def stoneCount(initArr: list[int], blinks: int) -> int:
    counts = {n: initArr.count(n) for n in initArr} # {number: count}
    newCounts = {}
    
    for _ in range(blinks):
        for n,c in counts.items():
            if n == 0:
                newStones = [1]
            elif int(log10(n))  % 2 == 1: # even digits
                p = (int(log10(n)) + 1) // 2
                newStones = [n // 10**p, n % 10**p]
            else:
                newStones = [2024 * n]
    
            for k in newStones:
                if k in newCounts:
                    newCounts[k] = newCounts[k] + c
                else:
                    newCounts[k] = c
        
        counts = newCounts
        newCounts = {}
    
    return sum(counts.values())

print(stoneCount(initArr,25))

print(stoneCount(initArr,75))
