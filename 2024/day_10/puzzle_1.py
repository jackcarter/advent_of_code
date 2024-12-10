import math

with open("./data.txt") as data:
	lines = data.read().splitlines()

grid = []

for line in lines:
	grid.append(list([int(c) for c in line]))

def all_neighbors(i, j):
	directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	neighbors = []
	for direction in directions:
		ni = i + direction[0]
		nj = j + direction[1]
		if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[0]):
			neighbors.append((ni, nj))
	return neighbors

def increment_neighbors(i, j):
	increment_neighbors = []
	for ni, nj in all_neighbors(i, j):
		if grid[ni][nj] == grid[i][j] + 1:
			increment_neighbors.append((ni, nj))
	return increment_neighbors

paths = {}

def find_paths(i, j):
	neighbors = increment_neighbors(i, j)
	while len(neighbors) > 0:
		ni, nj = neighbors.pop()
		if grid[ni][nj] == 9:
			if (i, j) in paths:
				paths[(i, j)].add((ni, nj))
			else:
				paths[(i, j)] = set([(ni, nj)])
		else:
			neighbors += increment_neighbors(ni, nj)

for i in range(len(grid)):
	for j in range(len(grid[0])):
		if grid[i][j] == 0:
			find_paths(i, j)

print(sum([len(path) for path in paths.values()]))