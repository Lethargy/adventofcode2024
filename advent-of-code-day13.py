with open('day13input.txt', 'r') as file:
    input = [line.rstrip() for line in file]
    
# part 1
import re

N = (len(input) + 1) // 4
ans = 0

for i in range(N):
    a,c = re.findall(r'\d+', input[4*i])
    a,c = int(a), int(c)
    b,d = re.findall(r'\d+', input[4*i+1])
    b,d = int(b), int(d)
    e,f = re.findall(r'\d+', input[4*i+2])
    e,f = int(e), int(f)

    det = a*d-b*c
    x = (e*d - b*f) // det if (e*d - b*f) % det == 0 else None
    y = (a*f - c*e) // det if (a*f - c*e) % det == 0 else None

    if x and y:
        ans = ans + 3 * x + y

print(ans)

# part 2

ans2 = 0

for i in range(N):
    a,c = re.findall(r'\d+', input[4*i])
    a,c = int(a), int(c)
    b,d = re.findall(r'\d+', input[4*i+1])
    b,d = int(b), int(d)
    e,f = re.findall(r'\d+', input[4*i+2])
    e,f = 10**13 + int(e), 10**13 + int(f)

    det = a*d-b*c
    x = (e*d - b*f) // det if (e*d - b*f) % det == 0 else None
    y = (a*f - c*e) // det if (a*f - c*e) % det == 0 else None

    if x and y:
        ans2 = ans2 + 3 * x + y

print(ans2)