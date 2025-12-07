def load_file(filename):
    with open(filename, 'r') as f:
        data = f.read().split("\n")
        for i in range(len(data)):
            data[i] = list(data[i])
        return data
    
data = load_file('data')
start = -1
for i in range(len(data[0])):
    if data[0][i] == "S":
        start = i
        break

beams = set([start])
count = 0
for j in range(len(data)):
    for i in list(beams):
        if data[j][i] == "^":
            count += 1
            beams.remove(i)
            if i-1 > -1:
                beams.add(i-1)
                data[j][i-1] = "|"
            if i+1 < len(data[0]):
                beams.add(i+1)
                data[j][i+1] = "|"
        else:
            data[j][i] = "|"
        
print(count)
data[0][start] = 1

for j in range(1, len(data)):
    for i in range(len(data[j])):
        a = 0
        if data[j][i] == "|":
            if type(data[j-1][i]) == int:
                a += data[j-1][i]
            if i > 0 and data[j][i-1] == "^" and type(data[j-1][i-1]) == int:
                a += data[j-1][i-1]
            if i < len(data[0])-1 and data[j][i+1] == "^" and type(data[j-1][i+1]) == int:
                a += data[j-1][i+1]
            data[j][i] = a

paths = 0
for a in data[-1]:
    if type(a) == int:
        paths += a
print(paths)
