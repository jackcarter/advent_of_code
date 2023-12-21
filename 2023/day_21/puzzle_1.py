with open("data.txt") as data:
	lines = data.read().splitlines()

grid = []
for line in lines:
	grid.append([c for c in line])
	if 'S' in line:
		start = tuple((len(grid) - 1, line.index('S')))

def get_valid_neighbors(r, c):
	candidates = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
	in_bounds = [c for c in candidates if c[0] >= 0 and c[0] < len(grid) and c[1] >= 0 and c[1] < len(grid[0])]
	return set([c for c in in_bounds if grid[c[0]][c[1]] != '#'])

current = set([start])
for i in range(64, 0, -1):
	next = set()
	for i in current:
		for n in get_valid_neighbors(i[0], i[1]):
			next.add(n)
	current = next
print(len(current))