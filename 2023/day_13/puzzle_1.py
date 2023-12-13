with open("./data.txt") as data:
	lines = data.read().splitlines()

grids = [[]]
for line in lines:
	if line == "":
		grids.append([])
	else:
		grids[-1].append([c for c in line])

total = 0
for grid in grids:
	for ii in range(len(grid)-1):
		if grid[ii] == grid[ii+1]:
			for jj in range(min(ii, len(grid)-ii-2)):
				if grid[ii-jj-1] == grid[ii+jj+2]:
					continue
				else:
					break
			else:
				total += 100*(ii+1)
				break
	else:
		for cc in range(len(grid[0])-1):
			if all([grid[rr][cc] == grid[rr][cc+1] for rr in range(len(grid))]):
				for vv in range(min(cc, len(grid[0])-cc-2)):
					if all([grid[rr][cc-vv-1] == grid[rr][cc+vv+2] for rr in range(len(grid))]):
						continue
					else:
						break
				else:
					total += cc+1
					break
print(total)