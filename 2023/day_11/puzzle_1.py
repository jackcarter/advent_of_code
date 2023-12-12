import itertools
with open("./data.txt") as data:
	lines = data.read().splitlines()

grid = [[c for c in line] for line in lines]

def expand_grid(grid):
	newrows = []
	for ii, row in enumerate(grid):
		if all([c == '.' for c in row]):
			newrows.append(ii)
	#find all columns that are all '.'
	newcols = []
	for ii, col in enumerate(zip(*grid)):
		if all([c == '.' for c in col]):
			newcols.append(ii)
	
	#double each row in newrows
	for ii in newrows[::-1]:
		grid.insert(ii, ['.']*len(grid[0]))
	#double each col in newcols
	for ii in newcols[::-1]:
		for row in grid:
			row.insert(ii, '.')
	return grid

def find_galaxies(grid):
	galaxies = []
	for ii, jj in itertools.product(range(len(grid)), range(len(grid[0]))):
		if grid[ii][jj] == '#':
			galaxies.append((ii,jj))
	return galaxies

def shortest_path(galaxy1, galaxy2):
	#manhattan distance between two galaxies
	return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

grid = expand_grid(grid)

galaxies = find_galaxies(grid)

#find shortest path through all galaxies
paths = {}
for galaxy1, galaxy2 in itertools.combinations(galaxies, 2):
	paths[(galaxy1, galaxy2)] = shortest_path(galaxy1, galaxy2)
print(sum(paths.values()))