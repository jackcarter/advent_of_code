with open("data.txt") as data:
	lines = data.read().splitlines()

shapescores = {'A': 1, 'B': 2, 'C': 3, 1: 1, 2: 2, 0: 3, }

def convert(op, xyz):
	if xyz == 'Y':
		return op, op
	elif xyz == 'Z':
		return op, (shapescores[op] + 1) % 3
	else:
		return op, (shapescores[op] - 1) % 3

def score(op, me):
	op, me = convert(op, me)
	shapescore = shapescores[me]
	winner = (shapescores[me] - shapescores[op] + 1) % 3
	return shapescore + winner*3

print(sum([score(*line.split(' ')) for line in lines]))