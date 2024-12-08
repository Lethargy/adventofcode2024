# -*- coding: utf-8 -*-

reports = []
with open('day02input.txt', 'r') as f:
    for line in f:
        reports.append([int(x) for x in line.split()])
        
# problem 1
def isSafe(report):
    if report[0] < report[-1]:
        for i in range(len(report)-1):
            if not (1 <= report[i+1] - report[i] <= 3):
                return 0
        return 1
    elif report[0] == report[-1]:
        return 0
    else:
        return isSafe(report[::-1])
    
print(sum(isSafe(report) for report in reports))

# problem 2
unSafeReports = []
for report in reports:
    if not isSafe(report):
        unSafeReports.append(report)
        
def canBeSafe(report):
    for i in range(len(report)):
        if isSafe(report[:i] + report[i+1:]):
            return 1

    return 0

print(sum(isSafe(report) for report in reports)
      + sum(canBeSafe(report) for report in unSafeReports))
