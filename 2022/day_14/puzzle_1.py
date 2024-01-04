import itertools

with open("data.txt") as data:
	lines = data.read().splitlines()

rocks = set()
sand = set()
for line in lines:
	paths = line.split(' -> ')
	for i, _ in enumerate(paths[:-1]):
		x, y = [int(n) for n in paths[i].split(',')]
		x2, y2 = [int(n) for n in paths[i+1].split(',')]
		#connect x,y to x2,y2 and add to rocks
		if x == x2:
			for j in range(min(y, y2), max(y, y2)+1):
				rocks.add((x, j))
		elif y == y2:
			for j in range(min(x, x2), max(x, x2)+1):
				rocks.add((j, y))
		else:
			print("wtf")
			exit(0)
rocksand = rocks

def drop_sand(x=500, y=0):
	while True:
		if y > max([y for _, y in rocks]):
			return True
		elif (x, y+1) not in rocksand:
			y += 1
		elif (x-1, y+1) not in rocksand:
			x -= 1
			y += 1
		elif (x+1, y+1) not in rocksand:
			x += 1
			y += 1
		else:
			break
	sand.add((x, y))
	rocksand.add((x, y))
	return False

i = 0
while True:
	if drop_sand():
		break
	i += 1
print(i)
