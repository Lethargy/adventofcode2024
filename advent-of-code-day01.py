# -*- coding: utf-8 -*-

A = []
B = []

with open('day01input.txt', 'r') as f:
    for line in f:
        num1, num2 = line.split()
        A.append(int(num1))
        B.append(int(num2))
        
# part a
A.sort()
B.sort()

print(sum(abs(a-b) for (a,b) in zip(A,B)))

# part b
from collections import Counter

B_count = Counter(B)
ans = 0

for a in A:
    if a in B_count:
        ans = ans + a * B_count[a]

print(ans)
