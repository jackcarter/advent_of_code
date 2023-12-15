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

def roll_north(grid):
	# for each cell, check if it's 'O'
	# if it is, move it up rows as far as possible (until it hits another O or a #)
	for ii, row in enumerate(grid):
		for jj, cell in enumerate(row):
			if cell == "O":
				for kk in range(ii, 0, -1):
					if grid[kk-1][jj] in ['#', 'O']:
						break
					grid[kk-1][jj] = "O"
					grid[kk][jj] = "."
	return grid

grid = roll_north(grid)
print(calculate_load(grid))