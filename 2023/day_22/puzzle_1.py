from collections import OrderedDict
with open("data.txt") as data:
	lines = data.read().splitlines()

grid = []
for line in lines:
	grid.append([c for c in line])

maxxyz = [0,0,0]
bricks = []
for ii, line in enumerate(lines):
	a, b = line.split('~')
	x1, y1, z1 = [int(i) for i in a.split(',')]
	x2, y2, z2 = [int(i) for i in b.split(',')]
	if x1 > maxxyz[0]:
		maxxyz[0] = x1
	if y1 > maxxyz[1]:
		maxxyz[1] = y1
	if z1 > maxxyz[2]:
		maxxyz[2] = z1
	if x2 > maxxyz[0]:
		maxxyz[0] = x2
	if y2 > maxxyz[1]:
		maxxyz[1] = y2
	if z2 > maxxyz[2]:
		maxxyz[2] = z2
	bricks.append(((x1, y1, z1), (x2, y2, z2)))

def get_tiles(brick):
	(x1, y1, z1) = brick[0]
	(x2, y2, z2) = brick[1]
	if x1 < x2:
		return [(x, y1, z1) for x in range(x1, x2 + 1)]
	elif y1 < y2:
		return [(x1, y, z1) for y in range(y1, y2 + 1)]
	elif z1 < z2:
		return [(x1, y1, z) for z in range(z1, z2 + 1)]
	else:
		return [(x1, y1, z1)]

def conflict(brick, occupied):
	for tile in get_tiles(brick):
		if tile in occupied.keys():
			return True
	return False

def supporting_bricks(brick, occupied):
	sb = set()
	brick_tiles = get_tiles(brick)
	for (x, y, z) in brick_tiles:
		if (x, y, z-1) in brick_tiles:
			continue
		if (x, y, z-1) in occupied.keys():
			sb.add(occupied[(x, y, z-1)])
	return sb


occupied = {}	
sortedbricks = sorted(bricks,key=lambda x: min(x[0][2], x[1][2]))
fallenbricks = []
for brick in sortedbricks:
	(x1, y1, z1) = brick[0]
	(x2, y2, z2) = brick[1]
	while not conflict(((x1, y1, z1-1), (x2, y2, z2-1)), occupied) and z1 > 0 and z2 > 0:
		z1 -= 1
		z2 -= 1
	
	fallenbricks.append(((x1, y1, z1), (x2, y2, z2)))

	for tile in get_tiles(((x1, y1, z1), (x2, y2, z2))):
		occupied[tile] = len(fallenbricks) - 1
	
sortedfallenbricks = sorted(fallenbricks,key=lambda x: min(x[0][2], x[1][2]))

nondisintegrable_bricks = set()
for brick in sortedfallenbricks:
	# check each square below brick and figure out which brick it belongs to, if any
	(x1, y1, z1) = brick[0]
	(x2, y2, z2) = brick[1]
	# check if brick is on the ground
	if z1 == 0 or z2 == 0:
		continue
	supports = supporting_bricks(brick, occupied)
	if len(supports) == 0:
		exit("shouldn't be here")
	elif len(supports) == 1:
		#print(supports)
		nondisintegrable_bricks.add(next(iter(supports)))
	else:
		continue

print(len(sortedfallenbricks)-len(nondisintegrable_bricks))