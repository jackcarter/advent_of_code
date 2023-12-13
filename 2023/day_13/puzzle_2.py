from copy import deepcopy
with open("./data.txt") as data:
	lines = data.read().splitlines()

grids = [[]]
for line in lines:
	if line == "":
		grids.append([])
	else:
		grids[-1].append([c for c in line])

def find_reflection(grid, ignorerc=None, ignoren=None):
	for ii in range(len(grid)-1):
		if grid[ii] == grid[ii+1]:
			for jj in range(min(ii, len(grid)-ii-2)):
				if grid[ii-jj-1] == grid[ii+jj+2]:
					continue
				else:
					break
			else:
				if ignorerc == 'r' and ignoren == ii:
					continue
				return ("r", ii)
	else:
		for cc in range(len(grid[0])-1):
			if all([grid[rr][cc] == grid[rr][cc+1] for rr in range(len(grid))]):
				for vv in range(min(cc, len(grid[0])-cc-2)):
					if all([grid[rr][cc-vv-1] == grid[rr][cc+vv+2] for rr in range(len(grid))]):
						continue
					else:
						break
				else:
					if ignorerc == 'c' and ignoren == cc:
						continue
					return ("c", cc)
	return None, None

def find_smudge(grid):
	originalrc, originaln = find_reflection(grid)
	for rr in range(len(grid)):
		for cc in range(len(grid[rr])):
			if originalrc == 'c' and cc == originaln:
				continue
			newgrid = deepcopy(grid)
			if grid[rr][cc] == "#":
				newgrid[rr][cc] = "."
			else:
				newgrid[rr][cc] = "#"
			rc, n = find_reflection(newgrid, originalrc, originaln)
			if rc is not None:
				if rc != originalrc or n != originaln:
					if rc == "r":
						return 100*(n+1)
					else:
						return n+1
				
total = 0
for grid in grids:
	total += find_smudge(grid)
	
print(total)