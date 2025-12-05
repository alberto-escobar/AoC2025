def load_file(filename):
    with open(filename, 'r') as f:
        return f.read()
data = load_file("data")
data = data.split("\n\n")
intervals = data[0].split("\n")
ids = data[1].split("\n")

for i in range(len(intervals)):
    a, b = intervals[i].split("-")
    intervals[i] = [int(a), int(b)]

for i in range(len(ids)):
    ids[i] = int(ids[i])

count = 0
for id in ids:
    for start, end in intervals:
        if id >= start and id <= end:
            count += 1
            break
print(count)

intervals.sort()
merged = [intervals[0]]
for start, end in intervals:
    if merged[-1][1] >= start:
        merged[-1][1] = max(merged[-1][1], end) 
    else:
        merged.append([start, end])

count = 0
for interval in merged:
    count += interval[1] - interval[0] + 1

print(count)