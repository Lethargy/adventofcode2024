list1 = []
list2 = []

with open('day01input.txt', 'r') as f:
    for line in f:
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))
        
# part 1
list1.sort()
list2.sort()

print(sum(abs(n-m) for (n,m) in zip(list1,list2)))

# part 2
from collections import Counter
count2 = Counter(list2)

print(sum(n * count2[n] for n in list1 if n in count2))
