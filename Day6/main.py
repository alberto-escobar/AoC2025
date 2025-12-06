def load_file(filename):
    with open(filename, 'r') as f:
        return f.read()

data = load_file('data')
data = data.split("\n")

for i in range(len(data)):
    data[i] = data[i].split()

def op(arr, operation):
    out = 1
    for num in arr:
        if operation == "+":
            out += int(num)
        else:
            out *= int(num)
    if operation == "+":
        out -= 1
    return out
        

m = len(data)
n = len(data[0])
res = 0

for i in range(n):
    arr = []
    for j in range(m-1):
        arr.append(data[j][i])
    res += op(arr, data[m-1][i])

print(res)

data = load_file('data')
data = data.split("\n")

start = 0
length = 1
out = 0
for i in range(1,len(data[-1])):
    if data[-1][i] == " ":
        length += 1
    elif data[-1][i] != " ":
        matrix = []
        for i in range(len(data)-1):
            matrix.append(data[i][start:start+length])

        # thanks the lord for linear algebra
        matrix = [list(row) for row in zip(*matrix)]
        
        arr = []
        for i in range(len(matrix)):
            new = ''.join(matrix[i]).replace(' ', '')
            if new == '':
                continue

            arr.append(int(new))
        
        out += op(arr, data[-1][start])
        start += length
        length = 1

matrix = []
for i in range(len(data)-1):
    matrix.append(data[i][start:])

matrix = [list(row) for row in zip(*matrix)]

arr = []
for i in range(len(matrix)):
    new = ''.join(matrix[i]).replace(' ', '')
    if new == '':
        continue

    arr.append(int(new))

out += op(arr, data[-1][start])
start += length
length = 1

print(out)