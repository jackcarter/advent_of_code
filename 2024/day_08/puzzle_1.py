import math

with open("./data.txt") as data:
	lines = data.read().splitlines()

characters = {}

for row, line in enumerate(lines):
	for col, char in enumerate(line):
		if char == '.':
			continue
		if char not in characters:
			characters[char] = [(row, col)]
		else:
			characters[char].append((row, col))
antinodes = set()
for char, coords in characters.items():
	for i, (row, col) in enumerate(coords):
	  # calculate the distance between the two points
		for j in range(i+1, len(coords)):
			row2, col2 = coords[j]
			dx = row2 - row
			dy = col2 - col
			antinode1 = (row2 + dx, col2 + dy)
			antinode2 = (row - dx, col - dy)
			for antinode in [antinode1, antinode2]:
				if antinode[0] < 0 or antinode[0] >= len(lines) or antinode[1] < 0 or antinode[1] >= len(lines[0]):
					continue
				else:
					antinodes.add(antinode)
print(len(antinodes))