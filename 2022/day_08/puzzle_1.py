import numpy as np
with open("data.txt") as data:
	lines = data.read().splitlines()

grid = []
for line in lines:
	grid.append([int(i) for i in line])

df = np.array(grid)

def check_visibility(df, turns, visibility):
	df = np.rot90(df, turns)
	visibility = np.rot90(visibility, turns)
	for r in range(len(df)):
		max = -1
		for c in range(len(grid[r])):
			if df[r,c] > max:
				max = df[r,c]
				visibility[r,c] = 1
	df = np.rot90(df, -turns)
	visibility = np.rot90(visibility, -turns)
	return visibility

visibility = np.zeros((len(df), len(df[0])))
for i in range(4):
	visibility = check_visibility(df, i, visibility)

print(int(sum(sum(visibility))))