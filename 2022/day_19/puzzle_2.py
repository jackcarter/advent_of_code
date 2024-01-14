import time
start_time = time.perf_counter()

with open("data.txt") as data:
	lines = data.read().splitlines()

def adjacent_cubes(cube):
	x, y, z = cube
	return [(x + dx, y + dy, z + dz) for dx in (-1, 0, 1) for dy in (-1, 0, 1) for dz in (-1, 0, 1) if abs(dx) + abs(dy) + abs(dz) == 1]

def flood_fill_3d(point):
	visited = set()
	to_visit = set([point])
	while len(to_visit) > 0:
		point = to_visit.pop()
		visited.add(point)
		for adj in adjacent_cubes(point):
			if adj not in visited and adj not in cubes:
				to_visit.add(adj)
				if adj[0] < min_x or adj[0] > max_x or adj[1] < min_y or adj[1] > max_y or adj[2] < min_z or adj[2] > max_z:
					return set()
	return visited

cubes = set()

for line in lines:
	cube = tuple(int(x) for x in line.split(','))
	cubes.add(cube)

min_x = min(cubes, key=lambda c: c[0])[0]
min_y = min(cubes, key=lambda c: c[1])[1]
min_z = min(cubes, key=lambda c: c[2])[2]
max_x = max(cubes, key=lambda c: c[0])[0]
max_y = max(cubes, key=lambda c: c[1])[1]
max_z = max(cubes, key=lambda c: c[2])[2]

for x in range(min_x, max_x + 1):
	for y in range(min_y, max_y + 1):
		for z in range(min_z, max_z + 1):
			if (x, y, z) not in cubes:
				fill_points = flood_fill_3d((x, y, z))
				for point in fill_points:
					cubes.add(point)

cube_counts = {}
for cube in cubes:
	cube_counts[cube] = 6 - sum([1 for adj in adjacent_cubes(cube) if adj in cubes])

print(sum(cube_counts.values()))