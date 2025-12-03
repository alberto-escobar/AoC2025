import re


def load_file(filepath):
    with open(filepath, 'r') as f:
        return f.read()

data = load_file("data")
data = data.split(",")

count = 0 
count2 = 0
for line in data:
    start, end = line.split("-")
    start = int(start)
    end = int(end)
    for num in range(start, end+1):
        str_num = str(num)
        match = re.match(r'^(\d+)\1$', str_num)
        if match:
            count += num
        match = re.match(r'^(\d+)\1+$', str_num)
        if match:
            count2 += num


print(count)
print(count2)

