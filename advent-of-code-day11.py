with open('day11input.txt', 'r') as file:
    line = next(file)
    initArr = [int(n) for n in line.split()]
    
from math import log10

def stoneCount(initArr,blinks):
    nums = {n: initArr.count(n) for n in initArr} # {number: count}
    newNums = {}
    
    for _ in range(blinks):
        for n,c in nums.items():
            if n == 0:
                nextNums = [1]
            elif int(log10(n))  % 2 == 1: # even digits
                p = (int(log10(n)) + 1) // 2
                nextNums = [n // 10**p, n % 10**p]
            else:
                nextNums = [2024 * n]
    
            for k in nextNums:
                if k in newNums:
                    newNums[k] = newNums[k] + c
                else:
                    newNums[k] = c
        
        nums = newNums
        newNums = {}
    
    return sum(nums.values())

print(stoneCount(initArr,25))

print(stoneCount(initArr,75))