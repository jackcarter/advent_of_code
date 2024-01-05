import re

with open("data.txt") as data:
	lines = data.read().splitlines()

sensors = []
for line in lines:
	sx, sy, bx, by = [int(i) for i in re.findall(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)[0]]
	distance = abs(bx-sx) + abs(by-sy)
	sensors.append((sx, sy, bx, by, distance))

keyrow = 2000000
impossible_xs = set()

for s in sensors:
	if keyrow + s[4] < s[1] or keyrow - s[4] > s[1]:
		pass
	else:
		impossible_length_on_keyrow = (s[4] - abs(keyrow - s[1]))
		ix = [i for i in range(s[0]-impossible_length_on_keyrow, s[0]+impossible_length_on_keyrow+1)]
		impossible_xs.update(ix)

keyrow_beacon_xs = set(s[2] for s in sensors if int(s[3]) == keyrow)
impossible_xs -= keyrow_beacon_xs
print(len(impossible_xs))