import math
import numpy as np
with open("data.txt") as data:
	lines = data.read().splitlines()

grid = []
for line in lines:
	grid.append([])
	for c in line:
		if c == 'S':
			grid[-1].append(0)	
		elif c == 'E':
			grid[-1].append(int(ord('z'))-97)
			start = (len(grid)-1, len(grid[-1])-1)
		else:
			grid[-1].append(int(ord(c)-97))

def get_valid_neighbors(current):
	dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	neighbors = []
	for r, c in dirs:
		nr, nc = (current[0] + r, current[1] + c)
		if nr < 0 or nr >= len(grid):
			continue
		if nc < 0 or nc >= len(grid[0]):
			continue
		if grid[nr][nc] < grid[current[0]][current[1]] - 1:
			continue
		else:
			neighbors.append((nr, nc))
	return neighbors

def print_path(path):
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			if (r, c) in path:
				print("{:03d}".format(path.index((r,c)))+',', end='')
			else:
				print('___,', end='')
		print()

def print_path2(path):
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			if (r, c) in path:
				print(str(grid[r][c])+'x', end='')
			else:
				print(str(grid[r][c])+'.', end='')
		print()

def recreate_path(parents, current):
	path = [current]
	while current in parents:
		current = parents[current]
		path.append(current)
	#print_path2(path)
	return path[::-1]

frontier = [start]
explored = set()
parents = {}

while len(frontier) > 0:
	current = frontier.pop(0)
	explored.add(current)
	if grid[current[0]][current[1]] == 0:
		print(len(recreate_path(parents, current))-1)
		break
	neighbors = get_valid_neighbors(current)
	for neighbor in neighbors:
		if neighbor not in frontier and neighbor not in explored:
			frontier.append(neighbor)
			parents[neighbor] = current