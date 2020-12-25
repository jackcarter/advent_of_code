from functools import reduce
import operator
from pprint import pprint
import math

def print_tile(tile):
	print(tile['tileNum'])
	for line in tile['tile']:
		print ("".join(line))

def compare_edge(edge1, edge2):
	return edge1 == edge2

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

def compare_edges(tile1, tile2):
	e1 = get_edges(tile1)
	e2 = get_edges(tile2)
	pass

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
	#print(unused_tiles)
	matches = []
	for tilenum2, tile2 in unused_tiles.items():
		#print(tile2)
		match = compare_tiles(tile1['tile'], tile2['tile'])
		if match>0:
			matches.append(tilenum2)
	return matches

def single_edge_match(tile1edge, tile2):
	for t2p in get_permutations(tile2):
		e2 = get_edges(t2p)
		for edge2 in e2:
			print("edges",tile1edge, edge2)
			if tile1edge == edge2:
				return t2p
	return False

def get_oriented_match(tile1edge, unused_tiles):
	matches = []
	for tile2 in unused_tiles.values():
		#print(tile2['tileNum'])
		match = single_edge_match(tile1edge, tile2['tile'])
		if match:
			print("match", match)
			print_tile(tile1)
			print_tile(tile2)
			return tile2['tileNum'], t2p
	return False

def unused(tiles, jigsaw):
	used_tilenums = [j['tileNum'] for j in jigsaw]
	unused_tiles = {k: v for k, v in tiles.items() if k not in used_tilenums}
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
			tiles[tilenum] = {'tile': tile, 'orientationFixed':False, 'countMatches': 0, 'tileNum': tilenum}
			tile = []
		else:
			tile.append([l for l in line])
	return tiles

with open("data.txt") as data:
	lines = data.read().splitlines()

tiles = parse_tiles(lines)

corners = []
for tilenum1, tile1 in tiles.items():
	matches = get_matches(tile1, unused(tiles, [tiles[tilenum1]]))

	tiles[tilenum1]['countMatches']=len(matches)
	if len(matches) == 2:
		corners.append(tilenum1)
print("Corners:",corners)

corner_prod = reduce(operator.mul, corners, 1)

print("Answer:", corner_prod)

# Answer: 20913499394191

