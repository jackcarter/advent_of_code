import itertools
with open("./data.txt") as data:
	lines = data.read().splitlines()

grid = [[c for c in line] for line in lines]
grid = [['.'] + row + ['.'] for row in grid]
grid = [['.']*len(grid[0])] + grid + [['.']*len(grid[0])]

start_index = [(ii, jj) for ii in range(len(grid)) for jj in range(len(grid[ii])) if grid[ii][jj]=='S'][0]

def get_neighbors(index):
	neighbors = []
	for r, c in itertools.product([-1,0,1],[-1,0,1]):
		neighbors.append(grid[index[0]+r][index[1]+c])
	return neighbors

pipes = {
	'|': [(-1,0),(1,0)],
	'-': [(0,-1),(0,1)],
	'L': [(-1,0),(0,1)],
	'J': [(-1,0),(0,-1)],
	'7': [(0,-1),(1,0)],
	'F': [(0,1),(1,0)],
}
pipe_chars = [p[0] for p in pipes]

loop_tiles = [['.' for i in range(len(grid[0]))] for j in range(len(grid))]
inside_markers = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

def invert_relative_index(index):
	return (index[0]*-1,index[1]*-1)

def get_on_track(start_index):
	adjacent = []
	for r, c in [[-1,0],[0,-1],[0,1],[1,0]]:
		target = grid[start_index[0]+r][start_index[1]+c]
		if target in pipe_chars:
			if invert_relative_index((r,c)) in pipes[target]:
				f = (start_index[0]+r,start_index[1]+c)
				loop_tiles[current_index[0]][current_index[1]] = grid[current_index[0]][current_index[1]]
				adjacent.append((r,c))
	delta = set(adjacent)
	#figure out if S is a 7 or an L
	#7 and L don't count as an intersection when we calculate point-in-polygon with diagonal line going down/right
	for k,v in pipes.items():
		if delta == set(v):
			loop_tiles[start_index[0]][start_index[1]] = k
	return f

def get_next(current_index, prev_index):
	dirx, diry = (current_index[0]-prev_index[0],current_index[1]-prev_index[1])
	target = grid[current_index[0]][current_index[1]]
	if target in pipe_chars:
		if invert_relative_index((dirx,diry)) == pipes[target][0]:
			next_relative = pipes[target][1]
		elif invert_relative_index((dirx,diry)) == pipes[target][1]:
			next_relative = pipes[target][0]
		else:
			raise Exception("uh oh",target, current_index,(dirx,diry),invert_relative_index((dirx,diry)),pipes[target])
		f = (current_index[0]+next_relative[0],current_index[1]+next_relative[1])
		loop_tiles[current_index[0]][current_index[1]] = grid[current_index[0]][current_index[1]]
	return f

current_index = start_index

count = 0
next_index = get_on_track(current_index)

count += 1
while True:
	count+= 1
	current_index, next_index = next_index, get_next(next_index, current_index)
	if next_index == start_index:
		break

for r in range(len(loop_tiles)):
	for c in range(len(loop_tiles[0])):
		if loop_tiles[r][c] == '.':
			intersections = 0
			for ii in range(len(loop_tiles[0])-c+1):
				if r+ii > len(loop_tiles)-1:					
					break
				if c+ii > len(loop_tiles[0])-1:					
					break	
				target = loop_tiles[r+ii][c+ii]
				if target in ['F','|','-','J','S']:
					intersections += 1
			inside_markers[r][c] = intersections

print(len([i for j in inside_markers for i in j if i % 2 == 1]))