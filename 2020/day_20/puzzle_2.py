import math

def get_edge(tile, edge):
	edges = {"top": tile[0],
	"bottom": tile[-1],
	"left": [t[0] for t in tile],
	"right": [t[-1] for t in tile]
	}
	return edges[edge]

def get_edges(tile):
	return get_edge(tile, "top"), get_edge(tile, "bottom"), get_edge(tile, "left"), get_edge(tile, "right")

def rotate_tile(tile):
	# https://stackoverflow.com/questions/5164642/python-print-a-generator-expression
	return list(zip(*tile[::-1]))

def flip_tile(tile):
	return [t[::-1] for t in tile]

def get_permutations(tile):
	functions_list = [lambda x: x,
	lambda x: rotate_tile(x),
	lambda x: rotate_tile(rotate_tile(x)),
	lambda x: rotate_tile(rotate_tile(rotate_tile(x))),
	lambda x: flip_tile(x),
	lambda x: flip_tile(rotate_tile(x)),
	lambda x: flip_tile(rotate_tile(rotate_tile(x))),
	lambda x: flip_tile(rotate_tile(rotate_tile(rotate_tile(x))))]

	return [f(tile) for f in functions_list]

def edge_match(tile1, tile2):
	e1 = get_edges(tile1)
	e2 = get_edges(tile2)
	for edge1 in e1:
		for edge2 in e2:
			if edge1 == edge2:
				return True
	return False

def compare_tiles(tile1, tile2):
	match_count = 0
	for ii, t2p in enumerate(get_permutations(tile2)):
		if edge_match(tile1, t2p):
			match_count+=1
	return match_count

def get_matches(tile1, unused_tiles):
	matches = []
	for tilenum2, tile2 in unused_tiles.items():
		match = compare_tiles(tile1['tile'], tile2['tile'])
		if match>0:
			matches.append(tilenum2)
	return matches

def single_edge_match(tile1edge, tile2):
	for t2p in get_permutations(tile2):
		e2 = get_edges(t2p)
		for edge2 in e2:
			if tile1edge == edge2:
				return t2p
	return False

def opposite(input_dir):
	dirs = {'left': 'right', 'right': 'left', 'top': 'bottom', 'bottom': 'top'}
	return dirs[input_dir]
	
def specific_edge_match(tile1edge, tile2, tile2edgedir):
	for t2p in get_permutations(tile2):
		tile2edge = get_edge(t2p, tile2edgedir)
		if tuple(tile1edge) == tuple(tile2edge):
			return t2p
	return False

def get_oriented_match(tile1, tile1edgedir, unused_tiles, log=False):
	if log: print(tile1)
	matches = []
	tile1edge = get_edge(tile1, tile1edgedir)
	if log: print(tile1edge)
	for tile2 in unused_tiles.values():
		if log: print(tile2)
		match = specific_edge_match(tile1edge, tile2['tile'], opposite(tile1edgedir))
		if match:
			return tile2['tileNum'], match
	return False, False

def unused(tiles, jigsaw):
	tiles_in_jigsaw = [t[0] for line in jigsaw for t in line]
	unused_tiles = {tile: tiles[tile] for tile in tiles if tile not in tiles_in_jigsaw}
	return unused_tiles

def parse_tiles(lines):
	tiles = {}
	tile = []
	for ii, line in enumerate(lines):
		if line[:4]=="Tile":
			x, tilenum = line.split(" ")
			tilenum = int(tilenum[:-1])
			tiles[tilenum] = []
		elif line=="":
			tiles[tilenum] = {'tile': tile, 'tileNum': tilenum}
			tile = []
		else:
			tile.append([l for l in line])
	return tiles

def remove_border(tile):
	return [row[1:-1] for row in tile[1:-1]]

def get_big_image(jigsaw):
	jigsaw_dim = len(jigsaw[0])
	tile_dim = len(jigsaw[0][0][1])-2
	big_image = [['x']*tile_dim*jigsaw_dim for c in range(tile_dim*jigsaw_dim)]
	for ii, row in enumerate(jigsaw):
		for jj, jigsawtile in enumerate(row):
			borderless = remove_border(jigsawtile[1])
			#print("jj",jj)
			for ii2, row2 in enumerate(borderless):
				#print(row2)
				for jj2, col2 in enumerate(row2):
					big_image[ii*tile_dim+ii2][jj*tile_dim+jj2] = borderless[ii2][jj2]
	return big_image

def get_monster():
	return [
'                  # ',
'#    ##    ##    ###',
' #  #  #  #  #  #   '
 ]

def count_monster_hashes():
	return len([cell for row in get_monster() for cell in row if cell == "#"])

def get_monster_offsets():
	monster = get_monster()
	offsets = []
	for ii, row in enumerate(monster):
		for jj, col in enumerate(row):
			if monster[ii][jj] == "#":
				offsets.append((ii, jj))
	return offsets

def check_monster(big_image, row, col):
	monster_offsets = get_monster_offsets()
	big_image_shape = (len(big_image), len(big_image[0]))
	for offset in monster_offsets:
		search_x = row+offset[0]
		search_y = col+offset[1]
		if search_x > big_image_shape[0]-1 or search_y > big_image_shape[1]-1 or big_image[search_x][search_y] != "#":
			return False
	return True


def get_monsters(big_image):
	monsters = 0
	for row in range(len(big_image)):
		for col in range(len(big_image[0])):
			if check_monster(big_image, row, col):
				monsters += 1
	return monsters

def count_seas(big_image, monsters_count):
	return len([cell for row in big_image for cell in row if cell == "#"]) - count_monster_hashes()*monsters_count

with open("data.txt") as data:
	lines = data.read().splitlines()

tiles = parse_tiles(lines)

corners = []
for tilenum1, tile1 in tiles.items():
	matches = get_matches(tile1, {i:tiles[i] for i in tiles if i!=tilenum1})

	if len(matches) == 2:
		corners.append(tilenum1)

corner1 = corners[0]

jigsaw_dim = int(math.sqrt(len(tiles)))
jigsaw = [[] for x in range(jigsaw_dim)] # This represents the joined-up tiles, in order

latestnum = corner1
for orientation in get_permutations(tiles[corner1]['tile']):
	#Figure out which way to orient the first corner so that there's a match to the right and bottom
	match_num, oriented = get_oriented_match(orientation, 'right', {tile: tiles[tile] for tile in tiles if tile != corner1})
	match_num2, oriented2 = get_oriented_match(orientation, 'bottom', {tile: tiles[tile] for tile in tiles if tile != corner1})
	if match_num and match_num2:
		jigsaw[0].append((corner1, orientation))
		break

#Fill out the top row
for ii in range(jigsaw_dim-1):
	match_num, oriented = get_oriented_match(jigsaw[0][ii][1], 'right', unused(tiles, jigsaw))	
	jigsaw[0].append((match_num, oriented))

#Fill down each column
for col in range(jigsaw_dim):
	for row in range(1, jigsaw_dim):
		match_num, oriented = get_oriented_match(jigsaw[row-1][col][1], 'bottom', unused(tiles, jigsaw))
		jigsaw[row].append((match_num, oriented))
	
big_image = get_big_image(jigsaw)
for orientation in get_permutations(big_image):
	monsters_count = get_monsters(orientation)
	if monsters_count > 0:
		print("Answer:",count_seas(big_image, monsters_count))
		break

# Answer: 2209