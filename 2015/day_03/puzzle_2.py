from collections import defaultdict

with open("data.txt") as data:
	lines = data.readlines()

houses = defaultdict(lambda: 0)

x, y = 0, 0
rx, ry = 0, 0
houses[(x,y)] += 1
houses[(rx,ry)] += 1

for ii, direction in enumerate(lines[0]):
	if ii % 2 == 0:
		if direction == '<':
			x -= 1
		elif direction == '>':
			x += 1
		elif direction == 'v':
			y -= 1
		elif direction == '^':
			y += 1
		houses[(x,y)] += 1
	else:
		if direction == '<':
			rx -= 1
		elif direction == '>':
			rx += 1
		elif direction == 'v':
			ry -= 1
		elif direction == '^':
			ry += 1
		houses[(rx,ry)] += 1

	

print(len(houses))

# Answer: 2360