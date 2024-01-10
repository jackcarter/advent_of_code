import time
start_time = time.perf_counter()

with open("data.txt") as data:
	jets = data.read().splitlines()[0]

def print_grid():
	for y in range(max(max_heights) + 3, min(max_heights)-10, -1):
		print(''.join(['#' if (x, y) in fallen_block_spaces else '.' for x in range(container_width)]))

def block_below_max_height(block):
	return any([y <= max(max_heights) for x, y in block])

def block_resting(block):
	return any([(x, y - 1) in fallen_block_spaces for x, y in block])

def jet_blow(block, jet_index):
	jet_direction = (1, 0) if jet(jet_index) == '>' else (-1, 0)
	if any([x + jet_direction[0] == -1 or x + jet_direction[0] == container_width for x, y in block]):
		# block is at the edge of the container; leave it alone
		new_block = [(x, y) for x, y in block]
	elif any([(x + jet_direction[0], y) in fallen_block_spaces for x, y in block]):
		# block would collide with another block
		new_block = [(x, y) for x, y in block]
	else:	
		new_block = [(x + jet_direction[0], y) for x, y in block]
	return new_block

def fall(block):
	new_block = [(x, y - 1) for x, y in block]
	return new_block

def block_rests(block):
	global fallen_block_spaces
	global max_heights
	global offset
	fallen_block_spaces.extend(block)
	for x, y in block:
		if y > max_heights[x]:
			max_heights[x] = y
	fallen_block_spaces = [(x, y) for x, y in fallen_block_spaces if y >= min(max_heights) - 2]

	
def jet(jet_index):
	return jets[jet_index % len(jets)]

def drop_block(block_index, jet_index):
	block = blocks[block_index%len(blocks)]
	left = 2
	bottom = max(max_heights) + 4
	new_block = [(x + left, y + bottom) for x, y in block]
	while True:
		new_block = jet_blow(new_block, jet_index)

		jet_index += 1
		resting = block_resting(new_block)
		if resting:
			# block is sitting on top of another block
			break
		else:
			new_block = fall(new_block)
	block_rests(new_block)
	return jet_index

blocks = [[(0,0), (1,0), (2,0), (3,0)], 		# '####'
		  [(1,0), (0,1), (1,1), (2,1), (1,2)], 	# '.#.','###','.#.'
		  [(0,0), (1,0), (2,0), (2,1), (2,2)],	# '..#','..#','###'
		  [(0,0), (0,1), (0,2), (0,3)],			# '#','#','#','#'
		  [(0,0), (0,1), (1,0), (1,1)]]			# '##','##'

offset = 0
container_width = 7
fallen_block_spaces = [(x,-1) for x in range(container_width)]
max_heights = [-1]*container_width
blocks_to_drop = 2022
jet_index = 0
for i in range(blocks_to_drop):
	jet_index = drop_block(i, jet_index)

print(max(max_heights)+1)

print(time.perf_counter() - start_time) #4.2 seconds