with open("./data.txt") as data:
	lines = data.read().splitlines()

# empty array size of lines grid
guard_positions = [[lines[i][j] for j in range(len(lines[0]))] for i in range(len(lines))]

def turn_guard_right(guard):
	directions = ['^', '>', 'v', '<']
	return (guard[0], guard[1], directions[(directions.index(guard[2]) + 1) % 4])

def move_guard_to_obstruction(guard):
	direction = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
	next_position = (guard[0] + direction[guard[2]][0], guard[1] + direction[guard[2]][1])
	while next_position[0] >= 0 and next_position[0] < len(lines) and next_position[1] >= 0 and next_position[1] < len(lines[0]) and lines[next_position[0]][next_position[1]] in ('.', '^'):
		guard = (next_position[0], next_position[1], guard[2])
		guard_positions[guard[0]][guard[1]] = guard[2]
		next_position = (guard[0] + direction[guard[2]][0], guard[1] + direction[guard[2]][1])
	if next_position[0] < 0 or next_position[0] >= len(lines) or next_position[1] < 0 or next_position[1] >= len(lines[0]):
		return False # out of bounds
	if lines[next_position[0]][next_position[1]] == '#':
		return turn_guard_right(guard) # found obstruction
	

for i, line in enumerate(lines):
	if '^' in line:
		guard = (i, line.index('^'), '^')

while True:
	guard = move_guard_to_obstruction(guard)
	if guard:
		continue
	else:
		break

distinct_positions = 0
for line in guard_positions:
	#print(''.join(line))
	distinct_positions += line.count('^') + line.count('v') + line.count('<') + line.count('>')
print(distinct_positions)
