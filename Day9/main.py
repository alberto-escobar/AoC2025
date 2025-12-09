from shapely import Polygon
import itertools

def load_file(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()
raw_data = load_file('data')

data = []

for row in raw_data:
    a, b = row.split(',')
    data.append([int(a), int(b)])

n = len(data)

polygon = Polygon(data)
max_area = 0
max_area_within = 0

for p1, p2 in itertools.combinations(data, 2):
    x1, y1 = p1
    x2, y2 = p2
    area = (abs(x1-x2)+1)*(abs(y1-y2)+1)
    max_area = max(max_area, area)

    polygon2 = Polygon([[x1, y1], [x2, y1], [x2, y2], [x1, y2]])
    if polygon.contains(polygon2):
        max_area_within = max(max_area_within, area)


print(max_area)
print(max_area_within)

# thanks u/Background_Nail698/ for the idea to use shapely