import re
import collections

with open("data.txt") as data:
	lines = data.read().splitlines()

sensors = []
for line in lines:
	sx, sy, bx, by = [int(i) for i in re.findall(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)[0]]
	distance = abs(bx-sx) + abs(by-sy)
	sensors.append((sx, sy, bx, by, distance))

search_range = 4000000

def tuning_frequency(x, y):
	return (x * 4000000) + y

def just_outside(sensor):
	perimeter = set()
	sx, sy, bx, by, distance = sensor
	for i in range(distance + 2):
		# mark the perimeter of the sensor + distance + 1
		y = sy - distance - 1 + i
		perimeter.add((sx-i, y))
		perimeter.add((sx+i, y))
		y2 = sy + distance + 1 - i
		perimeter.add((sx-i, y2))
		perimeter.add((sx+i, y2))
	return perimeter


perims = []
for i, s in enumerate(sensors):
	perims.extend([t for t in just_outside(s)])

counts = collections.Counter(perims)
result = [element for element, count in counts.items() if count == 4]
print(tuning_frequency(*result[0]))