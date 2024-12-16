with open('day03input.txt', 'r') as file:
    string = file.read()
        
# part 1
import re

def sum_mul(s):
    ans = 0
    for a in re.findall(r'mul\(\d+,\d+\)', s):
        n, m = re.findall(r'\d+', a)
        ans = ans + int(n) * int(m)
    
    return ans

print(sum_mul(string))

# part 2
temp = 'do()' + string + 'don\'t()'
ans = 0

while 'do()' in temp:
    i = temp.find('do()')
    j = temp.find('don\'t()')
    ans = ans + sum_mul(temp[i:j])
    temp = temp[j+7:]

print(ans)
