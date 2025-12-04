def load_file(filename):
    with open(filename, 'r') as f:
        matrix = [list(line.strip()) for line in f]
    return matrix

data = load_file("data")
m = len(data)
n = len(data[0])
count = 0

def check_surronding(j, i):
    count = 0
    loc = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]
    def in_bound(y, x):
        return y > -1 and y < m and x > -1 and x < n
    for l in loc:
        y = j+l[0]
        x = i+l[1]
        if not in_bound(y,x):
            continue
        if data[y][x] == "@":
            count +=1
    return count

count = 0
for j in range(m):
    for i in range(n):
        if data[j][i] == ".":
            continue
        if check_surronding(j, i) < 4:
            count += 1

print(count)

count = 0      
while True:
    to_remove = set()

    for j in range(m):
        for i in range(n):
            if data[j][i] == ".":
                continue
            if check_surronding(j, i) < 4:
                to_remove.add((j, i))
    
    for roll in list(to_remove):
        j, i = roll
        data[j][i] = "."
        count += 1

    if len(to_remove) == 0:
        break
print(count)