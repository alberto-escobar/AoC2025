from collections import deque

def load_file(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

raw_data = load_file('data')


lights = []
buttons = []
joltage = []

for row in raw_data:
    arr = row.split()
    light = arr[0].strip('[]')
    length = len(light)
    light = light.replace(".", "0")
    light = light.replace("#", "1")
    lights.append(int(light[::-1], 2))

    btns = arr[1:-1]
    a = []
    for btn in btns:
        bits = list("0"*length)
        btn = btn.strip('()').split(',')
        for num in btn:
            bits[int(num)] = '1'
        bits = ''.join(bits)
        a.append(int(bits[::-1], 2))
    buttons.append(a)

def bfs(target, buttons):
    queue = deque()
    for button in buttons:
        queue.append((button, 1))
    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps
        for button in buttons:
            queue.append((current^button, steps+1))

count = 0
for i in range(len(lights)):
    print(f"{i}/{len(lights)}")
    light = lights[i]
    button = buttons[i]
    steps = bfs(light, button)
    count += steps
print(count)

from scipy.optimize import linprog

joltages = []
buttons = []

for row in raw_data:
    arr = row.split()
    joltage = arr[-1].strip('{}').split(",")
    joltages.append([int(s) for s in joltage])

    btns = arr[1:-1]
    a = []
    for btn in btns:
        btn = btn.strip('()').split(',')
        a.append([int(s) for s in btn])
    buttons.append(a)

count = 0
for i in range(len(joltages)):
    print(f"{i}/{len(joltages)}")
    joltage = joltages[i]
    button = buttons[i]
    costs = [1]*len(button)
    A = [[(i in b) for b in button] for i in range(len(joltage))] 
    count += linprog(costs, A_eq=A, b_eq=joltage, integrality=1).fun
print(count)

# thanks u/4HbQ for introducing linear programming to me
