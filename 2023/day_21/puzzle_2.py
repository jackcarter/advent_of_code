with open("data.txt") as data:
	lines = data.read().splitlines()

grid = []
for line in lines:
	grid.append([c for c in line])

def get_valid_neighbors(r, c):
	candidates = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
	in_bounds = [c for c in candidates if c[0] >= 0 and c[0] < len(grid) and c[1] >= 0 and c[1] < len(grid[0])]
	return set([c for c in in_bounds if grid[c[0]][c[1]] != '#'])

for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == 'S':
			start = (i, j)
			break

def iterate(start, iterations):
	current = set([start])
	total = []
	for i in range(iterations, 0, -1):
		total.append(len(current))
		next = set()
		for i in current:
			for n in get_valid_neighbors(i[0], i[1]):
				next.add(n)
		current = next
	return len(current)

		
def count_total(iterations, side_length=None):
	if side_length is None:
		side_length = len(grid[0])
	if len(grid[0]) != len(grid):
		raise Exception("Grid is not square")
	
	n = (iterations - side_length//2)//side_length
	odd_parity_tiles = (n + 1)**2
	even_parity_tiles = n**2
	odd_corners = (n + 1)
	even_corners = n


	full_oddcount = iterate(start, len(grid)+2)
	full_evencount = iterate(start, len(grid)+1)

	corner_oddcount = iterate(start, len(grid)+2) - iterate(start, side_length // 2 ) 
	corner_evencount =  iterate(start, len(grid)+1) - iterate(start, side_length // 2 - 1 ) 
	return full_oddcount*odd_parity_tiles + full_evencount*even_parity_tiles - corner_oddcount*odd_corners + (corner_evencount)*even_corners


answer = count_total(26501365)
print(answer)