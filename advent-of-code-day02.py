with open('day02input.txt', 'r') as f:
    reports = [[int(x) for x in line.split()] for line in f]
        
# problem 1
def isSafe(report: list[int]) -> bool:
    if report[0] <= report[-1]:
        return all(1 <= report[i+1] - report[i] <= 3 
                       for i in range(len(report)-1))
    else:
        return isSafe(report[::-1])
        
print(sum(isSafe(report) for report in reports))

# problem 2
def canBeSafe(report: list[int]) -> bool:
    for i in range(len(report)):
        if isSafe(report[:i] + report[i+1:]):
            return True

    return False

print(sum(isSafe(report) or canBeSafe(report) for report in reports))
