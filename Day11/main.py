from collections import deque
from functools import cache

def load_file(filepath):
    with open(filepath, 'r') as f:
        return f.read().splitlines()

graph = {}
raw_data = load_file('data')
for row in raw_data:
    node, edges = row.split(': ')
    edges = edges.split()
    graph[node] = edges

paths = 0
queue = deque(['you'])
while queue:
    node = queue.popleft()
    
    if node == 'out':
        paths += 1

    else:
        for a in graph[node]:
            queue.append((a))

print(paths)

#ol' reliable
@cache
def dfs(node, dac, fft):
    if node == "out":
        return dac and fft
    dac = (node == "dac") or dac
    fft = (node == "fft") or fft
    s = []
    for n in graph[node]:
        s.append(dfs(n, dac, fft))
    return sum(s)

print(dfs('svr', False, False))