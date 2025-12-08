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

n = len(data)

distances = []

for i in range(n):
    for j in range(i+1, n):
        x1,y1,z1 = data[i]
        x2,y2,z2 = data[j]
        dist = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
        distances.append((dist, i, j))

distances.sort(key=lambda x:x[0])

circuits = {}

for i in range(n):
    circuits[i] = set([i])

connections = 0
num_of_circuits = len(circuits)

while connections < 1000:
    _, p1, p2 = distances[connections]
    if p1 not in circuits[p2] and p2 not in circuits[p1]:
        new_circuit = circuits[p1].union(circuits[p2])
        for p in new_circuit:
            circuits[p] = new_circuit
        num_of_circuits -= 1
    connections += 1

a = set()
b = []

for circuit in circuits.values():
    if id(circuit) not in a:
        a.add(id(circuit))
        b.append(len(circuit))

b.sort(key=lambda x: -x)

print(b[0]*b[1]*b[2])

while True:
    _, p1, p2 = distances[connections]
    if p1 not in circuits[p2] and p2 not in circuits[p1]:
        new_circuit = circuits[p1].union(circuits[p2])
        for p in new_circuit:
            circuits[p] = new_circuit
        num_of_circuits -= 1
        if num_of_circuits == 1:
            print(data[p1][0]*data[p2][0])
            break
    connections += 1