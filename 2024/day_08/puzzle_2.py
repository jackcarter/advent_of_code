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
			max_steps = (max(len(lines), len(lines[0])) + 1)
			for i in range(-max_steps, max_steps):
				potential_antinode = row + i*dx, col + i*dy
				if potential_antinode[0] < 0 or potential_antinode[0] >= len(lines) or potential_antinode[1] < 0 or potential_antinode[1] >= len(lines[0]):
					continue
				else:
					antinodes.add(potential_antinode)
print(len(antinodes))