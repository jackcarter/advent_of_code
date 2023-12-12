import itertools
with open("./data.txt") as data:
	lines = data.read().splitlines()

grid = [[c for c in line] for line in lines]

def expand_grid(grid):
	for ii, row in enumerate(grid):
		if all([c == '.' for c in row]):
			#replace all '.' with ' ' in this row
			grid[ii] = [' ']*len(row)
	#find all columns that are all '.'
	for ii, col in enumerate(zip(*grid)):
		if all([c in ['.',' '] for c in col]):
			#replace all '.' with ' ' in this column
			for jj, row in enumerate(grid):
				grid[jj][ii] = ' '
	return grid

def find_galaxies(grid):
	galaxies = []
	for ii, jj in itertools.product(range(len(grid)), range(len(grid[0]))):
		if grid[ii][jj] == '#':
			galaxies.append((ii,jj))
	return galaxies

def shortest_path(galaxy1, galaxy2, grid):
	crossed_characters = []
	for ii in range(min(galaxy1[0], galaxy2[0])+1, max(galaxy1[0], galaxy2[0])+1):
		crossed_characters.append(grid[ii][galaxy1[1]])
	for jj in range(min(galaxy1[1], galaxy2[1])+1, max(galaxy1[1], galaxy2[1])+1):
		crossed_characters.append(grid[galaxy2[0]][jj])
	distance = 0
	for c in crossed_characters:
		if c != ' ':
			distance += 1
		else:
			distance += 10**6
	return distance

grid = expand_grid(grid)

galaxies = find_galaxies(grid)

paths = {}
for galaxy1, galaxy2 in itertools.combinations(galaxies, 2):
	paths[(galaxy1, galaxy2)] = shortest_path(galaxy1, galaxy2,grid)
print(sum(paths.values()))
