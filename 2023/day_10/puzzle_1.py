import itertools
with open("./data.txt") as data:
	lines = data.read().splitlines()

grid = [[c for c in line] for line in lines]
grid = [['.'] + row + ['.'] for row in grid]
grid = [['.']*len(grid[0])] + grid + [['.']*len(grid[0])]

start_index = [(ii, jj) for jj in range(len(grid)) for ii in range(len(grid[jj])) if grid[ii][jj]=='S'][0]

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

def invert_relative_index(index):
	return (index[0]*-1,index[1]*-1)

def get_on_track(start_index):
	for r, c in [[-1,0],[0,-1],[0,1],[1,0]]:
		target = grid[start_index[0]+r][start_index[1]+c]
		if target in pipe_chars:
			f = (start_index[0]+r,start_index[1]+c)
			break
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
print(count//2)