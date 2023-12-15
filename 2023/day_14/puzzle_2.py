from functools import cache
with open("./data.txt") as data:
	lines = data.read().splitlines()

grid = []
for line in lines:
		grid.append([c for c in line])

def calculate_load(grid):
	load = 0
	for ii, row in enumerate(grid):
		row_multiplier = len(grid) - ii
		for cell in row:
			if cell == "O":
				load += row_multiplier
	return load

def roll(grid, direction):
	#convert grid to list of lists
	grid = [list(row) for row in grid]
	# for each cell, check if it's 'O'
	# if it is, move it in "direction" as far as possible (until it hits another O or a #)
	# direction is one of ["north", "south", "east", "west"]
	if direction == "north":
		for ii, row in enumerate(grid):
			for jj, cell in enumerate(row):
				if cell == "O":
					for kk in range(ii, 0, -1):
						if grid[kk-1][jj] in ['#', 'O']:
							break
						grid[kk-1][jj] = "O"
						grid[kk][jj] = "."
	elif direction == "south":
		for ii, row in reversed(list(enumerate(grid))):
			for jj, cell in enumerate(row):
				if cell == "O":
					for kk in range(ii, len(grid)-1):
						if grid[kk+1][jj] in ['#', 'O']:
							break
						grid[kk+1][jj] = "O"
						grid[kk][jj] = "."
	elif direction == "west":
		for ii in range(len(grid[0])):
			for jj in range(len(grid)):
				if grid[jj][ii] == "O":
					for kk in range(ii, 0, -1):
						if grid[jj][kk-1] in ['#', 'O']:
							break
						grid[jj][kk-1] = "O"
						grid[jj][kk] = "."
	elif direction == "east":
		for ii in reversed(range(len(grid[0]))):
			for jj in range(len(grid)):
				if grid[jj][ii] == "O":
					for kk in range(ii, len(grid[jj])-1):
						if grid[jj][kk+1] in ['#', 'O']:
							break
						grid[jj][kk+1] = "O"
						grid[jj][kk] = "."
	grid = tuple(tuple(row) for row in grid)
	return grid

@cache
def cycle(grid):
	grid = roll(grid, "north")
	grid = roll(grid, "west")
	grid = roll(grid, "south")
	grid = roll(grid, "east")
	return grid

grid = tuple(tuple(row) for row in grid)
past_grids = []
past_grids.append(grid)
for _ in range(1000000000):
	grid = cycle(grid)
	if grid in past_grids:
		last_match = past_grids.index(grid) 
		cycle_length = _ - last_match - 1
		adder = (1000000000-last_match) % cycle_length
		index = adder + last_match
		print(calculate_load(past_grids[index]))
		exit(0)
	past_grids.append(grid)