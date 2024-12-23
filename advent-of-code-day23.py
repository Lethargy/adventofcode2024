with open('day23input.txt', 'r') as file:
    data = file.read().splitlines()
    
# build graph

graph = dict()

for line in data:
    a, b = line.split('-')
    
    if a in graph:
        graph[a].add(b)
    else:
        graph[a] = {b}
        
    if b in graph:
        graph[b].add(a)
    else:
        graph[b] = {a}
        
# part 1
cycles = set()

for node1 in graph:
    if node1[0] != 't':
        continue
        
    for node2 in graph[node1]:
        I = graph[node2].intersection(graph[node1])
        
        if not I:
            continue
            
        for node3 in I:
            cycle = frozenset([node1,node2,node3]) # we can't have sets of sets
            cycles.add(cycle)
                
print(len(cycles))


# part 2

# Bron Kerbosch algorithm
R = set()
X = set()
P = set(graph.keys())
ans = set()

stack = [(R,P,X)]

while stack:
    r,p,x = stack.pop()
    
    if len(p) == 0 and len(x) == 0:
        if len(r) > len(ans):
            ans = r
        continue
        
    for v in p:
        N = graph[v]
        stack.append((r | {v}, p.intersection(N), x.intersection(N)))
        p = p - {v}
        x = x | {v}
        
print(','.join(sorted(ans)))