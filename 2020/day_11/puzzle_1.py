import itertools
from pprint import pprint
import numpy as np

def get_neighbor_occupied_count(old_seats, row, col):
	neighbors = [old_seats[row-1][col-1],
	old_seats[row-1][col],
	old_seats[row-1][col+1],
	old_seats[row][col-1],
	old_seats[row][col+1],
	old_seats[row+1][col-1],
	old_seats[row+1][col],
	old_seats[row+1][col+1],
	]
	return neighbors.count('#')


def update_seats(old_seats):
	new_seats = np.copy(old_seats)
	for row in range(1,len(old_seats)-1):
		for col in range(1,len(old_seats[0])-1):
			if old_seats[row][col] == "L":
				if get_neighbor_occupied_count(old_seats, row, col) == 0:
					new_seats[row][col]="#"
				else:
					new_seats[row][col]=old_seats[row][col]
			elif old_seats[row][col] == "#":
				if get_neighbor_occupied_count(old_seats, row, col) >= 4:
					new_seats[row][col]="L"
				else:
					new_seats[row][col]=old_seats[row][col]
			else:
				new_seats[row][col]=old_seats[row][col]
	return new_seats

with open("data.txt") as data:
	lines = data.read().splitlines()
	lines = [['.']+[c for c in line]+['.'] for line in lines]
	seats = [['.']*len(lines[0])]
	seats.extend(lines)
	seats.extend([['.']*len(lines[0])])

old_seats = np.array(seats)

for ii in itertools.count(1):
	new_seats = update_seats(old_seats)
	if np.array_equal(old_seats, new_seats):
		print(new_seats)
		print("Answer:",np.count_nonzero(new_seats == "#"))
		break
	else:
		old_seats = new_seats.copy()

# Answer: 2277