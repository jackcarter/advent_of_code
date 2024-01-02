import numpy as np
with open("data.txt") as data:
	lines = data.read().splitlines()

def move(head, tail):
	if head[0] == tail[0] + 2:
		if head[1] == tail[1] + 2:
			tail = tail[0] + 1, tail[1] + 1
		elif head[1] == tail[1] - 2:
			tail = tail[0] + 1, tail[1] - 1
		else:
			tail = tail[0] + 1, head[1]
	elif head[0] == tail[0] - 2:
		if head[1] == tail[1] + 2:
			tail = tail[0] - 1, tail[1] + 1
		elif head[1] == tail[1] - 2:
			tail = tail[0] - 1, tail[1] - 1
		else:
			tail = tail[0] - 1, head[1]
	elif head[1] == tail[1] + 2:
		tail = head[0], tail[1] + 1
	elif head[1] == tail[1] - 2:
		tail = head[0], tail[1] - 1
	return tail

def printgrid(rope):
	for r in range(-10, 10):
		for c in range(-10, 20):
			if (r, c) in rope:
				print(rope.index((r,c)), end='')
			else:
				print('.', end='')
		print()


dirs = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

rope = [(0,0) for _ in range(10)]


touched = set()

for line in lines:
	dirtxt, dist = line[0], int(line[2:])
	dir = dirs[dirtxt]
	for i in range(dist):
		rope[0] = rope[0][0] + dir[0], rope[0][1] + dir[1]
		for i in range(0, len(rope)-1):
			rope[i+1] = move(rope[i], rope[i+1])
		touched.add(rope[-1])

print(len(touched))
		