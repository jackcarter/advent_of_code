import re
with open("./data.txt") as data:
	lines = data.read().splitlines()

instructions = []
for line in lines:
	hex = line.split(' ')[2][2:-1]
	dir = int(hex[-1])
	dist = int(hex[:-1], 16)
	instructions.append((dir, dist))

start = (sum([i[1] for i in instructions]) // 2, sum([i[1] for i in instructions]) // 2)

dirmap = {3: (0, -1), 1: (0, 1), 2: (-1, 0), 0: (1, 0)}

corners = [start]
perimeter = 0
for dir, dist in instructions:
	next = start[0] + dirmap[dir][0] * dist, start[1] + dirmap[dir][1] * dist
	corners.append(next)
	perimeter += abs(next[0] - start[0]) + abs(next[1] - start[1])
	start = next

def shoelace_algorithm(corners):
	s = 0
	for i in range(len(corners)-1):
		s += corners[i][0] * corners[i+1][1] - corners[i+1][0] * corners[i][1]
	s += corners[-1][0] * corners[0][1] - corners[0][0] * corners[-1][1]
	return s // 2

def total_area(corners, grid):
	return shoelace_algorithm(corners) + perimeter//2 + 1

print(total_area(corners, perimeter))