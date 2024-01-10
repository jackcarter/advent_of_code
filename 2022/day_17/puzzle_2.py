from collections import OrderedDict
import time
import functools

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
	fallen_block_spaces.extend(block)
	for x, y in block:
		if y > max_heights[x]:
			max_heights[x] = y
	fallen_block_spaces = [(x, y) for x, y in fallen_block_spaces if y >= min(max_heights) - 2]

	
def jet(jet_index):
	return jets[jet_index % len(jets)]

def drop_block(block_index, jet_index):
	global states
	block = blocks[block_index%len(blocks)]
	state = (block_index%len(blocks), jet_index % len(jets), tuple([max_height - min(max_heights) for max_height in max_heights]))

	if state in states:
		block_cycle_len = block_index - states[state][0]
		height_cycle_diff = max(max_heights) - states[state][1]
		more, remain = (blocks_to_drop - block_index) // block_cycle_len, (blocks_to_drop - block_index) % block_cycle_len
		if remain == 0:
			answer = height_cycle_diff * more + max(max_heights) + 1
			print(answer)
			exit(0)
	


	states[state] = (block_index, max(max_heights))
	left = 2
	bottom = max(max_heights) + 4
	new_block = [(x + left, y + bottom) for x, y in block]
	while True:
		if new_block[0][1] < 0:
			#print_grid()
			input()
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

container_width = 7
fallen_block_spaces = [(x,-1) for x in range(container_width)]
max_heights = [-1]*container_width
blocks_to_drop = 1000000000000
jet_index = 0
adder = -1

states = OrderedDict()

for i in range(blocks_to_drop):
	jet_index = drop_block(i, jet_index)

print(max(max_heights)+1)