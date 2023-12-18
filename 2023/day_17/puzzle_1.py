from math import inf
with open("./data.txt") as data:
	lines = data.read().splitlines()

grid = []
for line in lines:
	grid.append([c for c in line])

def print_grid(grid):
	for r in range(len(grid)):
		print(''.join(grid[r]))

def next_dir(direction):
	if direction in [(1,0), (-1,0)]:
		return [(0,1), (0,-1)]
	elif direction in [(0,1), (0,-1)]:
		return [(1,0), (-1,0)]
	else:
		return [(1,0), (-1,0), (0,1), (0,-1)]

	return [c for c in candidates if c[0] >= 0 and c[0] < len(grid) and c[1] >= 0 and c[1] < len(grid[0])]

def reconstruct_path(came_from, coords, direction):
	print(came_from)
	print(coords, direction)
	current = (coords, direction)
	total_path = [current]
	i = 0
	while current in came_from:
		i += 1
		print(i, current)
		#input("next...")
		current = came_from[current]
		total_path.append(current)
	return total_path

def print_path(grid, path):
	path = list(reversed(path[:-1]))
	printgrid = []
	for r in range(len(grid)):
		printgrid.append(['.' for c in range(len(grid[r]))])
	for ii, pathnode in enumerate(path):
		if ii == 0:
			printgrid[pathnode[0]][pathnode[1]] = '.'
		else:
			if path[ii - 1][0] > pathnode[0]:
				printgrid[pathnode[0]][pathnode[1]] = '↑'
			elif path[ii - 1][0] < pathnode[0]:
				printgrid[pathnode[0]][pathnode[1]] = '↓'
			elif path[ii - 1][1] > pathnode[1]:
				printgrid[pathnode[0]][pathnode[1]] = '←'
			elif path[ii - 1][1] < pathnode[1]:
				printgrid[pathnode[0]][pathnode[1]] = '→'
	for r in range(len(printgrid)):
		print(''.join(printgrid[r]))

def calculate_g(grid, state):
	r, c, direction = state
	return int(grid[r][c])

def breadth_first_search(grid, start, goal):
	startstate = (start[0], start[1], "down")
	frontier = set()
	came_from = {}
	visited = set()
	heat_map = {(0,0): 0}
	for new_dir in [(1,0), (-1,0), (0,1), (0,-1)]:
		frontier.add((start, new_dir, 0))
		came_from[(start, new_dir)] = None
	i = 0
	while len(frontier) > 0:
		i += 1
		print(i, len(heat_map), len(frontier))
		coords, direction, heat = min(frontier, key=lambda x: x[2] + abs(x[0][0] - goal[0]) + abs(x[0][1] - goal[1]))
		frontier.remove((coords, direction, heat))
		if coords[0] == goal[0] and coords[1] == goal[1]:
			break
		new_dirs = next_dir(direction)
		for new_dir in new_dirs:
			new_heat = heat
			previous_coord = coords
			previous_dir = direction
			for steps in range(1, 4):
				new_coord = (coords[0] + steps * new_dir[0], coords[1] + steps * new_dir[1])
				if new_coord[0] < 0 or new_coord[1] < 0 \
					or new_coord[0] >= len(grid) or new_coord[1] >= len(grid[0]):
					continue
				new_heat = new_heat + int(grid[new_coord[0]][new_coord[1]])
				if heat_map.get((new_coord, new_dir), inf) <= new_heat: 
					continue
				heat_map[(new_coord, new_dir)] = new_heat
				came_from[(new_coord, new_dir)] = previous_coord, previous_dir
				frontier.add((new_coord, new_dir, new_heat))
				previous_coord = new_coord
				previous_dir = new_dir
	return heat

print(breadth_first_search(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1)))