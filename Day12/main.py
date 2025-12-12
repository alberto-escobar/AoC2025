def load_file(filename):
    with open(filename, 'r') as f:
        return f.read().split("\n\n")

raw_data = load_file('data')

shapes = raw_data[0:6]
present_area = []

for row in shapes:
    present_area.append(row.count('#'))

data = raw_data[6].splitlines()

# here we define two strategies for packing:
# packing strategy 1 = we place each present in a 3 x 3 cell in the available space.
# packing strategy 2 = we place presents in a optimized fashion.
#
# For strategy 2 let us not worry about the how, just look at space available vs space needed
# 
# If the counts for both strategies are equal, then we know that each line of the data can be packed 
# via the packing strategy 1 without needed to rely on some optimized packing to fit all the presents

packing_strategy_1_count = 0
packing_strategy_2_count = 0

for row in data:
    a, b = row.split(': ')
    a = a.split('x')
    b = b.split(' ')

    # packing strategy 1 decision
    cells_available = int(a[0])//3*int(a[1])//3
    cells_needed = int(b[0])+int(b[1])+int(b[2])+int(b[3])+int(b[4])+int(b[5])
    if cells_available >= cells_needed:
        packing_strategy_1_count += 1

    # packing strategy 2 decision
    area_available = int(a[0])*int(a[1])
    area_needed = 0 
    for i in range(6):
        area_needed += present_area[i]*int(b[i])
    if area_available >= area_needed:
        packing_strategy_2_count += 1
    

if packing_strategy_1_count == packing_strategy_2_count:
    print(packing_strategy_1_count)
else:
    print("we must venture further into the rabbit hole")