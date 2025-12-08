def load_file(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

raw_data = load_file('data')
data = []
for row in raw_data:
    a = []
    for num in row.split(','):
        a.append(int(num))
    data.append(a)

distances = []
n = len(data)
for i in range(n):
    for j in range(i+1, n):
        x1,y1,z1 = data[i]
        x2,y2,z2 = data[j]
        dist = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
        distances.append((dist, i, j))

distances.sort(key=lambda x:x[0])


sets = {}
for i in range(n):
    sets[i] = set([i])

connections = 0
curr = 0
g = len(sets)
while connections < 1000: 
    _, p1, p2 = distances[curr]
    if p1 not in sets[p2] and p2 not in sets[p1]:
        merged = sets[p1] | sets[p2]
        for member in merged:
            sets[member] = merged
        g -= 1
    connections += 1
    curr += 1

unique_sets_list = [set(fs) for fs in set(frozenset(s) for s in sets.values())]
unique_sets_list.sort(key=lambda x: -len(x))

result = len(unique_sets_list[0]) * len(unique_sets_list[1]) * len(unique_sets_list[2])
print(result)

while True: 
    _, p1, p2 = distances[curr]
    if p1 not in sets[p2] and p2 not in sets[p1]:
        merged = sets[p1] | sets[p2]
        for member in merged:
            sets[member] = merged
        g -= 1
        if g == 1:
            x1, _, _ = data[p1]
            x2, _, _ = data[p2]
            print(x1*x2)
            break
    curr += 1