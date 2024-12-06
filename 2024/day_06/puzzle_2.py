with open("./data.txt") as data:
	lines = data.read().splitlines()
lines_copy = [line for line in lines]
# empty array size of lines grid
guard_positions = set()

def turn_guard_right(guard):
	directions = ['^', '>', 'v', '<']
	return (guard[0], guard[1], directions[(directions.index(guard[2]) + 1) % 4])

direction = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
def move_guard_to_obstruction(guard):
	next_position = (guard[0] + direction[guard[2]][0], guard[1] + direction[guard[2]][1])
	while next_position[0] >= 0 and next_position[0] < len(lines) and next_position[1] >= 0 and next_position[1] < len(lines[0]) and lines[next_position[0]][next_position[1]] in ('.', '^'):
		guard = (next_position[0], next_position[1], guard[2])
		guard_positions.add(guard)
		next_position = (guard[0] + direction[guard[2]][0], guard[1] + direction[guard[2]][1])
	if next_position[0] < 0 or next_position[0] >= len(lines) or next_position[1] < 0 or next_position[1] >= len(lines[0]):
		return False # out of bounds
	if lines[next_position[0]][next_position[1]] == '#':
		return turn_guard_right(guard) # found obstruction

for i, line in enumerate(lines):
	if '^' in line:
		guard = (i, line.index('^'), '^')

original_guard_position = guard

while True:
	guard = move_guard_to_obstruction(guard)
	if guard:
		continue
	else:
		break

def check_loop(guard):
	guard = move_guard_to_obstruction(guard)
	guard_positions.add(guard)
	while guard:
		guard = move_guard_to_obstruction(guard)
		if guard:
			if guard in guard_positions: # guard has been here before in this direction, so we have a loop
				return True
			else:
				guard_positions.add(guard)
		else:
			break
	return False

loop_count = 0
# for each position in the grid, add new obstruction and check if guard loops
for i in range(len(lines)):
	for j in range(len(lines[0])):
		if lines[i][j] == '.':
			lines = [line for line in lines_copy]
			lines[i] = lines[i][:j] + '#' + lines[i][j + 1:]
			guard = original_guard_position
			guard_positions = set()
			if check_loop(guard):
				loop_count += 1
	print(i, '/', len(lines))

print(loop_count)