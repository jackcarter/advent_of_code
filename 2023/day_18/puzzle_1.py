import re
with open("./data.txt") as data:
	lines = data.read().splitlines()

instructions = []
for line in lines:
	s = line.split(' ')
	instructions.append((s[0], int(s[1])))

grid = []
for i in range(sum([i[1] for i in instructions])):
	grid.append(['.' for i in range(sum([i[1] for i in instructions]))])

start = (len(grid) // 2, len(grid) // 2)

dirmap = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

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