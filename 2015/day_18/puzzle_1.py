import re

with open("data.txt") as data:
	lines = data.read().splitlines()

lights = []
for line in lines:
	lights.append([])
	for char in line:
		if char == '#':
			lights[-1].append(1)
		else:
			lights[-1].append(0)

def count_neighbors(lights, x, y):
	count = 0
	for dx in range(-1, 2):
		for dy in range(-1, 2):
			if dx == 0 and dy == 0:
				continue
			if x+dx < 0 or x+dx >= len(lights):
				continue
			if y+dy < 0 or y+dy >= len(lights[0]):
				continue
			count += lights[x+dx][y+dy]
	return count

for i in range(100):
	new_lights = []
	for r in range(len(lights)):
		new_lights.append([])
		for c in range(len(lights[0])):
			n = count_neighbors(lights, r, c)
			new_lights[-1].append(1 if (lights[r][c] == 1 and n in [2, 3]) or (lights[r][c] == 0 and n == 3) else 0)
	lights = new_lights
print(sum([sum(x) for x in lights]))