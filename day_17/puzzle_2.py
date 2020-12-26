import itertools
from pprint import pprint
import numpy as np
from copy import deepcopy

def c2h(coord):
	return "$".join([str(c) for c in coord])

def h2c(hash):
	return list(map(int, hash.split("$")))

def get_cell_default(cells, coord):
	try:
		return cells[c2h(coord)]
	except KeyError:
		return '.'

def get_neighbor_coords(cells, coord):
	delta = [-1,0,1]
	return [(coord[0]+dw, coord[1]+dz, coord[2]+dy, coord[3]+dx) for dw in delta for dz in delta for dy in delta for dx in delta if dz!=0 or dy!=0 or dx!=0 or dw!=0]

def get_active_neighbors(cells, coord):
	neighbor_coords = get_neighbor_coords(cells, coord)
	neighbors = [get_cell_default(cells, new_coord) for new_coord in neighbor_coords]
	active_neighbor_count = neighbors.count("#")
	#print(c2h(coord), active_neighbor_count)
	return active_neighbor_count

def step(cells):
	#first, add a buffer around all active cells
	for cell in list(cells): #use list to create a static copy, avoiding runtimeerror (https://stackoverflow.com/questions/11941817)
		neighbors = get_neighbor_coords(cells, h2c(cell))
		for neighbor in neighbors:
			neighbor_hash = c2h(neighbor)
			if cells[cell] == '#' and neighbor_hash not in cells:
				cells[neighbor_hash] = '.'
	new_cells = deepcopy(cells)
	for cell in cells:
		active_neighbors = get_active_neighbors(cells, h2c(cell))
		if cells[cell]=='#':
			if active_neighbors not in [2, 3]:
				new_cells[cell] = '.'
			else:
				new_cells[cell] = '#'
		
		if cells[cell]=='.': 
			if active_neighbors == 3:
				new_cells[cell] = '#'
			else:
				new_cells[cell] = '.'
	return new_cells

def count_active(cells):
	return len([cells[c] for c in cells if cells[c]=='#'])

cells = {}

with open("data.txt") as data:
	lines = data.read().splitlines()
	for ii in range(len(lines)):
		for jj in range(len(lines[ii])):
			cells[c2h((0, 0, ii, jj))] = lines[ii][jj]

for ii in range(6):
	cells = step(cells)

print("Answer:",count_active(cells))

# Answer: 1624