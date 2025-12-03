def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

raw_data = read_file("data")
data = []
for line in raw_data:
    row = []
    for char in line:
        row.append(int(char))
    data.append(row)

def find_max_index(arr):
    max = 0
    max_index = -1
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
            max_index = i
    return max, max_index

sum = 0
for line in data:
    first_max, i = find_max_index(line)
    a, a_i = find_max_index(line[:i])
    b, b_i = find_max_index(line[i+1:])
    if a == 0:
        max_joltage = int(str(first_max)+str(b))
    elif b == 0:
        max_joltage = int(str(a)+str(first_max))
    else:
        max_joltage = max(int(str(a)+str(first_max)), int(str(first_max)+str(b)))
    sum += max_joltage

print(sum)

def get_first_max(arr):
    if not arr:
        return None, None
    
    max_value = arr[0]
    max_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i
    
    return max_value, max_index

sum = 0
target_length = 12

for line in data:
    l = 0
    num = []
    
    while len(num) < target_length:
        remaining_needed = target_length - len(num)
        r = len(line) - remaining_needed
        
        first_max, i = get_first_max(line[l:r+1])
        num.append(str(first_max))

        l = l + i + 1
    
    result = int(''.join(num))
    sum += result
    
print(sum)