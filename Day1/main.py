def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

data = read_file("data")
dial = 50
land_on_zero = 0
passed_zero_once = 0

for turn in data:
    clicks_to_turn = int(turn[1:])
    direction = 1
    if turn[0] == "L":
        direction *= -1
    
    flag = False
    for _ in range(abs(clicks_to_turn)):
        dial += direction
        dial = dial%100
        if dial == 0:
            passed_zero_once += 1
            flag = True

        
    if dial == 0:
        land_on_zero += 1
    
    

# part 1
print(land_on_zero)

# part 2
print(passed_zero_once)
