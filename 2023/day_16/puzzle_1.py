with open("./data.txt") as data:
	lines = data.read().splitlines()

grid = []
for line in lines:
	grid.append([c for c in line])

def next(r, c, direction):
	if direction == "down":
		next = (r + 1, c)
	elif direction == "up":
		next = (r - 1, c)
	elif direction == "left":
		next = (r, c - 1)
	elif direction == "right":
		next = (r, c + 1)
	if next[0] < 0 or next[0] >= len(grid) or next[1] < 0 or next[1] >= len(grid[0]):
		return None, None, None
	return next[0], next[1], direction

def advance(beams):
	newbeams = []
	for beam in beams:
		newbeams.append(next(*beam))
	newbeams = [beam for beam in newbeams if beam[0] is not None]
	for beam in newbeams:
		energized[beam[0]][beam[1]] = '#'
	return newbeams

def action(r, c, direction):
	if grid[r][c] == ".":
		return [(r, c, direction)]
	elif grid[r][c] == "|":
		if direction in ['left', 'right']:
			return [(r, c, 'up'), (r, c, 'down')]
		else:
			return [(r, c, direction)]
	elif grid[r][c] == "-":
		if direction in ['up', 'down']:
			return [(r, c, 'left'), (r, c, 'right')]
		else:
			return [(r, c, direction)]
	elif grid[r][c] == "/":
		if direction == "up":
			return [(r, c, 'right')]
		elif direction == "down":
			return [(r, c, 'left')]
		elif direction == "left":
			return [(r, c, 'down')]
		elif direction == "right":
			return [(r, c, 'up')]
	elif grid[r][c] == '\\':
		if direction == "up":
			return [(r, c, 'left')]
		elif direction == "down":
			return [(r, c, 'right')]
		elif direction == "left":
			return [(r, c, 'up')]
		elif direction == "right":
			return [(r, c, 'down')]

energized = []
for line in grid:
	energized.append(['.' for c in line])
r, c, direction = (0, -1, "right")
beams = action(r, c, direction)
print(beams)
beams = [(r, c, direction)]
print(beams)
exit(0)
ii = 0
past_beams = []
while len(beams) > 0:
	ii += 1
	beams = advance(beams)
	newbeams = []
	for beam in beams:
		newbeams.extend(action(*beam))
	beams = set(newbeams)
	beams = list(beams)
	newbeams2 = []
	for beam in beams:
		if beam in past_beams:
			pass
		else:
			newbeams2.append(beam)
	beams = newbeams2
	past_beams.extend(beams)

print(sum([sum([1 for c in line if c == '#']) for line in energized]))