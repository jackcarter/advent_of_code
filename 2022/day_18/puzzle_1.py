import time
start_time = time.perf_counter()

with open("data.txt") as data:
	lines = data.read().splitlines()

def adjacent_cubes(cube):
	x, y, z = cube
	return [(x + dx, y + dy, z + dz) for dx in (-1, 0, 1) for dy in (-1, 0, 1) for dz in (-1, 0, 1) if abs(dx) + abs(dy) + abs(dz) == 1]

cubes = {}

for line in lines:
	cube = tuple(int(x) for x in line.split(','))
	cubes[cube] = 6
	for adj in adjacent_cubes(cube):
		if adj in cubes:
			cubes[adj] -= 1
			cubes[cube] -= 1

print(sum(cubes.values()))

