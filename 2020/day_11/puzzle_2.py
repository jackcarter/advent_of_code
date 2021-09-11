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

def get_first_visible_occupied_count(old_seats, row, col):
	nearest_neighbors = []
	nearest_neighbor_coords = []
	for row_delt in [-1, 0, 1]:
		for col_delt in [-1, 0, 1]:
			if row_delt == 0 and col_delt == 0:
				#don't care about this case; we'll never get anywhere
				continue
			examine_seat_row = row
			examine_seat_col = col
			while(True):
				examine_seat_row = examine_seat_row+row_delt
				examine_seat_col = examine_seat_col+col_delt
				if len(old_seats)-1 < examine_seat_row or 0 > examine_seat_row or len(old_seats[0])-1 < examine_seat_col or 0 > examine_seat_col:
					break
				examine_seat = old_seats[examine_seat_row][examine_seat_col]
				if examine_seat != '.':
					nearest_neighbors.append(examine_seat)
					nearest_neighbor_coords.append([examine_seat_row, examine_seat_col])
					break
	#print(row, col, nearest_neighbors, nearest_neighbor_coords)
	return nearest_neighbors.count("#")



def update_seats(old_seats):
	new_seats = np.copy(old_seats)
	for row in range(len(old_seats)):
		for col in range(len(old_seats[0])):
			if old_seats[row][col] == "L":
				if get_first_visible_occupied_count(old_seats, row, col) == 0:
					new_seats[row][col]="#"
				else:
					new_seats[row][col]=old_seats[row][col]
			elif old_seats[row][col] == "#":
				if get_first_visible_occupied_count(old_seats, row, col) >= 5:
					new_seats[row][col]="L"
				else:
					new_seats[row][col]=old_seats[row][col]
			else:
				new_seats[row][col]=old_seats[row][col]
	return new_seats

with open("data.txt") as data:
	lines = data.read().splitlines()
	seats = [[c for c in line] for line in lines]

old_seats = np.array(seats)
print(old_seats)
for ii in itertools.count(1):
	new_seats = update_seats(old_seats)
	if np.array_equal(old_seats, new_seats):
		print("Answer:",np.count_nonzero(new_seats == "#"))
		break
	else:
		old_seats = new_seats.copy()

# Answer: 2066