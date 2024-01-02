import numpy as np
with open("data.txt") as data:
	lines = data.read().splitlines()

grid = []
for line in lines:
	grid.append([int(i) for i in line])

def score(r, c):
	height = grid[r][c]
	score = 1
	for dir in [(-1,0), (0,-1), (1,0), (0,1)]:
		steps = 0
		while True:
			steps += 1
			nr, nc = r + steps*dir[0], c + steps*dir[1]
			if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[r]):
				steps -= 1
				break
			if grid[nr][nc] >= height:
				break
		score *= steps
	return score

print(max([score(r, c) for r in range(len(grid)) for c in range(len(grid[r]))]))